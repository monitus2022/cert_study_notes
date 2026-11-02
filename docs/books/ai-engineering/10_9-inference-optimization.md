# 9. Inference Optimization

---

## Why Inference Optimization Matters
- New models come and go, but making them better, cheaper, and faster stays relevant.
- A model that is too slow loses user patience or makes predictions useless.
- A model that is too expensive delivers poor return on investment.
- This chapter focuses on making models faster and cheaper, not better.

---

## Levels of Optimization
- Inference optimization happens at three levels: model, hardware, and service.
- Model level: reduce trained model size or design more efficient architectures.
- Hardware level: design more powerful hardware, such as AI accelerators.
- Service level: run models on given hardware, optimizing for usage and traffic patterns.

---

## Trade-offs and Practical Value
- Inference optimization is interdisciplinary, involving model researchers, developers, system engineers, and hardware architects.
- Some techniques help both speed and cost, such as reducing model precision.
- Often optimization requires trade-offs, like faster hardware at higher cost.
- Even without implementing these techniques, understanding them helps evaluate inference services and frameworks.

---

## Training vs. Inference

- Two distinct phases in an AI model's lifecycle: training and inference.
- Training is the process of building a model.
- Inference is using a model to compute an output for a given input.
- Unless you train or finetune, you'll mostly care about inference.

---

## Inference Server

- In production, the component that runs model inference is the inference server.
- It hosts available models and has access to necessary hardware.
- It allocates resources based on application requests, such as user prompts.
- It executes the appropriate models and returns responses to users.

---

## Inference Service

- An inference server is part of a broader inference service.
- The service receives, routes, and possibly preprocesses requests.
- Preprocessing happens before requests reach the inference server.
- This section introduces shared vocabulary used throughout the chapter.

---

## Inference Overview

- Training builds a model; inference uses a model to compute an output for a given input.
- An inference server hosts models, allocates hardware, and returns responses to applications.
- An inference service also receives, routes, and may preprocess requests before the server.
- Model APIs from OpenAI and Google are inference services; self-hosting means building your own.

---

## Computational Bottlenecks

- Compute-bound tasks are limited by computation needed; memory bandwidth-bound tasks are limited by data transfer rate.
- Arithmetic intensity is arithmetic operations per byte of memory access; roofline charts classify workloads.
- Image generators like Stable Diffusion are typically compute-bound; autoregressive language model inference is typically memory bandwidth-bound.
- Compute-bound workloads may benefit from more chips or higher FLOP/s; bandwidth-bound workloads from higher bandwidth.

---

## Prefill and Decode

- Prefill processes input tokens in parallel, limited by operations hardware can execute; it is compute-bound.
- Decode generates one output token at a time, loading large matrices into GPUs; it is memory bandwidth-bound.
- Because their computational profiles differ, prefill and decode are often decoupled onto separate machines.
- Context length, output length, and batching strategies affect the amount of prefill and decode computation.

---

## Online and Batch Inference APIs

- Online APIs optimize for latency, processing requests as soon as they arrive.
- Batch APIs optimize for cost, allowing batching and cheaper hardware when latency requirements are loose.
- Batch use cases include synthetic data generation, periodic reporting, onboarding, model migration, and reindexing.
- Streaming mode returns each token as generated, reducing wait time but risking users seeing bad responses.

---

## Latency Metrics
- Latency: time from query to complete response; for autoregressive streaming, split into TTFT and TPOT.
- TTFT measures first token after query, corresponds to prefill, depends on input length.
- TPOT measures each output token after first; total latency = TTFT + TPOT × output tokens.
- Average latency can mislead; use percentiles p50, p90, p95, p99 and plot TTFT vs input length.

---

## Throughput and Goodput
- Throughput: output tokens per second across all users; input and output throughput should be counted separately.
- Throughput also measured as completed requests per second (RPS) or per minute (RPM).
- Higher throughput typically lowers compute cost; batching can improve throughput but reduce latency.
- Goodput measures requests per second satisfying the SLO, e.g., TTFT ≤200 ms and TPOT ≤100 ms.

---

## Utilization: MFU and MBU
- GPU utilization from nvidia-smi is percentage of time GPU actively processes tasks, not efficiency.
- MFU is observed throughput relative to theoretical maximum throughput at peak FLOP/s.
- MBU measures percentage of achievable memory bandwidth used; bandwidth = parameter count × bytes/param × tokens/s.
- Compute-bound workloads typically have higher MFU and lower MBU; bandwidth-bound workloads show lower MFU and higher MBU.

---

## What Is an AI Accelerator?
- Accelerator: chip designed to speed up a specific computational workload; AI accelerators target AI workloads.
- GPUs dominate AI accelerators; NVIDIA is the biggest economic driver of the early 2020s AI boom.
- CPUs have few powerful cores for sequential, general-purpose tasks and high single-thread performance.
- GPUs have thousands of smaller cores for parallel tasks; matrix multiplication is highly parallelizable.

---

## Specialized Inference Chips
- Inference can exceed training cost, accounting for up to 90% of ML costs in deployed systems.
- Training needs more memory and higher precision; inference emphasizes minimizing latency.
- Inference chips optimize for lower precision and faster memory access, not large memory capacity.
- Examples: Apple Neural Engine, AWS Inferentia, MTIA, Google Edge TPU, NVIDIA Jetson Xavier.

---

## Key Chip Characteristics
- Computational capability measured by peak FLOP/s; actual-to-theoretical ratio is a utilization metric.
- Higher precision means fewer operations per second; H100 specs vary by precision format.
- Memory matters: size and bandwidth across CPU DRAM, GPU HBM, and on-chip SRAM.
- Power consumption: maximum power draw and TDP indicate expected energy use and heat.

---

## Selecting Accelerators
- Match chips to workload: compute-bound workloads favor more FLOP/s; memory-bound favor bandwidth and memory.
- Three questions: can the hardware run your workloads, how long does it take, how much does it cost?
- FLOP/s, memory size, and memory bandwidth answer the first two questions.
- Cloud pricing is usage-based and similar across providers; buying adds initial price plus power costs.

---

## Levels of Inference Optimization

- Inference optimization can be applied at three levels: model, hardware, or service.
- Model-level optimization is like crafting better arrows.
- Hardware-level optimization is like training a stronger, better archer.
- Service-level optimization is like refining the entire shooting process, including bow and aiming conditions.

---

## Quality Trade-offs in Optimization

- Ideally, optimizing a model for speed and cost shouldn’t change model quality.
- However, many optimization techniques might cause model degradation.
- Different inference service providers may show slight model quality variations.
- Figure 9-8 compares the same Llama models on benchmarks across providers.

---

## Scope of Optimization Techniques
- Hardware design is outside the scope of this book
- Focus is on techniques at the model and service levels
- Techniques are discussed separately for clarity
- In production, optimization typically involves techniques at more than one level

---

## Model Optimization: Overview

- Model-level optimization makes the model more efficient by modifying the model itself
- Modifying the model can alter its behavior
- Many foundation models follow the transformer architecture
- They include an autoregressive language model component

---

## Why Inference Is Resource-Intensive

- Three characteristics make inference resource-intensive
- Model size
- Autoregressive decoding
- The attention mechanism
- Approaches exist to address each of these challenges

---

## Model Compression: Pruning

