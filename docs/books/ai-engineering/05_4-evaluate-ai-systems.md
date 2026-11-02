# 4. Evaluate AI Systems

---

## Evaluating AI in Your Application Context

- A model is only useful if it works for its intended purposes
- Evaluate models in the context of your application, not in isolation
- Chapter 3 covers automatic evaluation approaches; this chapter applies them
- The chapter has three parts: criteria, model selection, and hosting choices

---

## Part 1: Defining Evaluation Criteria

- Start by deciding which criteria matter for your application
- Define how each criterion is calculated and measured
- Example: factual consistency — how is AI making up facts detected?
- Domain-specific capabilities like math, science, reasoning, and summarization need measurement

---

## Parts 2 and 3: Selecting and Hosting Models

- Many foundation models exist; choosing the right one can feel overwhelming
- Thousands of benchmarks evaluate models along different criteria
- Questions: can benchmarks be trusted, which to use, and how to read leaderboards?
- Decide whether to host your own model or use a model API — a recurring question

---

## Why Evaluation Criteria Matter
- Deployed but unevaluable applications are worse than never-deployed ones, according to conference responses.
- Such applications cost to maintain, and taking them down may cost even more.
- Questionable ROI is common when developers lack visibility into usage and accuracy.
- Examples include a used-car valuation model and customer support chatbots.

---

## Evaluation-Driven Development
- Define evaluation criteria before building, inspired by test-driven development.
- Sensible business decisions rely on returns on investment, not hype.
- Applications should demonstrate value before deployment.
- Common production applications tend to have clear evaluation criteria.

---

## Common Criteria and Caveat
- Recommender success measured by engagement or purchase-through rates.
- Fraud detection success measured by money saved from prevented frauds.
- Generated code evaluated by functional correctness; classification tasks easier than open-ended.
- Focusing only on measurable outcomes is like looking for the lost key under the lamppost.

---

## Evaluation Criteria and Domain Capability
- Evaluation is the biggest bottleneck to AI adoption; reliable evaluation pipelines unlock new applications.
- Start with application-specific criteria: domain-specific capability, generation capability, instruction-following capability, and cost and latency.
- Domain-specific capability means the model can perform required domain tasks, such as writing code or translating Latin.
- It is constrained by model configuration and training data; models lacking required capabilities won’t work.

---

## Evaluating Domain-Specific Capability
- Use public or private domain-specific benchmarks covering code, math, science, reasoning, legal knowledge, tool use, and more.
- Coding capabilities are commonly evaluated with exact evaluation, typically functional correctness.
- Efficiency can be exactly evaluated via runtime or memory; BIRD-SQL compares generated query runtime with ground truth.
- Code readability lacks an obvious exact method, so subjective evaluation such as AI judges may be needed.

---

## Multiple-Choice Benchmarks: Strengths and Limits
- Non-coding capabilities often use close-ended tasks like multiple-choice questions, which are easier to verify and reproduce.
- In April 2024, 75% of lm-evaluation-harness tasks were multiple-choice, including MMLU, AGIEval, and ARC-C.
- MCQ metrics include accuracy and point systems; classification also uses F1, precision, and recall.
- MCQs are prompt-sensitive and test classification, not generation; they suit knowledge and reasoning better.

---

## Generation Capability: From NLG to Foundation Models

- NLG studies open-ended text generation; early tasks included translation, summarization, and paraphrasing.
- Early metrics: fluency (grammatical, natural-sounding) and coherence (logical structure).
- Task-specific metrics: faithfulness for translation, relevance for summarization.
- Faithfulness and relevance were later repurposed, with modifications, for foundation models.

---

## Why Older Metrics Matter Less

- Early generated texts had grammatical errors and awkward sentences, so fluency and coherence were key.
- As models improved, AI text became nearly indistinguishable from human text.
- Fluency and coherence remain useful for weaker models, creative writing, and low-resource languages.
- These can be measured with an AI judge or with perplexity.

---

## New Capabilities, New Metrics

- The most pressing new issue is undesired hallucinations—desirable for creative tasks, not factual ones.
- Factual consistency is a metric many application developers want to measure.
- Safety is an umbrella term for all types of toxicity and biases.
- Other qualities developers may track include controversiality, friendliness, positivity, creativity, and conciseness.

---

## Factual Consistency

- Factual inconsistency can have catastrophic consequences.
- Many techniques have been and will be developed to detect and measure it.
- This chapter covers only the broad strokes.

---

## Two Verification Settings

- A model’s output can be verified against explicitly provided facts, or context.
- It can also be verified against open knowledge.

---

## Local vs. Global Consistency
- Local factual consistency evaluates an output against a given context.
- An output is consistent if the context supports it.
- Global factual consistency evaluates an output against open knowledge.
- Local suits summarization, customer support, and business analysis; global suits chatbots, fact-checking, market research.

---

## Verifying Facts Is Hard
- Factual consistency is easier to verify against explicit facts and reliable sources.
- Without context, you must search reliable sources, derive facts, then validate the statement.
- Determining what the facts are is often the hardest part of verification.
- Trusted sources and internet misinformation complicate this; absence-of-evidence fallacy can make “no link” seem factual.

---

## How Models Judge Evidence
- Wan et al. (2024) found models rely heavily on website relevance to the query.
- Models largely ignore stylistic features humans find important, such as scientific references or neutral tone.

---

## Designing Hallucination Benchmarks
- Analyze model outputs to find query types most likely to trigger hallucinations.
- Focus benchmark queries on those high-risk types rather than uniformly sampling.
- Niche knowledge is riskier: the VMO was hallucinated more than the IMO.
- Queries about things that don’t exist are riskier: “What did X say about Y?” when X never did.

---

## AI as a Judge for Factual Consistency
- Most straightforward approach: ask an AI judge to check factual consistency against provided or retrieved context.
- Liu et al. (2023) and Luo et al. (2023): GPT-3.5 and GPT-4 outperform previous factual-consistency methods.
- TruthfulQA’s finetuned GPT-judge predicts human truthfulness judgments with 90–96% accuracy.
- Liu et al.’s prompt asks whether the summary contains facts unsupported by the source text.

---

## TruthfulQA and Advanced Verification
- TruthfulQA measures how models mimic human falsehoods; GPT-judge was finetuned on it.
- More sophisticated AI-as-judge techniques: self-verification and knowledge-augmented verification.

---

## Self-Verification & Knowledge-Augmented Verification

- SelfCheckGPT assumes an output is likely hallucinated if new responses disagree with it.
- It generates N new responses and measures consistency, but requires many costly AI queries.
- SAFE (Google DeepMind) verifies responses using search engine results in four steps.
- Steps: decompose into statements, make self-contained, propose queries, check consistency.

---

## Textual Entailment for Factual Consistency

- Textual entailment determines the relationship between a premise (context) and hypothesis (output).
- Entailment: hypothesis inferred from premise; Contradiction: contradicts premise; Neutral: undetermined.
- Entailment implies factual consistency; contradiction implies inconsistency; neutral is undetermined.
- Specialized scorers (e.g., DeBERTa-v3-base-mnli-feveranli) treat this as a classification task.

---

## TruthfulQA Benchmark

- TruthfulQA has 817 questions humans might answer incorrectly due to false beliefs or misconceptions.
- Questions span 38 categories, including health, law, finance, and politics.
- It includes GPT-judge, finetuned to evaluate factual consistency with a reference response.
- Human expert baseline is 94%; factual consistency is crucial for evaluating RAG systems.

---

## Safety: Harm Categories
- Unsafe outputs span profanity, explicit content, harmful tutorials, and self-destructive encouragement.
- Hate speech covers racist, sexist, homophobic, and other discriminatory language.
- Violence includes threats and graphic detail; stereotypes assign traits by gender or group.
- Ideological bias can make models generate only content supporting one political or religious view.

---

## Measuring Ideological Bias
- Studies show models can inherit political biases from their training.
- GPT-4 is described as more left-wing and libertarian-leaning.
- Meta's Llama is described as more authoritarian.
- Figure 4-3 compares political and economic leanings of foundation models.

---

## Detecting Harmful Outputs
- General-purpose AI judges (GPTs, Claude, Gemini) can detect many harmful outputs if prompted properly.
- Model providers build moderation tools, some exposed for external use.
- Specialized toxicity detectors are smaller, faster, and cheaper than general-purpose judges.
- Examples: Facebook's hate speech model, Skolkovo's toxicity classifier, Perspective API, plus language-specific models.

---

## Instruction-Following Capability

- Measures how well a model follows the instructions you give it, regardless of instruction quality.
- Poor instruction-following breaks structured outputs like JSON, regex, or A/B/C classifications.
- It goes beyond structure: e.g., using only words of at most four characters.
- Hard to isolate from domain-specific or generation capability; a *lục bát* failure is ambiguous.

---

## Benchmarks: IFEval and INFOBench

- IFEval (Google) checks whether outputs follow an expected format, using 25 automatically verifiable instruction types.
- Score is the fraction of instructions followed correctly out of all instructions.
- INFOBench (Qin et al.) also covers content constraints, linguistic guidelines, and style rules.
- INFOBench verifies via yes/no criteria answered by humans or AI judges; GPT-4 was reasonably reliable.

---

## Roleplaying Evaluation

- Roleplaying is the eighth most common use case in LMSYS's one-million-conversation dataset.
- It serves entertainment (games, companions) and prompt engineering purposes.
- Benchmarks: RoleLLM (similarity scores plus AI judges) and CharacterEval (human annotators, reward model).
- Evaluate both style and knowledge; AI as a judge is the easiest automatic approach.

---

## Balancing Quality, Latency, and Cost
- A model with high-quality outputs that is too slow or expensive is not useful.
- Many companies opt for lower-quality models if they offer better cost and latency.
- Pareto optimization: be clear about which objectives you can and can't compromise on.
- If latency is non-negotiable, filter out models failing requirements, then pick the best.

---

## Latency: Metrics and Control
- Latency metrics include time to first token, time per token, time between tokens, time per query.
- Latency depends on the model, each prompt, and sampling variables.
- Autoregressive models generate token by token; more tokens means higher total latency.
- Distinguish must-have from nice-to-have latency; high latency is often an annoyance, not a deal breaker.

---

## Cost, Scale, and Model Selection
- API pricing is per token; more input and output tokens cost more.
- Self-hosting cost is compute; many choose the largest model that fits their machines.
- API cost per token changes little with scale; self-hosted cost per token can drop.
- Reevaluate API versus self-hosting at different scales.

---

## Model Selection: Fit Over Best

- You don't care which model is best overall; you care which is best for your application.
- Define application criteria first, then evaluate models against those criteria.
- Model selection recurs throughout development, across different adaptation techniques.
- Criteria turn abstract quality goals into concrete, comparable model evaluations.

---

## Iterative Model Selection

- Prompt engineering may start with the strongest model to test feasibility.
- Then work backward to check whether smaller models suffice.
- With finetuning, start small to test code, then scale up.
- Move toward the biggest model that fits your hardware constraints, such as one GPU.

---

## Criteria, Metrics, and Benchmarks

- Each criterion maps to a metric, a benchmark, and a hard requirement.
- Example: factual consistency uses an internal GPT metric on an internal hallucination dataset.
- Hard requirement: above 0.8; ideal: above 0.9.
- Use these thresholds to judge candidate models.

---

## Model Selection: Two Core Steps
- Identify the best achievable performance for each technique
- Map models along cost–performance axes
- Choose the model giving best performance for your budget
- Actual selection is more nuanced than these two steps suggest

---

## Hard vs. Soft Attributes
- Hard attributes are impossible or impractical to change: licenses, training data, model size, privacy, control
- Hard attributes can significantly reduce the pool of potential models
- Soft attributes can be improved: accuracy, toxicity, factual consistency
- Latency is soft if you can optimize the model; hard if hosted by someone else

