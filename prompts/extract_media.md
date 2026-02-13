Extract references to media (books, movies, TV shows, games, music) consumed or mentioned by the author in this journal entry. Your response must be a valid JSON object with one key: `media`.

Guidelines for `media`:

- Include specific titles of books, movies, TV shows, video games, songs, or albums.
- Look for italicized text as a potential cue (e.g., *The Matrix*), but use your judgement as titles may not always be formatted.
- Exclude generic references (e.g., "watched a movie", "listened to some music", "reading a book").
- Exclude names of artists, authors, musicians, or other creators. Only include pieces of media.
- Format: Title Case (e.g., "The Great Gatsby", "Elden Ring").

Only include valid JSON in your response. Return no other text.

Example format:

## Example 1: Items found

```json
{
  "media": ["Dune", "The Bear", "Midnights"]
}
```

## Example 2: No items found

```json
{
  "media": []
}
```
