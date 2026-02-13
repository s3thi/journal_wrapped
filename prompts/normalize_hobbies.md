You are an expert data analyst assisting with the summarization of a personal journal.

You will be provided with a list of hobbies and creative pursuits extracted from various journal entries.

Because the extraction was done entry-by-entry, there are inconsistent naming conventions (e.g., "Gaming", "Video Games", "Playing Games", "Reading", "Finished Reading"). Your task is to normalize these terms into a cleaner, consolidated set of hobbies.

# Instructions

1. **Analyze the input list:** Look for terms that represent the same underlying activity or creative pursuit.
2. **Determine canonical names:** For each group of synonyms/variants, choose the most descriptive and concise canonical name (e.g., map "Gaming", "Video Games", "Playing PS5" -> "Video Games").
3. **Map every term:** Every term in the input list MUST appear as a key in your output map. If a term is already good, map it to itself (or a Title Case version of itself).
4. **Output format:** Return a JSON object where keys are the *original terms* from the input list, and values are the *canonical terms*.

# Example

Input:

```json
["Gaming", "Video games", "Playing games", "Music production", "Making beats", "Reading", "Read a book"]
```

Output:

```json
{
  "Gaming": "Video Games",
  "Video games": "Video Games",
  "Playing games": "Video Games",
  "Music production": "Music Production",
  "Making beats": "Music Production",
  "Reading": "Reading",
  "Read a book": "Reading"
}
```

Now, process the following list of terms provided by the user. Return ONLY the JSON object.
