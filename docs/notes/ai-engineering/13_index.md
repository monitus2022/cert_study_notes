# Index

---

## Core AI Engineering Concepts
- Index covers backpropagation and trainable parameters, plus online and batch inference APIs.
- Batching topics include batch size, continuous batching, dynamic batching, and static batching.
- Benchmarks include comparative evaluation, data contamination detection, and domain-specific capability.
- Biases of AI as a judge and instruction-following criteria are indexed.

---

## Systems and Evaluation Topics
- Bottlenecks include autoregressive decoding, computational, compute-bound, memory, and scaling bottlenecks.
- Bits-per-byte (BPB) and bits-per-character (BPC) are indexed metrics.
- Retrieval topics include chunking, contextual retrieval, and comparing retrieval algorithms.
- Conversational feedback includes sentiment, error correction, regeneration, and early termination.

---

## Data and Dataset Engineering
- Data acquisition, annotation, curation, inspection, and organization are core dataset engineering tasks.
- Data processing includes cleaning/filtering, formatting, deduplication, and coverage checks.
- Data augmentation and synthesis include AI-powered synthesis, rule-based, simulation, and model distillation.
- Data verification and lineage address quality, privacy, contamination, and copyright concerns.

---

## Evaluation and Finetuning
- Evaluation methodology covers AI as judge, comparative ranking, exact evaluation, and functional correctness.
- Foundation model evaluation faces challenges: lack of standardization, scalability bottlenecks, and comparative vs absolute performance.
- Finetuning techniques include LoRA, PEFT, model merging, and multi-task finetuning.
- Finetuning decisions weigh domain-specific capability against reasons not to finetune; hyperparameters include batch size, learning rate, epochs.

---

## AI Engineering Architecture and Defensive Prompt Engineering
- AI engineering architecture includes pipeline orchestration, monitoring, observability, and drift detection.
- Guardrails, model routers, gateways, and caching (exact and semantic) improve control and latency.
- Defensive prompt engineering addresses jailbreaking, prompt injection, and automated attacks.
- Defenses operate at prompt, model, and system levels.

---

## Core AI Engineering Concepts
- Model architectures include H3 and Jamba; hallucinations stem from the probabilistic nature of AI.
- Finetuning and RAG require factual consistency metrics; superficial imitation is a challenge.
- Model selection uses hashing, deduplication, HellaSwag, and public leaderboards.
- Embedding-based retrieval uses HNSW, IVF, and k-NN; term-based retrieval uses IDF.

---

## Inference Optimization and Performance
- AI accelerators have computational capabilities, memory size/bandwidth, and power consumption.
- Inference performance metrics: latency (TTFT, TPOT), throughput/goodput, utilization (MFU, MBU).
- Optimization techniques: batching, decoupling prefill/decode, parallelism, prompt caching, KV cache.
- Model optimization includes kernels/compilers, attention mechanism optimization, quantization, compression.

---

## Security and Advanced Topics
- Jailbreaking includes automated attacks, direct manual prompt hacking, and indirect prompt injection.
- Instruction-following criteria and capability are evaluated with IFEval and INFOBench.
- Information retrieval optimization involves chunking strategy, contextual retrieval, query rewriting, reranking.
- Knowledge augmentation and knowledge-augmented verification support factual consistency.

---

## Language Modeling Metrics
- Language modeling metrics are covered under "Understanding Language Modeling Metrics."
- Perplexity has its own entry plus "Perplexity Interpretation and Use Cases."
- Related metrics include cross entropy, entropy, bits-per-character, and bits-per-byte.
- Bits-per-character and bits-per-byte are grouped together in the index.

---

## Models, Training, and Efficiency
- Language models are traced from large language models to foundation models.
- Large multimodal model (LMM) appears under that same foundation-model discussion.
- LoRA entries cover configurations, why LoRA works, low-rank factorization, and serving LoRA adapters.
- Related efficiency topics: quantized LoRA (QLoRA), inference quantization, model distillation, and learning rate.

