# 3. Evaluation Methodology

---

## Why Evaluation Matters
- More AI use means more opportunities for catastrophic failure.
- Real harms: a chatbot encouraged suicide; lawyers filed AI-hallucinated false evidence.
- Air Canada paid damages after its chatbot gave a passenger false information.
- Without quality control of AI outputs, risk may outweigh benefits.

---

## Evaluation as the Core Hurdle
- Many teams find evaluation the biggest hurdle to shipping AI applications.
- For some applications, figuring out evaluation takes most of the development effort.
- Evaluation must be considered in the context of a whole system, not in isolation.
- Identify likely failure points first; you may need to redesign for visibility into failures.

---

## Challenges and Approach
- Evaluation is difficult, so many settle for word of mouth or eyeballing results.
- This adds risk and slows iteration; invest in systematic evaluation instead.
- Language model metrics like cross entropy and perplexity guide training and finetuning.
- Open-ended models are hard to evaluate; human evaluators remain necessary but slow and costly.
- Goal: automate evaluation, including exact and subjective methods.

---

## Why Foundation Model Evaluation Is Harder

- Smarter models are harder to evaluate; validating PhD-level answers or summaries needs expertise.
- Sophisticated tasks make evaluation far more time-consuming: fact-checking and reasoning replace surface judgments.
- Open-ended tasks undermine ground-truth comparison; many correct responses make comprehensive lists impossible.
- Most foundation models are black boxes, so you can only evaluate observed outputs.

---

## Benchmark Saturation and Expanding Scope

- Benchmarks should capture full model capabilities but saturate quickly as AI progresses.
- GLUE saturated in a year, prompting SuperGLUE; NaturalInstructions became Super-NaturalInstructions; MMLU was largely replaced by MMLU-Pro.
- General-purpose models expand evaluation scope: discovering new tasks, not just measuring known ones.
- Evaluation now explores AI's potential and limitations, including tasks beyond human capabilities.

---

## Growing Interest, Lagging Investment

- LLM evaluation papers grew exponentially in early 2023, from 2 to almost 35 per month.
- Over 50 of GitHub's top 1,000 AI repositories were dedicated to evaluation as of May 2024.
- Evaluation still lags: Balduzzi et al. note little systematic attention versus algorithm development.
- Inadequate investment yields inadequate infrastructure; many people just eyeball results with ad hoc prompts.

---

## Why Language Modeling Metrics Matter

- Many foundation models still use language models as main components.
- Language model performance often correlates with downstream application performance.
- A rough grasp of language modeling metrics helps understand downstream performance.
- Evaluation lags other AI engineering areas in open source tools.

---

## Core Language Modeling Metrics

- Most autoregressive language models are trained using cross entropy or perplexity.
- Bits-per-character (BPC) and bits-per-byte (BPB) are variations of cross entropy.
- Cross entropy, perplexity, BPC, and BPB are closely related.
- Given one value and necessary information, the other three can be computed.

---

## What These Metrics Capture

- Language models encode statistical information about how likely tokens are in context.
- More captured statistical information means better next-token prediction.
- A language model learns the distribution of its training data.
- Better learning of that distribution lowers training cross entropy.

---

## Entropy Measures Information per Token
- Entropy measures how much information, on average, a token carries.
- Higher entropy means each token carries more information and needs more bits.
- Example: two-token language has entropy 1; four-token language has entropy 2.
- Figure 3-4 shows two languages describing positions within a square.

---

## Entropy and Predictability
- Entropy measures how difficult it is to predict what comes next in a language.
- Lower entropy means a language is more predictable.
- Two-token language is easier to predict than four-token language.
- If you can perfectly predict what I say next, it carries no new information.

---

## Cross Entropy: Definition
- Goal: train a language model to learn the training data's distribution.
- Cross entropy measures how difficult it is for the model to predict what comes next.
- Lower difficulty means the model better captures the training data distribution.
- Cross entropy is computed on a dataset, not on a single example.

---

## Two Qualities Behind Cross Entropy
- The training data's predictability, measured by the training data's entropy.
- How the model's learned distribution diverges from the true training distribution.
- Entropy and cross entropy share the same mathematical notation, _H_.
- Let _P_ be the true distribution and _Q_ the distribution learned by the model.

---

## The Cross Entropy Formula
- Training data entropy is written as _H_(_P_).
- Divergence of _Q_ with respect to _P_ is measured by KL divergence: DKL(_P_ || _Q_).
- Cross entropy combines both: _H_(_P_, _Q_) = _H_(_P_) + DKL(_P_ || _Q_).
- So cross entropy equals data entropy plus the model's divergence from the truth.

---

## Cross Entropy and Model Training
- Cross entropy is asymmetric: H(P,Q) differs from H(Q,P).
- Language models minimize cross entropy with respect to training data.
- Perfect learning makes model cross entropy equal training data entropy.
- Then KL divergence of Q with respect to P is zero.

---

## Bits-per-Character (BPC)
- Entropy and cross entropy measured in bits; cross entropy of 6 bits means 6 bits per token.
- Bits per token not comparable across models due to different tokenization methods.
- BPC = bits per token divided by average characters per token.
- Character encoding schemes complicate BPC; ASCII encodes each character using 7 bits.

---

## Bits-per-byte and compression
- UTF-8 characters can use 8–32 bits; bits-per-byte (BPB) standardizes model representation.
- BPB equals BPC divided by bits per character as a fraction of a byte.
- Example: BPC 3 and 7-bit characters give BPB = 3 / (7/8) = 3.43.
- BPB 3.43 represents each original byte in 3.43 bits, compressing text below half size.

---

## Perplexity definitions
- Perplexity is the exponential of entropy and cross entropy; often shortened to PPL.
- For true distribution P: PPL(P) = 2^H(P).
- For model distribution Q: PPL(P,Q) = 2^H(P,Q).
- Cross entropy measures prediction difficulty; perplexity measures uncertainty among possible next tokens.

---

## Example and units
- A perfect model for 4 position tokens has cross entropy 2 bits and perplexity 4.
- Perplexity 4 means choosing among 2^2 = 4 possible options.
- Bit uses base 2; nat uses base e, so PPL(P,Q) = e^H(P,Q).
- TensorFlow and PyTorch use nat; many report perplexity due to bit/nat confusion.

---

## Perplexity: What Drives It
- The more uncertainty a model has predicting the next token, the higher the perplexity.
- More structured data—e.g., HTML—gives lower expected perplexity than everyday text.
- The bigger the vocabulary, the higher the perplexity; character-based is lower than word-based.
- The longer the context length, the lower the perplexity.

---

## Interpreting Perplexity Values
- Good values depend on the data and how perplexity is computed, including context length.
- Perplexity as low as 3 is not uncommon; a perplexity of 3 means 1-in-3 odds per token.
- The more accurately a model predicts a text, the lower these metrics are.
- Larger GPT-2 models consistently give lower perplexity across datasets and are more powerful.

