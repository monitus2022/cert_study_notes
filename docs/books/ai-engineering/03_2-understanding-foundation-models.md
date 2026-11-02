# 2. Understanding Foundation Models

---

## Why Understand Foundation Models

- Building applications requires foundation models; high-level understanding helps you choose and adapt them.
- Training a foundation model is complex and costly, and details are often protected by confidentiality agreements.
- This chapter does not teach how to build a ChatGPT competitor.
- It focuses on design decisions that consequentially impact downstream applications.

---

## Where Model Differences Come From

- Growing lack of transparency makes it hard to know all design decisions behind a model.
- Differences generally trace to training data, model architecture and size, and post-training.
- Training data reveals much about a model's capabilities and limitations, especially its distribution.
- The transformer architecture dominates, but the chapter asks what might replace it and how size is chosen.

---

## Pre-Training, Post-Training, and Sampling

- Training is often divided into pre-training and post-training.
- Pre-training makes a model capable, but not necessarily safe or easy to use.
- Post-training aims to align the model with human preferences, strongly affecting usability.
- Sampling—how a model picks an output from all options—is often overlooked and underrated.

---

## Training Data Determines Capability
- A model is only as good as the data it was trained on.
- No Vietnamese in training data means no English-to-Vietnamese translation.
- Image classifiers trained only on animals fail on photos of plants.
- Collecting sufficient training data is difficult and expensive; developers often use available data.

---

## Common Crawl and Quality Concerns
- Common Crawl is a nonprofit that sporadically crawls websites; it crawled 2–3 billion pages monthly in 2022–2023.
- Google provides a clean subset called Colossal Clean Crawled Corpus, or C4.
- Quality is questionable: clickbait, misinformation, propaganda, conspiracy theories, racism, and misogyny.
- A Washington Post study found low-trustworthiness outlets among the 1,000 most common websites.

---

## Curation and Data Quality
- Common Crawl variations are used in disclosed foundation models including GPT-3 and Gemini.
- OpenAI trained GPT-2 using only Reddit links with at least three upvotes.
- "Use what we have, not what we want" can yield models misaligned with your tasks.
- Gunasekar et al. (2023) trained a 1.3B model on 7B high-quality coding tokens, outperforming larger models.

---

## English Dominance in Training Data

- English accounts for 45.88% of Common Crawl, eight times more than Russian at 5.97%.
- Languages with limited training data availability are called *low-resource* languages.
- Many widely spoken languages are severely under-represented relative to their speaker populations.
- Ideally the ratio of world population share to Common Crawl share should be 1.

---

## Under-Representation Hurts Performance

- General-purpose models work much better for English than for other languages.
- On MMLU, GPT-4 performed much better in English than in under-represented languages like Telugu.
- Telugu, Marathi, and Punjabi score worst on MMLU and are among the most under-represented.
- Language structure and embodied culture can also make a language harder to learn.

---

## Translation, Misinformation, and Token Cost

- Translating queries to English requires a model that understands under-represented languages, and causes information loss.
- Vietnamese pronouns denoting speaker relationships collapse into *I* and *you* in English.
- ChatGPT produced false claims in simplified and traditional Chinese all seven times, but declined six of seven in English.
- Tokenization is less efficient: median token length is 7 in English, 32 in Hindi, 72 in Burmese.

---

## Domain-Specific Models: Why Specialization Matters

- General-purpose models (Gemini, GPTs, Llamas) perform well across many domains thanks to their training data.
- Figure 2-3 shows domain distribution in Common Crawl per the *Washington Post*'s 2023 analysis.
- Caveat: the analysis shows only included categories, not missing ones.
- Vision data domain distribution is rarely analyzed; images are harder to categorize than texts.

---

## Inferring Domains from Benchmarks

- Benchmark performance can reveal a model's domains when data analysis is lacking.
- Table 2-3 compares CLIP and Open CLIP on birds, flowers, cars, and more categories.
- The world is far bigger and more complex than these few benchmark categories.

---

## When General Models Fall Short

- General models likely fail on domain-specific tasks unseen during training, e.g., drug discovery and cancer screening.
- Drug discovery uses protein, DNA, and RNA data—specific formats, expensive, rarely public.
- Cancer screening uses X-ray and fMRI scans, hard to obtain due to privacy.
- Domain-specific examples: AlphaFold (~100,000 proteins), NVIDIA BioNeMo, Google Med-PaLM2.

---

## Modeling Decisions

- Before training, decide the model's architecture and number of parameters.
- These choices affect both model capabilities and usability in downstream applications.
- A 7B-parameter model is vastly easier to deploy than a 175B-parameter model.
- Optimizing a transformer for latency differs from optimizing other architectures.

---

## Model Architecture

- The transformer architecture (Vaswani et al., 2017) dominates language-based foundation models.
- It is based on the attention mechanism.
- It addresses many limitations of previous architectures, contributing to its popularity.
- The transformer has its own limitations; the section analyzes it and its alternatives.

---

## Modeling Decisions

- Before training, developers decide the model's architecture and parameter count.
- Architecture: what structure the model follows.
- Parameter count: how large the model is.
- Size and architecture affect both capabilities and deployment usability.

---

## Architecture Impacts Deployment

- A 7B-parameter model is vastly easier to deploy than a 175B-parameter model.
- Optimizing a transformer for latency differs greatly from optimizing other architectures.

---

## Transformer Dominance
- The transformer architecture (Vaswani et al., 2017) is the dominant architecture for language-based foundation models.
- It is based on the attention mechanism.
- It addresses many limitations of previous architectures, which contributed to its popularity.
- The transformer architecture has its own limitations.

---

## From Seq2seq to Attention
- Transformer architecture is based on the attention mechanism.
- It addresses many limitations of previous architectures, contributing to its popularity.
- This section analyzes the transformer and its alternatives.

---

## Alternatives and Limitations
- The transformer architecture has its own limitations.
- The section analyzes the transformer architecture and its alternatives.
- The material goes into technical details of different architectures and can be technically dense.

---

## Transformer Architecture: Origins

- Transformer popularized after seq2seq success in machine translation and summarization
- Seq2seq has an encoder processing inputs and a decoder generating outputs
- Both inputs and outputs are sequences of tokens
- Seq2seq uses RNNs as its encoder and decoder

---

## Limitations of Seq2seq

- Vanilla seq2seq decoder generates outputs using only the final hidden state of the input
- This is like answering questions about a book using only its summary
- RNN encoder and decoder process input and output sequentially
- Sequential processing makes seq2seq slow for long sequences

---

## How Attention Addresses These Problems

- Attention lets the model weigh the importance of different input tokens
- Each output token can reference relevant input tokens, not just a summary
- A simplified transformer architecture is shown in the bottom half of Figure 2-4
- The transformer was introduced by Vaswani et al. (2017)

---

## Attention and the Transformer
- Attention was introduced three years before the transformer paper.
- Attention can also be used with other architectures.
- Google used attention with seq2seq in its 2016 GNMT model.
- Transformers dispense with RNNs and process input tokens in parallel.

---

## Inference: Prefill
- Transformer-based autoregressive language models still have a sequential output bottleneck.
- Inference for transformer-based language models consists of two steps; prefill is first.
- Prefill processes the input tokens in parallel.
- It creates intermediate state for the first output token, including key and value vectors.

---

## Decode

- The model generates one output token at a time.
- Decoding is sequential in nature.
- Prefilling is parallelizable, while decoding is not.
- These traits motivate inference optimization techniques.

---

## Architecture Context

- Transformers replaced seq2seq architectures.
- Attention is central to the transformer mechanism.
- Weights are distributed across model components.

---

## Model Dimensions

- Dimension values differ across Llama model variants.
- Layer designs vary: transformer, Mamba, and Jamba.
- Architecture choices shape model behavior.

---

## Attention: Query, Key, Value
- Attention mechanism is at the heart of the transformer architecture
- Query (Q): current decoder state, like a person seeking information
- Key (K): represents a previous token, like a page number
- Value (V): the token's learned value, like the page's content

---

## Scoring and Computing Vectors
- Dot product between query and key scores how much attention a token gets
- High score means more of that token's value vector is used
- K, V, Q computed by applying key, value, query matrices to input x
- Longer sequences require more key and value vectors to be computed and stored

---

## Multi-Headed Attention
- Attention is almost always multi-headed; heads attend to different token groups simultaneously
- Llama 2-7B: hidden dimension 4096, so each matrix is 4096 × 4096
- Llama 2-7B has 32 heads, splitting each vector into 32 vectors of dimension 128
- Attention head outputs are concatenated, then transformed by an output projection matrix

---

## Transformer Blocks
- A transformer architecture is composed of multiple transformer blocks.
- The exact content of a block varies between models.
- Each transformer block generally contains the attention module.
- Each transformer block also generally contains the MLP module.

---

## Attention and Layer Variations
- Attention is used within the transformer block.
- Figure 2-5 shows an example of the attention mechanism in action.
- Figure 2-7 visualizes transformer, Mamba, and Jamba layers.

---

## Attention Module Weights
- Each attention module consists of four weight matrices.
- The four matrices are query, key, value, and output projection.

---

## MLP and Activation Functions
- MLP module: linear layers separated by nonlinear activation functions
- Linear layer (feedforward layer) is a weight matrix for linear transformations
- Activation functions let linear layers learn nonlinear patterns
- Common functions: ReLU (converts negative values to 0, ReLU(x) = max(0, x)) and GELU (used by GPT-2 and GPT-3)

---

## Embedding, Output, and Model Size
- Embedding module before transformer blocks: embedding matrix plus positional embedding matrix
- Number of position indices determines maximum context length; techniques can extend it
- Output layer (head) maps output vectors to token probabilities; typically the unembedding layer
- Size determined by model dimension, number of transformer blocks, feedforward dimension, vocabulary size

---

## Weight Composition and Llama Dimensions
- Larger dimension values result in larger model sizes
- Increased context length impacts memory footprint, not total parameter count
- Llama 2-70B: 80 blocks, model dim 8,192, feedforward dim 22,016, vocab 32K
- Llama 3-405B: 126 blocks, model dim 16,384, feedforward dim 53,248, vocab 128K

---

## Beyond the Transformer
- Transformers have dominated since 2017; seq2seq lasted roughly 2014–2018, GANs 2014–2019.
- Replacing the transformer is hard: it is heavily optimized and must perform at scale on relevant hardware.
- Several alternative architectures are gaining traction, especially for long-sequence modeling.
- Developing a rival architecture could change model adaptation techniques, but not fundamental approaches.