---

## Evaluation, Latency, and Retrieval
- LLM-as-a-judge is indexed under "AI as a Judge," cross-referenced with AI-as-a-judge.
- Latency topics include inference performance, TTFT, TPOT, and AI judges' increased costs and latency.
- Logs and traces, plus logprobs, support evaluation and sampling discussions.
- Locality-sensitive hashing (LSH) appears under embedding-based retrieval.

---

## Model Architecture and Selection
- Mamba architecture appears under Other model architectures in the index
- Model selection covers build versus buy and open source versus model APIs
- Model size topics include scaling bottlenecks, scaling extrapolation, and compute-optimal scaling laws
- Model merging techniques include concatenation, layer stacking, and summing

---

## Memory and Performance Metrics
- Memory topics include internal knowledge, long-term memory, and short-term memory
- Memory math covers memory needed for inference and memory needed for training
- Memory bottlenecks include bandwidth-bound issues and quantization
- Quantization is split into inference quantization and training quantization

---

## Evaluation and Monitoring
- Metrics cover AI as a judge, generation capability, and hallucination measurement
- Similarity measurements compare reference-based versus reference-free approaches
- Monitoring and observability track MTTD and MTTR
- Public leaderboards include Massive Multitask Language Understanding (MMLU)

---

## Prompt Engineering and Defense
- Prompt engineering basics: context length, in-context learning, best practices, iterating, organizing prompts.
- Defensive prompt engineering covers jailbreaking, prompt injection, direct and indirect attacks.
- Defenses include prompt-level and system-level strategies against prompt attacks.
- Proprietary prompts and reverse prompt engineering are also addressed.

---

## Model Deployment and Optimization
- Online and batch inference APIs; on-device deployment trade-offs.
- Open source models versus model APIs: cost, control, access, transparency, privacy, performance.
- Optimization techniques: quantization (inference, training, QAT, QLoRA), LoRA, PEFT.
- Parallel decoding, kernels and compilers, and parallelism improve efficiency.

---

## Evaluation, Data, and Training
- Evaluation uses public benchmarks, leaderboards, reward models, pairwise comparison, and bias analysis.
- Data concerns include lineage, copyright, privacy, quality control, and synthesis techniques.
- Training covers post-training, supervised and preference finetuning, PPO, and potential model collapse.
- Retrieval optimization includes query rewriting, embedding-based retrieval, and product quantization.

---

## RAG and Variants
- RAG architecture covers retrieval-augmented generation.
- RAG beyond texts includes multimodal RAG and RAG with tabular data.
- Finetuning and RAG are related topics.
- RAG-RAG with tabular data finetuning is mentioned.

---

## Retrieval Algorithms and Optimization
- Retrieval algorithms include combining and comparing retrieval algorithms.
- Embedding-based retrieval and term-based retrieval are types.
- Retrieval optimization covers chunking strategy, contextual retrieval, query rewriting, and reranking.
- Sparse versus dense retrievers are compared.

---

## Evaluation and Related Concepts
- Reference-based and reference-free metrics evaluate similarity against reference data.
- Ranking models use comparative evaluation; judges can be reference-based.
- RLHF, reward models, and preference finetuning are covered.
- Roleplaying, routers, and rule-based data synthesis are also indexed.

---

## Sampling and Generation
- Sampling fundamentals, strategies, stopping condition, temperature, top-k, top-p.
- Structured outputs, constrained sampling, and speculative decoding.
- Hallucination tied to probabilistic nature of AI.
- Test time compute and scaling bottlenecks.

---

## Evaluation and Safety
- Evaluation criteria: safety, cost and latency, domain-specific capability, generation, instruction-following.
- Evaluation pipeline: guidelines, methods, data, scoring rubrics, system components.
- Self-evaluation, models as judges, self-verification, factual consistency.
- System-level defense and safety as evaluation criteria.

---