---

## Use Cases and Caveats
- Perplexity is a good proxy for capabilities: bad next-token prediction predicts bad downstream performance.
- Low perplexity on benchmark data can signal contamination; high perplexity can gate data deduplication.
- Perplexity is highest for unpredictable or gibberish text, so it can detect abnormal texts.
- Warning: perplexity may not proxy post-trained models (SFT, RLHF), which often raise perplexity; quantization can shift it unpredictably.

---

## Perplexity as a Proxy Metric

- Perplexity and related metrics reveal the underlying language model's performance
- They act as a proxy for performance on downstream tasks
- The rest of the chapter measures downstream task performance directly
- A model's perplexity for a text measures how hard that text is to predict

---

## Computing a Text's Perplexity

- Given model X and token sequence [x1, x2, ..., xn], perplexity is defined over that sequence
- It uses P(xi | x1, ..., xi−1): the probability X assigns to token xi given previous tokens
- The formula takes the inverse n-th root of the sequence probability
- Computing it requires access to next-token probabilities or logprobs

---

## Access Limits and Exact Evaluation

- Not all commercial models expose their logprobs, as discussed in Chapter 2
- Without logprobs, perplexity cannot be computed directly
- Evaluation should distinguish exact evaluation from subjective evaluation
- Exact evaluation produces (source text ends here)

---

## Functional Correctness: Definition
- Functional correctness evaluates whether a system performs its intended functionality.
- Example: does a generated website meet your requirements, or does a reservation succeed?
- It is the ultimate metric: it measures whether your application does what it's intended to do.
- But it isn't always straightforward to measure, and its measurement can't be easily automated.

---

## Execution Accuracy and pass@k
- Code generation allows automated functional correctness measurement, sometimes called execution accuracy.
- Generated code is run in an interpreter to check validity and correct output, as in unit tests.
- For each problem, k code samples are generated; a problem is solved if any sample passes all its test cases.
- The pass@k score is the fraction of solved problems—e.g., solving 5 of 10 gives pass@3 = 50%.

---

## Benchmarks and Measurable Objectives
- HumanEval and MBPP use functional correctness; text-to-SQL benchmarks like Spider, BIRD-SQL, and WikiSQL also rely on it.
- Each benchmark problem comes with test cases: a scenario and its expected output.
- More samples give more chances to solve, so pass@1 is expected to be lower than pass@10.
- Measurable-objective tasks like game bots (Tetris score) or energy-optimizing scheduling also suit functional correctness.

---

## Reference-Based Evaluation Overview
- Reference data follows (input, reference responses) format; inputs may have multiple reference responses
- Reference responses are called ground truths or canonical responses; metrics needing them are reference-based
- Reference data is typically human-generated (gold standard) but increasingly AI-generated, then human-reviewed
- Four similarity approaches: evaluator judgment, exact match, lexical similarity, semantic similarity

---

## Exact Match and Lexical Similarity
- Exact match is binary; suits short answers like math, trivia, and common-knowledge queries
- Containment variation accepts outputs containing the reference, but can accept factually wrong answers
- Lexical similarity uses token overlap, fuzzy matching (edit distance), and n-gram similarity
- Common metrics: BLEU, ROUGE, METEOR++, TER, CIDEr; drawbacks include incomplete or wrong references

---

## Semantic Similarity
- Semantic similarity compares meaning by transforming texts into embeddings, then computing similarity
- Cosine similarity scores range from 1 (identical embeddings) to –1 (opposite embeddings)
- Metrics include BERTScore (BERT embeddings) and MoverScore (mixture of algorithms)
- Needs less comprehensive references, but depends on embedding quality and requires nontrivial compute

---

## What Is an Embedding?
- An embedding is a numerical representation that aims to capture the meaning of the original data.
- An embedding is a vector; vector sizes typically range from 100 to 10,000 elements.
- Specialized embedding models include BERT, CLIP, and Sentence Transformers; proprietary models are offered as APIs.
- Many models, including GPTs and Llamas, also generate embeddings, though quality may be lower.

---

## Judging Embedding Quality
- A good embedding algorithm places more-similar texts closer together, measured by cosine similarity or related metrics.
- "the cat sits on a mat" should be closer to "the dog plays on the grass" than to "AI research is super fun".
- Quality can also be evaluated by utility for tasks: classification, topic modeling, recommender systems, and RAG.
- MTEB, Massive Text Embedding Benchmark, measures embedding quality on multiple tasks.

---

## Joint Embeddings Across Modalities
- CLIP maps text and images into a joint embedding space, trained on (image, text) pairs.
- Text and image encoders project embeddings into a joint space, aligning an image with its corresponding text.
- ULIP aims to unify text, images, and 3D point clouds; ImageBind spans six modalities.
- Any data can be embedded: Criteo and Coveo embed products; Pinterest embeds images, graphs, queries, and users.

---

## Multimodal Embedding Spaces
- A multimodal embedding space represents data from different modalities jointly.
- In text–image space, an image of a man fishing is closer to “a fisherman” than “fashion show.”
- Joint embeddings let different modalities be compared and combined.
- This enables text-based image search by finding images closest to a text.

---

## AI as a Judge
- Open-ended response evaluation challenges lead many teams to human evaluation.
- Using AI to evaluate AI is called AI as a judge or LLM as a judge.
- An AI model that evaluates other AI models is an AI judge.
- AI as a judge became practical around 2020 with GPT-3 and is common in production.

---

## Why AI as a Judge?

- AI judges are fast, easy to use, and relatively cheap compared to human evaluators.
- They can work without reference data, suiting production environments lacking reference data.
- AI models can judge outputs on any criteria: correctness, repetitiveness, toxicity, wholesomeness, hallucinations, and more.
- As aggregations of the masses, AI models can make judgments representative of the masses.

---

## AI Judges vs. Human Evaluators

- Zheng et al. (2023) found GPT-4–human agreement reached 85% on MT-Bench, above human–human agreement (81%).
- AlpacaEval authors (Dubois et al., 2023) found near-perfect (0.98) correlation with LMSYS's human-evaluated Chat Arena leaderboard.
- AI judges can explain their decisions, which is useful when auditing evaluation results.
- Even when not as good as human judgments, AI judgments may be good enough to guide development.

---

## Flexibility and Practical Use

- AI's flexibility makes it useful for a wide range of applications.
- For some applications, AI judging is the only automatic evaluation option.
- With the right prompt for the right model, you can get reasonably good judgments on a wide range of topics.
- AI judgments can't always be trusted, just as people's opinions can't always be trusted.

---

## Three Ways to Use AI as a Judge
- Evaluate a response by itself, given the original question, using a 1–5 score.
- Compare a generated response to a reference answer; output True or False.
- Compare two generated responses and pick the better one; output A or B.
- Comparison produces preference data for alignment, test-time compute, and ranking.

