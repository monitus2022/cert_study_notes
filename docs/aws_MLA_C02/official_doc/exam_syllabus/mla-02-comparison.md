

# Comparison of MLA-C01 and MLA-C02
<a name="mla-02-comparison"></a>

## Side-by-side comparison
<a name="mla-02-side-by-side"></a>

The following table shows the domains and the percentage of scored questions in each domain for the MLA-C01 exam (in use until September 28, 2026) and the MLA-C02 exam (in use beginning September 29, 2026).


| MLA-C01 Domain | MLA-C02 Content Domain | 
| --- | --- | 
| Domain 1: Data Preparation for Machine Learning (ML) (28%) | Content Domain 1: Data Preparation for ML and AI (28% of scored content) | 
| Domain 2: ML Model Development (26%) | Content Domain 2: ML Model and Foundation Model (FM) Development (24% of scored content) | 
| Domain 3: Deployment and Orchestration of ML Workflows (22%) | Content Domain 3: Deployment and Orchestration of ML and AI Workflows (24% of scored content) | 
| Domain 4: ML Solution Monitoring, Maintenance, and Security (24%) | Content Domain 4: Operating, Monitoring, and Securing ML and AI Solutions (24% of scored content) | 

## Additions of content for MLA-C02
<a name="mla-02-additions"></a>

In Task 1.1, the following content was added:
+ 1.1.7 Configure scalable vector databases for AI applications (for example, OpenSearch Service, Amazon RDS with pgvector, Amazon S3) based on specifications.
+ 1.1.8 Ingest and store diverse data types (for example, text, images, audio) for AI and ML applications.

In Task 1.2, the following content was added:
+ 1.2.5 Configure and use embedding models to transform text and image data into numerical representations.
+ 1.2.6 Apply advanced text pre-processing techniques (for example, tokenization, domain-specific augmentation).
+ 1.2.7 Prepare documents for Retrieval Augmented Generation (RAG) applications (for example, chunking strategies, metadata extraction).
+ 1.2.8 Mask, redact, and anonymize data.
+ 1.2.9 Prepare data for FM fine-tuning, continuous pre-training, and model distillation.

In Task 1.3, the following content was added:
+ 1.3.4 Optimize multimodal data distributions by applying bias metrics across numeric, text, and image assets.
+ 1.3.6 Validate AI training data integrity (for example, prompt-response pair validation, content safety screening).
+ 1.3.7 Clean data (for example, by detecting outliers, imputing missing data, deduplication).

In Task 2.1, the following content was added:
+ 2.1.1 Evaluate and select appropriate FMs from Amazon Bedrock based on task requirements and performance criteria.
+ 2.1.2 Identify fine-tuning strategies for pre-trained FMs to meet business needs.
+ 2.1.4 Evaluate tradeoffs between custom solutions, managed services, pre-trained models, and FMs to meet business needs.
+ 2.1.5 Select Retrieval Augmented Generation (RAG) architecture patterns based on use case requirements.
+ 2.1.7 Assess tradeoffs between AI model performance, latency, and cost.

In Task 2.2, the following content was added:
+ 2.2.8 Apply customization techniques for AI solutions (for example, task-specific prompt engineering, fine-tuning).
+ 2.2.9 Optimize retrieval components and embedding models.

In Task 2.3, the following content was added:
+ 2.3.7 Implement integrated human evaluation frameworks (for example, human-in-the-loop workflows, text generation quality assessment).
+ 2.3.8 Apply natural language processing (NLP) evaluation metrics (for example, bilingual evaluation understudy [BLEU], Recall-Oriented Understudy for Gisting Evaluation [ROUGE], BERTScore, semantic similarity).
+ 2.3.9 Perform AI evaluation (for example, model output assessment, content quality validation, bias detection, LLM-as-a-judge frameworks).
+ 2.3.10 Configure RAG system monitoring, including retrieval accuracy assessment.

In Task 3.1, the following content was added:
+ 3.1.4 Evaluate and select appropriate foundation model (FM) deployment options.
+ 3.1.5 Deploy models that were built outside of AWS into AWS environments (for example, Amazon SageMaker AI, Amazon Bedrock Custom Model Import).
+ 3.1.6 Deploy and configure agents for specific tasks, integration with other services and tools, and agent communication protocols.
+ 3.1.7 Configure FM deployment, model hosting, and resource allocation.
+ 3.1.8 Apply Retrieval Augmented Generation (RAG) system configurations (for example, retrieval strategies, reranking).

In Task 3.2, the following content was added:
+ 3.2.7 Create and manage Amazon Bedrock knowledge bases with vector database configurations, document indexing, and retrieval optimization.
+ 3.2.8 Implement retrieval pipelines to meet business needs.
+ 3.2.9 Implement agent state management systems.
+ 3.2.10 Implement AI-specific resource scaling for GPU workloads.
+ 3.2.11 Deploy agentic workflow infrastructure.