## Model Development and Optimization
- Finetuning: SFT, PEFT, sequential finetuning, model merging (SLERP, linear combination, pruning).
- Model selection: build vs buy, public benchmarks, data contamination, custom leaderboards.
- Scaling law, compute-optimal models, scaling extrapolation.
- Memory, retrieval algorithms, semantic caching, parallelism.

---

## Evaluation and Performance Metrics
- Task-based and turn-based evaluation assess system components; TruthfulQA appears in public leaderboards.
- Latency metrics include TTFT, TPOT, TBT; throughput and goodput are also covered.
- Setting expectations involves latency, TTFT, and TPOT.
- Top-k and top-p are sampling parameters.

---

## Model Architecture and Training
- Transformer architecture includes attention mechanism, transformer blocks with attention, MLP, embedding, and output layers.
- Tokenization, tokenizer, and tokens relate to language models and model size.
- Training involves backpropagation, trainable parameters, training data, and training quantization.
- Domain-specific and multilingual models use training data; transfer learning connects to finetuning.

---

## Retrieval and Structured Outputs
- Term frequency (TF) and term-based retrieval relate to chunking strategy and tokenization.
- Text-to-SQL and structured outputs involve functional correctness and RAG with tabular data.
- Tool use and tool selection are covered.
- Logs and traces are referenced.

---

## Data, Memory, and Use Case Evaluation
- Unstructured data relates to data organization and memory.
- Use case evaluation connects to AI product defensibility and usefulness threshold.
- Use case evaluation also links to setting expectations.
- These topics frame early decisions in AI engineering.

---

## User Feedback: Types and Design
- User feedback connects to degenerate feedback loops.
- Conversational feedback extraction relates to dialogue diversity.
- Natural language feedback includes sentiment and other conversational feedback.
- Feedback design covers how and when to collect feedback.

---

## Feedback Limitations, Vectors, and Models
- Feedback limitations connect to degenerate feedback loops and biases.
- Value vector (V) relates to the attention mechanism.
- Vector databases connect to embedding-based retrieval; vectorization relates to kernels and compilers.
- Vocabulary connects to perplexity interpretation; language models are defined under vocabulary.

---

## Index Terms: W

- WinoGrande appears as an indexed term in this chapter.
- Public leaderboards are indexed under workflow automation.
- Workflow automation is a cross-referenced index entry.
- Write actions are indexed and cross-referenced.

---

## Cross-References

- Workflow automation links to public leaderboards.
- Write actions appear as a linked index entry.
- Index entries use cross-references to connect related terms.

---

## Zero-Shot Learning — Index Entry

- Zero-shot learning appears in the index under the letter **Z**.
- It is cross-referenced to "In-Context Learning: Zero-Shot and Few-Shot".
- The related section is also titled "Context Learning: Zero-Shot and Few-Shot".
- The index points readers to that section for the term.

---

## Note from the Index

- The index entry carries the source attribution "_OceanofPDF.com_".
- No further details on zero-shot learning appear in this section.
- For substantive coverage, consult the cross-referenced in-context learning section.

## Practice Questions

### Question 1: Which of the following is listed as a foundation model use case in...

Which of the following is listed as a foundation model use case in the source index?

- [ ] A) Coding
- [ ] B) Power consumption
- [ ] C) Contextual retrieval
- [ ] D) Prompt caching

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** A

    **Explanation:** The index lists Coding under “Foundation Model Use Cases.” The other options are separate index entries outside that list.

### Question 2: Which set of limitations is listed under AI-as-a-judge in the sourc...

Which set of limitations is listed under AI-as-a-judge in the source index?

- [ ] A) Biases, criteria ambiguity, inconsistency, increased costs and latency
- [ ] B) Tool failures, planning failures, efficiency
- [ ] C) Power consumption, memory size and bandwidth
- [ ] D) Finetuning, LoRA, concatenation

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** A

    **Explanation:** The index lists biases, criteria ambiguity, inconsistency, and increased costs and latency under “Limitations of AI as a Judge.” The other sets are not listed there.

