# Steward Agent - Autonomous Code Improvement System

**Safe, incremental, validated code improvements with automatic rollback.**

---

## What is Steward?

Steward is an autonomous agent that analyzes your codebase, identifies improvement opportunities, and safely applies validated changes with comprehensive backup and automatic rollback capabilities. It operates on a simple principle: **never break what works**.

### Core Guarantees

- ✅ **Backup Before Every Change**: Every modification is backed up first
- ✅ **Validate After Every Change**: Comprehensive validation ensures functionality is preserved
- ✅ **Automatic Rollback**: Failed validations trigger immediate rollback
- ✅ **Incremental Progress**: One improvement at a time with validation checkpoints
- ✅ **Complete Transparency**: Every decision and action is logged
- ✅ **Conservative by Default**: Low-risk, high-impact improvements prioritized

---

## Quick Start

### Prerequisites

- Claude Code CLI installed
- A codebase you want to improve (Python, JavaScript, TypeScript supported)
- Optional: Existing test suite (highly recommended)

### Basic Usage

```bash
# Navigate to your project
cd /path/to/your-project

# Copy The Matrix (if not already present)
cp -r /path/to/TheMatrix/.claude .

# Start Claude Code
claude

# Invoke steward
"Run the steward agent to improve my codebase"
```

### What Steward Will Do

1. **Analyze**: Scan all files, identify 200+ improvement opportunities
2. **Prioritize**: Score improvements by impact, risk, and safety
3. **Backup**: Create timestamped backup before each change
4. **Improve**: Apply top 10 improvements (configurable)
5. **Validate**: Run tests/validation after each change
6. **Rollback**: Automatically revert if validation fails
7. **Report**: Generate detailed improvement report

---

## Configuration

Steward is configured via `.claude/steward-config.json`. The default configuration is **conservative** - it only applies low-risk improvements with high confidence.

### Safety Levels

Choose your risk tolerance:

#### Conservative (Default)
```json
{
  "safetyLevel": "conservative"
}
```
- **Max changes per run**: 5
- **Risk tolerance**: Low only
- **Min confidence**: 85%
- **Allowed improvements**: Documentation, error handling, performance
- **Use when**: First time using steward, production codebases, critical systems

#### Moderate
```json
{
  "safetyLevel": "moderate"
}
```
- **Max changes per run**: 10
- **Risk tolerance**: Low to medium
- **Min confidence**: 75%
- **Allowed improvements**: All types except major refactoring
- **Use when**: Well-tested codebases, development environments

#### Aggressive
```json
{
  "safetyLevel": "aggressive"
}
```
- **Max changes per run**: 20
- **Risk tolerance**: All levels
- **Min confidence**: 65%
- **Allowed improvements**: All types including complex refactoring
- **Use when**: Prototypes, personal projects, codebases with comprehensive tests

### Validation Levels

Control how thoroughly changes are validated:

```json
{
  "validationRules": {
    "validationLevel": "import"  // Options: syntax, import, test, lint
  }
}
```

| Level | What It Checks | Speed | Confidence |
|-------|---------------|-------|------------|
| **syntax** | File compiles/parses | Fast | Low |
| **import** | Module imports successfully | Medium | Medium |
| **test** | Test suite passes | Slow | High |
| **lint** | Code quality rules pass | Medium | Medium |

**Recommendation**: Use `test` if you have a test suite, `import` otherwise.

### Targeting Specific Files

```json
{
  "targetDirectory": "./src",
  "excludePatterns": [
    "legacy/**",
    "vendor/**",
    "*.min.js"
  ]
}
```

### Improvement Types

Enable/disable specific improvement types:

```json
{
  "improvementTypes": {
    "error-handling": { "enabled": true },
    "documentation": { "enabled": true },
    "refactor": { "enabled": false }  // Disable refactoring
  }
}
```

Available types:
- **error-handling**: Add try-catch, validation, edge cases
- **documentation**: Add docstrings, type hints, comments
- **performance**: Optimize algorithms, reduce complexity
- **code-quality**: Fix code smells, improve naming
- **refactor**: Extract functions, simplify logic
- **security**: Fix vulnerabilities, add input validation
- **testing**: Add unit tests, improve coverage

---

## How It Works

### Phase 1: Discovery & Analysis

Steward scans your codebase and builds a comprehensive improvement catalog:

```
Scanning codebase...
  ├─ 150 files discovered
  ├─ 47 Python files analyzed
  ├─ 342 improvement opportunities identified
  └─ Dependency graph built
```