---

## RWKV and State Space Models
- RWKV is an RNN-based model that can be parallelized for training.
- In theory its RNN nature avoids transformer context length limits; in practice this doesn't guarantee long-context performance.
- SSMs (state space models) show promise for long-range memory and have evolved through several techniques.
- S4 made SSMs more efficient; H3 adds a mechanism to recall and compare tokens, akin to attention but more efficient.

---

## Mamba and Jamba
- Mamba scales SSMs to three billion parameters; Mamba-3B outperforms same-size transformers and matches twice-size ones.
- Mamba's inference computation scales linearly with sequence length, versus quadratic scaling for transformers.
- Jamba interleaves transformer and Mamba layers: 52B total parameters (12B active), fitting a single 80 GB GPU.
- Jamba handles context up to 256K tokens with a small memory footprint versus vanilla transformers.

---

## Model Size and Parameters
- Recent AI progress is largely attributed to increased model size.
- Foundation models are often described by their number of parameters.
- Parameter count is usually appended to the model name.
- Example: Llama-13B is a Llama version with 13 billion parameters.

---

## Larger Models, Greater Capacity
- Increasing a model’s parameters generally increases its capacity to learn.
- This increased capacity tends to result in better models.
- Within the same model family, larger versions are likely to perform better.
- Example: a 13-billion-parameter model likely outperforms a 7-billion-parameter model.

---

## Parameters and Model Size
- Parameters estimate compute needed to train and run a model.
- Newer-generation models tend to outperform older models of the same size.
- Llama 3-8B (2024) outperforms Llama 2-70B (2023) on MMLU.
- A 7B model at 2 bytes/parameter needs at least 14 GB for inference.

---

## Sparse Models and Mixture-of-Experts
- Parameter count can mislead for sparse models with many zero-value parameters.
- A 7B model that is 90% sparse has only 700 million non-zero parameters.
- MoE models divide parameters into experts; only a subset is active per token.
- Mixtral 8x7B has 46.7B parameters but only 12.9B active per token.

---

## Data Size and Training Tokens
- A larger model can underperform a smaller one if trained on too little data.
- Dataset size is better measured in tokens than in training samples.
- Llama used 1.4T, 2T, and 15T tokens for Llama 1, 2, and 3 respectively.
- Training tokens differ from dataset tokens: two epochs over 1T tokens means 2T training tokens.

---

## Measuring Compute for Pre-training
- Pre-training large models requires compute, measured by number of machines (GPUs, CPUs, TPUs).
- Different machines have very different capacities and costs, so machine count is not standardized.
- FLOP (floating point operation) is a standardized unit for a model’s compute requirement.
- FLOP measures floating point operations performed for a certain task.

---

## FLOPs Examples and FLOP/s Distinction
- Google’s largest PaLM-2 model was trained using 10^22 FLOPs.
- GPT-3-175B was trained using 3.14 × 10^23 FLOPs.
- FLOPs measure compute requirement; FLOP/s measures a machine’s peak performance.
- NVIDIA H100 NVL GPU delivers max 60 TeraFLOP/s: 6 × 10^13 FLOPs/second or 5.2 × 10^18 FLOPs/day.

---

## Data Quantity, Quality, Diversity
- Quantity isn’t the only thing that matters for training data.
- Data quality and data diversity matter, too.
- Quantity, quality, and diversity are the three golden goals for training data.
- These goals are discussed further in Chapter 8.

---

## Notation and Compute
- FLOP/s is often written FLOPS, which looks similar to FLOPs.
- OpenAI uses FLOP/s-day to avoid this confusion.
- 1 FLOP/s-day equals 86,400 FLOPs.
- This book uses FLOPs for operations and FLOP/s for operations per second.

---

## Training Time and Utilization
- With 256 H100s at maximum capacity, GPT-3-175B training takes about 236 days.
- That is approximately 7.8 months, assuming no training mistakes.
- 50% utilization is okay; above 70% is considered great.
- At 70% utilization and $2/H100/hour, GPT-3-175B training costs over $4 million.

---

## Model Size: Three Key Numbers

- Number of parameters: a proxy for the model’s learning capacity.
- Number of training tokens: a proxy for how much the model learned.
- Number of FLOPs: a proxy for the training cost.
- Together, these three numbers signal a model’s scale.

---

## Inverse Scaling

- Bigger models are usually better, but not always.
- Anthropic (2022): more alignment training can reduce alignment with human preference.
- More-aligned models more often express specific political, religious, and self-related views.
- Example: pro-gun rights, immigration, Buddhist views, moral self-worth, desire not to be shut down.

---

## The Inverse Scaling Prize

- Launched in 2023, mostly by New York University researchers.
- Sought tasks where larger language models perform worse.
- Prizes: $5,000 third, $20,000 second, $100,000 first.
- 99 submissions; 11 third prizes; no second or first prizes awarded.

---

## Findings on Inverse Scaling

- Larger models are only sometimes worse, on memorization and strong-prior tasks.
- No submitted task showed real-world failures, only small test-set failures.
- Hence no second or first prizes were given.

---

## Scaling Law: Compute-Optimal Models
- Model performance depends on model size and dataset size; both require compute, which costs money.
- Teams start with a compute budget and find the best model and dataset size they can afford.
- A compute-optimal model achieves the best performance given a fixed compute budget.
- The Chinchilla scaling law (DeepMind, 2022) calculates optimal model and dataset size.

---

## The Chinchilla Scaling Law
- Authors trained 400 language models from 70M to over 16B parameters on 5 to 500B tokens.
- For compute-optimal training, training tokens should be approximately 20 times the model size.
- A 3B-parameter model needs approximately 60B training tokens.
- Model size and tokens scale equally: doubling model size doubles training tokens.

---

## Beyond Compute-Optimal: Trade-offs and Diminishing Returns
- Scaling law assumes data acquisition is much cheaper than compute; a second calculation covers costly data.
- The law was developed for dense models on human data; adapting to sparse models and synthetic data is active research.
- Model quality isn't everything: Llama chose smaller models for easier use and cheaper inference.
- Cost for the same performance is falling, but improving performance remains expensive; a 2% error rate may need an order of magnitude more data.

---

## Hyperparameter Tuning for Small Models
- Model performance depends heavily on hyperparameter values.
- Small models: train multiple times with different hyperparameter sets.
- Select the best-performing model from these runs.

---

## Challenges for Large Models
- Large models are rarely trained multiple times.
- A single training run is already resource-draining.
- Hyperparameter tuning via multiple runs is thus impractical.

---

## Parameters vs. Hyperparameters
- Parameters are learned by the model during training.
- Hyperparameters are set by users to configure the model and control learning.
- Configuring hyperparameters include number of layers, model dimension, and vocabulary size.
- Learning-control hyperparameters include batch size, epochs, learning rate, and per-layer initial variance.

---

## Scaling Extrapolation
- Scaling extrapolation predicts which hyperparameters will give best performance for large models.
- It studies hyperparameters on smaller models, then extrapolates to the target model size.
- A 2022 Microsoft and OpenAI paper transferred hyperparameters from a 40M model to a 6.7B model.
- It is niche and difficult: ten hyperparameters require studying 1,024 combinations.

---

## Emergent Abilities and Extrapolation
- Emergent abilities are present only at scale and may not appear in smaller models.
- They make scaling extrapolation less accurate.
- The source points to “On the Difficulty of Extrapolation with NN Scaling” by Luke Metz, 2022.

---

## Scaling Bottlenecks

- Each order-of-magnitude increase in model size has raised model performance.
- GPT-1 to GPT-2: 117 million to 1.5 billion parameters—one order of magnitude.
- GPT-2 to GPT-3: 1.5 billion to 175 billion—two orders of magnitude.
- Model sizes grew three orders of magnitude between 2018 and 2021.

---

## Two Visible Bottlenecks

- Scaling further faces two visible bottlenecks: training data and electricity.
- Training dataset size grows faster than new data is generated (Villalobos et al., 2022).
- There is realistic concern the internet will run out of usable data in a few years.
- Assume anything posted online may enter some language model's training data.

---

## Data as Influence and Attack Surface

- People publish text online hoping it enters future models' training data.
- They aim to influence future models to generate desired responses.
- Bad actors can use the same approach for prompt injection attacks.
- Prompt injection is discussed further in Chapter 5.

---

## Data Limits and Forgetting

- Open question: how to make a model forget specific information learned during training
- Deleted content may still be reproduced if it was in training data
- The web is full of ChatGPT outputs, so new models train on AI-generated data
- Researchers worry recursive training on AI data degrades performance over time

---

## Proprietary Data as Advantage

- Once public data is exhausted, proprietary data is the most feasible human-generated source
- Unique data—books, translations, contracts, medical records, genomes—becomes a competitive advantage
- OpenAI negotiated deals with publishers and media outlets like Axel Springer and AP
- Reddit and Stack Overflow changed terms; 45% of C4 is now restricted

---

## The Electricity Bottleneck

- Electricity is a less obvious but more pressing bottleneck than data
- Data centers are estimated to consume 1–2% of global electricity today
- That is estimated to reach 4% to 20% by 2030
- Without more energy production, data centers can grow at most 50 times

---

## Post-Training: Purpose and Steps
- Post-training starts from a pre-trained model and addresses two issues.
- Issue one: self-supervision optimizes text completion, not conversations.
- Issue two: indiscriminate internet data can produce racist, sexist, rude, or wrong outputs.
- Post-training generally consists of supervised finetuning, then preference finetuning.

---

## SFT and Preference Finetuning
- SFT finetunes the pre-trained model on high-quality instruction data for conversations.
- Preference finetuning further tunes responses to align with human preference.
- Techniques include RLHF (GPT-3.5, Llama 2), DPO (Llama 3), and RLAIF (potentially Claude).
- Avoid the ambiguous term “instruction finetuning,” which can mean SFT alone or both steps.

---

## Pre-Training vs Post-Training
- Pre-training optimizes token-level quality: predicting the next token accurately.
- Users care about the quality of the entire response, which post-training optimizes.
- InstructGPT used only 2% of compute for post-training and 98% for pre-training.
- Figure 2-10 shows the workflow of pre-training, SFT, and RLHF.

---

## Why Supervised Finetuning
- Pre-trained models are optimized for completion, not conversation; "How to make pizza" gets continued, not answered.
- To respond to users appropriately, the model must give instructions rather than add context or follow-ups.
- Models mimic their training data, so show examples of appropriate responses.
- Demonstration data follows the (prompt, response) format; this is sometimes called behavior cloning.

