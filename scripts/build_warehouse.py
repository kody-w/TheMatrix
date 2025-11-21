#!/usr/bin/env python3
"""
The Matrix Data Warehouse Builder

Extracts metadata from The Matrix repository and builds a queryable SQLite database.
Inspired by Simon Willison's data extraction patterns.

Usage:
    python scripts/build_warehouse.py [--db matrix.db] [--verbose]
"""

import argparse
import json
import os
import re
import sqlite3
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, List, Optional
import subprocess
import hashlib


class MatrixWarehouse:
    """Builds a data warehouse from The Matrix repository."""

    def __init__(self, db_path: str = "matrix.db", verbose: bool = False):
        self.db_path = db_path
        self.verbose = verbose
        self.repo_root = Path(__file__).parent.parent
        self.conn = sqlite3.connect(db_path)
        self.conn.row_factory = sqlite3.Row
        self.timestamp = datetime.utcnow().isoformat()

    def log(self, message: str):
        """Log message if verbose mode enabled."""
        if self.verbose:
            print(f"[{datetime.now().strftime('%H:%M:%S')}] {message}")

    def init_schema(self):
        """Initialize database schema."""
        self.log("Initializing database schema...")

        cursor = self.conn.cursor()

        # Repository snapshots table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS repo_snapshots (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp TEXT NOT NULL,
                commit_hash TEXT,
                branch TEXT,
                file_count INTEGER,
                total_lines INTEGER,
                agent_count INTEGER,
                workflow_count INTEGER
            )
        """)

        # Files table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS files (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                snapshot_id INTEGER,
                path TEXT NOT NULL,
                file_type TEXT,
                size_bytes INTEGER,
                line_count INTEGER,
                hash TEXT,
                created_at TEXT,
                modified_at TEXT,
                FOREIGN KEY (snapshot_id) REFERENCES repo_snapshots (id)
            )
        """)

        # Agents table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS agents (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                snapshot_id INTEGER,
                name TEXT NOT NULL,
                file_path TEXT,
                description TEXT,
                model TEXT,
                tools TEXT,
                FOREIGN KEY (snapshot_id) REFERENCES repo_snapshots (id)
            )
        """)

        # Workflows table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS workflows (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                snapshot_id INTEGER,
                name TEXT NOT NULL,
                file_path TEXT,
                description TEXT,
                triggers TEXT,
                jobs TEXT,
                FOREIGN KEY (snapshot_id) REFERENCES repo_snapshots (id)
            )
        """)

        # Markdown documents table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS documents (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                snapshot_id INTEGER,
                path TEXT NOT NULL,
                title TEXT,
                word_count INTEGER,
                heading_count INTEGER,
                code_block_count INTEGER,
                link_count INTEGER,
                FOREIGN KEY (snapshot_id) REFERENCES repo_snapshots (id)
            )
        """)

        # Agent changelog entries
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS agent_changelog (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                snapshot_id INTEGER,
                phase_number INTEGER,
                phase_name TEXT,
                date TEXT,
                agent_type TEXT,
                task TEXT,
                duration TEXT,
                success_rate TEXT,
                impact TEXT,
                FOREIGN KEY (snapshot_id) REFERENCES repo_snapshots (id)
            )
        """)

        # Knowledge base entries
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS knowledge_base (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                snapshot_id INTEGER,
                category TEXT,
                file_path TEXT,
                title TEXT,
                content_preview TEXT,
                FOREIGN KEY (snapshot_id) REFERENCES repo_snapshots (id)
            )
        """)

        # Create indexes
        cursor.execute("CREATE INDEX IF NOT EXISTS idx_files_path ON files(path)")
        cursor.execute("CREATE INDEX IF NOT EXISTS idx_files_type ON files(file_type)")
        cursor.execute("CREATE INDEX IF NOT EXISTS idx_agents_name ON agents(name)")
        cursor.execute("CREATE INDEX IF NOT EXISTS idx_documents_path ON documents(path)")

        self.conn.commit()
        self.log("Schema initialized successfully")

    def get_git_info(self) -> Dict[str, Optional[str]]:
        """Get current git commit and branch."""
        try:
            commit = subprocess.check_output(
                ["git", "rev-parse", "HEAD"],
                cwd=self.repo_root,
                text=True
            ).strip()

            branch = subprocess.check_output(
                ["git", "rev-parse", "--abbrev-ref", "HEAD"],
                cwd=self.repo_root,
                text=True
            ).strip()

            return {"commit": commit, "branch": branch}
        except subprocess.CalledProcessError:
            return {"commit": None, "branch": None}

    def get_file_stats(self, file_path: Path) -> Dict[str, Any]:
        """Get statistics for a file."""
        stat = file_path.stat()

        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
                line_count = len(content.splitlines())
                file_hash = hashlib.sha256(content.encode()).hexdigest()[:16]
        except (UnicodeDecodeError, PermissionError):
            line_count = 0
            file_hash = None

        return {
            "size_bytes": stat.st_size,
            "line_count": line_count,
            "hash": file_hash,
            "modified_at": datetime.fromtimestamp(stat.st_mtime).isoformat()
        }

    def extract_markdown_metadata(self, file_path: Path) -> Dict[str, Any]:
        """Extract metadata from markdown files."""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()

            # Extract title (first h1 heading)
            title_match = re.search(r'^#\s+(.+)$', content, re.MULTILINE)
            title = title_match.group(1) if title_match else file_path.stem

            word_count = len(re.findall(r'\w+', content))
            heading_count = len(re.findall(r'^#{1,6}\s+', content, re.MULTILINE))
            code_block_count = len(re.findall(r'```', content)) // 2
            link_count = len(re.findall(r'\[.+?\]\(.+?\)', content))

            return {
                "title": title,
                "word_count": word_count,
                "heading_count": heading_count,
                "code_block_count": code_block_count,
                "link_count": link_count
            }
        except Exception as e:
            self.log(f"Error extracting metadata from {file_path}: {e}")
            return {}

    def extract_agent_metadata(self, file_path: Path) -> Dict[str, Any]:
        """Extract metadata from agent definition files."""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()

            # Extract YAML frontmatter
            frontmatter_match = re.search(r'^---\n(.*?)\n---', content, re.DOTALL)
            if not frontmatter_match:
                return {}

            frontmatter = frontmatter_match.group(1)

            # Parse key fields
            name = file_path.stem
            description_match = re.search(r'description:\s*(.+)', frontmatter)
            model_match = re.search(r'model:\s*(.+)', frontmatter)
            tools_match = re.search(r'tools:\s*(.+)', frontmatter)

            return {
                "name": name,
                "description": description_match.group(1) if description_match else None,
                "model": model_match.group(1) if model_match else None,
                "tools": tools_match.group(1) if tools_match else None
            }
        except Exception as e:
            self.log(f"Error extracting agent metadata from {file_path}: {e}")
            return {}

    def extract_workflow_metadata(self, file_path: Path) -> Dict[str, Any]:
        """Extract metadata from GitHub workflow files."""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()

            name_match = re.search(r'name:\s*["\']?(.+?)["\']?\s*$', content, re.MULTILINE)

            # Extract triggers
            triggers = []
            if 'on:' in content or 'on :' in content:
                trigger_section = re.search(r'on:\s*(.*?)(?=\n\w|\Z)', content, re.DOTALL)
                if trigger_section:
                    triggers = re.findall(r'(\w+):', trigger_section.group(1))

            # Extract job names
            jobs = []
            jobs_match = re.search(r'jobs:(.*?)(?=\n\w|\Z)', content, re.DOTALL)
            if jobs_match:
                jobs = re.findall(r'(\w+):', jobs_match.group(1))

            return {
                "name": name_match.group(1) if name_match else file_path.stem,
                "triggers": json.dumps(triggers),
                "jobs": json.dumps(jobs)
            }
        except Exception as e:
            self.log(f"Error extracting workflow metadata from {file_path}: {e}")
            return {}

    def scan_repository(self, snapshot_id: int):
        """Scan repository and extract all metadata."""
        self.log("Scanning repository files...")

        cursor = self.conn.cursor()

        # Track statistics
        file_count = 0
        total_lines = 0

        # Scan all files
        for root, dirs, files in os.walk(self.repo_root):
            # Skip common ignore patterns but keep .claude and .github
            dirs[:] = [d for d in dirs if (
                d in ['.claude', '.github'] or
                (not d.startswith('.') and d not in ['node_modules', '__pycache__', 'venv'])
            )]

            for filename in files:
                if filename.startswith('.'):
                    continue

                file_path = Path(root) / filename
                rel_path = file_path.relative_to(self.repo_root)

                file_type = file_path.suffix.lstrip('.') or 'unknown'
                stats = self.get_file_stats(file_path)

                cursor.execute("""
                    INSERT INTO files (snapshot_id, path, file_type, size_bytes, line_count, hash, modified_at)
                    VALUES (?, ?, ?, ?, ?, ?, ?)
                """, (
                    snapshot_id,
                    str(rel_path),
                    file_type,
                    stats['size_bytes'],
                    stats['line_count'],
                    stats['hash'],
                    stats['modified_at']
                ))

                file_count += 1
                total_lines += stats['line_count']

                # Extract type-specific metadata
                if file_type == 'md':
                    md_meta = self.extract_markdown_metadata(file_path)
                    if md_meta:
                        cursor.execute("""
                            INSERT INTO documents (snapshot_id, path, title, word_count, heading_count, code_block_count, link_count)
                            VALUES (?, ?, ?, ?, ?, ?, ?)
                        """, (
                            snapshot_id,
                            str(rel_path),
                            md_meta.get('title'),
                            md_meta.get('word_count'),
                            md_meta.get('heading_count'),
                            md_meta.get('code_block_count'),
                            md_meta.get('link_count')
                        ))

                # Extract agent definitions
                if '.claude/agents' in str(rel_path) and file_type == 'md':
                    agent_meta = self.extract_agent_metadata(file_path)
                    if agent_meta:
                        cursor.execute("""
                            INSERT INTO agents (snapshot_id, name, file_path, description, model, tools)
                            VALUES (?, ?, ?, ?, ?, ?)
                        """, (
                            snapshot_id,
                            agent_meta.get('name'),
                            str(rel_path),
                            agent_meta.get('description'),
                            agent_meta.get('model'),
                            agent_meta.get('tools')
                        ))

                # Extract workflow definitions
                if '.github/workflows' in str(rel_path) and file_type in ('yml', 'yaml'):
                    workflow_meta = self.extract_workflow_metadata(file_path)
                    if workflow_meta:
                        cursor.execute("""
                            INSERT INTO workflows (snapshot_id, name, file_path, triggers, jobs)
                            VALUES (?, ?, ?, ?, ?)
                        """, (
                            snapshot_id,
                            workflow_meta.get('name'),
                            str(rel_path),
                            workflow_meta.get('triggers'),
                            workflow_meta.get('jobs')
                        ))

                # Extract knowledge base entries
                if '.knowledge-bases' in str(rel_path) and file_type == 'md':
                    try:
                        with open(file_path, 'r', encoding='utf-8') as f:
                            content = f.read()

                        category = Path(rel_path).parent.name
                        title = re.search(r'^#\s+(.+)$', content, re.MULTILINE)
                        preview = content[:500] if len(content) > 500 else content

                        cursor.execute("""
                            INSERT INTO knowledge_base (snapshot_id, category, file_path, title, content_preview)
                            VALUES (?, ?, ?, ?, ?)
                        """, (
                            snapshot_id,
                            category,
                            str(rel_path),
                            title.group(1) if title else file_path.stem,
                            preview
                        ))
                    except Exception as e:
                        self.log(f"Error extracting knowledge base entry from {file_path}: {e}")

        self.conn.commit()
        self.log(f"Scanned {file_count} files with {total_lines:,} total lines")

        return file_count, total_lines

    def extract_agent_changelog(self, snapshot_id: int):
        """Extract entries from AGENT_CHANGELOG.md if it exists."""
        changelog_path = self.repo_root / "AGENT_CHANGELOG.md"
        if not changelog_path.exists():
            return

        self.log("Extracting agent changelog entries...")

        try:
            with open(changelog_path, 'r', encoding='utf-8') as f:
                content = f.read()

            cursor = self.conn.cursor()

            # Parse phases
            phases = re.findall(
                r'###\s+Phase\s+(\d+):\s+(.+?)\s+\((.+?)\)(.*?)(?=###\s+Phase|\Z)',
                content,
                re.DOTALL
            )

            for phase_num, phase_name, date, phase_content in phases:
                agent_type_match = re.search(r'\*\*Agent\*\*:\s*(.+)', phase_content)
                task_match = re.search(r'\*\*Task\*\*:\s*(.+)', phase_content)
                duration_match = re.search(r'\*\*Duration\*\*:\s*(.+)', phase_content)
                success_match = re.search(r'\*\*Success Rate\*\*:\s*(.+)', phase_content)
                impact_match = re.search(r'\*\*Impact\*\*:(.*?)(?=\*\*|\Z)', phase_content, re.DOTALL)

                cursor.execute("""
                    INSERT INTO agent_changelog (
                        snapshot_id, phase_number, phase_name, date, agent_type,
                        task, duration, success_rate, impact
                    )
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
                """, (
                    snapshot_id,
                    int(phase_num),
                    phase_name.strip(),
                    date.strip(),
                    agent_type_match.group(1).strip() if agent_type_match else None,
                    task_match.group(1).strip() if task_match else None,
                    duration_match.group(1).strip() if duration_match else None,
                    success_match.group(1).strip() if success_match else None,
                    impact_match.group(1).strip() if impact_match else None
                ))

            self.conn.commit()
            self.log(f"Extracted {len(phases)} changelog entries")
        except Exception as e:
            self.log(f"Error extracting changelog: {e}")

    def create_snapshot(self):
        """Create a new repository snapshot."""
        self.log("Creating repository snapshot...")

        git_info = self.get_git_info()

        cursor = self.conn.cursor()
        cursor.execute("""
            INSERT INTO repo_snapshots (timestamp, commit_hash, branch, file_count, total_lines, agent_count, workflow_count)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (
            self.timestamp,
            git_info.get('commit'),
            git_info.get('branch'),
            0,  # Will update after scan
            0,  # Will update after scan
            0,  # Will update after scan
            0   # Will update after scan
        ))

        snapshot_id = cursor.lastrowid
        self.conn.commit()

        self.log(f"Created snapshot #{snapshot_id}")
        return snapshot_id

    def update_snapshot_stats(self, snapshot_id: int):
        """Update snapshot statistics after scanning."""
        cursor = self.conn.cursor()

        # Count files
        cursor.execute("SELECT COUNT(*) FROM files WHERE snapshot_id = ?", (snapshot_id,))
        file_count = cursor.fetchone()[0]

        # Sum lines
        cursor.execute("SELECT SUM(line_count) FROM files WHERE snapshot_id = ?", (snapshot_id,))
        total_lines = cursor.fetchone()[0] or 0

        # Count agents
        cursor.execute("SELECT COUNT(*) FROM agents WHERE snapshot_id = ?", (snapshot_id,))
        agent_count = cursor.fetchone()[0]

        # Count workflows
        cursor.execute("SELECT COUNT(*) FROM workflows WHERE snapshot_id = ?", (snapshot_id,))
        workflow_count = cursor.fetchone()[0]

        cursor.execute("""
            UPDATE repo_snapshots
            SET file_count = ?, total_lines = ?, agent_count = ?, workflow_count = ?
            WHERE id = ?
        """, (file_count, total_lines, agent_count, workflow_count, snapshot_id))

        self.conn.commit()

        return {
            "file_count": file_count,
            "total_lines": total_lines,
            "agent_count": agent_count,
            "workflow_count": workflow_count
        }

    def build(self):
        """Build the complete data warehouse."""
        self.log("=" * 60)
        self.log("The Matrix Data Warehouse Builder")
        self.log("=" * 60)

        self.init_schema()
        snapshot_id = self.create_snapshot()

        self.scan_repository(snapshot_id)
        self.extract_agent_changelog(snapshot_id)

        stats = self.update_snapshot_stats(snapshot_id)

        self.log("=" * 60)
        self.log("Build Complete!")
        self.log(f"Database: {self.db_path}")
        self.log(f"Snapshot ID: {snapshot_id}")
        self.log(f"Files: {stats['file_count']:,}")
        self.log(f"Lines: {stats['total_lines']:,}")
        self.log(f"Agents: {stats['agent_count']}")
        self.log(f"Workflows: {stats['workflow_count']}")
        self.log("=" * 60)

    def close(self):
        """Close database connection."""
        self.conn.close()


def main():
    parser = argparse.ArgumentParser(
        description="Build The Matrix data warehouse",
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    parser.add_argument(
        "--db",
        default="matrix.db",
        help="Database file path (default: matrix.db)"
    )
    parser.add_argument(
        "-v", "--verbose",
        action="store_true",
        help="Enable verbose logging"
    )

    args = parser.parse_args()

    warehouse = MatrixWarehouse(db_path=args.db, verbose=args.verbose)
    try:
        warehouse.build()
    finally:
        warehouse.close()


if __name__ == "__main__":
    main()
