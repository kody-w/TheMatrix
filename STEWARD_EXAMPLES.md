# Steward Agent - Example Invocations & Use Cases

This document provides practical examples of how to invoke and use the Steward Agent for various code improvement scenarios.

---

## Basic Invocation

### Example 1: First-Time Stewardship (Conservative)

**Scenario**: You have a legacy Python codebase with no tests and want to safely add documentation.

**Invocation**:
```
Claude, please run the steward agent on my codebase with these parameters:
- Target directory: ./src
- Safety level: conservative
- Focus on: documentation improvements only
- Max changes: 5
- Use dry run first to preview changes
```

**Expected Flow**:
```
1. Steward analyzes ./src directory
2. Identifies 200+ improvement opportunities
3. Prioritizes top 5 documentation improvements
4. Shows preview (dry run mode)
5. User approves
6. Steward applies 5 documentation improvements
7. Validation via import checks
8. Generates report
```

**Result**: 5 functions documented with docstrings, type hints, and examples.

---

## Advanced Invocation Patterns

### Example 2: Error Handling Sprint

**Scenario**: Add comprehensive error handling across entire codebase.

**Invocation**:
```
Run the steward agent to improve error handling:
- Target: ./
- Safety level: moderate
- Focus on: error-handling and security
- Max changes: 15
- Validation: run existing test suite
```

**Configuration Update**:
```json
{
  "safetyLevel": "moderate",
  "validationRules": {
    "validationLevel": "test",
    "maxChangesPerRun": 15
  },
  "improvementPriorities": [
    "security",
    "error-handling"
  ],
  "improvementTypes": {
    "error-handling": { "enabled": true },
    "security": { "enabled": true },
    "documentation": { "enabled": false },
    "refactor": { "enabled": false }
  }
}
```

**Expected Output**:
```
STEWARD RUN COMPLETE ✅

15 error handling improvements applied:
- 8 try-catch blocks added
- 4 input validation functions added
- 3 custom exception classes created

All tests passed ✅
Average confidence: 89%
```

---

### Example 3: Documentation Generation for Library

**Scenario**: You're publishing a Python library and need comprehensive documentation.

**Invocation**:
```
Steward, please generate comprehensive documentation for my library:
- Target: ./mylib
- Exclude: ./mylib/tests, ./mylib/__pycache__
- Type: documentation only
- Include: docstrings, type hints, usage examples
- Max changes: 25
- Safety: moderate (we have good test coverage)
```

**Configuration**:
```json
{
  "safetyLevel": "moderate",
  "targetDirectory": "./mylib",
  "excludePatterns": [
    "tests/**",
    "__pycache__/**"
  ],
  "validationRules": {
    "maxChangesPerRun": 25
  },
  "improvementTypes": {
    "documentation": { "enabled": true }
  }
}
```

**Result**: All public functions, classes, and modules documented with comprehensive docstrings.

---

### Example 4: Performance Optimization

**Scenario**: Optimize slow utility functions.

**Invocation**:
```
Steward: Analyze and optimize performance in ./src/utils
- Focus on: performance and code-quality
- Safety: moderate
- Validation: Run pytest with timing benchmarks
- Max changes: 10
```

**Configuration**:
```json
{
  "safetyLevel": "moderate",
  "targetDirectory": "./src/utils",
  "improvementPriorities": [
    "performance",
    "code-quality"
  ],
  "validationRules": {
    "validationLevel": "test",
    "maxChangesPerRun": 10
  }
}
```

**Expected Improvements**:
- List comprehensions replacing loops
- Generator expressions for large data
- Memoization for repeated calculations
- Algorithm optimization (O(n²) → O(n log n))

---

### Example 5: Refactoring Legacy Code

**Scenario**: Large legacy module needs refactoring.

**Invocation**:
```
Steward: Refactor ./src/legacy/processor.py
- Extract long functions into smaller ones
- Reduce complexity
- Improve naming
- Safety: moderate (we have comprehensive tests)
- Validation: Full test suite must pass
- Max changes: 8
```

**Configuration**:
```json
{
  "safetyLevel": "moderate",
  "targetDirectory": "./src/legacy",
  "improvementTypes": {
    "refactor": { "enabled": true },
    "code-quality": { "enabled": true }
  },
  "validationRules": {
    "requireTests": true,
    "validationLevel": "test",
    "maxChangesPerRun": 8
  }
}
```

**Safety Note**: Refactoring requires tests. Steward will only refactor if comprehensive tests exist.

---

## Multi-Stage Workflows