### Question 3: In the source index, “AI Engineering Versus ML Engineering” is asso...

In the source index, “AI Engineering Versus ML Engineering” is associated with which section?

- [ ] A) AI interface
- [ ] B) Three Layers of the AI Stack
- [ ] C) Prompt caching
- [ ] D) Adapters

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** A

    **Explanation:** The index entry “AI engineering versus ML engineering” points to “AI Engineering Versus ML Engineering-AI interface.” The other options are separate index entries.

### Question 4: Which entry is listed under accelerators in the source index?

Which entry is listed under accelerators in the source index?

- [ ] A) Power consumption
- [ ] B) Milestone planning
- [ ] C) Agent failure modes and evaluation
- [ ] D) Data organization

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** A

    **Explanation:** The index lists “Power consumption” under accelerators. The other options appear as separate entries elsewhere in the index.

### Question 5: According to the index, which term is cross-referenced with “Give t...

According to the index, which term is cross-referenced with “Give the Model Time to Think”?

- [ ] A) chain-of-thought (CoT)
- [ ] B) continuous batching
- [ ] C) constrained sampling
- [ ] D) cross entropy

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** A

    **Explanation:** The index lists “chain-of-thought (CoT), Give the Model Time to Think-Give the Model Time to Think, Data Curation.”

### Question 6: Which index entry covers both bits-per-character and bits-per-byte?

Which index entry covers both bits-per-character and bits-per-byte?

- [ ] A) Bits-per-Character and Bits-per-Byte
- [ ] B) Cross Entropy
- [ ] C) Context Length and Context Efficiency
- [ ] D) Batching

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** A

    **Explanation:** The index lists “bits-per-byte (BPB), Bits-per-Character and Bits-per-Byte” and “bits-per-character (BPC), Bits-per-Character and Bits-per-Byte.”

### Question 7: Which of the following is listed as a type of bottleneck in the index?

Which of the following is listed as a type of bottleneck in the index?

- [ ] A) computational bottlenecks
- [ ] B) conversational bottlenecks
- [ ] C) copyright bottlenecks
- [ ] D) criteria bottlenecks

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** A

    **Explanation:** The index includes “computational bottlenecks, Computational bottlenecks-Computational bottlenecks” along with related memory and scaling bottlenecks.

### Question 8: According to the index, which problem is listed under limitations o...

According to the index, which problem is listed under limitations of data synthesis?

- [ ] A) Potential model collapse
- [ ] B) Exact caching
- [ ] C) Goodput
- [ ] D) Grouped-query attention

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** A

    **Explanation:** The index lists “potential model collapse” under data synthesis limitations.

### Question 9: Which of the following is listed as a category of prompt attack def...

Which of the following is listed as a category of prompt attack defense?

- [ ] A) Model-level defense
- [ ] B) Semantic caching
- [ ] C) Drift detection
- [ ] D) Data flywheel

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** A

    **Explanation:** The index lists model-level defense, prompt-level defense, and system-level defense under prompt attack defense.

### Question 10: Which topic is listed under finetuning memory bottlenecks?

Which topic is listed under finetuning memory bottlenecks?

- [ ] A) Backpropagation and trainable parameters
- [ ] B) Exact caching
- [ ] C) Elo
- [ ] D) Data lineage

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** A

    **Explanation:** The index lists backpropagation and trainable parameters, memory math, numerical representations, and quantization under memory bottlenecks.

### Question 11: According to the index, which term is cross-referenced with “Embedd...

According to the index, which term is cross-referenced with “Embedding-based retrieval”?

- [ ] A) HNSW
- [ ] B) IDF
- [ ] C) IFEval
- [ ] D) HellaSwag

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** A

    **Explanation:** The index lists “hierarchical navigable small world (HNSW), Embedding-based retrieval.” IDF is linked to term-based retrieval, IFEval to instruction-following criteria, and HellaSwag to public leaderboards.

### Question 12: According to the index, which item is cross-referenced with “Public...

According to the index, which item is cross-referenced with “Public leaderboards”?

