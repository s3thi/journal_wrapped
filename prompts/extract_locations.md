Extract a list of specific locations mentioned in this journal entry. Your response must be a valid JSON object with one key: `locations`.

Guidelines for `locations`:

- Include specific cities, countries, neighborhoods, and named venues (e.g. "Bangalore", "Cubbon Park", "Blue Tokai Coffee").
- Exclude generic places ("home", "work", "the gym", "the office") unless a specific name is attached.
- Exclude rooms ("kitchen", "bedroom").

Example format:

## Example 1: Entities found

```json
{
  "locations": ["Bangalore", "Underline Center"]
}
```

## Example 2: No entities found

```json
{
  "locations": []
}
```
