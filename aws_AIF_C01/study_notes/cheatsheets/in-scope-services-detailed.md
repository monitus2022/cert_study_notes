# AWS Certified AI Practitioner (AIF-C01) Study Notes

> These notes summarize the listed in-scope AWS services and emphasize common AI use cases, service selection, and exam comparisons. AWS service capabilities and names can change; verify the latest AWS documentation before the exam.

---

## 1. Analytics

### AWS Data Exchange

**Purpose:** Find, subscribe to, and access third-party datasets in the AWS Cloud.

**Example use case:**

- A financial company subscribes to market data and combines it with internal transaction data in Amazon S3.
- A machine learning team uses external weather data to improve demand forecasting.

**Exam points:**

- Reduces the effort required to discover and acquire third-party data.
- Can provide data through files, APIs, and other supported data products.
- Commonly used as an input to analytics and machine learning workflows.

---

### Amazon EMR

**Purpose:** Managed big-data platform for processing large datasets using frameworks such as Apache Spark, Hive, and Hadoop.

**Example use case:**

- Process terabytes of clickstream data to create features for a recommendation model.
- Run distributed Spark jobs for log analysis.

**Exam points:**

- Suitable for large-scale batch processing and big-data analytics.
- Provides more control over distributed processing infrastructure than serverless ETL services.
- Can use Amazon S3 as a data lake storage layer.

---

### AWS Glue

**Purpose:** Serverless data integration and ETL service.

**Key components:**

- **Glue Data Catalog:** Central metadata repository for tables, schemas, and data locations.
- **Crawlers:** Discover schemas and populate the Data Catalog.
- **ETL jobs:** Transform and move data.
- **Glue Studio:** Visual interface for designing data integration jobs.
- **Glue Data Quality:** Helps evaluate data quality rules.
- **Workflows and triggers:** Orchestrate data-processing jobs.

**Example use case:**

- Crawl CSV files in Amazon S3, infer their schema, transform them into Parquet, and load them into an analytics data lake.

**Exam points:**

- Serverless and managed.
- Commonly used with Amazon S3, Lake Formation, Athena, and Redshift.
- Glue is primarily for data integration and ETL, not general-purpose application hosting.

---

### AWS Glue DataBrew

**Purpose:** Visual, no-code or low-code data preparation and profiling.

**Example use case:**

- A data analyst removes duplicates, standardizes date formats, and handles missing values before training a machine learning model.

**Exam points:**

- Designed for interactive data preparation.
- Useful for analysts who do not want to write ETL code.
- Different from Glue ETL jobs, which are more suitable for repeatable production pipelines.

---

### AWS Lake Formation

**Purpose:** Build, govern, secure, and manage data lakes on AWS.

**Example use case:**

- Allow the marketing team to access customer segmentation data while restricting access to personally identifiable information.

**Exam points:**

- Provides centralized governance for data lakes.
- Integrates with Amazon S3 and the Glue Data Catalog.
- Supports fine-grained access controls, including table- and column-level permissions.
- Helps implement data discovery, permissions, and auditability.

---

### Amazon OpenSearch Service

**Purpose:** Managed search, log analytics, observability, and vector search service.

**Example use cases:**

- Search product descriptions in an e-commerce application.
- Analyze application logs and security events.
- Store embeddings for semantic search or retrieval-augmented generation.

**Exam points:**

- Supports text search and analytics.
- Can support vector search for similarity-based retrieval.
- Often used as a retrieval store for generative AI applications.
- Do not confuse it with Amazon Kendra, which is designed primarily for enterprise search.

---

### Amazon Quick

The list may refer to **Amazon QuickSight** and/or the newer Amazon Quick analytics experiences.

**Purpose:** Business intelligence, dashboards, visualization, and natural-language analytics.

**Example use case:**

- Executives view sales dashboards.
- A business user asks a natural-language question about revenue trends.
- A company embeds analytics dashboards into an application.

**Exam points:**

- Used for visualization and business intelligence rather than raw data storage.
- Can connect to services such as Amazon S3, Athena, Redshift, and databases.
- Generative AI features can assist with natural-language questions, summaries, and dashboard creation, depending on the AWS offering and region.

---

### Amazon Redshift

**Purpose:** Fully managed cloud data warehouse for structured and semi-structured analytics.

**Example use case:**

- Aggregate sales, customer, and inventory data for enterprise reporting.
- Run analytical SQL queries over large datasets.

**Exam points:**

- Optimized for analytical workloads and large-scale SQL queries.
- Supports integrations with data lakes and other AWS analytics services.
- Different from Amazon RDS, which is primarily for transactional relational workloads.
- Redshift Serverless removes the need to manage provisioned warehouse capacity.

---

## 2. Cloud Financial Management

### AWS Budgets

**Purpose:** Set custom cost, usage, reservation, or savings-plan budgets and receive alerts.

**Example use case:**

- Notify a machine learning team when monthly Amazon SageMaker spending exceeds a threshold.
- Alert administrators when an account approaches its training budget.

**Exam points:**

- Proactive monitoring and alerting.
- Can trigger notifications or automated actions.
- Useful for preventing unexpected AI experimentation costs.

---

### AWS Cost Explorer

**Purpose:** Analyze historical and forecasted AWS costs and usage.

**Example use case:**

- Determine which AWS Region or service is driving generative AI costs.
- Compare Amazon Bedrock inference spending month over month.

**Exam points:**

- Primarily an analysis and visualization tool.
- AWS Budgets is used for thresholds and alerts.
- Cost Explorer is used to investigate spending patterns.

---

## 3. Compute

### Amazon EC2

**Purpose:** Resizable virtual servers with control over operating systems, networking, storage, and instance types.

**Example use cases:**

