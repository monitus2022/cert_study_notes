# Reciprocal Rank Fusion

**Time:** 15 min  
**Topic:** Hybrid retrieval  
**Language:** Python

## Prompt

Implement reciprocal rank fusion (RRF) over several ranked result lists.

```python
def rrf(rankings: list[list[str]], k: int = 60) -> list[str]:
    ...
```

For each document, its score is the sum of `1 / (k + rank)` across every list where it appears. Ranks start at 1. Return document IDs sorted by descending score. Break ties by document ID in ascending order.

## Constraints

- Deduplicate a document within a single ranking before scoring it.
- Do not assume the input lists are the same length.
- `k` is positive and defaults to 60.
- Target `O(N log N)` time, where `N` is the number of distinct documents.

## Starter

```python
def rrf(rankings: list[list[str]], k: int = 60) -> list[str]:
    ...
```

## Tests

```python
assert rrf([["a", "b"], ["b", "a"]]) == ["a", "b"]
assert rrf([["a", "b", "c"], ["c", "a"]]) == ["a", "c", "b"]
assert rrf([["a", "a", "b"]]) == ["a", "b"]
assert rrf([[], ["a"]]) == ["a"]
assert rrf([]) == []
```

## Solution

```python
from collections import defaultdict


def rrf(rankings: list[list[str]], k: int = 60) -> list[str]:
    scores: dict[str, float] = defaultdict(float)

    for ranking in rankings:
        seen: set[str] = set()
        for rank, doc_id in enumerate(ranking, start=1):
            if doc_id in seen:
                continue
            seen.add(doc_id)
            scores[doc_id] += 1.0 / (k + rank)

    return sorted(scores, key=lambda doc_id: (-scores[doc_id], doc_id))
```

## Notes

- **Why RRF:** it combines rankings without normalising raw scores, which matters when BM25 and vector similarity live on different scales.
- **`k`:** a larger `k` flattens the advantage of top ranks. `60` is a common default, not a law.
- **Deduplication:** deduplicate per list. Deduplicating globally would incorrectly drop a document from later lists.
- **Complexity:** `O(N)` score accumulation plus `O(N log N)` sorting.
- **Common mistakes:** starting ranks at 0, summing raw scores instead of reciprocal ranks, and treating missing documents as rank 0.
- **Follow-ups:** weighted RRF, evaluating with recall@k and MRR, and why score fusion needs calibration while rank fusion does not.
