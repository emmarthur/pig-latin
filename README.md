# Pig Latin (catalog #493)

Al Sweigart — *The Big Book of Small Python Projects*, Project #54.

| Artifact | Path |
|----------|------|
| Book steps | [`BOOK_DIRECTIONS.md`](./BOOK_DIRECTIONS.md) |
| Upstream script | [`reference/piglatin.py`](./reference/piglatin.py) |
| CLI | [`reference/run_cli.py`](./reference/run_cli.py) |
| Shared logic | [`pig_latin_core.py`](./pig_latin_core.py) |
| Web (FastAPI) | [`web/`](./web/) — port **3024** |

## Run the web demo

```powershell
Set-Location "c:\Users\emmak\Desktop\Content\CodingProjects\PortProjects\demos\pig-latin\web"
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
uvicorn main:app --reload --port 3024
```

Open [http://127.0.0.1:3024/](http://127.0.0.1:3024/).

## Run the CLI

```powershell
Set-Location "c:\Users\emmak\Desktop\Content\CodingProjects\PortProjects\demos\pig-latin"
python reference\run_cli.py
```

Portfolio: [`PORTFOLIO_INTEGRATION.md`](./PORTFOLIO_INTEGRATION.md).