### Example 6: Progressive Improvement Pipeline

**Stage 1: Documentation (Week 1)**
```
Run steward:
- Safety: conservative
- Type: documentation
- Max changes: 20
```

**Stage 2: Error Handling (Week 2)**
```
Run steward:
- Safety: moderate (confidence built from stage 1)
- Type: error-handling, security
- Max changes: 20
```

**Stage 3: Code Quality (Week 3)**
```
Run steward:
- Safety: moderate
- Type: code-quality, performance
- Max changes: 15
```

**Stage 4: Refactoring (Week 4)**
```
Run steward:
- Safety: moderate
- Type: refactor
- Max changes: 10
- Requirement: All files have tests
```

**Result**: Comprehensive codebase improvement over 4 weeks with validated progress.

---

## Domain-Specific Examples

### Example 7: Express.js API Server

**Scenario**: Add error handling and documentation to Express routes.

**Invocation**:
```
Steward: Improve Express.js API in ./routes
- Language: JavaScript
- Add: error handling, input validation, JSDoc comments
- Validation: Run npm test
- Safety: moderate
- Max changes: 12
```

**File Type Config**:
```json
{
  "fileTypeConfig": {
    "javascript": {
      "extensions": [".js"],
      "validationOrder": ["syntax", "test"],
      "testDirectories": ["tests/"]
    }
  }
}
```

**Expected Improvements**:
- Try-catch in async route handlers
- Input validation middleware
- JSDoc comments for all routes
- Proper HTTP status codes

---

### Example 8: React Component Library

**Scenario**: Add TypeScript types and prop documentation.

**Invocation**:
```
Steward: Improve React components in ./src/components
- Language: TypeScript/TSX
- Add: PropTypes, JSDoc, component documentation
- Focus on: documentation, code-quality
- Safety: moderate
- Max changes: 15
```

**Expected Improvements**:
- TypeScript interfaces for props
- JSDoc comments with usage examples
- Prop validation
- Storybook-friendly documentation

---

### Example 9: Data Science Scripts

**Scenario**: Add error handling and documentation to Jupyter notebooks converted to scripts.

**Invocation**:
```
Steward: Improve data science scripts in ./scripts
- Add: error handling for file I/O, data validation
- Add: function documentation with parameter types
- Validation: Import validation (no test suite)
- Safety: conservative
- Max changes: 10
```

**Expected Improvements**:
- Try-catch around file operations
- Data validation (check for NaN, empty dataframes)
- Type hints for NumPy/Pandas types
- Usage examples in docstrings

---

## Special Use Cases

### Example 10: Pre-Production Hardening

**Scenario**: Preparing codebase for production deployment.

**Invocation**:
```
Steward: Harden codebase for production:
- Focus on: security, error-handling
- Target: ./src
- Validation: Full test suite + security linting
- Safety: moderate
- Max changes: 20
```

**Configuration**:
```json
{
  "improvementPriorities": [
    "security",
    "error-handling"
  ],
  "validationRules": {
    "validationLevel": "test",
    "maxChangesPerRun": 20
  }
}
```

**Expected Improvements**:
- Input validation for all user-facing functions
- SQL injection prevention
- XSS protection
- Comprehensive error handling
- Logging for debugging

---

### Example 11: Open Source Library Preparation

**Scenario**: Preparing code for open source release.

**Invocation**:
```
Steward: Prepare codebase for open source:
- Add comprehensive documentation (docstrings, README examples)
- Add error handling with clear messages
- Improve code quality (naming, structure)
- Target: ./src
- Safety: moderate
- Max changes: 30
```

**Multi-Run Strategy**:
```bash
# Run 1: Documentation
steward --type documentation --max 30

# Run 2: Error handling
steward --type error-handling --max 20

# Run 3: Code quality
steward --type code-quality --max 15
```

---

### Example 12: Test Coverage Improvement

**Scenario**: Add test coverage before enabling refactoring.

**Invocation**:
```
Steward: Add test coverage for untested modules:
- Target: ./src/core
- Type: testing
- Generate: unit tests for all public functions
- Max changes: 15
- Safety: moderate
```

**Note**: This is a future enhancement. Current steward focuses on code improvement, not test generation.

---

## Interactive Mode Examples

### Example 13: Review Before Apply

**Scenario**: You want to review each change before it's applied.

**Invocation**:
```
Steward: Improve ./src with interactive mode:
- Show me each proposed change
- Let me approve/reject individually
- Focus on: refactoring
- Max changes: 10
```