---

## Prompting an AI Judge
- A judge prompt should clearly state the task the model must perform.
- Specify detailed criteria, e.g., whether the answer addresses the question per ground truth.
- Choose a scoring system: classification, discrete numbers, or continuous values.
- Models handle text better than numbers; classification beats numerical scoring.
- Include examples of each score and why a response receives it.

---

## Criteria and Scoring Caveats
- Judges can evaluate any custom criteria, such as role consistency or image trustworthiness.
- Built-in criteria vary by tool: Azure AI Studio, MLflow, LangChain, Ragas.
- Criteria aren't standardized; the same "relevance" score differs across tools.
- For numerical scoring, discrete beats continuous, and narrower ranges (1–5) work better.

---

## AI Judges as Systems
- An AI judge is a system: a model plus a prompt.
- Changing model, prompt, or sampling parameters creates a different judge.
- Teams hesitate because AI evaluating AI seems tautological and probabilistic.
- Some treat AI judges as fallback when no other evaluation exists, especially production.

---

## Inconsistency and Ambiguous Criteria
- AI judges are probabilistic; same judge and input can output different scores.
- Evaluation examples can improve consistency but may not improve accuracy.
- Longer prompts raise inference costs; one experiment quadrupled GPT-4 spending.
- Faithfulness criteria differ across MLflow, Ragas, LlamaIndex in prompts and scoring.

---

## Costs, Latency, and Bias
- Using GPT-4 to generate and evaluate doubles API calls and approximately doubles costs.
- Three evaluation prompts can increase API calls four times; weaker judges and spot-checking reduce costs.
- Production judges add latency; reduced risk may conflict with strict latency requirements.
- AI judges show self-bias and first-position bias; humans show recency bias.

---

## Choosing a Judge
- Stronger judge: better judgments, can guide weaker models; but cost and latency favor weaker generators.
- Strongest model has no eligible judge; need alternative evaluation to determine which model is strongest.
- Self-evaluation (self-critique) risks self-bias but helps sanity checks and nudges models to revise responses.
- Weaker judges may work since judging is easier than generating; stronger models correlate better with human preference (Zheng et al.).

---

## Specialized Judges
- Small specialized judges trained on specific criteria and scoring systems can outperform larger general-purpose judges.
- Reward model scores (prompt, response) quality; Google's Cappy outputs 0-1 with 360 million parameters.
- Reference-based judge compares to references: BLEURT outputs similarity; Prometheus outputs quality score 1-5.
- Preference model takes (prompt, response 1, response 2) and predicts which is better; examples include PandaLM and JudgeLM.

---

## Judge Biases and Limits
- Verbosity bias: GPT-4 and Claude-1 prefer longer responses (~100 words) with factual errors over shorter correct ones (~50 words).
- Saito et al.: large length differences almost always favor longer response; GPT-4 less prone than GPT-3.5.
- AI judges share privacy and IP limitations; proprietary judges require sending data to providers.
- Supplement AI judges with exact evaluation methods and/or human evaluation.

---

## Comparative vs. Pointwise Evaluation

- Pointwise: evaluate each model independently, then rank by scores.
- Comparative: evaluate models against each other and rank from comparison results.
- Comparative is easier when quality is subjective—easier to pick the better song than score it.
- First used in AI by Anthropic in 2021; powers LMSYS Chatbot Arena leaderboard.

---

## How Comparative Evaluation Works

- Each comparison is a *match*; evaluators (human or AI) pick a winner, often allowing ties.
- Win rate of A over B = percentage of matches where A wins.
- A *rating algorithm* computes scores from comparative signals, then ranks models.
- Algorithms like Elo, Bradley–Terry, and TrueSkill adapt from sports and games.

---

## Caveats and Distinctions

- Not all questions should be answered by preference—many require correctness instead.
- Preference voting only works if voters are knowledgeable in the subject.
- Asking users to pick can cause frustration when they don't know the answer.
- Comparative evaluation differs from A/B testing: users see multiple outputs at once, not one.

---

## Limitations and Cost
- Human preference alone isn't enough when swapping model A for B.
- Cost is another important factor in model comparison.
- Without expected performance boost, cost-benefit analysis is difficult.
- If B costs twice A, comparative evaluation can't show if boost is worth cost.

---

## Why Comparative Evaluation Has a Future
- Comparing two outputs is easier than assigning concrete scores.
- Stronger models may surpass humans, making concrete scoring impossible.
- Humans may still detect differences, so comparative evaluation may be the only option.
- Llama 2 paper: humans gave valuable feedback comparing answers beyond annotator ability.

---

## Capturing Human Preference
- Comparative evaluation aims to capture human preference, the quality we care about.
- It reduces pressure to constantly create more benchmarks.
- Benchmarks can become useless when model performance achieves perfect.
- Comparative evaluation remains valuable despite its limitations.

---

## Why Evaluation Matters
- Stronger AI models raise potential for catastrophic failures, making evaluation more important.
- Open-ended powerful models are challenging to evaluate; many teams turn to human evaluation.
- Humans in the loop help sanity checks and are sometimes essential, but chapter focuses on automatic evaluation.
- Foundation models are harder to evaluate than traditional ML models; evaluation investment lags development.

---

## Automatic Evaluation Approaches
- Language modeling metrics include perplexity and cross entropy; interpretation matters for evaluation and data processing.
- Open-ended responses can be evaluated by functional correctness, similarity scores, and AI as a judge.
- Functional correctness and similarity are exact; AI as a judge is subjective.
- AI judges change with iteration, are unreliable over time, and should be supplemented with exact or human evaluation.

---

## Comparative Evaluation and Takeaways
- Models can be ranked by independent scores or by comparative signals: which of two models is better.
- Comparative evaluation is hard to game and trusted; it won't saturate while newer, stronger models appear.
- It provides discriminating signals and complements offline benchmarks and online A/B testing.
- Preference signals are expensive; preference models are specialized AI judges predicting preferred responses.

## Practice Questions

### Question 1: According to the source text, what do many teams quickly realize is...

According to the source text, what do many teams quickly realize is the biggest hurdle to bringing AI applications to reality?

- [ ] A) Collecting enough training data
- [ ] B) Evaluation
- [ ] C) Hiring human annotators
- [ ] D) Deploying models to production

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** The text states that as teams rush to adopt AI, many quickly realize that the biggest hurdle to bringing AI applications to reality is evaluation.

### Question 2: What does the source text say about relying on word of mouth or eye...

What does the source text say about relying on word of mouth or eyeballing results for evaluation?

- [ ] A) It is a reliable way to compare foundation models
- [ ] B) It creates even more risk and slows application iteration
- [ ] C) It is the recommended alternative to systematic evaluation
- [ ] D) It is necessary because evaluation is easy

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** The text says that because evaluation is difficult, many people settle for word of mouth or eyeballing results, which creates even more risk and slows application iteration.

