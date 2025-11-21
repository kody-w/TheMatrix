# Portfolio Steward Metadata Schema

**Version**: 1.0
**Created**: 2025-11-21
**Purpose**: Standardized metadata structure for tracking autonomous improvements

---

## Overview

This schema defines the metadata structure used across all steward improvements, ensuring consistent tracking, reporting, and portfolio demonstration capabilities.

---

## Core Metadata Fields

### Improvement Metadata

```json
{
  "improvement_id": "string (unique identifier)",
  "phase": "string (e.g., 'Phase 7', 'Phase 8')",
  "date": "ISO 8601 datetime",
  "agent": "string (agent type: steward, portfolio-steward, etc.)",
  "model": "string (claude model used)",
  "duration_minutes": "number",
  "status": "enum: completed | in_progress | failed | deferred",
  "success_rate": "number (0-100)",
  "breaking_changes": "number (target: 0)",
  "files_modified": "number",
  "files_created": "number",
  "files_deleted": "number",
  "backups_created": "number",
  "rollbacks_required": "number",
  "validation_passed": "boolean"
}
```

### Work Package Metadata

```json
{
  "package_id": "string",
  "package_name": "string",
  "category": "string (e.g., 'documentation', 'code-quality', 'performance')",
  "priority": "enum: low | medium | high | critical",
  "risk_level": "enum: low | medium | high",
  "effort_minutes": "number (estimated)",
  "actual_minutes": "number (actual)",
  "items_count": "number",
  "items_completed": "number",
  "defer_reason": "string (if deferred)"
}
```

### Work Item Metadata

```json
{
  "item_id": "string",
  "package_id": "string (foreign key)",
  "title": "string",
  "description": "string",
  "file_path": "string",
  "lines_changed": "number",
  "improvement_type": "enum",
  "before_state": "string (description)",
  "after_state": "string (description)",
  "impact": "enum: low | medium | high",
  "metrics": {
    "performance_gain": "number (percentage)",
    "quality_improvement": "number (0-100)",
    "coverage_increase": "number (percentage)"
  }
}
```

### Decision Log Metadata

```json
{
  "decision_id": "string",
  "timestamp": "ISO 8601 datetime",
  "context": "string (what required the decision)",
  "options": ["string (option 1)", "string (option 2)", ...],
  "chosen_option": "string",
  "rationale": "string (why this option)",
  "trade_offs": "string (what was sacrificed)",
  "confidence": "number (0-100)"
}
```

---

## Improvement Types

Standard improvement type enumerations:

- `error-handling` - Adding try-catch, validation, error recovery
- `documentation` - JSDoc, README, inline comments
- `performance` - Optimization, caching, lazy loading
- `security` - Input validation, XSS prevention, CSP
- `accessibility` - ARIA labels, keyboard navigation, screen readers
- `testing` - Unit tests, integration tests, validation
- `code-quality` - Refactoring, linting, formatting
- `organization` - File structure, naming, categorization
- `configuration` - Schema, validation, documentation
- `integration` - Cross-file references, navigation, discovery

---

## Portfolio Metrics

Aggregated metrics for portfolio demonstration:

```json
{
  "portfolio_metrics": {
    "total_improvements": "number",
    "total_phases": "number",
    "total_duration_hours": "number",
    "success_rate_overall": "number (0-100)",
    "breaking_changes_total": "number (target: 0)",
    "files_improved": "number",
    "grade_progression": [
      {"phase": "Phase 1", "grade": "B", "score": 75},
      {"phase": "Phase 7", "grade": "A", "score": 96}
    ],
    "safety_record": {
      "backups_created": "number",
      "rollbacks_required": "number",
      "rollback_rate": "number (percentage)"
    }
  }
}
```

---

## File Storage Structure

Metadata files stored in `.steward-reports/metadata/`:

```
.steward-reports/
├── metadata/
│   ├── phases/
│   │   ├── phase_1_metadata.json
│   │   ├── phase_7_metadata.json
│   │   └── ...
│   ├── improvements/
│   │   ├── improvement_001.json
│   │   ├── improvement_002.json
│   │   └── ...
│   ├── decisions/
│   │   ├── decision_log_phase_7.json
│   │   └── ...
│   └── portfolio_summary.json
└── metadata-schema.md (this file)
```

---

## Usage Examples

### Example: Phase 7 Improvement Metadata

