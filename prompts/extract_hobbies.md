Extract references to **hobbies and creative pursuits** the author engaged in during this journal entry. Your response must be a valid JSON object with one key: `hobbies`.

Guidelines for `hobbies`:

- Include active pastimes, creative endeavors, and skill-building activities.
- Examples: Reading, Writing, Video Games, Music Production, Painting, Coding, Gardening, Cooking, Hiking.
- Focus on the *activity* or the *pursuit* (e.g., "Playing Guitar", "Writing Poetry", "Video Games").
- If a specific game, book, or project is mentioned, extract the activity associated with it (e.g., "Playing Elden Ring" -> "Video Games" or "Gaming"; "Reading Dune" -> "Reading").
- Include creative outputs or projects (e.g., "Made a beat", "Edited a video").
- Exclude: Passive entertainment (e.g., "Watching TV") unless it involves active engagement/learning.
- Exclude: Routine chores or work tasks (unless they are explicitly described as enjoyable/hobby-like).
- Format: Title Case (e.g., "Music Production", "Photography").

Only include valid JSON in your response. Return no other text.

Example format:

## Example 1: Items found

```json
{
  "hobbies": ["Reading", "Music Production", "Video Games"]
}
```

## Example 2: No items found

```json
{
  "hobbies": []
}
```