- Host a custom model-serving application.
- Run GPU-based model training or inference.
- Deploy software that requires operating-system-level control.

**Exam points:**

- Provides more control than Lambda.
- Can use CPU, GPU, and specialized instance types.
- Customers are responsible for more infrastructure management, including patching and capacity planning.
- Suitable for long-running or specialized workloads.

---

### AWS Lambda

**Purpose:** Serverless, event-driven compute that runs code without managing servers.

**Example use cases:**

- Invoke a function when a document is uploaded to Amazon S3.
- Validate an API request before calling an AI service.
- Post-process Amazon Textract output.

**Exam points:**

- Automatically scales based on requests.
- Usually billed based on requests and execution duration.
- Suitable for short-lived event-driven tasks.
- Has execution time, memory, and concurrency limits.
- Not generally the best choice for long-running model training.

---

## 4. Containers

### Amazon ECS

**Purpose:** Managed container orchestration service.

**Key options:**

- **ECS on AWS Fargate:** Serverless container execution; AWS manages the underlying servers.
- **ECS on Amazon EC2:** Customer manages the EC2 instances while ECS manages containers.
- **ECS services and tasks:** Define and maintain running containers.
- **Amazon ECR:** Commonly used to store container images.

**Example use case:**

- Deploy a containerized inference API without managing Kubernetes.
- Run batch data-processing containers.

**Exam points:**

- Simpler AWS-native container orchestration than Kubernetes.
- Fargate reduces infrastructure management.
- ECS is not the same as EKS; ECS uses AWS-specific orchestration, while EKS uses Kubernetes.

---

### Amazon EKS

**Purpose:** Managed Kubernetes control plane.

**Example use cases:**

- Run a portable machine learning platform based on Kubernetes.
- Deploy model-serving workloads using Kubernetes-native tools.
- Use existing Kubernetes skills and ecosystem integrations.

**Exam points:**

- Provides managed Kubernetes, but Kubernetes concepts and operational complexity remain.
- Useful when portability, Kubernetes compatibility, or advanced orchestration is important.
- EKS is usually more complex than ECS for teams that do not require Kubernetes.

---

## 5. Database

### Amazon Aurora

**Purpose:** Fully managed, high-performance relational database compatible with MySQL or PostgreSQL.

**Example use cases:**

- Store orders and customer records for an AI-powered application.
- Maintain transactional data used to generate recommendation features.

**Exam points:**

- Relational database with SQL and transactions.
- Designed for high availability and scalable relational workloads.
- Aurora PostgreSQL can be used with supported vector capabilities for some AI search workloads, but it remains a relational database.

---

### Amazon DocumentDB

**Purpose:** Managed document database with MongoDB compatibility.

**Example use case:**

- Store flexible product catalogs, user profiles, or application documents with varying attributes.

**Exam points:**

- Document-oriented rather than relational.
- Useful when data has a flexible JSON-like structure.
- MongoDB compatibility does not mean it is the same database engine as MongoDB.

---

### Amazon DynamoDB

**Purpose:** Fully managed, serverless NoSQL key-value and document database.

**Example use cases:**

- Store user preferences for a personalization application.
- Maintain conversation sessions or application state.
- Serve low-latency metadata at large scale.

**Exam points:**

- Designed for predictable, low-latency access at scale.
- Uses partition keys and, optionally, sort keys.
- Supports on-demand and provisioned capacity modes.
- Does not provide the same relational joins and ad hoc SQL capabilities as a relational database.

---

### Amazon ElastiCache

**Purpose:** Managed in-memory caching using engines such as Redis-compatible or Memcached technologies.

**Example use cases:**

- Cache frequently requested AI responses.
- Store session data.
- Reduce database load and improve application latency.

**Exam points:**

- Primarily a cache, not the system of record.
- Useful for low-latency data access.
- Cached data can be lost or expire depending on configuration.
- Do not select ElastiCache when durable primary storage is required.

---

### Amazon Neptune

**Purpose:** Managed graph database.

**Example use cases:**

- Model relationships between users, products, and interests.
- Build fraud-detection graphs.
- Implement knowledge graphs for AI applications.

**Exam points:**

- Suitable for highly connected data and relationship traversal.
- Different from DynamoDB, which is optimized for key-value and document access patterns.
- A graph database can represent entities and relationships more naturally than a relational schema for some use cases.

---

### Amazon RDS

**Purpose:** Managed relational database service for engines such as PostgreSQL, MySQL, MariaDB, Oracle, and SQL Server.

**Example use cases:**

- Store application transactions.
- Maintain structured customer and order data.
- Provide SQL data to an analytics or AI application.

**Exam points:**

- AWS manages much of the infrastructure, backups, patching, and availability configuration.
- Customers still select the database engine, instance size, storage, and configuration.
- Compared with Aurora, RDS is the broader managed relational database service; Aurora is an AWS-designed cloud-optimized database engine.

---

## 6. Developer Tools

### Kiro

**Purpose:** AI-assisted development environment and software engineering tool.

**Example use cases:**

- Generate implementation plans and code from requirements.
- Help create tests, documentation, and application changes.
- Assist developers in understanding and modifying codebases.

**Exam points:**

- Intended to improve developer productivity throughout the software development lifecycle.
- AI-generated code should be reviewed, tested, and checked for security and correctness.
- It does not replace software testing, code review, or human accountability.

---

### Strands Agents

**Purpose:** Open-source SDK and framework for building AI agents and agentic applications.

**Example use cases:**

- Build an agent that calls tools to look up orders, query databases, or invoke business APIs.
- Create a multi-step workflow in which an agent plans, acts, observes results, and continues.

**Exam points:**

- Focuses on agent development patterns and tool use.
- An agent is more than a chatbot: it can reason over a task, choose tools, and perform actions.
- Agent permissions and tool access must be restricted using least privilege.