- [ ] A) HellaSwag
- [ ] B) HNSW
- [ ] C) IFEval
- [ ] D) IDF

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** A

    **Explanation:** The index entry reads “HellaSwag, Public leaderboards.” The other terms are linked to different topics in the index.

### Question 13: According to the index, which term is cross-referenced with “Term-b...

According to the index, which term is cross-referenced with “Term-based retrieval”?

- [ ] A) IDF (inverse document frequency)
- [ ] B) HNSW
- [ ] C) HellaSwag
- [ ] D) IFEval

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** A

    **Explanation:** The index lists “IDF (inverse document frequency), Term-based retrieval.” HNSW is linked to embedding-based retrieval, HellaSwag to public leaderboards, and IFEval to instruction-following criteria.

### Question 14: According to the index, which entry is cross-referenced with “LLM-a...

According to the index, which entry is cross-referenced with “LLM-as-a-judge”?

- [ ] A) AI as a Judge
- [ ] B) AI product defensibility
- [ ] C) Data synthesis
- [ ] D) Model distillation

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** A

    **Explanation:** The index lists “LLM-as-a-judge, AI as a Judge (see also AI-as-a-judge).”

### Question 15: Which of the following is listed in the index as a language modelin...

Which of the following is listed in the index as a language modeling metric?

- [ ] A) TTFT
- [ ] B) bits-per-byte
- [ ] C) LoRA
- [ ] D) LSH

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** The index lists bits-per-byte under language modeling metrics.

### Question 16: What does the index say LoRA stands for?

What does the index say LoRA stands for?

- [ ] A) Low-rank adaptation
- [ ] B) Locality-sensitive hashing
- [ ] C) Large multimodal model
- [ ] D) Logit vectors

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** A

    **Explanation:** The index entry reads “LoRA (low-rank adaptation).”

### Question 17: According to the index, what does MTTD stand for?

According to the index, what does MTTD stand for?

- [ ] A) mean time to detection
- [ ] B) model bandwidth utilization
- [ ] C) mean time to response
- [ ] D) model FLOPs utilization

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** A

    **Explanation:** The index lists "mean time to detection (MTTD)" under Monitoring and Observability.

### Question 18: Which technique is listed under model merging in the index?

Which technique is listed under model merging in the index?

- [ ] A) speculative decoding
- [ ] B) layer stacking
- [ ] C) KV cache size optimization
- [ ] D) model distillation

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** The index lists "layer stacking" under model merging, along with concatenation and summing.

### Question 19: What does MBU stand for according to the index?

What does MBU stand for according to the index?

- [ ] A) model bandwidth utilization
- [ ] B) mean time to response
- [ ] C) massive multitask language understanding
- [ ] D) model FLOPs utilization

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** A

    **Explanation:** The index lists "MBU (model bandwidth utilization)" under Utilization, MFU, and MBU.

### Question 20: According to the index, what does QLoRA stand for?

According to the index, what does QLoRA stand for?

- [ ] A) Quantized LoRA
- [ ] B) Quantization-aware training
- [ ] C) Queries per second
- [ ] D) Proximal policy optimization

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** A

    **Explanation:** The source lists “QLoRA (quantized LoRA)” and “quantized LoRA (QLoRA).”

### Question 21: Which abbreviation is defined in the index as “queries per second”?

Which abbreviation is defined in the index as “queries per second”?

- [ ] A) QPS
- [ ] B) QAT
- [ ] C) PPO
- [ ] D) QLoRA

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** A

    **Explanation:** The source lists “QPS (queries per second)” and “queries per second (QPS).”

### Question 22: Which topic is associated with “prefilling, decoupling from decodin...

Which topic is associated with “prefilling, decoupling from decoding” in the index?

- [ ] A) Decoupling prefill and decode
- [ ] B) Prompt caching
- [ ] C) Parallel decoding
- [ ] D) Operator fusion

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** A

    **Explanation:** The source lists “prefilling, decoupling from decoding, Decoupling prefill and decode.”

