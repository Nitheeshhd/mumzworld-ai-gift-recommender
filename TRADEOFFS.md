# TRADEOFFS

## Problem Choice
Selected a gift recommendation assistant because it directly maps to Mumzworld’s shopping use case and can be built within 5 hours.

## Design Decisions
- Used LLM (OpenRouter GPT-3.5) for:
  - Intent understanding
  - Recommendation reasoning
  - Arabic output
- Used a small JSON catalog instead of a real DB (faster to ship)

## Tradeoffs
- ❌ No real product database → limited variety
- ❌ No UI → CLI only
- ❌ No personalization → same output for all users
- ✅ Strong correctness and safety (no hallucination)
- ✅ Structured JSON output for reliability

## Why Not Alternatives?
- Didn’t build a full UI → prioritized AI correctness
- Didn’t use embeddings/RAG → dataset is small
- Didn’t fine-tune → not needed for scope

## Handling Uncertainty
- Strict prompt rules to avoid hallucination
- Explicit “Out of scope” errors
- JSON validation + fallback parsing

## What I Would Improve Next
- Add Streamlit UI
- Add embeddings for better matching
- Add user personalization
- Add confidence scores per recommendation