---

## Covering Tasks and Choosing Labelers
- Demonstration data should span the request types you want handled, such as question answering, summarization, and translation.
- Figure 2-12 shows the task distribution OpenAI used to finetune InstructGPT, a text-only model.
- Demonstration prompts may need critical thinking, information gathering, and judgment about appropriateness.
- ~90% of InstructGPT labelers had a college degree; over one-third held a master's degree.

---

## Cost of Human Annotation and Alternatives
- One (prompt, response) pair can take up to 30 minutes, especially for long-context tasks like summarization.
- At $10 per pair, 13,000 InstructGPT pairs would cost $130,000, excluding design, recruiting, and quality control.
- LAION mobilized 13,500 volunteers to produce 10,000 conversations: 161,443 messages, 35 languages, 461,292 quality ratings.
- Volunteer demographics were skewed; in a self-reported survey, 90% of labelers identified as male.

---

## Why Preference Finetuning
- Demonstration data teaches conversation, but not which conversations the model should have.
- Preference finetuning aims to make models behave according to human preference.
- The goal is ambitious: it assumes universal human preference exists and can be embedded.
- Over-censoring can make a model boring, driving users away.

---

## Reward Models and Comparison Data
- Pointwise scores vary between labelers, and even for the same labeler.
- Comparison data follows (prompt, winning_response, losing_response) and is easier to label.
- Comparisons cost roughly $3.50 each, versus $25 per written response.
- InstructGPT labelers' inter-labeler agreement was around 73%.

---

## RLHF and Alternatives
- RLHF trains a reward model, then optimizes the model to maximize its scores.
- The optimization step is often done with proximal policy optimization (PPO).
- DPO is gaining traction; Meta switched from RLHF for Llama 2 to DPO for Llama 3.
- RLHF and DPO both improve over SFT alone, but why remains debated.

---

## Context: Why Finetuning Exists
- SFT and preference finetuning address problems created by low-quality pre-training data.
- Better pre-training data or training methods might remove the need for SFT and preference finetuning.
- Some companies skip reinforcement learning entirely in their workflows.
- Stitch Fix and Grab find a reward model alone sufficient for their applications.

---

## Best of N Strategy
- Models generate multiple outputs, and the highest-scoring ones are selected.
- This approach is often referred to as the _best of N_ strategy.
- It leverages how a model samples outputs to improve performance.
- The next section explains how best of N works.

---

## Sampling Fundamentals
- A model constructs its outputs through a process known as _sampling_.
- Sampling strategies and sampling variables include temperature, top-k, and top-p.
- Sampling multiple outputs can improve a model's performance.
- Sampling can be modified to produce responses in certain formats and constraints.
- Sampling makes AI's outputs probabilistic, which matters for behaviors like inconsistency.

---

## Sampling Fundamentals

- A neural network first computes probabilities of possible outcomes from its input.
- Classification example: an email is 90% spam, 10% not spam.
- Decisions follow from probabilities, e.g. label spam above a 50% threshold.
- For a language model, the distribution covers every token in the vocabulary.

---

## Greedy Sampling vs. Sampling

- Always picking the most likely outcome is called greedy sampling.
- Greedy sampling often works well for classification tasks.
- For language models, greedy sampling creates boring outputs—always the most common words.
- Sampling instead picks tokens according to the distribution: "red" 30%, "green" 50%.

---

## From Logits to Probabilities

- Given an input, a neural network outputs a logit vector.
- Each logit corresponds to one token in the model's vocabulary.
- The logit vector size equals the size of the vocabulary.
- Larger logits mean higher probabilities, but logits aren't probabilities: they can be negative.

---

## Temperature Sampling
- Temperature divides logits before softmax, redistributing token probabilities.
- Higher temperature lowers common-token probability, raising rarer tokens for more creative output.
- Lower temperature favors the highest-logit token, making output more consistent but boring.
- Example: logits [1, 2] give [0.27, 0.73] at T=1, [0.12, 0.88] at T=0.5.

---

## Temperature Settings and Logprobs
- Providers typically limit temperature to 0–2; 0.7 is often recommended for creative use cases.
- Setting temperature to 0 makes the model pick the largest logit without softmax.
- Logprobs are probabilities in log scale, reducing underflow with large vocabularies.
- Logprobs help with classification, evaluation, and understanding models, but APIs are often limited.

---

## Top-k, Top-p, and Min-p
- Top-k performs softmax over only the top-k logits, reducing computation; k ranges 50–500.
- Smaller k makes text more predictable but less interesting.
- Top-p (nucleus) sampling considers the smallest set of values whose cumulative probability reaches p.
- Common top-p values are 0.9–0.95; min-p sets a minimum probability threshold for tokens.

---

## Test Time Compute
- Generate multiple responses per query instead of one, increasing the chance of good responses
- Best-of-N: randomly generate many outputs and pick one that works best
- Beam search generates a fixed number of most promising candidates at each step
- Vary sampling variables to diversify outputs; two outputs cost roughly twice as much

---

## Selecting the Best Output
- Show users multiple outputs, or devise a method to select the best one
- Pick highest probability output: product of token probabilities, summed on a log scale
- Average logprob avoids bias toward short sequences; the OpenAI API uses this
- Reward models or verifiers score outputs; Nextdoor called this the key factor

---

## Scaling Test Time Compute
- OpenAI: verifiers gave roughly the same boost as a 30× model size increase
- DeepMind argues scaling test time compute can be more efficient than scaling parameters
- OpenAI found gains only up to 400 outputs, after which performance decreased
- Heuristics: shortest response, valid SQL, or most common answer (Gemini sampled 32 on MMLU)

---

## Structured Outputs
- Production models often need specific formats for semantic parsing or downstream applications.
- Semantic parsing converts natural language into machine-readable formats like SQL or regex.
- Downstream apps may require JSON with specific keys; agentic workflows pass outputs to tools.
- Approaches include prompting, post-processing, test time compute, constrained sampling, and finetuning.

---

## Improving Structured Outputs
- Prompting is first action but cannot guarantee valid outputs.
- Post-processing fixes common repeated mistakes; LinkedIn’s YAML parser raised correctness from 90% to 99.99%.
- Constrained sampling filters logits using grammars; grammar verification can add latency.
- Finetuning is effective and general; classifier heads can guarantee classification outputs.

---

## The Probabilistic Nature of AI
- AI models sample responses, so outputs are probabilistic rather than deterministic.
- A model may answer "Vietnamese cuisine" 70% of the time and "Italian cuisine" 30%.
- Deterministic means the outcome can be determined without random variation.
- Probabilistic outputs cause inconsistency and hallucination; anything with non-zero probability can be generated.

---

## Inconsistency
- Same input, different outputs: identical prompts can yield very different responses.
- Slightly different input, drastically different outputs: even a capitalized letter can change results.
- Mitigations: cache answers, fix sampling variables (temperature, top-p, top-k), and fix the seed.
- Hardware differences can still affect outputs; fixing settings doesn't guarantee 100% consistency.

---

## Hallucination
- Hallucination is a response not grounded in facts, fatal for factuality-dependent tasks.
- Hypothesis 1: models can't distinguish given data from their own generated data (self-delusion).
- Snowballing: an incorrect initial assumption leads the model to justify it and keep erring.
- Hypothesis 2: mismatch between the model's internal knowledge and the labeler's knowledge.

---

## Chapter Summary: Model Design
- Foundation model design decisions include training data, architecture, size, and post-training.
- Providers often use available data, so models may not target your specific task.
- Transformer dominates language-based foundation models; scaling law guides parameters and tokens.
- Post-training uses supervised finetuning and preference finetuning to align outputs with user wants.

---

## Probabilistic Behavior and Evaluation
- Sampling makes model outputs probabilistic, enabling creativity but causing inconsistency and hallucinations.
- Prompting, concise responses, and context construction can help mitigate hallucinations.
- Detecting hallucinations is difficult; Chapter 4 discusses detection and measurement.
- Build workflows around probabilistic nature and establish evaluation pipelines to detect failures.

## Practice Questions

### Question 1: According to the source, differences in foundation models can gener...

According to the source, differences in foundation models can generally be traced back to decisions about what?

- [ ] A) Training data only
- [ ] B) Model architecture and size only
- [ ] C) Post-training alignment only
- [ ] D) Training data, model architecture and size, and post-training alignment

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** D

    **Explanation:** The text states that differences in foundation models can generally be traced to decisions about training data, architecture and size, and post-training alignment with human preferences.

### Question 2: What is the goal of post-training a foundation model?

What is the goal of post-training a foundation model?

- [ ] A) To reduce the model’s size
- [ ] B) To align the model with human preferences
- [ ] C) To replace the transformer architecture
- [ ] D) To collect training data

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** The source says pre-training makes a model capable, while post-training aims to align the model with human preferences.

### Question 3: How does the source describe sampling?

How does the source describe sampling?

- [ ] A) It is how a model chooses an output from all possible options and is often underrated.
- [ ] B) It is the process of curating training data.
- [ ] C) It is the main way developers determine model size.
- [ ] D) It is the step that replaces pre-training.

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** A

    **Explanation:** The text defines sampling as how a model chooses an output from all possible options and calls it perhaps one of the most underrated concepts in AI.

### Question 4: According to the Common Crawl analysis in the source text, what sha...

According to the Common Crawl analysis in the source text, what share of the data does English account for, and how does it compare with Russian?

- [ ] A) 45.88%, making it eight times more prevalent than Russian
- [ ] B) 5.97%, making it eight times more prevalent than Russian
- [ ] C) 45.88%, making it twice as prevalent as Russian
- [ ] D) 18.15%, making it eight times more prevalent than Russian

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** A

    **Explanation:** The text states English accounts for almost half of Common Crawl data (45.88%) and is eight times more prevalent than Russian (5.97%).

### Question 5: How does the source text define “low-resource” languages?

How does the source text define “low-resource” languages?

- [ ] A) Languages with fewer than one million speakers
- [ ] B) Languages with limited availability as training data, typically those not among languages with at least 1% in Common Crawl
- [ ] C) Languages that are never used on the internet
- [ ] D) Languages with unusually complex grammar

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** The text says languages with limited availability as training data—typically languages not included in the list of those with at least 1% in Common Crawl—are considered low-resource.

### Question 6: According to the source text, why is translating all non-English qu...

According to the source text, why is translating all non-English queries into English, getting responses, and translating them back not ideal?

