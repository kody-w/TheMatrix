# Contributing to The Matrix

Thank you for your interest in contributing to The Matrix AI orchestration framework! This document provides guidelines for contributing code, documentation, and ideas.

## Code of Conduct

Be respectful, inclusive, and constructive. We're building something amazing together.

## Ways to Contribute

### 1. Report Issues
- Bug reports
- Feature requests
- Documentation improvements
- Performance issues

### 2. Submit Code
- New agents
- Bug fixes
- New applications
- Framework improvements

### 3. Improve Documentation
- Fix typos and errors
- Add examples
- Write tutorials
- Create guides

### 4. Share Ideas
- Propose new features
- Suggest improvements
- Share use cases
- Provide feedback

## Getting Started

### Prerequisites
- Git installed
- Modern web browser
- Text editor or IDE
- Basic understanding of HTML/CSS/JavaScript (for app development)
- Understanding of AI orchestration concepts (for agent development)

### Fork and Clone

```bash
# Fork the repository on GitHub
# Then clone your fork
git clone https://github.com/YOUR_USERNAME/TheMatrix.git
cd TheMatrix

# Add upstream remote
git remote add upstream https://github.com/ORIGINAL_OWNER/TheMatrix.git
```

## Development Workflow

### 1. Create a Branch

```bash
# Create a feature branch
git checkout -b feature/your-feature-name

# Or a bug fix branch
git checkout -b fix/issue-description
```

### 2. Make Changes

Follow the project structure:
- **Apps**: Place in appropriate `apps/` subdirectory
- **Agents**: Create in `.claude/agents/`
- **Documentation**: Add to `docs/` with proper categorization
- **Configuration**: Update relevant JSON files

### 3. Test Your Changes

#### For Applications:
- Test in multiple browsers (Chrome, Firefox, Safari)
- Verify mobile responsiveness
- Check accessibility features
- Validate all functionality

#### For Agents:
- Test agent execution
- Verify output quality
- Check error handling
- Validate integrations

#### For Documentation:
- Check markdown formatting
- Verify all links work
- Test code examples
- Review for clarity

### 4. Commit Changes

Use clear, descriptive commit messages:

```bash
# Good commit messages
git commit -m "Add Pokemon team builder application"
git commit -m "Fix navigation bug in apps-gallery.html"
git commit -m "Update CLAUDE.md with error handling examples"

# Follow conventional commits format
# type(scope): description
# Types: feat, fix, docs, style, refactor, test, chore
git commit -m "feat(apps): add quantum physics simulator"
git commit -m "fix(agents): resolve parallel execution issue"
git commit -m "docs(guides): add integration cookbook examples"
```

### 5. Push and Create Pull Request

```bash
# Push to your fork
git push origin feature/your-feature-name

# Create pull request on GitHub
# Provide clear description of changes
# Reference any related issues
```

## Code Standards

### HTML Applications

```html
<!-- Include descriptive header comment -->
<!--
  Application: Pokemon Battle Assistant
  Purpose: Help trainers build optimal Pokemon teams
  Author: Your Name
  Date: 2025-11-20
  Dependencies: None (local-first)
-->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Descriptive Title</title>
    <!-- Additional meta tags for SEO and accessibility -->
</head>
<body>
    <!-- Semantic HTML structure -->
    <!-- Accessibility attributes (aria-labels, etc.) -->
    <!-- Responsive design -->
</body>
</html>
```

### JavaScript Style

```javascript
// Use modern ES6+ syntax
// Clear variable names
// Document complex logic
// Handle errors gracefully

const calculateOptimalTeam = (pokemon, constraints) => {
    try {
        // Implementation
        return team;
    } catch (error) {
        console.error('Team calculation failed:', error);
        return null;
    }
};
```

### Agent Development

Agents are defined in `.claude/agents/` with YAML frontmatter:

```markdown
---
name: your-agent
description: Clear description of agent purpose
tools: Read, Write, Edit, Bash, Task
model: haiku
---

# Agent Name

## Purpose
Clear statement of what this agent does

## Input
What information the agent receives

## Output
What the agent produces

## Process
Step-by-step workflow
```

## Documentation Standards

### Markdown Format

