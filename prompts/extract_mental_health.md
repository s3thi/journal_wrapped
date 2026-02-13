Extract mental health information **experienced by the author** in this journal entry.

1. Focus on the author: do not extract health issues relating to other people (friends, family, partners) mentioned in the text.
2. Symptoms & conditions: extract specific mental health symptoms or conditions (e.g., "Anxiety", "Depression", "Panic attack", "Burnout", "Insomnia").
3. Exclusions:
   - Do not include general fleeting states like "tired", "bored", or "stressed" unless they are described as severe or chronic (e.g., "Exhaustion", "Burnout", "Chronic Stress").
   - Do not include physical health issues (e.g. "Headache", "Flu") unless they are clearly psychosomatic or directly related to mental state.

## JSON structure

Return a single JSON object with this exact key:

- `mental_health_issues`: Array of strings (e.g., ["Anxiety", "Depressive episode"]).

If no relevant issues are found, return an empty array.

## Example output

### Example 1: Issues found

```json
{
  "mental_health_issues": ["Anxiety", "Low mood"]
}
```

### Example 2: No issues found

```json
{
  "mental_health_issues": []
}
```