---

## Four-Step Evaluation Workflow
- Filter out models whose hard attributes don't work for you
- Use public benchmarks and leaderboards to narrow promising models
- Run experiments with your own evaluation pipeline to find the best model
- Continually monitor in production to detect failure and collect feedback

---

## Model Build Versus Buy

- The choice is between using model APIs and self-hosting models.
- Table 4-4 lays out the pros and cons of each option.
- Cons are marked in italics in the table.

---

## Open Source Versus Proprietary

- The gap between open source and proprietary models is decreasing.
- Enterprises cite clear reasons for caring about open source models.

---

## Trust Your Own Evaluation

- If existing evaluations can't be trusted, build your own evaluation pipeline.
- Choose prompts and metrics you can trust.
- Self-designed evaluation keeps the build-versus-buy decision grounded in evidence.

---

## Model Build Versus Buy
- Most companies won’t build foundation models from scratch.
- The key choice is commercial model APIs versus self-hosting an open source model.
- This decision can significantly reduce the candidate model pool.
- “Open source model” is contentious; downloadable access is often sufficient.

---

## Open Source, Open Weight, Open Model
- Some argue a model is open only if its training data is public.
- Open data allows retraining from scratch with architecture, process, or data changes.
- Open data helps understand the model and supports auditing for compromised or illegal data.
- “Open weight” means no open data; “open model” means open data is included.

---

## Open Source and Open Weight

- This book uses *open source* for all models whose weights are public
- Training data availability and licenses are not required by this definition
- As of writing, the vast majority of open source models are open weight only
- Developers may hide training data to avoid public scrutiny and lawsuits

---

## Licenses Are Fragmented

- Foundation models worsened an already confusing licensing landscape (MIT, Apache 2.0, GPL, BSD, Creative Commons)
- Many models ship under their own unique licenses
- Meta released Llama 2 and Llama 3 under separate Community License Agreements
- Gemma and Mistral-7B were released under Apache 2.0; BigCode under BigCode Open RAIL-M v1

---

## Questions to Ask About a License

- Does the license allow commercial use? Meta's first Llama was noncommercial
- If commercial use is allowed, what restrictions apply?
- Llama-2 and Llama-3 require a special Meta license above 700 million monthly active users
- Does it allow outputs to train other models? Llama licenses still don't; distillation is a key use case

---

## Inference Services and Model APIs
- An inference service hosts the model, runs user queries, and returns responses.
- The model API is the interface users interact with; other APIs cover finetuning and evaluation.
- Developers can open source a model, serve it via API, or both.
- Providers typically open source weaker models and keep their best behind paywalls.

---

## Where Model APIs Come From
- APIs are offered by model providers, cloud providers, and third-party API providers.
- The same model can be available through different APIs with different features, constraints, and pricing.
- Performance may differ across APIs due to different optimization techniques; test thoroughly when switching.
- Commercial models are only accessible via APIs licensed by their developers.

---

## Build Versus Buy Considerations
- Open source models can be supported by any API provider, letting you pick the best fit.
- For commercial model providers, models are the competitive advantage; for API providers, APIs are.
- API providers may be more motivated to offer better APIs and better pricing.
- Building scalable inference services for large models is nontrivial, driving third-party inference and finetuning services.

---

## Build Versus Buy

- Whether to self-host a model or use a model API depends on the use case.
- The same use case can change over time.
- Seven axes to consider: data privacy, data lineage, performance, functionality, costs, control, on-device deployment.
- Commercial API providers that deploy within your private networks are treated like self-hosted models.

---

## Weighing APIs Against Self-Hosting

- Model APIs and self-hosted models each carry distinct pros and cons.
- Table 4-4 lays out those trade-offs side by side, with cons in italics.
- Use the comparison to match hosting choice to your use case's requirements.

---

## Data Privacy Drives Self-Hosting
- Strict data privacy policies rule out externally hosted model APIs for many companies.
- Samsung employees leaked proprietary information via ChatGPT; Samsung banned ChatGPT in May 2023.
- Some countries forbid sending certain data outside their borders, requiring local servers.
- API providers may train on your data; Zoom faced backlash after quietly changing terms in August 2023.

---

## Memorization and Data Lineage Risks
- Research suggests models can memorize training samples; StarCoder reportedly memorizes 8% of its training set.
- Memorized samples can leak to users or be exploited by bad actors.
- Training data transparency is low: Google's Gemini report and OpenAI's CTO gave little detail.
- AI IP laws are evolving; IP-dependent companies like gaming and movie studios hesitate to adopt AI.

---

## Weighing Open Source Versus Commercial Models
- Open models with public training data let the community inspect it, though full inspection is impractical.
- Open source models have limited legal resources; infringement risk may fall on you.
- Commercial model contracts can potentially protect you from data lineage risks.
- 

---

## Closing Performance Gap

- Benchmarks show the gap between open source and proprietary models is closing.
- Figure 4-7 shows this gap decreasing on the MMLU benchmark over time.
- Many believe an open source model may one day match or beat the strongest proprietary model.

---

## Why Proprietary Models Likely Stay Ahead

- Incentives discourage open sourcing the strongest model: capitalize on it yourself instead.
- Companies commonly keep strongest models behind APIs and open source their weaker models.
- Strongest open source model likely lags strongest proprietary models for the foreseeable future.
- Open source developers get no feedback from users on how models perform in the wild.

---

## Practical Takeaway

- For many use cases that don't need the strongest models, open source models might be sufficient.
- Commercial models benefit from user feedback that open source developers never receive.
- Once a model is open sourced, developers don't know how it is used or how well it works.

---

## Functionality: APIs Versus Self-Hosting

- APIs offer scalability, function calling, structured outputs, and guardrails out of the box.
- These functionalities are challenging and time-consuming to build yourself.
- Downside: you are restricted to what the API exposes, such as limited logprobs.
- Finetuning a commercial model requires the provider to offer a finetuning API.

---

## Cost, Reliability, and Swappability

