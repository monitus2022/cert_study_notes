# 8. Dataset Engineering

---

## Dataset Engineering Basics
- Model quality depends on training data quality; infinite compute cannot fix poor data.
- Goal: create a dataset that trains the best model within your allocated budget.
- Fewer companies can afford from-scratch models, so more differentiate through data.
- Data operations became dedicated roles: data labelers, dataset creators, and data quality engineers.

---

## Curation Scope and Process
- Data curation asks: what data do you need, how much, and what is high quality?
- Curation, generation, and processing are not linear; expect to go back and forth.
- Different training phases need different data attributes: pre-training counts tokens, supervised finetuning counts examples.
- The chapter focuses on post-training data, which is more relevant to application developers.

---

## Data-Centric vs Model-Centric AI
- Model-centric AI improves performance by enhancing models: architectures, size, and training techniques.
- Data-centric AI improves performance by enhancing data processing and creating high-quality datasets.
- Benchmarks shifted from model-centric to data-centric: same model, better dataset.
- Andrew Ng's 2021 competition: fix incorrect labels, add edge cases, augment data.

---

## Data Curation: Overview

- Data-centric benchmarks like DataComp, DataPerf, and dcbench evaluate datasets by resulting model performance.
- Data curation requires understanding how the model learns and available resources.
- Dataset builders should work closely with application and model developers.
- Data needs depend on task: self-supervised needs sequences; instruction finetuning needs (instruction, response).

---

## Teaching Complex Behaviors

- Training data should exhibit the behaviors you want the model to learn.
- CoT data includes step-by-step responses; it greatly improves CoT task performance but is less common.
- Tool use data often uses domain experts, but observing tasks ensures accuracy over recalled steps.
- Human-efficient actions may not suit AI; simulations and synthetic techniques generate tool use data.

---

## Conversation Data and Unlearning

- Consider whether you need single-turn, multi-turn, or both types of conversation data.
- Single-turn data is simpler and easier to obtain; multi-turn data captures back-and-forth tasks.
- Curation also means removing data to help a model unlearn bad behaviors.
- Data curation follows three criteria: data quality, data coverage, and data quantity.

---

## Quality Over Quantity
- High-quality data can outperform large amounts of noisy, irrelevant, or inconsistent data.
- Yi creators found 10K carefully crafted instructions superior to hundreds of thousands of noisy instructions.
- LIMA: 65B Llama with 1,000 curated prompts/responses was equivalent or preferred to GPT-4 in 43% of human-judged cases.
- Too few examples reduce robustness; LIMA is less robust than product-grade models.

---

## What Makes Data High-Quality
- Data is high-quality if it helps you do your job efficiently and reliably.
- Six general characteristics: relevant, aligned with task requirements, consistent, correctly formatted, unique, compliant.
- Specific use cases may have additional requirements beyond these six characteristics.
- Llama 3 found human data error-prone for nuanced safety policies; AI-assisted annotation tools helped ensure quality.

---

## Quality Characteristics in Practice
- Relevant: training examples must match the task; a 19th-century legal dataset suits 19th-century law, not today’s legal questions.
- Aligned: annotations should match task requirements, such as factual correctness, creativity, justifications, or concise answers.
- Consistent: annotations should be consistent across examples and annotators; inconsistent annotations confuse the model.
- Correctly formatted and unique: remove redundant formatting tokens; duplications can introduce biases and data contamination.

---

## Data Coverage and Diversity
- Training data should cover the range of problems the model is expected to solve.
- Real users express problems differently, so data must capture diverse usage patterns.
- Coverage requires sufficient data diversity; many call this attribute data diversity.
- Finetuning data should include both detailed and short instructions if users use both.

---

## Diversity Depends on Application
- Different applications have different dimensions of diversity.
- A French-to-English tool may need topic, length, and speaking-style diversity.
- A global product chatbot may need linguistic and cultural diversity.
- General-purpose chatbots need diverse topics and speaking patterns in finetuning data.

---

## Llama 3 Data Mix
- Domain diversity is consistent across pre-training, supervised finetuning, and preference finetuning.
- Llama 3’s optimal domain mix differs by training phase.
- Post-training also has diversity axes such as token counts, turns, and human/AI-generated ratio.
- Meta used scaling law experiments to find an optimal data mix.

---

## How Much Data Do You Need?
- The answer varies widely: from a single example to millions of finetuned examples.
- Foundation models need far more: Llama 2 used 2 trillion tokens, Llama 3 16 trillion.
- With millions of examples, evaluate training from scratch; ossification can make finetuning worse.
- Smaller models are more susceptible to ossification than larger models.

---

## Factors That Shape Data Needs
- Full finetuning needs orders of magnitude more data than PEFT methods like LoRA.
- Simple tasks, such as sentiment classification, need far less data than complex tasks.
- The closer the base model is to desirable performance, the fewer examples needed.
- With 100 examples, advanced models perform better; with 550,000, all models perform similarly.

---

## Estimating and Stretching Your Data
- Start with a small, well-crafted dataset (e.g., 50 examples) before curating large data.
- Plot performance on 25%, 50%, and 100% subsets to estimate the gain slope.
- Gains typically diminish with size; task diversity also matters, plateauing beyond 282 tasks.
- Budget constrains quantity: $10,000 at $2 per example allows at most 5,000 examples.

---

## Data Acquisition Goals
- Goal: large, quality, diverse dataset while respecting user privacy and regulations.
- Methods include public data, purchasing proprietary data, annotation, and synthesis.
- Data acquisition strategy research: meet specific requirements given a budget.
- Own application data is ideal; a data flywheel matches your task distribution.

---

## Mix-and-Match Dataset Example
- Check available datasets first; marketplaces offer open source and proprietary data.
- Example: start with 10,000 examples; remove low-quality instructions, leaving 9,000.
- Set aside 3,000 low-quality responses, leaving 6,000; manually write responses to reach 9,000.
- Add 2,000 synthetic instructions from templates and annotate them, reaching 11,000.

---

## Annotation and Public Data Caution
- Annotation requires clear guidelines for both manual and AI-powered annotation.
- Guidelines must state what a good response is and score distinctions.
- LinkedIn reported annotation guidelines were among the most challenging pipeline parts.
- Public datasets: check licenses, inspect and validate; never fully trust data.

---

## Data Augmentation and Synthesis
- Data is among AI’s hardest challenges, alongside compute and talent.
- Industry has long sought to generate data programmatically.
- Data augmentation creates new data from existing real data.
- Data synthesis generates data to mimic properties of real data.

---

## Distinction and Usage
- Evaluation examples can be augmented or used as seeds to synthesize new data.
- Augmented data is derived from real data; synthetic data isn’t real.
- Example: flip a real cat image; simulate mouse movements for bot data.
- Terms are sometimes interchangeable; the chapter often uses synthesis for both.

---

## Data Synthesis: Background and Scale
- Synthetic data historically generated fake test data via libraries like Faker and Chance.
- AI can now synthesize sophisticated data: doctor’s notes, contracts, financial statements, images, video.
- Biggest reason: produce data at scale for training/testing, especially when real data is scarce.
- More data helps models generalize; examples include rare weather, deep sea, self-driving accidents.

---

## Improving Coverage and Quality
- Generate targeted characteristics: short/long texts, toxic phrases, adversarial examples, rare classes.
- Anthropic generated datasets for 154 behaviors; LM-written datasets approach human quality.
- AI can generate complex math problems beyond average human expert; tool-use data differs.
- AI preference ratings can be more consistent and reliable than varied human ratings.

---

## Privacy, Distillation, and Limits
- Synthetic data mitigates privacy: healthcare patient records and insurance claims without sensitive information.
- Distill models: train cheaper/faster model on data generated by original model.
- Synthetic data doesn’t fully replace human data; mixing often produces best value.

