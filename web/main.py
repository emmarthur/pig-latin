"""
FastAPI app — Pig Latin translator.

Run: uvicorn main:app --reload --port 3024
"""

from __future__ import annotations

import sys
from pathlib import Path

from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel, Field

_DEMO_ROOT = Path(__file__).resolve().parent.parent
if str(_DEMO_ROOT) not in sys.path:
    sys.path.insert(0, str(_DEMO_ROOT))

from pig_latin_core import english_to_pig_latin, example_phrases  # noqa: E402

app = FastAPI(title="Pig Latin")
templates = Jinja2Templates(directory=str(Path(__file__).parent / "templates"))
app.mount("/static", StaticFiles(directory=str(Path(__file__).parent / "static")), name="static")


class TranslateRequest(BaseModel):
    text: str = Field(..., max_length=8000)


@app.get("/", response_class=HTMLResponse)
async def index(request: Request) -> HTMLResponse:
    return templates.TemplateResponse(
        request,
        "index.html",
        {"examples": example_phrases()},
    )


@app.get("/help", response_class=HTMLResponse)
async def help_page(request: Request) -> HTMLResponse:
    return templates.TemplateResponse(request, "help.html")


@app.post("/api/translate")
async def api_translate(body: TranslateRequest) -> JSONResponse:
    if not body.text.strip():
        raise HTTPException(status_code=400, detail="Enter some text to translate.")
    return JSONResponse({"pig_latin": english_to_pig_latin(body.text)})