- APIs charge per usage and can become prohibitively expensive at heavy scale.
- Self-hosting demands nontrivial time, talent, and engineering effort to optimize and maintain.
- Using another API means depending on their SLA; unreliable APIs require your own guardrails.
- Prefer models following a standard API (many mimic OpenAI's) and with good community support.

---

## Control, Access, and Transparency

- A 2024 a16z study: enterprises value open source models for control and customizability.
- API users are subject to provider terms, rate limits, and over-censoring safety guardrails.
- Commercial models can't be frozen; changes and versions are often unannounced.
- Providers may drop your use case, industry, or country, or go out of business.

---

## On-device Deployment
- On-device deployment rules out third-party APIs.
- Local models help when internet access is unreliable.
- Privacy: an AI assistant can access device data without sending it externally.
- Table 4-4 summarizes pros and cons of model APIs versus self-hosting.

---

## Model APIs vs Self-Hosting
- Model APIs require sending data to providers; self-hosting avoids sending data externally.
- Best-performing models are likely closed source; best open source models likely a bit behind.
- APIs more likely support scaling, function calling, structured outputs; less likely expose logprobs.
- Self-hosting may lack function calling/structured outputs but can expose logprobs and intermediate outputs.

---

## Cost, Finetuning, and Control
- API cost versus self-hosting talent, time, and engineering effort to optimize, host, maintain.
- Model hosting services can mitigate self-hosting maintenance burden.
- APIs allow finetuning only where providers permit; self-hosting can finetune, quantize, optimize if licenses allow.
- APIs have rate limits, access-loss risk, and versioning opacity; self-hosting eases inspection but you own access.

---

## Using Model APIs

- This section is titled “Using model APIs.”

---

## Choose Hosting Approach
- Self-host models to build and maintain your own model APIs.
- Some edge use cases cannot run on device.
- Other edge cases can run on device but without internet access.
- Pros and cons help decide commercial API versus self-hosting.

---

## Narrow and Refine Selection
- The hosting decision should significantly narrow your options.
- Refine your selection using publicly available model performance data.
- Public benchmark data can inform the remaining model choice.

---

## Public Benchmarks

- Thousands of benchmarks exist to evaluate different model capabilities.
- Google’s BIG-bench (2022) alone contains 214 benchmarks.
- Benchmark numbers grow rapidly to match expanding AI use cases.
- Old benchmarks saturate as models improve, requiring new ones.

---

## Evaluation Harnesses

- An evaluation harness evaluates a model across multiple benchmarks at once.
- EleutherAI’s lm-evaluation-harness supports over 400 benchmarks.
- OpenAI’s evals lets you run roughly 500 existing benchmarks.
- OpenAI’s evals also lets you register new benchmarks to evaluate its models.

---

## Navigate Public Benchmarks: Leaderboard Limits

- Leaderboards rank models on a small benchmark subset due to compute constraints.
- HELM Lite excluded MS MARCO; Hugging Face opted out of HumanEval (large compute requirements).
- Hugging Face's Open LLM Leaderboard grew from four to six benchmarks by end of 2023.
- Small benchmark sets cannot represent foundation models' vast capabilities and failure modes.

---

## Comparing Leaderboards Is Hard

- Benchmark selection processes aren't always clear to users, making rankings hard to compare.
- Hugging Face's six benchmarks: ARC-C, MMLU, HellaSwag, TruthfulQA, WinoGrande, GSM-8K.
- HELM used ten benchmarks; only MMLU and GSM-8K overlapped with Hugging Face's list.
- HELM added MATH, LegalBench, MedQA, WMT 2014, NarrativeQA, OpenBookQA, and Natural Questions.

---

## Coverage and Correlation Trade-offs

- Leaderboards balance coverage against benchmark count, spanning reasoning, facts, and domains.
- No clarity on what coverage means or why it stops at six or ten benchmarks.
- Strongly correlated benchmarks are redundant and can exaggerate biases.
- Selecting benchmarks to rank models is genuinely hard.

---

## Public Benchmarks Saturate
- Many benchmarks became saturated or near-saturated while this book was written.
- June 2024: Hugging Face replaced benchmarks with harder, more practical ones.
- MATH lvl 5 replaced GSM-8K; MMLU-PRO replaced MMLU.
- New additions include GPQA, MuSR, BBH, and IFEval; these will likely saturate too.

---

## Correlation and Aggregation
- WinoGrande, MMLU, and ARC-C are strongly correlated because they test reasoning together.
- TruthfulQA is only moderately correlated: better reasoning and math don't always mean better truthfulness.
- Hugging Face averages benchmark scores, treating an 80% on TruthfulQA same as on GSM-8K.
- HELM authors instead use mean win rate: fraction of times a model beats another, averaged across scenarios.

---

## Building a Custom Leaderboard
- High leaderboard rank likely, but far from always, predicts good performance for your application.
- Choose benchmarks matching your capabilities (e.g., code benchmarks for a coding agent); prefer the latest.
- Verify reliability: anyone can publish a benchmark, and it may not measure what you expect.
- Scores use different units (accuracy, F1, BLEU); weigh them by importance and run missing evaluations yourself.

---

## Data Contamination with Public Benchmarks

- Data contamination has many names: data leakage, training on the test set, or cheating
- It happens when a model is trained on the same data it is evaluated on
- The model may memorize training answers, scoring higher than it should
- A model trained on MMLU can score well without being useful

---

## Demonstrating Contamination

- Rylan Schaeffer, a Stanford PhD student, published the 2023 satirical paper “Pretraining on the Test Set Is All You Need”
- He trained exclusively on data from several benchmarks
- His one-million-parameter model achieved near-perfect scores
- It outperformed much larger models on all these benchmarks

---

## How Data Contamination Happens

- Most contamination is unintentional: training data scraped from the internet can pull in public benchmark data.
- Benchmark data published before a model's training is likely included in that training data.
- This helps explain why existing benchmarks saturate quickly and why developers create new ones.

---

## Indirect and Intentional Contamination

- Indirect: training and evaluation data share a source, e.g. math textbooks used for training and for benchmark questions.
- Intentional, for good reasons: benchmark data is high quality and can improve model performance.
- A developer may exclude benchmarks initially, then continue training the best model on them before release.

---

## Consequences of Released Contamination

- The released model is contaminated, so users cannot evaluate it on contaminated benchmarks.
- Training on benchmark data before release may still be the right thing to do.

---

## Data Contamination Undermines Benchmarks
- Data contamination is prevalent and undermines the trustworthiness of evaluation benchmarks.
- High benchmark scores do not guarantee real-world competence.
- Example: passing the bar exam may reflect training on bar exam questions, not legal advising skill.
- Treat benchmark results with caution until contamination is ruled out.

---

## Detecting and Decontaminating Data
- First detect contamination, then decontaminate the data.
- Detection can use heuristics such as n-gram overlapping.
- Perplexity is another heuristic for detecting contamination.
- 

---

## N-Gram Overlapping and Dirty Samples

- N-gram overlapping checks whether evaluation sample token sequences appear in training data.
- If a 13-token sequence from an evaluation sample is in training data, the model likely saw it.
- Such an evaluation sample is considered dirty.
- Dirty samples can undermine evaluation because training overlap may inflate performance.

---

## Detecting Data Contamination

- Perplexity measures how easily a model predicts text; unusually low values may indicate prior exposure
- The n-gram overlapping approach is more accurate but time-consuming and expensive to run
- N-gram comparison requires comparing each benchmark example against the entire training data
- Perplexity is less accurate but much less resource-intensive

---

## Why Contamination Persists

- ML textbooks advised removing evaluation samples, but foundation model users often lack training data control
- High-quality benchmark data can improve model performance, so full removal may be undesirable
- Benchmarks created after training always exist, so contaminated samples are unavoidable
- OpenAI found 13 benchmarks with at least 40% of data in GPT-3's training data

---

## Mitigation and the Role of Benchmarks

- Developers should disclose what percentage of a benchmark appears in their training data
- Report performance on both the overall benchmark and its clean samples
- Leaderboard hosts like Hugging Face plot standard deviations to spot outliers
- Benchmarks should keep data private and offer tools to evaluate against hold-out data

---

## Design Your Evaluation Pipeline
- AI application success often hinges on differentiating good outcomes from bad outcomes.
- A reliable evaluation pipeline is needed to make this distinction.
- Many evaluation methods exist, making the right combination confusing.
- This section focuses on open-ended tasks; close-ended pipelines can be inferred.

---

## Step 1: Evaluate All Components
- Real-world AI applications are complex, with many components and multi-turn tasks.
- Evaluation can occur per task, per turn, and per intermediate output.
- Evaluate end-to-end output and each component’s intermediate output independently.
- Example: extract PDF text, then extract current employer from that text.

---

## Evaluate Every Component Independently
- Real-world AI applications are complex, with many components and multi-turn tasks.
- Evaluate end-to-end output and each component's intermediate output independently.
- Example: PDF-to-text extraction then employer extraction; failure could come from either step.
- Evaluate each step separately to identify exactly where the system fails.

---

## Turn-Based vs Task-Based Evaluation
- Turn-based evaluation assesses the quality of each output.
- Task-based evaluation assesses whether the system completes a task.
- Task-based evaluation matters more to users, but task boundaries can be hard to determine.
- Example: twenty_questions benchmark scores success and number of questions needed.

---

## Step 2: Create an Evaluation Guideline

- Clear guidelines are the most important step; ambiguous guidelines produce ambiguous, misleading scores.
- Define what the application should do *and* what it shouldn't do.
- Specify out-of-scope inputs, how to detect them, and how the app should respond.
- If you don't know what bad responses look like, you can't catch them.

---

## Define Criteria and Scoring Rubrics

- A correct response is not always a good response (e.g., "You are a terrible fit").
- LangChain users averaged 2.3 feedback criteria; example: relevance, factual consistency, safety.
- Choose a scoring system: binary, 1–5, 0–1, or three values (-1 contradiction, 1 entailment, 0 neutral).
- Build a rubric with examples, validate with humans, and refine until unambiguous.

---

## Tie Evaluation Metrics to Business Metrics

- The application must serve a business goal; interpret metrics in that context.
- 80% factual consistency may fail billing queries but suit product recommendations.
- Map metrics to outcomes, e.g.: 80% consistency → automate 30% of support requests.
- Knowing the gain from improving a metric builds confidence to invest resources.

---

## Choose Methods and Annotate Data
- Match criteria to methods: classifiers, semantic similarity, AI judges, and logprobs.
- Mix cheap broad signals with expensive high-quality judges on smaller subsets.
- Use production data; label with humans or AI; reuse annotation guidelines for finetuning.
- Slice data to avoid bias, debug, improve, and catch Simpson’s paradox.

---

## Size and Validate Evaluation Sets
- Evaluation sets should be large enough for reliable results but not prohibitively expensive.
- Bootstrap examples to check variance; use bigger sets if results vary wildly.
- OpenAI: detecting a 30% difference needs ~10 samples; 1% needs ~10,000.
- Evaluate pipeline signal, reliability, metric correlation, cost, and latency.

---

## Why Evaluation Matters
- A reliable evaluation pipeline is essential; lacking one blocks AI adoption.
- Evaluation takes time but reduces risks, reveals improvements, and benchmarks progress.
- Modern AI evaluation has limitations and biases; no perfect method exists.
- Combining methods can mitigate challenges, so evaluation remains necessary.

---

## Selecting Models and Benchmarks
- With many foundation models, developers must select the right model for their application.
- Evaluate domain-specific and generation capabilities, including factual consistency and safety.
- Hosting versus API involves trade-offs across privacy, lineage, performance, functionality, control, and cost.
- Public benchmarks help weed out bad models but may be contaminated and unclear.

---

## Building an Evaluation Pipeline
- Log evaluation variables: data, rubric, and prompt and sampling configurations for AI judges.
- Public leaderboards inform model selection, akin to creating a private leaderboard.
- Evaluation will recur throughout development, including retrieval, agents, costs, data quality, and user feedback.
- No single score captures a high-dimensional system; combine approaches.

## Practice Questions

### Question 1: According to the chapter, when should you evaluate models?

According to the chapter, when should you evaluate models?

- [ ] A) Only after deployment
- [ ] B) In the context of your application
- [ ] C) Only by using public leaderboards
- [ ] D) Only when using proprietary models

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** The text states that a model is only useful if it works for its intended purposes, so you need to evaluate models in the context of your application.

### Question 2: What does the first part of the chapter discuss?

What does the first part of the chapter discuss?

- [ ] A) How to host open source models
- [ ] B) Criteria for evaluating applications and how these criteria are defined and calculated
- [ ] C) How to build model API services
- [ ] D) How to aggregate benchmarks into leaderboards

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** The chapter says it starts with a discussion of the criteria you might use to evaluate your applications and how these criteria are defined and calculated.

### Question 3: What question does the text say many teams will need to visit over...

What question does the text say many teams will need to visit over and over again?

- [ ] A) Whether to use automatic evaluation or human evaluation
- [ ] B) Whether to trust public leaderboards
- [ ] C) Whether to host their own models or to use a model API
- [ ] D) Whether to evaluate factual consistency or domain-specific capabilities

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** C

    **Explanation:** The text states that a question many teams will need to visit over and over again is whether to host their own models or to use a model API.

### Question 4: According to the source, which is worse?

According to the source, which is worse?

- [ ] A) An application that has never been deployed
- [ ] B) An application that is deployed but no one knows whether it’s working
- [ ] C) An application with clear evaluation criteria
- [ ] D) An application with a high return on investment

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** The source says most conference attendees considered the deployed-but-unevaluable application worse, and the author agrees it is worse because it costs to maintain and may cost even more to take down.

### Question 5: What does evaluation-driven development mean in AI engineering?

What does evaluation-driven development mean in AI engineering?

- [ ] A) Writing tests before writing code
- [ ] B) Defining evaluation criteria before building an application
- [ ] C) Deploying an application before evaluating it
- [ ] D) Focusing only on open-ended generation tasks

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** The source states that evaluation-driven development means defining evaluation criteria before building, inspired by test-driven development in software engineering.

### Question 6: According to the source, why is coding a common generative AI use c...

According to the source, why is coding a common generative AI use case?

- [ ] A) Generated code can be evaluated using functional correctness
- [ ] B) Coding tasks are always open-ended
- [ ] C) Coding applications require no evaluation criteria
- [ ] D) Coding increases purchase-through rates

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** A

    **Explanation:** The source says coding is common because, unlike other generation tasks, generated code can be evaluated using functional correctness.

### Question 7: The source compares focusing only on applications whose outcomes ca...

The source compares focusing only on applications whose outcomes can be measured to what?

- [ ] A) Chasing the latest hype
- [ ] B) Looking for the lost key under the lamppost at night
- [ ] C) Using test-driven development
- [ ] D) Measuring fraud detection savings

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** The source says focusing only on measurable-outcome applications is similar to looking for the lost key under the lamppost at night: it is easier, but it may mean missing potentially game-changing applications.

### Question 8: According to the text, what constrains a model’s domain-specific ca...

According to the text, what constrains a model’s domain-specific capabilities?

- [ ] A) Only the model’s prompt engineering
- [ ] B) The model’s configuration and training data
- [ ] C) Only the model’s cost and latency
- [ ] D) The model’s generation capability metrics

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** The text states that domain-specific capabilities are constrained by configuration (such as architecture and size) and training data.

### Question 9: Why are multiple-choice questions (MCQs) popular for evaluating non...

Why are multiple-choice questions (MCQs) popular for evaluating non-coding domain capabilities?

- [ ] A) They are ideal for evaluating summarization and essay writing.
- [ ] B) They are easy to create, verify, and evaluate against the random baseline.
- [ ] C) They eliminate all prompt sensitivity.
- [ ] D) They require no public or private benchmarks.

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** The text says MCQs are popular because they are easy to create, verify, and evaluate against the random baseline.

### Question 10: What drawback of using MCQs does the text mention?

What drawback of using MCQs does the text mention?

- [ ] A) They cannot evaluate knowledge or reasoning.
- [ ] B) They are difficult to create and verify.
- [ ] C) A model’s performance can vary with small changes in how questions and options are presented.
- [ ] D) They always have multiple correct answers.

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** C

    **Explanation:** The text notes that MCQ performance can change with small presentation changes, such as an extra space or an added instructional phrase.

### Question 11: According to the text, what does fluency measure in generated text?

According to the text, what does fluency measure in generated text?

- [ ] A) Whether the text is grammatically correct and natural-sounding
- [ ] B) Whether the whole text follows a logical structure
- [ ] C) How faithful a translation is to the original sentence
- [ ] D) Whether a summary focuses on the most important aspects of the source document

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** A

    **Explanation:** The text defines fluency as whether the text is grammatically correct and natural-sounding.

### Question 12: Which metric measures how well-structured the whole text is?

Which metric measures how well-structured the whole text is?

- [ ] A) Faithfulness
- [ ] B) Relevance
- [ ] C) Coherence
- [ ] D) Controversiality

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** C

    **Explanation:** The text states that coherence measures how well-structured the whole text is and whether it follows a logical structure.

### Question 13: What does the text identify as the most pressing issue for generati...

What does the text identify as the most pressing issue for generative models that requires new metrics?

- [ ] A) Lack of fluency
- [ ] B) Undesired hallucinations
- [ ] C) Poor paraphrasing
- [ ] D) Low coherence

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** The text says the most pressing issue is undesired hallucinations, and factual consistency is a metric many application developers want to measure.

