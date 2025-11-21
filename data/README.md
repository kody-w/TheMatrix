# Data Directory

This directory contains all data files, configurations, and resources used throughout The Matrix framework.

## Directory Structure

```
data/
├── README.md (this file)
├── prompts/          # Prompt libraries and templates
├── configs/          # Configuration files
├── schemas/          # Data schemas and validation rules
└── resources/        # Static resources and assets
```

## Subdirectories

### prompts/
**Purpose**: Centralized storage for all prompt libraries and templates used by agents and orchestration workflows.

**Contents**:
- Prompt libraries organized by category (ESSENTIAL, POWERFUL, ULTIMATE, etc.)
- Agent instruction templates
- Workflow prompt sequences
- Meta-orchestration prompts

**Usage**: Agents and orchestrator reference these prompts for various tasks. Prompts are tagged with metadata for easy discovery and selection.

See [prompts/README.md](./prompts/README.md) for detailed documentation.

### configs/
**Purpose**: Configuration files for The Matrix framework components.

**Contents**:
- Agent configurations
- MCP server settings
- Application preferences
- Environment-specific configs

**Usage**: Load configurations at runtime to customize behavior without modifying code.

### schemas/
**Purpose**: Data validation schemas and structural definitions.

**Contents**:
- JSON schemas for data validation
- API response schemas
- Database schemas
- File format specifications

**Usage**: Validate data integrity and ensure consistency across components.

### resources/
**Purpose**: Static assets and resources used by applications.

**Contents**:
- Images and icons
- Fonts and stylesheets
- Data files (JSON, CSV, etc.)
- Media assets

**Usage**: Reference these resources in HTML apps and tools.

## Data Management Guidelines

### Adding New Data

1. **Choose the Right Subdirectory**
   - Prompts → `prompts/`
   - Configuration → `configs/`
   - Validation rules → `schemas/`
   - Static files → `resources/`

2. **Follow Naming Conventions**
   - Use lowercase with hyphens: `my-data-file.json`
   - Include version numbers if applicable: `schema-v2.json`
   - Be descriptive: `pokemon-battle-data.json` not `data1.json`

3. **Document Your Data**
   - Add inline comments where supported (JSONC, YAML)
   - Update this README with new subdirectories
   - Include schema documentation

### Data Formats

**Preferred Formats**:
- **Configuration**: JSON or YAML
- **Structured Data**: JSON or CSV
- **Text Data**: Markdown or plain text
- **Binary Data**: Minimize; prefer text formats when possible

**Format Guidelines**:
- Use 2-space indentation for JSON/YAML
- Validate all JSON files before committing
- Include UTF-8 encoding for text files
- Compress large binary files

### Version Control

- **Include**: Schema files, configurations, small data files
- **Exclude**: Generated data, large binary files, sensitive data
- **Track Changes**: Document breaking changes to schemas/configs
- **Migrations**: Provide migration scripts for schema updates

## Data Usage Patterns

### In HTML Applications

```javascript
// Load data from resources
fetch('/data/resources/pokemon-data.json')
  .then(response => response.json())
  .then(data => {
    // Use data
  });
```

### In Agent Workflows

Agents read data files during discovery phase:
- Scan `data/prompts/` for prompt libraries
- Load `data/configs/` for configuration
- Reference `data/schemas/` for validation

### In Orchestration

Orchestrator uses data for:
- Prompt selection and composition
- Configuration-driven agent spawning
- Schema validation of outputs
- Resource provisioning

## Data Security

### Sensitive Data

**Never commit**:
- API keys and secrets
- Personal information
- Credentials
- Private configurations

**Instead**:
- Use environment variables
- Reference external secure storage
- Use `.gitignore` for sensitive files
- Provide example configs (`.example` suffix)

### Example Configuration Pattern

```
# In repository
config.example.json   ← Template with placeholders

# In .gitignore
config.json           ← Actual config (not committed)
```

## Data Optimization

### File Size Guidelines

- **Small** (<100KB): Include directly in repository
- **Medium** (100KB-1MB): Evaluate necessity, consider compression
- **Large** (>1MB): Use external storage, link via URL

### Performance Considerations

- **Lazy Loading**: Load data only when needed
- **Caching**: Cache frequently accessed data
- **Chunking**: Split large datasets into chunks
- **Compression**: Use gzip for large text files

## Data Validation

### Schema Validation

All data files should have corresponding schemas:

```
data/
├── resources/
│   └── pokemon-data.json          ← Data file
└── schemas/
    └── pokemon-data.schema.json   ← Validation schema
```

### Validation Tools

Use JSON Schema validators:
```bash
# Validate data against schema
ajv validate -s schema.json -d data.json
```

## Backup and Recovery

### Steward Backups

The steward agent creates backups in `.steward-backups/` before making changes to data files.

**Retention**: 50 most recent backups
**Location**: `.steward-backups/`
**Restoration**: Copy backup to original location

### Manual Backups

For critical data:
1. Create timestamped copies before major changes
2. Store in `data/backups/` (excluded from git)
3. Document backup contents

## Data Migration

### Schema Updates

When updating schemas:
1. Create new schema version: `schema-v2.json`
2. Write migration script: `migrate-v1-to-v2.js`
3. Update all data files
4. Test thoroughly
5. Document breaking changes

### Data Transformation

Provide transformation utilities:
```javascript
// transform-data.js
function transformV1ToV2(oldData) {
  // Transformation logic
  return newData;
}
```

## Integration with Apps

### Pokemon Apps

Pokemon tools reference data files for:
- Pokemon base stats
- Move databases
- Type effectiveness charts
- Meta rankings

### Development Tools

Development apps use data for:
- Code templates
- Configuration presets
- Tool settings

### AI Tools

AI tools load prompts and configs:
- Prompt libraries from `prompts/`
- Model configurations
- Processing rules

## Contribution Guidelines

When adding data to this directory:

1. **Validate Format**: Ensure valid JSON/YAML/CSV
2. **Add Documentation**: Update this README
3. **Include Schema**: Provide validation schema if applicable
4. **Optimize Size**: Compress or externalize large files
5. **Test Integration**: Verify apps can load and use the data

## Future Enhancements

Planned improvements:
- Automated data validation in CI/CD
- Data versioning system
- Schema migration tools
- Data compression pipeline
- CDN integration for large files
- Data analytics and usage tracking

## Support

For questions about data organization or format, see the main Matrix documentation or create an issue in the repository.

---

**Keep data organized, validated, and optimized for the best Matrix experience!**