---

## Traditional Data Synthesis: Rule-Based
- Procedural generation uses algorithms to create data, unlike manual generation; common in gaming, testing, robotics.
- Templates with random generators (e.g., Faker) populate fields like transaction ID, date, amount, merchant.
- Synthetic transaction data trains fraud detection models before granting access to sensitive real data.
- Templates generate structured documents, grammars, and math equations (AlphaGeometry used 100 million synthetic examples).

---

## Transformations, Bias Mitigation, and Perturbation
- Simple transformations: rotate, crop, scale, or erase images; replace words with similar ones in text.
- Augmentation can mitigate bias by swapping gendered words, as shown in Table 8-2.
- Perturbation adds noise to data; one-pixel attacks misclassified 67.97% of CIFAR-10 test images.
- Training on perturbed data improves performance and robustness; BERT replaced 1.5% of tokens with random words.

---

## Simulation
- Simulations replace expensive or dangerous real-world experiments, e.g., self-driving car encountering a horse.
- Robotics training simulates scenarios (like pouring coffee) and uses only successful runs as training data.
- Simulations generate data for rare events: IPOs, bankruptcies, material defects, extreme weather scenarios.
- Sim2Real adapts simulation-trained algorithms to the real world; simulations remain simplifications of reality.

---

## Simulation and Self-Play
- AI can simulate outcomes of arbitrary programs, e.g. StableToolBench simulates APIs without evoking them.
- AI can simulate humans: OpenAI's Dota 2 bot played ~180 years of games daily.
- The bot learned via self-play, refining strategies over time; DeepMind used self-play for AlphaGo.
- Self-play also suits general agents: negotiating AIs, or customer versus support-agent roles.

---

## Paraphrasing and Translation
- AI can paraphrase queries, e.g. "How to reset my password?" into three new queries.
- MetaMath: 15,000 MATH and GSM-8K examples rewritten into almost 400,000 examples.
- Models trained on MetaMath outperformed larger models on related math benchmarks.
- Back-translation checks quality: translate the translation back and compare with the original.

---

## Code, Pre-Training, and Post-Training
- AI translates programming languages; Llama 3 used code translation of its SFT dataset.
- Llama 3 used back-translation for code explanations, keeping only faithful regenerations.
- Synthetic data appears far more in post-training; synthesizing new knowledge for pre-training is harder.
- Cosmopedia is a 25-billion-token synthetic dataset generated by Mixtral-8x7B-Instruct-v0.1.

---

## Instruction Data Synthesis Basics

- AI can synthesize instructions, responses, or both; humans can supply the other half.
- Generate instructions from topic lists, keywords, instruction types, or templates; AI can create these too.
- UltraChat: ChatGPT generated 30 topics, then 30–50 subtopics each, then instructions and responses.
- Alpaca: 175 Self-Instruct seed examples expanded by text-davinci-003 into 52,000 instruction-response pairs.

---

## Reverse Instruction and Long Context

- Long AI-generated responses risk hallucination more than short instructions.
- Reverse instruction: take existing high-quality long-form content and use AI to generate prompts eliciting it.
- Iterative loop: train weak model, generate instructions for quality content, finetune, repeat.
- Long-context finetuning: chunk long documents, generate question-answer pairs, then use full document as context.

---

## Llama 3 Coding Data Pipeline

- Generate diverse programming problem descriptions, then solutions per language; rules and CoT improve quality.
- Validate with parsers, linters, and AI-generated unit tests; prompt model to fix failures.
- Translate and back-translate code, filtering outputs that fail tests or verification.
- Pipeline produced over 2.7 million synthetic coding examples for Llama 3.1 supervised finetuning.

---

## Verifying Synthetic Data Quality

- Synthetic data quality is measured like other AI outputs: functional correctness and AI judges
- Techniques apply broadly to evaluating training data, not just synthetic data
- People tend to synthesize data they can verify, echoing evaluation-driven development
- Coding is commonly synthesized because it can be functionally evaluated; most Llama 3 synthetic data is coding-related

---

## AI Verifiers and Creative Checks

- For data not verifiable by execution, use AI verifiers: general judges or specialized scorers
- Verifiers can score examples 1–5, classify good/bad, or check stated quality requirements
- Factual inconsistency detection techniques can filter likely hallucinations
- Creative options: AI content detectors, conference-acceptance classifiers, topic detection, anomaly detection

---

## Heuristics and the Ultimate Test

- Synthetic data can be filtered with heuristics like real data: remove empty, too short, or too long examples
- Filter by keywords, user/author, creation date, metadata, or source
- Self-Instruct filtered repetitive examples, extreme lengths, mismatched responses, and input-repeating outputs
- Ultimate quality test remains real-world performance: whether data improves the model

---

## Synthetic Data’s Growing but Bounded Role
- Synthetic data is increasingly useful, making human annotation seem avoidable.
- Its importance will continue to grow over time.
- Yet AI-generated data might never entirely replace human-generated data.
- Four major limitations explain why replacement is unlikely.

---

## The Four Major Limitations
- **Quality difference**: AI-generated data differs in quality from human-generated data.
- **Limitations of imitation**: generation is constrained by imitating existing data.
- **Potential model collapse**: a risk associated with AI-generated data.
- **Obscured lineage**: AI generation makes the origin of data harder to trace.

---

## Quality Control for Synthetic Data
- AI-generated data can be of low quality.
- “Garbage in, garbage out” applies to synthetic data.
- Low-quality generated data limits its usefulness.

---

## Verifying Synthetic Data
- People hesitate to use synthetic data they cannot verify.
- Reliable methods to evaluate data are essential.
- Reliable metrics are essential to make synthetic data more useful.

---

## AI-Powered Data Synthesis: Superficial Imitation

- Imitation models may achieve only superficial performance by mimicking teacher style.
- "The False Promise of Imitating Proprietary LLMs" (Gudibande et al., 2023) warns of this risk.
- Imitating models can struggle with factual accuracy and generalization beyond training data.
- Imitation can even force the student model to hallucinate.

---

## How Imitation Teaches Hallucination

- A teacher capable of complex math produces solution-like responses.
- Training a student on these solutions teaches it to produce answers that look like solutions.
- The student may not actually be capable of solving the questions.
- The result is answers that imitate form without underlying reasoning.

---

## Improving Reasoning Requires Better Base Models

- Gudibande et al. (2023) suggest focusing on base model quality.
- Improvements in reasoning capabilities need stronger base models, not just imitation.
- Imitation alone is insufficient for genuine capability gains.

---

## Potential Model Collapse
- Shumailov et al. (2023) named *model collapse*: recursively training on generated data causes irreversible defects.
- Demonstrated in Variational Autoencoders, Gaussian mixture models, and LLMs; occurs in pre-training and post-training.
- Cause: models over-generate probable events and under-represent improbable ones, so rare events are forgotten.
- Gerstgrasser et al. (2024): collapse is inevitable with fully synthetic data, avoidable by mixing real data.

---

## Mixing, Scale, and Caveats
- Bertrand et al. (2023) and Dohmatob et al. (2024) report similar results; no definitive synthetic-to-real proportion is recommended.
- Li et al. (2024): synthetic data nearly as effective as real for finetuning Llama 2-7B on math.
- Synthetic data showed no clear saturation when scaled to roughly one million samples.
- Nemotron-4 340B-Instruct used 98% synthetic data for instruction and preference finetuning.

---

## Bias Amplification
- Taori and Hashimoto (2023): training on datasets containing previous model outputs can amplify existing biases.
- The more faithful outputs are to the original training distribution, the more stable the feedback loop.
- A stable feedback loop minimizes the risk of bias amplification.
- Large-synthetic-data successes were tested for only one model iteration.

---

## Obscure Data Lineage

