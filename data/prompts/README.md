# Prompt Libraries

This directory contains comprehensive prompt libraries organized by category and use case. These prompts demonstrate The Matrix's orchestration capabilities and serve as examples for building your own AI-powered workflows.

## Overview

The Matrix framework includes a curated collection of prompts that showcase parallel agent orchestration across various domains: software development, content creation, data engineering, business automation, creative work, and more.

Each prompt is designed to trigger parallel orchestration workflows where The Matrix:
1. Discovers and analyzes the domain
2. Generates work breakdown structure
3. Spawns N agents in parallel
4. Integrates results into cohesive output

## Categories

### ESSENTIAL (10 prompts)
**Purpose**: Foundational orchestration patterns every developer should know

**Focus Areas**:
- Basic parallel execution
- Common development tasks
- Standard workflows
- Entry-level complexity

**Example Use Cases**:
- Component generation
- API endpoint creation
- Test suite building
- Documentation writing

### POWERFUL (10 prompts)
**Purpose**: Advanced orchestration for complex, real-world scenarios

**Focus Areas**:
- Multi-stage workflows
- Cross-domain integration
- Advanced patterns
- Production-scale systems

**Example Use Cases**:
- Microservices architecture
- Full-stack applications
- Data pipeline suites
- CI/CD automation

### ULTIMATE (10 prompts)
**Purpose**: Mind-blowing demonstrations of orchestration at massive scale

**Focus Areas**:
- Maximum complexity
- Impressive scale (100+ outcomes)
- Multiple orchestration layers
- Showcase capabilities

**Example Use Cases**:
- Complete SaaS platforms
- Enterprise systems
- Large-scale migrations
- Complex simulations

## Prompt Library Files

### prompt-library-essential.json
**Contains**: 10 foundational orchestration prompts
**Complexity**: Low to Medium
**Outcomes**: 10-50 artifacts per prompt
**Best For**: Learning the basics, building confidence

**Categories Included**:
- Software Development (4 prompts)
- Content Creation (2 prompts)
- Data Engineering (2 prompts)
- DevOps (2 prompts)

### prompt-library-powerful.json
**Contains**: 10 advanced orchestration prompts
**Complexity**: Medium to High
**Outcomes**: 50-100 artifacts per prompt
**Best For**: Production use cases, real projects

**Categories Included**:
- Full-Stack Development (3 prompts)
- Business Automation (2 prompts)
- Creative Production (2 prompts)
- Infrastructure (3 prompts)

### prompt-library-ultimate.json
**Contains**: 10 mind-blowing orchestration prompts
**Complexity**: Very High
**Outcomes**: 100-500+ artifacts per prompt
**Best For**: Demonstrations, showcases, ambitious projects

**Categories Included**:
- Enterprise Systems (3 prompts)
- Creative Universes (2 prompts)
- Knowledge Synthesis (2 prompts)
- Mega Migrations (3 prompts)

## Prompt Structure

Each prompt in the libraries follows this structure:

```json
{
  "id": "unique-identifier",
  "title": "Human-readable title",
  "category": "software-dev|content|data-eng|business|creative|devops|etc",
  "complexity": "low|medium|high|very-high",
  "estimatedOutcomes": 50,
  "estimatedTime": "5-10 minutes",
  "prompt": "The actual orchestration prompt...",
  "expectedWorkflow": {
    "discovery": "What to analyze",
    "packages": 10,
    "itemsPerPackage": 5,
    "totalOutcomes": 50,
    "integration": "What integrator creates"
  },
  "tags": ["api", "backend", "microservices"],
  "requiredContext": "Description of what project context is needed",
  "outcomes": "Description of what gets generated"
}
```

## How to Use Prompts

### Method 1: Direct Copy-Paste

1. Open the appropriate prompt library file
2. Find the prompt you want to use
3. Copy the `prompt` field value
4. Paste into Claude Code conversation
5. The Matrix orchestrator will handle the rest