- Model compression reduces model size, which can also make it faster.
- Quantization (Chapter 7) lowers precision; distillation (Chapter 8) trains a small model to mimic a large one.
- Pruning has two meanings: removing entire nodes (changing architecture) or zeroing least-useful parameters.
- Zeroing parameters keeps the parameter count but increases sparsity, reducing storage and speeding computation.

---

## Pruning: Results and Practical Limits

- Pruned models can be used as-is or finetuned to restore performance lost to pruning.
- Pruning can reveal promising smaller architectures, which can also be trained from scratch.
- Frankle and Carbin (2019) reduced non-zero parameters of certain networks by over 90% without compromising accuracy.
- In practice pruning is less common: it's harder, gains less, and sparse models need supporting hardware.

---

## What's Most Used

- Weight-only quantization is by far the most popular: easy to use, works out of the box, extremely effective.
- Reducing precision from 32 bits to 16 bits halves the memory footprint.
- Quantization is near its limit—we can't go below 1 bit per value.
- Distillation is also common, yielding a smaller model comparable to a much larger one for your needs.

---

## The Autoregressive Decoding Bottleneck
- Autoregressive language models generate one token after another.
- Generating 100 tokens at 100 ms each takes 10 seconds.
- This process is both slow and expensive.
- Small improvements in generation can significantly improve user experience.

---

## Why Output Tokens Matter
- Output tokens cost approximately two to four times an input token across API providers.
- Anyscale found one output token can impact latency like 100 input tokens.
- Techniques to overcome this bottleneck are rapidly evolving.
- Future architectures may avoid this bottleneck entirely.

---

## Speculative Decoding Process
- Draft model proposes K tokens; target model verifies them in parallel.
- Target accepts longest left-to-right subsequence it agrees with.
- If j tokens accepted, target generates one extra token, then loop repeats.
- Output is 1 token if none accepted, K+1 if all accepted.

---

## Why Speculative Decoding Works
- Verification is parallelizable, faster than sequential generation; decoding becomes like prefilling.
- Some tokens are easier to predict; a weaker draft model can achieve high acceptance.
- Decoding is memory bandwidth-bound; idle FLOPs enable free verification.
- Acceptance rate is domain-dependent; structured text like code has higher acceptance.

---

## Practical Considerations
- Larger K means fewer target verification calls but lower draft acceptance rate.
- Draft model should share vocabulary and tokenizer with target; can be custom or existing.
- Example: Chinchilla-70B with 4B draft model gave 8x faster token generation, >50% latency reduction.
- Easy to implement, no quality change; supported in vLLM, TensorRT-LLM, llama.cpp.

---

## Inference with Reference

- Responses often repeat tokens from input: quoting documents, fixing code, multi-turn chat.
- Instead of generating repeated tokens, copy them from the input to speed up generation.
- Similar to speculative decoding, but draft tokens are selected from the input, not a model.
- Key challenge: identify the most relevant text span from context at each decoding step.

---

## How It Works and When to Use It

- Simplest approach: find a text span in the context that matches the current tokens.
- No extra model required, unlike speculative decoding.
- Useful only when context and output overlap significantly: retrieval, coding, multi-turn conversations.
- Yang et al. (2023) report two times generation speedup in such use cases.

---

## Parallel Decoding
- Breaks autoregressive sequential dependency by generating multiple future tokens simultaneously.
- Works because existing context often suffices to predict the next few tokens.
- Example: given "the cat sits," the following word "the" may be predictable without knowing "on/under/behind."
- Parallel tokens generated by same decoder (Lookahead decoding) or separate heads (Medusa).

---

## Medusa and Verification
- Medusa extends the frozen original model with multiple decoding heads, each predicting a future position.
- NVIDIA claimed Medusa boosted Llama 3.1 token generation up to 1.9× on HGX H200 GPUs.
- Parallel tokens must be verified for coherence, since they aren't generated sequentially.
- Medusa uses tree-based attention: each head produces options, organized into a tree to select the best sequence.

---

## Jacobi Decoding
- Lookahead decoding uses the Jacobi method to verify generated tokens.
- K future tokens are generated in parallel, then verified for coherence and consistency.
- Failed tokens are regenerated or adjusted individually rather than discarding all K.
- Refinement continues until all tokens pass verification and are integrated; this family is called Jacobi decoding.

---

## Attention Mechanism Optimization

- Generating token x_t needs key and value vectors for all previous tokens x_1 … x_t–1
- Generating x_t+1 needs those same vectors, plus the one for x_t
- Instead of recomputing earlier key/value vectors, reuse them from the previous step
- Only the most recent token's key and value vectors must be computed

---

## KV Cache

- The cache storing key and value vectors for reuse is called the KV cache
- Newly computed key and value vectors are added to the KV cache
- This avoids recomputing key and value vectors at each decoding step

---

## KV Cache: Inference-Only Mechanism

- KV cache is used only during inference, not training.
- In training, all tokens are known, so next-token generation is computed all at once.
- Attention computations grow exponentially with sequence length; KV cache size grows linearly.
- KV cache size also grows with larger batch sizes.

---

## Calculating KV Cache Size

- Memory = 2 × B × S × L × H × M.
- B: batch size; S: sequence length; L: transformer layers.
- H: model dimension; M: memory per value (e.g., FP16 or FP32).
- Example: LLama 2 13B, batch 32, sequence 2,048, 2 bytes → 54 GB.

---

## KV Cache Bottlenecks and Attention Optimization

- A 500B+ model with batch 512 and context 2048 can need a 3TB KV cache.
- Cache size is limited by hardware storage, bottlenecking long-context applications.
- Large caches take time to load, an issue for strict-latency applications.
- Techniques fall into three buckets: redesigning attention, optimizing KV cache, writing attention kernels.

---

## Redesigning Attention: Trade-offs

- These techniques alter the attention mechanism itself, so they require training or finetuning
- **Local windowed attention** attends only to a fixed window of nearby tokens
- Reduces effective sequence length, shrinking both KV cache and attention computation
- Example: 10,000-token sequences with a 1,000-token window cut KV cache 10x

---

## Reducing KV Cache Memory

- **Cross-layer attention** shares key-value vectors across adjacent layers
- Three layers sharing key-value vectors reduces the KV cache three times
- **Multi-query attention** shares key-value vectors across all query heads
- **Grouped-query attention** groups query heads and shares key-value pairs within each group

---

## Case: Character.AI

- Average conversation has a dialogue history of 180 messages
- With long sequences, KV cache size is the primary bottleneck for throughput
- Multi-query attention, interleaved local/global attention, and cross-layer attention cut KV cache over 20x
- Memory is no longer a bottleneck for serving large batch sizes

---

## KV Cache Management

- KV cache management is critical for mitigating the memory bottleneck during inference.
- Effective management enables larger batch sizes, especially for long-context applications.
- Many techniques are actively being developed to reduce and manage the KV cache.

---

## KV Cache Optimization Techniques

- vLLM gained popularity by introducing PagedAttention for optimized memory management.
- PagedAttention divides the KV cache into non-contiguous blocks and reduces fragmentation.
- It enables flexible memory sharing to improve LLM serving efficiency.
- Other techniques include KV cache quantization, adaptive KV cache compression, and selective KV cache.

---

## Kernel Optimization for Attention
- This approach optimizes how attention scores are computed, rather than changing mechanism design or storage.
- It is most effective when it accounts for the hardware executing the computation.
- A kernel is code optimized for a specific chip.
- Kernel writing is discussed further in the next section.