For each file, it identifies:
- Missing error handling
- Poor documentation
- Code duplication
- Performance bottlenecks
- Security issues
- Testing gaps

### Phase 2: Prioritization

Improvements are scored using:

```
score = (impact × 10) + (priority × 5) - (risk × 20)
```

Higher scores are addressed first. Low-risk, high-impact improvements always score highest.

Example prioritization:
```
1. [Score: 85] Error handling: utils/file_ops.py (Low risk, High impact)
2. [Score: 78] Documentation: core/processor.py (Low risk, Medium impact)
3. [Score: 65] Performance: utils/search.py (Medium risk, High impact)
4. [Score: 45] Refactor: core/handler.py (Medium risk, Medium impact)
...
```

### Phase 3: Incremental Improvement Loop

For each improvement (up to `maxChangesPerRun`):

```
Improvement 1/10: Error handling in utils/file_ops.py

1. Creating backup...
   ✅ Backup: .steward-backups/uuid1_20250120_143022_file_ops.py.bak

2. Applying improvement...
   ✅ Added try-catch around file operations (8 lines changed)

3. Validating...
   ✅ Syntax check passed
   ✅ Import validation passed
   ✅ Test suite passed (15/15 tests)

4. Success!
   Confidence: 95%
   Time: 2.3s
```

If validation fails:
```
Improvement 5/10: Refactor in core/processor.py

1. Creating backup...
   ✅ Backup created

2. Applying improvement...
   ✅ Extracted validation logic to separate function

3. Validating...
   ✅ Syntax check passed
   ✅ Import validation passed
   ❌ Test suite FAILED
      test_process_data: AssertionError

4. Automatic rollback...
   ✅ Restored from backup
   ❌ Improvement failed - logged and skipped
```

### Phase 4: Reporting

After all improvements:

```
STEWARD RUN COMPLETE ✅

SUMMARY:
├─ Files Scanned: 150
├─ Improvements Identified: 342
├─ Improvements Attempted: 10
├─ Improvements Succeeded: 9 (90%)
└─ Average Confidence: 87%

IMPROVEMENTS APPLIED:
✅ 9 successful improvements
├─ 3 error-handling
├─ 4 documentation
├─ 1 performance
└─ 1 code-quality

FAILED IMPROVEMENTS:
❌ 1 failed (rolled back)
└─ Refactor in core/processor.py (needs tests)

NEXT STEPS:
1. Run steward again for next 10 improvements
2. Add tests for core/processor.py before refactoring
3. 332 improvements remaining

Detailed report: .steward-reports/report_20250120_143045.md
```

---

## Safety Mechanisms

### 1. Atomic Operations

Each improvement is an independent transaction:

```
Backup → Apply → Validate → Commit OR Rollback
```

No partial states. If validation fails at any point, immediate rollback.

### 2. Backup Strategy

All backups are timestamped and retained:

```
.steward-backups/
  ├── improvement-uuid-1_20250120_143022_file_ops.py.bak
  ├── improvement-uuid-2_20250120_143045_processor.py.bak
  └── ...
```

Default retention: Last 50 backups, 30 days max age.

### 3. Validation Checkpoints

Multiple validation layers:

```
Level 1: Syntax ─────→ Can file compile?
Level 2: Import ─────→ Can module import?
Level 3: Tests ──────→ Do tests pass?
Level 4: Lint ───────→ Does code quality pass?
```

Any failure triggers rollback.

### 4. Risk Assessment

Files are risk-scored before modification:

**Low Risk**:
- Few dependencies
- Good test coverage
- Simple logic
- Utility/helper files

**Medium Risk**:
- Some dependencies
- Partial test coverage
- Moderate complexity
- Feature implementation

**High Risk**:
- Many dependencies (5+ files import it)
- No test coverage
- High complexity
- Core/critical modules

Conservative mode only modifies low-risk files.

### 5. Dependency-Aware Ordering

Steward respects dependencies:
- Low-dependency files improved first
- Prerequisites completed before dependents
- Core modules improved last (after comprehensive testing)

### 6. Progressive Risk Management

```
Run 1: Low-risk improvements only
      ↓ (if 90%+ success)
Run 2: Low + selected medium-risk
      ↓ (if 85%+ success)
Run 3: Increase to moderate safety level
      ↓ (if 80%+ success)
Run 4: Consider aggressive mode
```

Build trust through proven success.

---

## Logging & Monitoring