```markdown
# Main Title (H1 - only one per document)

## Section (H2)

### Subsection (H3)

Use **bold** for emphasis, *italic* for terms.

Code blocks with language:
```javascript
const example = "with syntax highlighting";
```

Links: [Description](URL)
Images: ![Alt text](path/to/image.png)
```

### Documentation Structure

- **README files**: Overview, features, usage, support
- **Guides**: Step-by-step instructions with examples
- **Reference**: Complete API/configuration documentation
- **Tutorials**: Learning-focused with explanations

## Agent Contribution Guidelines

### Creating New Agents

1. **Define Purpose**: What specific task does the agent handle?
2. **Specify Tools**: What tools does the agent need?
3. **Document Process**: Step-by-step agent workflow
4. **Provide Examples**: Show agent in action
5. **Test Thoroughly**: Verify agent works as expected

### Agent Template

```markdown
---
name: your-agent-name
description: One-line description (< 100 characters)
tools: Read, Write, Edit, Glob, Grep, Bash, Task
model: haiku
---

# Your Agent Name

## Purpose
[Clear statement of agent's role in orchestration]

## When to Use
[Scenarios where this agent is appropriate]

## Input Requirements
[What information the agent needs to start]

## Process
1. [Step 1]
2. [Step 2]
3. [Step 3]

## Output Format
[What the agent produces]

## Success Criteria
[How to validate agent completed successfully]

## Examples
[Real examples of agent usage]
```

## Application Contribution Guidelines

### Application Checklist

- [ ] Descriptive filename (lowercase, hyphens)
- [ ] Header comment explaining purpose
- [ ] Responsive design (mobile, tablet, desktop)
- [ ] Accessibility features (keyboard nav, aria-labels)
- [ ] Error handling for edge cases
- [ ] Local-first architecture (no external dependencies if possible)
- [ ] Tested in multiple browsers
- [ ] README entry added (if new category)

### Application Categories

Place applications in the appropriate directory:
- `apps/ai-tools/` - AI development and deployment
- `apps/business/` - Sales, marketing, enterprise
- `apps/development/` - Developer tools
- `apps/education/` - Educational applications
- `apps/games/` - Interactive games
- `apps/health/` - Wellness applications
- `apps/media/` - Creative tools
- `apps/productivity/` - Task and time management
- `apps/utilities/` - General utilities

## Pull Request Process

### Before Submitting

1. **Update Documentation**: Add/update relevant docs
2. **Test Thoroughly**: Verify all functionality
3. **Check Style**: Follow code standards
4. **Rebase**: Keep commits clean
5. **Review Changes**: Self-review your code

### PR Description Template

```markdown
## Description
[Clear description of what this PR does]

## Type of Change
- [ ] Bug fix
- [ ] New feature
- [ ] Documentation update
- [ ] Code refactoring
- [ ] Performance improvement

## Related Issues
Fixes #[issue number]
Related to #[issue number]

## Testing
[How you tested these changes]

## Screenshots (if applicable)
[Add screenshots for UI changes]

## Checklist
- [ ] Code follows project standards
- [ ] Documentation updated
- [ ] Tested in multiple browsers
- [ ] Commits are clear and descriptive
```

### Review Process

1. **Automated Checks**: Code passes automated validation
2. **Manual Review**: Maintainer reviews code
3. **Feedback**: Address any requested changes
4. **Approval**: PR approved by maintainer
5. **Merge**: PR merged into main branch

## Community

### Getting Help

- **GitHub Issues**: Ask questions, report bugs
- **Discussions**: Share ideas, get feedback
- **Documentation**: Check docs first
- **Examples**: Review existing code

### Staying Updated

```bash
# Sync your fork with upstream
git fetch upstream
git checkout main
git merge upstream/main
git push origin main
```

## Recognition

Contributors are recognized in:
- GitHub contributor list
- Project documentation
- Release notes
- Community highlights

## License

By contributing, you agree that your contributions will be licensed under the same MIT License that covers the project. See [LICENSE](LICENSE) for details.

## Questions?

If you have questions about contributing:
1. Check this guide
2. Review existing contributions
3. Ask in GitHub Discussions
4. Open an issue for clarification

---

**Thank you for contributing to The Matrix!** Your contributions help make AI orchestration accessible and powerful for everyone.
