Extract physical health information **experienced by the author** in this journal entry.

1. Focus on the author: do not extract health issues relating to other people (friends, family, partners) mentioned in the text.
2. Symptoms & conditions: extract specific physical symptoms (e.g., "Sore throat", "Migraine", "Back pain") or diagnosed conditions (e.g., "Flu", "Covid"). Normalize informal descriptions to standard terms where possible (e.g., "my tummy hurts" -> "Stomach ache").
3. Exclusions:
   - Do not include general fleeting states like "tired", "hungry" unless they are described as severe (e.g. "Exhaustion").
   - Do not include physical activities (e.g., "went for a run") unless they resulted in an injury or pain.
   - Do not include purely mental health issues (e.g. "Anxiety", "Depression"), though physical symptoms of them (e.g. "Panic attack symptoms" like racing heart) can be included if explicitly physical.

## JSON structure

Return a single JSON object with this exact key:

- `physical_health_issues`: Array of strings (e.g., ["Back pain", "Stomach ache"]).

If no relevant issues are found, return an empty array.

## Example output

### Example 1: Issues found

```json
{
  "physical_health_issues": ["Sore throat", "Headache"]
}
```

### Example 2: No issues found

```json
{
  "physical_health_issues": []
}
```