### Question 3: What does this chapter focus on, according to the source text?

What does this chapter focus on, according to the source text?

- [ ] A) How to select models for an application and build an evaluation pipeline
- [ ] B) Different evaluation methods for open-ended models, how these methods work, and their limitations
- [ ] C) Only human evaluation methods and annotation costs
- [ ] D) How to train language models from scratch

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** The text says this chapter covers different evaluation methods used to evaluate open-ended models, how these methods work, and their limitations, while the next chapter focuses on model selection and building an evaluation pipeline.

### Question 4: According to the source, why does greater model intelligence make e...

According to the source, why does greater model intelligence make evaluation harder?

- [ ] A) Intelligent models always produce longer outputs
- [ ] B) Evaluators may need to fact-check, reason, and incorporate domain expertise rather than judge only by how a response sounds
- [ ] C) Intelligent models cannot be evaluated with benchmarks
- [ ] D) Intelligent models require no human evaluation

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** The text says that for sophisticated tasks, evaluation becomes more time-consuming and you can no longer evaluate a response based only on how it sounds; you may need to fact-check, reason, and use domain expertise.

### Question 5: What does the open-ended nature of foundation models undermine?

What does the open-ended nature of foundation models undermine?

- [ ] A) The traditional approach of evaluating a model against ground truths
- [ ] B) The use of classification models
- [ ] C) The need for public benchmarks
- [ ] D) The ability to observe model outputs

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** A

    **Explanation:** The source states that open-ended tasks have so many possible correct responses that it is impossible to curate a comprehensive list of correct outputs to compare against, undermining evaluation against ground truths.

### Question 6: According to the text, why are most foundation models treated as bl...

According to the text, why are most foundation models treated as black boxes?

- [ ] A) Because they are always trained without data
- [ ] B) Because model providers may not expose details, or application developers may lack expertise to understand them
- [ ] C) Because benchmarks are saturated too quickly
- [ ] D) Because AI judges cannot evaluate them

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** The text says this happens either because model providers choose not to expose models’ details or because application developers lack the expertise to understand them.

### Question 7: Which example does the source use to illustrate that foundation mod...

Which example does the source use to illustrate that foundation model benchmarks are becoming saturated fast?

- [ ] A) GLUE became saturated in just a year, leading to SuperGLUE
- [ ] B) MMLU was replaced by GLUE in 2018
- [ ] C) NaturalInstructions was replaced by MMLU-Pro in 2024
- [ ] D) SuperGLUE was replaced by GLUE in 2019

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** A

    **Explanation:** The text states that GLUE came out in 2018 and became saturated in just a year, necessitating the introduction of SuperGLUE in 2019.

### Question 8: According to the source, why can a rough understanding of language...

According to the source, why can a rough understanding of language modeling metrics help with downstream performance?

- [ ] A) Because evaluation tools are the most common open source AI tools
- [ ] B) Because the language model component’s performance tends to correlate with a foundation model’s downstream application performance
- [ ] C) Because language modeling metrics have changed significantly since 1951
- [ ] D) Because downstream applications no longer use foundation models

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** The source states that for many foundation models, the language model component’s performance tends to be well correlated to downstream application performance.

### Question 9: Which two metrics does the source describe as variations of cross e...

Which two metrics does the source describe as variations of cross entropy?

- [ ] A) Accuracy and F1
- [ ] B) Bits-per-character (BPC) and bits-per-byte (BPB)
- [ ] C) Perplexity and accuracy
- [ ] D) Recall and precision

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** The source says BPC and BPB are both variations of cross entropy.

### Question 10: What relationship does the source give among cross entropy, perplex...

What relationship does the source give among cross entropy, perplexity, BPC, and BPB?

- [ ] A) They are unrelated and cannot be converted
- [ ] B) If you know one value, you can compute the other three given the necessary information
- [ ] C) They apply only to text tokens
- [ ] D) They are used only for downstream evaluation

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** The source states that all four metrics are closely related and one can be computed from another when the necessary information is available.

### Question 11: According to the source, these language modeling metrics can be use...

According to the source, these language modeling metrics can be used for what kinds of models?

- [ ] A) Only models that generate text
- [ ] B) Only foundation models
- [ ] C) Any model that generates sequences of tokens, including non-text tokens
- [ ] D) Only models trained with supervised learning

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** C

    **Explanation:** The source says that although it calls them language modeling metrics, they can be used for any model that generates sequences of tokens, including non-text tokens.

### Question 12: According to the source, what does entropy measure?

According to the source, what does entropy measure?

- [ ] A) How many tokens a language model can generate per second
- [ ] B) How much information, on average, a token carries
- [ ] C) How closely a model’s training data matches production data
- [ ] D) How many parameters a language model contains

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** The source states that entropy measures how much information, on average, a token carries.

### Question 13: In the square-position example, what is the entropy of a language w...

In the square-position example, what is the entropy of a language with only two tokens, where each token tells whether the position is upper or lower?

- [ ] A) 0
- [ ] B) 1
- [ ] C) 2
- [ ] D) 4

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** The source says that with only two tokens, one bit is sufficient to represent them, so the entropy of this language is 1.

### Question 14: In the square-position example, why does the language with four tok...

In the square-position example, why does the language with four tokens have higher entropy than the language with two tokens?

- [ ] A) Each token carries more information but requires more bits to represent
- [ ] B) Each token carries less information and requires fewer bits to represent
- [ ] C) It has fewer possible tokens, making it easier to predict
- [ ] D) It uses no bits to represent each token

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** A

    **Explanation:** The source says the four-token language has higher entropy because each token carries more information, but each token requires more bits to represent.

### Question 15: According to the source, what does lower entropy imply about a lang...

According to the source, what does lower entropy imply about a language?

- [ ] A) It is more difficult to predict what comes next
- [ ] B) It is more predictable
- [ ] C) It always requires more bits per token
- [ ] D) It cannot be used to describe positions in a square

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** The source states that the lower a language’s entropy, the more predictable that language.

### Question 16: What does a language model’s cross entropy on a dataset measure?

What does a language model’s cross entropy on a dataset measure?

- [ ] A) How quickly the model trains on the dataset
- [ ] B) How difficult it is for the model to predict what comes next in the dataset
- [ ] C) How large the dataset is compared with the model
- [ ] D) How many parameters the model has learned

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** The source states that a language model’s cross entropy on a dataset measures how difficult it is for the language model to predict what comes next in this dataset.

### Question 17: A model’s cross entropy on the training data depends on which two q...

A model’s cross entropy on the training data depends on which two qualities?

- [ ] A) The training data’s entropy and how the model’s distribution diverges from the true training distribution
- [ ] B) The model size and the number of training epochs
- [ ] C) The learning rate and the batch size
- [ ] D) The dataset size and the vocabulary size

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** A

    **Explanation:** The source lists the training data’s predictability, measured by its entropy, and how the distribution captured by the language model diverges from the true distribution of the training data.

