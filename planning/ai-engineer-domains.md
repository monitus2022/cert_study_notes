# AI Engineer Job Domain

I'll look up current AI-engineer interview expectations so the domains I suggest match what companies actually test, then map them to a question-bank structure that fits your background.

I have a solid picture of 2026 interview loops. Next I’ll pull independent views on which domains matter most for someone with your backend + data-science + AWS MLA-C02 mix.

Your instinct is right: a **forced-choice question bank** is a better prep system than textbooks, especially after MLA-C02. Cert questions train AWS *selection*. Interviews train **tradeoffs, debugging, and numbers**.

An AI Engineer loop in 2026 is usually: coding screen → LLM/RAG system design → fundamentals → project deep dive → behavioral. Applied AI roles skew to products on foundation models (RAG, agents, evals, cost, safety). Hybrid ML Engineer roles still add classical ML. You should prep for both.

Below is a domain map you can drop into one repo and start writing questions against.

## How to use this

Treat each domain as a **folder of questions**, not a reading list. For every topic, write items in this order:

1. **MCQ with close distractors** (your cert style)
2. **Debug scenario** (“this RAG is failing — what do you check first?”)
3. **Forced tradeoff** (RAG vs fine-tune vs prompt; latency vs cost vs quality)
4. **Numerical estimate** (tokens, GPU, $ per 1M requests)
5. **Whiteboard design** (only after 1–4)

Your resume project should be the **source of truth** for scenarios. If you cannot write 10 questions from a design decision you made, that decision is not interview-ready yet.

---

## Ranked domains (highest interview ROI first)

### 1. RAG as an information-retrieval problem
**Why first:** this is the most common opener. Interviewers do not want “I used LangChain + Pinecone.” They want you to debug *retrieval before the model*.

**Must-have**
- Chunking: fixed, recursive, semantic, document-aware; overlap vs lost context
- Embeddings: what they capture / fail to capture; dim, multilingual, code vs text
- ANN vs exact search; cosine / dot / L2; HNSW vs IVF
- Dense vs sparse vs hybrid; RRF; rerankers (cross-encoder)
- Metadata filters and ACLs (retrieval must respect permissions)
- Context packing: lost-in-the-middle, citation grounding, long-doc strategies
- RAG eval: recall@k, precision@k, MRR, faithfulness, answer relevance, context precision
- Failure modes: irrelevant chunks, stale index, query/doc mismatch, over-chunking tables/code

**Nice-to-have:** ColBERT, graph RAG, multimodal RAG, 10M-doc latency math.

**Question formats:** MCQ + debug first. Design last.

**Stems to seed the bank**
- “RAG returns fluent but wrong answers. Rank the next 4 debug steps.”
- “When is hybrid search worth the extra latency?”
- “Your recall@20 is 0.91 but faithfulness is 0.4. What is broken?”
- “Chunk size 256 vs 1024 for policy PDFs with tables — pick one and justify.”

**Your gap:** MLA-C02 covers *configuring* vector DBs, embeddings, and chunking. Interviews ask you to **measure and debug** them without AWS as a crutch.

---

### 2. LLM fundamentals (working internals, not paper-level math)
**Why:** every later tradeoff (cost, latency, agents, long context) collapses if you cannot reason about tokens and the generation loop.

**Must-have**
- Tokenization; why “count the words” is wrong for cost/context
- Prefill vs decode; TTFT vs tokens/sec
- Context window vs usable context; lost-in-the-middle; context rot
- Sampling: temperature, top-p, top-k; greedy vs nucleus; when determinism matters
- KV cache; why long conversations get expensive
- Attention at “implement the formula / explain QKV” level, not from-scratch GPT
- Structured output: JSON schema, constrained decoding, tool/function calling
- Reasoning models vs chat models: extra tokens, latency, when not to use them

**Nice-to-have:** RoPE, MoE routing, speculative decoding internals, writing attention in numpy.

**Question formats:** MCQ + “what happens to TTFT if…” numericals.

**Stems**
- “Input is 8k tokens, output is 20 tokens. Where is the latency?”
- “Temperature 0 still varies. Why?”
- “Context is 128k. Why did the model ignore the middle PDF section?”

**Your gap:** cert is applied. Interviews want mechanism → production consequence.

---

### 3. Evals and reliability (“eval is the new system design”)
**Why:** this is where candidates fail even if they can draw a RAG diagram. Take-homes and project deep-dives are graded on evals, not demos.

**Must-have**
- Golden set vs production traces vs synthetic data
- Offline vs online eval; LLM-as-judge and how it is calibrated
- Task metrics: exact match, F1, pass@k vs pass^k, rubric scores
- RAG-specific vs agent-specific (trajectory vs final answer)
- Error analysis: slice by query type, not just average score
- Gating: what blocks a deploy
- Regression: prompt/model/index change silently dropped quality
- Human review sampling under privacy constraints

**Nice-to-have:** full red-team harness, statistical significance of A/B on LLM outputs.

