#!/usr/bin/env python3
"""
lint.py - Layer dependency enforcer for src/ directory.

This linter verifies:
1. Every source file lives inside a layer directory
2. Imports respect the forward dependency direction
3. No file exceeds 300 lines

Layer dependency chain: types → config → repo → service → runtime → ui
Cross-cutting: providers may import from types, config, utils, providers
Leaf: utils may only import from utils (nothing internal)
"""

import ast
import os
import sys
from pathlib import Path
from typing import List, Tuple, Set

# Layer order (forward dependency direction)
LAYERS = ['types', 'config', 'repo', 'service', 'runtime', 'ui', 'providers', 'utils']
LAYER_INDEX = {layer: idx for idx, layer in enumerate(LAYERS)}

# Allowed imports per layer
ALLOWED_IMPORTS = {
    'types': {'types'},
    'config': {'types', 'config'},
    'repo': {'types', 'config', 'repo'},
    'service': {'types', 'config', 'repo', 'providers', 'service'},
    'runtime': {'types', 'config', 'repo', 'service', 'providers', 'runtime'},
    'ui': {'types', 'config', 'service', 'runtime', 'providers', 'ui'},
    'providers': {'types', 'config', 'utils', 'providers'},
    'utils': {'utils'},
}

MAX_LINES = 300
SRC_DIR = Path('/workspace/pong-duel-6241/src')


def get_layer(filepath: Path) -> str:
    """Get the layer name for a file path."""
    parts = filepath.relative_to(SRC_DIR).parts
    if len(parts) > 0:
        return parts[0]
    return ''


def get_imports(filepath: Path) -> List[str]:
    """Extract import statements from a Python file."""
    imports = []
    try:
        with open(filepath, 'r') as f:
            tree = ast.parse(f.read(), filename=str(filepath))
        
        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                for alias in node.names:
                    imports.append(alias.name.split('.')[0])
            elif isinstance(node, ast.ImportFrom):
                if node.module:
                    imports.append(node.module.split('.')[0])
    except SyntaxError as e:
        print(f"  Syntax error in {filepath}: {e}")
    return imports


def check_line_count(filepath: Path) -> Tuple[bool, str]:
    """Check if file exceeds MAX_LINES."""
    with open(filepath, 'r') as f:
        lines = f.readlines()
    if len(lines) > MAX_LINES:
        return False, f"File has {len(lines)} lines (max {MAX_LINES})"
    return True, ""


def check_imports(filepath: Path) -> List[str]:
    """Check if imports respect layer dependencies."""
    errors = []
    layer = get_layer(filepath)
    imports = get_imports(filepath)
    
    allowed = ALLOWED_IMPORTS.get(layer, set())
    
    for imp in imports:
        # Skip standard library and external imports (not in our layers)
        if imp not in LAYERS:
            continue
        
        if imp not in allowed:
            errors.append(f"Import '{imp}' not allowed from layer '{layer}'")
    
    return errors


def find_all_source_files() -> List[Path]:
    """Find all Python files under src/."""
    source_files = []
    if not SRC_DIR.exists():
        return source_files
    
    for root, _, files in os.walk(SRC_DIR):
        for file in files:
            if file.endswith('.py'):
                source_files.append(Path(root) / file)
    
    return source_files


def lint() -> bool:
    """Run all linter checks. Returns True if all checks pass."""
    all_passed = True
    source_files = find_all_source_files()
    
    if not source_files:
        print("No source files found under src/")
        return True
    
    print(f"Linting {len(source_files)} source file(s)...\n")
    
    for filepath in source_files:
        layer = get_layer(filepath)
        
        # Verify file is in a layer directory
        if layer not in LAYERS:
            print(f"FAIL: {filepath} is not in a recognized layer directory")
            all_passed = False
            continue
        
        # Check line count
        ok, msg = check_line_count(filepath)
        if not ok:
            print(f"FAIL: {filepath}: {msg}")
            all_passed = False
        
        # Check imports
        import_errors = check_imports(filepath)
        for error in import_errors:
            print(f"FAIL: {filepath}: {error}")
            all_passed = False
    
    if all_passed:
        print("All checks passed!")
    else:
        print("\nSome checks failed. Fix the issues above.")
    
    return all_passed


if __name__ == '__main__':
    success = lint()
    sys.exit(0 if success else 1)
