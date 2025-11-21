# Auto-Discovery Scripts

## Overview

This system automatically discovers and registers **demos** and **apps** without manual configuration file editing.

## Demo Auto-Discovery System

This system automatically discovers and registers demos without manual configuration file editing.

### How It Works

1. **Add metadata to your demo HTML file** (in the `<head>` section):

```html
<!-- Demo Metadata (for auto-discovery) -->
<meta name="demo:id" content="my-awesome-demo">
<meta name="demo:title" content="My Awesome Demo">
<meta name="demo:description" content="A brief description of what this demo does">
<meta name="demo:tags" content="Tag 1, Tag 2, Tag 3">
<meta name="demo:status" content="ready">
<meta name="demo:statusLabel" content="LIVE">
```

2. **Run the generator script**:

```bash
# Python (no dependencies)
python3 scripts/generate-demos-config.py

# OR Node.js (requires jsdom)
# npm install jsdom
# node scripts/generate-demos-config.js
```

3. **Demos automatically appear** in the Matrix interface!

### Metadata Fields

| Field | Required | Description | Example |
|-------|----------|-------------|---------|
| `demo:id` | ✅ Yes | Unique identifier | `"pokemon-battle-assistant"` |
| `demo:title` | ✅ Yes | Display name | `"Pokemon Battle Assistant"` |
| `demo:description` | ❌ No | What the demo does | `"Interactive battle assistant..."` |
| `demo:tags` | ❌ No | Comma-separated tags | `"Interactive Demo, Pure HTML"` |
| `demo:status` | ❌ No | Status: `ready` or `coming-soon` | `"ready"` |
| `demo:statusLabel` | ❌ No | Badge text | `"LIVE"` or `"COMING SOON"` |

### Status Options

- **Ready/Live Demo**:
  ```html
  <meta name="demo:status" content="ready">
  <meta name="demo:statusLabel" content="LIVE">
  ```
  Shows green badge, opens demo when clicked

- **Coming Soon**:
  ```html
  <meta name="demo:status" content="coming-soon">
  <meta name="demo:statusLabel" content="COMING SOON">
  ```
  Shows gray badge, displays "coming soon" modal when clicked

### Complete Example

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>My Awesome Demo</title>

    <!-- Demo Metadata (for auto-discovery) -->
    <meta name="demo:id" content="my-awesome-demo">
    <meta name="demo:title" content="My Awesome Demo">
    <meta name="demo:description" content="An amazing interactive demonstration of cool features">
    <meta name="demo:tags" content="Interactive Demo, Pure HTML/CSS/JS">
    <meta name="demo:status" content="ready">
    <meta name="demo:statusLabel" content="LIVE">

    <style>
        /* Your styles */
    </style>
</head>
<body>
    <!-- Your demo content -->
</body>
</html>
```

### Adding a New Demo - Zero Manual Config

1. Create your demo HTML file anywhere in the project
2. Add the demo metadata tags to the `<head>` section
3. Run `python3 scripts/generate-demos-config.py`
4. Refresh the Matrix interface - your demo appears automatically!

### Automation Options

#### Git Hook (Auto-run on commit)

Add to `.git/hooks/pre-commit`:

```bash
#!/bin/bash
python3 scripts/generate-demos-config.py
git add data/config/demos_config.json
```

Make executable: `chmod +x .git/hooks/pre-commit`

#### VS Code Task

Add to `.vscode/tasks.json`:

```json
{
  "label": "Regenerate Demos Config",
  "type": "shell",
  "command": "python3 scripts/generate-demos-config.py",
  "problemMatcher": []
}
```

#### npm script

Add to `package.json`:

```json
{
  "scripts": {
    "demos": "python3 scripts/generate-demos-config.py"
  }
}
```

Run: `npm run demos`

### Scanned Directories

The script scans these paths by default:
- `apps/games/pokemon/`
- `apps/games/`
- `apps/`
- `.` (root directory)

To customize, edit the `DEMO_PATHS` array in the script.

### Notes

- **DO NOT manually edit** `data/config/demos_config.json` - it will be overwritten
- The script skips `node_modules`, `.git`, `archive`, and `.steward-backups`
- Files are discovered recursively in scanned directories
- Only HTML files with `demo:id` metadata are included
- Demos are automatically sorted alphabetically by title

---

## App Auto-Discovery System

This system automatically discovers ALL apps in the `apps/` directory.

### How It Works

**No metadata tags required!** The script automatically scans all HTML files in:
- `apps/ai-tools/`
- `apps/business/`
- `apps/development/`
- `apps/education/`
- `apps/games/`
- `apps/health/`
- `apps/media/`
- `apps/productivity/`
- `apps/utilities/`
- `apps/index-variants/`

### Run the Generator

```bash
python3 scripts/generate-apps-config.py
```

### Optional: Add Metadata for Better Info

You can optionally add metadata to your app HTML files:

```html
<!-- App Metadata (optional) -->
<meta name="app:id" content="my-awesome-app">
<meta name="app:title" content="My Awesome App">
<meta name="app:description" content="What this app does">
<meta name="app:tags" content="tag1, tag2, tag3">
<meta name="app:icon" content="🚀">
<meta name="app:category" content="games">
```

If no metadata is found, the script uses:
- **ID**: filename
- **Title**: extracted from `<title>` tag or filename
- **Description**: "A [category] application"
- **Icon**: default emoji based on category
- **Tags**: [category]

### Adding a New App - Zero Configuration

1. **Drop your HTML file** anywhere in `apps/`
2. **Run the generator**: `python3 scripts/generate-apps-config.py`
3. **Refresh browser** - app appears automatically!

### Automation

The git pre-commit hook automatically runs both generators:
- `generate-demos-config.py`
- `generate-apps-config.py`

So every commit auto-updates both configs!