---

## FlashAttention
- FlashAttention is a well-known kernel optimized for attention computation (Dao et al., 2022).
- It fuses many operations commonly used in transformer-based models to run faster.
- Figure 9-13 illustrates FlashAttention fusing several common operators.

---

## Kernels for AI Hardware
- Kernels are specialized code optimized for accelerators such as GPUs and TPUs.
- They perform computationally intensive routines repeatedly, often in parallel, to maximize accelerator performance.
- Matrix multiplication, attention computation, and convolution have specialized kernels for efficient hardware computation.
- Writing kernels requires understanding memory hierarchy: caches, global/shared memory, and registers.

---

## Kernel Languages and Roles
- Kernels are written in low-level languages like CUDA, Triton, and ROCm.
- These languages enable fine-grained control over thread management and memory access.
- They are harder to learn than languages most AI engineers know, such as Python.
- Chip makers and AI frameworks employ optimization and kernel engineers for hardware/framework efficiency.

---

## Vectorization

- Applies to a loop or a nested loop
- Instead of processing one data element at a time, execute multiple elements simultaneously
- The elements processed together are contiguous in memory
- Reduces latency by minimizing data I/O operations

---

## Parallelization

- Divide an input array (or n-dimensional array) into independent chunks
- Chunks are processed simultaneously on different cores or threads
- Speeds up the computation

---

## Loop Tiling

- Optimizes the data accessing order in a loop
- Targets the hardware's memory layout and cache
- This optimization is hardware-dependent
- An efficient CPU tiling pattern may not work well on GPUs

---

## Operator Fusion and Kernels

- Operator fusion combines multiple operators into a single pass, avoiding redundant memory access.
- Fusing two loops over the same array reduces how often data is read and written.
- Fusion requires deep understanding of a model's specific operators and architecture, demanding more engineer attention.
- Kernels are hardware-specific: new architectures require new kernels, e.g., FlashAttention for A100, FlashAttention-3 for H100.

---

## Lowering and Compilers

- A model script specifies operations; running on hardware requires conversion to a compatible language.
- This conversion process is called *lowering*; a tool that lowers code is a compiler.
- Compilers bridge ML models and the hardware they run on.
- During lowering, operations are converted into specialized kernels where possible for faster execution.

---

## PyTorch Inference Optimization Case Study

- Figure 9-14 shows throughput gains the PyTorch team gave Llama-7B through optimization steps.
- Steps: call torch.compile for efficient kernels, quantize weights to INT8, then INT4, add speculative decoding.
- The experiment ran on an A100 GPU with 80 GB of memory.
- It was unclear how these optimization steps impact the model's output quality.

---

## Batching Strategies
- Batching groups simultaneous requests to cut cost, like putting drivers on a bus.
- Static batching waits until a fixed batch is full, delaying the first request.
- Dynamic batching sets a max time window, keeping latency controlled but batches may be underfull.
- Continuous batching returns completed responses immediately and fills freed slots with new requests.

---

## Continuous Batching and Decoupling
- Naive batching holds short responses until the longest request in the batch finishes.
- Continuous (in-flight) batching, from Orca, returns each response as soon as it completes.
- Prefill is compute-bound and decode is memory bandwidth-bound, so sharing a machine causes contention.
- Disaggregating prefill and decode onto different instances improves throughput while meeting latency requirements.

---

## Prompt Caching
- Prompt caches store overlapping prompt segments, such as system prompts, for reuse across queries.
- Useful for long documents and multi-turn conversations where earlier messages can be reused.
- Anthropic reports up to 90% cost savings and up to 75% latency reduction.
- Cache storage consumes memory, and self-implementing caching requires significant engineering effort.

---

## Parallelism
- Replica parallelism creates multiple model copies to handle more requests, using more chips.
- Tensor parallelism splits operator tensors across devices, enabling large models and lower latency.
- Pipeline parallelism divides computation into stages on different devices, but adds communication latency.
- Pipeline parallelism is typically avoided for strict latency needs but common in training for throughput.

---

## Inference Cost and Latency Metrics
- Usability depends on inference cost and latency; cheaper inference makes AI decisions more affordable.
- Latency splits into time to first token (TTFT, prefilling) and time per output token (TPOT, decoding).
- Throughput metrics relate directly to cost; latency and throughput trade off against each other.
- Efficiency depends on hardware, so optimization differs across accelerators.

---

## Model-Level vs Service-Level Optimization
- Model-level optimization changes the model itself, which can change model behaviors.
- Model-agnostic techniques include quantization and distillation; architectures need their own optimization.
- Transformer bottlenecks sit in attention, addressed via KV cache management and attention kernels.
- Service-level techniques keep the model intact: batching, parallelism, prefilling/decoding decoupling, prompt caching.

---

## Choosing Techniques by Workload
- KV caching matters more for long contexts; prompt caching suits long overlapping prompts and multi-turn conversations.
- If low latency outranks cost, scale up replica parallelism to allocate more resources per request.
- Most impactful across use cases: quantization, tensor parallelism, replica parallelism, attention mechanism optimization.
- Context parallelism splits input sequences across devices; sequence parallelism splits operators across machines.

## Practice Questions

### Question 1: According to the text, at what levels can inference optimization be...

According to the text, at what levels can inference optimization be done?

- [ ] A) Data, training, and deployment levels
- [ ] B) Model, hardware, and service levels
- [ ] C) Prompt, fine-tuning, and evaluation levels
- [ ] D) Storage, network, and security levels

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** The text states that inference optimization can be done at the model, hardware, and service levels.

### Question 2: Which of the following is given as a model-level inference optimiza...

Which of the following is given as a model-level inference optimization technique?

- [ ] A) Designing more powerful hardware
- [ ] B) Reducing a trained model’s size or developing more efficient architectures
- [ ] C) Allocating resources based on traffic patterns
- [ ] D) Collaborating with data center operators

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** The text says model-level optimization can reduce a trained model’s size or develop more efficient architectures, such as one without attention-mechanism bottlenecks.

### Question 3: What does the text say about trade-offs in inference optimization?

What does the text say about trade-offs in inference optimization?

- [ ] A) Optimization never requires trade-offs.
- [ ] B) Reducing a model’s precision makes it smaller and faster, but optimization often requires trade-offs such as faster hardware at higher cost.
- [ ] C) The best hardware always lowers both latency and cost.
- [ ] D) Service-level optimization is unrelated to latency and cost.

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** The text notes that reducing precision can make a model smaller and faster, but often optimization requires trade-offs, for example, the best hardware may run faster at a higher cost.

### Question 4: According to the text, what are the two distinct phases in an AI mo...

According to the text, what are the two distinct phases in an AI model’s lifecycle?

- [ ] A) Training and inference
- [ ] B) Preprocessing and routing
- [ ] C) Hosting and allocation
- [ ] D) Building and finetuning

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** A

    **Explanation:** The text states that training refers to building a model and inference refers to using a model to compute an output for a given input.

### Question 5: In production, what is the component that runs model inference called?

In production, what is the component that runs model inference called?

- [ ] A) An inference service
- [ ] B) An inference server
- [ ] C) A training server
- [ ] D) A preprocessing server

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** The text says that in production, the component that runs model inference is called an inference server.

