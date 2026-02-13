Extract items the author is **grateful for** in this journal entry.

1. **Gratitude**: Look for explicit expressions of thanks, gratitude, or appreciation (e.g., "I'm so thankful for...", "Grateful for...", "It was lovely to..."). Also include simple pleasures or positive moments that the author seemingly cherishes (e.g., "The sunset was beautiful today").
2. **Focus on the author**: Gratitude can be towards others or about external events.

## JSON structure

Return a single JSON object with these exact keys:

- `gratitude_items`: Array of strings (e.g., ["Morning coffee", "Supportive friends"]).

If no relevant items are found, return empty arrays.

## Example output

### Example 1: Items found

```json
{
  "gratitude_items": ["Snowy weather", "Dinner with Zaphod"]
}
```

### Example 2: No items found

```json
{
  "gratitude_items": []
}
```