---

### Amazon Q

**Purpose:** Generative AI assistant for developers, business users, and AWS-related tasks.

**Key use cases:**

- **Amazon Q Developer:** Code generation, explanation, debugging, modernization, AWS assistance, and developer productivity.
- **Amazon Q Business:** Answers questions using an organization’s enterprise data while respecting configured permissions.
- **Amazon Q in AWS services:** Provides assistance in selected AWS consoles and workflows.

**Example use case:**

- A developer asks for help troubleshooting an AWS Lambda function.
- An employee asks questions about internal policies and documents.
- A team uses Q to accelerate application modernization.

**Exam points:**

- Amazon Q is a managed generative AI assistant.
- Enterprise data access must be governed through identity, permissions, and data-source configuration.
- Outputs should be validated because generative AI can produce inaccurate results.

---

# 7. Machine Learning and AI Services

## Amazon Augmented AI

### Amazon A2I

**Purpose:** Add human review to machine learning predictions or AI-generated results.

**Example use cases:**

- Require a human to review low-confidence identity-document classifications.
- Review sensitive content moderation decisions.
- Validate extracted fields before they are entered into a business system.

**Exam points:**

- Also called **Amazon Augmented AI**.
- Supports human review workflows and worker interfaces.
- Useful when predictions require human oversight for accuracy, compliance, or safety.
- Often integrated with services such as Amazon Textract and Amazon Rekognition.
- A2I is not a model-training service; it provides human review of inference results.

---

## Amazon Bedrock

**Purpose:** Fully managed service for building generative AI applications using foundation models from Amazon and other providers through a unified API.

### Important Bedrock capabilities

- **Foundation models:** Access models for text, chat, embeddings, image generation, and other modalities.
- **Model inference:** Generate text, images, embeddings, or structured responses.
- **Model customization:** Customize selected models using techniques such as fine-tuning or continued pretraining, where supported.
- **Knowledge Bases:** Implement managed retrieval-augmented generation.
- **Agents:** Build agents that can reason over requests, use tools, and access data.
- **Guardrails:** Apply configurable controls for harmful content, denied topics, and sensitive information.
- **Prompt management:** Create and manage reusable prompts.
- **Model evaluation:** Compare model quality, accuracy, robustness, and other criteria.
- **Provisioned Throughput:** Reserve capacity for supported models and predictable workloads.
- **Amazon Bedrock Marketplace:** Discover and use additional models, subject to availability and configuration.
- **Model invocation logging:** Capture invocation information for monitoring and auditing, subject to configuration and privacy requirements.

### Example use cases

- Build a customer-service chatbot.
- Summarize legal or business documents.
- Generate product descriptions.
- Create a RAG application over internal company documents.
- Invoke an image-generation model for marketing content.

### Exam points

- Bedrock provides access to foundation models without managing model infrastructure.
- It is generally the natural choice for consuming foundation models through APIs.
- **RAG** retrieves relevant enterprise data at inference time instead of changing the model’s internal parameters.
- **Fine-tuning** changes model behavior using additional training data.
- **Guardrails** help control model inputs and outputs but do not guarantee perfect safety.
- Model selection should consider quality, modality, latency, context window, cost, and deployment requirements.

---

## Amazon Bedrock AgentCore

**Purpose:** Capabilities for deploying, operating, securing, and governing production AI agents and agentic applications.

**Example use cases:**

- Deploy an agent that calls internal tools and enterprise services.
- Secure agent identity and tool access.
- Monitor agent sessions and traces.
- Manage runtime and memory requirements for long-running agent interactions.

**Exam points:**

- Focuses on production operational needs for agents, such as runtime, identity, tools, memory, observability, and governance.
- Bedrock is the broader generative AI platform for models and application capabilities.
- AgentCore is oriented toward operationalizing agents, including agents built with supported frameworks.
- Agents should use narrowly scoped permissions and controlled tools.

---

## Amazon Comprehend

**Purpose:** Natural language processing service for analyzing text.

**Key capabilities:**

- Sentiment analysis.
- Entity recognition.
- Key phrase extraction.
- Language detection.
- Syntax analysis.
- Topic modeling.
- Personally identifiable information detection.
- Custom classification and custom entity recognition.

**Example use cases:**

- Classify customer feedback as positive, neutral, or negative.
- Extract names, organizations, and locations from documents.
- Detect sensitive information in text.
- Route support tickets by topic.

**Exam points:**

- Comprehend analyzes text; it does not primarily generate text.
- Custom models can be trained for organization-specific classification or entity extraction.
- Do not confuse Comprehend with Amazon Transcribe, which converts speech to text.

---

## Amazon Lex

**Purpose:** Build conversational interfaces using speech or text.

**Example use cases:**

- Create a banking chatbot that checks account balances.
- Build a voice-enabled appointment-booking bot.
- Use intents, slots, prompts, and fulfillment logic to complete tasks.

**Exam points:**

- **Intent:** What the user wants to do.
- **Slot:** Information required to fulfill the intent.
- **Fulfillment:** Business logic executed after required information is collected.
- Lex is designed for conversational bots and task completion.
- It can integrate with Lambda for backend fulfillment.

---

## Amazon Nova

**Purpose:** Family of foundation models and generative AI capabilities from AWS.

**Potential model capabilities include:**

- Text understanding and generation.
- Multimodal understanding.
- Image or video understanding.
- Embeddings or other model capabilities, depending on the specific model and availability.

**Example use cases:**

- Summarize documents.
- Analyze text and images together.
- Build an assistant using an AWS model through Amazon Bedrock.

**Exam points:**