### Question 6: Besides the inference server, what is the broader inference service...

Besides the inference server, what is the broader inference service responsible for?

- [ ] A) Training and finetuning models
- [ ] B) Building models and allocating hardware
- [ ] C) Receiving, routing, and possibly preprocessing requests
- [ ] D) Computing outputs and returning responses only

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** C

    **Explanation:** The text states that an inference service is also responsible for receiving, routing, and possibly preprocessing requests before they reach the inference server.

### Question 7: According to the source, which step of transformer-based language m...

According to the source, which step of transformer-based language model inference is compute-bound?

- [ ] A) Prefill
- [ ] B) Decode
- [ ] C) Both prefill and decode
- [ ] D) Neither prefill nor decode

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** A

    **Explanation:** The source says prefilling processes input tokens in parallel and is compute-bound, while decoding is memory bandwidth-bound.

### Question 8: What is the main difference between online APIs and batch APIs as d...

What is the main difference between online APIs and batch APIs as described in the source?

- [ ] A) Online APIs optimize for latency, while batch APIs optimize for cost.
- [ ] B) Online APIs optimize for cost, while batch APIs optimize for latency.
- [ ] C) Online APIs cannot batch requests, while batch APIs always return streaming responses.
- [ ] D) Online APIs are only for synthetic data generation, while batch APIs are only for chatbots.

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** A

    **Explanation:** The source states that online APIs optimize for latency and batch APIs optimize for cost, with batch processing allowing higher latency and more efficient processing.

### Question 9: In the source, what is the formula for total latency in autoregress...

In the source, what is the formula for total latency in autoregressive generation?

- [ ] A) TTFT + TPOT × (number of output tokens)
- [ ] B) TTFT × TPOT + (number of input tokens)
- [ ] C) TPOT + TTFT × (number of input tokens)
- [ ] D) TTFT ÷ TPOT × (number of output tokens)

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** A

    **Explanation:** The text states that total latency equals TTFT + TPOT × (number of output tokens).

### Question 10: Why does the source recommend looking at latency percentiles such a...

Why does the source recommend looking at latency percentiles such as p90, p95, and p99 rather than only the average?

- [ ] A) Averages can be skewed by outliers, while percentiles describe a percentage of requests and help reveal outliers.
- [ ] B) Percentiles measure throughput across all users.
- [ ] C) Percentiles eliminate the need to measure TTFT.
- [ ] D) Percentiles are only useful for precomputed batch inference.

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** A

    **Explanation:** The text says the average can be misleading because outliers skew it, and percentiles help discover outliers.

### Question 11: What does goodput measure for LLM applications?

What does goodput measure for LLM applications?

- [ ] A) The number of requests per second that satisfy the SLO
- [ ] B) The number of output tokens per second across all users
- [ ] C) The percentage of time the GPU is actively processing tasks
- [ ] D) The ratio of observed throughput to theoretical peak FLOP/s

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** A

    **Explanation:** Goodput is adapted from networking and measures the number of requests per second that satisfy the SLO.

### Question 12: Which pair correctly defines MFU and MBU?

Which pair correctly defines MFU and MBU?

- [ ] A) MFU: observed throughput relative to theoretical maximum at peak FLOP/s; MBU: percentage of achievable memory bandwidth used
- [ ] B) MFU: percentage of time GPU is active; MBU: number of requests per second satisfying SLO
- [ ] C) MFU: number of output tokens per second; MBU: time to first token
- [ ] D) MFU: percentage of achievable memory bandwidth used; MBU: observed throughput relative to peak FLOP/s

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** A

    **Explanation:** The text defines MFU as Model FLOP/s Utilization and MBU as Model Bandwidth Utilization.

### Question 13: According to the text, what is the primary goal when optimizing inf...

According to the text, what is the primary goal when optimizing inference systems, rather than simply maximizing chip utilization?

- [ ] A) Achieving the highest possible utilization rate on the hardware
- [ ] B) Getting jobs done faster and cheaper
- [ ] C) Minimizing power consumption at all costs
- [ ] D) Maximizing FLOP/s regardless of latency

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** The text states that higher utilization means nothing if cost and latency both increase, and the real goal is to get jobs done faster and cheaper.

### Question 14: What is the main architectural difference between CPUs and GPUs as...

What is the main architectural difference between CPUs and GPUs as described in the text?

- [ ] A) CPUs have thousands of cores for parallel tasks, while GPUs have few powerful cores for sequential tasks.
- [ ] B) CPUs are designed for general-purpose usage with few powerful cores, while GPUs are designed for parallel processing with thousands of smaller cores.
- [ ] C) CPUs use HBM memory, while GPUs use DDR SDRAM.
- [ ] D) CPUs are optimized for matrix multiplication, while GPUs are optimized for I/O operations.

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** The text explains that CPUs have a few powerful cores for general-purpose and sequential tasks, whereas GPUs have thousands of smaller cores optimized for parallel processing like matrix multiplication.

### Question 15: According to the text, what are inference-specific chips typically...

According to the text, what are inference-specific chips typically optimized for?

- [ ] A) Large memory capacity and high precision
- [ ] B) Lower precision and faster memory access
- [ ] C) High power consumption and maximum FLOP/s
- [ ] D) General-purpose sequential processing

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** The text states that chips designed for inference are often optimized for lower precision and faster memory access, rather than large memory capacity.

### Question 16: According to the source, inference optimization can be done at whic...

According to the source, inference optimization can be done at which levels?

- [ ] A) Model, hardware, or service level
- [ ] B) Training, validation, or test level
- [ ] C) Prompt, context, or output level
- [ ] D) Data, label, or metric level

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** A

    **Explanation:** The source states that inference optimization can be done at the model, hardware, or service level.

### Question 17: In the archery analogy, what does model-level optimization correspo...

In the archery analogy, what does model-level optimization correspond to?

- [ ] A) Training a stronger and better archer
- [ ] B) Crafting better arrows
- [ ] C) Refining the entire shooting process, including the bow and aiming conditions
- [ ] D) Changing the target after shooting

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** The source says model-level optimization is like crafting better arrows.

### Question 18: What does the source say about optimizing a model for speed and cost?

What does the source say about optimizing a model for speed and cost?

- [ ] A) It always improves model quality
- [ ] B) It never affects model behavior
- [ ] C) Ideally it shouldn’t change quality, but many techniques might cause model degradation
- [ ] D) It only applies to hardware-level optimization

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** C

    **Explanation:** The source states that ideally optimizing for speed and cost shouldn’t change quality, but many techniques might cause model degradation.

### Question 19: What does Figure 9-8 illustrate about inference service providers?

What does Figure 9-8 illustrate about inference service providers?

- [ ] A) Different providers cannot serve the same Llama models
- [ ] B) Providers may use optimization techniques that alter a model’s behavior, causing slight model quality variations
- [ ] C) Model quality is identical across all providers
- [ ] D) Hardware-level optimization is the only cause of quality differences

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** The source says an inference service provider might use optimization techniques that can alter a model’s behavior, causing different providers to have slight model quality variations.

### Question 20: According to the text, at which levels does the book discuss optimi...

According to the text, at which levels does the book discuss optimization techniques?

- [ ] A) Hardware and software levels
- [ ] B) Model and service levels
- [ ] C) Data and network levels
- [ ] D) Training and deployment levels

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** The text states that since hardware design is outside the scope of the book, techniques are discussed at the model and service levels.

