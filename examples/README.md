# Examples & Demonstrations

This directory contains working examples demonstrating The Matrix orchestration framework's capabilities across different domains.

## Directory Structure

### `/html-demos/` - Interactive HTML Demonstrations

Fully functional, standalone HTML applications showcasing parallel generation capabilities.

#### Pokemon Battle Assistant Suite
- **pokemon-battle-assistant-v2.html** - Advanced battle management system
- **pokemon-battle-assistant-original.html** - Original implementation
- **pokemon-browser.html** - Pokemon data browser
- **iv-calculator.html** - Individual Values calculator
- **team-builder.html** - Team composition optimizer
- **battle-simulator.html** - Battle simulation engine
- **training-mode.html** - Training progress tracker
- **type-chart.html** - Type effectiveness reference
- **move-database.html** - Comprehensive move database
- **rankings-enhanced.html** - Pokemon rankings system

#### Meta Demonstrations
- **windows95-emulator.html** - Nostalgic Windows 95 interface (1MB+ of pure local-first code)
- **meta-dashboard.html** - Orchestration visualization and metrics
- **advanced-tools.html** - Advanced utility toolkit

**All demos are:**
- Pure HTML/CSS/JavaScript (no dependencies)
- Fully functional offline
- Self-contained with embedded data
- Production-ready examples

### `/prompts/` - JSON Prompt Collections

Ready-to-use orchestration prompts organized by category and use case.

- **ULTIMATE_MIND_BLOWERS.json** - Top 10 most impressive orchestration scenarios
- **BUSINESS_IMPACT_PROMPTS.json** - Business-focused use cases
- **prompts-user-experience.json** - User experience scenarios
- **creative-prompts.json** - Creative and innovative use cases
- **SCALE_FIRST_PROMPTS.json** - Scale-oriented orchestration patterns

**Prompt Format:**
```json
{
  "prompts": [
    {
      "id": "unique-id",
      "title": "Descriptive Title",
      "description": "What this orchestration does",
      "prompt": "The actual prompt text",
      "category": "domain",
      "complexity": "high|medium|low",
      "estimatedTime": "15-30 minutes",
      "outcomes": "N×M outcomes description"
    }
  ]
}
```

## How to Use Examples

### Running HTML Demos

1. Navigate to any HTML file in `/html-demos/`
2. Open directly in your browser (no server required)
3. All functionality works offline
4. Explore features and interactions

Example:
```bash
open examples/html-demos/pokemon-battle-assistant-v2.html
```

### Using Prompt Collections

1. Browse prompts in `/prompts/` directory
2. Select a prompt matching your use case
3. Copy the prompt text
4. Provide to Claude Code with your project context
5. The Matrix will orchestrate parallel generation

Example workflow:
```bash
# In Claude Code
"Use this prompt: [paste from ULTIMATE_MIND_BLOWERS.json]"
```

## Example Use Cases by Domain

### Software Development
See: Pokemon Battle Assistant suite (10+ interconnected tools)
- Demonstrates: Component generation, state management, API design
- Outcome: Complete feature-rich application suite

### Interactive Experiences
See: Windows 95 Emulator
- Demonstrates: UI generation, nostalgic recreation, attention to detail
- Outcome: 1MB+ self-contained application

### Data Visualization
See: Meta Dashboard
- Demonstrates: Real-time visualization, metrics tracking
- Outcome: Interactive orchestration monitoring

## Integration with Main Repository

These examples complement the core framework:

- **Framework Core**: [../.claude/](../.claude/) - Agent system and orchestration
- **Documentation**: [../docs/](../docs/) - Guides and references
- **Generated Infrastructure**: [../agent-ecosystem/](../agent-ecosystem/) - Full platform example

## Learning Path

1. **Explore Demos**: Open HTML files to see end results
2. **Study Prompts**: Review JSON files to understand inputs
3. **Read Briefings**: Check [../docs/briefings/](../docs/briefings/) for how these were orchestrated
4. **Apply Patterns**: Use insights for your own projects

## Contributing Examples

To add new examples:

1. **HTML Demos**: Add self-contained HTML to `/html-demos/`
   - Must work offline
   - Include inline styles and scripts
   - Document features clearly

2. **Prompts**: Add to appropriate JSON in `/prompts/`
   - Follow existing format
   - Include metadata (category, complexity, outcomes)
   - Test prompt before adding

3. **Document**: Update this README with new additions

---

**These examples prove The Matrix's capabilities across domains. Build on them to create your own orchestration workflows.**