- Nova models can be accessed through AWS generative AI services such as Amazon Bedrock, subject to model and Region availability.
- Select the model based on modality, performance, cost, latency, and context requirements.
- Nova is a model family; Bedrock is the managed platform used to access and build applications with models.

---

## Amazon Personalize

**Purpose:** Create individualized recommendations and personalization using machine learning.

**Example use cases:**

- Recommend products to shoppers.
- Recommend movies, music, or articles.
- Personalize search results or marketing content.

**Exam points:**

- Designed for recommendation and personalization use cases.
- Can use user, item, and interaction data.
- Reduces the need to build recommendation algorithms from scratch.
- Different from Amazon Bedrock, which is primarily for generative AI applications.
- Recommendation quality depends on data quality, behavioral history, and appropriate item/user metadata.

---

## Amazon Polly

**Purpose:** Text-to-speech service.

**Example use cases:**

- Read news articles aloud.
- Create voice responses for an accessibility application.
- Produce audio prompts for a conversational application.

**Exam points:**

- Input: Text.
- Output: Speech audio.
- Supports different voices and languages.
- Do not confuse Polly with Transcribe, which converts speech into text.

---

## Amazon Rekognition

**Purpose:** Analyze images and videos using computer vision.

**Key capabilities:**

- Object and scene detection.
- Facial analysis.
- Face comparison and face search.
- Text detection in images.
- Content moderation.
- Custom Labels for custom image classification and object detection.
- Video analysis.

**Example use cases:**

- Detect unsafe or inappropriate content.
- Identify objects in warehouse images.
- Compare a face with an authorized identity image, subject to legal and policy requirements.
- Extract text from images.

**Exam points:**

- Image and video analysis.
- Custom Labels is used when built-in labels are insufficient.
- Rekognition is not the same as Textract: Rekognition focuses on visual analysis, while Textract focuses on document text and structure extraction.
- Biometric use cases require careful consideration of consent, privacy, bias, and applicable law.

---

## Amazon SageMaker AI

**Purpose:** Managed service for building, training, tuning, deploying, and monitoring machine learning models.

### Important SageMaker capabilities

- **Studio:** Integrated environment for data science and machine learning development.
- **Notebooks:** Interactive development environments.
- **Data Wrangler:** Prepare and transform data visually.
- **Feature Store:** Store, share, and retrieve machine learning features.
- **Training jobs:** Run managed model training.
- **Built-in algorithms:** AWS-provided algorithms for common tasks.
- **Hyperparameter tuning:** Search for effective hyperparameter values.
- **Distributed training:** Train models across multiple instances.
- **Processing jobs:** Run data-processing and evaluation tasks.
- **Model Registry:** Organize, version, approve, and deploy models.
- **Endpoints:** Host real-time inference.
- **Batch Transform:** Run batch inference without maintaining a persistent endpoint.
- **Serverless Inference:** Serve models without managing endpoint capacity, for supported workloads.
- **Asynchronous Inference:** Queue requests for large payloads or longer-running inference.
- **Inference Recommender:** Help select instance types and configurations.
- **Model Monitor:** Monitor data quality, model quality, bias, and drift, depending on configuration.
- **Clarify:** Help detect bias and provide model explainability.
- **Pipelines:** Build and automate repeatable ML workflows.
- **Projects and MLOps features:** Support standardized development and deployment processes.
- **Model Cards:** Document intended use, limitations, risks, evaluation results, and other model information.
- **Canvas:** Visual, low-code machine learning development.
- **Autopilot:** Automated machine learning for supported tabular problems.
- **Ground Truth:** Data labeling and annotation workflows.
- **Inference components and deployment options:** Support cost and performance optimization for model hosting.

### Example use case

- Ingest customer data, prepare features, train a fraud model, evaluate it, register the approved model, deploy it to an endpoint, and monitor for drift.

### Exam points

- SageMaker is appropriate when an organization needs control over the ML lifecycle.
- A real-time endpoint is appropriate for low-latency online predictions.
- Batch Transform is appropriate for offline predictions over a dataset.
- Model Monitor detects changes after deployment; it is not a substitute for model training.
- Clarify focuses on bias detection and explainability.
- Model Cards document model information; they do not automatically make a model unbiased or compliant.

---

## Amazon SageMaker JumpStart

**Purpose:** Accelerate model and solution development using pretrained models, foundation models, built-in algorithms, and example solutions.

**Example use cases:**

- Start with a pretrained image-classification model.
- Deploy or experiment with a foundation model.
- Use a solution template for a recommendation or forecasting workload.

**Exam points:**

- JumpStart accelerates discovery, experimentation, and deployment.
- It can help users avoid training a model from scratch.
- It is part of the SageMaker ecosystem but is not the same as Amazon Bedrock.
- Bedrock emphasizes managed access to foundation models and generative AI application development; JumpStart emphasizes model discovery and development within SageMaker.

---

## Amazon Textract

**Purpose:** Extract text, handwriting, forms, tables, and document structure from scanned documents and images.

**Example use cases:**

- Extract fields from invoices.
- Read identity documents.
- Extract tables from financial statements.
- Process loan applications.

**Exam points:**

- Goes beyond basic optical character recognition by identifying document structure.
- Can analyze forms and tables.
- A2I can add human review for low-confidence extractions.
- Textract extracts document information; Comprehend analyzes the meaning of text.

---

## Amazon Transcribe

**Purpose:** Automatic speech recognition that converts speech to text.

**Example use cases:**

- Transcribe contact-center calls.
- Generate subtitles.
- Convert meeting audio into text for summarization.

**Exam points:**

- Input: Audio or speech.
- Output: Text transcript.
- Can support features such as speaker identification and custom vocabulary, depending on the feature and use case.
- A common pipeline is Transcribe → Comprehend → Bedrock for transcription, analysis, and summarization.