- AI generation obscures data lineage: models can regurgitate training data without users knowing.
- Using model X to generate training data can propagate model X's copyright violations.
- If model X was trained on benchmark B, your model's score on B is contaminated.
- Without clear lineage, assessing commercial viability or trusting performance is hard.

---

## Risks of AI-Generated Data

- Data lineage risk is a subtle limitation of AI-powered data synthesis.
- Models are influenced by their training data and may reproduce it unknowingly.
- Contaminated benchmarks can inflate apparent performance misleadingly.
- Copyright and evaluation contamination both stem from unclear data provenance.

---

## Seed and Generated Tasks

- AI synthesis can create tasks from seed examples, as in Alpaca training.
- Figure 8-5 shows a seed task alongside its generated counterpart.
- Generated tasks expand training data, but lineage remains a concern.

---

## Model Distillation
- Model distillation (knowledge distillation) trains a small student model to mimic a larger teacher model.
- Traditionally used to produce smaller, faster models for deployment while retaining comparable performance.
- DistilBERT reduces BERT size by 40%, retains 97% language comprehension, and is 60% faster.
- Student can be trained from scratch (DistilBERT) or finetuned from a pre-trained model (Alpaca).

---

## Examples and Licensing
- Alpaca finetuned Llama-7B on text-davinci-003 outputs; it behaves similarly while being 4% the teacher's size.
- Not all models can be distilled; many licenses prohibit using outputs to train other models, especially competitors.
- Synthetic instruction data is often used with adapter-based techniques like LoRA.
- BuzzFeed finetuned Flan-T5 with LoRA on text-davinci-003 examples, reducing inference cost by 80%.

---

## Distillation vs Synthetic Data
- Not all training with synthetic data is model distillation.
- Distillation implies the teacher model’s performance is the student’s gold standard.
- Synthetic data can train a student larger and more powerful than the teacher.
- Examples: model bootstrapping with reverse instruction; NVIDIA Nemotron-4 finetuned a 340B base model with Mixtral-8x7B-Instruct-v0.1 data.

---

## Synthetic Data: Promise and Pitfalls
- Nemotron-4-340B-Instruct, a student model, outperformed its teacher on a variety of tasks (NVIDIA, 2024)
- Llama 3 paper: training on data from a more competent model can significantly improve performance
- Training indiscriminately on self-generated data doesn't improve performance and can even degrade it
- Verifying synthetic data quality and using only verified data enabled continual improvement with generated data

---

## Data Processing and Paper Reading
- Data needs to be processed according to the requirements of each use case
- Processing steps vary by use case; the section offers steps for reference
- Model papers disclosing dataset details often contain useful tips on curation, generation, and processing
- Reading such papers is a helpful way to learn how researchers handled data

---

## Inspecting Raw Data
- First step after gathering raw data: inspect it to gauge quality.
- Ask where data comes from, how it was processed, what else it was used for.
- Plot distributions of tokens, input lengths, response lengths, and special tokens.
- Check topic and language distributions, and their relevance to your task.

---

## Creative Statistics and Model Comparison
- Be creative with statistics: Microsoft researchers (2023) used (verb, direct object, noun) pair distributions.
- They also compared response length for GPT-3 and GPT-4 on the same instructions.
- GPT-4 showed broader, more diverse verb-noun pairings and tended to generate longer responses.
- Such analysis helps evaluate data and also evaluate models.

---

## Slicing Distributions and Manual Inspection
- Plot distributions by data source, time, and annotator to spot patterns and outliers.
- Check whether scores follow a normal distribution per annotator; some bias high or write short.
- With multiple annotations per example, compute inter-annotator disagreement and resolve conflicts.
- Manual inspection is irreplaceable: staring at data for 15 minutes often saves hours.

---

## Deduplicate Data: Why It Matters

- Duplicated data can skew the data distribution and introduce biases into your model.
- In Table 8-3, duplicates might wrongly suggest all red-colored items are expensive.
- Duplications can cause test set contamination when splitting data into train and test sets.
- One example may land in the train set while its duplicate lands in the test set.

---

## Evidence of Harm from Duplication

- Studies show negative impact of training data duplications on model performance (Lee et al., 2021; Tirumala et al., 2023).
- Repeating 0.1% of data 100 times degraded an 800M parameter model to 400M-level performance (Hernandez et al., 2022).
- This occurred despite the other 90% of training tokens remaining unique.
- Even when duplications don't hurt performance, they waste time and compute.

---

## Types and Definitions of Duplication

- Whole document duplications: the same document appearing more than once.
- Intra-document duplications: e.g., the same paragraph appears twice in one document.
- Cross-document duplications: e.g., the same popular quote appears in multiple documents.
- Definition choices: document, paragraph, sentence, or token level; exact match vs. 80% overlap.

---

## Deduplication Techniques

- Pairwise comparison: compute similarity scores between every pair using exact, n-gram, fuzzy, or semantic match.
- Hashing: hash examples into buckets and compare only within the same bucket (MinHash, Bloom filter).
- Dimensionality reduction: reduce dimensions first, then do pairwise comparison.
- Libraries include dupeGuru, Dedupe, datasketch, TextDistance, TheFuzz, and deduplicate-text-datasets.

---

## Clean and Filter Data
- Clean data to make models performant and safe.
- Remove extraneous formatting tokens like HTML tags from scraped datasets.
- Databricks: removing Markdown/HTML tokens improved accuracy 20%, cut input tokens 60%.
- Strip anything non-compliant with policies: PII, sensitive, copyrighted, or toxic data.

---

## Removing Low-Quality Data
- Remove fields you're not allowed to use, such as zip code, name, and gender.
- Use data verification techniques to detect low-quality data.
- Manual inspection helps spot patterns usable as heuristics.
- Heuristics can be nonobvious: Kern et al. (2024) found second-half annotations lower quality, likely from fatigue.

---

## Format Data for Finetuning

- Each model expects a specific tokenizer and chat template; wrong templates cause strange bugs.
- Supervised finetuning data usually follows the (instruction, response) format.
- Instructions can decompose into (system prompt, user prompt).
- Finetuning instructions typically need no task descriptions or examples.

---

## From Prompting to Finetuning

- Multi-shot prompt examples can be converted into individual training examples.
- Food classification: prompts with burger, car, mushroom become input–output pairs.
- Finetuned model then accepts a simple prompt like `{INPUT}-->`.
- Shorter prompts help manage input token costs.

---

## Match Prompts to Training Format

- Different finetuning data formats can affect the finetuned model's performance.
- Run experiments to find the best format for your task.
- Prompts used with the finetuned model must match the finetuning data format.

---

## Dataset Design Principles
- Start by identifying behaviors to learn, then design dataset to demonstrate them.
- Data needs vary by use case and training phase: pre-training, instruction finetuning, preference finetuning.
- Across phases, dataset design shares three criteria: quality, coverage, quantity.
- High-quality data with sufficient coverage can matter as much as quantity.

---

## Synthetic Data and Hard Parts
- Synthetic data became practical when AI could create realistic, complex data for more use cases.
- Synthetic data must be evaluated for quality before training; reliable evaluation encourages use.
- Dataset creation remains hard to automate: annotation guidelines, verification, and attention to detail.
- Dataset design requires creativity; many construction and evaluation techniques can inspire practice.

## Practice Questions

### Question 1: According to the text, what is the goal of dataset engineering?

According to the text, what is the goal of dataset engineering?

- [ ] A) To design new model architectures that improve AI performance.
- [ ] B) To create a dataset that allows training the best model, ideally within the allocated budget.
- [ ] C) To reduce the number of data labelers and data quality engineers.
- [ ] D) To replace model-centric AI benchmarks with ImageNet.

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** The text states that the goal of dataset engineering is to create a dataset that allows you to train the best model, ideally within your allocated budget.

