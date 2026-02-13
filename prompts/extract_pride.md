Extract things the author is **proud of accomplishing** in this journal entry.

1. **Accomplishments**: Look for tasks finished, goals reached, or personal wins (e.g., "Finally finished the report", "Ran 5km", "Fixed the sink"). These can be small daily wins or major milestones.
2. **Focus on the author**: Only extract accomplishments of the author.

## JSON structure

Return a single JSON object with these exact keys:

- `accomplishments`: Array of strings (e.g., ["Finished reading 'Dune'", "Cleaned the garage"]).

If no relevant items are found, return empty arrays.

## Example output

### Example 1: Items found

```json
{
  "accomplishments": ["Wrote 500 words", "Went to the gym"]
}
```

### Example 2: No items found

```json
{
  "accomplishments": []
}
```