### Question 14: In the text, safety is described as an umbrella term for what?

In the text, safety is described as an umbrella term for what?

- [ ] A) Fluency and coherence
- [ ] B) Faithfulness and relevance
- [ ] C) All types of toxicity and biases
- [ ] D) Creativity and conciseness

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** C

    **Explanation:** The text defines safety as an umbrella term for all types of toxicity and biases.

### Question 15: According to the text, factual consistency can be verified under wh...

According to the text, factual consistency can be verified under which two settings?

- [ ] A) Against model size or against training time
- [ ] B) Against user feedback or against benchmark scores
- [ ] C) Against explicitly provided facts (context) or against open knowledge
- [ ] D) Against latency metrics or against cost metrics

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** C

    **Explanation:** The source states factual consistency can be verified against explicitly provided facts (context) or against open knowledge.

### Question 16: Why have many techniques been developed to detect and measure factu...

Why have many techniques been developed to detect and measure factual inconsistency?

- [ ] A) Because it has potential for catastrophic consequences
- [ ] B) Because it is always easy to measure
- [ ] C) Because it only affects open knowledge
- [ ] D) Because it eliminates the need for context

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** A

    **Explanation:** The text says factual inconsistency’s potential for catastrophic consequences has led to many techniques being developed.

### Question 17: What does the text say about covering all techniques for detecting...

What does the text say about covering all techniques for detecting and measuring factual inconsistency?

- [ ] A) One chapter can cover them all completely
- [ ] B) It is impossible to cover them all in one chapter, so only broad strokes are given
- [ ] C) Only open-knowledge techniques are worth covering
- [ ] D) No techniques currently exist

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** The source states it is impossible to cover all techniques in one chapter, so it goes over only the broad strokes.

### Question 18: According to the text, when is an output considered locally factual...

According to the text, when is an output considered locally factually consistent?

- [ ] A) When it matches commonly accepted open knowledge
- [ ] B) When it is supported by the given context
- [ ] C) When it contains scientific references and a neutral tone
- [ ] D) When no reliable sources can be found

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** The text says the output is evaluated against a context and is factually consistent if it is supported by that context.

### Question 19: For which type of task is local factual consistency described as im...

For which type of task is local factual consistency described as important?

- [ ] A) Summarization
- [ ] B) General chatbots
- [ ] C) Market research
- [ ] D) Fact-checking

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** A

    **Explanation:** The text lists summarization as a task with limited scope where local factual consistency is important.

### Question 20: According to the text, what is often the hardest part of factual co...

According to the text, what is often the hardest part of factual consistency verification?

- [ ] A) Finding a model that ignores website relevance
- [ ] B) Determining what the facts are
- [ ] C) Avoiding the use of explicit facts
- [ ] D) Making every statement a commonly accepted fact

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** The text states that often the hardest part of factual consistency verification is determining what the facts are.

### Question 21: What did Wan et al. (2024) find about existing models when processi...

What did Wan et al. (2024) find about existing models when processing evidence?

- [ ] A) They rely heavily on website relevance to the query and largely ignore stylistic features humans find important
- [ ] B) They rely mainly on neutral tone and scientific references rather than website relevance
- [ ] C) They always reject misinformation from biased social media posts
- [ ] D) They verify facts only against explicit local context

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** A

    **Explanation:** The text says Wan et al. found models rely heavily on website relevance to the query while largely ignoring stylistic features humans find important.

### Question 22: When designing metrics to measure hallucinations, what should a ben...

When designing metrics to measure hallucinations, what should a benchmark focus on?

- [ ] A) Queries that the model is more likely to hallucinate on
- [ ] B) Randomly selected queries regardless of model behavior
- [ ] C) Only queries involving commonly referenced knowledge
- [ ] D) Queries that never require factual consistency

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** A

    **Explanation:** The source says to analyze model outputs to understand the types of queries it is more likely to hallucinate on, and the benchmark should focus more on these queries.

### Question 23: In the source’s example, why was the model more likely to hallucina...

In the source’s example, why was the model more likely to hallucinate on VMO queries than IMO queries?

- [ ] A) VMO is much less commonly referenced than IMO
- [ ] B) VMO is more commonly referenced than IMO
- [ ] C) IMO involves niche knowledge while VMO does not
- [ ] D) VMO queries always ask about things that do not exist

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** A

    **Explanation:** The source states the model was more likely to hallucinate about the VMO than the IMO because the VMO is much less commonly referenced than the IMO.

### Question 24: What does “TruthfulQA: Measuring How Models Mimic Human Falsehoods”...

What does “TruthfulQA: Measuring How Models Mimic Human Falsehoods” show about the finetuned GPT-judge?

- [ ] A) It can predict whether a statement is considered truthful by humans with 90–96% accuracy
- [ ] B) It can retrieve context for factual consistency evaluation
- [ ] C) It can outperform GPT-4 at all evaluation tasks
- [ ] D) It can identify only queries about things that do not exist

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** A

    **Explanation:** The source says Lin et al. (2022) shows their finetuned model GPT-judge is able to predict whether a statement is considered truthful by humans with 90–96% accuracy.

### Question 25: What assumption does SelfCheckGPT rely on when evaluating a response?

What assumption does SelfCheckGPT rely on when evaluating a response?

- [ ] A) If a model generates multiple outputs that disagree with one another, the original output is likely hallucinated.
- [ ] B) If a response is long, it is more likely to be factually consistent.
- [ ] C) If a search engine returns no results, the response is necessarily false.
- [ ] D) If a model can translate a response, the response is factually correct.

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** A

    **Explanation:** The source states SelfCheckGPT assumes that disagreement among multiple generated outputs suggests the original output is likely hallucinated.

### Question 26: In SAFE, what is done immediately after the response is decomposed...

In SAFE, what is done immediately after the response is decomposed into individual statements?

- [ ] A) Each statement is sent directly to a search engine without revision.
- [ ] B) Each statement is revised to make it self-contained.
- [ ] C) Each statement is translated into another language.
- [ ] D) Each statement is checked only by a human expert.

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** SAFE’s second step is to revise each statement so it is self-contained, such as replacing “it” with the original subject.

### Question 27: Given the premise “Mary likes all fruits,” which hypothesis is neut...

Given the premise “Mary likes all fruits,” which hypothesis is neutral according to the source’s textual entailment example?

- [ ] A) Mary likes apples.
- [ ] B) Mary hates oranges.
- [ ] C) Mary likes chickens.
- [ ] D) Mary likes all fruits.

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** C

    **Explanation:** The source lists “Mary likes chickens” as the neutral example because the premise neither entails nor contradicts it.

### Question 28: What does TruthfulQA comprise?

What does TruthfulQA comprise?

- [ ] A) 817 questions that some humans would answer incorrectly due to a false belief or misconception, spanning 38 categories.
- [ ] B) 184 million annotated premise-hypothesis pairs for training DeBERTa.
- [ ] C) A search engine API used by SAFE to fact-check individual statements.
- [ ] D) A set of N new responses generated by SelfCheckGPT to measure consistency.

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** A

    **Explanation:** The source states TruthfulQA comprises 817 questions across 38 categories that some humans would answer incorrectly due to false beliefs or misconceptions.

### Question 29: According to the text, which of the following is listed as a catego...

According to the text, which of the following is listed as a category of unsafe content?

- [ ] A) Factual inconsistency
- [ ] B) Inappropriate language, including profanity and explicit content
- [ ] C) Model latency
- [ ] D) Token count

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** The text lists inappropriate language, including profanity and explicit content, as one category of unsafe content, while factual consistency is discussed separately.

### Question 30: According to the text, which foundation model is described as more...

According to the text, which foundation model is described as more authoritarian in its political leanings?

- [ ] A) GPT-4
- [ ] B) Meta’s Llama
- [ ] C) Claude
- [ ] D) Gemini

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** The text states that OpenAI’s GPT-4 is more left-winged and libertarian-leaning, whereas Meta’s Llama is more authoritarian.

### Question 31: According to the text, how do specialized toxicity detection models...

According to the text, how do specialized toxicity detection models compare with general-purpose AI judges?

- [ ] A) They tend to be much smaller, faster, and cheaper
- [ ] B) They tend to be larger, slower, and more expensive
- [ ] C) They can only detect factual inconsistencies
- [ ] D) They are only available for human-generated text

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** A

    **Explanation:** The text says specialized models for detecting toxicity tend to be much smaller, faster, and cheaper than general-purpose AI judges.

### Question 32: What question does instruction-following measurement ask?

What question does instruction-following measurement ask?

- [ ] A) How much domain knowledge does the model have?
- [ ] B) How good is this model at following the instructions you give it?
- [ ] C) How quickly can the model generate outputs?
- [ ] D) How toxic are the model’s outputs?

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** The source states that instruction-following measurement asks how good a model is at following the instructions you give it.

### Question 33: What does the Google benchmark IFEval focus on?

What does the Google benchmark IFEval focus on?

- [ ] A) Whether the model can produce outputs following an expected format
- [ ] B) Whether the model can roleplay a fictional character
- [ ] C) Whether the model can avoid all toxic prompts
- [ ] D) Whether the model can discuss only climate change

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** A

    **Explanation:** The source says IFEval focuses on whether the model can produce outputs following an expected format, using automatically verifiable instructions.

### Question 34: How is a model’s final score computed on INFOBench?

How is a model’s final score computed on INFOBench?

- [ ] A) By counting only whether the output is in JSON format
- [ ] B) By averaging human ratings on a five-point scale
- [ ] C) By dividing the number of criteria a model gets right by the total number of criteria for all instructions
- [ ] D) By measuring the average length of the model’s outputs

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** C

    **Explanation:** The source states that the final INFOBench score is the number of criteria a model gets right divided by the total number of criteria for all instructions.

### Question 35: Which benchmark used human annotators and trained a reward model to...

Which benchmark used human annotators and trained a reward model to evaluate each roleplaying aspect on a five-point scale?

- [ ] A) IFEval
- [ ] B) RealToxicityPrompts
- [ ] C) CharacterEval
- [ ] D) BOLD

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** C

    **Explanation:** The source says CharacterEval used human annotators and trained a reward model to evaluate each roleplaying aspect on a five-point scale.

### Question 36: According to the source, what is the active field of study for opti...

According to the source, what is the active field of study for optimizing for multiple objectives such as model quality, latency, and cost?

- [ ] A) Pareto optimization
- [ ] B) Token optimization
- [ ] C) Prompt optimization
- [ ] D) Autoregressive optimization

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** A

    **Explanation:** The source states that optimizing for multiple objectives is an active field of study called Pareto optimization.

### Question 37: Which statement about latency for foundation models is supported by...

Which statement about latency for foundation models is supported by the source?

- [ ] A) Latency depends only on the underlying model.
- [ ] B) Time to first token is the only latency metric for foundation models.
- [ ] C) Latency depends on the underlying model and also on each prompt and sampling variables.
- [ ] D) Autoregressive models generate all output tokens at once, so token count does not affect latency.

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** C

    **Explanation:** The source says latency depends not only on the underlying model but also on each prompt and sampling variables, and autoregressive models typically generate outputs token by token.

### Question 38: If you host your own models, what does the source say about cost pe...

If you host your own models, what does the source say about cost per token as you scale?

- [ ] A) Cost per token usually does not change much as you scale.
- [ ] B) Cost per token can get much cheaper as you scale.
- [ ] C) Cost per token always increases in direct proportion to tokens served.
- [ ] D) Cost per token is determined only by engineering cost.

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** The source contrasts model APIs, where cost per token usually doesn’t change much as you scale, with self-hosted models, where cost per token can get much cheaper as you scale.