**Configuration**:
```json
{
  "advancedOptions": {
    "interactive": true
  }
}
```

**Workflow**:
```
Improvement 1/10: Refactor utils/helpers.py

PROPOSED CHANGE:
[Shows diff]

Risk: Medium
Confidence: 78%

Apply this improvement? [y/n/skip remaining]: y
✅ Applied

Improvement 2/10: Refactor core/processor.py
[Shows diff]

Apply this improvement? [y/n/skip remaining]: n
⏭️ Skipped
```

---

## Validation Strategy Examples

### Example 14: Syntax-Only Validation (Fast)

**Scenario**: Quick improvements with minimal validation overhead.

**Invocation**:
```
Steward: Quick documentation pass:
- Validation: syntax only (fast)
- Type: documentation
- Max changes: 30
- Safety: conservative
```

**Use when**: Adding documentation or comments (low-risk changes).

---

### Example 15: Full Test Suite Validation (Safe)

**Scenario**: Complex refactoring with comprehensive validation.

**Invocation**:
```
Steward: Refactor with full validation:
- Validation: complete test suite
- Type: refactor
- Max changes: 5
- Safety: moderate
- Requirement: 100% test pass rate
```

**Use when**: Refactoring or performance optimizations (higher-risk changes).

---

## Troubleshooting Examples

### Example 16: Recovering from Failed Run

**Scenario**: Steward run failed mid-way, need to resume.

**Invocation**:
```
Steward: Resume from last successful improvement:
- Check .steward-log.jsonl for last completed improvement
- Resume from next improvement in queue
- Same configuration as previous run
```

**Steward will**:
1. Read log to find last successful improvement
2. Skip completed improvements
3. Resume from next in queue
4. Continue with same safety parameters

---

### Example 17: Rollback Specific Improvement

**Scenario**: One improvement from a successful run needs to be reverted.

**Manual Rollback**:
```bash
# Find improvement in log
grep "improvement-uuid-5" .steward-log.jsonl

# Locate backup
ls .steward-backups/ | grep "improvement-uuid-5"

# Restore from backup
cp .steward-backups/uuid-5_timestamp_file.py.bak src/module.py
```

---

## Validation with Steward-Validator

### Example 18: Full Audit After Steward Run

**Invocation**:
```
After steward completes, run steward-validator:
- Validate run ID: {runId}
- Check safety compliance
- Assess improvement quality
- Generate audit report
```

**Validator Output**:
```
STEWARD VALIDATOR AUDIT COMPLETE ✅

Safety Compliance: 100%
Improvement Quality: 4.3/5.0
Trust Level: High

RECOMMENDATION: Approve for continued autonomous operation
```

---

## Summary of Invocation Patterns

| Use Case | Safety Level | Validation | Max Changes | Focus |
|----------|-------------|------------|-------------|-------|
| **First time** | Conservative | Import | 5 | Documentation |
| **Add docs** | Moderate | Import | 20-30 | Documentation |
| **Error handling** | Moderate | Test | 15 | Error-handling |
| **Performance** | Moderate | Test | 10 | Performance |
| **Refactoring** | Moderate | Test | 5-10 | Refactor |
| **Security** | Moderate | Test + Lint | 15 | Security |
| **Production prep** | Moderate | Test | 20 | Security + Error |
| **Open source** | Moderate | Test | 30 | Docs + Quality |

---

## Best Practices

1. **Start Conservative**: First run should be conservative with dry-run enabled
2. **Progressive Trust**: Increase safety level after successful runs
3. **Validate Thoroughly**: Use test-level validation for refactoring
4. **Review Reports**: Always read the steward report after each run
5. **Use Validator**: Run steward-validator for high-stakes codebases
6. **Iterate**: Multiple focused runs better than one large run
7. **Version Control**: Always run steward in a git repository

---

## Quick Reference Commands

```bash
# Basic stewardship
"Run steward on my codebase"

# Conservative with dry run
"Steward: dry run, conservative mode, document ./src"

# Moderate with validation
"Steward: moderate mode, add error handling, validate with tests, max 15 changes"

# Focused improvement
"Steward: improve performance in ./utils, max 10 changes"

# Interactive review
"Steward: interactive mode, refactor ./core, show me each change"

# Full audit
"Run steward-validator to audit the last steward run"
```

---

**For detailed configuration**: See `.claude/steward-config.json`

**For agent instructions**: See `.claude/agents/steward.md`

**For validator**: See `.claude/agents/steward-validator.md`

**For full documentation**: See `STEWARD.md`
