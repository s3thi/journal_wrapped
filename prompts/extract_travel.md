Extract trips taken by the author away from their home city in this journal entry. Your response must be a valid JSON object with one key: `travel`.

Guidelines for `travel`:

- Include trips taken by the author away from their home city.
- Examples: Vacations, business trips, weekend getaways.
- Format: "City, Country" or "Place Name" (e.g., "Paris, France", "Yosemite National Park").
- Exclude: Commutes, routine travel within the home city.

Example format:

## Example 1: Items found

```json
{
  "travel": ["Tokyo, Japan", "Kyoto"]
}
```

## Example 2: No items found

```json
{
  "travel": []
}
```