### Question 18: Using P as the true distribution of the training data and Q as the...

Using P as the true distribution of the training data and Q as the distribution learned by the language model, what is the model’s cross entropy with respect to the training data?

- [ ] A) H(P, Q) = H(P) − DKL(P || Q)
- [ ] B) H(P, Q) = DKL(P || Q) − H(P)
- [ ] C) H(P, Q) = H(P) + DKL(P || Q)
- [ ] D) H(P, Q) = H(Q) + DKL(Q || P)

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** C

    **Explanation:** The source gives the model’s cross entropy as H(P, Q) = H(P) + DKL(P || Q).

### Question 19: Which statement about cross entropy is correct according to the text?

Which statement about cross entropy is correct according to the text?

- [ ] A) Cross entropy is symmetric, so H(P, Q) always equals H(Q, P).
- [ ] B) Cross entropy is not symmetric, so H(P, Q) can differ from H(Q, P).
- [ ] C) Cross entropy is always zero when P and Q differ.
- [ ] D) Cross entropy is the same as KL divergence in all cases.

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** The text states that cross entropy isn’t symmetric and that H(P, Q) is different from H(Q, P).

### Question 20: If a language model’s cross entropy is 6 bits per token and each to...

If a language model’s cross entropy is 6 bits per token and each token consists of 2 characters on average, what is the bits-per-character (BPC)?

- [ ] A) 2
- [ ] B) 6
- [ ] C) 3
- [ ] D) 12

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** C

    **Explanation:** The text says BPC is calculated as bits per token divided by average characters per token, so 6/2 = 3.

### Question 21: What complication with bits-per-character (BPC) does the text mention?

What complication with bits-per-character (BPC) does the text mention?

- [ ] A) BPC cannot be calculated from bits per token.
- [ ] B) BPC only applies to models that use words as tokens.
- [ ] C) BPC is always higher than bits per token.
- [ ] D) Different character encoding schemes can use different numbers of bits per character.

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** D

    **Explanation:** The text notes that BPC is complicated by different character encoding schemes, giving ASCII as an example where each character is encoded using 7 bits.

### Question 22: If the bits-per-character (BPC) is 3 and each character is 7 bits,...

If the bits-per-character (BPC) is 3 and each character is 7 bits, or ⅞ of a byte, what is the bits-per-byte (BPB)?

- [ ] A) 3 / (7/8) = 3.43
- [ ] B) 3 × (7/8) = 2.625
- [ ] C) 3 + (7/8) = 3.875
- [ ] D) 3 − (7/8) = 2.125

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** A

    **Explanation:** The source states that BPB is calculated as 3 / (⅞) = 3.43 when BPC is 3 and each character is 7 bits.

### Question 23: If a language model has a BPB of 3.43, what does this imply about c...

If a language model has a BPB of 3.43, what does this imply about compressing the original training text?

- [ ] A) It can compress the text to exactly its original size.
- [ ] B) It can compress the text to less than half the text’s original size.
- [ ] C) It cannot compress the text at all.
- [ ] D) It can compress the text to more than double its original size.

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** The source says a BPB of 3.43 means the model can represent each original byte using 3.43 bits, compressing the original training text to less than half its original size.

### Question 24: What does perplexity measure about a language model when predicting...

What does perplexity measure about a language model when predicting the next token?

- [ ] A) The amount of uncertainty it has
- [ ] B) The exact number of training tokens
- [ ] C) The number of bytes in the original text
- [ ] D) The speed of the model in tokens per second

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** A

    **Explanation:** The source states that perplexity measures the amount of uncertainty a model has when predicting the next token, while cross entropy measures how difficult prediction is.

### Question 25: In popular ML frameworks such as TensorFlow and PyTorch, which unit...

In popular ML frameworks such as TensorFlow and PyTorch, which unit is used for entropy and cross entropy, making perplexity equal to e^H(P,Q)?

- [ ] A) Byte
- [ ] B) Bit
- [ ] C) Nat
- [ ] D) Token

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** C

    **Explanation:** The source says TensorFlow and PyTorch use nat, the base of natural logarithm, as the unit, so perplexity is the exponential of e: PPL(P,Q) = e^H(P,Q).

### Question 26: According to the text, which factor tends to lower a model’s expect...

According to the text, which factor tends to lower a model’s expected perplexity?

- [ ] A) A larger vocabulary
- [ ] B) A shorter context length
- [ ] C) More structured data
- [ ] D) Post-training with SFT and RLHF

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** C

    **Explanation:** The text says more structured data is more predictable, so expected perplexity should be lower; larger vocabulary and shorter context tend to raise perplexity.

### Question 27: What does the text say about perplexity as a proxy for models post-...

What does the text say about perplexity as a proxy for models post-trained with techniques like SFT and RLHF?

- [ ] A) It is always a reliable proxy because post-training lowers perplexity.
- [ ] B) It might not be a great proxy because post-training can increase perplexity as task completion improves.
- [ ] C) It is only useful for HTML code.
- [ ] D) It cannot be computed after post-training.

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** The warning states that post-training teaches task completion and a model might get worse at next-token prediction, so perplexity typically increases after post-training.

### Question 28: How can perplexity be used to detect data contamination?

How can perplexity be used to detect data contamination?

- [ ] A) Low perplexity on a benchmark’s data suggests the benchmark was likely included in training data, making performance less trustworthy.
- [ ] B) High perplexity on a benchmark’s data proves the benchmark was included in training data.
- [ ] C) Perplexity cannot be used for contamination detection.
- [ ] D) Low perplexity always means the text is abnormal.

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** A

    **Explanation:** The text says perplexity is lowest for texts the model has seen and memorized, so low perplexity on benchmark data can indicate contamination.

### Question 29: What does a model’s perplexity with respect to a text measure?

What does a model’s perplexity with respect to a text measure?

- [ ] A) How difficult it is for the model to predict that text
- [ ] B) How many parameters the model has
- [ ] C) How long the model takes to train
- [ ] D) How fluent the model’s generated text sounds

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** A

    **Explanation:** The source states that a model’s perplexity with respect to a text measures how difficult it is for the model to predict that text.

### Question 30: To compute a text’s perplexity, what must you have access to?

To compute a text’s perplexity, what must you have access to?

- [ ] A) The model’s probabilities or logprobs for each next token
- [ ] B) The model’s training dataset
- [ ] C) The model’s hardware configuration
- [ ] D) The model’s number of layers

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** A

    **Explanation:** The source says that to compute perplexity, you need access to the probabilities (or logprobs) the language model assigns to each next token.

### Question 31: According to the text, what limitation affects computing perplexity...

According to the text, what limitation affects computing perplexity for some commercial models?