### Question 23: According to the index, which of the following is listed as a RAG v...

According to the index, which of the following is listed as a RAG variant?

- [ ] A) multimodal RAG
- [ ] B) term-based retrieval
- [ ] C) replica parallelism
- [ ] D) reverse prompt engineering

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** A

    **Explanation:** The index lists “multimodal RAG” as an entry, while the other options are separate topics.

### Question 24: In the index, RLHF is cross-referenced with which section?

In the index, RLHF is cross-referenced with which section?

- [ ] A) Preference Finetuning
- [ ] B) Router
- [ ] C) Roleplaying
- [ ] D) Transformer architecture

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** A

    **Explanation:** The index entry for RLHF points to “Preference Finetuning-Finetuning using the reward model.”

### Question 25: In the index, recurrent neural networks (RNNs) are cross-referenced...

In the index, recurrent neural networks (RNNs) are cross-referenced with which section?

- [ ] A) Transformer architecture
- [ ] B) RAG Architecture
- [ ] C) Retrieval Optimization
- [ ] D) Rule-based data synthesis

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** A

    **Explanation:** The index lists “recurrent neural networks (RNNs), Transformer architecture.”

### Question 26: Which of the following is listed as a retrieval optimization topic...

Which of the following is listed as a retrieval optimization topic in the index?

- [ ] A) Chunking strategy
- [ ] B) Reward models
- [ ] C) Routers
- [ ] D) Roleplaying

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** A

    **Explanation:** The index includes “chunking strategy” among retrieval optimization-related entries such as contextual retrieval, query rewriting, and reranking.

### Question 27: Which of the following is listed as a sampling strategy in the sour...

Which of the following is listed as a sampling strategy in the source text?

- [ ] A) Top-k
- [ ] B) SLERP
- [ ] C) SFT
- [ ] D) SQL queries

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** A

    **Explanation:** The source lists top-k under sampling strategies.

### Question 28: Which technique is associated with model merging and multi-task fin...

Which technique is associated with model merging and multi-task finetuning in the source text?

- [ ] A) Top-p
- [ ] B) Spherical linear interpolation (SLERP)
- [ ] C) Semantic caching
- [ ] D) Speculative decoding

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** The source lists spherical linear interpolation (SLERP) under Model Merging and Multi-Task Finetuning.

### Question 29: Which of the following is listed as a PEFT technique in the source...

Which of the following is listed as a PEFT technique in the source text?

- [ ] A) Soft prompt-based PEFT methods
- [ ] B) Static batching
- [ ] C) Structured outputs
- [ ] D) Superficial imitation

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** A

    **Explanation:** The source lists soft prompt-based PEFT methods under PEFT techniques.

### Question 30: Which of the following is listed as an evaluation criterion for sys...

Which of the following is listed as an evaluation criterion for systems evaluation in the source text?

- [ ] A) Cost and latency
- [ ] B) Top-k
- [ ] C) SLERP
- [ ] D) Static features

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** A

    **Explanation:** The source lists cost and latency under evaluation criteria for systems evaluation.

### Question 31: In the index, what does TPOT stand for?

In the index, what does TPOT stand for?

- [ ] A) time per output token
- [ ] B) time between tokens
- [ ] C) time to first token
- [ ] D) task-based evaluation

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** A

    **Explanation:** The source lists “time per output token (TPOT)” and also references TPOT under latency-related entries.

### Question 32: Which term is cross-referenced with “Term-based retrieval” in the i...

Which term is cross-referenced with “Term-based retrieval” in the index?

- [ ] A) term frequency (TF)
- [ ] B) top-k
- [ ] C) top-p
- [ ] D) tool use

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** A

    **Explanation:** The source lists “term frequency (TF), Term-based retrieval,” linking term frequency to term-based retrieval.

### Question 33: Which benchmark is listed under “Public leaderboards” in the index?

Which benchmark is listed under “Public leaderboards” in the index?