**Question formats:** forced choice on *what to measure*, then “design a 50-example eval that would catch this bug.”

**Stems**
- “Accuracy is 92% and users hate it. What did you measure wrong?”
- “LLM-as-judge agrees with itself but not with humans. Next step?”
- “Ship a support bot with 40 labeled tickets. What is the minimum eval you accept?”

**Your strength:** MS Data Science should make metrics, splits, and bias feel familiar. Translate that into *LLM* evals, not sklearn accuracy.

---

### 4. AI system design + LLMOps (cost, latency, serving, ops)
**Why:** this is where a backend engineer can outperform pure DS candidates — if you talk like a production engineer, not a Bedrock console user.

**Must-have**
- End-to-end design rubric: problem → data/eval → retrieval/model → serving → guardrails → monitoring → cost → scale
- Latency budget: p50/p95/p99, TTFT, streaming
- Cost: input vs output tokens, caching, routing cheap vs expensive models
- Reliability: timeouts, retries, idempotency, fallbacks, hedging
- Caching: exact prompt cache, semantic cache, document cache
- Serving: batching, quantization, autoscaling, GPU vs CPU vs API
- Observability: traces, token cost per request, refusal rate, drift, quality sampling
- CI/CD for prompts, indexes, and models (versioning + rollback)
- Decision framework: managed API vs self-host vs Bedrock/SageMaker

**Nice-to-have:** PagedAttention, tensor parallelism, vLLM internals — only if targeting infra-heavy roles.

**Question formats:** architecture MCQs, then 30–40 min design, then “cut cost 50% without tanking quality.”

**Stems**
- “1M queries/day, 4k-token context, need p95 < 2s. Sketch cost and architecture.”
- “Provider quality dropped after a silent model update. How do you detect it?”
- “When do you *not* self-host?”

**Your strength:** backend + MLA-C02 Domain 3/4. Practice doing the same designs **without naming AWS first**. Interviewers often want vendor-neutral reasoning, then “and on AWS I would use X.”

---

### 5. Agents, tools, and workflows
**Why:** growing fast in 2026. The trap is describing ReAct and then being unable to talk about failure compounding.

**Must-have**
- Agent vs workflow (when a DAG/state machine is enough)
- Tool design: few tools, strict schemas, least privilege, idempotency
- Loop control: max steps, timeouts, human approval for side effects
- Memory: conversation vs episodic vs retrieved
- Multi-agent: supervisor vs swarm vs handoff; when multiple agents are unjustified
- Observability of traces; eval on whole trajectories
- MCP / tool servers at a conceptual level

**Nice-to-have:** research-agent paper architectures, custom planners.

**Question formats:** “agent or workflow?” forced choice; then failure-mode debug.

**Stems**
- “Research + write a report. Components, stop conditions, eval.”
- “Agent called `refund_customer` twice. What was missing in tool design?”
- “Single tool-using agent vs 3 agents. When is the extra hop worth it?”

**Your gap:** MLA-C02 mentions agentic workflows. Interviews want **control, eval, and blast radius**, not “I used an agent framework.”

---

### 6. Production Python and coding screens
**Why:** you never reach the RAG whiteboard if the screen is weak. AI Engineer screens are often: Python, JSON/APIs, retries, parsing model output, plus some algorithms.

**Must-have**
- Python: typing, dataclasses/pydantic, async, generators, error handling
- Calling a model API: timeouts, retries with jitter, structured output parsing
- Data wrangling: pandas/numpy enough to clean a dataset and compute a metric
- Algorithms at interview-medium: hashes, heaps, two pointers, graphs, prefix sums
- ML-flavored coding: implement cosine similarity, chunker, eval scorer, simple logistic regression / k-means from numpy
- SQL for data questions (joins, window functions) — still common

**Nice-to-have:** CUDA, distributed training loops, LeetCode hard grind.

**Question formats:** 20–40 min coding; plus MCQs on “what is wrong with this retry/backoff snippet.”

**Your strength:** backend. **Your risk:** rustiness on timed algorithm problems and “implement the metric” notebooks.

---

### 7. Security, safety, and guardrails
**Why:** OWASP LLM Top 10, prompt injection, and PII show up in design *and* fundamentals. Saying “we’ll add a system prompt” is a fail.

**Must-have**
- Prompt injection vs jailbreak; indirect injection via retrieved docs
- Least-privilege tools; no secrets in prompts; confirm before side effects
- PII: redact before send, retention, log minimization, retrieval ACLs
- Output validation; over-refusal vs under-blocking as a product metric
- Data poisoning of indexes; supply-chain of prompts/tools
- Responsible AI at a practical level (bias slices, audit traces)

**Nice-to-have:** dual-LLM patterns, full threat-model papers.

**Stems**
- “Retrieved wiki page says ‘ignore previous instructions.’ Architecture fix?”
- “Which of these 4 guardrail placements actually reduces refund-tool abuse?”