---

## Amazon Translate

**Purpose:** Neural machine translation between supported languages.

**Example use cases:**

- Translate customer support messages.
- Localize application content.
- Translate product descriptions.

**Exam points:**

- Translation service, not general-purpose text generation.
- Can be combined with Transcribe for multilingual voice workflows.
- Translation quality should be validated for legal, medical, and other high-risk content.

---

## AWS Transform

**Purpose:** AI-assisted transformation and modernization of applications, code, and workloads.

**Example use cases:**

- Help migrate or modernize legacy applications.
- Transform source code between supported languages or frameworks.
- Assist with mainframe or enterprise workload modernization, where supported.

**Exam points:**

- Helps accelerate migration and modernization.
- Generated changes require testing, security review, and validation.
- It is not a generic model-training service.

---

# 8. Management and Governance

## AWS CloudTrail

**Purpose:** Record AWS API activity and account actions.

**Example use cases:**

- Determine who changed an IAM policy.
- Audit who invoked or configured an AWS service.
- Investigate unauthorized activity.

**Exam points:**

- Primarily an audit and governance service.
- Records API calls and related events.
- Often integrated with Amazon S3, CloudWatch Logs, and security monitoring tools.
- CloudTrail answers “who did what, when, and where?”

---

## Amazon CloudWatch

**Purpose:** Monitor AWS resources, applications, logs, metrics, alarms, and events.

**Example use cases:**

- Create an alarm when a Lambda function has high error rates.
- Monitor SageMaker endpoint latency.
- Collect application logs.
- Trigger automation when an operational event occurs.

**Exam points:**

- CloudWatch monitors operational health and performance.
- CloudTrail records API activity.
- CloudWatch Logs stores and analyzes logs.
- CloudWatch alarms can notify users or trigger automated actions.

---

## AWS Config

**Purpose:** Assess, record, and evaluate the configuration and compliance state of AWS resources.

**Example use cases:**

- Detect S3 buckets that are not encrypted.
- Check whether resources comply with organizational rules.
- Track configuration changes over time.

**Exam points:**

- Configuration compliance and resource inventory.
- Can use managed or custom rules.
- Different from CloudTrail: Config focuses on resource configuration state; CloudTrail focuses on API activity.

---

## AWS Trusted Advisor

**Purpose:** Provide recommendations related to cost optimization, performance, security, fault tolerance, service limits, and operational excellence.

**Example use cases:**

- Identify underutilized EC2 resources.
- Find security group exposure.
- Detect approaching service limits.

**Exam points:**

- Recommendation service.
- Does not replace detailed architecture review or continuous monitoring.
- Available checks and features depend on account support level.

---

## AWS Well-Architected Tool

**Purpose:** Review workloads against AWS architectural best practices.

**Six pillars:**

1. Operational excellence.
2. Security.
3. Reliability.
4. Performance efficiency.
5. Cost optimization.
6. Sustainability.

**Example use case:**

- Review an AI application before production and identify weaknesses in security, resilience, cost, and operational processes.

**Exam points:**

- Used for structured architecture reviews.
- It provides questions and improvement guidance rather than automatically fixing an architecture.
- Cost optimization is only one of the six pillars.

---

# 9. Networking and Content Delivery

## Amazon CloudFront

**Purpose:** Content delivery network that caches and serves content from edge locations closer to users.

**Example use cases:**

- Deliver AI-generated images and application assets globally.
- Reduce latency for a web application.
- Securely expose content from Amazon S3 or an application origin.

**Exam points:**

- Improves latency and reduces origin load.
- Can integrate with AWS WAF and access controls.
- It is a content delivery service, not a general-purpose compute service.
- Caching AI responses requires careful consideration of personalization and sensitive data.

---

## Amazon VPC

**Purpose:** Logically isolated virtual network in AWS.

**Key components:**

- Subnets.
- Route tables.
- Internet gateways.
- NAT gateways.
- Security groups.
- Network ACLs.
- VPC endpoints.
- Flow Logs.
- Peering and Transit Gateway integrations.

**Example use case:**

- Place a database and model endpoint in private subnets while allowing controlled access from an application tier.

**Exam points:**

- **Security groups:** Stateful, instance or network-interface-level controls.
- **Network ACLs:** Stateless, subnet-level controls.
- **VPC endpoints:** Private connectivity to supported AWS services without traversing the public internet.
- A VPC provides network isolation; IAM provides identity-based authorization.

---

# 10. Security, Identity, and Compliance

## AWS Artifact

**Purpose:** Provide on-demand access to AWS compliance reports, certifications, and agreements.

**Example use case:**

- Download AWS compliance documentation for an internal audit or regulatory review.

**Exam points:**

- Used to obtain AWS compliance documentation.
- Does not automatically make a customer’s workload compliant.
- Customers remain responsible for their own configuration and compliance obligations.

---

## AWS IAM

**Purpose:** Control authentication and authorization for AWS resources.

**Key concepts:**

- Users.
- Groups.
- Roles.
- Policies.
- Permissions.
- Identity-based policies.
- Resource-based policies.
- Multi-factor authentication.
- Federation and identity providers.
- Least privilege.

**Example use case:**

- Allow a Lambda function to read documents from one S3 bucket and invoke a specific Bedrock model without granting broad administrator access.

**Exam points:**

- **IAM roles:** Provide temporary credentials and are commonly assumed by AWS services.
- **Policies:** Define allowed or denied actions on resources.
- **Explicit deny:** Overrides an allow.
- Prefer roles and temporary credentials over long-term access keys.
- IAM controls access; KMS encrypts data; CloudTrail audits activity.

---

## Amazon Inspector

**Purpose:** Automated vulnerability management for supported AWS workloads.

