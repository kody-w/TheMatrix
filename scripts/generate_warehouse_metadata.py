#!/usr/bin/env python3
"""
Generate metadata about the Matrix data warehouse.

Creates a JSON file with statistics and schema information.
"""

import json
import sqlite3
from pathlib import Path
from datetime import datetime


def generate_metadata():
    """Generate warehouse metadata."""
    db_path = Path(__file__).parent.parent / "data" / "matrix.db"

    if not db_path.exists():
        print(f"Database not found: {db_path}")
        return

    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    metadata = {
        "generated_at": datetime.utcnow().isoformat(),
        "database": {
            "path": "data/matrix.db",
            "size_bytes": db_path.stat().st_size
        },
        "tables": {},
        "latest_snapshot": {},
        "statistics": {}
    }

    # Get table information
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' ORDER BY name")
    tables = [row[0] for row in cursor.fetchall()]

    for table in tables:
        cursor.execute(f"SELECT COUNT(*) FROM {table}")
        count = cursor.fetchone()[0]

        cursor.execute(f"PRAGMA table_info({table})")
        columns = [{"name": row[1], "type": row[2]} for row in cursor.fetchall()]

        metadata["tables"][table] = {
            "row_count": count,
            "columns": columns
        }

    # Get latest snapshot info
    cursor.execute("""
        SELECT *
        FROM repo_snapshots
        ORDER BY id DESC
        LIMIT 1
    """)
    snapshot = cursor.fetchone()

    if snapshot:
        metadata["latest_snapshot"] = {
            "id": snapshot["id"],
            "timestamp": snapshot["timestamp"],
            "commit_hash": snapshot["commit_hash"],
            "branch": snapshot["branch"],
            "file_count": snapshot["file_count"],
            "total_lines": snapshot["total_lines"],
            "agent_count": snapshot["agent_count"],
            "workflow_count": snapshot["workflow_count"]
        }

    # Calculate statistics
    snapshot_id = snapshot["id"] if snapshot else None

    if snapshot_id:
        # File type distribution
        cursor.execute("""
            SELECT file_type, COUNT(*) as count, SUM(line_count) as lines
            FROM files
            WHERE snapshot_id = ?
            GROUP BY file_type
            ORDER BY count DESC
        """, (snapshot_id,))

        metadata["statistics"]["file_types"] = [
            {"type": row[0], "count": row[1], "lines": row[2]}
            for row in cursor.fetchall()
        ]

        # Document statistics
        cursor.execute("""
            SELECT
                COUNT(*) as doc_count,
                SUM(word_count) as total_words,
                AVG(word_count) as avg_words,
                SUM(code_block_count) as total_code_blocks
            FROM documents
            WHERE snapshot_id = ?
        """, (snapshot_id,))

        doc_stats = cursor.fetchone()
        metadata["statistics"]["documents"] = {
            "count": doc_stats[0],
            "total_words": doc_stats[1],
            "average_words": round(doc_stats[2], 2) if doc_stats[2] else 0,
            "total_code_blocks": doc_stats[3]
        }

        # Agent statistics
        cursor.execute("""
            SELECT name, model, tools
            FROM agents
            WHERE snapshot_id = ?
            ORDER BY name
        """, (snapshot_id,))

        metadata["statistics"]["agents"] = [
            {"name": row[0], "model": row[1], "tools": row[2]}
            for row in cursor.fetchall()
        ]

        # Workflow statistics
        cursor.execute("""
            SELECT name, triggers, jobs
            FROM workflows
            WHERE snapshot_id = ?
            ORDER BY name
        """, (snapshot_id,))

        metadata["statistics"]["workflows"] = [
            {"name": row[0], "triggers": row[1], "jobs": row[2]}
            for row in cursor.fetchall()
        ]

        # Knowledge base statistics
        cursor.execute("""
            SELECT category, COUNT(*) as count
            FROM knowledge_base
            WHERE snapshot_id = ?
            GROUP BY category
            ORDER BY count DESC
        """, (snapshot_id,))

        metadata["statistics"]["knowledge_base"] = [
            {"category": row[0], "count": row[1]}
            for row in cursor.fetchall()
        ]

        # Agent changelog statistics
        cursor.execute("""
            SELECT COUNT(*) as phase_count
            FROM agent_changelog
            WHERE snapshot_id = ?
        """, (snapshot_id,))

        changelog_count = cursor.fetchone()[0]
        metadata["statistics"]["agent_changelog"] = {
            "phase_count": changelog_count
        }

    conn.close()

    # Write metadata file
    output_path = Path(__file__).parent.parent / "data" / "warehouse-metadata.json"
    output_path.parent.mkdir(exist_ok=True)

    with open(output_path, 'w') as f:
        json.dump(metadata, f, indent=2)

    print(f"Metadata written to {output_path}")
    print(f"Database size: {metadata['database']['size_bytes']:,} bytes")
    print(f"Tables: {len(metadata['tables'])}")
    print(f"Latest snapshot: {metadata['latest_snapshot'].get('timestamp', 'N/A')}")


if __name__ == "__main__":
    generate_metadata()