### Question 21: What does the text say about optimization in production?

What does the text say about optimization in production?

- [ ] A) It relies solely on model-level techniques
- [ ] B) It relies solely on service-level techniques
- [ ] C) It typically involves techniques at more than one level
- [ ] D) It requires custom hardware design

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** C

    **Explanation:** The text notes that while techniques are discussed separately, production optimization typically involves techniques at more than one level.

### Question 22: Why does the text exclude hardware design from discussion?

Why does the text exclude hardware design from discussion?

- [ ] A) It is outside the scope of the book
- [ ] B) It is irrelevant to inference
- [ ] C) It is covered in another chapter
- [ ] D) It is too simple to warrant discussion

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** A

    **Explanation:** The text explicitly says hardware design is outside the scope of this book.

### Question 23: What is the aim of model-level optimization?

What is the aim of model-level optimization?

- [ ] A) To make the model more efficient, often by modifying the model itself
- [ ] B) To make the model larger without changing efficiency
- [ ] C) To avoid modifying the model under all circumstances
- [ ] D) To eliminate autoregressive language model components

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** A

    **Explanation:** The source states that model-level optimization aims to make the model more efficient, often by modifying the model itself.

### Question 24: What does the source say can happen when the model itself is modified?

What does the source say can happen when the model itself is modified?

- [ ] A) Its behavior can be altered
- [ ] B) Its architecture must become non-transformer
- [ ] C) Its inference cost always increases
- [ ] D) Its autoregressive component is removed

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** A

    **Explanation:** The source notes that modifying the model itself can alter its behavior.

### Question 25: According to the source, which three characteristics make inference...

According to the source, which three characteristics make inference resource-intensive for many foundation models?

- [ ] A) Model size, autoregressive decoding, and the attention mechanism
- [ ] B) Model size, batch size, and tokenization
- [ ] C) Autoregressive decoding, quantization, and pruning
- [ ] D) The attention mechanism, caching, and distillation

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** A

    **Explanation:** The source lists model size, autoregressive decoding, and the attention mechanism as the three characteristics that make inference resource-intensive.

### Question 26: What architecture does the source say many foundation models follow...

What architecture does the source say many foundation models follow as of this writing?

- [ ] A) The transformer architecture with an autoregressive language model component
- [ ] B) A non-autoregressive convolutional architecture
- [ ] C) A retrieval-only architecture without a language model component
- [ ] D) A rule-based architecture without attention

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** A

    **Explanation:** The source says many foundation models follow the transformer architecture and include an autoregressive language model component.

### Question 27: According to the text, which of the following is one meaning of pru...

According to the text, which of the following is one meaning of pruning in neural networks?

- [ ] A) Removing entire nodes of a neural network, changing its architecture and reducing its number of parameters
- [ ] B) Training a small model to mimic the behavior of a large model
- [ ] C) Reducing the precision of a model to reduce its memory footprint
- [ ] D) Increasing the total number of parameters while keeping all parameters non-zero

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** A

    **Explanation:** The text states that one meaning of pruning is to remove entire nodes of a neural network, which changes its architecture and reduces its number of parameters.

### Question 28: What does the text say about the practical use of pruning as of the...

What does the text say about the practical use of pruning as of the time of writing?

- [ ] A) It is the most common optimization approach and always provides the largest performance boost
- [ ] B) It is less common, harder to do because it requires understanding the original model’s architecture, and its performance boost is often much less than other approaches
- [ ] C) It is easy to use, works out of the box for many models, and is extremely effective
- [ ] D) It never results in sparse models and works on all hardware architectures

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** The text says pruning is less common in practice, harder to do because it requires understanding the original model’s architecture, and often brings a much smaller performance boost than other approaches.

### Question 29: Why does the text describe weight-only quantization as by far the m...

Why does the text describe weight-only quantization as by far the most popular approach?

- [ ] A) Because it requires an understanding of the original model’s architecture and always produces sparse models
- [ ] B) Because it can reduce precision below 1 bit per value
- [ ] C) Because it is easy to use, works out of the box for many models, and is extremely effective
- [ ] D) Because it trains a small model to mimic the behavior of a large model

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** C

    **Explanation:** The text states that weight-only quantization is by far the most popular approach since it is easy to use, works out of the box for many models, and is extremely effective.

### Question 30: According to the source, if it takes 100 ms to generate one token,...

According to the source, if it takes 100 ms to generate one token, how long will a 100-token response take?

- [ ] A) 1 second
- [ ] B) 10 seconds
- [ ] C) 100 seconds
- [ ] D) 1,000 seconds

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** The source states that at 100 ms per token, a 100-token response will take 10 seconds.

### Question 31: Across model API providers, an output token costs approximately how...

Across model API providers, an output token costs approximately how many times an input token?

- [ ] A) One to two times
- [ ] B) Two to four times
- [ ] C) Four to six times
- [ ] D) Ten times

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** The source says an output token costs approximately two to four times an input token across model API providers.

### Question 32: In an experiment by Anyscale, a single output token can have the sa...

In an experiment by Anyscale, a single output token can have the same impact on latency as how many input tokens?

- [ ] A) 10 input tokens
- [ ] B) 50 input tokens
- [ ] C) 100 input tokens
- [ ] D) 1,000 input tokens

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** C

    **Explanation:** The source reports that Anyscale found a single output token can have the same impact on latency as 100 input tokens.

### Question 33: What does the source say about techniques being developed to overco...

What does the source say about techniques being developed to overcome the autoregressive decoding bottleneck?

- [ ] A) They are fully settled and no longer changing
- [ ] B) They are still evolving
- [ ] C) They apply only to input tokens
- [ ] D) They eliminate the need for tokens

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** The source states that the techniques covered are still evolving and are meant to illustrate what a solution might look like.

### Question 34: In speculative decoding, what is the role of the draft or proposal...

In speculative decoding, what is the role of the draft or proposal model?

- [ ] A) It generates a sequence of tokens that the target model then verifies.
- [ ] B) It verifies the target model’s generated tokens in parallel.
- [ ] C) It replaces the target model for the entire response.
- [ ] D) It trains the target model on easier-to-predict tokens.

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** A

    **Explanation:** The source says speculative decoding uses a faster but less powerful model to generate tokens, which are then verified by the target model.

### Question 35: If the target model accepts all K draft tokens, how many tokens doe...

If the target model accepts all K draft tokens, how many tokens does the speculative decoding loop produce?

- [ ] A) K tokens
- [ ] B) K + 1 tokens
- [ ] C) 1 token
- [ ] D) 2K tokens

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** The source states that if all draft tokens are accepted, the loop produces K + 1 tokens, with K generated by the draft model and one by the target model.

### Question 36: Why can the target model verify a sequence of tokens faster than it...

Why can the target model verify a sequence of tokens faster than it can generate the sequence?

- [ ] A) Verification is parallelizable, while generation is sequential.
- [ ] B) Verification uses a smaller vocabulary than generation.
- [ ] C) The draft model always predicts every token correctly.
- [ ] D) The target model skips computation during verification.

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** A

    **Explanation:** The source explains that verification is parallelizable while generation is sequential, so speculative decoding turns decoding’s computation profile into that of prefilling.

### Question 37: What trade-off does using a larger value of K create in speculative...

What trade-off does using a larger value of K create in speculative decoding?

