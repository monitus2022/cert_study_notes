# Foundation Model Fine-Tuning: Supervised (SFT) vs. Reinforcement Fine-Tuning (RFT)

On the AWS Certified AI Practitioner (AIF-C01) exam, questions about model fine-tuning test your ability to match the **business problem** and **available training data** to the correct customization strategy: **Supervised Fine-Tuning (SFT)** versus **Reinforcement Fine-Tuning (RFT / RLHF)**.

---

## 1. Core Conceptual Difference

* **Supervised Fine-Tuning (SFT)**: Trains the model on **labeled input-output pairs** (`{prompt, target_response}`). The model directly learns to mimic target answers.
* **Reinforcement Fine-Tuning (RFT / RLHF)**: Trains the model using **feedback and reward signals** rather than explicit target answers. The model generates candidate outputs, and a reward function (rule-based script, Lambda function, or LLM-as-a-judge) scores those outputs to steer weight updates toward higher-scoring behaviors.

---

## 2. How the Exam Frames Questions (Scenario Patterns)

### Pattern 1: Data Availability
* **SFT Scenario Anchor**: You have explicit **labeled input-output pairs** (e.g., 10,000 curated customer emails with approved target responses).
  * *Choice*: **Supervised Fine-Tuning (SFT)**.
* **RFT Scenario Anchor**: No labeled target answers exist, but candidate responses can be **scored programmatically or via reward rules** (e.g., unit tests evaluating generated code).
  * *Choice*: **Reinforcement Fine-Tuning (RFT / RLHF)**.

### Pattern 2: Goal & Behavior Alignment
* **SFT Primary Goals**: Modifying output style, brand persona, domain language, or enforcing a strict structural output format (e.g., valid JSON schema).
* **RFT Primary Goals**: Aligning model behavior with human preferences, improving safety/helpfulness, or optimizing complex reasoning tasks (e.g., math, multi-step tool calls, or code) where a reward function can judge output quality.

### Pattern 3: AWS Bedrock Architecture
* **SFT Configuration**: Uploading a `.jsonl` dataset containing `"prompt"` and `"completion"` fields directly to an Amazon S3 bucket, then launching an **Amazon Bedrock Model Customization Job**.
* **RFT Configuration**: Uploading prompts to Amazon S3 and configuring a reward function (such as an **AWS Lambda function** or rule-based check) that evaluates generated completions during the Amazon Bedrock RFT job.

---

## 3. Comparative Matrix for Exam Quick-Recall

| Dimension | Supervised Fine-Tuning (SFT) | Reinforcement Fine-Tuning (RFT / RLHF) |
| :--- | :--- | :--- |
| **Input Dataset Format** | Labeled `(prompt, response)` pairs (`.jsonl`). | Prompts + Reward Function / Evaluation Grader. |
| **Learning Signal** | Direct imitation of static target text. | Iterative feedback scores (reward signal). |
| **Primary Use Cases** | Tone, persona, JSON formatting, domain-specific Q&A. | Preference alignment, safety/toxicity reduction, verifiable tasks (math/code). |
| **Bedrock Evaluation Engine** | Validation loss on test dataset. | AWS Lambda reward function, rule checks, or LLM-as-a-judge. |

---

## 4. High-Yield Exam Decision Rules & Traps

1. **Labeled pairs $\rightarrow$ SFT**: If the scenario explicitly mentions a dataset of high-quality, ground-truth input-output examples, choose **Supervised Fine-Tuning**.
2. **Reward function / preference scoring $\rightarrow$ RFT**: If the scenario mentions evaluating candidate completions with reward functions, human feedback, or AWS Lambda scoring scripts, choose **Reinforcement Fine-Tuning**.
3. **Unlabeled raw text $\rightarrow$ Continuous Pre-Training**: Do not confuse SFT with Continuous Pre-Training. Unlabeled text dumps (e.g., raw textbooks, medical journals) are used for *Continuous Pre-Training* to teach domain jargon, not SFT.
4. **Injecting live factual data $\rightarrow$ RAG**: Neither SFT nor RFT should be used to update a model with frequently changing factual information. Dynamic factual retrieval requires **Amazon Bedrock Knowledge Bases (RAG)**.