### Question 2: How does the source describe the evolution of data operations?

How does the source describe the evolution of data operations?

- [ ] A) They remain side tasks handled only when people have time.
- [ ] B) They have become dedicated roles such as data labelers, dataset creators, and data quality engineers.
- [ ] C) They are now entirely automated with no need for human roles.
- [ ] D) They are only performed by core engineering teams.

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** The text says data operations have evolved from side tasks to dedicated roles, and many AI companies now employ data labelers, dataset creators, and data quality engineers.

### Question 3: What distinguishes data-centric AI from model-centric AI according...

What distinguishes data-centric AI from model-centric AI according to the text?

- [ ] A) Data-centric AI improves AI by enhancing models, while model-centric AI improves data.
- [ ] B) Data-centric AI improves AI by enhancing data, while model-centric AI improves models.
- [ ] C) Both focus exclusively on increasing model size.
- [ ] D) Data-centric AI avoids using benchmarks like ImageNet.

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** The text defines model-centric AI as trying to improve AI performance by enhancing the models themselves, and data-centric AI as trying to improve AI performance by enhancing the data.

### Question 4: According to the text, how is data quantity typically measured for...

According to the text, how is data quantity typically measured for pre-training versus supervised finetuning?

- [ ] A) Pre-training by number of examples; finetuning by number of tokens.
- [ ] B) Pre-training by number of tokens; finetuning by number of examples.
- [ ] C) Both by number of tokens.
- [ ] D) Both by number of examples.

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** The text states that data quantity for pre-training is often measured in the number of tokens, whereas data quantity for supervised finetuning is often measured in the number of examples.

### Question 5: What was the goal of the 2023 DataComp competition?

What was the goal of the 2023 DataComp competition?

- [ ] A) To create the best dataset for training a CLIP model
- [ ] B) To evaluate datasets for language models from 412M to 7B parameters
- [ ] C) To benchmark data-centric algorithms like DataPerf and dcbench
- [ ] D) To train a reward model using preference data

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** A

    **Explanation:** The text states that DataComp hosted a competition whose goal was to create the best dataset for training a CLIP model.

### Question 6: According to the text, what data format is needed for preference fi...

According to the text, what data format is needed for preference finetuning?

- [ ] A) Sequences of data
- [ ] B) (instruction, response)
- [ ] C) (instruction, winning response, losing response)
- [ ] D) ((instruction, response), score)

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** C

    **Explanation:** The text specifies that for preference finetuning, you need data in the (instruction, winning response, losing response) format.

### Question 7: Why are chain-of-thought (CoT) datasets less common compared to oth...

Why are chain-of-thought (CoT) datasets less common compared to other instruction datasets?

- [ ] A) CoT data is only useful for math problems
- [ ] B) Generating multi-step responses is tedious and time-consuming
- [ ] C) Models cannot learn from CoT responses
- [ ] D) CoT data requires special multi-message chat formats

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** The text explains that generating multi-step responses can be tedious and time-consuming, making CoT datasets less common.

### Question 8: What are the three high-level criteria that data curation follows?

What are the three high-level criteria that data curation follows?

- [ ] A) Data quality, data coverage, and data quantity
- [ ] B) Single-turn data, multi-turn data, and tool use data
- [ ] C) Pretraining data, finetuning data, and preference data
- [ ] D) Model-centric, data-centric, and hybrid approaches

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** A

    **Explanation:** The text states that at a high level, data curation follows the three criteria: data quality, data coverage, and data quantity.

### Question 9: According to the source, what did the creators of the Yi model fami...

According to the source, what did the creators of the Yi model family find about instruction data?

- [ ] A) Hundreds of thousands of noisy instructions always outperform carefully crafted instructions.
- [ ] B) 10K carefully crafted instructions are superior to hundreds of thousands of noisy instructions.
- [ ] C) Data quality matters less than model size for instruction tuning.
- [ ] D) Human-generated instructions are always better than AI-assisted annotations.

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** The source states that the Yi model creators found 10K carefully crafted instructions superior to hundreds of thousands of noisy instructions.

### Question 10: What does the LIMA example show about finetuning data?

What does the LIMA example show about finetuning data?

- [ ] A) A 65B-parameter Llama model finetuned with 1,000 carefully curated prompts and responses can sometimes produce answers equivalent or preferred to GPT-4.
- [ ] B) A model finetuned with too few examples is always more robust than product-grade models.
- [ ] C) Noisy data is preferable because it improves robustness.
- [ ] D) 1,000 prompts and responses are enough to make any model product-grade.

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** A

    **Explanation:** The source says LIMA shows that 1,000 carefully curated prompts and responses can produce answers equivalent or strictly preferred to GPT-4 in 43% of cases, though it is not as robust as product-grade models.

### Question 11: Which set lists the six general characteristics of high-quality dat...

Which set lists the six general characteristics of high-quality data given in the source?

- [ ] A) Relevant, aligned with task requirements, consistent, correctly formatted, unique, and compliant.
- [ ] B) Large, noisy, inconsistent, redundant, creative, and confidential.
- [ ] C) Accurate, long, diverse, random, duplicated, and compliant.
- [ ] D) Relevant, anonymous, biased, formatted, duplicated, and creative.

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** A

    **Explanation:** The source says data can generally be considered high-quality if it is relevant, aligned with task requirements, consistent, correctly formatted, unique, and compliant.

### Question 12: Why does the source use the term “sufficiently unique” for training...

Why does the source use the term “sufficiently unique” for training data?

- [ ] A) Because all use cases require exactly zero duplication.
- [ ] B) Because duplications can introduce biases and cause data contamination, but different use cases can tolerate different levels of duplication.
- [ ] C) Because unique examples are irrelevant to model training.
- [ ] D) Because duplication always improves model learning and consistency.

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** The source explains that duplications can introduce biases and cause data contamination, while specific use cases can tolerate different levels of duplication.

### Question 13: According to the source text, what does data coverage require?

According to the source text, what does data coverage require?

- [ ] A) Sufficient data diversity
- [ ] B) The largest possible data volume
- [ ] C) Only human-generated data
- [ ] D) Only domain-specific data

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** A

    **Explanation:** The text states that coverage requires sufficient data diversity, which is why many refer to this attribute as data diversity.

### Question 14: Which statement best reflects the text’s discussion of diversity di...

Which statement best reflects the text’s discussion of diversity dimensions across applications?

- [ ] A) Every application needs exactly the same diversity axes.
- [ ] B) A French-to-English tool doesn’t need language diversity but might benefit from diversity in topics, lengths, and speaking styles.
- [ ] C) A global product recommender doesn’t need linguistic or cultural diversity.
- [ ] D) General-purpose chatbots need only domain diversity.

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** The text says different applications have different dimensions of diversity and gives the French-to-English tool as an example that doesn’t need language diversity but may benefit from topic, length, and speaking-style diversity.

### Question 15: How did Meta decide on the right data mix for Llama 3, according to...

How did Meta decide on the right data mix for Llama 3, according to the text?

- [ ] A) By using only real-world application usage logs
- [ ] B) By training several small models on candidate data mixes and using the results to predict large-model performance
- [ ] C) By adding as much heterogeneous data as possible
- [ ] D) By using only synthetic data

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** The text says Meta performed scaling law experiments: for each candidate data mix, they trained several small models and used that to predict the performance of a large model on that mix.

### Question 16: According to the source, which of the following is one of the three...

According to the source, which of the following is one of the three factors—besides data quality and data diversity—that influence how much finetuning data you need?

- [ ] A) The color scheme used in the training dashboard
- [ ] B) The finetuning technique, such as full finetuning versus PEFT methods like LoRA
- [ ] C) The number of GPUs available for inference only
- [ ] D) The programming language used to write the training script

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** The source lists finetuning techniques, task complexity, and base model performance as three factors influencing data quantity, and notes full finetuning requires orders of magnitude more data than PEFT methods like LoRA.