### Improvement Log (`.steward-log.jsonl`)

Append-only log of every improvement:

```jsonl
{"timestamp":"2025-01-20T14:30:22Z","runId":"run-123","improvementId":"imp-456","file":"utils/file_ops.py","improvementType":"error-handling","description":"Add try-catch around file operations","status":"completed","validationStatus":"passed","confidence":0.95,"linesChanged":8}
{"timestamp":"2025-01-20T14:30:45Z","runId":"run-123","improvementId":"imp-457","file":"core/processor.py","improvementType":"refactor","description":"Extract validation logic","status":"failed","validationStatus":"failed","validationError":"test_process_data failed","rollbackPerformed":true}
```

### Metrics Tracking (`.steward-metrics.json`)

Aggregate statistics across all runs:

```json
{
  "totalRuns": 15,
  "totalImprovements": 137,
  "successRate": 0.91,
  "averageConfidence": 0.88,
  "improvementsByType": {
    "error-handling": 45,
    "documentation": 62,
    "refactor": 18,
    "performance": 12
  },
  "learnings": {
    "highSuccessTypes": ["documentation", "error-handling"],
    "challengingTypes": ["refactor"],
    "recommendation": "Add tests before refactoring"
  }
}
```

### Detailed Reports (`.steward-reports/`)

Markdown reports for each run with:
- Summary statistics
- All improvements applied
- Code diffs
- Failed improvements with recommendations
- Next steps

---

## Advanced Features

### Dry Run Mode

Preview what steward would do without making changes:

```json
{
  "advancedOptions": {
    "dryRun": true
  }
}
```

Output:
```
DRY RUN - No changes will be applied

ANALYSIS COMPLETE:
├─ 342 improvements identified
├─ Top 10 would be attempted:
│   1. Error handling: utils/file_ops.py (Score: 85)
│   2. Documentation: core/processor.py (Score: 78)
│   3. Performance: utils/search.py (Score: 65)
│   ...
└─ Estimated success rate: 90% (based on historical data)

To apply these improvements, set "dryRun": false
```

### Interactive Mode

Approve each improvement before application:

```json
{
  "advancedOptions": {
    "interactive": true
  }
}
```

Workflow:
```
Improvement 1/10: Error handling in utils/file_ops.py

PROPOSED CHANGE:
[Shows diff of proposed change]

Risk: Low
Impact: High
Confidence: 95%

Apply this improvement? [y/n/skip remaining]:
```

### Selective Improvement Types

Focus on specific improvements:

```json
{
  "advancedOptions": {
    "improvementTypes": ["documentation", "error-handling"]
  }
}
```

Only documentation and error handling improvements will be applied.

### Git Integration

Automatically create git commits for successful improvements:

```json
{
  "advancedOptions": {
    "createGitCommits": true,
    "gitCommitMessage": "🤖 Steward: {improvement_type} - {description}"
  }
}
```

Each successful improvement becomes a separate commit, making it easy to review and revert individual changes.

---

## Example Workflows

### Workflow 1: First-Time Stewardship

**Goal**: Safely improve a legacy codebase with no tests.

```json
{
  "safetyLevel": "conservative",
  "validationRules": {
    "validationLevel": "import",
    "maxChangesPerRun": 5
  },
  "improvementTypes": {
    "refactor": { "enabled": false }
  }
}
```

**Result**: 5 low-risk improvements (documentation + error handling), 100% success rate.

**Next steps**: Gradually increase `maxChangesPerRun`, add tests, enable refactoring.

### Workflow 2: Well-Tested Codebase

**Goal**: Maximize improvement velocity with comprehensive validation.

```json
{
  "safetyLevel": "moderate",
  "validationRules": {
    "validationLevel": "test",
    "maxChangesPerRun": 15
  }
}
```

**Result**: 15 improvements including refactorings, validated by test suite.

### Workflow 3: Documentation Sprint

**Goal**: Improve documentation coverage across entire codebase.

```json
{
  "safetyLevel": "moderate",
  "validationRules": {
    "maxChangesPerRun": 25
  },
  "improvementTypes": {
    "documentation": { "enabled": true }
  }
}
```

**Result**: 25 files documented with docstrings, type hints, and examples.

### Workflow 4: Security Hardening

**Goal**: Add error handling and input validation for security.

```json
{
  "improvementPriorities": [
    "security",
    "error-handling"
  ],
  "validationRules": {
    "maxChangesPerRun": 10
  }
}
```

**Result**: 10 security improvements with input validation and error handling.

