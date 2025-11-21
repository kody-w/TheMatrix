# Steward Agent - Quick Reference Card

**Autonomous Code Improvement System**

---

## Quick Invocation Commands

### Basic Usage
```
"Run steward on my codebase"
```

### Conservative Mode (First Time)
```
"Steward: conservative mode, documentation only, dry run first, max 5 changes"
```

### Moderate Mode (Well-Tested Codebase)
```
"Steward: moderate mode, add error handling + documentation, validate with tests, max 15"
```

### Focused Improvement
```
"Steward: improve performance in ./utils, max 10 changes"
```

### Audit Last Run
```
"Run steward-validator to audit the last steward run"
```

---

## Safety Levels

| Level | Risk | Max Changes | Confidence | Use When |
|-------|------|-------------|------------|----------|
| **Conservative** | Low only | 5 | 85%+ | First time, production, critical |
| **Moderate** | Low-Medium | 10 | 75%+ | Well-tested, development |
| **Aggressive** | All levels | 20 | 65%+ | Prototypes, personal projects |

---

## Improvement Types

| Type | Risk | Impact | Description |
|------|------|--------|-------------|
| **Documentation** | Low | High | Docstrings, type hints, examples |
| **Error Handling** | Low | High | Try-catch, validation, edge cases |
| **Security** | Medium | Critical | Input validation, vulnerabilities |
| **Performance** | Medium | High | Algorithm optimization, efficiency |
| **Code Quality** | Low | Medium | Naming, structure, duplication |
| **Refactoring** | Medium | Medium | Extract functions, simplify logic |
| **Testing** | Low | High | Unit tests, coverage |

---

## Validation Levels

| Level | Speed | Confidence | Requirements |
|-------|-------|------------|--------------|
| **Syntax** | Fast | Low | Always available |
| **Import** | Medium | Medium | Module can import |
| **Test** | Slow | High | Test suite exists |
| **Lint** | Medium | Medium | Linter configured |

---

## Key Files

| File | Purpose |
|------|---------|
| `.claude/agents/steward.md` | Core agent definition |
| `.claude/agents/steward-validator.md` | Validator agent |
| `.claude/steward-config.json` | Configuration |
| `.steward-log.jsonl` | Improvement audit log |
| `.steward-backups/` | File backups |
| `.steward-reports/` | Run reports |
| `STEWARD.md` | Full documentation |
| `STEWARD_EXAMPLES.md` | Use case examples |

---

## Configuration Quick Edit

```json
{
  "safetyLevel": "conservative|moderate|aggressive",
  "validationRules": {
    "validationLevel": "syntax|import|test|lint",
    "maxChangesPerRun": 5,
    "minConfidence": 0.85
  },
  "improvementTypes": {
    "documentation": { "enabled": true },
    "error-handling": { "enabled": true },
    "refactor": { "enabled": false }
  }
}
```

---

## Example Workflows

### Workflow 1: First-Time Use
```
1. "Steward: dry run, conservative, document ./src"
2. Review proposed improvements
3. "Steward: apply improvements (no dry run)"
4. Review report in .steward-reports/
5. "Run steward-validator"
```

### Workflow 2: Continuous Improvement
```
Week 1: Documentation (conservative, 5 changes)
Week 2: Error handling (moderate, 10 changes)
Week 3: Performance (moderate, 10 changes)
Week 4: Refactoring (moderate, 5 changes)
```

### Workflow 3: Production Hardening
```
"Steward: moderate mode, focus on security + error-handling,
validate with full test suite, max 20 changes"
```

---

## Safety Guarantees

✅ **Backup before every change**
✅ **Validate after every change**
✅ **Automatic rollback on failure**
✅ **One improvement at a time**
✅ **Complete audit trail**
✅ **Conservative by default**

---

## Troubleshooting

### High Rollback Rate
- Lower safety level to conservative
- Use dry run to preview
- Add tests before refactoring

### No Improvements Found
- Check excludePatterns
- Enable more improvement types
- Lower safety level

### Validation Failures
- Verify validation commands for your stack
- Check existing test suite passes
- Use import validation if no tests

---

## Quick Stats

After each run, check:
```bash
# View last report
ls -lt .steward-reports/ | head -n 1

# Check success rate
tail -20 .steward-log.jsonl | jq '.status'

# Count improvements by type
jq -s 'group_by(.improvementType) |
  map({type: .[0].improvementType, count: length})'
  .steward-log.jsonl
```

---

## Trust Building Path

```
Run 1: Dry run only → Preview
  ↓
Run 2: Conservative (3 docs) → 100% success
  ↓
Run 3: Conservative (5 docs + error) → 90% success
  ↓
Run 4: Moderate (10 mixed) → 85% success
  ↓
Run 5: Moderate (15 with refactor) → 80% success
  ↓
Trusted autonomous operation ✅
```

---

## Best Practices

1. **Start conservative**: First run should be low-risk
2. **Use dry run**: Preview before applying
3. **Review reports**: Read every steward report
4. **Have tests**: Tests enable refactoring safely
5. **Use git**: Version control enables easy revert
6. **Run validator**: Audit steward's work regularly
7. **Iterate**: Multiple focused runs better than one large run

---

## Language Support

| Language | Extensions | Validation | Status |
|----------|-----------|------------|--------|
| **Python** | .py | syntax, import, pytest | ✅ Full |
| **JavaScript** | .js, .jsx | syntax, import, npm test | ✅ Full |
| **TypeScript** | .ts, .tsx | syntax, import, jest | ✅ Full |
| **Go** | .go | - | 🔄 Planned |
| **Rust** | .rs | - | 🔄 Planned |
| **Java** | .java | - | 🔄 Planned |

---

## When to Use Steward

✅ **Perfect for:**
- Improving legacy codebases
- Adding documentation systematically
- Improving error handling
- Preparing for production
- Continuous code quality improvement

❌ **Not suitable for:**
- New feature development (use outcome-generator)
- Breaking API changes
- Major architecture changes
- Codebases with zero validation strategy

---

## Getting Help

1. Read `STEWARD.md` (comprehensive guide)
2. Review `STEWARD_EXAMPLES.md` (18 use cases)
3. Check `.steward-log.jsonl` (detailed logs)
4. Review `.steward-reports/` (run-specific reports)
5. See `STEWARD_IMPLEMENTATION_SUMMARY.md` (technical details)

---

## Success Metrics

**Conservative Mode**:
- 90-95% success rate
- 85-90% avg confidence
- 30-60s per improvement

**Moderate Mode**:
- 85-90% success rate
- 80-85% avg confidence
- 45-90s per improvement

**Aggressive Mode**:
- 75-85% success rate
- 70-80% avg confidence
- 60-120s per improvement

---

**Quick Start**: `"Run steward on my codebase"`

**Documentation**: See `STEWARD.md`

**Examples**: See `STEWARD_EXAMPLES.md`

**Trust**: Safety-first, backup → validate → rollback

**License**: MIT

---

**Safe, incremental, autonomous code improvement.** 🛡️