In Task 3.3, the following content was added:
+ 3.3.7 Manage prompts (for example, Amazon Bedrock Prompt Management).
+ 3.3.8 Implement automated agent deployment pipelines and agent version management.
+ 3.3.9 Implement AI model testing frameworks, including prompt testing.
+ 3.3.10 Configure FM deployment automation with fine-tuned model versioning.
+ 3.3.11 Configure AI-specific pipeline orchestration for RAG system updates and knowledge base refresh cycles.

In Task 4.1, the following content was added:
+ 4.1.5 Monitor and automate the management of agent performance and coordination (for example, coordination failure detection, truncated streaming, tool failures).
+ 4.1.6 Configure AI-specific performance monitoring for foundation models (FMs), such as Amazon Bedrock evaluations.

In Task 4.2, the following content was added:
+ 4.2.7 Evaluate cost implications of using FMs for inference in production.
+ 4.2.8 Monitor agent resource consumption patterns.
+ 4.2.9 Manage FM inference costs with usage optimization.
+ 4.2.10 Monitor AI-specific cost patterns (for example, token usage optimization, embedding computation costs, vector database storage optimization).

In Task 4.3, the following content was added:
+ 4.3.1 Secure continuous integration and continuous delivery (CI/CD) pipelines by checking for code and image vulnerabilities (for example, by using Amazon CodeGuru, Amazon Inspector).
+ 4.3.8 Select the appropriate credential type to access FMs (for example, Amazon Bedrock API keys, IAM credentials).
+ 4.3.9 Implement safeguards and sensitive data protection to meet application requirements and responsible AI policies (for example, by using Amazon Bedrock Guardrails).

## Deletions of content for MLA-C02
<a name="mla-02-deletions"></a>

In Task 1.3, the following content was removed:
+ Configuring data to load into the model training resource (for example, Amazon EFS, Amazon FSx)

In Task 2.2, the following content was removed:
+ Using custom datasets to fine-tune pre-trained models (for example, Amazon Bedrock, SageMaker JumpStart)
+ Reducing model size (for example, by altering data types, pruning, updating feature selection, compression)

In Task 3.1, the following content was removed:
+ Methods to optimize models on edge devices (for example, SageMaker Neo)

In Task 3.2, the following content was removed:
+ Bring your own container (BYOC) with SageMaker

In Task 4.2, the following content was removed:
+ Monitoring infrastructure (for example, by using Amazon EventBridge events)
+ Troubleshooting capacity concerns that involve cost and performance (for example, provisioned concurrency, service quotas, auto scaling)

## Recategorizations of content for MLA-C02
<a name="mla-02-recategorizations"></a>

The following content reorganizations have occurred in the transition from MLA-C01 to MLA-C02:

The following task statements have been recategorized:

MLA-C01 Task Statement 1.1 is mapped to the following task in MLA-C02:
+ 1.1 Collect and store data.

MLA-C01 Task Statement 1.2 is mapped to the following task in MLA-C02:
+ 1.2 Perform data transformation, feature engineering, and pre-processing.

MLA-C01 Task Statement 1.3 is mapped to the following task in MLA-C02:
+ 1.3 Validate data quality and manage bias.

MLA-C01 Task Statement 2.1 is mapped to the following task in MLA-C02:
+ 2.1 Choose appropriate modeling approaches for ML and AI solutions.

MLA-C01 Task Statement 2.2 is mapped to the following task in MLA-C02:
+ 2.2 Train, fine-tune, and customize models for ML and AI solutions.

MLA-C01 Task Statement 2.3 is mapped to the following task in MLA-C02:
+ 2.3 Analyze and evaluate the performance of ML and AI systems.

MLA-C01 Task Statement 3.1 is mapped to the following task in MLA-C02:
+ 3.1 Manage deployment infrastructure for ML and AI model types.

MLA-C01 Task Statement 3.2 is mapped to the following task in MLA-C02:
+ 3.2 Provision and configure resources for ML and AI workloads based on existing architecture and requirements.

MLA-C01 Task Statement 3.3 is mapped to the following task in MLA-C02:
+ 3.3 Implement automated orchestration and continuous integration and continuous delivery (CI/CD) pipelines for MLOps and AI workloads.

MLA-C01 Task Statement 4.1 is mapped to the following task in MLA-C02:
+ 4.1 Monitor ML and AI model inference and performance.

MLA-C01 Task Statement 4.2 is mapped to the following task in MLA-C02:
+ 4.2 Optimize and manage ML and AI infrastructure costs and performance.

MLA-C01 Task Statement 4.3 is mapped to the following task in MLA-C02:
+ 4.3 Secure ML and AI workloads and model endpoints.