### Question 39: When evaluating models based on latency, why does the source advise...

When evaluating models based on latency, why does the source advise differentiating between must-have and nice-to-have?

- [ ] A) Because users will always reject any model with high latency.
- [ ] B) Because latency is always a deal breaker rather than an annoyance.
- [ ] C) Because if asked, nobody will say no to lower latency, but high latency is often an annoyance, not a deal breaker.
- [ ] D) Because latency metrics are irrelevant when using model APIs.

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** C

    **Explanation:** The source notes that users will never say no to lower latency, but high latency is often an annoyance rather than a deal breaker, so must-have and nice-to-have latency should be distinguished.

### Question 40: According to the text, what should you care about when selecting a...

According to the text, what should you care about when selecting a model?

- [ ] A) Which model is the best overall
- [ ] B) Which model is the best for your application
- [ ] C) Which model has the largest parameter count
- [ ] D) Which model is cheapest to run

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** The text says you don’t really care about which model is best overall; you care about which model is best for your application.

### Question 41: In prompt engineering, what model selection approach does the text...

In prompt engineering, what model selection approach does the text suggest?

- [ ] A) Start with the smallest model and move upward
- [ ] B) Start with the strongest model overall to evaluate feasibility, then work backward to see if smaller models would work
- [ ] C) Avoid evaluating models against application criteria
- [ ] D) Only use models that fit one GPU

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** The text gives prompt engineering as an example where you might start with the strongest model overall to evaluate feasibility and then work backward to smaller models.

### Question 42: When finetuning, what model selection approach does the text describe?

When finetuning, what model selection approach does the text describe?

- [ ] A) Start with the biggest model and then move to smaller models
- [ ] B) Start with a small model to test your code and move toward the biggest model that fits your hardware constraints
- [ ] C) Always use the strongest model overall regardless of hardware
- [ ] D) Skip model selection after defining criteria

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** The text says if you decide to do finetuning, you might start with a small model to test your code and move toward the biggest model that fits your hardware constraints.

### Question 43: In the example criteria table, what is the hard requirement for fac...

In the example criteria table, what is the hard requirement for factual consistency measured by the internal GPT metric on the internal hallucination dataset?

- [ ] A) > 0.9
- [ ] B) > 0.8
- [ ] C) < 0.8
- [ ] D) = 0.8

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** The table lists factual consistency with the internal GPT metric and internal hallucination dataset, with a hard requirement of > 0.8 and an ideal of > 0.9.

### Question 44: According to the source, what distinguishes hard attributes from so...

According to the source, what distinguishes hard attributes from soft attributes in model selection?

- [ ] A) Hard attributes are always related to cost, while soft attributes are always related to latency.
- [ ] B) Hard attributes are impossible or impractical to change, while soft attributes can be improved upon.
- [ ] C) Hard attributes are only benchmark scores, while soft attributes are only leaderboard rankings.
- [ ] D) Hard attributes apply only to open source models, while soft attributes apply only to commercial APIs.

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** The source defines hard attributes as what is impossible or impractical to change and soft attributes as what you can and are willing to change.

### Question 45: What is the first step in the high-level evaluation workflow descri...

What is the first step in the high-level evaluation workflow described in the source?

- [ ] A) Continually monitor the model in production to detect failure.
- [ ] B) Run experiments with your own evaluation pipeline to find the best model.
- [ ] C) Filter out models whose hard attributes don’t work for you.
- [ ] D) Use public benchmarks and leaderboard rankings to narrow down models.

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** C

    **Explanation:** The source lists filtering out models whose hard attributes don’t work as step 1 of the four-step evaluation workflow.

### Question 46: Why does the source describe the four evaluation workflow steps as...

Why does the source describe the four evaluation workflow steps as iterative?

- [ ] A) Because newer information from a current step may lead you to change a decision from a previous step.
- [ ] B) Because public benchmarks are always sufficient to choose the final model.
- [ ] C) Because hard attributes never depend on internal policies or hosting choices.
- [ ] D) Because monitoring in production is not part of the evaluation workflow.

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** A

    **Explanation:** The source says the steps are iterative because you might change a previous decision with newer information from the current step.

### Question 47: According to the text, what should you do when something can’t be t...

According to the text, what should you do when something can’t be trusted?

- [ ] A) Design your own evaluation pipeline with prompts and metrics you can trust
- [ ] B) Use any available evaluation pipeline
- [ ] C) Avoid designing prompts and metrics
- [ ] D) Trust the existing metrics

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** A

    **Explanation:** The text says that when something can’t be trusted, you need to design your own evaluation pipeline with prompts and metrics you can trust.

### Question 48: What does the text say your own evaluation pipeline should include?

What does the text say your own evaluation pipeline should include?

- [ ] A) Prompts and metrics you can trust
- [ ] B) Only prompts
- [ ] C) Only metrics
- [ ] D) No prompts or metrics

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** A

    **Explanation:** The text specifically mentions designing an evaluation pipeline with prompts and metrics you can trust.

### Question 49: According to the text, what is the main build-versus-buy question f...

According to the text, what is the main build-versus-buy question for companies leveraging foundation models?

- [ ] A) Whether to build foundation models from scratch or buy them
- [ ] B) Whether to use commercial model APIs or host an open source model yourself
- [ ] C) Whether to use open weight or open model
- [ ] D) Whether to audit training data or not

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** The text states that since most companies won’t build foundation models from scratch, the question is whether to use commercial model APIs or host an open source model yourself.

### Question 50: How does the text distinguish between “open weight” and “open model”?

How does the text distinguish between “open weight” and “open model”?

- [ ] A) Open weight includes open data, while open model does not
- [ ] B) Open weight does not come with open data, while open model comes with open data
- [ ] C) Open weight is commercial, while open model is open source
- [ ] D) The terms are used interchangeably

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** The text says “open weight” is used for models that don’t come with open data, whereas “open model” is used for models that come with open data.

### Question 51: Why do some argue that a model should be considered open only if it...

Why do some argue that a model should be considered open only if its training data is also publicly available?

- [ ] A) Because being able to download the model is sufficient for all use cases
- [ ] B) Because open data allows more flexible usage, such as retraining from scratch and auditing
- [ ] C) Because commercial APIs require open data
- [ ] D) Because open weight models cannot be downloaded

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** The text explains that open data allows retraining with modifications and makes it easier to understand and audit the model, such as checking for compromised or illegally acquired data.

### Question 52: In this book, how is the term “open source” used for models?

In this book, how is the term “open source” used for models?

- [ ] A) Only for models whose training data and licenses are fully open
- [ ] B) For all models whose weights are made public, regardless of training data availability and licenses
- [ ] C) Only for models released under Apache 2.0
- [ ] D) Only for models that allow commercial use without restrictions

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** The note says open source is used for simplicity to refer to all models whose weights are made public, regardless of training data availability and licenses.

### Question 53: As of the writing, what is true of the vast majority of open source...

As of the writing, what is true of the vast majority of open source models?

- [ ] A) They are fully open, including training data
- [ ] B) They are open weight only
- [ ] C) They are released under GPL
- [ ] D) They prohibit all commercial use

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** The source states that as of this writing, the vast majority of open source models are open weight only.

### Question 54: What restriction do Llama-2 and Llama-3 licenses specify regarding...

What restriction do Llama-2 and Llama-3 licenses specify regarding commercial use?

- [ ] A) Commercial use is entirely prohibited
- [ ] B) Applications with more than 700 million monthly active users require a special license from Meta
- [ ] C) Commercial use is allowed only under Apache 2.0
- [ ] D) Outputs may never be used for any purpose

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** The text says Llama-2 and Llama-3 specify that applications with more than 700 million monthly active users require a special license from Meta.

### Question 55: Which models were released under Apache 2.0 according to the source?

Which models were released under Apache 2.0 according to the source?

- [ ] A) Llama 2 and Llama 3
- [ ] B) BigCode and Llama 2
- [ ] C) Google’s Gemma and Mistral-7B
- [ ] D) Meta’s first Llama model and BigCode

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** C

    **Explanation:** The source states that both Google’s Gemma and Mistral-7B were released under Apache 2.0.

### Question 56: What is the service called that hosts a model, receives user querie...

What is the service called that hosts a model, receives user queries, runs the model to generate responses, and returns those responses to users?

- [ ] A) Model API
- [ ] B) Inference service
- [ ] C) Finetuning API
- [ ] D) Evaluation API

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** The source defines an inference service as the service that hosts and runs the model and returns generated responses to users.

### Question 57: According to the source, why might API providers that do not have t...

According to the source, why might API providers that do not have their own models be more motivated to provide better APIs with better pricing?

- [ ] A) Because models are their competitive advantage
- [ ] B) Because they are required to open source all models
- [ ] C) Because APIs are their competitive advantage
- [ ] D) Because cloud providers do not offer API access

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** C

    **Explanation:** The text states that for API providers without their own models, APIs are their competitive advantage, which may motivate better APIs and pricing.

### Question 58: What does the source recommend when switching between model APIs th...

What does the source recommend when switching between model APIs that provide the same model?

- [ ] A) Avoid using commercial models
- [ ] B) Run thorough tests, since performance may differ due to different optimization techniques
- [ ] C) Only use APIs from the model developer
- [ ] D) Assume the model behaves identically across APIs

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** The source notes that the same model can be available through different APIs and that slight performance differences may occur, so thorough testing is advised when switching.

### Question 59: According to the note, how are commercial API providers that can de...

According to the note, how are commercial API providers that can deploy their services within your private networks treated in the discussion?

- [ ] A) As fully external services unrelated to self-hosting
- [ ] B) Similarly to self-hosted models
- [ ] C) As unsuitable for private networks
- [ ] D) As equivalent to on-device deployment only

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** The note says privately deployed commercial APIs are treated similarly to self-hosted models.

### Question 60: What does the source say determines whether to host a model yoursel...

What does the source say determines whether to host a model yourself or use a model API?

- [ ] A) Only the model’s parameter count
- [ ] B) Only the provider’s pricing
- [ ] C) The use case, which can change over time
- [ ] D) Whether the model is open source

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** C

    **Explanation:** The source states that the answer depends on the use case, and the same use case can change over time.

### Question 61: Which set of axes does the source list for considering self-hosting...

Which set of axes does the source list for considering self-hosting versus using a model API?

- [ ] A) Data privacy, data lineage, performance, functionality, costs, control, and on-device deployment
- [ ] B) Accuracy, latency, throughput, storage, licensing, support, and training data
- [ ] C) Cost, speed, size, modality, vendor, region, and uptime
- [ ] D) Privacy, security, compliance, scalability, reliability, observability, and fairness

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** A

    **Explanation:** The source explicitly lists these seven axes: data privacy, data lineage, performance, functionality, costs, control, and on-device deployment.

### Question 62: Why were externally hosted model APIs ruled out for some companies...

Why were externally hosted model APIs ruled out for some companies with strict data privacy policies?

- [ ] A) Because the APIs were too expensive to license
- [ ] B) Because sending data outside the organization violates their policies
- [ ] C) Because the APIs could not handle large volumes of data
- [ ] D) Because the providers refused to sign any contracts

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** The text states that externally hosted model APIs are out of the question for companies whose strict data privacy policies can't send data outside of the organization.

### Question 63: What incident led Samsung to ban ChatGPT in May 2023?

What incident led Samsung to ban ChatGPT in May 2023?

- [ ] A) Samsung employees entered proprietary company information into ChatGPT, leaking company secrets
- [ ] B) ChatGPT was found to memorize 8% of its training set
- [ ] C) Zoom changed its terms of service to train models on user data
- [ ] D) Google refused to disclose Gemini's training data

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** A

    **Explanation:** The text describes Samsung employees putting proprietary information into ChatGPT, accidentally leaking the company's secrets, which led Samsung to ban ChatGPT.

