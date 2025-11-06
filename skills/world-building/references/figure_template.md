# Figure Biography Structure

All biographical files for significant historical figures should follow this structure.

## File Naming

- Filename: `{first-name-last-name-lowercase}.md`
- Location: `figures/`

## Structure

```markdown
---
name: Full Name
birth: DD Month YYYY (or YYYY if exact date unknown)
death: DD Month YYYY (or YYYY if exact date unknown, or "living" if still alive)
nationality: Country Name
role: Primary role or title (e.g., "King", "General", "Revolutionary Leader")
species: human/animal (include animal type if not human, e.g., "owl")
gender: male/female/other
---

# Full Name

## Overview

Brief introduction: who they were, why they're significant, their lasting impact.

## Early Life

- Birth details (date, location, family background)
- Childhood experiences
- Education or training
- Formative events

## Career/Major Accomplishments

Chronological account of their significant achievements:
- How they rose to prominence
- Major positions held (with dates)
- Key decisions or actions
- Battles won, laws passed, works created, etc.

Each major event should include:
- Date
- Context
- Actions taken
- Outcomes

## Personal Life

- Family (spouse, children, parents if relevant)
- Relationships with other significant figures
- Character traits, personality
- Interests or hobbies
- Controversies or scandals

## Death and Legacy

- Circumstances of death (if applicable)
- Immediate aftermath
- Long-term historical impact
- How they're remembered
- Monuments, memorials, or honors

## Timeline

Condensed chronological timeline of life events:
- YYYY: Born in [location]
- YYYY: [Significant event]
- DD Month YYYY: [Specific significant event]
- YYYY: Died in [location]

## Related Entities

Cross-references:
- Countries: `countries/{country-name}.md`
- Events: `events/{event-name}.md`
- Other figures: `figures/{figure-name}.md`
```

## Tips for Non-Human Characters

For animal characters (like Feathery Quol):
- Always specify species in frontmatter and early in the biography
- Describe how an animal came to hold their position (was it normal in that country? special circumstances?)
- Include any unique abilities or characteristics
- Address how their non-human nature affected their role and legacy

## Consistency Reminders

- Dates must align with events in other files
- Relationships must be reciprocal (if Person A is the parent of Person B, Person B's file should mention Person A)
- Death dates must be consistent across all references
- Titles and roles should match what's in country files
- Check existing canon before adding new details