- [ ] A) TruthfulQA
- [ ] B) TBT
- [ ] C) TTFT
- [ ] D) TPOT

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** A

    **Explanation:** The source lists “TruthfulQA, Public leaderboards,” indicating TruthfulQA is associated with public leaderboards.

### Question 34: In the index, which entry is listed alongside “unstructured data”?

In the index, which entry is listed alongside “unstructured data”?

- [ ] A) Data Organization
- [ ] B) Attention mechanism
- [ ] C) Perplexity Interpretation and Use Cases
- [ ] D) Feedback Design

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** A

    **Explanation:** The source lists “unstructured data, Data Organization, Memory.”

### Question 35: Which topic is cross-referenced with “extracting conversational fee...

Which topic is cross-referenced with “extracting conversational feedback” in the index?

- [ ] A) Dialogue diversity
- [ ] B) Degenerate feedback loop
- [ ] C) Kernels and compilers
- [ ] D) Language models

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** A

    **Explanation:** The source lists “extracting conversational feedback, Extracting Conversational Feedback-Dialogue diversity.”

### Question 36: According to the index, “feedback limitations” is cross-referenced...

According to the index, “feedback limitations” is cross-referenced to which entry?

- [ ] A) Feedback Limitations-Degenerate feedback loop
- [ ] B) Feedback Design-How to collect feedback
- [ ] C) When to collect feedback
- [ ] D) Other conversational feedback-Dialogue diversity

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** A

    **Explanation:** The source lists “feedback limitations, Feedback Limitations-Degenerate feedback loop.”

### Question 37: In the index, "Public leaderboards" is listed as a subentry under w...

In the index, "Public leaderboards" is listed as a subentry under which main entry?

- [ ] A) WinoGrande
- [ ] B) Workflow Automation
- [ ] C) Write actions
- [ ] D) Public leaderboards

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** A

    **Explanation:** The index line reads "WinoGrande, Public leaderboards," showing Public leaderboards nested under WinoGrande.

### Question 38: According to the index, "Write actions" appears as a subentry of wh...

According to the index, "Write actions" appears as a subentry of which term?

- [ ] A) Workflow Automation
- [ ] B) WinoGrande
- [ ] C) Public leaderboards
- [ ] D) W

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** A

    **Explanation:** The entry reads "workflow automation, Write actions," indicating Write actions is a subentry under Workflow Automation.

### Question 39: Under which index letter heading do the entries "WinoGrande" and "W...

Under which index letter heading do the entries "WinoGrande" and "Workflow Automation" appear?

- [ ] A) W
- [ ] B) V
- [ ] C) X
- [ ] D) Y

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** A

    **Explanation:** Both entries are listed in the section headed "W" in the index.

### Question 40: In the index, under which heading is "zero-shot learning" listed?

In the index, under which heading is "zero-shot learning" listed?

- [ ] A) In-Context Learning: Zero-Shot and Few-Shot
- [ ] B) Fine-Tuning and Transfer Learning
- [ ] C) Prompt Engineering Basics
- [ ] D) Retrieval-Augmented Generation

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** A

    **Explanation:** The index entry reads "zero-shot learning, In-Context Learning: Zero-Shot and Few-Shot," pointing to that section.

### Question 41: The index entry for zero-shot learning points to a section whose ti...

The index entry for zero-shot learning points to a section whose title names which two learning approaches?

- [ ] A) Zero-shot and few-shot
- [ ] B) Supervised and unsupervised
- [ ] C) Batch and online
- [ ] D) Reinforcement and imitation

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** A

    **Explanation:** The referenced section is titled "In-Context Learning: Zero-Shot and Few-Shot," naming zero-shot and few-shot learning.

### Question 42: Under which letter heading does the zero-shot learning index entry...

Under which letter heading does the zero-shot learning index entry appear?

- [ ] A) Z
- [ ] B) A
- [ ] C) I
- [ ] D) O

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** A

    **Explanation:** The entry is listed beneath the bold heading "Z" in the index.
