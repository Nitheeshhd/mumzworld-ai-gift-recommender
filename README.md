# Mumzworld AI Gift Recommender

## Summary
An AI-powered assistant that converts natural language queries into structured product recommendations for moms and babies, with multilingual support (English & Arabic) and strict out-of-scope handling.

---

## Features
- AI-based recommendation engine
- Structured JSON output
- Multilingual responses (EN + AR)
- Out-of-scope detection (no hallucination)
- Robust parsing & error handling

---

## How It Works
1. User enters a query
2. LLM (via OpenRouter) interprets intent
3. Matches against products.json
4. Returns structured JSON
5. CLI prints EN + AR output

---

## Tech Stack
- Python
- OpenRouter (GPT-3.5)
- JSON (mock product catalog)

---

## Setup (Run in < 5 minutes)

```bash
pip install -r requirements.txt
python app.py