- [ ] A) It always requires human translators
- [ ] B) It can cause information loss, such as losing relationship information in Vietnamese pronouns translated as “I” and “you”
- [ ] C) It cannot be done with GPT-4
- [ ] D) It makes the model worse at English

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** The text says translation can cause information loss, using Vietnamese pronouns that denote speaker relationships as an example.

### Question 7: In Yennie Jun’s MASSIVE benchmarking described in the source text,...

In Yennie Jun’s MASSIVE benchmarking described in the source text, which language had a median token length of 72, about ten times longer than English’s median of 7?

- [ ] A) Burmese
- [ ] B) Hindi
- [ ] C) Spanish
- [ ] D) Russian

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** A

    **Explanation:** The text states the median token length in English is 7, in Hindi is 32, and in Burmese is 72, ten times longer than English.

### Question 8: According to the text, why are general-purpose foundation models un...

According to the text, why are general-purpose foundation models unlikely to perform well on domain-specific tasks?

- [ ] A) They are unlikely to have seen those specific tasks during training
- [ ] B) They can only process English text
- [ ] C) They are always trained only on public internet data
- [ ] D) They cannot generate tokens for specialized domains

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** A

    **Explanation:** The text states that general-purpose models are unlikely to perform well on domain-specific tasks, especially if they never saw these tasks during training.

### Question 9: Which model is described as trained on the sequences and 3D structu...

Which model is described as trained on the sequences and 3D structures of around 100,000 known proteins?

- [ ] A) AlphaFold
- [ ] B) BioNeMo
- [ ] C) Med-PaLM2
- [ ] D) ChatGLM

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** A

    **Explanation:** The text identifies DeepMind’s AlphaFold as trained on the sequences and 3D structures of around 100,000 known proteins.

### Question 10: Which domain-specific model and focus are correctly paired accordin...

Which domain-specific model and focus are correctly paired according to the text?

- [ ] A) NVIDIA’s BioNeMo — biomolecular data for drug discovery
- [ ] B) Google’s Med-PaLM2 — protein structure prediction
- [ ] C) DeepMind’s AlphaFold — medical query answering
- [ ] D) CroissantLLM — cancer screening from fMRI scans

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** A

    **Explanation:** The text says NVIDIA’s BioNeMo focuses on biomolecular data for drug discovery.

### Question 11: According to the source, what decisions do developers need to make...

According to the source, what decisions do developers need to make before training a model?

- [ ] A) Only the training dataset size and learning rate
- [ ] B) The model architecture and number of parameters
- [ ] C) Only the deployment hardware and latency target
- [ ] D) The tokenizer vocabulary and licensing terms

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** The source says developers need to decide what the model should look like, including architecture and parameter count.

### Question 12: Why does the source mention a 7B-parameter model versus a 175B-para...

Why does the source mention a 7B-parameter model versus a 175B-parameter model?

- [ ] A) To show that larger models are always easier to optimize for latency
- [ ] B) To illustrate that parameter count affects usability for downstream applications
- [ ] C) To argue that transformer models cannot be deployed
- [ ] D) To compare two different attention mechanisms

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** The source uses this example to show that a 7B-parameter model will be vastly easier to deploy than a 175B-parameter model.

### Question 13: As of the source’s writing, what is the most dominant architecture...

As of the source’s writing, what is the most dominant architecture for language-based foundation models?

- [ ] A) The transformer architecture, based on the attention mechanism
- [ ] B) A recurrent architecture with no attention mechanism
- [ ] C) A convolutional architecture optimized only for images
- [ ] D) A rule-based architecture with no parameters

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** A

    **Explanation:** The source states that the transformer architecture is the most dominant for language-based foundation models and is based on the attention mechanism.

### Question 14: According to the text, what do developers need to decide before tra...

According to the text, what do developers need to decide before training a model?

- [ ] A) Only the training dataset size
- [ ] B) The model architecture and how many parameters it should have
- [ ] C) Only the deployment cloud provider
- [ ] D) The downstream application’s user interface

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** The text says developers need to decide what architecture the model should follow and how many parameters it should have before training.

### Question 15: What do the text’s modeling decisions impact?

What do the text’s modeling decisions impact?

- [ ] A) Only the model’s color scheme
- [ ] B) Only the training time
- [ ] C) The model’s capabilities and its usability for downstream applications
- [ ] D) Only the model’s license

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** C

    **Explanation:** The source states these decisions impact not only the model’s capabilities but also its usability for downstream applications.

### Question 16: According to the example in the text, which model will be vastly ea...

According to the example in the text, which model will be vastly easier to deploy?

- [ ] A) A 175B-parameter model
- [ ] B) A 7B-parameter model
- [ ] C) A model with no parameters
- [ ] D) A non-transformer model

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** The text gives the example that a 7B-parameter model will be vastly easier to deploy than a 175B-parameter model.

### Question 17: What does the text say about optimizing a transformer model for lat...

What does the text say about optimizing a transformer model for latency?

- [ ] A) It is identical to optimizing any other architecture
- [ ] B) It is unrelated to model architecture
- [ ] C) It is very different from optimizing another architecture
- [ ] D) It only depends on the number of parameters

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** C

    **Explanation:** The source says optimizing a transformer model for latency is very different from optimizing another architecture.

### Question 18: As of the writing of the source text, what is the most dominant arc...

As of the writing of the source text, what is the most dominant architecture for language-based foundation models?

- [ ] A) The transformer architecture
- [ ] B) The convolutional neural network architecture
- [ ] C) The recurrent neural network architecture
- [ ] D) The support vector machine architecture

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** A

    **Explanation:** The source states that the transformer architecture is the most dominant architecture for language-based foundation models as of this writing.

### Question 19: The transformer architecture is based on which mechanism?

The transformer architecture is based on which mechanism?

- [ ] A) The attention mechanism
- [ ] B) The convolution mechanism
- [ ] C) The recurrence mechanism
- [ ] D) The pooling mechanism

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** A

    **Explanation:** The source says the transformer architecture is based on the attention mechanism.

### Question 20: According to the source, which statement about the transformer arch...

According to the source, which statement about the transformer architecture is accurate?

- [ ] A) It has no limitations.
- [ ] B) It addresses many limitations of previous architectures but has its own limitations.
- [ ] C) It is not based on attention.
- [ ] D) It is the only architecture discussed in the section.

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** The source says the transformer addresses many limitations of previous architectures, contributing to its popularity, but it also has its own limitations.

### Question 21: What does the source say the section analyzes?

What does the source say the section analyzes?

- [ ] A) Only the transformer architecture
- [ ] B) The transformer architecture and its alternatives
- [ ] C) Only previous architectures
- [ ] D) Only attention mechanisms

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** The source states that the section analyzes the transformer architecture and its alternatives.

### Question 22: According to the source text, what does the seq2seq architecture us...

According to the source text, what does the seq2seq architecture use as its encoder and decoder?

- [ ] A) Transformers
- [ ] B) RNNs
- [ ] C) Attention mechanisms
- [ ] D) Convolutional networks

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** The text states that seq2seq uses RNNs (recurrent neural networks) as its encoder and decoder.

### Question 23: Which of the following is one of the two problems with seq2seq that...

Which of the following is one of the two problems with seq2seq that the transformer architecture addresses?

- [ ] A) The decoder generates output tokens using only the final hidden state of the input.
- [ ] B) The encoder and decoder use attention mechanisms.
- [ ] C) The model cannot process sequences of tokens.
- [ ] D) The decoder processes all input tokens in parallel.

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** A

    **Explanation:** The text says the vanilla seq2seq decoder generates output tokens using only the final hidden state of the input, limiting output quality.

### Question 24: What does the attention mechanism allow a transformer model to do?

What does the attention mechanism allow a transformer model to do?

- [ ] A) Process all input tokens simultaneously without any weighting
- [ ] B) Weigh the importance of different input tokens when generating each output token
- [ ] C) Replace the encoder and decoder with a single RNN
- [ ] D) Generate output tokens using only the final hidden state of the input

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** The text states that the attention mechanism allows the model to weigh the importance of different input tokens when generating each output token.

### Question 25: According to the source, when was the attention mechanism introduce...

According to the source, when was the attention mechanism introduced relative to the transformer paper?

- [ ] A) Three years after the transformer paper
- [ ] B) In the same year as the transformer paper
- [ ] C) Three years before the transformer paper
- [ ] D) It was introduced by the transformer paper itself

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** C

    **Explanation:** The source states that attention was introduced three years before the transformer paper.

### Question 26: What does the transformer architecture dispense with entirely, and...

What does the transformer architecture dispense with entirely, and what bottleneck do transformer-based autoregressive language models still have?

- [ ] A) It dispenses with attention and still has a sequential input bottleneck.
- [ ] B) It dispenses with RNNs entirely and still has a sequential output bottleneck.
- [ ] C) It dispenses with key and value vectors and still has a parallel output bottleneck.
- [ ] D) It dispenses with prefill and still has a parallel input bottleneck.

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** The source says transformers dispense with RNNs entirely, and autoregressive transformer-based language models still have the sequential output bottleneck.

### Question 27: During prefill, what does the model do?

During prefill, what does the model do?

- [ ] A) It processes output tokens sequentially to create key and value vectors for the last token only.
- [ ] B) It processes input tokens in parallel and creates the intermediate state needed to generate the first output token.
- [ ] C) It removes the sequential output bottleneck by generating all output tokens at once.
- [ ] D) It uses RNNs to process input tokens one by one before generating the first output token.

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** The source describes prefill as processing input tokens in parallel to create the intermediate state necessary to generate the first output token.

### Question 28: According to the text, how does the model generate output during de...

According to the text, how does the model generate output during decoding?

- [ ] A) It generates all output tokens simultaneously.
- [ ] B) It generates one output token at a time.
- [ ] C) It generates only the first and last tokens.
- [ ] D) It generates tokens only after prefilling is disabled.

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** The text states that during decode, the model generates one output token at a time.

### Question 29: Which aspect of decoding is mentioned as motivating optimization te...

Which aspect of decoding is mentioned as motivating optimization techniques?

- [ ] A) Its sequential nature.
- [ ] B) Its ability to avoid token generation.
- [ ] C) Its complete parallelism with prefilling.
- [ ] D) Its lack of effect on inference cost.

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** A

    **Explanation:** The text refers to the sequential aspect of decoding as one motivation for optimization techniques.

### Question 30: What do the parallelizable nature of prefilling and the sequential...