**Example use cases:**

- Scan EC2 instances for software vulnerabilities.
- Identify vulnerabilities in container images.
- Detect software package issues in supported Lambda functions.

**Exam points:**

- Focuses on vulnerabilities and exposure.
- It is not the primary service for detecting sensitive data in S3.
- It is not the same as GuardDuty, which focuses on threat detection and suspicious activity.

---

## AWS Key Management Service

### AWS KMS

**Purpose:** Create and manage cryptographic keys used for encryption and signing.

**Example use cases:**

- Encrypt S3 objects, database storage, and secrets.
- Control which IAM principals can use encryption keys.
- Maintain audit records for key usage.

**Exam points:**

- Supports customer managed keys and AWS managed keys.
- Integrates with many AWS services.
- Key policies and IAM policies influence access.
- Encryption protects data, but authorization is still required.
- KMS is not the same as Secrets Manager: KMS manages cryptographic keys; Secrets Manager stores and rotates secrets.

---

## Amazon Macie

**Purpose:** Discover and protect sensitive data, especially personally identifiable information, in Amazon S3.

**Example use cases:**

- Identify S3 objects containing names, account numbers, or other sensitive information.
- Detect unexpectedly public or weakly protected S3 data.
- Support data privacy assessments.

**Exam points:**

- Focuses on sensitive data discovery and data security in S3.
- Useful for identifying PII before it is used for machine learning.
- Do not confuse Macie with Inspector, which focuses on workload vulnerabilities.

---

## AWS Secrets Manager

**Purpose:** Securely store, retrieve, and rotate application secrets.

**Example use cases:**

- Store database passwords.
- Store API keys used by an AI application.
- Rotate credentials without embedding them in source code.

**Exam points:**

- Supports secret rotation for supported integrations.
- Applications retrieve secrets at runtime.
- Commonly encrypts secrets using KMS.
- Do not store secrets in source code, AMIs, container images, or plaintext configuration files.

---

# 11. Storage

## Amazon S3

**Purpose:** Durable, scalable object storage.

**Key concepts:**

- Buckets and objects.
- Storage classes.
- Lifecycle policies.
- Versioning.
- Encryption.
- Access policies.
- Event notifications.
- Replication.
- Object Lock.
- S3 Select.
- Multipart upload.
- Access points.

**Example use cases:**

- Store training datasets, documents, images, model artifacts, logs, and backups.
- Create a central data lake.
- Trigger a Lambda function when a document arrives.

**Exam points:**

- Object storage, not a traditional file system or relational database.
- Strong read-after-write consistency for supported operations.
- S3 is commonly used as the foundation for AI data lakes.
- Use IAM, bucket policies, encryption, and block public access to secure data.
- Storage class selection should consider access frequency, retrieval requirements, and cost.

---

## Amazon S3 Glacier

**Purpose:** Low-cost archival storage within the Amazon S3 ecosystem.

**Storage classes include:**

- S3 Glacier Instant Retrieval.
- S3 Glacier Flexible Retrieval.
- S3 Glacier Deep Archive.

**Example use cases:**

- Archive old training datasets.
- Retain compliance records and historical logs.
- Store model versions that are rarely accessed.

**Exam points:**

- Lower storage cost generally comes with retrieval delays, retrieval charges, or minimum storage-duration considerations.
- Use S3 Lifecycle policies to transition objects to archival classes.
- Glacier is for archival and infrequent access, not low-latency active inference data.
- Objects remain managed through S3 APIs and controls.

---

# Key Comparisons Commonly Tested

## Generative AI and machine learning services

| Compare | Key distinction | Choose when |
|---|---|---|
| Amazon Bedrock vs SageMaker AI | Bedrock provides managed access to foundation models and generative AI capabilities; SageMaker provides broader control over the ML lifecycle | Use Bedrock for foundation-model applications; SageMaker for custom training, deployment, and MLOps |
| Bedrock vs SageMaker JumpStart | Bedrock is a managed model-access platform; JumpStart accelerates model discovery and development in SageMaker | Use JumpStart when working in SageMaker; use Bedrock for simpler managed foundation-model integration |
| RAG vs fine-tuning | RAG retrieves external information at inference time; fine-tuning changes model behavior using training data | Use RAG for changing/private knowledge; use fine-tuning for behavior, style, or task adaptation |
| Prompt engineering vs fine-tuning | Prompt engineering changes the input instructions; fine-tuning changes model parameters | Start with prompt engineering because it is usually faster and less expensive |
| Amazon Personalize vs Bedrock | Personalize provides recommendations; Bedrock provides generative AI model access | Use Personalize for individualized product/content recommendations |
| Comprehend vs Bedrock | Comprehend performs managed NLP analysis; Bedrock generates or reasons over content using foundation models | Use Comprehend for sentiment, entities, PII, and classification |
| Textract vs Rekognition | Textract extracts text, forms, and tables from documents; Rekognition analyzes images and videos | Use Textract for invoices and forms; Rekognition for objects, faces, moderation, and scenes |
| Transcribe vs Polly | Transcribe converts speech to text; Polly converts text to speech | Use together for voice applications |
| Lex vs Bedrock Agents | Lex builds structured conversational bots with intents and slots; Bedrock agents support foundation-model-driven reasoning and tool use | Use Lex for predictable task-oriented bots; use Bedrock agents for more flexible agentic interactions |
| A2I vs SageMaker Ground Truth | A2I provides human review of inference results; Ground Truth labels data for model training | Use A2I after inference; use Ground Truth before or during training |

---

## Compute and containers