- [ ] A) Not all commercial models expose their models’ logprobs
- [ ] B) Commercial models cannot assign probabilities to tokens
- [ ] C) Commercial models do not use token sequences
- [ ] D) Commercial models always have zero perplexity

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** A

    **Explanation:** The source notes that not all commercial models expose their models’ logprobs, which are needed to compute perplexity.

### Question 32: The text says it is important to differentiate between which two ty...

The text says it is important to differentiate between which two types of evaluation?

- [ ] A) Exact and subjective evaluation
- [ ] B) Training and testing evaluation
- [ ] C) Perplexity and accuracy evaluation
- [ ] D) Online and offline evaluation

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** A

    **Explanation:** The source explicitly states that when evaluating models’ performance, it’s important to differentiate between exact and subjective evaluation.

### Question 33: What does functional correctness evaluation measure?

What does functional correctness evaluation measure?

- [ ] A) Whether a system's output is grammatically correct
- [ ] B) Whether a system performs the intended functionality
- [ ] C) Whether a system's response is graded subjectively
- [ ] D) Whether a system uses the largest foundation model

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** The source defines functional correctness as evaluating a system based on whether it performs the intended functionality.

### Question 34: In code generation, what is functional correctness sometimes called?

In code generation, what is functional correctness sometimes called?

- [ ] A) Similarity accuracy
- [ ] B) Intent classification
- [ ] C) Execution accuracy
- [ ] D) Essay grading

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** C

    **Explanation:** The source states that functional correctness in coding is sometimes execution accuracy, where generated code is run to check validity and correct output.

### Question 35: In pass@k evaluation, when is a problem considered solved by a model?

In pass@k evaluation, when is a problem considered solved by a model?

- [ ] A) When all k generated code samples are identical
- [ ] B) When any of the k generated code samples pass all of that problem's test cases
- [ ] C) When the model's first code sample is graded by a human
- [ ] D) When the model generates fewer than k code samples

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** The source says a model solves a problem if any of the k code samples it generated pass all of that problem's test cases, and pass@k is the fraction of solved problems.

### Question 36: Each example in reference data follows which format?

Each example in reference data follows which format?

- [ ] A) (input, reference responses)
- [ ] B) (prompt, model weights)
- [ ] C) (embedding, cosine score)
- [ ] D) (edit distance, n-gram)

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** A

    **Explanation:** The source states that each example in reference data follows the format (input, reference responses), and an input can have multiple reference responses.

### Question 37: Which statement about exact match is correct?

Which statement about exact match is correct?

- [ ] A) It gives a sliding-scale score between 0 and 1.
- [ ] B) It is binary and works for short, exact responses such as simple math or trivia.
- [ ] C) It is the best method for long open-ended translations.
- [ ] D) It compares meaning using embeddings.

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** The source says exact matching scores are binary, and exact match works for tasks expecting short, exact responses such as simple math problems and trivia-style questions.

### Question 38: What is a drawback of lexical similarity mentioned in the source?

What is a drawback of lexical similarity mentioned in the source?

- [ ] A) It never requires reference responses.
- [ ] B) It always correlates with functional correctness.
- [ ] C) A good response can get a low score if the reference set lacks a similar response.
- [ ] D) It can only be used for image captioning.

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** C

    **Explanation:** The source notes that lexical similarity requires curating a comprehensive set of reference responses, so a good response can receive a low similarity score if the reference set does not contain a similar response.

### Question 39: How is semantic similarity between two embeddings commonly computed?

How is semantic similarity between two embeddings commonly computed?

- [ ] A) By counting edit operations
- [ ] B) By exact string matching
- [ ] C) By cosine similarity
- [ ] D) By n-gram overlap

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** C

    **Explanation:** The source says semantic similarity, also called embedding similarity, can be computed using metrics such as cosine similarity, where identical embeddings score 1 and opposite embeddings score –1.

### Question 40: According to the source, what is an embedding?

According to the source, what is an embedding?

- [ ] A) A numerical representation that aims to capture the meaning of the original data
- [ ] B) A benchmark for measuring embedding quality on multiple tasks
- [ ] C) A transformer layer used only for text generation
- [ ] D) A proprietary API for creating image captions

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** A

    **Explanation:** The source defines an embedding as “a numerical representation that aims to capture the meaning of the original data.”

### Question 41: At a high level, when is an embedding algorithm considered good?

At a high level, when is an embedding algorithm considered good?

- [ ] A) When its embedding vectors always have exactly 768 elements
- [ ] B) When more-similar texts have closer embeddings, measured by cosine similarity or related metrics
- [ ] C) When it uses only open source embedding models
- [ ] D) When its embeddings look identical to the original text

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** The source says an embedding algorithm is considered good if more-similar texts have closer embeddings, measured by cosine similarity or related metrics.

### Question 42: Which model was one of the first major models that could map text a...

Which model was one of the first major models that could map text and images into a joint embedding space?

- [ ] A) BERT
- [ ] B) Sentence Transformers
- [ ] C) CLIP
- [ ] D) ULIP

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** C

    **Explanation:** The source states that CLIP was one of the first major models that could map data of different modalities, text and images, into a joint embedding space.

### Question 43: According to the source, why are AI judges useful compared to human...

According to the source, why are AI judges useful compared to human evaluators?

- [ ] A) They are always more accurate than human evaluators.
- [ ] B) They are fast, easy to use, relatively cheap, and can work without reference data.
- [ ] C) They require reference data in production environments.
- [ ] D) They cannot evaluate toxicity or hallucinations.

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** The source states AI judges are fast, easy to use, and relatively cheap compared to human evaluators, and can work without reference data.

### Question 44: In 2023, what did Zheng et al. find on the MT-Bench evaluation benc...

In 2023, what did Zheng et al. find on the MT-Bench evaluation benchmark?

- [ ] A) Agreement between GPT-4 and humans reached 85%, higher than agreement among humans at 81%.
- [ ] B) Agreement between GPT-4 and humans reached 81%, lower than agreement among humans at 85%.
- [ ] C) AI judges had a near-perfect 0.98 correlation with the Chat Arena leaderboard.
- [ ] D) Human evaluators agreed with each other 98% of the time.

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** A

    **Explanation:** The source says Zheng et al. found that on MT-Bench, agreement between GPT-4 and humans reached 85%, even higher than the 81% agreement among humans.

### Question 45: What did the AlpacaEval authors (Dubois et al., 2023) find about th...

What did the AlpacaEval authors (Dubois et al., 2023) find about their AI judges?

- [ ] A) They had no correlation with human-evaluated leaderboards.
- [ ] B) They had a near-perfect 0.98 correlation with LMSYS’s Chat Arena leaderboard.
- [ ] C) They reached 85% agreement with humans on MT-Bench.
- [ ] D) They could not explain their decisions for auditing.

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** The source states the AlpacaEval authors found their AI judges have a near-perfect 0.98 correlation with LMSYS’s Chat Arena leaderboard, which is evaluated by humans.

