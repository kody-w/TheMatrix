#!/usr/bin/env python3

"""
Auto-generates utility_apps_config.json by scanning HTML files for app metadata

Usage: python3 scripts/generate-apps-config.py

This script scans all HTML files in apps/ and looks for app metadata
in <meta> tags, then automatically generates data/config/utility_apps_config.json
"""

import os
import json
import re
from pathlib import Path
from datetime import datetime

# Configuration
PROJECT_ROOT = Path(__file__).parent.parent
OUTPUT_FILE = PROJECT_ROOT / 'data' / 'config' / 'utility_apps_config.json'
APPS_PATHS = [
    'apps/ai-tools',
    'apps/business',
    'apps/development',
    'apps/education',
    'apps/games',
    'apps/health',
    'apps/media',
    'apps/productivity',
    'apps/utilities',
    'apps/index-variants'
]

# Metadata keys to look for in HTML files
META_KEYS = {
    'appId': 'app:id',
    'appTitle': 'app:title',
    'appDescription': 'app:description',
    'appTags': 'app:tags',
    'appIcon': 'app:icon',
    'appCategory': 'app:category'
}

def extract_meta_content(html, meta_name):
    """Extract content from meta tag by name"""
    pattern = f'<meta\\s+name=["\']?{re.escape(meta_name)}["\']?\\s+content=["\']([^"\']+)["\']'
    match = re.search(pattern, html, re.IGNORECASE)
    if match:
        return match.group(1)

    # Try reverse order (content before name)
    pattern = f'<meta\\s+content=["\']([^"\']+)["\']\\s+name=["\']?{re.escape(meta_name)}["\']?'
    match = re.search(pattern, html, re.IGNORECASE)
    return match.group(1) if match else None


def extract_title_from_html(html):
    """Extract title from <title> tag as fallback"""
    match = re.search(r'<title>([^<]+)</title>', html, re.IGNORECASE)
    return match.group(1) if match else None


def extract_app_metadata(html_path, category):
    """Extract app metadata from HTML file"""
    try:
        with open(html_path, 'r', encoding='utf-8') as f:
            html = f.read()

        # Check if this file has app metadata
        app_id = extract_meta_content(html, META_KEYS['appId'])

        # If no explicit app metadata, use file name as ID
        if not app_id:
            app_id = Path(html_path).stem

        # Extract metadata
        title = extract_meta_content(html, META_KEYS['appTitle'])
        if not title:
            # Try to get from <title> tag
            title = extract_title_from_html(html)
            if not title:
                # Use file name as title
                title = Path(html_path).stem.replace('-', ' ').title()

        description = extract_meta_content(html, META_KEYS['appDescription'])
        if not description:
            description = f"A {category} application"

        tags_str = extract_meta_content(html, META_KEYS['appTags'])
        tags = [tag.strip() for tag in tags_str.split(',')] if tags_str else [category]

        icon = extract_meta_content(html, META_KEYS['appIcon'])
        if not icon:
            # Default icons by category
            icon_map = {
                'ai-tools': '🤖',
                'business': '💼',
                'development': '💻',
                'education': '🎓',
                'games': '🎮',
                'health': '❤️',
                'media': '📹',
                'productivity': '📋',
                'utilities': '🔧',
                'index-variants': '📄'
            }
            icon = icon_map.get(category, '📱')

        # Get relative path from project root
        rel_path = './' + os.path.relpath(html_path, PROJECT_ROOT).replace('\\', '/')

        metadata = {
            'id': app_id,
            'title': title,
            'description': description,
            'tags': tags,
            'path': rel_path,
            'icon': icon
        }

        return metadata

    except Exception as e:
        print(f"❌ Error processing {html_path}: {e}")
        return None


def scan_directory(directory, category):
    """Recursively scan directory for HTML files"""
    html_files = []

    if not os.path.exists(directory):
        return html_files

    for root, dirs, files in os.walk(directory):
        # Skip hidden directories
        dirs[:] = [d for d in dirs if not d.startswith('.')]

        for file in files:
            if file.endswith('.html'):
                html_files.append(os.path.join(root, file))

    return html_files


def generate_apps_config():
    """Generate apps config from all HTML files"""
    print("🔍 Scanning for app files...\n")

    apps = []
    categories = set()

    # Scan configured paths
    for app_path in APPS_PATHS:
        full_path = PROJECT_ROOT / app_path
        if not full_path.exists():
            continue

        # Extract category from path
        category = Path(app_path).name

        html_files = scan_directory(full_path, category)

        for html_file in html_files:
            metadata = extract_app_metadata(html_file, category)
            if metadata:
                apps.append(metadata)
                categories.add(category)
                print(f"✅ Found app: {metadata['title']} ({metadata['path']})")

    # Sort apps by title
    apps.sort(key=lambda x: x['title'])

    # Create config object
    config = {
        "$schema": "https://json-schema.org/draft-07/schema#",
        "$comment": "Auto-generated by scripts/generate-apps-config.py - DO NOT EDIT MANUALLY",
        "version": "2.0",
        "lastUpdated": datetime.now().isoformat(),
        "description": "Centralized registry of 100+ local-first HTML applications across 10 categories",
        "categories": sorted(list(categories)),
        "apps": apps
    }

    # Ensure output directory exists
    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)

    # Write config file
    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        json.dump(config, f, indent=2, ensure_ascii=False)

    print(f"\n✅ Generated {OUTPUT_FILE}")
    print(f"📊 Found {len(apps)} app(s) across {len(categories)} categories\n")

    return apps


if __name__ == '__main__':
    generate_apps_config()
