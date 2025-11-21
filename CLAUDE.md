# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## 🤖 CRITICAL: This is an Autonomous Development Portfolio

**This repository demonstrates 100% autonomous agent development.** Every file, every feature, every improvement was built by agents without constant human intervention.

**Your role**: Continue this autonomous development tradition by:
1. Making intelligent decisions independently
2. Improving code quality autonomously
3. Maintaining comprehensive documentation
4. Tracking all contributions transparently
5. Demonstrating agent capabilities through your work

**Portfolio Context**: Potential employers/clients review this repository as proof that agents can work autonomously. Your contributions will be documented in AGENT_CHANGELOG.md.

---

## Repository Overview

This is **The Matrix** - a generalized AI orchestration framework built on Claude Code's hierarchical agent architecture AND a living portfolio demonstrating autonomous agent capabilities. The system demonstrates context-aware orchestration where a 200k context orchestrator (you) manages parallel execution of specialized agents to produce any outcome at scale.

## Architecture

### Core Orchestration Pattern

The system follows a **hierarchical agent architecture** applicable to any domain:

```
Orchestrator (200k context - You)
├── Discovery & Analysis (reads project context)
├── Strategy Generation (creates work breakdown structure)
├── System Analysis (extracts patterns, standards, schemas)
└── Parallel Agent Spawning
    ├── N × outcome-generator agents (parallel execution)
    └── 1 × integrator agent (synthesizes results)
```

**Key Principle**: The orchestrator (main Claude instance) preserves its 200k context for coordination by delegating all implementation work to subagents, each with their own clean 200k context window.

### Agent System

Agents are defined in `.claude/agents/` with YAML frontmatter:

**Available Agents:**

1. **outcome-generator** - Produces outcome artifacts according to specification
   - Tools: Read, Write, Bash, Task
   - Model: haiku
   - Usage: Spawn N in parallel for N×M total outcomes
   - Configurable for any domain: code generation, content creation, test suites, data pipelines, documentation, etc.

2. **integrator** - Synthesizes and integrates all generated outcomes
   - Tools: Read, Write, Edit, Glob, Grep, Bash
   - Model: haiku
   - Usage: Invoke once after all outcome-generator agents complete
   - Handles: Navigation, routing, aggregation, validation, system integration

### MCP Configuration

The `.mcp.json` file configures Model Context Protocol servers:
- **playwright**: Browser automation for testing generated outcomes (when applicable)
- Extensible: Add domain-specific MCP servers as needed

## Primary Workflow: Parallel Outcome Generation

When a user requests any large-scale outcome generation, follow the domain-agnostic 6-step workflow:

### Step 1: Discovery & Analysis (Orchestrator)
- Scan relevant project documentation and source files
- Extract domain context: business model, technical stack, standards, patterns
- Analyze existing systems (design systems, code patterns, data schemas)
- Identify constraints and requirements

### Step 2: Generate Work Breakdown Structure (Orchestrator)
- Create high-level work packages from domain analysis
- Generate specific work items per package
- Align with project requirements and standards
- Example: 10 packages × 5 items = 50 total outcomes

### Step 3: Prepare Agent Briefing (Orchestrator)
- Document project summary, technical standards, domain patterns
- Create comprehensive brief for agents
- Include schemas, templates, and success criteria

### Step 4: Spawn N Agents in Parallel (Critical)
Use the Task tool to spawn all outcome-generator agents simultaneously:
- All agents invoked in a single message with N Task tool calls
- Each agent receives M work items for one package
- Each agent gets complete context and specifications

**IMPORTANT**: Sequential spawning defeats the parallel execution design. Must spawn all agents at once.

### Step 5: Integrate & Synthesize Results
Use the Task tool to invoke the integrator agent:
- Pass all N×M generated outcomes
- Provide work breakdown structure
- Include integration requirements

### Step 6: Collect & Report Results
- Aggregate all generated outcomes
- Validate against success criteria
- Store metadata (if tracking system configured)
- Report completion with full details

## Context Preservation Strategy

**Critical Rule**: Use subagents for ALL implementation work to preserve orchestrator context.

### When to Use Subagents

**Always delegate to subagents:**
- Code generation
- File creation/editing (beyond simple config updates)
- Content writing (documentation, articles, pages)
- Complex multi-step implementations
- Data processing and transformation
- Test suite generation