### Question 64: Why is it a concern that an API provider might use your data to tra...

Why is it a concern that an API provider might use your data to train its models?

- [ ] A) It always increases the provider's pricing tiers
- [ ] B) It prevents the provider from offering open source models
- [ ] C) Research suggests models can memorize training samples, which can be leaked or exploited
- [ ] D) It automatically transfers your IP ownership to the provider

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** C

    **Explanation:** The text notes studies suggesting AI models can memorize training samples (e.g., StarCoder memorizing 8% of its training set), which can be accidentally leaked or intentionally exploited.

### Question 65: According to the text, why do many companies opt for commercial mod...

According to the text, why do many companies opt for commercial models over open source models when concerned about data lineage?

- [ ] A) Commercial models always have fully transparent training data
- [ ] B) Open source models have limited legal resources, so the infringed party is more likely to go after you, while commercial contracts can potentially protect you
- [ ] C) Open source models are not permitted under US patent law
- [ ] D) Commercial models are the only ones that can be inspected by the community

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** The text explains that open source models tend to have limited legal resources, making users the likelier target of infringement claims, whereas contracts with commercial model providers can potentially protect you from data lineage risks.

### Question 66: What does Figure 4-7 show about open source and proprietary models...

What does Figure 4-7 show about open source and proprietary models on the MMLU benchmark?

- [ ] A) The gap between open source and proprietary models is increasing.
- [ ] B) The gap between open source and proprietary models is decreasing over time.
- [ ] C) Open source models have already surpassed the strongest proprietary models.
- [ ] D) Proprietary models are no longer evaluated on MMLU.

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** The source says Figure 4-7 shows the gap between open source models and proprietary models decreasing on the MMLU benchmark over time.

### Question 67: Why does the author doubt that open source models will catch up wit...

Why does the author doubt that open source models will catch up with the strongest proprietary models?

- [ ] A) Open source models are always more expensive to train.
- [ ] B) Companies tend to keep their strongest models behind APIs and open source their weaker models.
- [ ] C) Open source models cannot be evaluated with benchmarks.
- [ ] D) Proprietary models do not use APIs.

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** The author argues the incentives are not set up for open source to catch up, noting companies commonly keep their strongest models behind APIs and open source weaker models.

### Question 68: According to the source, what is another reason open source models...

According to the source, what is another reason open source models may lag behind commercial models?

- [ ] A) Open source developers do not receive user feedback to improve their models.
- [ ] B) Open source models are not allowed to use MMLU.
- [ ] C) Commercial models are always released as open source.
- [ ] D) Open source models are only used for the strongest use cases.

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** A

    **Explanation:** The source states that open source developers do not receive feedback from users the way commercial models do, because once a model is open sourced, developers do not know how it is used or how well it works in the wild.

### Question 69: What does the source suggest about open source models for many use...

What does the source suggest about open source models for many use cases that do not need the strongest models?

- [ ] A) They are never sufficient.
- [ ] B) They might be sufficient.
- [ ] C) They are always stronger than proprietary models.
- [ ] D) They cannot be used in production.

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** The source says that although the strongest open source model will likely lag behind the strongest proprietary models, open source models might be sufficient for many use cases that don’t need the strongest models.

### Question 70: According to the source, what is a downside of using a model API?

According to the source, what is a downside of using a model API?

- [ ] A) It always requires more engineering effort than hosting your own model.
- [ ] B) You are restricted to the functionalities that the API provides.
- [ ] C) It cannot be used for RAG or agentic use cases.
- [ ] D) It never supports structured outputs such as JSON.

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** The text states that the downside of using a model API is being restricted to the functionalities the API provides.

### Question 71: Why might commercial model providers hesitate to expose logprobs?

Why might commercial model providers hesitate to expose logprobs?

- [ ] A) Logprobs are only useful for image generation.
- [ ] B) Logprobs are too expensive to compute for any provider.
- [ ] C) They fear others might use logprobs to replicate their models.
- [ ] D) Logprobs are illegal in strictly regulated applications.

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** C

    **Explanation:** The source says providers might hesitate to expose logprobs for fear of others using them to replicate their models.

### Question 72: What does the source say about API cost versus engineering cost?

What does the source say about API cost versus engineering cost?

- [ ] A) APIs are expensive, but engineering can be even more so.
- [ ] B) Hosting a model yourself never requires significant engineering effort.
- [ ] C) APIs are always cheaper than hosting your own model at any scale.
- [ ] D) Engineering cost is irrelevant once a company uses APIs.

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** A

    **Explanation:** The text notes that APIs are expensive, but hosting a model yourself requires nontrivial time, talent, and engineering effort, so engineering can be even more costly.

### Question 73: According to the source, why do enterprises care about open source...

According to the source, why do enterprises care about open source models?

- [ ] A) Open source models always have better performance than proprietary models.
- [ ] B) The key reasons include control and customizability.
- [ ] C) Open source models eliminate all safety guardrails.
- [ ] D) Open source models are always easier to scale than proprietary models.

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** The source cites a 2024 a16z study showing that two key reasons enterprises care about open source models are control and customizability.

### Question 74: Why are third-party APIs out of the question for on-device deployment?

Why are third-party APIs out of the question for on-device deployment?

- [ ] A) They are always more expensive than self-hosted models
- [ ] B) They require sending data to external model providers rather than running locally
- [ ] C) They cannot be used for classification tasks
- [ ] D) They do not support structured outputs

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** The source says that if you want to run a model on-device, third-party APIs are out of the question, and using model APIs means you have to send your data to model providers.

### Question 75: Which is listed as an advantage of self-hosting models over using m...

Which is listed as an advantage of self-hosting models over using model APIs?

- [ ] A) The best-performing model will likely be open source
- [ ] B) More likely to support scaling and function calling
- [ ] C) You don’t have to send your data externally
- [ ] D) Less talent and engineering effort is required

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** C

    **Explanation:** Table 4-4 lists “Don’t have to send your data externally” under self-hosting models, while using model APIs requires sending data to model providers.

### Question 76: According to Table 4-4, which is a disadvantage of self-hosting mod...

According to Table 4-4, which is a disadvantage of self-hosting models?

- [ ] A) Rate limits
- [ ] B) Risk of losing access to the model
- [ ] C) Lack of transparency in model changes and versioning
- [ ] D) Talent, time, and engineering effort to optimize, host, and maintain

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** D

    **Explanation:** The table lists talent, time, and engineering effort to optimize, host, and maintain as a cost of self-hosting, though it notes this can be mitigated by using model hosting services.

### Question 77: Which statement about functionality is consistent with the source?

Which statement about functionality is consistent with the source?

- [ ] A) Model APIs are less likely to expose logprobs, while self-hosted models can access logprobs and intermediate outputs
- [ ] B) Self-hosted models are more likely to support function calling and structured outputs
- [ ] C) Model APIs have no support for scaling
- [ ] D) Self-hosted models always outperform commercial models

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** A

    **Explanation:** The table says model APIs are less likely to expose logprobs, while self-hosting can access logprobs and intermediate outputs, which are helpful for classification, evaluation, and interpretability.

### Question 78: What does the section "Using model APIs" focus on?

What does the section "Using model APIs" focus on?

- [ ] A) Training a model from scratch on a custom dataset
- [ ] B) Accessing models through provider APIs
- [ ] C) Designing the user interface of an AI product
- [ ] D) Writing evaluation datasets by hand

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** The section is titled "Using model APIs," indicating its focus is on working with models through APIs.

### Question 79: In the chapter's evaluation workflow, "Using model APIs" refers to...

In the chapter's evaluation workflow, "Using model APIs" refers to which way of working with models?

- [ ] A) Calling models through an API interface
- [ ] B) Compiling models into static binaries
- [ ] C) Replacing benchmarks with manual review
- [ ] D) Avoiding model providers entirely

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** A

    **Explanation:** The section heading names model APIs as the means of use, i.e., interacting with models via an API.

### Question 80: According to the text, what can help you decide whether to use a co...

According to the text, what can help you decide whether to use a commercial API or host a model yourself?

- [ ] A) The pros and cons of each approach
- [ ] B) The number of public benchmarks available
- [ ] C) The size of the model’s training dataset
- [ ] D) The programming language used for the API

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** A

    **Explanation:** The text says the pros and cons of each approach can help you decide between a commercial API and self-hosting.

### Question 81: After deciding whether to use a commercial API or self-host a model...

After deciding whether to use a commercial API or self-host a model, what does the text suggest using to further refine your selection?

- [ ] A) Publicly available model performance data
- [ ] B) Only internal user feedback
- [ ] C) The model’s license length
- [ ] D) The number of API endpoints

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** A

    **Explanation:** The text states that next you can further refine your selection using publicly available model performance data.

### Question 82: What does the text mention as a constraint related to edge use cases?

What does the text mention as a constraint related to edge use cases?

- [ ] A) Whether the model can run on device
- [ ] B) Whether the model uses a commercial API
- [ ] C) Whether the model has public benchmarks
- [ ] D) Whether the model API is self-hosted

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** A

    **Explanation:** The text lists edge use cases in terms of models that can’t run on device or can run on device but may be hard to access without internet.

### Question 83: According to the text, how many benchmarks does Google's BIG-bench...

According to the text, how many benchmarks does Google's BIG-bench (2022) contain?

- [ ] A) 214
- [ ] B) 400
- [ ] C) 500
- [ ] D) 1,000

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** A

    **Explanation:** The text states that Google's BIG-bench (2022) alone has 214 benchmarks.

### Question 84: What does the text identify as a tool that helps you evaluate a mod...

What does the text identify as a tool that helps you evaluate a model on multiple benchmarks?

- [ ] A) A benchmark registry
- [ ] B) An evaluation harness
- [ ] C) A saturation index
- [ ] D) A capability matrix

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** The text explicitly defines an evaluation harness as a tool that helps you evaluate a model on multiple benchmarks.

### Question 85: As of this writing, approximately how many existing benchmarks does...

As of this writing, approximately how many existing benchmarks does OpenAI's evals let you run?

- [ ] A) Over 400
- [ ] B) 214
- [ ] C) About 500
- [ ] D) Over 1,000

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** C

    **Explanation:** The text says OpenAI's evals lets you run any of the approximately 500 existing benchmarks, while over 400 refers to EleutherAI's lm-evaluation-harness.

### Question 86: Why does the text say old benchmarks saturate?

Why does the text say old benchmarks saturate?

- [ ] A) Because they are too expensive to run
- [ ] B) Because AI models improve, necessitating new benchmarks
- [ ] C) Because evaluation harnesses cannot support them
- [ ] D) Because they cover too many use cases

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** The text states that as AI models improve, old benchmarks saturate, necessitating the introduction of new benchmarks.

### Question 87: What does aggregating benchmark results to rank models give you?

What does aggregating benchmark results to rank models give you?

- [ ] A) A leaderboard
- [ ] B) A training dataset
- [ ] C) A toxicity score only
- [ ] D) A guarantee that one model is best for every use case

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** A

    **Explanation:** The source states that aggregating benchmark results to rank models gives you a leaderboard.

### Question 88: According to the source, what are the two questions to consider whe...

According to the source, what are the two questions to consider when creating a leaderboard from benchmarks?

- [ ] A) What benchmarks to include, and how to aggregate their results to rank models
- [ ] B) How to train models, and how to deploy them
- [ ] C) How to reduce toxicity, and how to increase coding speed
- [ ] D) How many models to discard, and how many benchmarks to ignore

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** A

    **Explanation:** The source lists these two questions: what benchmarks to include in your leaderboard, and how to aggregate these benchmark results to rank models.

