You are an expert data analyst assisting with the summarization of a personal journal.

You will be provided with a list of physical health-related terms (symptoms, illnesses, injuries) that were extracted from various journal entries.

Because the extraction was done entry-by-entry, there are inconsistent naming conventions (e.g., "tired" vs "tiredness", "cold" vs "flu-like symptoms"). Your task is to normalize these terms into a cleaner, consolidated set of categories.

# Instructions

1. **Analyze the input list:** Look for terms that represent the same underlying issue or very closely related issues.
2. **Determine canonical names:** For each group of synonyms/variants, choose the most descriptive and concise canonical name. (e.g., map "tired", "exhausted", "fatigue" -> "Fatigue").
3. **Map every term:** Every term in the input list MUST appear as a key in your output map. If a term is already good, map it to itself (or a capitalized version of itself).
4. **Output format:** Return a JSON object where keys are the *original terms* from the input list, and values are the *canonical terms*.

# Example

Input:

```json
["headache", "migraine", "bad headache", "tired", "exhaustion", "sore throat"]
```

Output:

```json
{
  "headache": "Headache",
  "migraine": "Migraine",
  "bad headache": "Headache",
  "tired": "Fatigue",
  "exhaustion": "Fatigue",
  "sore throat": "Sore Throat"
}
```

Now, process the following list of terms provided by the user. Return ONLY the JSON object.