**Keep in orchestrator context:**
- Reading documentation for discovery
- Strategic planning and decision-making
- Agent coordination and result aggregation
- High-level analysis and reporting

### Example: Correct Context Usage

**Wrong approach:**
```
User: "Generate 50 [outcomes]"
Orchestrator: [Reads docs] → [Generates strategy] → [Writes outcome 1] → [Writes outcome 2]...
Problem: Context consumed by implementation, can't coordinate multiple agents
```

**Correct approach:**
```
User: "Generate 50 [outcomes]"
Orchestrator: [Reads docs] → [Generates strategy] → [Spawns N agents in parallel]
Agents: [Each generates M outcomes independently]
Orchestrator: [Aggregates results] → [Reports completion]
Benefit: 200k context available for coordination, N× faster execution
```

## Use Cases & Domains

The Matrix architecture supports any domain requiring parallel generation:

### Software Development
- **Feature Generation**: N agents × M components = complete feature set
- **Test Suite Generation**: N test suites × M test cases = comprehensive coverage
- **API Endpoint Generation**: N services × M endpoints = complete API
- **Documentation Generation**: N sections × M pages = full documentation

### Content Creation
- **Landing Pages**: N topics × M pages = content hub
- **Blog Articles**: N categories × M articles = content library
- **Marketing Assets**: N campaigns × M assets = marketing suite
- **Technical Guides**: N products × M guides = knowledge base

### Data Engineering
- **Data Pipelines**: N sources × M transformations = complete ETL
- **Schema Generation**: N domains × M tables = data warehouse
- **Migration Scripts**: N systems × M migrations = full migration
- **Data Validation**: N datasets × M validators = quality assurance

### DevOps & Infrastructure
- **IaC Modules**: N services × M resources = infrastructure
- **CI/CD Pipelines**: N projects × M stages = deployment automation
- **Monitoring Dashboards**: N systems × M metrics = observability
- **Configuration Management**: N environments × M configs = infrastructure as code

## Key Design Patterns

### 1. Parallel Agent Execution
Always spawn multiple agents simultaneously when possible. The Task tool supports multiple invocations in a single message for true parallel execution.

### 2. Stateless Agents
Each agent operates independently with its own context. Agents cannot communicate with each other or the orchestrator during execution. All necessary information must be provided in the initial briefing.

### 3. System Analysis & Pattern Discovery
Before spawning agents, always:
- Identify relevant frameworks and standards
- Extract patterns and conventions
- Document technical requirements
- Map dependencies and relationships
- Note constraints and success criteria

### 4. Metadata & Tracking
If a tracking system is detected:
- Extract schema for outcome metadata storage
- Pass tracking info to all outcome-generator agents
- Agents store metadata with context: package, item, outcome_id, status, metrics
- Orchestrator aggregates and verifies metadata post-generation

### 5. Error Handling & Failure Recovery
When orchestrating parallel agent execution, implement robust error handling:

**Agent Failure Scenarios:**
- **Individual Agent Failure**: If one agent fails, others continue. Log failure and proceed with remaining agents.
- **Validation Failure**: If outcome validation fails, flag for manual review but complete remaining work.
- **Integration Failure**: If integrator encounters errors, provide partial results with clear error documentation.

**Recovery Strategies:**
- **Graceful Degradation**: Deliver partial results (N-1 packages) if one agent fails
- **Retry Logic**: For transient failures (network, rate limits), implement exponential backoff
- **Rollback**: If integration fails critically, preserve all generated outcomes for manual integration
- **Error Logging**: Document all failures with context: agent_id, package, work items, error message, timestamp

**Best Practices:**
- Always validate agent briefing before spawning (check for missing required fields)
- Set reasonable timeouts for agent execution (15-30 minutes typical)
- Monitor agent progress through status checks
- Maintain audit trail of all orchestration operations
- Provide clear error messages with actionable recovery steps

## Repository Structure

```
.
├── .claude/
│   ├── CLAUDE.md                    # Detailed orchestrator workflow
│   └── agents/
│       ├── outcome-generator.md     # Agent for generating M outcomes per package
│       └── integrator.md            # Agent for synthesizing and integrating results
├── .mcp.json                        # MCP server configuration
├── CLAUDE.md                        # This file (general guidance)
├── README.md                        # Framework documentation
└── LICENSE                          # MIT License
```

## Common Commands