### Question 89: What does the example of Model A performing better on a coding benc...

What does the example of Model A performing better on a coding benchmark but worse on a toxicity benchmark illustrate?

- [ ] A) Choosing between models can be difficult when benchmark results conflict
- [ ] B) Model A is always the better choice
- [ ] C) Toxicity benchmarks are the only benchmarks that matter
- [ ] D) Coding benchmarks should never be used

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** A

    **Explanation:** The source uses this example to show the difficulty of deciding which model to choose when one model performs better on one benchmark but worse on another.

### Question 90: For inspiration on how to create your own leaderboard from public b...

For inspiration on how to create your own leaderboard from public benchmarks, what does the source suggest?

- [ ] A) Looking into how public leaderboards create theirs
- [ ] B) Ignoring all public benchmarks
- [ ] C) Using only one benchmark for every use case
- [ ] D) Avoiding aggregation entirely

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** A

    **Explanation:** The source says it is useful to look into how public leaderboards create their own leaderboards from public benchmarks.

### Question 91: Why did HELM Lite leave out an information retrieval benchmark such...

Why did HELM Lite leave out an information retrieval benchmark such as MS MARCO?

- [ ] A) Because it is expensive to run
- [ ] B) Because it is not relevant to language models
- [ ] C) Because it is too easy for foundation models
- [ ] D) Because its results are not public

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** A

    **Explanation:** The source says HELM Lite left out MS MARCO because it is expensive to run.

### Question 92: Why did Hugging Face opt out of HumanEval when developing its leade...

Why did Hugging Face opt out of HumanEval when developing its leaderboard?

- [ ] A) Because HumanEval measures only medical knowledge
- [ ] B) Because it requires generating a lot of completions and has large compute requirements
- [ ] C) Because it was already fully covered by MMLU
- [ ] D) Because it is not used by any public leaderboard

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** The source states Hugging Face opted out of HumanEval due to its large compute requirements, needing to generate many completions.

### Question 93: In late 2023, which two benchmarks were used by both Hugging Face’s...

In late 2023, which two benchmarks were used by both Hugging Face’s Open LLM Leaderboard and Stanford’s HELM Leaderboard?

- [ ] A) ARC-C and HellaSwag
- [ ] B) TruthfulQA and WinoGrande
- [ ] C) MMLU and GSM-8K
- [ ] D) LegalBench and MedQA

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** C

    **Explanation:** The source says HELM used ten benchmarks, only two of which—MMLU and GSM-8K—were in the Hugging Face leaderboard.

### Question 94: Why is benchmark correlation important when selecting benchmarks?

Why is benchmark correlation important when selecting benchmarks?

- [ ] A) If two benchmarks are perfectly correlated, you don’t want both, and strongly correlated benchmarks can exaggerate biases
- [ ] B) Correlated benchmarks always make leaderboards cheaper to run
- [ ] C) Correlated benchmarks are required to compare different leaderboards
- [ ] D) Correlated benchmarks eliminate the need for public leaderboards

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** A

    **Explanation:** The source says that if two benchmarks are perfectly correlated, you don’t want both, and strongly correlated benchmarks can exaggerate biases.

### Question 95: According to the source, in June 2024 Hugging Face updated its lead...

According to the source, in June 2024 Hugging Face updated its leaderboard and replaced GSM-8K with which benchmark?

- [ ] A) MMLU-PRO
- [ ] B) MATH lvl 5
- [ ] C) GPQA
- [ ] D) BBH

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** The source states that GSM-8K was replaced by MATH lvl 5, which consists of the most challenging questions from the competitive math benchmark MATH.

### Question 96: The source notes that TruthfulQA is only moderately correlated with...

The source notes that TruthfulQA is only moderately correlated with the other leaderboard benchmarks. What does this suggest?

- [ ] A) Improving reasoning and math capabilities always improves truthfulness
- [ ] B) Truthfulness scores are perfectly correlated with MMLU
- [ ] C) Improving a model’s reasoning and math capabilities doesn’t always improve its truthfulness
- [ ] D) TruthfulQA is strongly correlated with ARC-C and WinoGrande

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** C

    **Explanation:** The source says TruthfulQA is only moderately correlated to other benchmarks, suggesting that improving a model’s reasoning and math capabilities doesn’t always improve its truthfulness.

### Question 97: How do HELM authors aggregate benchmark results instead of averaging?

How do HELM authors aggregate benchmark results instead of averaging?

- [ ] A) They use mean win rate: the fraction of times a model obtains a better score than another model, averaged across scenarios
- [ ] B) They give truthfulness double weight
- [ ] C) They use only code generation benchmarks
- [ ] D) They rank models by GSM-8K alone

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** A

    **Explanation:** The source says HELM authors shun averaging in favor of mean win rate, defined as the fraction of times a model obtains a better score than another model, averaged across scenarios.

### Question 98: What does the source say is the goal of evaluating models using pub...

What does the source say is the goal of evaluating models using public benchmarks?

- [ ] A) To pick the single overall best model and deploy it immediately
- [ ] B) To select a small subset of models for more rigorous experiments using your own benchmarks and metrics
- [ ] C) To avoid running any custom evaluation
- [ ] D) To determine whether OpenAI models are getting worse

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** The source states the goal is to select a small subset of models to do more rigorous experiments using your own benchmarks and metrics, since public benchmarks may not represent your application’s needs and are likely contaminated.

### Question 99: What is data contamination?

What is data contamination?

- [ ] A) When a model is evaluated on data it was never trained on
- [ ] B) When a model was trained on the same data it's evaluated on
- [ ] C) When a model's training data is deleted before evaluation
- [ ] D) When a benchmark is updated after a model is trained

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** Data contamination occurs when a model is trained on the same data it's evaluated on, so it may memorize answers and score higher than it should.

### Question 100: Why can data contamination inflate a model's benchmark scores?

Why can data contamination inflate a model's benchmark scores?

- [ ] A) The model may memorize answers it saw during training
- [ ] B) The benchmark questions are made easier over time
- [ ] C) The model receives more compute during evaluation
- [ ] D) The evaluation set is smaller than the training set

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** A

    **Explanation:** If the model saw the evaluation answers during training, it can memorize them, causing higher evaluation scores than it should.

### Question 101: What did Rylan Schaeffer's 2023 satirical paper "Pretraining on the...

What did Rylan Schaeffer's 2023 satirical paper "Pretraining on the Test Set Is All You Need" demonstrate?

- [ ] A) That larger models always outperform smaller models on benchmarks
- [ ] B) That training exclusively on benchmark data let a one-million-parameter model achieve near-perfect scores and outperform much larger models
- [ ] C) That MMLU is the only benchmark resistant to contamination
- [ ] D) That data contamination cannot affect evaluation results

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** Schaeffer trained exclusively on data from several benchmarks, and his one-million-parameter model achieved near-perfect scores and outperformed much larger models on all these benchmarks.

### Question 102: A model trained on the MMLU benchmark can achieve high MMLU scores...

A model trained on the MMLU benchmark can achieve high MMLU scores without being useful. What does this illustrate?

- [ ] A) That MMLU is an invalid benchmark for all purposes
- [ ] B) That high benchmark scores can result from data contamination rather than genuine capability
- [ ] C) That smaller models are always better than larger models
- [ ] D) That benchmarks should never be used to evaluate models

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** The source uses this example to show that contamination lets a model score highly by memorization without actually being useful.

### Question 103: According to the source, most data contamination is:

According to the source, most data contamination is:

- [ ] A) intentional and meant to mislead
- [ ] B) unintentional
- [ ] C) caused by benchmark creators
- [ ] D) limited to math benchmarks

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** The source says some might intentionally train on benchmark data, but most data contamination is unintentional.

### Question 104: Why do existing benchmarks become saturated quickly?

Why do existing benchmarks become saturated quickly?

- [ ] A) Benchmark data published before a model’s training is likely included in the model’s training data.
- [ ] B) Models are trained only on private benchmark data.
- [ ] C) Benchmark creators stop updating benchmarks.
- [ ] D) Users refuse to evaluate models on benchmarks.

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** A

    **Explanation:** The source states that benchmark data published before training is likely included in the model’s training data, which is one reason benchmarks become saturated quickly.

### Question 105: Which situation is an example of indirect data contamination?

Which situation is an example of indirect data contamination?

- [ ] A) Intentionally training a model on benchmark data before release
- [ ] B) Using math textbooks in training data while someone else uses questions from the same textbooks to create a benchmark
- [ ] C) Excluding benchmark data from training data
- [ ] D) Creating a new benchmark for a new model

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** The source describes indirect contamination as happening when evaluation and training data come from the same source, such as math textbooks.

### Question 106: According to the text, what does the prevalence of data contaminati...

According to the text, what does the prevalence of data contamination undermine?

- [ ] A) The speed of model training
- [ ] B) The trustworthiness of evaluation benchmarks
- [ ] C) The size of training datasets
- [ ] D) The cost of running evaluations

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** The text states that the prevalence of data contamination undermines the trustworthiness of evaluation benchmarks.

### Question 107: Why might a model's high score on a bar exam be misleading, accordi...

Why might a model's high score on a bar exam be misleading, according to the text?

- [ ] A) Bar exams are too easy to measure legal ability
- [ ] B) The model may have been trained on many bar exam questions
- [ ] C) Bar exams do not test legal knowledge
- [ ] D) The model may have been trained only on legal advice

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** The text warns that high bar exam performance could simply mean the model was trained on many bar exam questions, not that it gives good legal advice.

### Question 108: What two steps does the text say are needed to deal with data conta...

What two steps does the text say are needed to deal with data contamination?

- [ ] A) First decontaminate the data, then detect contamination
- [ ] B) First detect the contamination, then decontaminate your data
- [ ] C) First retrain the model, then re-evaluate it
- [ ] D) First collect new data, then discard the old data

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** The text states that to deal with data contamination, you first need to detect the contamination and then decontaminate your data.

### Question 109: Which heuristics does the text mention for detecting data contamina...

Which heuristics does the text mention for detecting data contamination?

- [ ] A) Accuracy and F1 score
- [ ] B) N-gram overlapping and perplexity
- [ ] C) Precision and recall
- [ ] D) Latency and throughput

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** The text says contamination can be detected using heuristics like n-gram overlapping and perplexity.

### Question 110: In the context of N-gram overlapping, when is an evaluation sample...

In the context of N-gram overlapping, when is an evaluation sample considered dirty?

- [ ] A) When it contains fewer than 13 tokens
- [ ] B) When a sequence of tokens in the evaluation sample is also in the training data
- [ ] C) When it is evaluated by more than one benchmark
- [ ] D) When it has no overlapping tokens with the training data

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** The source states that if a sequence of tokens in an evaluation sample is also in the training data, the evaluation sample is considered dirty.

### Question 111: If a sequence of 13 tokens in an evaluation sample is also in the t...

If a sequence of 13 tokens in an evaluation sample is also in the training data, what does this suggest?

- [ ] A) The model has likely seen this evaluation sample during training
- [ ] B) The evaluation sample is too short to be valid
- [ ] C) The benchmark cannot be used publicly
- [ ] D) The model has never encountered the sample

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** A

    **Explanation:** The source says that if a sequence of 13 tokens in an evaluation sample is also in the training data, the model has likely seen this evaluation sample during training.

### Question 112: What is the example sequence length used in the source to illustrat...

What is the example sequence length used in the source to illustrate N-gram overlapping?

- [ ] A) 5 tokens
- [ ] B) 10 tokens
- [ ] C) 13 tokens
- [ ] D) 20 tokens

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** C

    **Explanation:** The source uses an example of a sequence of 13 tokens in an evaluation sample that is also in the training data.

### Question 113: According to the source, what might unusually low perplexity on eva...

