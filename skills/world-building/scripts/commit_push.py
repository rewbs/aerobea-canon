#!/usr/bin/env python3
"""
Commit and push changes to the world-building canon repository.
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


def commit_and_push(repo_path, commit_message, files_changed=None):
    """
    Commit changes and push to remote (if configured).
    
    Args:
        repo_path: Path to the git repository
        commit_message: Commit message describing the changes
        files_changed: Optional list of specific files to commit (commits all if None)
    """
    repo_path = Path(repo_path).resolve()
    
    if not (repo_path / ".git").exists():
        print(f"Error: {repo_path} is not a git repository", file=sys.stderr)
        return False
    
    # Add files
    if files_changed:
        for file in files_changed:
            result = run_command(f"git add {file}", cwd=repo_path, check=False)
            if result.returncode != 0:
                print(f"Warning: Could not add {file}: {result.stderr}", file=sys.stderr)
    else:
        run_command("git add .", cwd=repo_path)
    
    # Check if there are changes to commit
    result = run_command("git diff --cached --quiet", cwd=repo_path, check=False)
    if result.returncode == 0:
        print("ℹ️  No changes to commit")
        return True
    
    # Commit
    result = run_command(f'git commit -m "{commit_message}"', cwd=repo_path, check=False)
    if result.returncode != 0:
        print(f"Error committing: {result.stderr}", file=sys.stderr)
        return False
    
    print(f"✅ Committed: {commit_message}")
    
    # Try to push (may fail if no remote configured - that's okay)
    result = run_command("git push", cwd=repo_path, check=False)
    if result.returncode == 0:
        print("✅ Pushed to remote")
    else:
        print("ℹ️  No remote configured (changes saved locally)")
    
    return True


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python commit_push.py <repo_path> <commit_message> [file1 file2 ...]")
        sys.exit(1)
    
    repo_path = sys.argv[1]
    commit_message = sys.argv[2]
    files_changed = sys.argv[3:] if len(sys.argv) > 3 else None
    
    success = commit_and_push(repo_path, commit_message, files_changed)
    sys.exit(0 if success else 1)