| Compare | Key distinction | Choose when |
|---|---|---|
| Lambda vs EC2 | Lambda is serverless and event-driven; EC2 provides configurable virtual servers | Use Lambda for short, event-driven tasks; EC2 for long-running or specialized workloads |
| ECS vs EKS | ECS is AWS-native container orchestration; EKS is managed Kubernetes | Use ECS for simpler AWS container management; EKS when Kubernetes compatibility is required |
| ECS Fargate vs ECS on EC2 | Fargate removes server management; EC2 provides more host control | Use Fargate for reduced operations; EC2 for special instance or host requirements |
| SageMaker endpoint vs Batch Transform | Endpoint provides online predictions; Batch Transform processes a dataset offline | Use endpoints for real-time requests; Batch Transform for scheduled bulk inference |
| Real-time vs asynchronous inference | Real-time is low-latency and synchronous; asynchronous queues longer or larger requests | Choose based on latency, payload size, and processing duration |

---

## Analytics and data services

| Compare | Key distinction | Choose when |
|---|---|---|
| Glue vs Glue DataBrew | Glue is managed data integration and ETL; DataBrew is visual data preparation | Use Glue for production ETL pipelines; DataBrew for analyst-friendly preparation |
| EMR vs Glue | EMR gives control over big-data frameworks; Glue is serverless managed ETL | Use EMR for customized Spark/Hadoop workloads; Glue for serverless data integration |
| Redshift vs RDS/Aurora | Redshift is an analytical data warehouse; RDS/Aurora are primarily transactional relational databases | Use Redshift for analytics; RDS/Aurora for application transactions |
| OpenSearch vs Redshift | OpenSearch is optimized for search, logs, and vector retrieval; Redshift is optimized for analytical SQL | Use OpenSearch for keyword or semantic search; Redshift for warehouse analytics |
| DynamoDB vs ElastiCache | DynamoDB is durable primary NoSQL storage; ElastiCache is an in-memory cache | Use DynamoDB as a system of record; ElastiCache to accelerate frequent reads |
| Neptune vs relational database | Neptune represents highly connected entities and relationships; relational databases use tables and joins | Use Neptune for graph traversal and relationship-heavy workloads |
| S3 vs EBS/EFS | S3 is object storage; EBS is block storage; EFS is shared file storage | Use S3 for data lakes and artifacts; EBS for EC2 disks; EFS for shared file access |

---

## Governance, monitoring, and security

| Compare | Key distinction | Choose when |
|---|---|---|
| CloudTrail vs CloudWatch | CloudTrail audits API activity; CloudWatch monitors metrics, logs, and operational events | Use CloudTrail for “who did what”; CloudWatch for performance and health |
| AWS Config vs CloudTrail | Config evaluates resource configuration; CloudTrail records API events | Use Config to check compliance state; CloudTrail to investigate actions |
| Macie vs Inspector | Macie discovers sensitive data in S3; Inspector finds workload vulnerabilities | Use Macie for PII discovery; Inspector for software and workload vulnerabilities |
| IAM vs KMS | IAM controls access; KMS manages encryption keys | Use IAM for authorization; KMS for cryptographic key management |
| KMS vs Secrets Manager | KMS manages keys; Secrets Manager stores and rotates secrets | Use Secrets Manager for passwords and API keys |
| Artifact vs Config | Artifact provides AWS compliance documents; Config evaluates customer resource configurations | Use Artifact for audit reports; Config for workload compliance checks |
| Budgets vs Cost Explorer | Budgets alerts on thresholds; Cost Explorer analyzes spending | Use Budgets for proactive controls; Cost Explorer for investigation |
| Trusted Advisor vs Well-Architected Tool | Trusted Advisor provides automated recommendations; Well-Architected Tool structures architecture reviews | Use Trusted Advisor for checks; Well-Architected Tool for workload assessment |

---

# Complete AI Pipeline Examples

## Example 1: Intelligent invoice-processing pipeline

**Business use case:** Automate accounts-payable invoice processing while requiring human review for uncertain results.

1. Vendors upload invoices to **Amazon S3**.
2. An S3 event invokes **AWS Lambda**.
3. Lambda calls **Amazon Textract** to extract text, tables, and form fields.
4. Low-confidence fields are sent to **Amazon A2I** for human review.
5. **Amazon Comprehend** detects sensitive information and classifies invoice content.
6. Structured invoice data is stored in **Amazon Aurora** or **Amazon DynamoDB**.
7. Original documents and extracted results are retained in S3.
8. **AWS KMS** encrypts stored data.
9. **IAM** roles restrict Lambda and Textract access.
10. **CloudWatch** monitors processing errors and latency.
11. **CloudTrail** records API activity.
12. **AWS Config** checks that S3 encryption and public-access controls remain enabled.

---

## Example 2: Customer-support voice assistant

**Business use case:** Provide multilingual customer support and automatically summarize calls.

1. Customer speech is captured by the contact-center application.
2. **Amazon Transcribe** converts speech to text.
3. **Amazon Comprehend** analyzes sentiment, entities, topics, and sensitive information.
4. **Amazon Bedrock** summarizes the conversation and proposes a response.
5. **Amazon Translate** translates the transcript or response when needed.
6. **Amazon Polly** converts the final response to speech.
7. **Amazon Lex** can manage structured tasks such as order lookup or appointment booking.
8. **Amazon DynamoDB** stores conversation state and customer preferences.
9. **Amazon ElastiCache** caches frequently requested responses.
10. **Amazon CloudFront** distributes web-based support assets globally.
11. **Amazon CloudWatch** monitors latency, error rates, and service health.
12. **Amazon Bedrock Guardrails** help restrict unsafe or inappropriate responses.

---

## Example 3: Enterprise knowledge assistant using RAG

**Business use case:** Employees ask questions about internal policies and technical documentation.