```json
{
  "improvement_id": "phase_7_001",
  "phase": "Phase 7",
  "date": "2025-11-21T10:50:00Z",
  "agent": "autonomous-steward",
  "model": "claude-sonnet-4.5",
  "duration_minutes": 40,
  "status": "completed",
  "success_rate": 100,
  "breaking_changes": 0,
  "files_modified": 5,
  "files_created": 1,
  "files_deleted": 0,
  "backups_created": 1,
  "rollbacks_required": 0,
  "validation_passed": true,
  "work_packages": [
    {
      "package_id": "pkg_documentation",
      "package_name": "Documentation Accuracy",
      "category": "documentation",
      "priority": "high",
      "risk_level": "low",
      "effort_minutes": 15,
      "actual_minutes": 12,
      "items_count": 3,
      "items_completed": 3,
      "defer_reason": null
    },
    {
      "package_id": "pkg_performance",
      "package_name": "Cathedral Performance",
      "category": "performance",
      "priority": "medium",
      "risk_level": "low",
      "effort_minutes": 25,
      "actual_minutes": 20,
      "items_count": 2,
      "items_completed": 2,
      "defer_reason": null
    }
  ],
  "decisions": [
    {
      "decision_id": "dec_001",
      "timestamp": "2025-11-21T10:30:00Z",
      "context": "Multiple strategies proposed for improvements",
      "options": [
        "Safety-First: Low-risk docs updates first",
        "Impact-First: High-impact cathedral optimization first",
        "Quick-Wins: Fastest ROI improvements"
      ],
      "chosen_option": "Consensus of 8 strategies: docs + cathedral + metadata",
      "rationale": "8 parallel strategy agents voted; majority consensus identified",
      "trade_offs": "Deferred complex error handling for dedicated run",
      "confidence": 95
    }
  ]
}
```

### Example: Portfolio Summary

```json
{
  "portfolio_summary": {
    "repository": "TheMatrix",
    "autonomous_development": true,
    "last_updated": "2025-11-21T11:00:00Z",
    "total_phases": 8,
    "total_improvements": 92,
    "total_duration_hours": 12.5,
    "success_rate": 100,
    "breaking_changes": 0,
    "current_grade": "A",
    "current_score": 96,
    "files_total": 323,
    "apps_total": 178,
    "categories_total": 12,
    "safety_metrics": {
      "backups_created": 70,
      "rollbacks_required": 0,
      "rollback_rate": 0,
      "validation_success_rate": 100
    },
    "progression": [
      {"phase": "Phase 1", "grade": "B-", "score": 70},
      {"phase": "Phase 2", "grade": "B", "score": 75},
      {"phase": "Phase 4", "grade": "A-", "score": 90},
      {"phase": "Phase 7", "grade": "A", "score": 95},
      {"phase": "Phase 8", "grade": "A", "score": 96}
    ]
  }
}
```

---

## Integration Guidelines

### For Steward Agents

When performing improvements:

1. **Start**: Create improvement metadata at beginning of run
2. **Track**: Record all changes to work packages and items
3. **Decide**: Log all decision points with rationale
4. **Complete**: Update metadata with final metrics
5. **Report**: Generate summary report referencing metadata

### For Portfolio Viewers

When showcasing work:

1. **Query**: Read portfolio_summary.json for overall stats
2. **Drill Down**: Access phase-specific metadata for details
3. **Visualize**: Create charts from progression data
4. **Demonstrate**: Show decision logs for autonomous capability proof

### For Future Agents

When continuing work:

1. **Context**: Read recent phase metadata for current state
2. **Learn**: Analyze decision logs for patterns
3. **Improve**: Use metrics to identify highest-impact areas
4. **Extend**: Add new metadata fields as needed

---

## Schema Evolution

### Version History

- **v1.0** (2025-11-21): Initial schema
  - Core improvement, package, item metadata
  - Decision logging structure
  - Portfolio summary format

### Future Enhancements

Planned additions:

- **Test Coverage Metadata** - Track test creation and coverage
- **Performance Benchmarks** - Before/after performance metrics
- **Security Scan Results** - Vulnerability tracking
- **Accessibility Scores** - WCAG compliance tracking
- **User Impact Metrics** - Download counts, usage stats

---

## Best Practices

### Metadata Completeness

✅ **Always include**:
- Timestamps (ISO 8601 format)
- Success/failure status
- Safety metrics (backups, rollbacks)
- Validation results
- Decision rationale

❌ **Avoid**:
- Partial metadata (complete or nothing)
- Missing timestamps
- Undocumented decisions
- Untracked file changes

### Consistency

- Use standard enumerations (don't invent new statuses)
- Follow naming conventions (snake_case for keys)
- Include units in metric names (minutes, percentage, etc.)
- Link related metadata (use foreign keys)

### Privacy

- Don't store sensitive data in metadata
- Don't include API keys or credentials
- Don't track personally identifiable information
- Metadata is for portfolio demonstration, not surveillance

---

## Validation

Example JSON Schema for validation (future implementation):

```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "type": "object",
  "required": ["improvement_id", "phase", "date", "agent", "status"],
  "properties": {
    "improvement_id": {"type": "string"},
    "phase": {"type": "string"},
    "date": {"type": "string", "format": "date-time"},
    "agent": {"type": "string"},
    "status": {
      "type": "string",
      "enum": ["completed", "in_progress", "failed", "deferred"]
    },
    "success_rate": {
      "type": "number",
      "minimum": 0,
      "maximum": 100
    },
    "breaking_changes": {
      "type": "number",
      "minimum": 0
    }
  }
}
```

---

## License

MIT License - Part of The Matrix framework

---

**Maintained by**: Autonomous Steward Agents
**Schema Version**: 1.0
**Last Updated**: 2025-11-21