### Question 17: What does the source say about how base model size affects the numb...

What does the source say about how base model size affects the number of examples needed for finetuning?

- [ ] A) Bigger base models always need more finetuning examples, just as in pre-training.
- [ ] B) Base model size has no effect on finetuning data needs.
- [ ] C) Assuming bigger base models are better, you might need fewer examples to finetune big models, which is the opposite of pre-training.
- [ ] D) Smaller base models require fewer finetuning examples because they are less susceptible to ossification.

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** C

    **Explanation:** The source states that the closer the base model is to desirable performance, the fewer examples are needed, and that bigger models may need fewer examples for finetuning—the opposite of pre-training.

### Question 18: In OpenAI’s finetuning guide experiment described in the source, wh...

In OpenAI’s finetuning guide experiment described in the source, what happened with 100 examples versus 550,000 examples?

- [ ] A) With 100 examples, more advanced models gave much better performance after finetuning; with 550,000 examples, all five models performed similarly.
- [ ] B) With 100 examples, all models performed similarly; with 550,000 examples, only the smallest model improved.
- [ ] C) With 100 examples, smaller models performed best; with 550,000 examples, larger models performed far worse.
- [ ] D) The number of examples had no impact on finetuning performance for any model.

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** A

    **Explanation:** The source says that with 100 examples, more advanced models give better finetuning performance, but after finetuning on 550,000 examples, all five models in the experiment performed similarly.

### Question 19: The source describes a performance gain curve and notes that additi...

The source describes a performance gain curve and notes that additional training examples usually yield diminishing returns. What does a plateau slope in such a curve suggest?

- [ ] A) Doubling your data will give only a small improvement.
- [ ] B) Doubling your data will always double model performance.
- [ ] C) You should immediately switch from PEFT to full finetuning.
- [ ] D) The dataset has too much diversity and should be made less diverse.

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** A

    **Explanation:** The source states that a plateau slope means doubling your data will give only a small improvement, while a steep slope means you can expect significant improvement from doubling your data.

### Question 20: According to the text, what does data augmentation do?

According to the text, what does data augmentation do?

- [ ] A) It generates data that is not real to mimic real data properties.
- [ ] B) It creates new data from existing real data.
- [ ] C) It replaces evaluation guidelines with synthetic examples.
- [ ] D) It simulates bot movements through a web page.

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** The text defines data augmentation as creating new data from existing data, which is real.

### Question 21: Which example does the text give for data synthesis?

Which example does the text give for data synthesis?

- [ ] A) Flipping a real image of a cat to create a new image.
- [ ] B) Curating evaluation guidelines and data.
- [ ] C) Simulating how a mouse moves through a web page to generate bot-movement data.
- [ ] D) Using evaluation examples as seed examples.

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** C

    **Explanation:** The text gives simulating mouse movement through a web page as an example of data synthesis.

### Question 22: Why does the text say data augmentation and data synthesis are some...

Why does the text say data augmentation and data synthesis are sometimes used interchangeably?

- [ ] A) Because both terms mean data must be real.
- [ ] B) Because both aim to automate data creation.
- [ ] C) Because synthetic data is always derived from real data.
- [ ] D) Because evaluation data cannot be augmented.

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** The text states that since the goal of both augmentation and synthesis is to automate data creation, the terms are sometimes used interchangeably.

### Question 23: According to the text, what is the biggest reason for data synthesis?

According to the text, what is the biggest reason for data synthesis?

- [ ] A) To completely replace human-generated data
- [ ] B) To produce data at scale for training and testing AI models
- [ ] C) To eliminate all privacy concerns
- [ ] D) To reduce the size of AI models

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** The text says the biggest reason for data synthesis is that it allows you to produce data at scale, promising an abundant supply for training and testing AI models.

### Question 24: Which example does the text give for using synthetic data to increa...

Which example does the text give for using synthetic data to increase data coverage?

- [ ] A) Generating synthetic patient records for healthcare
- [ ] B) Generating factually inconsistent summaries to train models to detect factual inconsistency
- [ ] C) Training a cheaper model to imitate another model
- [ ] D) Using Faker to generate names and addresses for testing

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** The text cites Gekhman et al. (2022) using LLMs to generate factually inconsistent summaries to train models to detect factual inconsistency as an example of increasing coverage.

### Question 25: What does the text say about mixing human- and AI-generated data?

What does the text say about mixing human- and AI-generated data?

- [ ] A) It is always inferior to purely human-generated data
- [ ] B) It often produces the best value in many use cases
- [ ] C) It is only useful for testing software programs
- [ ] D) It should be avoided because of privacy concerns

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** The text states that in many use cases, mixing human- and AI-generated data often produces the best value.

### Question 26: Which statement about synthetic data quality is supported by the text?

Which statement about synthetic data quality is supported by the text?

- [ ] A) Synthetic data is always lower quality than human-generated data
- [ ] B) Human-generated data can sometimes be lower quality because of fundamental human limitations
- [ ] C) AI cannot generate complex math problems
- [ ] D) AI-generated preference ratings are less consistent than human ratings

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** The text says sometimes humans have fundamental limitations that cause human-generated data to be lower quality than AI-generated data.

### Question 27: What does the source call using algorithms to generate data, as opp...

What does the source call using algorithms to generate data, as opposed to manual generation?

- [ ] A) Procedural generation
- [ ] B) Simulation synthesis
- [ ] C) AI-powered synthesis
- [ ] D) Template augmentation

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** A

    **Explanation:** The source states that using algorithms to generate data is also called procedural generation, as opposed to manual generation.

### Question 28: According to the source, why are many fraud detection models first...

According to the source, why are many fraud detection models first trained on synthetic transaction data generated from templates?

- [ ] A) Because synthetic transactions are always more accurate than real transactions
- [ ] B) Because transaction data is sensitive, so models can prove feasibility before getting access to real data
- [ ] C) Because templates eliminate the need for fraud detection models
- [ ] D) Because real transaction data cannot be used for training AI models

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** The source says that due to the sensitivity of transaction data, many fraud detection models are first trained on synthetic transaction data to prove feasibility before being given access to real data.

### Question 29: What does the source describe perturbation as in data synthesis?

What does the source describe perturbation as in data synthesis?

- [ ] A) Replacing an entire dataset with simulated data
- [ ] B) Adding noise to existing data to generate new data
- [ ] C) Using templates to generate documents with a specific structure
- [ ] D) Translating examples from one language to another

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** The source defines perturbation as adding noise to existing data to generate new data.

### Question 30: According to the source, what is a key benefit of simulations for g...

According to the source, what is a key benefit of simulations for generating data?

- [ ] A) They guarantee that algorithms trained in simulation will work in the real world
- [ ] B) They allow multiple experiments with minimal costs while avoiding accidents and physical damage
- [ ] C) They remove the need for real-world data in all AI projects
- [ ] D) They are only useful for generating text data

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** The source states that simulations allow multiple experiments with minimal costs while avoiding accidents and physical damage.

### Question 31: According to the text, what does “StableToolBench” demonstrate?

According to the text, what does “StableToolBench” demonstrate?

- [ ] A) Using AI to simulate APIs without having to evoke them
- [ ] B) Using AI to translate code between programming languages
- [ ] C) Using AI judges to create preference data
- [ ] D) Using AI to generate synthetic textbooks and blog posts

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** A

    **Explanation:** The text states that StableToolBench demonstrates how to use AI to simulate APIs without having to evoke them, which can avoid costly or slow actual API calls.

### Question 32: In the Dota 2 example, about how much gameplay did OpenAI’s simulat...