1. Documents are uploaded to **Amazon S3**.
2. **AWS Glue** crawlers discover document metadata and populate the Data Catalog.
3. **AWS Lake Formation** applies access controls to governed data.
4. Documents are chunked and converted into embeddings using an embedding model available through **Amazon Bedrock**.
5. Embeddings and document metadata are stored in **Amazon OpenSearch Service** or a supported Bedrock Knowledge Base storage configuration.
6. An employee submits a question through a web application.
7. The application authenticates the employee using **IAM** or an external identity provider.
8. The retrieval system finds relevant document chunks.
9. **Amazon Bedrock** generates an answer using the retrieved context.
10. **Bedrock Guardrails** apply content and topic controls.
11. **CloudWatch** monitors application and model-invocation metrics.
12. **CloudTrail** records administrative and API activity.
13. **Macie** scans S3 data for sensitive information.
14. **AWS Budgets** alerts the organization if model usage exceeds the planned budget.

**Important design principle:** RAG allows the application to use current enterprise information without retraining the foundation model every time a document changes.

---

## Example 4: Personalized e-commerce recommendation system

**Business use case:** Recommend products based on customer behavior.

1. Product, user, and interaction data is stored in **Amazon S3**.
2. **AWS Glue** cleans and transforms the data.
3. **Amazon Personalize** trains recommendation models using user interactions and item metadata.
4. Recommendations are generated for users through an online campaign or recommendation endpoint.
5. Frequently requested recommendations are cached in **Amazon ElastiCache**.
6. Product and user profile data is stored in **Amazon DynamoDB**.
7. The web application runs on **Amazon ECS with AWS Fargate**.
8. **Amazon CloudFront** delivers the web experience globally.
9. **Amazon CloudWatch** monitors application latency and error rates.
10. **AWS Cost Explorer** analyzes the cost of data processing and personalization workloads.
11. **AWS Budgets** alerts the team when spending exceeds the approved limit.

---

## Example 5: Custom fraud-detection ML lifecycle

**Business use case:** Predict whether a financial transaction is fraudulent.

1. Historical transaction data is stored in **Amazon S3**.
2. **Macie** checks for sensitive data and helps identify PII exposure.
3. **AWS Glue DataBrew** is used by analysts to profile and clean the dataset.
4. **AWS Glue** creates a repeatable production ETL pipeline.
5. **SageMaker Data Wrangler** performs additional feature preparation.
6. **SageMaker Feature Store** stores reusable transaction features.
7. **SageMaker AI** trains several candidate models.
8. **Hyperparameter tuning** searches for improved model configurations.
9. **SageMaker Clarify** evaluates bias and explainability.
10. An approved model is recorded in the **SageMaker Model Registry**.
11. **SageMaker Pipelines** automates evaluation and deployment.
12. The model is deployed to a **real-time SageMaker endpoint**.
13. Transactions are scored in real time by an application running on **Lambda**, ECS, or EC2.
14. Low-confidence transactions are routed to **Amazon A2I** for human review.
15. **SageMaker Model Monitor** checks for data drift and model-quality issues.
16. **CloudWatch** monitors endpoint latency and errors.
17. **CloudTrail**, IAM, KMS, and Config support auditability and security.

---

## Example 6: Image moderation and catalog enrichment

**Business use case:** Automatically screen user-uploaded images and enrich product metadata.

1. Images are uploaded to **Amazon S3**.
2. An S3 event invokes **AWS Lambda**.
3. **Amazon Rekognition** detects objects, scenes, unsafe content, and text.
4. **Amazon Textract** is called when the image contains a document or structured form.
5. Low-confidence or high-risk results are sent to **Amazon A2I**.
6. **Amazon Comprehend** analyzes any extracted text.
7. **Amazon Bedrock** generates a product description from the approved metadata.
8. Product records are stored in **Amazon DynamoDB** or **Amazon Aurora**.
9. Images and generated assets are served through **Amazon CloudFront**.
10. **AWS KMS** encrypts stored content.
11. **IAM** restricts which functions can read, write, or invoke AI services.
12. **CloudWatch** and **CloudTrail** provide monitoring and audit trails.

---

# High-Value Exam Selection Rules

- Choose **Amazon Bedrock** when the requirement is to use a foundation model without managing the underlying infrastructure.
- Choose **SageMaker AI** when the requirement is custom training, detailed ML lifecycle control, MLOps, or model monitoring.
- Choose **Amazon Personalize** for recommendations.
- Choose **Amazon Comprehend** for text analysis.
- Choose **Amazon Textract** for document extraction.
- Choose **Amazon Rekognition** for image and video analysis.
- Choose **Amazon Transcribe** for speech-to-text.
- Choose **Amazon Polly** for text-to-speech.
- Choose **Amazon Translate** for language translation.
- Choose **Amazon Lex** for structured conversational bots.
- Choose **Amazon A2I** when human review is required after an AI prediction.
- Choose **S3** for durable object-based datasets, documents, and model artifacts.
- Choose **DynamoDB** for scalable low-latency key-value or document access.
- Choose **Aurora or RDS** for relational transactions.
- Choose **Redshift** for data warehousing and analytical SQL.
- Choose **OpenSearch** for search, logs, and vector retrieval.
- Choose **CloudTrail** for API auditing.
- Choose **CloudWatch** for metrics, logs, alarms, and operational monitoring.
- Choose **AWS Config** for configuration compliance.
- Choose **Macie** for sensitive-data discovery in S3.
- Choose **Inspector** for software and workload vulnerability assessment.
- Choose **KMS** for encryption key management.
- Choose **Secrets Manager** for passwords, API keys, and secret rotation.
- Choose **IAM roles** for temporary, least-privilege access between AWS services.
- Use **AWS Budgets** for spending alerts and **Cost Explorer** for spending analysis.