### Question 46: Why can AI judges be especially useful when auditing evaluation res...

Why can AI judges be especially useful when auditing evaluation results?

- [ ] A) They can only provide a score without any explanation.
- [ ] B) They can evaluate a response and also explain their decision.
- [ ] C) They eliminate the need for any human judgment.
- [ ] D) They always match human evaluators perfectly.

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** The source notes that AI can evaluate a response and explain its decision, which is especially useful when you want to audit evaluation results.

### Question 47: According to the source, which of the following is one of the three...

According to the source, which of the following is one of the three naive example approaches for using AI as a judge?

- [ ] A) Fine-tuning the judge model on human labels
- [ ] B) Comparing a generated response to a reference response
- [ ] C) Replacing all human evaluation with automated scoring
- [ ] D) Training a separate classifier for each criterion

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** The source lists evaluating a response by itself, comparing it to reference data, and comparing it to another response as three example approaches.

### Question 48: What does the source say about AI-as-a-judge criteria such as “rele...

What does the source say about AI-as-a-judge criteria such as “relevance” across tools?

- [ ] A) They are standardized across all AI tools
- [ ] B) They depend only on the user’s original question
- [ ] C) They are not standardized and can differ based on the judge’s underlying model and prompt
- [ ] D) They are always identical to human-designed similarity measurements

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** C

    **Explanation:** The source states that AI judge criteria aren’t standardized, and Azure AI Studio’s relevance scores might differ from MLflow’s depending on the judge’s model and prompt.

### Question 49: According to the source’s tip on scoring systems for AI judges, whi...

According to the source’s tip on scoring systems for AI judges, which statement is most accurate?

- [ ] A) AI judges generally work better with continuous numerical scoring than with classification
- [ ] B) AI judges generally work better with classification than with numerical scoring systems
- [ ] C) Wider discrete scoring ranges tend to improve AI judge performance
- [ ] D) Language models are generally better with numbers than with text

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** The source reports that AI judges work better with classification than numerical scoring, and that discrete scoring seems to work better than continuous scoring.

### Question 50: According to the source, why is inconsistency a limitation of AI ju...

According to the source, why is inconsistency a limitation of AI judges?

- [ ] A) AI judges cannot evaluate more than one criterion at a time.
- [ ] B) The same judge, on the same input, can output different scores if prompted differently or run twice.
- [ ] C) AI judges always produce lower scores than human evaluators.
- [ ] D) AI judges require human-written ground truth answers for every input.

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** The source states that AI judges are probabilistic, so the same judge can output different scores with different prompts or across repeated runs.

### Question 51: What does the source say about the criterion “faithfulness” across...

What does the source say about the criterion “faithfulness” across MLflow, Ragas, and LlamaIndex?

- [ ] A) All three tools use the same instructions and the same 1–5 scoring system.
- [ ] B) Only MLflow has a built-in faithfulness criterion.
- [ ] C) Their instructions and scoring systems are all different, so their faithfulness scores won’t be comparable.
- [ ] D) Ragas and LlamaIndex both output YES or NO for faithfulness.

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** C

    **Explanation:** The source says MLflow uses 1–5, Ragas uses 0 and 1, and LlamaIndex asks for YES and NO, making their scores non-comparable.

### Question 52: According to the source, what happens to API costs if you use GPT-4...

According to the source, what happens to API costs if you use GPT-4 to both generate and evaluate responses?

- [ ] A) API costs stay the same because evaluation calls are free.
- [ ] B) API costs are approximately doubled because you do twice as many GPT-4 calls.
- [ ] C) API costs are reduced because AI judges replace human evaluators.
- [ ] D) API costs increase only when using weaker models as judges.

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** The source states that using GPT-4 to both generate and evaluate responses means twice as many GPT-4 calls, approximately doubling API costs.

### Question 53: What is self-bias in AI judges, as described in the source?

What is self-bias in AI judges, as described in the source?

- [ ] A) A judge favors the first answer in a pairwise comparison.
- [ ] B) A judge favors responses generated by other models over its own.
- [ ] C) A judge favors its own responses over responses generated by other models.
- [ ] D) A judge consistently makes the same mistakes when given more examples.

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** C

    **Explanation:** The source defines self-bias as a model favoring its own responses, citing GPT-4 and Claude-v1 favoring themselves in Zheng et al.’s 2023 experiment.

### Question 54: According to the text, what is one benefit of using a stronger mode...

According to the text, what is one benefit of using a stronger model as a judge for responses generated by a weaker model?

- [ ] A) It removes the need for any exact evaluation methods
- [ ] B) It can make better judgments and help guide weaker models to generate better responses
- [ ] C) It is always cheaper and faster than using a weaker model
- [ ] D) It guarantees the judge has no privacy or IP limitations

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** The text says stronger models can make better judgments and can help improve weaker models by guiding them to generate better responses.

### Question 55: What does the text say self-evaluation or self-critique can be usef...

What does the text say self-evaluation or self-critique can be useful for?

- [ ] A) Eliminating self-bias completely
- [ ] B) Replacing human evaluation in all cases
- [ ] C) Sanity checks and nudging a model to revise and improve its responses
- [ ] D) Determining which model is the strongest without any alternative evaluation method

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** C

    **Explanation:** The text states that self-evaluation can be great for sanity checks and can nudge a model to revise and improve its responses.

### Question 56: Which example of a reference-based judge is given in the text, and...

Which example of a reference-based judge is given in the text, and what does it output?

- [ ] A) Cappy, which outputs a score between 0 and 1 indicating correctness
- [ ] B) PandaLM, which outputs which of two responses is better and explains its rationale
- [ ] C) BLEURT, which takes a candidate response and reference response and outputs a similarity score
- [ ] D) Prometheus, which outputs which of two responses is preferred by users

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** C

    **Explanation:** The text describes BLEURT as a reference-based judge that takes a candidate response and reference response pair and outputs a similarity score.

### Question 57: What argument does the text mention for why a weaker model might be...

What argument does the text mention for why a weaker model might be able to judge a stronger model?

- [ ] A) Judging is an easier task than generating, so weaker models should be able to judge stronger models’ outputs
- [ ] B) Weaker models are always better correlated with human preference
- [ ] C) Weaker models have no biases when used as judges
- [ ] D) Weaker models are the only models that can perform self-evaluation

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** A

    **Explanation:** The text says some argue that judging is easier than generating, comparing having an opinion about a song with writing a song.

### Question 58: According to the text, what is the difference between pointwise eva...

According to the text, what is the difference between pointwise evaluation and comparative evaluation?

