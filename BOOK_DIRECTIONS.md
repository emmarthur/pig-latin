# Book directions — Pig Latin

**Catalog #493** · Al Sweigart, *The Big Book of Small Python Projects*, **Project #54** — Pig Latin

- Invent with Python: [project54.html](https://inventwithpython.com/bigbookpython/project54.html)
- Upstream: [piglatin.py](https://github.com/asweigart/the-big-book-of-small-python-projects/blob/main/piglatin.py)
- Local reference: [`reference/piglatin.py`](./reference/piglatin.py)
- Shared logic: [`pig_latin_core.py`](./pig_latin_core.py)

## What the book asks you to build

Read a message and print the **Pig Latin** translation:

- Split on whitespace; for each word, peel leading/trailing non-letters.
- Move leading consonants to the end + `ay`, or append `yay` if the word starts with a vowel (`a,e,i,o,u,y`).
- Restore ALL CAPS or Title Case; optional `pyperclip` copy in the terminal.

## Web version (`web/` — FastAPI, port **3024**)

| Book step | Web equivalent |
|-----------|----------------|
| `englishToPigLatin` | `pig_latin_core.english_to_pig_latin` |
| User message | Textarea + `POST /api/translate` |
| Clipboard | Browser **Copy result** button |

CLI: [`reference/run_cli.py`](./reference/run_cli.py)
