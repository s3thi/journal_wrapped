Extract a list of distinct people mentioned in this journal entry. Your response must be a valid JSON object with one key: `people`.

Guidelines for `people`:

- Exclude the author ("I", "me").
- Exclude generic references ("the driver", "a friend").
- Normalize names to Title Case.

Return a single valid JSON object with no other text.

## Example formats

## Example 1: Entities found

```json
{
  "people": ["Mom", "Ankush", "Tanvi"]
}
```

## Example 2: No entities found

```json
{
  "people": []
}
```