- [ ] A) It means fewer verifying calls for the target model but a lower acceptance rate of draft tokens.
- [ ] B) It means more verifying calls for the target model and a higher acceptance rate.
- [ ] C) It has no effect on verifying calls or acceptance rate.
- [ ] D) It reduces the target model’s response quality.

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** A

    **Explanation:** The source says larger K values mean fewer verifying calls for the target model but a low acceptance rate of the draft tokens.

### Question 38: What is the core idea behind inference with reference?

What is the core idea behind inference with reference?

- [ ] A) Using a smaller model to generate draft tokens before verification
- [ ] B) Copying relevant tokens from the input instead of making the model generate repeated tokens
- [ ] C) Compressing the model weights before inference
- [ ] D) Caching all possible outputs for future requests

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** The source states that inference with reference copies repeated tokens from the input to speed up generation instead of having the model generate them.

### Question 39: How does inference with reference differ from speculative decoding?

How does inference with reference differ from speculative decoding?

- [ ] A) It requires an extra model to generate draft tokens
- [ ] B) It selects draft tokens from the input rather than using a model to generate them
- [ ] C) It cannot be used with retrieval systems or coding
- [ ] D) It always produces lower-quality outputs

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** The source says inference with reference is similar to speculative decoding, but it selects draft tokens from the input instead of using a model to generate draft tokens.

### Question 40: In which scenario is inference with reference most useful?

In which scenario is inference with reference most useful?

- [ ] A) When there is little overlap between the context and the output
- [ ] B) When the model must generate entirely novel text with no input reference
- [ ] C) When there is significant overlap between contexts and outputs, such as retrieval systems, coding, or multi-turn conversations
- [ ] D) When no input context is available

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** C

    **Explanation:** The source states that inference with reference is useful only when there is significant overlap between contexts and outputs, such as in retrieval systems, coding, or multi-turn conversations.

### Question 41: According to Yang et al. (2023), what generation speedup does infer...

According to Yang et al. (2023), what generation speedup does inference with reference help achieve in suitable use cases?

- [ ] A) Two times
- [ ] B) Five times
- [ ] C) Ten times
- [ ] D) No speedup

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** A

    **Explanation:** The source says that in “Inference with Reference: Lossless Acceleration of Large Language Models” (Yang et al., 2023), the technique helps achieve two times generation speedup in such use cases.

### Question 42: What is the primary aim of parallel decoding techniques described i...

What is the primary aim of parallel decoding techniques described in the text?

- [ ] A) To generate multiple future tokens simultaneously by breaking the sequential dependency
- [ ] B) To generate draft tokens and then verify them with the original model
- [ ] C) To reduce memory use by quantizing model weights
- [ ] D) To train multiple decoding heads while unfreezing the original model

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** A

    **Explanation:** The text says parallel decoding techniques attempt to generate future tokens simultaneously instead of making autoregressive generation faster with draft tokens.

### Question 43: In Medusa, what is each decoding head trained to do?

In Medusa, what is each decoding head trained to do?

- [ ] A) Predict only the immediate next token x_t+1
- [ ] B) Predict a future token at a specific position, with the kth head predicting x_t+k+1
- [ ] C) Verify generated tokens using the Jacobi method
- [ ] D) Replace the original model entirely during inference

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** The text states that each Medusa head is a small neural network layer trained to predict a future token at a specific position, and the kth head predicts x_t+k+1.

### Question 44: How does Lookahead decoding verify and integrate parallel tokens?

How does Lookahead decoding verify and integrate parallel tokens?

- [ ] A) By using a tree-based attention mechanism to select the most promising combination
- [ ] B) By using the Jacobi method and refining failed tokens until all pass verification
- [ ] C) By scoring tokens with a separate draft model
- [ ] D) By freezing the original model and training new heads

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** The text says Lookahead decoding uses the Jacobi method to verify generated tokens and regenerates or adjusts only failed tokens until they pass verification.

### Question 45: According to the text, what did NVIDIA claim about Medusa on HGX H2...

According to the text, what did NVIDIA claim about Medusa on HGX H200 GPUs?

- [ ] A) It helped boost Llama 3.1 token generation by up to 1.9×
- [ ] B) It provided a 21× speedup for Llama 3.1 token generation
- [ ] C) It reduced Llama 3.1 memory use by up to 1.9×
- [ ] D) It eliminated the need for verification in parallel decoding

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** A

    **Explanation:** The text states NVIDIA claimed Medusa helped boost Llama 3.1 token generation by up to 1.9× on their HGX H200 GPUs.

### Question 46: According to the source text, what does generating the next token r...

According to the source text, what does generating the next token require?

- [ ] A) Only the most recent token’s key vector
- [ ] B) The key and value vectors for all previous tokens
- [ ] C) Only the value vectors for the first token
- [ ] D) The attention weights for future tokens

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** The text states that generating the next token requires the key and value vectors for all previous tokens.

### Question 47: What is the KV cache used for in attention mechanism optimization?

What is the KV cache used for in attention mechanism optimization?

- [ ] A) Storing key and value vectors so they can be reused
- [ ] B) Storing only the generated output tokens
- [ ] C) Recomputing key and value vectors at each decoding step
- [ ] D) Storing attention weights for future tokens

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** A

    **Explanation:** The source defines the KV cache as the cache that stores key and value vectors for reuse.

### Question 48: When generating token x_t+1, which key and value vectors need to be...

When generating token x_t+1, which key and value vectors need to be computed instead of recomputing all previous ones?

- [ ] A) The vectors for tokens x_1 through x_t–1
- [ ] B) The vectors for all future tokens
- [ ] C) Only the vectors for the most recent token, x_t
- [ ] D) No key or value vectors need to be computed

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** C

    **Explanation:** The text says you reuse previous vectors from the KV cache and compute key and value vectors only for the most recent token, x_t.

### Question 49: According to the source text, when is a KV cache used?

According to the source text, when is a KV cache used?

- [ ] A) During both training and inference
- [ ] B) Only during training
- [ ] C) Only during inference
- [ ] D) Only during model evaluation

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** C

    **Explanation:** The text states that a KV cache is used only during inference, not training.

### Question 50: How does the KV cache size grow with sequence length, according to...

How does the KV cache size grow with sequence length, according to the text?

- [ ] A) Exponentially
- [ ] B) Linearly
- [ ] C) Quadratically
- [ ] D) Logarithmically

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** The text says the KV cache size grows linearly with sequence length, while attention computations grow exponentially.

### Question 51: What is the formula given in the text for calculating the memory ne...

What is the formula given in the text for calculating the memory needed for the KV cache without any optimization?

- [ ] A) 2 × B × S × L × H × M
- [ ] B) B × S × L × H × M
- [ ] C) 2 × B × S × L × H
- [ ] D) B × S × L × H × M × 2

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** A

    **Explanation:** The text provides the formula: 2 × B × S × L × H × M, where B is batch size, S is sequence length, L is number of transformer layers, H is model dimension, and M is memory needed for the cache’s numerical representation.

### Question 52: According to the source, what does local windowed attention do when...

According to the source, what does local windowed attention do when generating a new token?

- [ ] A) It attends to all previous tokens but compresses their representations.
- [ ] B) It attends only to a fixed-size window of nearby tokens.
- [ ] C) It shares key-value vectors across adjacent layers.
- [ ] D) It groups query heads and shares key-value pairs within each group.

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** The source states that local windowed attention attends only to a fixed size window of nearby tokens instead of all previous tokens.

