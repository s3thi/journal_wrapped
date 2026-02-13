Extract organized or semi-organized social gatherings the author participated in this journal entry. Your response must be a valid JSON object with one key: `social_activities`.

Guidelines for `social_activities`:

- Include organized or semi-organized social gatherings the author participated in.
- Examples: Clubs, parties, meetups, workshops, team dinners, weddings, concerts, festivals.
- Exclude: Routine hangouts with close friends unless it's a specific named event (e.g., "Dinner at John's" is routine, "John's Birthday Party" is an activity).

Only include valid JSON in your response. Return no other text.

Example format:

## Example 1: Items found

```json
{
  "social_activities": ["Office Christmas Party", "Salsa Class"]
}
```

## Example 2: No items found

```json
{
  "social_activities": []
}
```
