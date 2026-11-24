# Lost in the Middle: How Language Models Use Long Contexts

| Field | Value |
| --- | --- |
| **Source** | [Lost in the Middle: How Language Models Use Long Contexts](https://arxiv.org/abs/2307.03172) |
| **Type** | Paper |
| **Authors** | Nelson F. Liu, Kevin Lin, John Hewitt, Ashwin Paranjape, Michele Bevilacqua, Fabio Petroni, Percy Liang |
| **Date** | 2023-07-06 |

## Core idea

Model quality on multi-document question answering depends on **where** the relevant information appears in the context, not just whether it appears. Performance is highest when the evidence is at the beginning or end of the context and degrades when it is buried in the middle. A larger context window raises the ceiling on what can be passed in; it does not guarantee that the model will use all of it.

## Key points

- The position effect is U-shaped: primacy and recency both help, and the middle is the worst place for relevant evidence.
- Adding more retrieved documents can lower accuracy even when the correct document is present. More context also means more distractors.
- Long-context models still show the effect. A 128k window is capacity, not a guarantee of usable attention.
- Ordering, reranking, and compression are first-class retrieval decisions, not cosmetic prompt tweaks.
- Evaluations should control for position. Shuffle the evidence and report results across arrangements instead of a single lucky ordering.
- The paper studies multi-document QA and key-value retrieval. The exact curve will differ by task, model, and prompt, but the design lesson generalises.

## Where it applies

- **RAG context packing:** rerank before packing, cap the number of chunks, and put the strongest evidence near the start or end.
- **Long-document workflows:** summarise or retrieve sections instead of stuffing the whole document into the prompt.
- **Evaluation:** add position-controlled cases to the golden set so a prompt change cannot pass by accident.
- **Design reviews:** "Why not just use the 1M-token window?" now has a concrete answer: cost, latency, distraction, and position sensitivity.

## Open questions

- How much of the effect disappears with newer long-context models and targeted instruction tuning?
- How does position interact with document length, number of distractors, and query complexity?
- Which compression strategy preserves the evidence the model actually needs without introducing new omissions?

## Quotes and links

- [arXiv:2307.03172](https://arxiv.org/abs/2307.03172)