### Question 53: How does cross-layer attention reduce the memory footprint of the K...

How does cross-layer attention reduce the memory footprint of the KV cache?

- [ ] A) By sharing key and value vectors across adjacent layers.
- [ ] B) By sharing key-value vectors across query heads.
- [ ] C) By attending only to a fixed-size window of nearby tokens.
- [ ] D) By interleaving local attention with global attention.

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** A

    **Explanation:** The source says cross-layer attention shares key and value vectors across adjacent layers, reducing the KV cache.

### Question 54: What does grouped-query attention do, according to the source?

What does grouped-query attention do, according to the source?

- [ ] A) It shares one set of key-value pairs for all query heads.
- [ ] B) It shares key and value vectors across adjacent layers.
- [ ] C) It puts query heads into smaller groups and shares key-value pairs only among query heads in the same group.
- [ ] D) It attends only to a fixed-size window of nearby tokens.

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** C

    **Explanation:** The source describes grouped-query attention as a generalization of multi-query attention that groups query heads and shares key-value pairs within each group.

### Question 55: According to Character.AI’s example in the source, what is the prim...

According to Character.AI’s example in the source, what is the primary bottleneck for inference throughput given typically long sequences?

- [ ] A) The number of query heads.
- [ ] B) The KV cache size.
- [ ] C) The size of the local attention window.
- [ ] D) The number of adjacent layers sharing key-value vectors.

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** The source states that given typically long sequences, the primary bottleneck for inference throughput is the KV cache size.

### Question 56: What does PagedAttention optimize in LLM serving?

What does PagedAttention optimize in LLM serving?

- [ ] A) It divides the KV cache into non-contiguous blocks to reduce fragmentation and enable flexible memory sharing.
- [ ] B) It eliminates the KV cache entirely for long-context applications.
- [ ] C) It increases the KV cache size by storing all attention weights contiguously.
- [ ] D) It converts the KV cache into model parameters during inference.

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** A

    **Explanation:** The source states that PagedAttention optimizes memory management by dividing the KV cache into non-contiguous blocks, reducing fragmentation, and enabling flexible memory sharing.

### Question 57: Which inference framework gained popularity for introducing PagedAt...

Which inference framework gained popularity for introducing PagedAttention?

- [ ] A) TensorRT-LLM
- [ ] B) vLLM
- [ ] C) Hugging Face TGI
- [ ] D) Ollama

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** The source says vLLM gained popularity for introducing PagedAttention to optimize KV cache memory management.

### Question 58: Which of the following is listed in the source as a KV cache optimi...

Which of the following is listed in the source as a KV cache optimization technique besides PagedAttention?

- [ ] A) KV cache quantization
- [ ] B) Continuous batching
- [ ] C) Speculative decoding
- [ ] D) Model pruning

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** A

    **Explanation:** The source lists KV cache quantization, adaptive KV cache compression, and selective KV cache as other techniques for reducing and managing the KV cache.

### Question 59: What does the approach of writing kernels for attention computation...

What does the approach of writing kernels for attention computation focus on?

- [ ] A) Changing the attention mechanism design
- [ ] B) Optimizing storage of attention scores
- [ ] C) Making the computation of attention scores more efficient
- [ ] D) Reducing the number of transformer layers

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** C

    **Explanation:** The source says this approach looks into how attention scores are computed and finds ways to make that computation more efficient.

### Question 60: According to the source, when is writing kernels for attention comp...

According to the source, when is writing kernels for attention computation most effective?

- [ ] A) When it ignores the hardware executing the computation
- [ ] B) When it takes into account the hardware executing the computation
- [ ] C) When it changes the mechanism design
- [ ] D) When it optimizes storage instead of computation

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** The text states this approach is most effective when it takes into account the hardware executing the computation.

### Question 61: What is FlashAttention described as in the source?

What is FlashAttention described as in the source?

- [ ] A) A storage optimization technique for attention scores
- [ ] B) A mechanism design change for transformer models
- [ ] C) A well-known kernel optimized for attention computation that fuses common operations
- [ ] D) A method for reducing the number of operations in a transformer by changing its design

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** C

    **Explanation:** The source identifies FlashAttention as a well-known kernel optimized for attention computation that fused together many commonly used operations to run faster.

### Question 62: What are kernels in the context of AI inference optimization?

What are kernels in the context of AI inference optimization?

- [ ] A) Specialized pieces of code optimized for specific hardware accelerators such as GPUs or TPUs
- [ ] B) High-level Python libraries used to train models
- [ ] C) General-purpose operating system routines for memory management
- [ ] D) Data storage formats for model weights

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** A

    **Explanation:** The text defines kernels as specialized pieces of code optimized for specific hardware accelerators, such as GPUs or TPUs.

### Question 63: Which lower-level programming language is described as developed by...

Which lower-level programming language is described as developed by OpenAI for writing custom kernels?

- [ ] A) CUDA
- [ ] B) Triton
- [ ] C) ROCm
- [ ] D) Python

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** The text states that Triton is a language developed by OpenAI for writing custom kernels.

### Question 64: According to the text, why did writing kernels used to be a “dark a...

According to the text, why did writing kernels used to be a “dark art practiced by a few”?

- [ ] A) Because kernels required deep hardware knowledge and lower-level languages that most AI engineers were not familiar with
- [ ] B) Because kernels could only be written by AI framework users
- [ ] C) Because kernels were not useful for AI workloads
- [ ] D) Because kernels were written only in Python

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** A

    **Explanation:** The text attributes the entry barrier to kernels being written in lower-level languages and requiring deep understanding of hardware architecture, making them harder to learn than languages like Python.

### Question 65: What does vectorization do instead of processing one data element a...

What does vectorization do instead of processing one data element at a time?

- [ ] A) It processes elements in random memory order
- [ ] B) It simultaneously executes multiple data elements that are contiguous in memory
- [ ] C) It splits the loop across multiple machines
- [ ] D) It compiles the loop into a recursive function

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** The source states that vectorization simultaneously executes multiple data elements that are contiguous in memory rather than processing one element at a time.

### Question 66: According to the source, how does vectorization reduce latency?

According to the source, how does vectorization reduce latency?

- [ ] A) By minimizing data I/O operations
- [ ] B) By increasing the number of loop iterations
- [ ] C) By caching all data on disk
- [ ] D) By parallelizing across separate processes

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** A

    **Explanation:** The source says vectorization reduces latency by minimizing data I/O operations.

### Question 67: To which of the following does the source say vectorization can be...

To which of the following does the source say vectorization can be applied?

- [ ] A) Only single, non-nested loops
- [ ] B) Only recursive functions
- [ ] C) A loop or a nested loop
- [ ] D) Only database queries

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** C

    **Explanation:** The source introduces vectorization as applying to “a loop or a nested loop.”

### Question 68: What is the main purpose of parallelization as described in the sou...

What is the main purpose of parallelization as described in the source text?

- [ ] A) To divide an input array into independent chunks that can be processed simultaneously on different cores or threads
- [ ] B) To reorder loop data accesses for the hardware’s memory layout and cache
- [ ] C) To reduce the number of cores needed for computation
- [ ] D) To convert CPU tiling patterns into GPU tiling patterns

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** A

    **Explanation:** The source states that parallelization divides an input array or n-dimensional array into independent chunks processed simultaneously on different cores or threads.