In the Dota 2 example, about how much gameplay did OpenAI’s simulator enable the bot to play every day?

- [ ] A) Approximately 18 years’ worth of games
- [ ] B) Approximately 180 years’ worth of games
- [ ] C) Approximately 1,800 years’ worth of games
- [ ] D) Approximately 180 days’ worth of games

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** The text says OpenAI used a simulator that enabled the Dota 2 bot to play approximately 180 years’ worth of games every day.

### Question 33: How does the text describe using back-translation to verify transla...

How does the text describe using back-translation to verify translation quality?

- [ ] A) Translate the original sentence into a low-resource language and accept it without comparison
- [ ] B) Translate the translation back into the original language and compare it with the original sentence
- [ ] C) Use an AI judge twice with the response order swapped
- [ ] D) Generate code snippets from explanations and documentation

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** The text explains that if the original English sentence is X and the translated Lao sentence is Y, you can translate Y back into X′ and compare X′ with X; if they are very different, Y is likely bad.

### Question 34: In creating UltraChat, how did the authors structure their topic ge...

In creating UltraChat, how did the authors structure their topic generation before generating instructions and responses?

- [ ] A) They started with 175 seed examples and generated 52,000 pairs.
- [ ] B) They asked ChatGPT to generate 30 topics, then 30 to 50 subtopics per topic.
- [ ] C) They used reverse instruction on Wikipedia articles.
- [ ] D) They generated unit tests for each topic.

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** The text states the authors first asked ChatGPT to generate 30 topics and then 30 to 50 subtopics for each topic before generating instructions and responses.

### Question 35: What is the “reverse instruction” approach described in the source...

What is the “reverse instruction” approach described in the source text?

- [ ] A) Using AI to generate long responses and humans to write short instructions.
- [ ] B) Taking existing long-form, high-quality content and using AI to generate prompts that would elicit such content.
- [ ] C) Reversing the order of instruction and response during finetuning.
- [ ] D) Using a weak model to generate instructions from scratch without seed examples.

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** The text defines reverse instruction as taking existing long-form, high-quality content like stories, books, and Wikipedia articles and using AI to generate prompts that would elicit such content.

### Question 36: In the long-context finetuning process described, what is done afte...

In the long-context finetuning process described, what is done after generating several (question, answer) pairs for each short chunk?

- [ ] A) The short chunk is discarded and only the question is used.
- [ ] B) The original long document is used as the context for each (question, answer) pair.
- [ ] C) The model is trained only on the short chunks without questions.
- [ ] D) The long document is split into even shorter chunks under 1K tokens.

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** The text says that for each (question, answer) pair, the original long document is used as the context, which may exceed 8K tokens but be shorter than the target length.

### Question 37: In Llama 3’s coding data synthesis pipeline, which step is used to...

In Llama 3’s coding data synthesis pipeline, which step is used to catch runtime execution errors in generated code?

- [ ] A) Parsers and linters
- [ ] B) Unit tests generated by AI
- [ ] C) Back-translation verification
- [ ] D) Code translation to other languages

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** The text states that unit tests are used to catch runtime execution errors, and interestingly, AI was used to generate these unit tests.

### Question 38: According to the text, what are the four major limitations or reaso...

According to the text, what are the four major limitations or reasons AI-generated data might not entirely replace human-generated data?

- [ ] A) Cost, speed, privacy, and storage
- [ ] B) Difference in quality, limitations of imitation, potential model collapse, and obscured lineage
- [ ] C) Licensing, bias, annotation speed, and compute requirements
- [ ] D) Lack of volume, lack of diversity, lack of labels, and lack of benchmarks

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** The text explicitly lists these four major reasons: quality difference, limitations of imitation, potential model collapse, and obscured lineage.

### Question 39: What does the text suggest about the possibility of never having to...

What does the text suggest about the possibility of never having to worry about human-annotated data again?

- [ ] A) It is certain to happen soon because synthetic data is always better
- [ ] B) It is impossible because synthetic data has no usefulness
- [ ] C) It is exciting to imagine, but AI-generated data might never entirely replace human-generated data
- [ ] D) It has already happened because human annotation is no longer used

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** C

    **Explanation:** The text says it is exciting to imagine never worrying about human-annotated data again, but AI-generated data might never entirely replace human-generated data.

### Question 40: Which limitation of AI-generated data is described as obscuring its...

Which limitation of AI-generated data is described as obscuring its lineage?

- [ ] A) The way AI generation of data obscures its lineage
- [ ] B) The difference in quality
- [ ] C) The limitations of imitation
- [ ] D) Potential model collapse

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** A

    **Explanation:** The text names “the way AI generation of data obscures its lineage” as one of the four major limitations.

### Question 41: According to the text, why can AI-generated data be problematic?

According to the text, why can AI-generated data be problematic?

- [ ] A) It is always too expensive to produce
- [ ] B) It can be of low quality, following the principle “garbage in, garbage out”
- [ ] C) It cannot be stored in datasets
- [ ] D) It is only useful for manual labeling

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** The source states that AI’s generated data can be of low quality and invokes “garbage in, garbage out.”

### Question 42: What will be essential in making synthetic data more useful?

What will be essential in making synthetic data more useful?

- [ ] A) Avoiding all quality metrics
- [ ] B) Replacing human judgment entirely
- [ ] C) Developing reliable methods and metrics to evaluate data
- [ ] D) Generating data without any verification

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** C

    **Explanation:** The text says reliable methods and metrics to evaluate data are essential for making synthetic data more useful.

### Question 43: When will people be hesitant to use synthetic data?

When will people be hesitant to use synthetic data?

- [ ] A) When they can easily verify its quality
- [ ] B) When it is generated by AI
- [ ] C) When it is used only for evaluation
- [ ] D) When they can’t verify its quality

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** D

    **Explanation:** The source states that people will be hesitant to use synthetic data if they can’t verify its quality.

### Question 44: According to “The False Promise of Imitating Proprietary LLMs,” wha...

According to “The False Promise of Imitating Proprietary LLMs,” what might be superficial about imitation models?

- [ ] A) Their ability to reduce training costs
- [ ] B) Their perceived performance from mimicking teacher models
- [ ] C) Their ability to generalize to all outside tasks
- [ ] D) Their factual accuracy on every task

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** The source says the perceived performance achieved by mimicking might be superficial, and imitation models may mimic style while struggling with factual accuracy and generalization.

### Question 45: What can happen when a student model is trained on a capable teache...

What can happen when a student model is trained on a capable teacher model’s solutions to complex math questions?

- [ ] A) The student model is guaranteed to solve those questions
- [ ] B) The student model learns to produce answers that look like solutions even if it cannot solve the questions
- [ ] C) The student model stops mimicking the teacher’s style
- [ ] D) The student model improves its base model quality automatically

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** The source says this training effectively teaches the student to produce answers that look like solutions even if it isn’t capable of solving the questions, and imitation can force hallucination.

### Question 46: What do Gudibande et al. (2023) suggest is needed for improvement i...

What do Gudibande et al. (2023) suggest is needed for improvement in reasoning capabilities?

- [ ] A) More imitation of teacher model style
- [ ] B) Training only on teacher model solutions
- [ ] C) Improving the quality of the base models
- [ ] D) Avoiding factual accuracy and generalization

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** C

    **Explanation:** The source states that Gudibande et al. suggest focusing on improving the quality of the base models for improvement in reasoning capabilities.

### Question 47: What did Shumailov et al. (2023) name the phenomenon in which recur...

What did Shumailov et al. (2023) name the phenomenon in which recursively using AI-generated data in training causes irreversible defects and degrading performance over time?

- [ ] A) Data feedback loop
- [ ] B) Model collapse
- [ ] C) Synthetic saturation
- [ ] D) Bias amplification

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** The source states that Shumailov et al. (2023) named this phenomenon model collapse and demonstrated it in models including Variational Autoencoders, Gaussian mixture models, and LLMs.