### Method 2: Customization

1. Select a prompt that's close to your needs
2. Copy the prompt text
3. Modify details for your specific project:
   - Change domain/technology
   - Adjust scale (N packages, M items)
   - Add specific requirements
   - Include project-specific context
4. Submit to Claude Code

### Method 3: Combination

1. Select multiple prompts from different categories
2. Combine elements from each
3. Create a custom multi-stage workflow
4. Execute sequentially or in phases

## Prompt Categories Explained

### Software Development
Build code artifacts: components, APIs, services, tests, etc.

**Examples**:
- "Generate 50 React components for my design system"
- "Create 100 REST API endpoints for microservices"
- "Build comprehensive test suite with 200 test cases"

### Content Creation
Generate written content: articles, documentation, pages, etc.

**Examples**:
- "Write 50 blog articles for my SaaS marketing"
- "Create 100 documentation pages for my product"
- "Generate 75 landing pages for multi-product site"

### Data Engineering
Build data pipelines, transformations, warehouses, etc.

**Examples**:
- "Generate 50 ETL pipelines for data warehouse"
- "Create 100 data transformation scripts"
- "Build complete data lake architecture"

### Business Automation
Automate business processes and workflows.

**Examples**:
- "Generate 50 workflow automations for operations"
- "Create 100 business process templates"
- "Build complete automation suite for sales"

### Creative Production
Generate creative assets and content at scale.

**Examples**:
- "Create 200 character profiles for fantasy world"
- "Generate 150 story scenarios for game"
- "Build 100 visual designs for brand"

### DevOps & Infrastructure
Build infrastructure, deployment, and operations tooling.

**Examples**:
- "Generate 50 Terraform modules for AWS"
- "Create 100 CI/CD pipeline configurations"
- "Build complete Kubernetes deployment suite"

## Complexity Levels

### Low Complexity
- **Outcomes**: 10-25
- **Packages**: 3-5
- **Items Per Package**: 3-5
- **Time**: 2-5 minutes
- **Best For**: Quick wins, learning, simple projects

### Medium Complexity
- **Outcomes**: 25-75
- **Packages**: 5-10
- **Items Per Package**: 5-8
- **Time**: 5-15 minutes
- **Best For**: Real projects, production use

### High Complexity
- **Outcomes**: 75-150
- **Packages**: 10-15
- **Items Per Package**: 7-10
- **Time**: 15-30 minutes
- **Best For**: Ambitious projects, complex systems

### Very High Complexity
- **Outcomes**: 150-500+
- **Packages**: 15-50
- **Items Per Package**: 10-20
- **Time**: 30-60+ minutes
- **Best For**: Enterprise systems, demonstrations, showcases

## Adding New Prompts

To add prompts to the libraries:

### 1. Choose the Right Category

Determine complexity level based on:
- Number of outcomes
- Integration complexity
- Domain knowledge required
- Time to execute

### 2. Write the Prompt

Follow this template:

```
Generate [N × M] [artifacts] for [project type].

Context:
[Describe the project domain, tech stack, requirements]

Structure:
Create [N] [packages/categories] with [M] [items] each:

[Package 1]: [Description]
  - [Item 1]
  - [Item 2]
  - ...

[Package 2]: [Description]
  - [Item 1]
  - ...

Requirements:
- [Requirement 1]
- [Requirement 2]
- [Integration requirement]

Success Criteria:
- [Criterion 1]
- [Criterion 2]
```

### 3. Test the Prompt

1. Run the prompt through The Matrix
2. Verify all outcomes generated
3. Check integration works
4. Validate quality and consistency

### 4. Add Metadata

Complete all metadata fields:
- `id`: Unique identifier (kebab-case)
- `title`: Clear, descriptive title
- `category`: Match existing categories
- `complexity`: Based on testing
- `estimatedOutcomes`: Actual count from testing
- `estimatedTime`: Measured execution time
- `tags`: 3-5 relevant tags
- `requiredContext`: What project info is needed
- `outcomes`: Clear description of results

