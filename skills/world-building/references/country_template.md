# Country File Structure

All country files should follow this canonical structure using YAML frontmatter and markdown sections.

## File Naming

- Filename: `{country-name-lowercase}.md`
- Location: `countries/`

## Structure

```markdown
---
name: Country Name
capital: Capital City
founded: YYYY or DD Month YYYY
population: Approximate population (optional)
location: Brief description of geographic location
---

# Country Name

## Overview

Brief introduction to the country, its identity, and its place in the world.

## Geography

Detailed description of:
- Location within the real-world map (which region of Europe, neighboring areas)
- Physical features (mountains, rivers, coastlines, climate)
- Major cities and regions

## History

### Founding

How the country was established, including:
- Founding date and circumstances
- Founding figures
- Initial government structure

### Major Events

Chronological list of significant historical events:
- Wars, conflicts, peace treaties
- Political revolutions or reforms
- Economic developments
- Natural disasters or major crises
- Correlation with real-world events (e.g., involvement in WWII)

Each event should include:
- Date (specific as possible)
- Description
- Key figures involved
- Consequences

## Government and Politics

### Current System

Description of the government structure:
- Type of government (monarchy, democracy, etc.)
- Key institutions
- How leaders are selected

### Timeline of Leaders

Chronological list of all leaders with:
- Name and title
- Period in power (start date - end date)
- How they came to power
- How their leadership ended (election, death, revolution, etc.)
- Brief description of their rule
- Major accomplishments or failures

### Political Parties

For each significant political party:
- Name
- Founded date
- Ideology
- Key figures
- Electoral history
- Notable policies or positions

## Notable Figures

Brief profiles of significant historical figures (detailed biographies should be in `figures/` directory):
- Full name
- Birth and death dates
- Role/position
- Major contributions
- Link to detailed biography if available

## Economy and Trade

- Main industries
- Trading partners
- Economic system
- Currency
- Natural resources

## International Relations

### Allies

List of allied countries with:
- Country name
- Nature of relationship
- Treaties or agreements
- Historical context

### Rivals or Enemies

List of countries with hostile relationships:
- Country name
- Nature of conflict
- Historical background

### Neutrality

If applicable, countries with neutral relationships

## Cultural Notes

- Language(s)
- Religion(s)
- Notable cultural practices or traditions
- National symbols (flag, anthem, etc.)

## References

Cross-references to related files:
- Key events: `events/{event-name}.md`
- Key figures: `figures/{figure-name}.md`
- Treaties/Relations: `relations/{relation-name}.md`
```

## Tips

- Use specific dates whenever possible (DD Month YYYY)
- Always check existing canon before adding new information
- Maintain chronological consistency in timelines
- Cross-reference related entities (people, events, other countries)
- Be detailed but avoid contradictions
- Real-world event correlations should be plausible and internally consistent
