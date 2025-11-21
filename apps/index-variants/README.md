# Index Variants Collection

This directory contains 7 alternative versions of the main index.html gateway, optimized for different deployment scenarios and platforms.

## Variants

**index_MAC_local.html**
- Optimized for macOS local development
- Local file access enabled
- Development tools integrated
- Performance monitoring

**index_MAC.html**
- macOS deployment version
- Production-ready configuration
- Optimized asset loading
- Platform-specific features

**index_slim_cloud.html**
- Lightweight cloud deployment
- Minimal dependencies
- Fast loading time
- CDN-optimized

**index_slim_cloud_tools.html**
- Cloud version with development tools
- Debug console included
- Performance metrics
- Error tracking

**index_slim_cloud_qr.html**
- Cloud version with QR code generator
- Easy mobile access
- Share via QR code
- Cross-device testing

**index_slim.html**
- Minimal version for embedded use
- Smallest file size
- Essential features only
- Fast loading

## Usage

### Choosing a Variant

**Local Development**: Use `index_MAC_local.html`
- Full development tools
- Local file access
- Debug capabilities

**Production Cloud**: Use `index_slim_cloud.html`
- Optimized performance
- CDN-ready
- Production-stable

**Mobile Testing**: Use `index_slim_cloud_qr.html`
- QR code generation
- Easy device access
- Cross-platform testing

**Embedded/Widget**: Use `index_slim.html`
- Minimal footprint
- Fast loading
- Essential features

## Deployment

### Local
```bash
# Serve locally
python -m http.server 8000
# Open: http://localhost:8000/index_MAC_local.html
```

### Cloud (GitHub Pages)
```bash
# Use slim cloud variant as index.html
cp index_slim_cloud.html ../index.html
git commit -m "Deploy cloud variant"
git push origin main
```

### Custom Domain
All variants support custom domains. Configure in the variant file's settings.

## Customization

Each variant can be customized:
1. Edit the configuration section
2. Modify app lists and categories
3. Adjust styling and themes
4. Add custom integrations

## Performance

| Variant | Size | Load Time | Features |
|---------|------|-----------|----------|
| index_slim.html | ~20KB | <100ms | Essential |
| index_slim_cloud.html | ~35KB | <200ms | Standard |
| index_MAC_local.html | ~50KB | <300ms | Full |

---

**Total Variants**: 7
**Category**: Gateway Configurations
**Last Updated**: 2025-11-20
