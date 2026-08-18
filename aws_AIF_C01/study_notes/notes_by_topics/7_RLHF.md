# Reinforcement Learning from Human Feedback (RLHF) & Alignment (AIF-C01)

Reinforcement Learning from Human Feedback (RLHF) is an advanced model optimization technique used to align Foundation Model outputs with human values, preferences, and safety guidelines. It transitions a model from merely predicting the next token to generating helpful, honest, and harmless responses.

---

## 1. What is RLHF & Why Is It Needed?

* **Definition**: A fine-tuning methodology that combines Reinforcement Learning (RL) with human evaluation to optimize model behavior based on a reward signal.
* **The Problem It Solves**: Base FMs or Supervised Fine-Tuned (SFT) models often exhibit unintended behaviors—such as generating toxic language, inventing facts (hallucinations), or failing to infer user intent—because standard cross-entropy loss only measures token prediction accuracy, not human satisfaction.
* **Core Objective**: Aligning models to the **3 Hs**:
  * **Helpfulness**: Accurately following user instructions and inferring intent.
  * **Honesty**: Minimizing hallucinations and admitting uncertainty.
  * **Harmlessness**: Avoiding toxicity, dangerous advice, and social bias.

---

## 2. The 3-Step RLHF Pipeline

1. **Step 1: Supervised Fine-Tuning (SFT Baseline)**
   * Start with a pre-trained FM and fine-tune it on high-quality human demonstration datasets (prompt-response pairs) to establish baseline conversational ability.

2. **Step 2: Reward Model (RM) Training**
   * Prompt the SFT model to generate multiple candidate completions for a given prompt.
   * Human evaluators rank these candidate responses from best to worst.
   * Train a dedicated **Reward Model** on these preference rankings to mathematically output a scalar score (reward) representing response quality.

3. **Step 3: Reinforcement Learning Optimization (PPO)**
   * Use an RL algorithm—typically **Proximal Policy Optimization (PPO)**—to adjust the LLM's weights.
   * The LLM generates responses, the Reward Model scores them, and PPO updates the LLM to maximize high-reward generations while preventing drastic divergence from the baseline model.

---

## 3. RLHF Variants & Alternatives

* **RLAIF (Reinforcement Learning from AI Feedback)**
  * **How It Works**: Replaces human labelers with a larger, highly capable LLM (LLM-as-a-judge) to rank candidate outputs and score rewards.
  * **Exam Advantage**: Drastically reduces annotation costs, speeds up iteration, and supports superalignment at scale.
* **DPO (Direct Preference Optimization)**
  * **How It Works**: Optimizes LLM weights directly on preferred vs. dispreferred response pairs using a specialized classification loss, bypassing the need to train a separate Reward Model.
  * **Exam Advantage**: Lower computational complexity and memory footprint compared to traditional PPO-based RLHF.

---

## 4. AWS Ecosystem Integration for RLHF

* **Amazon SageMaker Ground Truth**: Provides managed human workflows and custom data labeling interfaces to collect preference rankings from human evaluators for Reward Model training.
* **Amazon SageMaker AI**: Used for self-hosted RLHF pipelines (training Reward Models, running PPO, or executing DPO scripts on distributed GPU clusters).
* **Amazon Bedrock Model Customization**: Supports **Reinforcement Fine-Tuning (RFT)** jobs, allowing developers to supply prompts and reward evaluation logic (e.g., via AWS Lambda or automated reward scripts) directly within managed Bedrock environments.

---

## 5. Exam Selection Cheat Sheet & High-Yield Decision Rules

| Optimization Goal / Data Scenario | Correct Approach | Key Exam Anchor |
| :--- | :--- | :--- |
| **Align model behavior with human preference / safety** | **RLHF / RFT** | Human preference rankings or reward model evaluation |
| **Adapt model tone, persona, or output format** | **Supervised Fine-Tuning (SFT)** | Curated static prompt-response (.jsonl) pairs |
| **Inject live / dynamic business knowledge** | **RAG (Knowledge Bases)** | Vector retrieval from S3 or database without training |
| **Teach raw domain jargon or specialized language** | **Continued Pre-Training** | Unlabeled text corpora (textbooks, whitepapers) |
| **Human data labeling / preference annotation workflow** | **SageMaker Ground Truth** | Human-in-the-loop data labeling service |