### 5. Submit

Add to appropriate library file and test integration.

## Prompt Selection Guide

### For Learning
Start with **ESSENTIAL** category:
- Lower complexity
- Clear patterns
- Quick results
- Build confidence

### For Production
Use **POWERFUL** category:
- Real-world scale
- Production quality
- Complete integrations
- Proven patterns

### For Demonstrations
Choose **ULTIMATE** category:
- Impressive scale
- Complex workflows
- Showcase capabilities
- Maximum impact

## Advanced Techniques

### Multi-Stage Prompts

Combine multiple prompts sequentially:

```
Stage 1: Generate 50 API endpoints (ESSENTIAL)
Stage 2: Generate 50 tests for endpoints (ESSENTIAL)
Stage 3: Generate API documentation (POWERFUL)
Stage 4: Generate integration suite (POWERFUL)
```

### Nested Orchestration

Use orchestration output as input for next level:

```
Level 1: Generate 10 microservices (POWERFUL)
Level 2: For each service, generate 10 endpoints (ESSENTIAL)
Level 3: For each endpoint, generate 5 tests (ESSENTIAL)
Total: 10 × 10 × 5 = 500 artifacts
```

### Cross-Domain Orchestration

Combine prompts from different domains:

```
Software: Generate backend API (POWERFUL)
Content: Generate API documentation (ESSENTIAL)
DevOps: Generate deployment config (ESSENTIAL)
Result: Complete, documented, deployable system
```

## Performance Tips

### Optimize Prompt Clarity
- Be specific about requirements
- Include technical details upfront
- Specify integration needs
- Define success criteria clearly

### Right-Size Outcomes
- Start smaller, scale up
- Test with 10-25 outcomes first
- Increase to 50-100 for production
- Use 100+ for demonstrations

### Leverage Caching
- Reuse patterns across prompts
- Reference previous work
- Build on existing systems
- Maintain consistency

## Troubleshooting

### Prompt Not Working?

**Check**:
- Is project context sufficient?
- Are requirements clear?
- Is scale too ambitious?
- Are dependencies specified?

**Solutions**:
- Add more discovery context
- Clarify requirements
- Reduce N or M values
- Specify integration needs

### Outcomes Inconsistent?

**Check**:
- Are patterns documented?
- Is system analysis included?
- Are standards specified?
- Is validation defined?

**Solutions**:
- Add pattern analysis step
- Document technical standards
- Include example outcomes
- Define validation criteria

### Integration Failing?

**Check**:
- Are dependencies clear?
- Is structure specified?
- Are integration points defined?

**Solutions**:
- Map dependencies explicitly
- Specify directory structure
- Define integration requirements
- Include routing/navigation needs

## Future Enhancements

Planned improvements to prompt libraries:

- **Industry-Specific Prompts**: Healthcare, finance, education, etc.
- **Language-Specific Prompts**: Python, JavaScript, Go, Rust, etc.
- **Framework-Specific Prompts**: React, Vue, Angular, Django, etc.
- **Platform-Specific Prompts**: AWS, Azure, GCP, Kubernetes, etc.
- **AI-Generated Prompts**: Meta-prompt for generating custom prompts
- **Prompt Validation**: Automated testing of prompt quality
- **Prompt Analytics**: Track usage, success rates, performance

## Contributing

To contribute new prompts:

1. Follow the prompt structure guidelines
2. Test thoroughly before submitting
3. Document complexity and requirements
4. Add comprehensive metadata
5. Include usage examples
6. Submit via pull request

## Support

For questions about using prompts or adding new ones:
- See main Matrix documentation
- Review example workflows
- Check troubleshooting guide
- Open issue in repository

---

**Use these prompts to unleash The Matrix's full orchestration power!**