### Question 48: According to Gerstgrasser et al. (2024), how can model collapse be...

According to Gerstgrasser et al. (2024), how can model collapse be avoided?

- [ ] A) By using only synthetic data for all training
- [ ] B) By mixing synthetic data with real data
- [ ] C) By avoiding post-training entirely
- [ ] D) By training only on improbable events

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** The source says Gerstgrasser et al. argue that model collapse is inevitable if the entire training dataset is synthetic, but it can be avoided by mixing synthetic data with real data.

### Question 49: According to Taori and Hashimoto (2023), what can happen when model...

According to Taori and Hashimoto (2023), what can happen when models are trained on datasets that include previous model outputs?

- [ ] A) Existing biases in the model can be amplified
- [ ] B) Rare events become over-represented
- [ ] C) Model collapse is completely prevented
- [ ] D) Synthetic data becomes identical to real data

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** A

    **Explanation:** The source states that when models are trained on datasets including previous model outputs, any existing biases in the model can be amplified.

### Question 50: What did Nemotron-4 340B-Instruct use during its instruction finetu...

What did Nemotron-4 340B-Instruct use during its instruction finetuning and preference finetuning phase?

- [ ] A) 50% synthetic data
- [ ] B) 98% synthetic data
- [ ] C) Only real data
- [ ] D) No finetuning data

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** The source states that Nemotron-4 340B-Instruct used 98% synthetic data during its instruction finetuning and preference finetuning phase.

### Question 51: According to the text, why is AI generation said to obscure data li...

According to the text, why is AI generation said to obscure data lineage?

- [ ] A) Because AI models always produce original content that cannot be traced
- [ ] B) Because AI models are influenced by their training data and can sometimes regurgitate it without the user knowing
- [ ] C) Because AI-generated data is never stored or logged
- [ ] D) Because data lineage only applies to human-created data

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** The text states that AI models are influenced by their training data and can sometimes regurgitate it without the user knowing, which obscures lineage.

### Question 52: The text gives an example where model X, used to generate training...

The text gives an example where model X, used to generate training data, was trained on data with copyright violations. What risk does this create for your model?

- [ ] A) Your model will definitely train faster
- [ ] B) Your model might also violate copyrights
- [ ] C) Your model will be immune to copyright issues
- [ ] D) Your model cannot be evaluated on any benchmark

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** The text says that if model X was trained on data with copyright violations, your model might also violate copyrights.

### Question 53: In the benchmark example, why would a strong result on benchmark B...

In the benchmark example, why would a strong result on benchmark B be contaminated?

- [ ] A) Because benchmark B was designed specifically for your model
- [ ] B) Because model X was also trained on benchmark B
- [ ] C) Because benchmarks cannot measure AI-generated data
- [ ] D) Because your model was trained only on human-written data

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** The text explains that if model X was also trained on benchmark B, your result on B is contaminated.

### Question 54: According to the text, what is hard to assess without clear data li...

According to the text, what is hard to assess without clear data lineage?

- [ ] A) The training speed of model X
- [ ] B) The size of benchmark B
- [ ] C) A model's commercial viability or trust in its performance
- [ ] D) The number of parameters in a model

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** C

    **Explanation:** The text states that without clear data lineage, it's hard to assess a model's commercial viability or trust its performance.

### Question 55: What is model distillation?

What is model distillation?

- [ ] A) Training a larger teacher model to mimic a smaller student model
- [ ] B) Training a small student model to mimic a larger teacher model
- [ ] C) Using synthetic data only to evaluate a model’s limitations
- [ ] D) Deploying a big model without reducing its resource use

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** The source defines model distillation as a method in which a small model (student) is trained to mimic a larger model (teacher).

### Question 56: Which statement about DistilBERT matches the source text?

Which statement about DistilBERT matches the source text?

- [ ] A) It reduces BERT’s size by 40%, retains 97% of language comprehension, and is 60% faster.
- [ ] B) It reduces BERT’s size by 60%, retains 40% of language comprehension, and is 97% faster.
- [ ] C) It keeps BERT’s size the same but makes it 97% faster.
- [ ] D) It reduces BERT’s size by 97%, retains 40% of language comprehension, and is 60% faster.

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** A

    **Explanation:** The source says DistilBERT reduces BERT’s size by 40% while retaining 97% of its language comprehension capabilities and being 60% faster.

### Question 57: How was Alpaca described in the source text?

How was Alpaca described in the source text?

- [ ] A) It was trained from scratch on data generated by a 7-billion-parameter teacher.
- [ ] B) It was finetuned from Llama-7B on examples generated by text-davinci-003 and is 4% the size of the teacher.
- [ ] C) It was distilled from DistilBERT and behaves like BERT while being 40% smaller.
- [ ] D) It was a 175-billion-parameter model trained on examples from Llama-7B.

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** The source says Taori et al. finetuned Llama-7B on examples generated by text-davinci-003, and Alpaca behaves similarly while being 4% the size of the teacher model.

### Question 58: Why does the source note that not all models can be distilled?

Why does the source note that not all models can be distilled?

- [ ] A) Because student models cannot be trained from scratch
- [ ] B) Because many model licenses prohibit using their outputs to train other models, particularly competing models
- [ ] C) Because distillation only works with adapter-based techniques such as LoRA
- [ ] D) Because synthetic instruction data cannot be used with finetuning

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** The source states that many model licenses prohibit using their outputs to train other models, particularly to train competing models.

### Question 59: According to the Llama 3 paper, what happens when a model is traine...

According to the Llama 3 paper, what happens when a model is trained indiscriminately on self-generated data?

- [ ] A) It always improves performance significantly
- [ ] B) It does not improve performance and can even degrade it
- [ ] C) It only affects data curation, not model performance
- [ ] D) It eliminates the need to verify synthetic data

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** The source states that training indiscriminately on self-generated data doesn’t improve performance and can even degrade it.

### Question 60: How were researchers able to continually improve a model using its...

How were researchers able to continually improve a model using its generated data, according to the Llama 3 paper?

- [ ] A) By using only data generated by the teacher model
- [ ] B) By avoiding all synthetic data
- [ ] C) By introducing mechanisms to verify synthetic data quality and using only verified synthetic data
- [ ] D) By processing data according to each use case

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** C

    **Explanation:** The source says they introduced mechanisms to verify the quality of synthetic data and used only verified synthetic data to continually improve the model.

### Question 61: Why does the author find it helpful to read model papers that discl...

Why does the author find it helpful to read model papers that disclose dataset details?

- [ ] A) They often contain tips on how researchers curated, generated, and processed data
- [ ] B) They prove that synthetic data is always better than real data
- [ ] C) They show that data processing is the same for every use case
- [ ] D) They explain why student models cannot outperform teacher models

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** A

    **Explanation:** The source says such papers often contain great tips on how researchers curated, generated, and processed data.

### Question 62: What does the source say about the student model Nemotron-4-340B-In...

What does the source say about the student model Nemotron-4-340B-Instruct?

- [ ] A) It was trained only on unverified self-generated data
- [ ] B) It outperformed the teacher model on a variety of tasks
- [ ] C) It was used to verify all synthetic data
- [ ] D) It required no data processing

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** The source states that Nemotron-4-340B-Instruct outperformed the teacher model on a variety of tasks.

### Question 63: According to the “Inspect Data” section, what should you do first a...

According to the “Inspect Data” section, what should you do first after gathering a raw dataset?

- [ ] A) Immediately train a model on it
- [ ] B) Inspect the data to get a sense of its quality
- [ ] C) Deduplicate all examples before looking at them
- [ ] D) Remove all outliers without reviewing them

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** The text says the first thing to do is inspect the data to get a sense of its quality, including getting its information and statistics.