- [ ] A) Pointwise evaluation compares models against each other, while comparative evaluation scores each model independently.
- [ ] B) Pointwise evaluation evaluates each model independently and ranks by scores, while comparative evaluation evaluates models against each other and computes a ranking from comparison results.
- [ ] C) Pointwise evaluation is only used for subjective quality, while comparative evaluation is only used for correctness.
- [ ] D) Pointwise evaluation requires pairwise matches, while comparative evaluation requires A/B testing.

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** The text defines pointwise evaluation as evaluating each model independently and ranking by scores, and comparative evaluation as evaluating models against each other and computing a ranking from comparison results.

### Question 59: Why does the text warn that not all questions should be answered by...

Why does the text warn that not all questions should be answered by preference?

- [ ] A) Preference-based voting is always more accurate than correctness-based evaluation.
- [ ] B) Preference voting can be used only when there are exactly two models.
- [ ] C) Some questions should be answered by correctness instead, and preference-based voting can lead to wrong signals and misaligned behaviors if used to train a model.
- [ ] D) Preference voting is identical to A/B testing and therefore cannot be used in production.

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** C

    **Explanation:** The text says many questions should be answered by correctness, and preference-based voting can produce wrong signals that may lead to misaligned behaviors if used for training.

### Question 60: According to the text, when is a ranking considered correct?

According to the text, when is a ranking considered correct?

- [ ] A) When the higher-ranked model always has more matches than the lower-ranked model.
- [ ] B) When the ranking is produced by Elo rather than Bradley–Terry.
- [ ] C) When, for any model pair, the higher-ranked model is more likely to win in a match against the lower-ranked model.
- [ ] D) When every model has the same win rate against every other model.

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** C

    **Explanation:** The text states that a ranking is correct if, for any model pair, the higher-ranked model is more likely to win against the lower-ranked model.

### Question 61: Why is comparative evaluation described as data-intensive and subje...

Why is comparative evaluation described as data-intensive and subject to scalability bottlenecks?

- [ ] A) Because computing scores to rank models is harder than designing metrics
- [ ] B) Because the number of model pairs to compare grows quadratically with the number of models
- [ ] C) Because pointwise evaluation requires direct comparisons between every model pair
- [ ] D) Because new models never need to be compared against existing models

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** The text states comparative evaluation is data-intensive and the number of model pairs grows quadratically with the number of models.

### Question 62: What assumption do ranking algorithms typically make, and why is it...

What assumption do ranking algorithms typically make, and why is it questionable for AI models?

- [ ] A) They assume all evaluators use the same prompts, which is guaranteed in crowdsourced evaluation
- [ ] B) They assume transitivity, but human preference may not be transitive and different model pairs may be evaluated by different evaluators and prompts
- [ ] C) They assume comparative evaluation directly measures absolute performance
- [ ] D) They assume private models can always be evaluated on public leaderboards

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** Ranking algorithms typically assume transitivity, but the text notes it is unclear whether this holds for AI models because human preference is not necessarily transitive and evaluations can vary by evaluator and prompt.

### Question 63: What limitation of comparative evaluation is illustrated by the exa...

What limitation of comparative evaluation is illustrated by the example of model B winning against model A 51% of the time?

- [ ] A) Comparative evaluation cannot rank models when win rates are close
- [ ] B) Comparative evaluation tells which model is better but not how good a model is or whether it is good enough for a use case
- [ ] C) Comparative evaluation always proves both models are good
- [ ] D) Comparative evaluation removes the need for any other form of evaluation

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** The text says comparative evaluation tells us which model is better, but not how good a model is or whether it is good enough; a 51% win rate does not clearly convert to absolute performance.

### Question 64: Why might comparative evaluation alone be insufficient when decidin...

Why might comparative evaluation alone be insufficient when deciding whether to swap model A for model B?

- [ ] A) It cannot compare two outputs.
- [ ] B) It does not account for human preference.
- [ ] C) It cannot determine whether B’s performance boost is worth the added cost if B costs twice as much as A.
- [ ] D) It always shows that B is better than A.

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** C

    **Explanation:** The text says comparative evaluation is not sufficient to determine if the performance boost from B will be worth the added cost when B costs twice as much as A.

### Question 65: According to the text, why might comparative evaluation remain the...

According to the text, why might comparative evaluation remain the only option as models become stronger and surpass human performance?

- [ ] A) Human evaluators may be unable to give concrete scores but may still detect differences when comparing two answers.
- [ ] B) Benchmarks will become more accurate than human evaluators.
- [ ] C) Concrete scoring becomes easier as models surpass humans.
- [ ] D) Cost–benefit analysis will no longer matter.

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** A

    **Explanation:** The text says it might become impossible for humans to give concrete scores, but they might still detect differences, so comparative evaluation could remain the only option.

### Question 66: What benefit of comparative evaluation is mentioned in relation to...

What benefit of comparative evaluation is mentioned in relation to benchmarks?

- [ ] A) It eliminates the need for human preference.
- [ ] B) It reduces the pressure to constantly create more benchmarks to catch up with AI’s expanding capabilities.
- [ ] C) It guarantees perfect model performance.
- [ ] D) It makes cost–benefit analysis unnecessary.

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** The text states that comparative evaluation aims to capture human preference and reduces the pressure to constantly create more benchmarks as AI capabilities expand.

### Question 67: According to the text, why is comparative evaluation considered rel...

According to the text, why is comparative evaluation considered relatively hard to game?

- [ ] A) It requires training on reference data.
- [ ] B) There is no easy way to cheat, such as training your model on reference data.
- [ ] C) It relies entirely on human judges.
- [ ] D) It uses exact metrics that cannot be manipulated.

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** The text states comparative evaluation is hard to game because there’s no easy way to cheat, like training your model on reference data.

### Question 68: How does the text characterize AI as a judge evaluation?

How does the text characterize AI as a judge evaluation?

- [ ] A) It is exact and objective.
- [ ] B) It is subjective and highly dependent on the judge.
- [ ] C) It is always more reliable than human evaluation.
- [ ] D) It is unaffected by iteration.

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** The text says AI as a judge evaluation is subjective, and subjective metrics are highly dependent on the judge.

### Question 69: What limitation does the text mention about using AI judges as benc...

What limitation does the text mention about using AI judges as benchmarks to track an application’s changes over time?

- [ ] A) They are too expensive to run frequently.
- [ ] B) Their judgments change as they are iterated upon, making them unreliable.
- [ ] C) They are always biased toward longer responses.
- [ ] D) They cannot evaluate open-ended responses.

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** The text explains that AI judges should be iterated upon, meaning their judgments change, which makes them unreliable as benchmarks to track an application’s changes over time.

### Question 70: What are preference models, according to the text?

What are preference models, according to the text?

- [ ] A) Specialized AI judges that predict which response users prefer.
- [ ] B) Exact evaluation metrics for functional correctness.
- [ ] C) A type of language modeling metric like perplexity.
- [ ] D) A method for online A/B testing only.

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** A

    **Explanation:** The text defines preference models as specialized AI judges that predict which response users prefer.
