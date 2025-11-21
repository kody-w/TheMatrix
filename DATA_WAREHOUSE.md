# The Matrix Data Warehouse

A Simon Willison-style data warehouse that tracks repository evolution, agent activity, and content patterns over time.

## Overview

The Matrix Data Warehouse automatically extracts metadata from the repository and builds a queryable SQLite database. It runs via GitHub Actions on every push and daily at midnight UTC, creating historical snapshots of the repository's state.

**Inspired by:** [Simon Willison's data journalism work](https://simonwillison.net/) and his extensive use of SQLite + GitHub Actions for data pipelines.

## Database Schema

### Tables

#### `repo_snapshots`
Tracks high-level repository state at each extraction.

| Column | Type | Description |
|--------|------|-------------|
| id | INTEGER | Snapshot ID (primary key) |
| timestamp | TEXT | ISO 8601 timestamp |
| commit_hash | TEXT | Git commit hash |
| branch | TEXT | Git branch name |
| file_count | INTEGER | Total files tracked |
| total_lines | INTEGER | Total lines of code |
| agent_count | INTEGER | Number of agents defined |
| workflow_count | INTEGER | Number of workflows |

#### `files`
Individual file metadata for each snapshot.

| Column | Type | Description |
|--------|------|-------------|
| id | INTEGER | File ID (primary key) |
| snapshot_id | INTEGER | Foreign key to repo_snapshots |
| path | TEXT | Relative file path |
| file_type | TEXT | File extension |
| size_bytes | INTEGER | File size in bytes |
| line_count | INTEGER | Number of lines |
| hash | TEXT | SHA-256 hash (first 16 chars) |
| created_at | TEXT | File creation timestamp |
| modified_at | TEXT | Last modified timestamp |

#### `documents`
Markdown document metadata.

| Column | Type | Description |
|--------|------|-------------|
| id | INTEGER | Document ID (primary key) |
| snapshot_id | INTEGER | Foreign key to repo_snapshots |
| path | TEXT | Relative file path |
| title | TEXT | Document title (first h1) |
| word_count | INTEGER | Total words |
| heading_count | INTEGER | Number of headings |
| code_block_count | INTEGER | Number of code blocks |
| link_count | INTEGER | Number of links |

#### `agents`
Agent definitions from `.claude/agents/`.

| Column | Type | Description |
|--------|------|-------------|
| id | INTEGER | Agent ID (primary key) |
| snapshot_id | INTEGER | Foreign key to repo_snapshots |
| name | TEXT | Agent name |
| file_path | TEXT | Path to agent definition |
| description | TEXT | Agent description |
| model | TEXT | LLM model (haiku, sonnet, opus) |
| tools | TEXT | Available tools |

#### `workflows`
GitHub Actions workflows from `.github/workflows/`.

| Column | Type | Description |
|--------|------|-------------|
| id | INTEGER | Workflow ID (primary key) |
| snapshot_id | INTEGER | Foreign key to repo_snapshots |
| name | TEXT | Workflow name |
| file_path | TEXT | Path to workflow file |
| description | TEXT | Workflow description |
| triggers | TEXT | JSON array of triggers |
| jobs | TEXT | JSON array of job names |

#### `knowledge_base`
Entries from `.knowledge-bases/`.

| Column | Type | Description |
|--------|------|-------------|
| id | INTEGER | Entry ID (primary key) |
| snapshot_id | INTEGER | Foreign key to repo_snapshots |
| category | TEXT | Knowledge base category |
| file_path | TEXT | Path to entry file |
| title | TEXT | Entry title |
| content_preview | TEXT | First 500 characters |

#### `agent_changelog`
Parsed entries from `AGENT_CHANGELOG.md`.

| Column | Type | Description |
|--------|------|-------------|
| id | INTEGER | Entry ID (primary key) |
| snapshot_id | INTEGER | Foreign key to repo_snapshots |
| phase_number | INTEGER | Phase number |
| phase_name | TEXT | Phase name |
| date | TEXT | Date of activity |
| agent_type | TEXT | Type of agent used |
| task | TEXT | Task description |
| duration | TEXT | How long it took |
| success_rate | TEXT | Success percentage |
| impact | TEXT | Impact description |

## Usage

### Local Development

Build the warehouse locally:

```bash
# Basic usage
python scripts/build_warehouse.py

# Custom database path
python scripts/build_warehouse.py --db custom-path.db

# Verbose output
python scripts/build_warehouse.py --verbose
```

Generate metadata and sample queries:

```bash
python scripts/generate_warehouse_metadata.py
python scripts/generate_sample_queries.py > queries.sql
```

### Querying the Database

**Direct SQL:**

```bash
# Interactive queries
sqlite3 data/matrix.db

# Run sample queries
sqlite3 data/matrix.db < data/sample-queries.sql

# One-liner queries
sqlite3 data/matrix.db "SELECT COUNT(*) FROM files"
```

**With Python:**

```python
import sqlite3

conn = sqlite3.connect('data/matrix.db')
conn.row_factory = sqlite3.Row
cursor = conn.cursor()

# Get latest snapshot
cursor.execute("""
    SELECT * FROM repo_snapshots
    ORDER BY id DESC
    LIMIT 1
""")
snapshot = cursor.fetchone()

print(f"Files: {snapshot['file_count']}")
print(f"Lines: {snapshot['total_lines']}")
```

**With Datasette (optional):**

```bash
# Install datasette
pip install datasette

# Serve the database
datasette data/matrix.db

# Or publish to Vercel
datasette publish vercel data/matrix.db \
    --project=matrix-warehouse \
    --metadata metadata.json
```

## Sample Queries

### Repository Overview

```sql
-- Latest snapshot summary
SELECT
    timestamp,
    file_count,
    total_lines,
    agent_count,
    workflow_count
FROM repo_snapshots
ORDER BY id DESC
LIMIT 1;
```

### Top 10 Largest Files

```sql
SELECT
    path,
    file_type,
    line_count,
    size_bytes
FROM files
WHERE snapshot_id = (SELECT MAX(id) FROM repo_snapshots)
ORDER BY line_count DESC
LIMIT 10;
```

### File Type Distribution

```sql
SELECT
    file_type,
    COUNT(*) as file_count,
    SUM(line_count) as total_lines,
    ROUND(AVG(line_count), 2) as avg_lines
FROM files
WHERE snapshot_id = (SELECT MAX(id) FROM repo_snapshots)
GROUP BY file_type
ORDER BY file_count DESC;
```

### Document Statistics

```sql
SELECT
    COUNT(*) as doc_count,
    SUM(word_count) as total_words,
    ROUND(AVG(word_count), 2) as avg_words,
    SUM(code_block_count) as total_code_blocks
FROM documents
WHERE snapshot_id = (SELECT MAX(id) FROM repo_snapshots);
```

### Agent Definitions

```sql
SELECT
    name,
    model,
    tools,
    description
FROM agents
WHERE snapshot_id = (SELECT MAX(id) FROM repo_snapshots)
ORDER BY name;
```

### Repository Growth Over Time

```sql
SELECT
    DATE(timestamp) as date,
    file_count,
    total_lines,
    agent_count
FROM repo_snapshots
ORDER BY timestamp;
```

**See `data/sample-queries.sql` for 30+ more example queries!**

## GitHub Actions Automation

The warehouse is automatically rebuilt by the `build-warehouse.yml` workflow:

**Triggers:**
- Push to `main` branch (when relevant files change)
- Daily at 00:00 UTC (cron schedule)
- Manual workflow dispatch

**What it does:**
1. Checks out the repository
2. Runs `build_warehouse.py` to extract data
3. Generates metadata and sample queries
4. Commits the updated database back to the repo
5. Uploads database as a build artifact
6. Posts summary to GitHub Actions UI

**Artifacts:**
- `data/matrix.db` - SQLite database (committed to repo)
- `data/warehouse-metadata.json` - JSON metadata
- `data/sample-queries.sql` - Sample SQL queries
- `matrix-warehouse` - Build artifact (30-day retention)

## Data Files

All generated data lives in the `data/` directory:

```
data/
├── matrix.db                  # SQLite database
├── warehouse-metadata.json    # JSON metadata
└── sample-queries.sql         # Sample SQL queries
```

## Extending the Warehouse

### Adding New Tables

1. Update schema in `scripts/build_warehouse.py`:

```python
def init_schema(self):
    # Add new table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS my_table (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            snapshot_id INTEGER,
            my_field TEXT,
            FOREIGN KEY (snapshot_id) REFERENCES repo_snapshots (id)
        )
    """)
```

2. Add extraction logic:

```python
def extract_my_data(self, snapshot_id: int):
    # Extract and insert data
    pass
```

3. Call from `build()` method:

```python
def build(self):
    # ... existing code ...
    self.extract_my_data(snapshot_id)
```

### Adding New Queries

Add queries to `scripts/generate_sample_queries.py`:

```python
SAMPLE_QUERIES = """
-- Your new query section
SELECT * FROM my_table;
"""
```

## Why SQLite?

**Advantages:**
- ✅ **Zero dependencies** - Single file, no server required
- ✅ **Git-friendly** - Small diffs, efficient storage
- ✅ **Fast queries** - Indexed, optimized for analytics
- ✅ **Portable** - Works everywhere Python runs
- ✅ **Queryable** - Standard SQL, wide tool support
- ✅ **Version controlled** - Full history in git

**Use cases:**
- Track repository evolution over time
- Analyze agent activity patterns
- Monitor documentation coverage
- Audit workflow configurations
- Research content patterns
- Generate reports and dashboards

## Datasette Integration (Optional)

For a web UI and API, deploy with [Datasette](https://datasette.io/):

```bash
# Install
pip install datasette datasette-publish-vercel

# Serve locally
datasette data/matrix.db

# Publish to Vercel
datasette publish vercel data/matrix.db \
    --project=matrix-warehouse \
    --metadata datasette-metadata.json

# Publish to Cloudflare Pages
datasette publish cloudflare data/matrix.db \
    --project=matrix-warehouse
```

**Features with Datasette:**
- Web-based SQL queries
- CSV/JSON export
- Faceted search
- Automatic API endpoints
- Custom SQL views
- Plugins for visualization

## Performance

**Database size:** ~100-500 KB (empty repo) to 5-10 MB (large repo)

**Query speed:**
- Simple queries: <1ms
- Aggregations: 1-10ms
- Complex joins: 10-50ms

**Build time:**
- Small repo (<100 files): ~1 second
- Medium repo (100-1000 files): ~5 seconds
- Large repo (1000+ files): ~30 seconds

**Optimizations:**
- Indexed on common query patterns
- Efficient schema design
- Batch inserts with transactions
- Hash-based change detection

## Troubleshooting

**Database locked error:**
```bash
# Close any open connections
fuser data/matrix.db  # Linux/Mac
# Kill processes if needed
```

**Permission errors:**
```bash
# Make scripts executable
chmod +x scripts/*.py
```

**Missing data in tables:**
```bash
# Rebuild with verbose output
python scripts/build_warehouse.py --verbose
```

**Query too slow:**
```sql
-- Add indexes for your query pattern
CREATE INDEX idx_my_column ON my_table(my_column);
```

## Related Projects

This warehouse is inspired by Simon Willison's work:

- [datasette](https://github.com/simonw/datasette) - Explore and publish data
- [sqlite-utils](https://github.com/simonw/sqlite-utils) - CLI tool for SQLite
- [git-history](https://github.com/simonw/git-history) - Track file changes over time
- [github-to-sqlite](https://github.com/dogsheep/github-to-sqlite) - GitHub data export

## License

MIT License - Same as The Matrix framework

## Credits

Built by Claude Code demonstrating autonomous data pipeline creation.

**Data warehouse philosophy:** "If you can track it, you can query it. If you can query it, you can understand it."

---

For more information about The Matrix framework, see [README.md](README.md).
