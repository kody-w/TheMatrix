#!/bin/bash

# Migration script to copy localFirstTools apps to Matrix/apps directory
# This preserves the local-first architecture while integrating with The Matrix

echo "Starting migration of localFirstTools apps to The Matrix..."

# Create apps directory structure
mkdir -p apps/ai-tools
mkdir -p apps/business
mkdir -p apps/development
mkdir -p apps/education
mkdir -p apps/games
mkdir -p apps/health
mkdir -p apps/media
mkdir -p apps/productivity
mkdir -p apps/utilities
mkdir -p apps/index-variants

# Copy all HTML applications
echo "Copying AI Tools..."
cp localFirstTools/apps/ai-tools/*.html apps/ai-tools/ 2>/dev/null || true

echo "Copying Business apps..."
cp localFirstTools/apps/business/*.html apps/business/ 2>/dev/null || true

echo "Copying Development apps..."
cp localFirstTools/apps/development/*.html apps/development/ 2>/dev/null || true

echo "Copying Education apps..."
cp localFirstTools/apps/education/*.html apps/education/ 2>/dev/null || true

echo "Copying Games..."
cp localFirstTools/apps/games/*.html apps/games/ 2>/dev/null || true

echo "Copying Health apps..."
cp localFirstTools/apps/health/*.html apps/health/ 2>/dev/null || true

echo "Copying Media apps..."
cp localFirstTools/apps/media/*.html apps/media/ 2>/dev/null || true

echo "Copying Productivity apps..."
cp localFirstTools/apps/productivity/*.html apps/productivity/ 2>/dev/null || true

echo "Copying Utilities..."
cp localFirstTools/apps/utilities/*.html apps/utilities/ 2>/dev/null || true

echo "Copying Index variants..."
cp localFirstTools/apps/index-variants/*.html apps/index-variants/ 2>/dev/null || true

# Copy the apps manifest
mkdir -p data/config
cp localFirstTools/data/config/utility_apps_config.json data/config/ 2>/dev/null || true

# Count migrated files
total=$(find apps -name "*.html" 2>/dev/null | wc -l)
echo ""
echo "✓ Migration complete!"
echo "✓ $total HTML applications copied to apps/ directory"
echo "✓ Apps manifest copied to data/config/"
echo ""
echo "Next steps:"
echo "1. Run this script: ./migrate-apps.sh"
echo "2. Create apps-gallery.html"
echo "3. Update index.html with gallery link"
echo "4. Push to GitHub Pages"
