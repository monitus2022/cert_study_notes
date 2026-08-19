# AWS Certified AI Practitioner (AIF-C01) — Amazon SageMaker Master Cheat Sheet

## 1. Core SageMaker Components for AIF-C01

| SageMaker Component | Key Purpose & Functionality | Primary Target User |
| :--- | :--- | :--- |
| **SageMaker Canvas** | Visual, **no-code ML interface** for building predictive models and generating insights from tabular, image, or text data without writing code. | Business Analysts |
| **SageMaker Data Wrangler** | Low-code tool to clean, normalize, transform, and visualize ML feature engineering pipelines (300+ built-in transformations). | Data Scientists / ML Engineers |
| **SageMaker Feature Store** | Centralized, secure repository to store, index, share, and reuse ML features across teams for both real-time (online) and batch (offline) inference. | MLOps / Data Engineering |
| **SageMaker JumpStart** | ML hub providing pre-trained **open-source models** (Llama, Mistral, FLAN-T5) with full access to weights, code, and hosting instances. | ML Engineers |
| **SageMaker Autopilot** | **AutoML engine** that automatically explores data, selects algorithms, tunes hyperparameters, and outputs full code notebooks. | Developers / Data Scientists |
| **SageMaker Clarify** | Detects **data and model bias** during training/inference and provides model explainability via SHAP (SHapley Additive exPlanations) values. | Compliance / AI Governance |
| **SageMaker Model Monitor** | Automatically detects **data drift** (input distribution shifts) and **concept drift** (model accuracy degradation) on live endpoints. | MLOps Engineers |
| **SageMaker Pipelines** | Workflow orchestration tool designed specifically for building end-to-end **MLOps CI/CD automation**. | MLOps Engineers |
| **SageMaker Model Registry** | Version-controlled repository to catalog, track lineage, approve, and deploy ML model artifacts. | Model Managers / MLOps |

---

### Service Comparisons: SageMaker vs. AWS Alternatives

#### SageMaker JumpStart vs. Amazon Bedrock

| Dimension | SageMaker JumpStart | Amazon Bedrock |
| :--- | :--- | :--- |
| **Model Type** | Open-source foundation models (Llama, Mistral, Stability) | Proprietary & open FMs (Claude, Llama, Titan, AI21) |
| **Infrastructure Control** | **High**: Deployed on dedicated SageMaker EC2 instances inside your VPC | **Zero**: 100% Serverless managed API endpoints |
| **Weights & Customization** | Full access to weights; deep custom hyperparameter tuning | Serverless Fine-Tuning API, RAG, and Guardrails |
| **Cost Structure** | Instance-based (paid per hourly compute node runtime) | Token-based (paid per input/output token processed) |

#### SageMaker Data Wrangler vs. AWS Glue DataBrew

| Dimension | SageMaker Data Wrangler | AWS Glue DataBrew |
| :--- | :--- | :--- |
| **Primary Integration** | Built directly into **SageMaker Studio** for ML pipelines | Integrated into **AWS Glue ETL** workflows |
| **Primary Output** | Exports directly to **SageMaker Feature Store / Pipelines** | Exports to **S3 / Redshift / Glue Catalog** |

---

## 2. End-to-End Business Workflow Example

### Scenario: E-Commerce Customer Churn Prediction & Model Governance

```text
[ Raw Logs in S3 ]
        │
        ▼
[ SageMaker Data Wrangler ] ──(Feature Prep)──► [ SageMaker Feature Store ]
                                                         │
                                                         ▼
[ SageMaker Pipelines ] ──────(AutoML)────────► [ SageMaker Autopilot ]
        │                                                │
        │                                                ▼
        ├────────────(Bias & Explainability)───► [ SageMaker Clarify ]
        │                                                │
        ▼                                                ▼
[ SageMaker Model Registry ] ──(Approval)─────► [ Real-Time Endpoint ]
                                                         │
                                                         ▼
[ S3 Baseline Data ] ───────(Drift Checks)────► [ SageMaker Model Monitor ]
```

1. **Data Ingestion**: Raw customer behavior logs land in an **Amazon S3** bucket.
2. **Feature Engineering**: **SageMaker Data Wrangler** cleans missing fields and extracts interaction metrics.
3. **Feature Management**: Prepared features are registered into **SageMaker Feature Store** for reusability across online and offline workloads.
4. **AutoML Training**: **SageMaker Autopilot** iterates through multiple classification models to find the optimal accuracy score.
5. **Bias & Explainability Audit**: **SageMaker Clarify** evaluates the model for demographic bias and generates SHAP feature attribution scores.
6. **Governance & Registry**: The trained model artifact is submitted to **SageMaker Model Registry** for team approval.
7. **Orchestration**: The entire training and evaluation sequence is automated using **SageMaker Pipelines**.
8. **Deployment**: Approved models are hosted on a **SageMaker Real-Time Inference Endpoint**.
9. **Production Governance**: **SageMaker Model Monitor** compares incoming live inference traffic against baseline data in **S3** to trigger alerts if data drift occurs.

---

## 3. AIF-C01 Exam Tips & Traps

### Key Exam Decision Triggers

* **Trigger**: *"Business analyst needs to build a model without writing code..."*
  * 🎯 **Answer**: **SageMaker Canvas**
* **Trigger**: *"Detect bias in training data or explain model decisions..."*
  * 🎯 **Answer**: **SageMaker Clarify**
* **Trigger**: *"Detect shifts in input data distribution over time in production..."*
  * 🎯 **Answer**: **SageMaker Model Monitor**
* **Trigger**: *"Store and share normalized ML features across real-time and batch applications..."*
  * 🎯 **Answer**: **SageMaker Feature Store**
* **Trigger**: *"Deploy an open-source model with full infrastructure isolation in a custom VPC..."*
  * 🎯 **Answer**: **SageMaker JumpStart**

### Common Exam Traps to Avoid

* ⚠️ **TRAP: SageMaker JumpStart vs. Bedrock**
  * If the question emphasizes *serverless*, *API calls*, or *zero infrastructure management*, choose **Bedrock**.
  * If the question emphasizes *open-source model weights*, *custom instance configuration*, or *deploying inside a private VPC*, choose **SageMaker JumpStart**.

* ⚠️ **TRAP: Bias Detection vs. PII Masking**
  * Use **SageMaker Clarify** for fairness, statistical bias, and model explainability.
  * Use **Amazon Comprehend** or **Bedrock Guardrails** for detecting and redacting Personally Identifiable Information (PII) or blocking toxic prompts.

* ⚠️ **TRAP: Automated Model Building**
  * Use **SageMaker Canvas** if the persona is a **no-code business analyst**.
  * Use **SageMaker Autopilot** if the persona is a **developer or data scientist** who wants automated training *and* underlying code notebook outputs.