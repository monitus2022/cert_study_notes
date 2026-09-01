# Complete AWS Machine Learning & GenAI Guide (AIF-C01)

## 1. AWS ML Service Spectrum & Hierarchy

AWS balances **Ease of Use** against **Control & Customization** across four distinct service tiers:

| Abstraction Level | AWS Services | ML Expertise Needed | Customization & Control | Infrastructure Management |
| :--- | :--- | :--- | :--- | :--- |
| **1. Managed AI Services** | Amazon Comprehend, Textract, Rekognition, Transcribe | **None** (API calls only) | **Lowest** (Fixed task-specific models) | **Zero** (Serverless APIs) |
| **2. Managed Foundation Models** | Amazon Bedrock | **Low to Medium** (Prompting, RAG) | **Medium** (Prompts, System Instructions, RAG, Managed Fine-Tuning) | **Zero** (Serverless API endpoints) |
| **3. Pre-trained Model Hub** | SageMaker JumpStart | **Medium to High** | **High** (Full access to weights, hyperparameters, hosting scripts) | **High** (Managed EC2 instance types, clusters, endpoints) |
| **4. Custom ML Development** | Amazon SageMaker (from scratch) | **Highest** | **Maximum** (Custom PyTorch/TF containers, algorithms, pipelines) | **Highest** (Full control over training & inference infra) |

### Fine-Tuning Distinction: Bedrock vs. SageMaker
* **Bedrock Fine-Tuning**: Fully serverless. Provide a dataset in S3; Bedrock fine-tunes a copy behind the scenes and serves it via an API endpoint.
* **SageMaker / JumpStart Fine-Tuning**: Infrastructure-managed. Configure compute instances (`ml.g5`/`ml.p4`), tune hyperparameters directly, monitor GPU memory, and host your own endpoints.

---

## 2. Why Amazon Comprehend Excels at Specific Tasks

Amazon Comprehend relies on narrow, deterministic models engineered purely for text classification and entity extraction rather than probabilistic text generation.

* **Deterministic Output & Confidence Scores**: Returns strict JSON with exact character offsets and mathematical confidence scores (e.g., `98.5%`), avoiding LLM hallucinations or schema breaking.
* **Zero Prompt Engineering**: Eliminates complex system instructions—simply call pre-built APIs like `DetectEntities` or `DetectSentiment`.
* **Specialized Domain Models**: Offers **Amazon Comprehend Medical** (pre-trained on RxNorm and ICD-10-CM ontologies) and native **PII Redaction APIs**.
* **Lower Latency & Cost**: Processes extraction tasks significantly faster and cheaper than running 70B+ parameter Foundation Models.

---

## 3. AIF-C01 Exam Decision Guide

### Scenario Rules
* **Amazon Comprehend**: Choose when the prompt specifies task-specific NLP (PII detection, sentiment analysis, entity extraction) on unstructured text without needing generative text output or custom model training.
* **Amazon Bedrock**: Choose when a scenario mentions *Generative AI*, *Foundation Models*, *RAG*, or *Guardrails* **without** wanting to manage EC2 instances or hosting infrastructure.
* **SageMaker JumpStart**: Choose over Bedrock when the scenario requires **open-source weights** (e.g., Llama, Mistral) or **full infrastructure control** over model fine-tuning and deployment inside custom VPCs.

### Task Comparison Matrix
| Scenario Priority / Requirement | Best AWS Service | Primary Reason |
| :--- | :--- | :--- |
| **Speed, exact JSON formatting, lowest cost** | **Amazon Comprehend** | Dedicated `DetectSentiment` API with zero setup. |
| **Summarizing text AND extracting sentiment** | **Amazon Bedrock** | Generative tasks (summarization) require Foundation Models. |
| **Detecting PII and redacting it automatically** | **Amazon Comprehend** | Native PII redaction APIs operate without complex prompting. |
| **Open-source model weights & custom VPC deployment** | **SageMaker JumpStart** | Full access to model artifacts with managed compute endpoints. |