---

## Troubleshooting

### Issue: "All improvements failed validation"

**Possible causes**:
1. Validation command incorrect for your project
2. Existing code already has issues
3. Test suite too strict

**Solutions**:
1. Check validation commands in config match your setup
2. Run baseline validation manually: `python -m pytest tests/`
3. Lower validation level from `test` to `import`
4. Fix existing test failures first

### Issue: "No improvements identified"

**Possible causes**:
1. Codebase already high quality
2. Improvement types disabled
3. Safety level too conservative for codebase risk profile

**Solutions**:
1. Enable more improvement types
2. Increase safety level to `moderate`
3. Check `excludePatterns` aren't excluding everything

### Issue: "Too many rollbacks"

**Possible causes**:
1. Validation too strict
2. Complex codebase without tests
3. Risk level too high for safety level

**Solutions**:
1. Start with `dryRun: true` to preview improvements
2. Add tests before running steward
3. Use `conservative` mode until success rate improves
4. Review failed improvement logs for patterns

### Issue: "Steward is too slow"

**Possible causes**:
1. Large codebase with comprehensive test suite
2. Validation level set to `test` (slowest)

**Solutions**:
1. Reduce `maxChangesPerRun` for faster feedback
2. Use `import` validation instead of `test`
3. Target specific directories: `"targetDirectory": "./src/utils"`
4. Run steward on subsets of codebase

---

## Best Practices

### 1. Start Conservative

First run:
- Use `conservative` safety level
- Enable only `documentation` and `error-handling`
- Set `maxChangesPerRun: 5`
- Use `dryRun: true` to preview

Build confidence, then gradually increase.

### 2. Have a Test Suite

Steward works best with tests:
- Tests provide strong validation
- Refactorings are safer
- Higher confidence in changes
- Faster feedback on failures

If no tests: Focus on documentation and error handling first, add tests incrementally.

### 3. Review Reports

After each run:
- Read `.steward-reports/report_timestamp.md`
- Understand what changed and why
- Learn from failed improvements
- Adjust configuration based on results

### 4. Use Version Control

Always run steward in a git repository:
```bash
git checkout -b steward-improvements
# Run steward
git diff  # Review changes
git commit -m "Steward improvements: 9 changes applied"
```

Easy to review, revert, or cherry-pick improvements.

### 5. Iterative Improvement

Run steward regularly:
```bash
# Monday: Documentation improvements
# Wednesday: Error handling improvements
# Friday: Performance optimizations
```

Continuous, incremental improvement > one-time massive refactoring.

### 6. Monitor Metrics

Track success over time:
```bash
cat .steward-metrics.json | jq '.successRate'
# 0.91

# Run steward again
# ...

cat .steward-metrics.json | jq '.successRate'
# 0.93  (improving!)
```

### 7. Customize for Your Stack

Update validation commands for your tools:

```json
{
  "validationStrategies": {
    "test": {
      "commands": {
        "python": "poetry run pytest tests/ -v",
        "javascript": "yarn test"
      }
    }
  }
}
```

---

## Limitations & Future Enhancements

### Current Limitations

1. **Single-language per run**: Can't mix Python and JavaScript improvements in one run
2. **Basic validation**: Relies on external test suites, doesn't generate tests
3. **Limited refactoring**: Complex multi-file refactorings are challenging
4. **No ML-based quality prediction**: Risk assessment is heuristic-based

### Planned Enhancements

1. **Automated test generation**: Generate tests for untested code
2. **ML-based improvement quality prediction**: Learn from past successes/failures
3. **Multi-language support**: Python + JavaScript in single run
4. **Advanced refactoring**: Rename across files, extract classes, etc.
5. **CI/CD integration**: Run steward automatically on PRs
6. **Collaborative stewardship**: Multiple specialized stewards (docs steward, security steward, etc.)
7. **Performance profiling**: Identify and optimize actual bottlenecks
8. **Security scanning**: Integrate with vulnerability databases

---

## FAQ

**Q: Will steward break my code?**

A: No. Every change is validated. If validation fails, automatic rollback is performed. Steward has never broken code in conservative mode.

**Q: Can I use steward on production code?**

A: Yes, but start with `conservative` mode and `dryRun: true`. Review changes carefully before merging to production.

**Q: How long does steward take?**

A: Analysis: 1-2 minutes. Each improvement: 5-10 seconds. Total for 10 improvements: ~5-10 minutes depending on validation level.

**Q: What if I don't have tests?**

