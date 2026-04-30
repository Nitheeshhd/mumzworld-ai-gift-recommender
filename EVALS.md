# EVALUATION

## Setup
- Model: GPT-3.5 via OpenRouter
- Data: products.json (mock catalog)
- Goal: Correct recommendations, strict domain handling, valid JSON

## Test Cases

1) Input: gift for baby under 100 AED  
Expected: low-cost baby items  
Result: ✅ Passed

2) Input: gift for baby under 200 AED  
Expected: multiple relevant items  
Result: ✅ Passed

3) Input: gift for 6 month baby  
Expected: age-appropriate items  
Result: ✅ Passed

4) Input: newborn essentials under 80 AED  
Expected: essentials within budget  
Result: ✅ Passed

5) Input: gift without budget  
Expected: reasonable items (no budget filter)  
Result: ✅ Passed

6) Input: gift under 10 AED  
Expected: no suitable products  
Result: ✅ Passed (returned error)

7) Input: necklace for girlfriend  
Expected: out-of-scope  
Result: ✅ Passed (Out of scope request)

8) Input: random text "asdfgh"  
Expected: out-of-scope  
Result: ✅ Passed

9) Input: high budget (under 500 AED)  
Expected: all relevant items within list  
Result: ✅ Passed

10) Input: mixed intent "gift for baby and phone"  
Expected: ignore non-domain, return baby items OR error  
Result: ✅ Passed (domain filtered)

## Metrics (Simple)
- Success rate: 10/10
- JSON validity: 10/10
- Out-of-scope handling: 3/3

## Failure Modes Observed
- Earlier version hallucinated products for out-of-scope queries (fixed via strict prompt + low temperature).
- Occasional extra text around JSON (handled via `extract_json`).

## Conclusion
System is robust:
- Valid outputs are grounded in provided products
- Out-of-scope queries are rejected
- JSON is consistently parsed and validated