### Question 69: What does loop tiling optimize?

What does loop tiling optimize?

- [ ] A) The number of threads used by an input array
- [ ] B) The data accessing order in a loop for the hardware’s memory layout and cache
- [ ] C) The conversion of independent chunks into n-dimensional arrays
- [ ] D) The simultaneous processing of different cores

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** The source defines loop tiling as optimizing the data accessing order in a loop for the hardware’s memory layout and cache.

### Question 70: Which statement about loop tiling is supported by the source text?

Which statement about loop tiling is supported by the source text?

- [ ] A) It is hardware-independent and works equally well on CPUs and GPUs.
- [ ] B) It is only used for parallelizing independent chunks.
- [ ] C) It is hardware-dependent, and an efficient CPU tiling pattern may not work well on GPUs.
- [ ] D) It eliminates the need for cache and memory layout considerations.

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** C

    **Explanation:** The source says loop tiling is hardware-dependent and that an efficient CPU tiling pattern may not work well on GPUs.

### Question 71: What is the main purpose of operator fusion?

What is the main purpose of operator fusion?

- [ ] A) To combine multiple operators into a single pass and avoid redundant memory access
- [ ] B) To convert model weights from FP32 to INT8
- [ ] C) To split a model across multiple hardware architectures
- [ ] D) To replace all kernels with speculative decoding

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** A

    **Explanation:** The source states that operator fusion combines multiple operators into a single pass to avoid redundant memory access, such as fusing two loops over the same array.

### Question 72: Why does operator fusion require more attention from optimization e...

Why does operator fusion require more attention from optimization engineers than vectorization, parallelization, and loop tiling?

- [ ] A) It can only be applied to Llama-7B models
- [ ] B) It requires a deeper understanding of a model’s specific operators and architecture
- [ ] C) It eliminates the need for compilers
- [ ] D) It works only on CPUs

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** The source says vectorization, parallelization, and loop tiling apply broadly, while operator fusion requires deeper understanding of a model’s specific operators and architecture.

### Question 73: What does the source say about kernels and hardware architectures?

What does the source say about kernels and hardware architectures?

- [ ] A) Kernels are independent of hardware, so new kernels are never needed
- [ ] B) Kernels are optimized for a hardware architecture, so new kernels need to be developed when a new hardware architecture is introduced
- [ ] C) FlashAttention was originally developed primarily for H100 GPUs
- [ ] D) Compilers eliminate the need to develop kernels for new hardware

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** The source states kernels are optimized for a hardware architecture and new kernels are needed for new hardware, citing FlashAttention for A100 and later FlashAttention-3 for H100.

### Question 74: In the PyTorch Llama-7B case study, which optimization step came im...

In the PyTorch Llama-7B case study, which optimization step came immediately after quantizing the model weights to INT8?

- [ ] A) Adding speculative decoding
- [ ] B) Calling torch.compile to compile the model into more efficient kernels
- [ ] C) Further quantizing the model weights to INT4
- [ ] D) Running the experiment on an H100 GPU

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** C

    **Explanation:** The listed steps are torch.compile, quantize weights to INT8, further quantize weights to INT4, then add speculative decoding.

### Question 75: Which batching technique returns each response as soon as it is com...

Which batching technique returns each response as soon as it is completed and can add a new request in its place?

- [ ] A) Static batching
- [ ] B) Dynamic batching
- [ ] C) Continuous batching
- [ ] D) Replica parallelism

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** C

    **Explanation:** Continuous batching allows completed responses to be returned immediately to users, and new requests can be processed in their place.

### Question 76: Why can using the same machine for both prefill and decode be ineff...

Why can using the same machine for both prefill and decode be inefficient?

- [ ] A) Prefill is memory bandwidth-bound and decode is compute-bound, causing cache misses.
- [ ] B) Prefill is compute-bound and decode is memory bandwidth-bound, so they compete for resources and can slow TTFT and TPOT.
- [ ] C) Prefill and decode cannot be run on GPUs.
- [ ] D) Decoupling always increases communication overhead beyond any benefit.

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** The source says prefill is compute-bound and decode is memory bandwidth-bound, and using the same machine can cause them to inefficiently compete for resources and significantly slow down both TTFT and TPOT.

### Question 77: What does a prompt cache store for reuse?

What does a prompt cache store for reuse?

- [ ] A) Model weights
- [ ] B) Overlapping text segments in prompts
- [ ] C) Only GPU memory addresses
- [ ] D) Only the final generated response

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** A prompt cache stores overlapping text segments in different prompts so they only need to be processed once.

### Question 78: Which parallelism strategy is typically avoided for applications wi...

Which parallelism strategy is typically avoided for applications with strict latency requirements because it increases total latency due to communication between stages?

- [ ] A) Replica parallelism
- [ ] B) Tensor parallelism
- [ ] C) Pipeline parallelism
- [ ] D) Data parallelism

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** C

    **Explanation:** Pipeline parallelism increases the total latency for each request due to extra communication between pipeline stages, so it is typically avoided for strict latency requirements.

### Question 79: According to the source, what does context parallelism involve?

According to the source, what does context parallelism involve?

- [ ] A) Splitting the input sequence itself across different devices to be processed separately
- [ ] B) Splitting operators needed for the entire input across machines
- [ ] C) Splitting the model’s parameters across different replicas
- [ ] D) Caching whole prompts for queries in the same chat session

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** A

    **Explanation:** The source states that in context parallelism, the input sequence is split across different devices, such as the first half on machine 1 and the second half on machine 2.

### Question 80: What does the chapter say about the relationship between latency an...

What does the chapter say about the relationship between latency and throughput?

- [ ] A) There is no meaningful trade-off between latency and throughput.
- [ ] B) Throughput metrics are unrelated to cost.
- [ ] C) You can potentially reduce cost if you are okay with increased latency, and reducing latency often involves increasing cost.
- [ ] D) Reducing latency always reduces cost.

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** C

    **Explanation:** The summary explicitly describes a trade-off: lower cost may come with increased latency, while reducing latency often increases cost.

### Question 81: Which statement best reflects the source’s distinction between mode...

Which statement best reflects the source’s distinction between model-level and inference service-level optimization?

- [ ] A) Model-level optimization typically keeps the model intact and only changes how it is served.
- [ ] B) Inference service-level optimization often requires changing the model itself and can change model behaviors.
- [ ] C) Model-level optimization often requires changing the model itself, which can lead to changes in model behaviors.
- [ ] D) Quantization is described as an inference service-level technique.

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** C

    **Explanation:** The source says model-level optimization often requires changing the model itself and can change model behaviors, while service-level optimization typically keeps the model intact.

### Question 82: Across various use cases, which techniques does the source identify...

Across various use cases, which techniques does the source identify as typically the most impactful?

- [ ] A) Quantization, tensor parallelism, replica parallelism, and attention mechanism optimization
- [ ] B) Prompt caching, context parallelism, sequence parallelism, and distillation
- [ ] C) Only prefilling/decoding decoupling and prompt caching
- [ ] D) Only KV cache management and writing attention kernels

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** A

    **Explanation:** The summary states that across use cases, the most impactful techniques are typically quantization, tensor parallelism, replica parallelism, and attention mechanism optimization.