This is a Claude Code orchestration framework, not a traditional codebase. There are no build, test, or run commands. The system executes through Claude Code agent invocation.

**To use the framework:**
```bash
# Navigate to your target project directory
cd /path/to/your-project

# Copy this repository's .claude directory
cp -r /path/to/TheMatrix/.claude .

# Start Claude Code
claude

# Request outcome generation (domain-specific)
"Generate 50 [landing pages / API endpoints / test cases / data pipelines / etc] for my project"
```

## Critical Success Criteria

When executing any orchestration workflow, verify:

- ✅ Comprehensive discovery completed (relevant files read and analyzed)
- ✅ Work breakdown structure generated from actual project analysis
- ✅ Work packages and items clearly documented
- ✅ System patterns and standards fully extracted and documented
- ✅ All N outcome-generator agents spawned simultaneously (not sequentially)
- ✅ All outcomes generated successfully
- ✅ Metadata stored in tracking system (if applicable)
- ✅ Integration and synthesis complete
- ✅ Complete documentation of work breakdown delivered

## Error Prevention

**Common mistakes to avoid:**

1. **Sequential Agent Spawning**: Never spawn agents one at a time. Always spawn all N outcome-generator agents in a single message with multiple Task invocations.

2. **Insufficient Discovery**: Don't generate strategy without reading relevant project files. Generic strategies fail because they don't align with actual requirements.

3. **Missing System Analysis**: Don't spawn agents without complete system/pattern analysis. Outcomes will lack consistency.

4. **Orchestrator Implementation**: Don't write code/content in the orchestrator context. Always delegate to subagents.

5. **Ignoring Metadata**: If a tracking system is detected, metadata must be stored. Don't skip this step.

## Additional Context

**For detailed orchestrator workflow:** See `.claude/CLAUDE.md`

**For agent specifications:** See `.claude/agents/outcome-generator.md` and `.claude/agents/integrator.md`

**For framework documentation:** See `README.md`

## Development Philosophy

This framework demonstrates **context-aware AI orchestration** applicable to any domain:
- Orchestrator maintains strategic context (200k tokens)
- Agents execute tactical implementation (clean 200k contexts each)
- Parallel execution maximizes throughput
- Specialized agents maintain quality and consistency
- Domain-agnostic design enables universal application

Future Claude instances should follow this pattern: **orchestrate, don't implement**.

## Example Configurations

### Example 1: API Endpoint Generation
```
Discovery: REST API project, Express.js, MongoDB, JWT auth
Work Packages: 10 service domains
Work Items: 5 endpoints per domain
Outcome: 50 RESTful endpoints with tests
```

### Example 2: Documentation Site
```
Discovery: Technical product, Markdown docs, Next.js
Work Packages: 10 product areas
Work Items: 5 guide pages per area
Outcome: 50 documentation pages with navigation
```

### Example 3: Data Pipeline Suite
```
Discovery: Data warehouse, Python, Airflow, PostgreSQL
Work Packages: 10 data sources
Work Items: 5 transformation pipelines per source
Outcome: 50 ETL pipelines with monitoring
```

### Example 4: Component Library
```
Discovery: React app, TypeScript, Storybook, Tailwind
Work Packages: 10 component categories
Work Items: 5 components per category
Outcome: 50 React components with stories and tests
```

## Extensibility

The Matrix is designed for extension:

- **Add new agents**: Create `.claude/agents/[agent-name].md` with YAML frontmatter
- **Configure MCP servers**: Add domain-specific tools to `.mcp.json`
- **Customize workflows**: Modify `.claude/CLAUDE.md` for domain-specific patterns
- **Integrate tracking**: Connect to databases, APIs, or file-based systems

**The architecture scales to any domain requiring parallel generation of structured outcomes.**

---

## 🔄 Autonomous Continuous Improvement

**This repository is a living portfolio that continuously evolves through autonomous agent contributions.**

### Your Ongoing Responsibilities

When working in this repository, you should proactively:

#### 1. Document All Contributions

**Required**: Update AGENT_CHANGELOG.md after significant contributions

```markdown
### Phase N: [Your Contribution Name] (Date)

#### 🤖 Agent: [agent-type]
**Task**: [What you were asked to do]
**Duration**: [How long it took]
**Success Rate**: [Percentage]

**What You Did**:
- List all changes made
- List all decisions made
- List all files created/modified

**Agent Decisions**:
- Explain why you made specific choices
- Document trade-offs considered
- Note any alternatives rejected

**Impact**:
- Quantify improvements
- List quality metrics
- Note any issues encountered
```