What do the parallelizable nature of prefilling and the sequential aspect of decoding motivate?

- [ ] A) Techniques to make language model inference cheaper and faster.
- [ ] B) Techniques to eliminate output tokens entirely.
- [ ] C) Techniques to make decoding fully parallel.
- [ ] D) Techniques to avoid using foundation models.

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** A

    **Explanation:** The text says both motivate many optimization techniques to make language model inference cheaper and faster.

### Question 31: In the attention mechanism described, what does the query vector (Q...

In the attention mechanism described, what does the query vector (Q) represent?

- [ ] A) The actual content of a previous token as learned by the model
- [ ] B) The page number identifying a previous token
- [ ] C) The current state of the decoder at each decoding step
- [ ] D) The final concatenated output of all attention heads

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** C

    **Explanation:** The source states that the query vector represents the current state of the decoder at each decoding step, analogous to a person looking for information to create a summary.

### Question 32: How does the attention mechanism compute how much attention to give...

How does the attention mechanism compute how much attention to give an input token?

- [ ] A) By concatenating all value vectors and applying an output projection matrix
- [ ] B) By performing a dot product between the query vector and the token’s key vector
- [ ] C) By dividing the hidden dimension by the number of attention heads
- [ ] D) By applying the key, value, and query matrices directly to the output projection matrix

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** The source says attention computes how much attention to give an input token by performing a dot product between the query vector and its key vector.

### Question 33: In Llama 2-7B, which has a hidden dimension of 4096 and 32 attentio...

In Llama 2-7B, which has a hidden dimension of 4096 and 32 attention heads, what is the dimension of each split K, V, and Q vector per attention head?

- [ ] A) 32
- [ ] B) 128
- [ ] C) 4096
- [ ] D) 8192

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** The source explains that with 32 attention heads, each 4096-dimensional K, V, and Q vector is split into 32 vectors of dimension 128 because 4096 / 32 = 128.

### Question 34: According to the text, what is a transformer architecture composed of?

According to the text, what is a transformer architecture composed of?

- [ ] A) A single attention module
- [ ] B) Multiple transformer blocks
- [ ] C) One MLP module and one attention head
- [ ] D) A stack of MLP modules only

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** The text states that a transformer architecture is composed of multiple transformer blocks.

### Question 35: In general, which two modules does each transformer block contain?

In general, which two modules does each transformer block contain?

- [ ] A) The attention module and the MLP module
- [ ] B) The embedding module and the output module
- [ ] C) The attention module and the normalization module
- [ ] D) The MLP module and the decoder module

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** A

    **Explanation:** The text says that, in general, each transformer block contains the attention module and the MLP (multi-layer perceptron) module.

### Question 36: What does the text say about the exact content of a transformer block?

What does the text say about the exact content of a transformer block?

- [ ] A) It is identical across all models
- [ ] B) It varies between models
- [ ] C) It contains only the attention module
- [ ] D) It is defined solely by the number of attention heads

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** The text notes that the exact content of the block varies between models, though it generally includes the attention and MLP modules.

### Question 37: What does MLP stand for in the text?

What does MLP stand for in the text?

- [ ] A) Multi-layer perceptron
- [ ] B) Multi-level processing
- [ ] C) Modular linear pipeline
- [ ] D) Multi-layer parameter

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** A

    **Explanation:** The text expands MLP as multi-layer perceptron.

### Question 38: How many weight matrices does each attention module consist of?

How many weight matrices does each attention module consist of?

- [ ] A) Two
- [ ] B) Three
- [ ] C) Four
- [ ] D) Five

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** C

    **Explanation:** The text states that each attention module consists of four weight matrices.

### Question 39: Which of the following is NOT one of the four weight matrices in an...

Which of the following is NOT one of the four weight matrices in an attention module?

- [ ] A) Query
- [ ] B) Key
- [ ] C) Value
- [ ] D) Embedding

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** D

    **Explanation:** The four weight matrices listed are query, key, value, and output projection; embedding is not among them.

### Question 40: Which set correctly lists the weight matrices of an attention module?

Which set correctly lists the weight matrices of an attention module?

- [ ] A) Query, key, value, and output projection
- [ ] B) Query, key, value, and input projection
- [ ] C) Query, score, value, and output projection
- [ ] D) Key, value, output projection, and bias

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** A

    **Explanation:** The text specifies exactly four matrices: query, key, value, and output projection.

### Question 41: What is a linear layer within an MLP module described as?

What is a linear layer within an MLP module described as?

- [ ] A) A nonlinear activation function
- [ ] B) A weight matrix used for linear transformations
- [ ] C) A positional embedding matrix
- [ ] D) An unembedding layer

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** The text states that each linear layer is a weight matrix used for linear transformations, and a linear layer is also called a feedforward layer.

### Question 42: According to the text, which activation functions were used by GPT-...

According to the text, which activation functions were used by GPT-2 and GPT-3, respectively?

- [ ] A) ReLU and Sigmoid
- [ ] B) GELU and ReLU
- [ ] C) ReLU and GELU
- [ ] D) Sigmoid and GELU

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** C

    **Explanation:** The text says ReLU and GELU were used by GPT-2 and GPT-3, respectively.

### Question 43: Naively, what determines a model's maximum context length?

Naively, what determines a model's maximum context length?

- [ ] A) The number of position indices
- [ ] B) The vocabulary size
- [ ] C) The feedforward layer dimension
- [ ] D) The number of transformer blocks

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** A

    **Explanation:** The text states that naively, the number of position indices determines the model's maximum context length.

### Question 44: Which of the following is NOT listed among the key values that dete...

Which of the following is NOT listed among the key values that determine a transformer model's size?

- [ ] A) The model's dimension
- [ ] B) The number of transformer blocks
- [ ] C) The dimension of the feedforward layer
- [ ] D) The number of position indices

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** D

    **Explanation:** The text lists the model's dimension, number of transformer blocks, feedforward layer dimension, and vocabulary size as key values; position indices are not among them.

### Question 45: Which model is described as an RNN-based architecture that can be p...

Which model is described as an RNN-based architecture that can be parallelized for training and, in theory, does not have the same context length limitation as transformer-based models?

- [ ] A) RWKV
- [ ] B) Mamba
- [ ] C) Jamba
- [ ] D) GAN

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** A

    **Explanation:** The text states RWKV is an RNN-based model that can be parallelized for training and in theory lacks the same context length limitation as transformer-based models.

### Question 46: According to the source, how does Mamba’s inference computation sca...

According to the source, how does Mamba’s inference computation scale with sequence length compared to transformers?

- [ ] A) Linearly, compared to quadratic scaling for transformers
- [ ] B) Quadratically, compared to linear scaling for transformers
- [ ] C) It does not scale with sequence length
- [ ] D) It scales exponentially, compared to linear scaling for transformers

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** A

    **Explanation:** The text says the Mamba authors show inference computation scales linearly with sequence length, compared to quadratic scaling for transformers.

### Question 47: What does Jamba interleave to scale up SSMs further?

What does Jamba interleave to scale up SSMs further?

- [ ] A) Blocks of transformer and Mamba layers
- [ ] B) Blocks of GAN and seq2seq layers
- [ ] C) Blocks of RWKV and S4 layers
- [ ] D) Blocks of H3 and transformer layers

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** A

    **Explanation:** The source describes Jamba as interleaving blocks of transformer and Mamba layers to scale up SSMs even further.

### Question 48: What does the "13B" in the model name Llama-13B refer to?

What does the "13B" in the model name Llama-13B refer to?

- [ ] A) The model was trained for 13 billion steps
- [ ] B) The model has 13 billion parameters
- [ ] C) The model supports 13 billion tokens
- [ ] D) The model was released in 2013

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** The source states that Llama-13B refers to the version of Llama with 13 billion parameters. The number of parameters is usually appended at the end of a model name.

### Question 49: In general, what happens when a model’s number of parameters is inc...

In general, what happens when a model’s number of parameters is increased?

- [ ] A) Its capacity to learn increases, resulting in better models
- [ ] B) Its capacity to learn decreases, resulting in simpler models
- [ ] C) Its number of parameters is no longer part of its name
- [ ] D) It can no longer be compared with models in the same family

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** A

    **Explanation:** The source says that increasing a model’s parameters increases its capacity to learn, resulting in better models.

### Question 50: Given two models from the same model family, which is likely to per...

Given two models from the same model family, which is likely to perform much better according to the source?

- [ ] A) The model with 7 billion parameters
- [ ] B) The model with fewer parameters
- [ ] C) The model with 13 billion parameters
- [ ] D) The model whose name does not include parameter count

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** C

    **Explanation:** The source states that between two models of the same family, the one with 13 billion parameters is likely to perform much better than the one with 7 billion parameters.

### Question 51: According to the source, why can a newer-generation model outperfor...

According to the source, why can a newer-generation model outperform an older-generation model of the same size?

- [ ] A) Newer models always have more parameters than older models.
- [ ] B) The community better understands how to train large models, so newer models tend to outperform older models of the same size.
- [ ] C) Older models are always sparse, while newer models are dense.
- [ ] D) Newer models are trained on fewer tokens but with higher-quality tokenization.

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** The note states that as the community better understands training large models, newer-generation models tend to outperform older-generation models of the same size.

### Question 52: Which statement about Mixtral 8x7B is correct based on the source?

Which statement about Mixtral 8x7B is correct based on the source?

- [ ] A) It has 56 billion active parameters for every token.
- [ ] B) It has 46.7 billion total parameters, but only 12.9 billion parameters are active for each token.
- [ ] C) It has 8 billion total parameters and all experts are active for each token.
- [ ] D) It is a dense model whose cost and speed match a 46.7-billion-parameter model.

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** The source says Mixtral 8x7B has 46.7 billion parameters due to shared parameters, and only 12.9 billion parameters are active for each token.

### Question 53: If a dataset contains 1 trillion tokens and a model is trained on t...

If a dataset contains 1 trillion tokens and a model is trained on that dataset for two epochs, what is the number of training tokens?

- [ ] A) 500 billion
- [ ] B) 1 trillion
- [ ] C) 2 trillion
- [ ] D) 3 trillion

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** C

    **Explanation:** The source defines an epoch as a pass through the dataset, so two epochs over 1 trillion tokens means 2 trillion training tokens.

### Question 54: What does FLOP measure?

What does FLOP measure?

- [ ] A) The number of floating point operations performed for a certain task
- [ ] B) A machine’s peak performance per second
- [ ] C) The number of GPUs needed for training
- [ ] D) The quality and diversity of training data

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** A

    **Explanation:** The text defines FLOP as floating point operation and says it measures the number of floating point operations performed for a certain task.

