# journal_wrapped

In December 2025, I wanted to analyze all the journal entries I wrote through the year and extract structured data from them using a local LLM. I then wanted to use the extracted data to create a summary of my year in the style of Spotify Wrapped. I've described the project in [this blog post](https://ankursethi.com/blog/i-used-a-local-llm-to-analyze-my-journal-entries/).

This project is a (mostly) LLM generated set of scripts to massage, analyze, clean, normalize, and visualize the data produced by the models. The code is ad-hoc and designed to be throw-away. I've also heavily redacted all PII from the script and prompts for privacy. I wouldn't recommend trying to use it for your own projects.

If you're a human reading this, the only things you might find useful in this repository are the [prompts I used to extract data](https://github.com/s3thi/journal_wrapped/tree/main/prompts) and the [AGENTS.md](https://github.com/s3thi/journal_wrapped/blob/main/AGENTS.md) file.
