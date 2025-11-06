# Event File Structure

All major historical events should have detailed documentation following this structure.

## File Naming

- Filename: `{event-name-lowercase}.md`
- Location: `events/`

## Structure

```markdown
---
name: Event Name
start_date: DD Month YYYY (or YYYY if exact date unknown)
end_date: DD Month YYYY (or YYYY, or "ongoing" for current events)
type: war/treaty/revolution/crisis/disaster/other
countries_involved: [Country1, Country2, Country3]
---

# Event Name

## Overview

Brief summary: what happened, when, where, and why it matters.

## Background

Context leading up to the event:
- Political situation
- Economic factors
- Social tensions
- Previous related events
- Why this event occurred

## Timeline

Detailed chronological account of the event:

### Phase 1 Name (Date Range)
- Key developments
- Important battles, negotiations, or moments
- Figures involved
- Outcomes

### Phase 2 Name (Date Range)
[continue as needed]

Use specific dates (DD Month YYYY) for major turning points.

## Key Figures

List of significant people involved:
- Name and role
- Their actions during the event
- Link to biography: `figures/{name}.md`

## Countries Involved

For each participating country:
- Role (aggressor, defender, ally, mediator, etc.)
- Motivation for involvement
- Actions taken
- Casualties or losses (if applicable)
- Link: `countries/{name}.md`

## Outcome

- How the event concluded
- Winners/losers (if applicable)
- Immediate consequences
- Treaties or agreements signed
- Territorial changes
- Casualties (military and civilian)

## Long-Term Impact

- Political changes
- Economic effects
- Social transformation
- How it changed international relations
- Cultural memory or significance
- Connection to later events

## Correlation with Real-World Events

If this event parallels or interacts with real historical events:
- What real-world event(s) does it correlate with?
- How does the timeline align?
- What are the similarities and differences?
- How did real-world events influence this fictional event?

## Heroes and Legends

Notable acts of heroism or legendary moments:
- Individual heroes and their deeds
- Famous battles or confrontations
- Dramatic turning points
- Stories that entered cultural memory

## Related Entities

Cross-references:
- Countries: `countries/{country-name}.md`
- Figures: `figures/{figure-name}.md`
- Other events: `events/{event-name}.md`
- Treaties/Relations: `relations/{relation-name}.md`
```

## Special Considerations for Wars

When documenting wars, include:
- Specific battles with dates and outcomes
- Military strategies employed
- Commanders for each side
- Technology or weapons used
- War crimes or atrocities (if any)
- Peace negotiations process

## Special Considerations for Political Events

For revolutions, elections, coups:
- Factions involved
- Ideology or goals
- Popular support
- Methods used (peaceful protest, armed conflict, etc.)
- Constitutional changes

## Consistency Requirements

- All dates must align with country timelines and figure biographies
- Countries involved must exist in canon at the specified time
- Figures mentioned must have biographies that support their involvement
- Outcomes must be reflected in country files
- Real-world correlations must be historically plausible