---

### 8. Modeling choices + classical ML refresh
**Why:** you still get “fine-tune or RAG?”, plus classic ML if the role is hybrid or the interviewer is an ML engineer.

**Must-have**
- Prompt / RAG / LoRA-fine-tune / continued pretrain: data need, cost, latency, freshness, control
- LoRA/QLoRA at conceptual level; catastrophic forgetting
- Distillation; when a small classifier beats an LLM
- Supervised vs unsupervised vs RL at interview depth
- Metrics: precision/recall/F1/AUC; when accuracy lies; class imbalance
- Overfitting, leakage, leakage via retrieval, leakage via eval set
- Feature stores / batch vs real-time scoring (hybrid roles)
- Simple recsys / ranking intuition

**Nice-to-have:** deriving backprop, XGBoost internals, full RLHF math (DPO/GRPO only if the job is post-training).

**Your strength:** MS DS + MLA-C02 Domain 2. Keep this **thin but sharp**. Do not rebuild a full ML master’s question bank.

---

## Likely coverage vs gaps for *you*

| Domain | You probably already have | Interview gap to close |
|---|---|---|
| Cloud MLOps, Bedrock/SageMaker, CI/CD, monitoring | Strong (MLA-C02) | Vendor-neutral design; numbers without the console |
| Data prep, embeddings, vector DB *setup* | Strong | Retrieval *debugging* and IR metrics |
| Classical ML / stats | Strong (MS) | Translate to LLM evals and leakage via RAG |
| Backend APIs, reliability, data stores | Strong | Apply to streaming tokens, tool side effects, cost |
| LLM internals, KV cache, sampling | Thin | Mechanism → latency/cost |
| Eval harnesses | Thin unless in your project | This is a hiring signal |
| Agents as production systems | Thin | Failure compounding, not diagrams |
| Timed coding | Unknown | Screens are binary |

If you only have time for three technical bets besides coding: **RAG debug, evals, cost/latency design**.

---

## Question-bank structure that also feeds the project deep-dive

Use one schema so every item is reusable:

```text
id: rag-debug-014
domain: rag
subtopic: hybrid-search
difficulty: 2/5
format: mcq | debug | tradeoff | numerical | design | coding
interview_round: screen | fundamentals | system-design | project-deep-dive
from_project: true/false
stem: ...
options: ...          # for MCQ
answer: ...
why_wrong: ...        # distractor autopsy — this is where learning happens
follow_up: ...        # the interviewer question after you answer
project_story: ...    # 4-sentence STAR if this came from your build
```

**Rule:** at least **30% of items tagged `from_project: true`.** Those become your deep-dive answers.

Write project questions like:
- “I chose chunk size X. What would have broken if I chose Y?”
- “My eval set had N examples. What failure class was missing?”
- “This architecture costs $A/day. Which 2 levers cut 40%?”

That is how the bank doubles as interview talk-track.

---

## 8–12 week weighting

Assume ~10 focused hours/week. Adjust if you are already strong in coding.

| Weeks | Focus | Share |
|---|---|---|
| Ongoing | Coding (Python + medium DS/algo + 1 ML-flavored problem) | 25% |
| 1–4 | RAG + LLM fundamentals MCQ/debug | 30% |
| 3–7 | Evals + system design/LLMOps numericals | 25% |
| 6–10 | Agents + security | 12% |
| 8–12 | Classical ML refresh + full mock designs + project stories | 8% |

Practice cadence that matches how you learn:
- 20–30 MCQs (timed, no notes)
- Review *only wrong + lucky-guess*
- 1 debug scenario written out loud
- 2–3 days/week: 45 min coding
- 1x/week: 35 min system design from a prompt in your bank

Do not add a new domain until you can explain a wrong answer in one minute without looking.

---

## Deprioritize even if it is popular

Skip or keep to a one-pager unless the job description demands it:

- Training an LLM from scratch / CUDA kernels / compiler internals
- Every LangChain/LlamaIndex abstraction
- Paper-level transformer variants
- Kaggle feature-engineering marathons
- Deep RL, GANs, academic CV
- Comparing 8 vector databases feature-by-feature
- Kubernetes internals (unless platform/ML infra role)
- Memorizing AWS service limits you already passed on the exam

Cert trivia is a trap in interviews. They want **decision quality**.

---

## Minimum viable bank to start this week

Do not wait for a complete ontology. Create 8 folders and seed **10 questions each** (80 total):

1. `rag/`
2. `llm-fundamentals/`
3. `evals/`
4. `system-design-llmops/`
5. `agents/`
6. `coding/`
7. `security/`
8. `modeling-and-classical-ml/`

First 10 in each folder should be **MCQ + 1 debug**. Expand only where you miss.

If you want a next step, I can turn domain 1 (RAG) into a starter set of ~25 cert-style MCQs with close distractors, written against a generic resume-project (internal-docs assistant), so you have a template for the other seven folders.