### Question 55: According to the text, what is the difference between FLOPs and FLO...

According to the text, what is the difference between FLOPs and FLOP/s?

- [ ] A) FLOPs measures a machine’s peak performance, while FLOP/s measures a task’s compute requirement
- [ ] B) FLOPs measures the compute requirement for a task, while FLOP/s measures a machine’s peak performance
- [ ] C) FLOPs measures data quantity, while FLOP/s measures data quality
- [ ] D) FLOPs and FLOP/s are two names for exactly the same measurement

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** The text states that FLOPs measure the compute requirement for a task, whereas FLOP/s measures a machine’s peak performance.

### Question 56: Why does the text say the number of machines is not a standardized...

Why does the text say the number of machines is not a standardized way to measure a model’s compute requirement?

- [ ] A) Because only GPUs are used for pre-training large models
- [ ] B) Because different machines have very different capacities and costs
- [ ] C) Because FLOP cannot be used for large models
- [ ] D) Because data diversity is more important than compute

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** The text notes that different machines have very different capacities and costs, so a more standardized unit such as FLOP is used.

### Question 57: What are described as the three golden goals for training data?

What are described as the three golden goals for training data?

- [ ] A) Speed, cost, and size
- [ ] B) Quantity, quality, and diversity
- [ ] C) FLOPs, FLOP/s, and compute
- [ ] D) GPUs, CPUs, and TPUs

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** The note states that quantity, quality, and diversity are the three golden goals for training data.

### Question 58: According to the text, what does FLOP/s denote?

According to the text, what does FLOP/s denote?

- [ ] A) Floating point operations counted in total
- [ ] B) FLOPs per second
- [ ] C) FLOPs per day
- [ ] D) A model size unit

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** The book uses FLOPs for counting floating point operations and FLOP/s for FLOPs per second.

### Question 59: According to the text, how many FLOPs is 1 FLOP/s-day?

According to the text, how many FLOPs is 1 FLOP/s-day?

- [ ] A) 24 FLOPs
- [ ] B) 1,440 FLOPs
- [ ] C) 86,400 FLOPs
- [ ] D) 5.2 × 10^18 FLOPs

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** C

    **Explanation:** The text states 1 FLOP/s-day = 60 × 60 × 24 = 86,400 FLOPs.

### Question 60: With 256 H100s used at maximum capacity and no training mistakes, a...

With 256 H100s used at maximum capacity and no training mistakes, approximately how long would it take to train GPT-3-175B?

- [ ] A) About 23.6 days
- [ ] B) About 86.4 days
- [ ] C) About 236 days, or approximately 7.8 months
- [ ] D) About 70 days

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** C

    **Explanation:** The text says it would take about 236 days, or approximately 7.8 months, under those assumptions.

### Question 61: According to the text, what level of utilization is generally consi...

According to the text, what level of utilization is generally considered great?

- [ ] A) 50% utilization
- [ ] B) Anything above 70% utilization
- [ ] C) Exactly 25% utilization
- [ ] D) Any utilization below 50%

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** The text says 50% utilization is doing okay, while anything above 70% utilization is considered great.

### Question 62: According to the source, what does the number of parameters serve a...

According to the source, what does the number of parameters serve as a proxy for?

- [ ] A) The model’s learning capacity
- [ ] B) How much the model learned
- [ ] C) The training cost
- [ ] D) The number of tokens used

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** A

    **Explanation:** The source states that the number of parameters is a proxy for the model’s learning capacity.

### Question 63: According to the source, what does the number of tokens a model was...

According to the source, what does the number of tokens a model was trained on serve as a proxy for?

- [ ] A) The model’s learning capacity
- [ ] B) How much a model learned
- [ ] C) The training cost
- [ ] D) The number of FLOPs

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** The source states that the number of tokens a model was trained on is a proxy for how much a model learned.

### Question 64: According to the source, what does the number of FLOPs serve as a p...

According to the source, what does the number of FLOPs serve as a proxy for?

- [ ] A) The model’s learning capacity
- [ ] B) How much a model learned
- [ ] C) The training cost
- [ ] D) The number of parameters

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** C

    **Explanation:** The source states that the number of FLOPs is a proxy for the training cost.

### Question 65: According to the source, what did Anthropic discover in 2022 about...

According to the source, what did Anthropic discover in 2022 about more alignment training?

- [ ] A) It always makes models larger
- [ ] B) It leads to models that align less with human preference
- [ ] C) It eliminates political and religious views
- [ ] D) It improves memorization on small test sets

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** The source says Anthropic found that more alignment training counterintuitively leads to models that align less with human preference.

### Question 66: According to the Inverse Scaling Prize findings, larger language mo...

According to the Inverse Scaling Prize findings, larger language models are sometimes worse on which types of tasks?

- [ ] A) Tasks requiring memorization and tasks with strong priors
- [ ] B) Tasks requiring no training data and no priors
- [ ] C) Tasks involving only arithmetic and coding
- [ ] D) Tasks that have no small test sets

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** A

    **Explanation:** The source states that larger language models are sometimes worse on tasks that require memorization and tasks with strong priors.

### Question 67: Why did the Inverse Scaling Prize not award any second or first pri...

Why did the Inverse Scaling Prize not award any second or first prizes?

- [ ] A) They received only 11 submissions total
- [ ] B) No submitted task showed failures for a small test set
- [ ] C) The submitted tasks did not demonstrate failures in the real world
- [ ] D) The prize money was reserved for Anthropic researchers

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** C

    **Explanation:** The source says no second or first prizes were awarded because none of the submitted tasks demonstrated failures in the real world.

### Question 68: According to the Chinchilla scaling law, for compute-optimal traini...

According to the Chinchilla scaling law, for compute-optimal training, the number of training tokens should be approximately what multiple of the model size?

- [ ] A) 2 times the model size
- [ ] B) 5 times the model size
- [ ] C) 20 times the model size
- [ ] D) 100 times the model size

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** C

    **Explanation:** The Chinchilla paper found that compute-optimal training requires training tokens to be approximately 20 times the model size, so a 3B-parameter model needs about 60B training tokens.

### Question 69: Under the Chinchilla scaling law, how should model size and number...

Under the Chinchilla scaling law, how should model size and number of training tokens be scaled relative to each other?

- [ ] A) Tokens should be held constant while model size doubles
- [ ] B) Both should be scaled equally, so doubling model size also doubles training tokens
- [ ] C) Tokens should quadruple for every doubling of model size
- [ ] D) Model size should be held constant while tokens double

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** The source states that model size and training tokens should be scaled equally: for every doubling of the model size, the number of training tokens should also be doubled.

### Question 70: Why did the Llama authors opt for smaller models despite having a c...

Why did the Llama authors opt for smaller models despite having a compute budget that could have supported bigger, better-performing models?

- [ ] A) Smaller models are easier to work with and cheaper to run inference on, aiding wider adoption
- [ ] B) Smaller models always achieve higher training accuracy
- [ ] C) The Chinchilla scaling law forbids larger models
- [ ] D) Larger models cannot be trained on human-generated data

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** A

    **Explanation:** The text notes Llama chose smaller models because they are easier to work with and cheaper to run inference on, which helped gain wider adoption, even though larger models could have performed better.

### Question 71: According to the source, what is the relationship between the cost...

According to the source, what is the relationship between the cost of achieving a given model performance and the cost of improving performance?

- [ ] A) Both costs are decreasing at the same rate
- [ ] B) The cost for the same model performance is decreasing, but the cost for performance improvement remains high
- [ ] C) The cost for the same performance is increasing while improvement costs are falling
- [ ] D) Both costs remain constant over time

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** The text states that while the cost for the same model performance is decreasing (e.g., ImageNet 93% accuracy cost halved from 2019 to 2021), the cost for model performance improvement remains high.

### Question 72: According to the text, what does the performance of a model depend...

According to the text, what does the performance of a model depend heavily on?

- [ ] A) The values of its hyperparameters
- [ ] B) The number of authors on the paper
- [ ] C) The length of the model’s name
- [ ] D) The programming language used for deployment

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** A

    **Explanation:** The text states that model performance depends heavily on the values of its hyperparameters.

### Question 73: What is a common practice when working with small models?

What is a common practice when working with small models?

- [ ] A) Avoiding hyperparameter tuning entirely
- [ ] B) Training a model multiple times with different hyperparameter sets and picking the best-performing one
- [ ] C) Training only once with fixed hyperparameters
- [ ] D) Using large models instead of small models

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** The text says that with small models it is common to train multiple times with different hyperparameter sets and choose the best performer.

### Question 74: Why is training a large model multiple times with different hyperpa...

Why is training a large model multiple times with different hyperparameters rarely possible?

- [ ] A) Large models do not have hyperparameters
- [ ] B) Small models always perform better
- [ ] C) Training a large model once is resource-draining enough
- [ ] D) Large models cannot be evaluated

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** C

    **Explanation:** The text explains that training large models once is already resource-draining enough, so training them multiple times is rarely possible.

### Question 75: According to the text, what is the difference between a parameter a...

According to the text, what is the difference between a parameter and a hyperparameter?

- [ ] A) A parameter is set by users, while a hyperparameter is learned during training.
- [ ] B) A parameter can be learned during training, while a hyperparameter is set by users to configure the model or control learning.
- [ ] C) A parameter controls batch size, while a hyperparameter controls vocabulary size.
- [ ] D) A parameter is only used in small models, while a hyperparameter is only used in large models.

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** The text states that a parameter can be learned by the model during training, whereas a hyperparameter is set by users to configure the model and control how it learns.

### Question 76: What does scaling extrapolation, also called hyperparameter transfe...

What does scaling extrapolation, also called hyperparameter transferring, try to do?

- [ ] A) Predict what hyperparameters will give the best performance for large models by studying smaller models and extrapolating.
- [ ] B) Reduce the vocabulary size of a model before training.
- [ ] C) Remove emergent abilities from large models.
- [ ] D) Set all hyperparameters to the same value across model sizes.

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** A

    **Explanation:** The text describes scaling extrapolation as predicting, for large models, what hyperparameters will give the best performance by studying models of different sizes and extrapolating.

### Question 77: Why is scaling extrapolation difficult according to the text?

Why is scaling extrapolation difficult according to the text?