According to the source, what might unusually low perplexity on evaluation data suggest?

- [ ] A) The benchmark is too easy for all models
- [ ] B) The model may have seen the evaluation data during training
- [ ] C) The model has been over-regularized
- [ ] D) The evaluation data contains too many n-grams

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** The source says low perplexity means the model can easily predict the text, so it may have seen this data before during training.

### Question 114: How does the n-gram overlapping approach compare with the perplexit...

How does the n-gram overlapping approach compare with the perplexity approach for detecting data contamination?

- [ ] A) It is less accurate but much less resource-intensive
- [ ] B) It is more accurate but time-consuming and expensive, and requires access to training data
- [ ] C) It is equally accurate and requires no training data
- [ ] D) It is only useful for benchmarks created after training

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** The source states n-gram overlapping is more accurate but can be time-consuming and expensive, and is impossible without access to training data.

### Question 115: What limitation of public benchmarks does the source emphasize?

What limitation of public benchmarks does the source emphasize?

- [ ] A) They can find the best model for your application but cannot filter bad models
- [ ] B) They help filter out bad models but won’t help you find the best models for your application
- [ ] C) They always remove all contaminated samples automatically
- [ ] D) They eliminate the need for a custom evaluation pipeline

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** The source says public benchmarks help filter out bad models but won’t help find the best models, so you still need your own evaluation pipeline.

### Question 116: What did OpenAI find when analyzing GPT-3’s contamination with comm...

What did OpenAI find when analyzing GPT-3’s contamination with common benchmarks?

- [ ] A) No benchmark had more than 1% of its data in training
- [ ] B) 13 benchmarks had at least 40% of their data in the training data
- [ ] C) All benchmarks were completely clean
- [ ] D) Perplexity detected every contaminated sample

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** The source states OpenAI found 13 benchmarks with at least 40% in the training data when analyzing GPT-3’s contamination.

### Question 117: According to the source text, what type of tasks does this section...

According to the source text, what type of tasks does this section focus on evaluating?

- [ ] A) Close-ended tasks only
- [ ] B) Open-ended tasks
- [ ] C) Only tasks with a single component
- [ ] D) Only tasks completed in one turn

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** The text states that the section focuses on evaluating open-ended tasks, while close-ended tasks are easier and their pipeline can be inferred.

### Question 118: In Step 1, what should you evaluate in a real-world AI application?

In Step 1, what should you evaluate in a real-world AI application?

- [ ] A) Only the final end-to-end output
- [ ] B) Only the first component’s output
- [ ] C) The end-to-end output and each component’s intermediate output independently
- [ ] D) Only the outputs from tasks that take many turns

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** C

    **Explanation:** Step 1 says you should evaluate the end-to-end output and each component’s intermediate output independently.

### Question 119: In the resume PDF example, what is the first step in the application?

In the resume PDF example, what is the first step in the application?

- [ ] A) Extract the current employer from the extracted text
- [ ] B) Extract all the text from the PDF
- [ ] C) Evaluate the end-to-end output
- [ ] D) Evaluate each intermediate output independently

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** The example lists extracting all the text from the PDF as step 1, followed by extracting the current employer from the extracted text.

### Question 120: According to the source, why should you evaluate the end-to-end out...

According to the source, why should you evaluate the end-to-end output and each component’s intermediate output independently?

- [ ] A) To reduce the number of evaluation methods needed for close-ended tasks
- [ ] B) To determine exactly where the system fails when the final output is wrong
- [ ] C) To ensure the application always completes a task in fewer turns
- [ ] D) To avoid evaluating the application per turn and per task

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** The source says that if a model fails to extract the right employer, either step could be responsible, and without independent component evaluation you don’t know where the system fails.

### Question 121: In the source, what is the difference between turn-based evaluation...

In the source, what is the difference between turn-based evaluation and task-based evaluation?

- [ ] A) Turn-based evaluation checks whether a system completes a task, while task-based evaluation checks the quality of each output
- [ ] B) Turn-based evaluation evaluates the quality of each output, while task-based evaluation evaluates whether a system completes a task
- [ ] C) Turn-based evaluation applies only to PDF extraction, while task-based evaluation applies only to chatbots
- [ ] D) Turn-based evaluation is more important than task-based evaluation because users care about individual outputs

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** The source defines turn-based evaluation as evaluating the quality of each output and task-based evaluation as evaluating whether a system completes a task.

### Question 122: What does the source say about the importance and challenge of task...

What does the source say about the importance and challenge of task-based evaluation?

- [ ] A) It is less important than turn-based evaluation, and its main challenge is that it cannot measure how many turns a task takes
- [ ] B) It is more important because users care about accomplishing tasks, but task boundaries can be hard to determine
- [ ] C) It is equally important to turn-based evaluation, and its main challenge is that models can only answer yes or no
- [ ] D) It is more important because tasks are always clearly separated in a conversation

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** The source states that task-based evaluation is more important because users care about whether a model helps them accomplish tasks, but determining boundaries between tasks can be hard.

### Question 123: In the `twenty_questions` benchmark described in the source, how is...

In the `twenty_questions` benchmark described in the source, how is the score determined?

- [ ] A) By whether Alice successfully chooses a concept and how many concepts she can list
- [ ] B) By whether Bob successfully guesses the concept and how many questions it takes Bob to guess it
- [ ] C) By whether Alice answers with more than yes or no and how quickly Bob responds
- [ ] D) By whether the model extracts text from a PDF and how similar the text is to ground truth

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** The source says Alice chooses a concept and answers only yes or no, while Bob asks questions, and the score is based on whether Bob guesses the concept and how many questions it takes.

### Question 124: According to the text, what is the most important step of the evalu...

According to the text, what is the most important step of the evaluation pipeline?

- [ ] A) Creating a clear evaluation guideline
- [ ] B) Choosing a binary scoring system
- [ ] C) Generating multiple responses with AI models
- [ ] D) Mapping evaluation metrics to business metrics

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** A

    **Explanation:** The text states that creating a clear evaluation guideline is the most important step, because an ambiguous guideline leads to ambiguous and misleading scores.

### Question 125: The LinkedIn example where “You are a terrible fit” might be correc...

The LinkedIn example where “You are a terrible fit” might be correct but not helpful illustrates which point?

- [ ] A) A correct response is not always a good response.
- [ ] B) Factual consistency is the only evaluation criterion.
- [ ] C) Safety should always use a 1-to-5 scoring system.
- [ ] D) Out-of-scope inputs should be ignored.

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** A

    **Explanation:** The text uses this example to show that a response can be correct yet still bad because it is not helpful, so a good response should explain the gap and how to close it.

### Question 126: For a customer support application, the text gives an example of a...

For a customer support application, the text gives an example of a good response defined using which three criteria?

- [ ] A) Relevance, factual consistency, and safety
- [ ] B) Relevance, response length, and cost
- [ ] C) Factual consistency, toxicity, and speed
- [ ] D) Entailment, contradiction, and neutrality

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** A

    **Explanation:** The text lists relevance, factual consistency, and safety as an example of three criteria for defining a good customer support response.

### Question 127: What does the text recommend for creating scoring rubrics?

What does the text recommend for creating scoring rubrics?

- [ ] A) Create a rubric with examples and validate it with humans, refining it if humans find it hard to follow
- [ ] B) Use only binary scoring because other systems are always ambiguous
- [ ] C) Avoid examples so that evaluators are not influenced by specific cases
- [ ] D) Rely only on AI models to validate the rubric without human review

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** A

    **Explanation:** The text says to create a rubric with examples, validate it with humans, and refine it to make it unambiguous if humans find it hard to follow.

### Question 128: According to the source, what is the “usefulness threshold”?

According to the source, what is the “usefulness threshold”?

- [ ] A) The maximum cost an evaluation pipeline can add before it is no longer useful
- [ ] B) The score an application must achieve for it to be useful
- [ ] C) The number of human evaluators needed to label production data
- [ ] D) The minimum number of examples required in every evaluation set

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** The source defines the usefulness threshold as the scores an application must achieve to be useful, such as a chatbot needing at least 50% factual consistency.

### Question 129: What example does the source give for mixing and matching evaluatio...

What example does the source give for mixing and matching evaluation methods for the same criteria?

- [ ] A) Using only an expensive AI judge on all data to maximize quality
- [ ] B) Using a cheap classifier on 100% of data and an expensive AI judge on 1% of data
- [ ] C) Using human evaluation only during experimentation and never in production
- [ ] D) Using logprobs instead of any scoring rubric

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** The source says you might use a cheap classifier for low-quality signals on all data and an expensive AI judge for high-quality signals on a small subset, keeping costs manageable.

### Question 130: When logprobs are available, what does the source say they can be u...

When logprobs are available, what does the source say they can be used for?

- [ ] A) Measuring how confident a model is about a generated token, especially for classification
- [ ] B) Guaranteeing that an AI judge has temperature set to 0
- [ ] C) Replacing all human evaluation in production
- [ ] D) Determining the business metrics a product should prioritize

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** A

    **Explanation:** The source says logprobs can measure model confidence about generated tokens, especially useful for classification, and can also evaluate perplexity for generated text.

### Question 131: What rough rule does the source cite from OpenAI about evaluation s...

What rough rule does the source cite from OpenAI about evaluation sample size?

- [ ] A) For every 3× decrease in score difference, the number of samples needed increases 10×
- [ ] B) For every 10× decrease in score difference, the number of samples needed increases 3×
- [ ] C) A fixed evaluation set of 100 examples is always sufficient
- [ ] D) Sample size only matters for human evaluation, not automatic metrics

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** A

    **Explanation:** The source states that for every 3× decrease in score difference, the number of samples needed increases 10×, based on OpenAI’s rough estimation table.

### Question 132: According to the summary, what is described as one of the biggest b...

According to the summary, what is described as one of the biggest blocks to AI adoption?

- [ ] A) Not having a reliable evaluation pipeline
- [ ] B) Having too many foundation models available
- [ ] C) Using public leaderboards for model selection
- [ ] D) Relying on user feedback in production

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** A

    **Explanation:** The summary states that not having a reliable evaluation pipeline is one of the biggest blocks to AI adoption.

### Question 133: What does the chapter say public benchmarks can and cannot do?

What does the chapter say public benchmarks can and cannot do?

- [ ] A) They can identify the best model for your application but cannot weed out bad models.
- [ ] B) They can help weed out bad models but will not help you find the best models for your applications.
- [ ] C) They can replace private leaderboards but cannot be used for model selection.
- [ ] D) They can guarantee model safety but cannot measure generation capabilities.

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** The summary says public benchmarks can help weed out bad models, but they won’t help you find the best models for your applications.

### Question 134: When iterating on an evaluation pipeline, what should you log for p...

When iterating on an evaluation pipeline, what should you log for proper experiment tracking?

- [ ] A) Only the final evaluation scores and the model’s license
- [ ] B) Only the evaluation data and the model’s hosting cost
- [ ] C) All variables that could change, including evaluation data, rubric, and prompt and sampling configurations for AI judges
- [ ] D) Only the prompts used by the application, not the AI judges

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** C

    **Explanation:** The source says to log all variables that could change in an evaluation process, including evaluation data, rubric, and prompt and sampling configurations used for AI judges.

### Question 135: Why does the summary say no perfect evaluation method exists?

Why does the summary say no perfect evaluation method exists?

- [ ] A) Because public benchmarks are always sufficient for model selection
- [ ] B) Because it is impossible to capture a high-dimensional system’s ability using one- or few-dimensional scores
- [ ] C) Because evaluation pipelines do not need experiment tracking
- [ ] D) Because foundation models no longer require domain-specific evaluation

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** The summary states that it’s impossible to capture the ability of a high-dimensional system using one- or few-dimensional scores.
