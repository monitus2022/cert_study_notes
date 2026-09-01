# AWS Certified AI Practitioner (AIF-C01) Master Exam Cheat Sheet

---

## 1. Master Scenario Anchor Cheat Sheet ("If You See X, Choose Y")

| If the Exam Scenario Mentions... | Choose This AWS Service / Solution | Why This Solution Wins |
| :--- | :--- | :--- |
| **"Extract text, tables, and handwriting from scanned PDFs without custom ML"** | **Amazon Textract** | Pre-trained, fully managed document extraction API. |
| **"Detect faces, custom objects, or moderate inappropriate images/video"** | **Amazon Rekognition** | Pre-trained computer vision API with zero model training required. |
| **"Build conversational voice or text chatbots using natural language understanding"** | **Amazon Lex** | Managed conversational AI engine powering automated bots. |
| **"Convert written text into lifelike spoken audio across multiple languages"** | **Amazon Polly** | Pre-trained text-to-speech (TTS) neural audio API. |
| **"Transcribe audio call recordings into time-stamped text files"** | **Amazon Transcribe** | Managed automatic speech recognition (ASR) service. |
| **"Extract sentiment, entities, and key topics from unstructured customer text"** | **Amazon Comprehend** | Pre-trained natural language processing (NLP) service. |
| **"Deliver real-time personalized product recommendations based on user history"** | **Amazon Personalize** | Pre-built recommendation engine powered by AWS ML. |
| **"Incorporate dynamic, up-to-date company policies without retraining the model"** | **Amazon Bedrock Knowledge Bases (RAG)** | Ground answers in external S3 vector stores to eliminate hallucinations. |
| **"Adapt model output style, tone, persona, or custom output format (e.g., JSON)"** | **Supervised Fine-Tuning (SFT)** | Updates internal model weights to enforce target behavior and formatting. |
| **"Teach a model specialized domain technical jargon/acronyms using unlabeled text"** | **Continuous Pre-Training** | Ingests unlabeled text to adapt base weights to specialized vocabulary. |
| **"Filter toxic prompts, block PII, reject denied topics, and block hallucinations in real time"** | **Guardrails for Amazon Bedrock** | Real-time safety filter applied directly to Bedrock inference requests. |
| **"Detect demographic bias in datasets/models and calculate SHAP feature importance"** | **Amazon SageMaker Clarify** | ML explainability and bias analysis engine for training and inference. |
| **"Route low-confidence predictions or sensitive AI completions to human reviewers"** | **Amazon Augmented AI (Amazon A2I)** | Managed human-in-the-loop workflow orchestrator for ML predictions. |
| **"Discover, classify, and redact sensitive PII in S3 buckets before data ingestion"** | **Amazon Macie** | Automated S3 security service using ML to detect PII and credentials. |
| **"Route Bedrock API traffic privately inside VPC without traversing public internet"** | **AWS PrivateLink** | Establishes private network endpoints between customer VPC and Bedrock. |
| **"Enforce strict, declarative tool execution limits on agents independently of LLM reasoning"** | **Policy in Amazon Bedrock AgentCore** | Gateway-level authorization controls that block unauthorized API calls. |
| **"Manage workload identities, inbound auth, and outbound OAuth keys for AI agents"** | **Amazon Bedrock AgentCore Identity** | Secure identity and token management runtime for autonomous agents. |
| **"Download AWS SOC/ISO compliance reports or sign HIPAA BAA"** | **AWS Artifact** | Central portal for downloading AWS compliance reports and legal agreements. |
| **"Continuously monitor AWS resource configurations for compliance drift"** | **AWS Config** | Evaluates resource states against security baselines and auto-remediates drift. |
| **"Document custom model training data, architecture, performance, and governance"** | **Amazon SageMaker Model Cards** | Customizable governance artifact for tracking custom ML models. |
| **"AWS-provided non-customizable documentation for pre-trained AWS AI services"** | **AWS AI Service Cards** | AWS-published documentation outlining capabilities and limits of pre-trained AI services. |

---

## 2. Domain 1 & 2: Core AI/ML & Generative AI Fundamentals

### Learning Paradigms Quick Comparison
* **Supervised Learning**: Model trains on **labeled data** ($X \rightarrow Y$).
  * *Classification*: Predicts discrete categorical labels (e.g., spam/not spam, churn/no churn).
  * *Regression*: Predicts continuous numerical values (e.g., house prices, temperature).
* **Unsupervised Learning**: Model trains on **unlabeled data** to find hidden patterns.
  * *Clustering*: Groups similar data points without prior class labels (e.g., customer segmentation).
* **Reinforcement Learning**: Agent interacts with an environment, learning optimal policies via **rewards and penalties**.

### Model Fitting & Parameter Adjustments

$$\text{High Bias} = \text{Underfitting (Model too simple)} \quad \Big\vert{} \quad \text{High Variance} = \text{Overfitting (Model memorizes noise)}$$

* **Overfitting Mitigation**: Increase training data, apply regularization, simplify model architecture, or reduce training epochs.
* **Underfitting Mitigation**: Increase model complexity, add relevant features, reduce regularization, or train for more epochs.
* **Hyperparameters vs. Weights**:
  * *Hyperparameters*: External settings configured *before* training (e.g., learning rate, batch size, epochs).
  * *Weights & Biases*: Internal parameters learned and updated *during* training.

### SageMaker Inference Options Selection Matrix

| SageMaker Inference Type | Operational Characteristics | Ideal Scenario |
| :--- | :--- | :--- |
| **Real-Time Inference** | Sub-second latency, persistent dedicated instances. | Sustained high-volume interactive web apps. |
| **Serverless Inference** | Scales down to **zero** when idle; pay-per-execution. | Unpredictable, intermittent traffic with long idle gaps. |
| **Asynchronous Inference** | Payloads up to 1 GB, processing time up to 1 hour, built-in queue. | Large file processing (e.g., high-res video) with queuing. |
| **Batch Transform** | Offline batch execution; resources terminate on completion. | Scheduled overnight bulk dataset scoring (e.g., daily risk reports). |

---

## 3. Domain 3: Foundation Model Applications & Design

### The FM Customization Spectrum

```text
[Prompt Engineering] ---> [RAG] ---> [Distillation] ---> [Fine-Tuning] ---> [Pre-Training]
 (Lowest Cost/Effort)                                                  (Highest Cost/Effort)