### Question 64: For large data processing, how should you decide the order of proce...

For large data processing, how should you decide the order of processing steps?

- [ ] A) Always clean each example before any deduplication
- [ ] B) Always filter out low-quality data before anything else
- [ ] C) Do the steps in whichever order saves time and compute
- [ ] D) Always follow a fixed alphabetical order

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** C

    **Explanation:** The text recommends doing data processing steps in whichever order saves time and compute, depending on which steps take longer.

### Question 65: Why does the text recommend keeping a copy of the original data ins...

Why does the text recommend keeping a copy of the original data instead of changing data in place?

- [ ] A) To avoid doing trial runs
- [ ] B) Because other teams might need different processing and bugs can corrupt data
- [ ] C) To make deduplication unnecessary
- [ ] D) To guarantee that all annotators agree

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** The text gives two reasons: another team might need to process the data differently, and bugs in scripts can corrupt the data.

### Question 66: What does the text say about data exploration tools compared with m...

What does the text say about data exploration tools compared with manual data inspection?

- [ ] A) Tools fully replace manual data inspection
- [ ] B) Manual inspection is unnecessary for annotated data
- [ ] C) Tools are useful but will not replace manual data inspection
- [ ] D) Manual inspection is only useful for checking token distributions

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** C

    **Explanation:** The text says many data exploration tools should be used, but they won’t replace manual data inspection.

### Question 67: According to the source, how can duplicated data cause test set con...

According to the source, how can duplicated data cause test set contamination?

- [ ] A) By making all duplicated examples appear only in the test set
- [ ] B) When splitting duplicated data into train and test sets, one example might be in the train set and its duplicate in the test set
- [ ] C) By forcing the model to ignore the training set
- [ ] D) By removing duplicates from the test set automatically

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** The source states that when splitting duplicated data into train and test sets, one example might be in the train set and its duplicate in the test set.

### Question 68: What did the Anthropic study cited in the source demonstrate about...

What did the Anthropic study cited in the source demonstrate about repeating 0.1% of the data 100 times?

- [ ] A) It can cause an 800M parameter model’s performance to degrade to that of a 400M parameter model despite the other 90% of training tokens remaining unique
- [ ] B) It always improves an 800M parameter model to match a larger model
- [ ] C) It has no effect as long as the other 90% of training tokens are unique
- [ ] D) It only affects models smaller than 400M parameters

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** A

    **Explanation:** The source says repeating 0.1% of the data 100 times can degrade an 800M parameter model to the performance of a 400M parameter model, even though the other 90% of training tokens remain unique.

### Question 69: Which deduplication approach involves hashing examples into differe...

Which deduplication approach involves hashing examples into different buckets and checking only among examples that fall into the same bucket?

- [ ] A) Pairwise comparison
- [ ] B) Dimensionality reduction
- [ ] C) Hashing
- [ ] D) Fact-checking annotations

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** C

    **Explanation:** The source describes hashing as hashing examples into different buckets and checking only among examples in the same bucket, with methods including MinHash and Bloom filter.

### Question 70: According to the source, what did Databricks find when they removed...

According to the source, what did Databricks find when they removed extraneous Markdown and HTML tokens?

- [ ] A) Model accuracy improved by 20% and input token lengths were reduced by 60%
- [ ] B) Model accuracy improved by 60% and input token lengths were reduced by 20%
- [ ] C) Model accuracy improved by 10% and input token lengths were reduced by 40%
- [ ] D) Model accuracy was unchanged but training time was reduced by 60%

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** A

    **Explanation:** The source states that removing extraneous Markdown and HTML tokens improved Databricks’ model accuracy by 20% while reducing input token lengths by 60%.

### Question 71: What types of data does the source say you need to clean because th...

What types of data does the source say you need to clean because they are not compliant with your policies?

- [ ] A) Only HTML tags and Markdown tokens
- [ ] B) PII, sensitive data, copyrighted data, or data considered toxic
- [ ] C) Only low-quality annotations from the second half of annotation sessions
- [ ] D) Only zip code, name, and gender fields

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** The source lists PII, sensitive data, copyrighted data, and toxic data as examples of non-compliant data that must be cleaned.

### Question 72: What did Kern et al. (2024) find about annotations made in the seco...

What did Kern et al. (2024) find about annotations made in the second half of an annotation session?

- [ ] A) They are higher quality because annotators become more practiced
- [ ] B) They are lower quality, likely due to annotator boredom or fatigue
- [ ] C) They are equally high quality as earlier annotations
- [ ] D) They are always unusable and should be discarded entirely

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** The source says Kern et al. (2024) found that annotations made in the second half of an annotation session are of lower quality, likely due to annotator boredom or fatigue.

### Question 73: According to the text, what can happen if you get data into the wro...

According to the text, what can happen if you get data into the wrong chat template for the model you’re finetuning?

- [ ] A) The model will automatically reformat the data
- [ ] B) It can cause strange bugs in your model
- [ ] C) The tokenizer will be replaced
- [ ] D) The data will be deduplicated again

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** The text states that getting data into the wrong chat template can cause strange bugs in your model.

### Question 74: For supervised finetuning, what format is your data most likely in?

For supervised finetuning, what format is your data most likely in?

- [ ] A) (system prompt, user prompt)
- [ ] B) (instruction, response)
- [ ] C) (input, label, example)
- [ ] D) (question, answer, task description)

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** The text says that if you’re doing supervised finetuning, your data is most likely in the format (instruction, response).

### Question 75: During finetuning, what do instructions typically NOT need?

During finetuning, what do instructions typically NOT need?

- [ ] A) A response
- [ ] B) A user prompt
- [ ] C) Task descriptions or examples
- [ ] D) A system prompt

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** C

    **Explanation:** The text states that during finetuning, instructions typically don’t need task descriptions or examples because the model can learn expected behavior from sufficient training examples.

### Question 76: According to the summary, what three core criteria are shared by da...

According to the summary, what three core criteria are shared by dataset design across training phases?

- [ ] A) Quality, coverage, and quantity
- [ ] B) Privacy, compliance, and annotation
- [ ] C) Latency, cost, and throughput
- [ ] D) Diversity, synthesis, and verification

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** A

    **Explanation:** The summary states that dataset design across training phases shares the same three core criteria: quality, coverage, and quantity.

### Question 77: What does the summary say about the relationship between high-quali...

What does the summary say about the relationship between high-quality data and large amounts of noisy data?

- [ ] A) Large noisy data always outperforms small high-quality data
- [ ] B) A small amount of high-quality data can outperform a large amount of noisy data
- [ ] C) High-quality data is only important during pre-training
- [ ] D) Noisy data is preferred because it improves diversity

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** The text explicitly says a small amount of high-quality data can outperform a large amount of noisy data.

### Question 78: What does the summary say must be done with synthetic data before i...

What does the summary say must be done with synthetic data before it is used to train models?

- [ ] A) It must be converted into ChatML format
- [ ] B) It must be evaluated to ensure its quality
- [ ] C) It must be combined only with real data
- [ ] D) It must be annotated by contracted data providers

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** The summary states that, just like real data, synthetic data must be evaluated to ensure its quality before being used to train models.

### Question 79: According to the summary, which statement reflects the difficulty o...

According to the summary, which statement reflects the difficulty of dataset creation?

- [ ] A) Creating annotation guidelines is easier than annotating data
- [ ] B) Automating data generation is harder than automating verification
- [ ] C) It is hard to automate verifying data, just as it is hard to automate data generation
- [ ] D) Thinking through what data you want can be fully automated

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** C

    **Explanation:** The summary says it is hard to automate data generation, but even harder to automate verifying it, and that you cannot automate thinking through what data you want.
