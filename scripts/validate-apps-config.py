#!/usr/bin/env python3

"""
Validates and cleans utility_apps_config.json by removing entries with non-existent files

Usage: python3 scripts/validate-apps-config.py
"""

import os
import json
from pathlib import Path

# Configuration
PROJECT_ROOT = Path(__file__).parent.parent
CONFIG_FILE = PROJECT_ROOT / 'data' / 'config' / 'utility_apps_config.json'

def validate_and_clean_config():
    """Remove apps with non-existent files from config"""

    print("🔍 Validating apps config...\n")

    # Load config
    with open(CONFIG_FILE, 'r', encoding='utf-8') as f:
        config = json.load(f)

    original_count = len(config['apps'])
    valid_apps = []
    removed_apps = []

    # Check each app
    for app in config['apps']:
        app_path = PROJECT_ROOT / app['path'].lstrip('./')

        if app_path.exists():
            valid_apps.append(app)
        else:
            removed_apps.append(app)
            print(f"❌ Removed: {app['title']} (path: {app['path']})")

    # Update config with only valid apps
    config['apps'] = valid_apps

    # Save cleaned config
    with open(CONFIG_FILE, 'w', encoding='utf-8') as f:
        json.dump(config, f, indent=2, ensure_ascii=False)

    print(f"\n✅ Validation complete!")
    print(f"📊 Original: {original_count} apps")
    print(f"📊 Removed: {len(removed_apps)} apps")
    print(f"📊 Valid: {len(valid_apps)} apps")
    print(f"\n✅ Updated {CONFIG_FILE}")

if __name__ == '__main__':
    validate_and_clean_config()
