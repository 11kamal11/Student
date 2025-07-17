#!/usr/bin/env python3
"""
Simple script to check if the Odoo module is properly structured
"""

import os
import ast

def check_module():
    print("=== Odoo Module Structure Check ===")
    
    # Check manifest file
    if not os.path.exists('__manifest__.py'):
        print("❌ __manifest__.py is missing!")
        return False
    
    try:
        with open('__manifest__.py', 'r') as f:
            manifest = ast.literal_eval(f.read())
        print("✅ __manifest__.py syntax is valid")
        
        # Check required fields
        required_fields = ['name', 'version', 'depends', 'installable']
        for field in required_fields:
            if field in manifest:
                print(f"✅ {field}: {manifest[field]}")
            else:
                print(f"❌ Missing required field: {field}")
        
        # Check installable flag
        if manifest.get('installable', False):
            print("✅ Module is marked as installable")
        else:
            print("❌ Module is NOT marked as installable")
            
        # Check application flag
        if manifest.get('application', False):
            print("✅ Module is marked as application")
        else:
            print("ℹ️  Module is not marked as application")
            
    except Exception as e:
        print(f"❌ Error parsing __manifest__.py: {e}")
        return False
    
    # Check __init__.py
    if os.path.exists('__init__.py'):
        print("✅ __init__.py exists")
    else:
        print("❌ __init__.py is missing!")
        return False
    
    # Check models directory
    if os.path.exists('models') and os.path.isdir('models'):
        print("✅ models directory exists")
        if os.path.exists('models/__init__.py'):
            print("✅ models/__init__.py exists")
        else:
            print("❌ models/__init__.py is missing!")
            return False
    else:
        print("❌ models directory is missing!")
        return False
    
    # Check data files
    data_files = manifest.get('data', [])
    print(f"\nChecking {len(data_files)} data files...")
    for data_file in data_files:
        if os.path.exists(data_file):
            print(f"✅ {data_file}")
        else:
            print(f"❌ {data_file} - FILE NOT FOUND!")
            return False
    
    print("\n=== Module Structure Check Complete ===")
    return True

if __name__ == "__main__":
    success = check_module()
    if success:
        print("\n🎉 Module structure looks good!")
        print("\nIf the module is still not visible in Odoo Apps:")
        print("1. Restart Odoo server")
        print("2. Update Apps List (Apps → Update Apps List)")
        print("3. Check if the module directory is in Odoo's addons path")
        print("4. Enable Developer Mode")
        print("5. Check Odoo logs for errors")
    else:
        print("\n❌ Module structure has issues that need to be fixed!")
