# goddamn it

The index file is too big for replit and too big to be hosted on GitHub

# BibleAI

ChatGPT designed to aid in understanding bible scripture.
You're welcome to use `index.json` for your own purposes, too. It's about 2Gb of scriptures. It cost me under $1 to build (if I don't value my time). Consider tipping to help me with my OpenAI costs (including each question asked).

[Google Drive Link (bible_scriptures_index.json)](https://drive.google.com/file/d/1kSpWLwG0eyJUOsALLFCZoVPyzNJ4iaOJ/view?usp=share_link)

# How it works

* First an index of all scriptures is built using the `text-embedding-ada-002` model
    * made a lot more simple with the [llama_index (now rebranded as gpt_index)](https://gpt-index.readthedocs.io/en/latest/index.html) python library.
* When a user asks a question, the index is queried, generating some "context" for ChatGPT
    * the context will be related snippets from scripture
* The users question - and included context - will be passed to the `gpt-3.5-turbo` model, for a user-friendly answer

## Bible source

* https://forum.obsidian.md/uploads/short-url/fK2XyRlWvpxGAuZJENEVUZzZUIh.zip