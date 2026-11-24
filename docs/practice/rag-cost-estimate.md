# Cost of a 1M-Request Assistant

```yaml
id: cost-001
domain: system-design
subtopic: cost
difficulty: 2/5
format: numerical
round: fundamentals
from_project: false
```

## Stem

A RAG assistant handles 1,000,000 requests per day. Each request sends 4,000 input tokens and generates 300 output tokens. The provider charges **3 USD per million input tokens** and **15 USD per million output tokens**.

Ignore retrieval, embedding, and infrastructure costs. Estimate the monthly model cost at 30 days.

## Answer

- Requests per month: `1,000,000 × 30 = 30,000,000`
- Input tokens per month: `30,000,000 × 4,000 = 120,000,000,000` tokens, or `120,000` million tokens
- Input cost: `120,000 × 3 = 360,000` USD
- Output tokens per month: `30,000,000 × 300 = 9,000,000,000` tokens, or `9,000` million tokens
- Output cost: `9,000 × 15 = 135,000` USD

**Total: 495,000 USD per month**, or **0.0165 USD per request** (`0.012` input + `0.0045` output).

## Why this matters

Input dominates the bill here: about 73% of the cost. A design that halves the retrieved context saves far more than a design that halves the output length. That is the kind of lever to look for before reaching for a cheaper model.

## Follow-ups

1. **What if 60% of input tokens are cached at 10% of the normal price?**
   - Full-price input: `40% × 360,000 = 144,000` USD
   - Cached input: `60% × 360,000 × 10% = 21,600` USD
   - New total: `144,000 + 21,600 + 135,000 = 300,600` USD per month, a 39% reduction.

2. **What if output length doubles?**
   - Output cost becomes `270,000` USD, total `630,000` USD per month.

3. **Which is cheaper: cutting input by 30% or cutting output by 30%?**
   - Input cut saves `0.30 × 360,000 = 108,000` USD.
   - Output cut saves `0.30 × 135,000 = 40,500` USD.
   - The input cut is worth more than twice as much.

## Common mistakes

- Forgetting to multiply by 30 days.
- Mixing dollars per token with dollars per million tokens.
- Applying the output price to input tokens.
- Calculating the per-request cost correctly but then multiplying by days instead of requests.
- Treating the cached-input discount as a discount on the whole bill rather than on the eligible input tokens.
