# Udemy course content


| Course Section | Primary MLA-C01 Domain & Task Statement Alignment |
| --- | --- |
| **Section 1: Introduction** | *Foundational Overview* (Exam scope, ML lifecycle alignment) |
| **Section 2: Data Ingestion and Storage** | **Domain 1 — Task 1.1:** Ingest and store data |
| **Section 3: Data Transformation, Integrity, & Feature Eng.** | **Domain 1 — Task 1.2:** Transform data and perform feature engineering<br>

<br>**Domain 1 — Task 1.3:** Validate data and ensure data integrity |
| **Section 4: AWS Managed AI Services** | **Domain 2 — Task 2.1:** Choose modeling approach & select algorithms *(Pre-trained APIs vs. custom ML)* |
| **Section 5: SageMaker Built-In Algorithms** | **Domain 2 — Task 2.1:** Choose modeling approach & select algorithms |
| **Section 6: Model Training, Tuning, and Evaluation** | **Domain 2 — Task 2.2:** Train and tune models<br>

<br>**Domain 2 — Task 2.3:** Analyze model performance and evaluate models |
| **Section 7: Generative AI Model Fundamentals** | **Domain 2 — Task 2.4:** Develop and manage models using Generative AI / Foundation Models |
| **Section 8: Building GenAI Apps with Bedrock** | **Domain 2 — Task 2.4:** Develop GenAI models / RAG<br>

<br>**Domain 3 — Task 3.1:** Choose deployment infrastructure *(Bedrock Provisioned Throughput/Agents)* |
| **Section 9: MLOps / AIOps with AWS** | **Domain 3 — Task 3.1:** Choose deployment infrastructure & endpoints<br>

<br>**Domain 3 — Task 3.2:** Provision compute & auto scaling<br>

<br>**Domain 3 — Task 3.3:** Set up CI/CD pipelines & workflow orchestration |
| **Section 10: Security, Identity, and Compliance** | **Domain 4 — Task 4.1:** Secure ML systems and resources *(IAM, KMS, VPC)* |
| **Section 11: Management and Governance** | **Domain 4 — Task 4.2:** Monitor models, data, and infrastructure<br>

<br>**Domain 4 — Task 4.3:** Maintain ML solutions *(Governance, Model Cards, Retraining)* |
| **Section 12: Machine Learning Best Practices** | *Cross-Domain Review* (Architectural trade-offs across Domains 1–4) |

---

### Detailed Breakdown by Exam Domain

#### Domain 1: Data Preparation for Machine Learning (28%)

* **Task 1.1 (Ingest and store data):** Covered in **Section 2** *(S3 storage classes, Kinesis/Data Firehose streaming, Glue crawlers, Feature Store ingestion, Database Migration Service)*.
* **Tasks 1.2 & 1.3 (Transform data & validate integrity):** Covered in **Section 3** *(SageMaker Data Wrangler, Glue DataBrew, PySpark/EMR, feature scaling, encoding, missing value imputation, and pre-training data quality checks)*.

#### Domain 2: ML Model Development (26%)

* **Task 2.1 (Choose approach & select algorithms):** Covered in **Section 4** *(Managed AI Services like Rekognition, Comprehend, Textract)* and **Section 5** *(Built-in algorithms like XGBoost, DeepAR, BlazingText, Image Classification, Factorization Machines)*.
* **Tasks 2.2 & 2.3 (Train, tune, & evaluate models):** Covered in **Section 6** *(SageMaker Script Mode, Automatic Hyperparameter Tuning [HPO], evaluation metrics like RMSE/AUC/Confusion Matrices, SageMaker Clarify explainability/SHAP values)*.
* **Task 2.4 (Generative AI / Foundation Models):** Covered in **Sections 7 & 8** *(Prompt engineering, fine-tuning, embeddings, Vector DBs/OpenSearch Serverless, RAG architectures with Amazon Bedrock, Knowledge Bases, and Guardrails)*.

#### Domain 3: Deployment and Orchestration of ML Workflows (22%)

* **Tasks 3.1 & 3.2 (Deployment infrastructure & compute provisioning):** Covered in **Section 9** *(SageMaker Endpoints: Real-time, Serverless, Async, Multi-Model Endpoints [MME], Auto-scaling policies)*.
* **Task 3.3 (Automated CI/CD pipelines):** Covered in **Section 9** *(SageMaker Pipelines DAGs, Model Registry approval workflows, Step Functions, EventBridge triggers)*.

#### Domain 4: ML Solution Monitoring, Maintenance, and Security (24%)

* **Task 4.1 (Secure ML systems):** Covered in **Section 10** *(IAM execution roles, S3 bucket policies, KMS encryption at rest/in transit, VPC Interface Endpoints / PrivateLink for isolated SageMaker Studio & endpoints)*.
* **Tasks 4.2 & 4.3 (Monitoring, Governance, & Maintenance):** Covered in **Section 11** *(SageMaker Model Monitor for Data & Concept Drift, CloudWatch Alarms, SageMaker Model Cards/Lineage Tracking, automated model retraining strategies)* and **Section 12** *(Cross-cutting architecture best practices)*.