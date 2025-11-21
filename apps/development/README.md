# Development Tools Collection

This directory contains 15 specialized development tools for building, testing, and deploying web applications and AI agents.

## Applications

### Code & Artifact Management

**artifact-converter.html**
- Convert between code artifact formats
- Transform Claude artifacts to standalone apps
- Export in multiple formats (HTML, React, Vue)
- Batch conversion support

**cdn-file-manager.html**
- Manage files on CDN services
- Upload, organize, and version assets
- Preview files before deployment
- Generate CDN URLs

**github-sync-manager.html**
- Synchronize local files with GitHub
- Commit and push directly from browser
- Branch management interface
- Conflict resolution tools

**github-gallery-setup.html**
- Set up GitHub Pages galleries
- Auto-generate navigation
- Deploy static sites quickly
- Configure custom domains

### Browser-Based Development

**local-browser.html**
- Local file browser and editor
- Test HTML/CSS/JS locally
- Live preview and hot reload
- Debug console integration

**browser-vm-app.html**
- Run lightweight VMs in browser
- Test across environments
- Sandboxed execution
- Resource monitoring

**browser-vm-docker.html**
- Docker container management from browser
- Build and run containers
- Interactive terminal access
- Container orchestration

**browser-vm-azure-function.html**
- Deploy and test Azure Functions
- Local development environment
- Function trigger simulator
- Log monitoring and debugging

### News & Content Aggregation

**azure-vm-hackernews.html**
- Hacker News reader optimized for Azure VMs
- Curated tech news feed
- Save articles for later
- Discuss with team

**azure-vm-hackernews-backup.html**
- Backup version with offline support
- Cached articles for slow connections
- Alternative UI layout

### Iframe & Embedding Tools

**iframe-tunneler-7.html**
- Advanced iframe embedding toolkit
- Cross-origin communication
- Security sandbox configuration
- Version 7 with latest features

**iframe-tunneler-10.html**
- Latest iframe tunneling technology
- Enhanced security protocols
- Performance optimizations
- WebSocket support

### Documentation & Visualization

**mermaid-viewer.html**
- Render Mermaid diagrams
- Interactive diagram editor
- Export diagrams as images
- Embed in documentation

### Educational Resources

**claude-subagents-tutorial.html**
- Learn Claude Code subagent patterns
- Step-by-step examples
- Interactive code playground
- Best practices guide

**claude-subagents-tutorial-continued.html**
- Advanced agent orchestration
- Complex workflow patterns
- Production deployment strategies
- Troubleshooting guide

## Key Features

### Common Capabilities
- **Local-first**: Work offline when possible
- **Browser-based**: No installation required
- **Responsive**: Works on all screen sizes
- **Fast**: Optimized performance
- **Secure**: Sandboxed execution

### Integration Points
- GitHub API integration
- Azure services connectivity
- CDN provider support
- Docker runtime access
- Claude Code API

## Usage

### Getting Started
1. Open any tool in a modern web browser
2. Grant necessary permissions (file access, etc.)
3. Follow the tool-specific setup wizard
4. Start developing!

### Common Workflows

**Local Development**:
```
1. Open local-browser.html
2. Load your project files
3. Edit code with live preview
4. Test in browser sandbox
5. Deploy with github-sync-manager.html
```

**CI/CD Pipeline**:
```
1. Write code locally
2. Convert artifacts with artifact-converter.html
3. Test in browser-vm-docker.html
4. Deploy with github-sync-manager.html
5. Monitor with azure-vm-hackernews.html
```

**Documentation**:
```
1. Create diagrams in mermaid-viewer.html
2. Set up gallery with github-gallery-setup.html
3. Sync with github-sync-manager.html
4. Serve via CDN with cdn-file-manager.html
```

## Technical Stack

### Frontend Technologies
- HTML5, CSS3, JavaScript (ES6+)
- Web Components for modularity
- Service Workers for offline support
- IndexedDB for local storage

### API Integrations
- GitHub REST API v3
- Azure Functions SDK
- Docker Engine API
- Claude Code API
- Various CDN providers

### Development Tools
- CodeMirror for code editing
- Monaco Editor integration
- Built-in JavaScript console
- Network request inspection

## Best Practices

### Security
- Never commit API keys to files
- Use environment variables
- Sandbox untrusted code
- Validate all user inputs

### Performance
- Minimize external dependencies
- Lazy-load heavy resources
- Cache frequently used data
- Optimize bundle sizes

### Workflow
- Use version control (Git)
- Test across browsers
- Document custom configurations
- Share reusable components

## Browser Compatibility

**Recommended**:
- Chrome/Edge 90+
- Firefox 88+
- Safari 14+

**Required Features**:
- ES6+ JavaScript support
- File System Access API (for some tools)
- Service Workers
- IndexedDB

## Troubleshooting

### Common Issues

**File Access Denied**:
- Grant browser file permissions
- Check CORS settings
- Use HTTPS when required

**API Rate Limits**:
- Implement caching strategies
- Use API keys for higher limits
- Space out API requests

**Performance Slow**:
- Close unnecessary browser tabs
- Clear browser cache
- Disable browser extensions
- Use hardware acceleration

## Support

**Framework Documentation**: `../../README.md`
**Contributing Guide**: `../../CONTRIBUTING.md`
**Quick Start**: `../../QUICK_START_GUIDE.md`

---

**Total Tools**: 15
**Category**: Development & Deployment
**Last Updated**: 2025-11-20
