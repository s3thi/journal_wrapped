Extract names of people the author met for the *first time* or got to know *newly* in this journal entry. Your response must be a valid JSON object with one key: `new_people`.

Guidelines for `new_people`:

- Include names of people the author met for the *first time* or got to know *newly* in this entry.
- Look for phrases like "met X", "introduced to Y", "first date with Z", "made a new friend".
- Exclude: People the author clearly already knows well (old friends, family, long-term partners).
- Format: Name (Title Case).

Example format:

## Example 1: Items found

```json
{
  "new_people": ["Zaphod", "The guy in the pink van"]
}
```

## Example 2: No items found

```json
{
  "new_people": []
}
```
