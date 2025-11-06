#!/usr/bin/env python3
"""
Initialize a git repository for world-building canon.
"""

import subprocess
import sys
from pathlib import Path


def run_command(cmd, cwd=None, check=True):
    """Run a shell command and return the result."""
    result = subprocess.run(
        cmd,
        shell=True,
        capture_output=True,
        text=True,
        cwd=cwd,
        check=check
    )
    return result


def init_repo(repo_path):
    """Initialize a git repository with the proper structure."""
    repo_path = Path(repo_path).resolve()
    
    # Create directory if it doesn't exist
    repo_path.mkdir(parents=True, exist_ok=True)
    
    # Initialize git
    result = run_command("git init", cwd=repo_path)
    if result.returncode != 0:
        print(f"Error initializing git: {result.stderr}", file=sys.stderr)
        return False
    
    # Configure git user (required for commits)
    run_command('git config user.name "Saul"', cwd=repo_path)
    run_command('git config user.email "saul@worldbuilding.local"', cwd=repo_path)
    
    # Create directory structure
    directories = [
        "countries",
        "figures", 
        "events",
        "relations"
    ]
    
    for dir_name in directories:
        (repo_path / dir_name).mkdir(exist_ok=True)
    
    # Create README
    readme_content = """# World-Building Canon Repository

This repository contains the canonical lore for Saul's imaginary countries.

## Structure

- `countries/` - Individual country files with comprehensive details
- `figures/` - Biographies of significant historical figures
- `events/` - Major historical events and timelines
- `relations/` - International relations and treaties

## Usage

This repository is maintained collaboratively by Saul and Claude using the world-building skill.
All changes are validated for internal consistency before being committed to canon.
"""
    
    (repo_path / "README.md").write_text(readme_content)
    
    # Create .gitignore
    gitignore_content = """# Editor files
*.swp
*.swo
*~
.DS_Store

# Temporary files
*.tmp
"""
    
    (repo_path / ".gitignore").write_text(gitignore_content)
    
    # Initial commit
    run_command("git add .", cwd=repo_path)
    run_command('git commit -m "Initial commit: Repository structure"', cwd=repo_path)
    
    print(f"✅ Repository initialized at {repo_path}")
    print(f"📁 Created directories: {', '.join(directories)}")
    return True


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python init_repo.py <repo_path>")
        sys.exit(1)
    
    repo_path = sys.argv[1]
    success = init_repo(repo_path)
    sys.exit(0 if success else 1)