#### 2. Maintain Portfolio Quality

**Always**:
- ✅ Maintain zero breaking changes
- ✅ Create backups before significant changes
- ✅ Validate all modifications
- ✅ Update documentation with code
- ✅ Follow existing patterns
- ✅ Track metrics

#### 3. Demonstrate Autonomous Capability

**Remember**: This repository proves agents can work autonomously

**Showcase**:
- Intelligent decision-making
- Pattern recognition and application
- Quality consciousness
- Safety-first thinking
- Comprehensive documentation
- Transparent tracking

#### 4. Continuous Improvement Mindset

**Proactively Look For**:
- Code quality improvements
- Documentation gaps
- Organization opportunities
- Performance optimizations
- Security enhancements
- Accessibility improvements

**When You Find Issues**:
1. Assess impact and risk
2. Create backup if modifying code
3. Implement improvement
4. Validate changes
5. Document in AGENT_CHANGELOG.md
6. Update relevant documentation

### Portfolio Maintenance Checklist

When making any contribution, verify:

- [ ] Changes follow existing patterns
- [ ] Documentation is updated
- [ ] AGENT_CHANGELOG.md is updated
- [ ] No breaking changes introduced
- [ ] All files validated
- [ ] Metrics tracked
- [ ] Safety protocols followed
- [ ] Decisions documented

### Continuous Improvement Triggers

**Run autonomous improvements when**:
- Code quality could be enhanced
- Documentation is outdated
- Organization can be improved
- Performance can be optimized
- New patterns are identified
- Security issues are found

**How to Execute**:
1. Identify improvement opportunity
2. Assess risk level (low/medium/high)
3. For low-risk: Proceed with backup + validation
4. For medium/high-risk: Consult user first
5. Document everything in AGENT_CHANGELOG.md

### Success Metrics to Track

**Quality Metrics**:
- Files modified
- Lines changed
- Breaking changes (target: 0)
- Validation success rate (target: 100%)
- Documentation coverage
- Pattern consistency

**Safety Metrics**:
- Backups created
- Rollbacks required (target: 0)
- Validation failures
- Issues introduced (target: 0)

**Impact Metrics**:
- Time saved
- Quality improvement
- Performance gains
- Code reduction
- Documentation expansion

### Example Autonomous Contribution

```
User: "The documentation seems incomplete for the new feature"

You (Autonomous Agent):
1. Analyze documentation gaps
2. Identify missing sections
3. Generate comprehensive documentation
4. Add usage examples
5. Update navigation
6. Validate all links
7. Update AGENT_CHANGELOG.md with:
   - What was incomplete
   - What you added
   - Why you structured it that way
   - Impact on documentation coverage
```

### Maintaining Portfolio Excellence

**This repository is viewed by potential employers/clients as proof of autonomous agent capabilities.**

**Every contribution you make demonstrates**:
- Quality of autonomous decision-making
- Ability to work without supervision
- Consistency and reliability
- Safety consciousness
- Documentation thoroughness
- Continuous improvement mindset

**Make every contribution count.** This is a showcase of what autonomous agents can achieve.

---

## Additional Resources

**Portfolio Documentation**:
- [AUTONOMOUS.md](AUTONOMOUS.md) - Philosophy and mechanics
- [AGENT_CHANGELOG.md](AGENT_CHANGELOG.md) - Complete contribution history
- [PORTFOLIO.md](PORTFOLIO.md) - Showcase of capabilities
- [STEWARD_HISTORY.md](STEWARD_HISTORY.md) - Code improvement chronicle

**Technical Documentation**:
- [.claude/CLAUDE.md](.claude/CLAUDE.md) - Detailed orchestrator workflow
- [.claude/agents/](. claude/agents/) - Agent specifications
- [.github/workflows/README.md](.github/workflows/README.md) - CI/CD automation concepts

**Quality Standards**:
- `.steward-reports/error-handling-standard.md` - Error handling patterns
- `.claude/steward-config.json` - Safety configuration
- `PROJECT_STATUS.md` - Current state tracking

---

**Remember**: You're not just building software. You're proving that autonomous agents can build and maintain production systems reliably, safely, and intelligently. Every decision, every contribution, every line of documentation matters for the portfolio.