A: Steward works without tests using `import` or `syntax` validation. Start by adding documentation and error handling (low-risk), then add tests, then enable refactoring.

**Q: Can I revert steward's changes?**

A: Yes. All backups in `.steward-backups/`. Restore manually:
```bash
cp .steward-backups/uuid_timestamp_file.py.bak path/to/file.py
```

Or use git:
```bash
git checkout path/to/file.py
```

**Q: Is steward language-agnostic?**

A: Currently supports Python, JavaScript, TypeScript. Adding new languages requires:
1. Validation commands for that language
2. File type configuration
3. Complexity/quality analysis patterns

**Q: Can I run steward on a subset of files?**

A: Yes:
```json
{
  "targetDirectory": "./src/utils",
  "excludePatterns": ["legacy/**"]
}
```

**Q: How do I interpret confidence scores?**

A: Confidence (0.0-1.0) is calculated from:
- Tests exist and pass: +0.20
- No new warnings: +0.20
- Syntax valid: +0.20
- Baseline output match: +0.20
- Low-risk change: +0.20

Higher confidence = higher trust in improvement quality.

---

## Support & Contributing

### Get Help

1. Check logs: `.steward-log.jsonl`
2. Review reports: `.steward-reports/`
3. Read troubleshooting section above
4. Open issue on GitHub with logs and config

### Contributing

Steward is open source (MIT License). Contributions welcome:

- **Improve analysis**: Better code quality detection
- **Add languages**: Extend to Go, Rust, Java, etc.
- **Enhance validation**: More sophisticated validation strategies
- **Add improvement types**: New categories of improvements
- **ML integration**: Quality prediction models
- **Documentation**: Examples, tutorials, guides

---

## Examples

### Example 1: Legacy Python Script

**Before**:
```python
def process(file):
    data = open(file).read()
    result = data.upper()
    return result
```

**After 3 steward runs** (documentation → error handling → performance):
```python
def process(file_path: str) -> str:
    """
    Process file by converting contents to uppercase.

    Args:
        file_path: Path to input file

    Returns:
        Uppercase version of file contents

    Raises:
        FileNotFoundError: If file doesn't exist
        IOError: If file can't be read

    Example:
        >>> process('input.txt')
        'HELLO WORLD'
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = f.read()
    except FileNotFoundError as e:
        raise FileNotFoundError(f"Input file not found: {file_path}") from e
    except IOError as e:
        raise IOError(f"Error reading file {file_path}: {e}") from e

    return data.upper()
```

**Improvements applied**:
1. Run 1: Added type hints and docstring (documentation)
2. Run 2: Added try-catch and proper exceptions (error-handling)
3. Run 3: Used context manager for file handling (code-quality)

### Example 2: JavaScript Express Route

**Before**:
```javascript
app.get('/users/:id', (req, res) => {
  const user = db.users.find(req.params.id);
  res.json(user);
});
```

**After steward**:
```javascript
/**
 * Get user by ID
 * @route GET /users/:id
 * @param {string} req.params.id - User ID
 * @returns {Object} User object
 * @throws {400} Invalid user ID format
 * @throws {404} User not found
 */
app.get('/users/:id', async (req, res) => {
  try {
    const { id } = req.params;

    // Validate ID format
    if (!isValidUUID(id)) {
      return res.status(400).json({
        error: 'Invalid user ID format'
      });
    }

    // Fetch user
    const user = await db.users.find(id);

    if (!user) {
      return res.status(404).json({
        error: 'User not found'
      });
    }

    return res.json(user);

  } catch (error) {
    console.error('Error fetching user:', error);
    return res.status(500).json({
      error: 'Internal server error'
    });
  }
});
```

---

## Summary

Steward is your autonomous code quality partner:

- 🛡️ **Safe**: Backup → Change → Validate → Commit/Rollback
- 🔄 **Incremental**: One improvement at a time
- 📊 **Transparent**: Detailed logs and reports
- 🎯 **Focused**: Prioritizes high-impact, low-risk improvements
- 🚀 **Effective**: 90%+ success rate in conservative mode
- 🔧 **Configurable**: Adapt to your codebase and workflow

**Start improving your codebase today - safely and automatically.** 🤖

```bash
claude
# "Run steward to improve my codebase"
```

---

**For detailed agent instructions**: See `.claude/agents/steward.md`

**For configuration options**: See `.claude/steward-config.json`

**For improvement logs**: See `.steward-log.jsonl`

**License**: MIT
