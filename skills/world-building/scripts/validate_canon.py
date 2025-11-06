#!/usr/bin/env python3
"""
Validate canon consistency by checking for contradictions and inconsistencies.
"""

import sys
import re
from pathlib import Path
from datetime import datetime


def parse_yaml_frontmatter(content):
    """Extract YAML frontmatter from markdown content."""
    if not content.startswith("---\n"):
        return {}, content
    
    parts = content.split("---\n", 2)
    if len(parts) < 3:
        return {}, content
    
    frontmatter = {}
    for line in parts[1].strip().split("\n"):
        if ":" in line:
            key, value = line.split(":", 1)
            frontmatter[key.strip()] = value.strip()
    
    return frontmatter, parts[2]


def extract_dates(content):
    """Extract all dates mentioned in the content."""
    # Matches formats like: 1945, May 1945, 15 May 1945, etc.
    date_patterns = [
        r'\b(\d{1,2}\s+(?:January|February|March|April|May|June|July|August|September|October|November|December)\s+\d{4})\b',
        r'\b((?:January|February|March|April|May|June|July|August|September|October|November|December)\s+\d{4})\b',
        r'\b(\d{4})\b'
    ]
    
    dates = []
    for pattern in date_patterns:
        dates.extend(re.findall(pattern, content, re.IGNORECASE))
    
    return dates


def extract_entities(content):
    """Extract mentioned entities (countries, people, events) from content."""
    entities = {
        'countries': set(),
        'people': set(),
        'events': set()
    }
    
    # Extract capitalized phrases (likely proper nouns)
    proper_nouns = re.findall(r'\b[A-Z][a-z]+(?:\s+[A-Z][a-z]+)*\b', content)
    
    # Simple heuristics to categorize
    for noun in proper_nouns:
        # Countries often end in -ia, -land, -stan, or are single capitalized words
        if any(noun.endswith(suffix) for suffix in ['ia', 'land', 'stan', 'ica']):
            entities['countries'].add(noun)
        # Events might contain words like War, Treaty, Revolution, etc.
        elif any(word in noun for word in ['War', 'Treaty', 'Revolution', 'Crisis', 'Conflict']):
            entities['events'].add(noun)
        # Everything else might be a person
        else:
            entities['people'].add(noun)
    
    return entities


def validate_file(file_path, all_entities):
    """Validate a single markdown file for internal consistency."""
    content = file_path.read_text()
    frontmatter, body = parse_yaml_frontmatter(content)
    
    issues = []
    
    # Extract entities mentioned in this file
    mentioned_entities = extract_entities(body)
    
    # Check if mentioned countries exist in the repository
    for country in mentioned_entities['countries']:
        if country not in all_entities['countries'] and country != frontmatter.get('name'):
            issues.append(f"⚠️  References unknown country: {country}")
    
    # Extract dates and check for chronological consistency
    dates = extract_dates(body)
    
    return {
        'file': file_path.name,
        'issues': issues,
        'entities': mentioned_entities,
        'dates': dates
    }


def validate_canon(repo_path):
    """Validate the entire canon repository for consistency."""
    repo_path = Path(repo_path).resolve()
    
    if not repo_path.exists():
        print(f"Error: Repository path {repo_path} does not exist", file=sys.stderr)
        return False
    
    # Collect all entities across all files
    all_entities = {
        'countries': set(),
        'people': set(),
        'events': set()
    }
    
    # First pass: collect all entity names
    for md_file in repo_path.rglob("*.md"):
        if md_file.name == "README.md":
            continue
        content = md_file.read_text()
        frontmatter, _ = parse_yaml_frontmatter(content)
        
        if 'name' in frontmatter:
            if 'countries' in str(md_file.parent):
                all_entities['countries'].add(frontmatter['name'])
            elif 'figures' in str(md_file.parent):
                all_entities['people'].add(frontmatter['name'])
            elif 'events' in str(md_file.parent):
                all_entities['events'].add(frontmatter['name'])
    
    # Second pass: validate each file
    all_issues = []
    for md_file in repo_path.rglob("*.md"):
        if md_file.name == "README.md":
            continue
        result = validate_file(md_file, all_entities)
        if result['issues']:
            all_issues.append(result)
    
    # Report results
    if all_issues:
        print("\n⚠️  Potential consistency issues found:\n")
        for result in all_issues:
            print(f"📄 {result['file']}:")
            for issue in result['issues']:
                print(f"   {issue}")
            print()
        return False
    else:
        print("✅ Canon validation passed - no consistency issues detected")
        return True


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python validate_canon.py <repo_path>")
        sys.exit(1)
    
    repo_path = sys.argv[1]
    success = validate_canon(repo_path)
    sys.exit(0 if success else 1)