- [ ] A) Because models have no hyperparameters to study.
- [ ] B) Because hyperparameters do not interact with each other.
- [ ] C) Because there can be many hyperparameters and many combinations to study, and emergent abilities make extrapolation less accurate.
- [ ] D) Because hyperparameters can only be transferred from a 6.7B model to a 40M model.

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** C

    **Explanation:** The text says scaling extrapolation is difficult due to the sheer number of hyperparameters and their interactions, giving the example of 1,024 combinations for ten hyperparameters, and notes that emergent abilities make extrapolation less accurate.

### Question 78: What are the two visible bottlenecks for scaling foundation models...

What are the two visible bottlenecks for scaling foundation models mentioned in the text?

- [ ] A) Training data and electricity
- [ ] B) Compute and memory
- [ ] C) Bandwidth and storage
- [ ] D) Algorithms and hardware

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** A

    **Explanation:** The text states there are already two visible bottlenecks for scaling: training data and electricity.

### Question 79: According to the text, how many orders of magnitude did model sizes...

According to the text, how many orders of magnitude did model sizes increase between 2018 and 2021?

- [ ] A) One
- [ ] B) Two
- [ ] C) Three
- [ ] D) Four

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** C

    **Explanation:** The text says there was a three-orders-of-magnitude increase in model sizes between 2018 and 2021.

### Question 80: What concern is raised about internet data in relation to training...

What concern is raised about internet data in relation to training foundation models?

- [ ] A) It is growing faster than training dataset sizes
- [ ] B) We may run out of internet data in the next few years
- [ ] C) It is not useful for training language models
- [ ] D) It is always used with explicit consent

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** The text states there’s a realistic concern we’ll run out of internet data in the next few years.

### Question 81: How can people inject data they want into the training data of futu...

How can people inject data they want into the training data of future models, according to the text?

- [ ] A) By training their own models from scratch
- [ ] B) By publishing the text they want on the internet
- [ ] C) By using only private APIs
- [ ] D) By buying data from model creators

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** The text says they do this simply by publishing the text they want on the internet, hoping it will influence future models.

### Question 82: According to the source, what is an open research question regardin...

According to the source, what is an open research question regarding information a model has learned during training?

- [ ] A) How to make a model forget specific information it has learned during training
- [ ] B) How to make a model train only on proprietary data
- [ ] C) How to make a model consume less electricity during inference
- [ ] D) How to make a model refuse all requests involving deleted blog posts

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** A

    **Explanation:** The source states that an open research question is how to make a model forget specific information it has learned during training.

### Question 83: What did Igor Babuschkin say explained Grok’s refusal that mentione...

What did Igor Babuschkin say explained Grok’s refusal that mentioned OpenAI’s use case policy?

- [ ] A) Grok was trained only on proprietary medical records
- [ ] B) Grok was trained on web data, and “the web is full of ChatGPT outputs”
- [ ] C) Grok was trained on data from Reddit and Stack Overflow only
- [ ] D) Grok was trained on AI-generated data from X users exclusively

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** The source says Babuschkin responded that Grok was trained on web data and that “the web is full of ChatGPT outputs.”

### Question 84: According to Longpre et al. (2024), what happened to the popular pu...

According to Longpre et al. (2024), what happened to the popular public dataset C4 between 2023 and 2024 due to data restrictions?

- [ ] A) Over 28% of the most critical sources in C4 became fully restricted, and a full 45% of C4 is now restricted
- [ ] B) All of C4 became fully restricted from use
- [ ] C) C4 was replaced entirely by proprietary data
- [ ] D) C4 became restricted only because of electricity shortages

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** A

    **Explanation:** The source states that over 28% of the most critical sources in C4 became fully restricted and that a full 45% of C4 is now restricted.

### Question 85: According to the source, what bottleneck is described as less obvio...

According to the source, what bottleneck is described as less obvious but more pressing than data availability?

- [ ] A) Electricity
- [ ] B) Copyrighted books
- [ ] C) Model forgetting
- [ ] D) AI-generated data

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** A

    **Explanation:** The source says the other bottleneck, less obvious but more pressing, is electricity.

### Question 86: According to the source, what are two typical issues with a pre-tra...

According to the source, what are two typical issues with a pre-trained foundation model?

- [ ] A) It cannot generate text at all and requires no further training.
- [ ] B) Self-supervision optimizes it for text completion rather than conversations, and indiscriminately scraped internet data can make outputs racist, sexist, rude, or wrong.
- [ ] C) It has already been aligned with human preferences and only needs more pre-training.
- [ ] D) It is too small to be useful and must be scaled up before any post-training.

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** The source states pre-trained models are optimized for text completion, not conversations, and can produce harmful or incorrect outputs due to indiscriminate internet data.

### Question 87: What are the two general steps of post-training described in the so...

What are the two general steps of post-training described in the source?

- [ ] A) Architecture selection and scale selection
- [ ] B) Self-supervised pre-training and token-level optimization
- [ ] C) Supervised finetuning and preference finetuning
- [ ] D) Reading to acquire knowledge and prompting alone

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** C

    **Explanation:** The source says post-training generally consists of supervised finetuning on high-quality instruction data and preference finetuning to align responses with human preference.

### Question 88: Which preference finetuning technique does the source say is used b...

Which preference finetuning technique does the source say is used by Llama 3?

- [ ] A) RLHF
- [ ] B) RLAIF
- [ ] C) DPO
- [ ] D) Self-supervised pre-training

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** C

    **Explanation:** The source lists DPO (Direct Preference Optimization) as used by Llama 3, while RLHF is used by GPT-3.5 and Llama 2 and RLAIF is potentially used by Claude.

### Question 89: In supervised finetuning, what is demonstration data?

In supervised finetuning, what is demonstration data?

- [ ] A) Pairs of (prompt, response) that show examples of appropriate responses
- [ ] B) A set of reward scores used to rank model outputs
- [ ] C) A collection of multimodal tasks used during pretraining
- [ ] D) A heuristic filter applied to internet dialogues

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** A

    **Explanation:** The source says examples of appropriate responses follow the format (prompt, response) and are called demonstration data; this process is also called behavior cloning.

### Question 90: Why does the source say companies often use highly educated labeler...

Why does the source say companies often use highly educated labelers to generate demonstration data?

- [ ] A) Because labeling objects in an image might take only seconds
- [ ] B) Because demonstration data may contain complex prompts whose responses require critical thinking, information gathering, and judgment
- [ ] C) Because volunteer labelers are always representative of the human population
- [ ] D) Because DeepMind used simple heuristics to filter internet data

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** The source states that unlike traditional data labeling, demonstration data may contain complex prompts requiring critical thinking, information gathering, and judgment about appropriateness.

### Question 91: What does the source say about LAION’s volunteer-generated conversa...

What does the source say about LAION’s volunteer-generated conversation data?

- [ ] A) It consisted of 13,000 (prompt, response) pairs and cost $130,000
- [ ] B) It was used to finetune InstructGPT with labelers who were ~90% college graduates
- [ ] C) It lacked much control for biases, and in a self-reported survey 90% of volunteer labelers identified as male
- [ ] D) It was filtered using DeepMind’s simple heuristics for high-quality dialogues

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** C

    **Explanation:** The source says LAION mobilized volunteers to generate conversations, but since the data was volunteer-generated there wasn’t much control for biases, and 90% of volunteer labelers identified as male.

### Question 92: What is the goal of preference finetuning, according to the source?

What is the goal of preference finetuning, according to the source?

- [ ] A) To get AI models to behave according to human preference
- [ ] B) To eliminate the self-supervised pre-training step
- [ ] C) To train a model only on demonstration data
- [ ] D) To replace comparison data with synthetic data

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** A

    **Explanation:** The source states that the goal of preference finetuning is to get AI models to behave according to human preference.

### Question 93: What are the two parts of RLHF described in the source?

What are the two parts of RLHF described in the source?

- [ ] A) Train a reward model that scores the foundation model’s outputs, then optimize the foundation model to generate responses for which the reward model gives maximal scores
- [ ] B) Collect demonstration data, then train a model from scratch without pre-training
- [ ] C) Compare two responses, then train DPO to reduce complexity
- [ ] D) Generate synthetic data, then eliminate human preference labeling

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** A

    **Explanation:** The source says RLHF consists of training a reward model to score outputs and optimizing the foundation model to generate responses that maximize the reward model’s scores.

### Question 94: According to the source, why is asking labelers to compare two resp...

According to the source, why is asking labelers to compare two responses often easier than asking them to score each response directly?

- [ ] A) Direct scoring is pointwise evaluation, and scores can vary between labelers and even for the same labeler
- [ ] B) Comparison data requires no fact-checking at all
- [ ] C) Comparison data removes the need for a reward model
- [ ] D) Direct scoring cannot be used for foundation models

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** A

    **Explanation:** The source explains that direct pointwise scores vary, while comparing two responses and deciding which is better is an easier task.

### Question 95: Why did Meta switch from RLHF for Llama 2 to DPO for Llama 3, accor...

Why did Meta switch from RLHF for Llama 2 to DPO for Llama 3, according to the source?

- [ ] A) To reduce complexity
- [ ] B) To eliminate the need for human preferences
- [ ] C) To avoid using a foundation model
- [ ] D) To make comparison data unnecessary

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** A

    **Explanation:** The source states that Meta switched from RLHF for Llama 2 to DPO for Llama 3 to reduce complexity.

### Question 96: According to the text, what problem do both SFT and preference fine...

According to the text, what problem do both SFT and preference finetuning aim to address?

- [ ] A) The low quality of data used for pre-training
- [ ] B) The high computational cost of inference
- [ ] C) The lack of reward models in production
- [ ] D) The probabilistic nature of sampling

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** A

    **Explanation:** The text states that both SFT and preference finetuning are steps taken to address the problem created by the low quality of data used for pre-training.

### Question 97: Which companies mentioned in the text find that having the reward m...

Which companies mentioned in the text find that having the reward model alone is good enough, using a best of N strategy?

- [ ] A) Stitch Fix and Grab
- [ ] B) Google and Meta
- [ ] C) OpenAI and Anthropic
- [ ] D) Microsoft and Amazon

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** A

    **Explanation:** The text explicitly names Stitch Fix and Grab as companies that use the reward model alone and generate multiple outputs to pick the ones given high scores.

### Question 98: What does sampling make AI's outputs, according to the text?

What does sampling make AI's outputs, according to the text?

- [ ] A) Probabilistic
- [ ] B) Deterministic
- [ ] C) Binary
- [ ] D) Static

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** A

    **Explanation:** The text states that sampling makes AI's outputs probabilistic and that understanding this probabilistic nature is important for handling behaviors such as inconsistency.

### Question 99: Which set of variables is mentioned in the text as sampling variables?

Which set of variables is mentioned in the text as sampling variables?

- [ ] A) Temperature, top-k, and top-p
- [ ] B) Learning rate, batch size, and epochs
- [ ] C) Precision, recall, and F1
- [ ] D) Latency, throughput, and cost

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** A

    **Explanation:** The text explicitly lists temperature, top-k, and top-p as sampling variables.

### Question 100: What is greedy sampling?

What is greedy sampling?

- [ ] A) Picking the outcome with the highest probability
- [ ] B) Sampling the next token according to the probability distribution
- [ ] C) Always picking the most common word in the vocabulary
- [ ] D) Converting logits to probabilities

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** A

    **Explanation:** The text defines greedy sampling as "Always picking the most likely outcome."

### Question 101: Why does greedy sampling often create boring outputs for language m...

Why does greedy sampling often create boring outputs for language models?

- [ ] A) It always picks the most common words regardless of context
- [ ] B) It requires too much computation
- [ ] C) It cannot handle classification tasks
- [ ] D) It ignores the probability distribution entirely

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** A

    **Explanation:** The text states that greedy sampling creates boring outputs, imagining a model that "always responds with the most common words."

### Question 102: Which statement about logits is true according to the text?

Which statement about logits is true according to the text?

- [ ] A) Logits are probabilities that sum to one
- [ ] B) Logits can be negative and do not sum to one
- [ ] C) Logits are only used for classification models
- [ ] D) Logits are always positive and sum to one

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** The text says logits don't represent probabilities, don't sum up to one, and can even be negative.

### Question 103: According to the text, what effect does using a higher temperature...

According to the text, what effect does using a higher temperature have on token probabilities?

- [ ] A) It reduces the probabilities of common tokens and increases the probabilities of rarer tokens.
- [ ] B) It increases the probabilities of common tokens and reduces the probabilities of rarer tokens.
- [ ] C) It removes the need for a softmax layer when sampling.
- [ ] D) It forces the model to always pick the token with the highest logit.

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** A

    **Explanation:** The text states that a higher temperature reduces the probabilities of common tokens and increases the probabilities of rarer tokens, enabling more creative responses.

### Question 104: What is the primary purpose of top-k sampling as described in the t...

What is the primary purpose of top-k sampling as described in the text?

- [ ] A) To reduce computation workload without sacrificing too much of the model’s response diversity.
- [ ] B) To dynamically choose the smallest set of tokens whose cumulative probability exceeds a threshold.
- [ ] C) To increase the model’s creativity by raising the temperature.
- [ ] D) To guarantee that the model always selects the most obvious token.

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** A

    **Explanation:** The text says top-k sampling reduces computation workload by performing softmax over only the top-k logits, while not sacrificing too much response diversity.

### Question 105: How does top-p (nucleus) sampling differ from top-k sampling?

How does top-p (nucleus) sampling differ from top-k sampling?

- [ ] A) Top-p dynamically selects the smallest set of values whose cumulative probability exceeds p, while top-k uses a fixed number k.
- [ ] B) Top-p fixes the number of considered values to k, while top-k uses a cumulative probability threshold.
- [ ] C) Top-p always reduces softmax computation load, while top-k never does.
- [ ] D) Top-p sets the temperature to 0, while top-k sets it to 1.

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** A

    **Explanation:** The text explains that top-p allows dynamic selection based on cumulative probability, whereas top-k fixes the number of values considered to k.

### Question 106: What is test time compute in the source text?

What is test time compute in the source text?

- [ ] A) Generating only one response per query to reduce cost
- [ ] B) Generating multiple responses per query to increase the chance of good responses
- [ ] C) Training a model for more time before deployment
- [ ] D) Reducing the number of tokens in the model’s vocabulary

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** The text defines test time compute as generating multiple responses per query instead of only one, increasing the chance of good responses.

### Question 107: When selecting the best output by probability, why might you use av...

When selecting the best output by probability, why might you use average logprob instead of total logprob?

- [ ] A) Because logprob values are usually positive and must be averaged
- [ ] B) Because summing logprobs can bias selection toward short sequences
- [ ] C) Because average logprob is required to generate JSON
- [ ] D) Because reward models cannot score long sequences

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** The text says longer sequences are likely to have a lower total logprob, so average logprob avoids biasing toward short sequences.

### Question 108: In OpenAI’s experiment described in the text, sampling more outputs...

In OpenAI’s experiment described in the text, sampling more outputs led to better performance only up to what point?

- [ ] A) 32 outputs
- [ ] B) 100 outputs
- [ ] C) 400 outputs
- [ ] D) 10,000 outputs

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** C

    **Explanation:** The text states that in OpenAI’s experiment, performance improved up to 400 outputs and decreased beyond that point.

### Question 109: According to the source, structured outputs are crucial for which t...

According to the source, structured outputs are crucial for which two scenarios?

- [ ] A) Tasks requiring structured outputs and tasks whose outputs are used by downstream applications
- [ ] B) Tasks requiring image generation and tasks requiring audio transcription
- [ ] C) Tasks requiring model training and tasks requiring model deployment
- [ ] D) Tasks requiring natural language generation and tasks requiring human evaluation

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** A

    **Explanation:** The text states structured outputs are crucial for tasks requiring structured outputs, such as semantic parsing, and for tasks whose outputs are used by downstream applications.

### Question 110: What does an API’s JSON mode typically guarantee?

What does an API’s JSON mode typically guarantee?

- [ ] A) That the JSON content has the correct keys and values
- [ ] B) That the output is valid JSON, but not the content of the JSON objects
- [ ] C) That the output will never be truncated
- [ ] D) That the output will always match a specified regex

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** The source says JSON mode typically guarantees only that outputs are valid JSON, not the content of the JSON objects, and valid JSON can still be truncated.

### Question 111: In constrained sampling, what does the model do to generate a token?

In constrained sampling, what does the model do to generate a token?

- [ ] A) It samples only from tokens that meet the constraints after filtering the logit vector
- [ ] B) It asks a separate judge model to rewrite the output
- [ ] C) It finetunes the model architecture during generation
- [ ] D) It post-processes the final output by adding missing brackets

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** A

    **Explanation:** The text explains that constrained sampling filters the logit vector to keep only tokens meeting the constraints, then samples from those valid tokens.

### Question 112: Which approach does the source describe as the most effective and g...

Which approach does the source describe as the most effective and general way to get models to generate outputs in a desired format?

- [ ] A) Prompting
- [ ] B) Post-processing
- [ ] C) Constrained sampling
- [ ] D) Finetuning

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** D

    **Explanation:** The source states that finetuning on examples following the desirable format is the most effective and general approach, though simple finetuning does not guarantee the format.

### Question 113: According to the source, what does it mean that AI models are proba...

According to the source, what does it mean that AI models are probabilistic?

- [ ] A) They always produce the same answer for the same prompt.
- [ ] B) They can sample different responses for the same question, such as answering “Vietnamese cuisine” 70% of the time and “Italian cuisine” 30% of the time.
- [ ] C) They can only generate responses that are grounded in facts.
- [ ] D) They cannot generate creative outputs.

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** The source explains that probabilistic models sample responses, so the same question can produce different answers depending on probabilities.

### Question 114: Which pair correctly describes the two scenarios in which model inc...

Which pair correctly describes the two scenarios in which model inconsistency manifests, according to the source?

- [ ] A) Same input, same output; different input, same output.
- [ ] B) Same input, different outputs; slightly different input, drastically different outputs.
- [ ] C) Same input, factual output; different input, hallucinated output.
- [ ] D) Same input, cached output; different input, deterministic output.

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** The source states inconsistency appears as same input producing different outputs and slightly different input producing drastically different outputs.

### Question 115: What is the first hypothesis about why language models hallucinate,...

What is the first hypothesis about why language models hallucinate, originally expressed by Ortega et al. at DeepMind?

- [ ] A) A language model hallucinates because it cannot differentiate between the data it is given and the data it generates.
- [ ] B) A language model hallucinates only because its temperature is set too low.
- [ ] C) A language model hallucinates because it has no training data.
- [ ] D) A language model hallucinates because it always refuses to follow instructions.

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** A

    **Explanation:** The source says Ortega et al. hypothesized that a language model hallucinates because it cannot distinguish given data from its own generated data, calling it a form of self-delusion.

### Question 116: According to the text, which prompting-related approach seems to he...

According to the text, which prompting-related approach seems to help with hallucinations because fewer tokens are generated?

- [ ] A) Asking for concise responses
- [ ] B) Increasing the model size
- [ ] C) Using a transformer architecture
- [ ] D) Training on more data

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** A

    **Explanation:** The text says asking models for concise responses seems to help, since the fewer tokens a model has to generate, the less chance it has to make things up.

### Question 117: How do the self-delusion and mismatched internal knowledge hypothes...

How do the self-delusion and mismatched internal knowledge hypotheses differ in focus?

- [ ] A) Self-delusion focuses on self-supervision causing hallucinations, while mismatched internal knowledge focuses on supervision causing hallucinations.
- [ ] B) Self-delusion focuses on supervision causing hallucinations, while mismatched internal knowledge focuses on self-supervision causing hallucinations.
- [ ] C) Both focus only on detecting hallucinations in users.
- [ ] D) Both focus only on reducing output tokens.

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** A

    **Explanation:** The text states that the self-delusion hypothesis focuses on how self-supervision causes hallucinations, whereas the mismatched internal knowledge hypothesis focuses on how supervision causes hallucinations.

### Question 118: According to the summary, post-training consists of which two steps?

According to the summary, post-training consists of which two steps?

- [ ] A) Supervised finetuning and preference finetuning
- [ ] B) Pretraining and sampling
- [ ] C) Tokenization and evaluation
- [ ] D) Architecture design and scaling

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** A

    **Explanation:** The text says post-training consists of two steps: supervised finetuning and preference finetuning.

### Question 119: What does the chapter call the first step toward systematic AI engi...

What does the chapter call the first step toward systematic AI engineering?

- [ ] A) Establishing a solid evaluation pipeline
- [ ] B) Training a foundation model from scratch
- [ ] C) Eliminating the probabilistic nature of models
- [ ] D) Maximizing the number of output tokens

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** A

    **Explanation:** The text says the first step toward systematic AI engineering is to establish a solid evaluation pipeline to help detect failures and unexpected changes.
