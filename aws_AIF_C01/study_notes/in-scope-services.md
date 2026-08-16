# Analytics

| AWS Service / Feature | Description | Example Use Case |
| :--- | :--- | :--- |
| AWS Data Exchange | Managed service to find, subscribe to, and import third-party datasets directly into AWS data lakes and analytics workflows. | Subscribing to third-party financial or demographic datasets to enrich AI model training data. |
| Amazon EMR | Big data platform for processing massive datasets using open-source frameworks like Apache Spark, Hive, and Presto. | Running distributed ETL and preprocessing pipelines across terabytes of raw telemetry data before training models. |
| AWS Glue | Serverless data integration service that automates ETL workflows, data preparation, and metadata cataloging. | Automatically crawling S3 buckets to build a unified catalog and preparing structured data for ML training. |
| AWS Glue DataBrew | Visual data preparation tool allowing analysts to clean, normalize, and transform datasets without writing code. | Applying pre-built data cleaning recipes to handle missing values and deduplicate data prior to ML modeling. |
| AWS Lake Formation | Centralized service to quickly set up, secure, and govern data lakes with fine-grained row- and column-level access control. | Enforcing column-level permissions so data science teams can query data lakes without viewing PII. |
| Amazon OpenSearch Service | Managed search engine with vector database capabilities for high-performance vector similarity search. | Serving as the vector store for RAG applications to execute fast semantic search over document embeddings. |
| Amazon Quick | AI-powered assistant for business intelligence, research, business insights, automation, and dashboard generation. | Enabling business analysts to generate visualizations and ask natural language questions about sales data. |
| Amazon Redshift | Enterprise cloud data warehouse for fast, SQL-based analytical querying across petabytes of structured data. | Querying historical customer transactions to extract features for predictive churn models. |

# Cloud Financial Management

| AWS Service / Feature | Description | Example Use Case |
| :--- | :--- | :--- |
| AWS Budgets | Cost management tool to set custom spending limits and receive automated alerts when thresholds are breached. | Setting an alert to trigger when monthly Amazon Bedrock token spend exceeds budget limits. |
| AWS Cost Explorer | Visual analytics tool to review, analyze, and forecast AWS spending patterns and usage trends over time. | Tracking daily spending trends across SageMaker endpoints and Bedrock models to detect cost anomalies. |

# Compute

| AWS Service / Feature | Description | Example Use Case |
| :--- | :--- | :--- |
| Amazon EC2 | Scalable virtual compute instances providing access to specialized GPU (`g5`, `p5`) and AWS silicon (`trn1`, `inf2`). | Hosting self-managed deep learning model training jobs or custom open-source inference runtimes. |
| AWS Lambda | Serverless compute service that runs code in response to events without provisioning or managing servers. | Serving as the backend execution tool for AI agents to invoke external APIs or database queries. |

# Containers

| AWS Service / Feature | Description | Example Use Case |
| :--- | :--- | :--- |
| Amazon Elastic Container Service (Amazon ECS) | Fully managed container orchestration service for running Docker containers at scale. | Deploying containerized AI microservices and web APIs on serverless AWS Fargate compute. |
| Amazon Elastic Kubernetes Service (Amazon EKS) | Managed Kubernetes service for running containerized applications and distributed ML workloads. | Orchestrating multi-node distributed deep learning training clusters using open-source Kubernetes tools. |

# Database

| AWS Service / Feature | Description | Example Use Case |
| :--- | :--- | :--- |
| Amazon Aurora | Cloud-native relational database (PostgreSQL/MySQL compatible) supporting `pgvector` for vector storage. | Storing transactional application data alongside vector embeddings for unified SQL and semantic search. |
| Amazon DocumentDB (with MongoDB compatibility) | Managed NoSQL document database supporting JSON data models and vector search capabilities. | Storing unstructured JSON user profiles and executing vector similarity search over text fields. |
| Amazon DynamoDB | Serverless, fully managed NoSQL key-value database delivering single-digit millisecond performance. | Storing real-time conversation history, memory state, and session contexts for AI agents. |
| Amazon ElastiCache | In-memory caching service (Redis/Memcached) for accelerating database reads and managing fast session state. | Caching frequent LLM prompt completions or vector search results to reduce response latency and token costs. |
| Amazon Neptune | Managed graph database service engineered to store and query highly connected datasets and knowledge graphs. | Querying entity relationships in knowledge graphs to enrich context for graph-augmented RAG applications. |
| Amazon RDS | Managed relational database supporting engines like PostgreSQL with `pgvector` extension capabilities. | Storing structured enterprise data while performing vector similarity search via `pgvector`. |

# Developer Tools

| AWS Service / Feature | Description | Example Use Case |
| :--- | :--- | :--- |
| Kiro | AI-assisted development workspace tool designed to accelerate code generation and software development workflows. | Generating boilerplate software code and streamlining developer workflows within coding environments. |
| Strands Agents | Developer framework and runtime for building, securing, and orchestrating resilient multi-agent software workflows. | Coordinating specialized AI agents that collaboratively write code, execute unit tests, and review security flaws. |
| Amazon Q | Generative AI-powered assistant for work that helps developers, IT teams, and business users answer questions and generate code. | Asking architectural questions about AWS services or generating unit tests in an IDE via Amazon Q Developer. |

# Machine Learning

| AWS Service / Feature | Description | Example Use Case |
| :--- | :--- | :--- |
| Amazon Augmented AI (Amazon A2I) | Managed service that coordinates human-in-the-loop review workflows for low-confidence ML predictions or AI responses. | Automatically routing low-confidence document extraction or sensitive LLM outputs to human operators for review. |
| Amazon Bedrock | Serverless API platform offering access to leading foundation models (FMs) from third-party providers and Amazon. | Building generative AI applications, text summarizers, and RAG systems without managing infrastructure. |
| Amazon Bedrock AgentCore | Managed runtime framework for building, executing, securing, and orchestrating multi-agent enterprise workflows. | Running production AI agents with built-in identity management, session isolation, and tool execution guardrails. |
| Amazon Comprehend | Natural language processing (NLP) service that extracts insights, sentiment, entities, and topics from unstructured text. | Analyzing customer review text to determine overall sentiment and categorize recurring product issues. |
| Amazon Lex | Service for building conversational AI interfaces (chatbots and voicebots) using natural language understanding (NLU). | Building automated voice and text chatbots for customer support routing and bank account inquiries. |
| Amazon Nova | Family of state-of-the-art foundation models delivering frontier intelligence, multimodal capabilities, and price-performance. | Generating multimodal assets and executing complex reasoning tasks at low latency and cost. |
| Amazon Personalize | Managed ML service that generates real-time personalized product recommendations, ranking, and content feeds. | Delivering tailored product recommendations on an e-commerce website based on past user behavior. |
| Amazon Polly | Text-to-speech (TTS) service that converts written text into natural, lifelike spoken audio across multiple languages. | Converting written news articles or blog posts into spoken audio for mobile app listeners. |
| Amazon Rekognition | Computer vision service that automates image and video analysis for facial recognition, object detection, and moderation. | Automatically scanning user-uploaded profile photos to detect and filter inappropriate content. |
| Amazon SageMaker AI | Comprehensive ML platform for building, training, fine-tuning, hosting, and monitoring custom models at scale. | Training, evaluating, and hosting a custom XGBoost model to predict customer credit risk. |
| Amazon SageMaker JumpStart | ML hub within SageMaker offering pre-built solution templates and one-click deployment/fine-tuning of open FMs. | Fine-tuning an open-weight foundation model on private company data with one-click deployment. |
| Amazon Textract | ML service that automatically extracts text, handwriting, tables, and structured form data from scanned documents and PDFs. | Extracting structured line items, invoice totals, and dates from scanned paper receipts. |
| Amazon Transcribe | Automatic speech recognition (ASR) service that converts spoken audio recordings into time-stamped text transcriptions. | Transcribing customer service phone calls to perform automated text analysis and quality auditing. |
| Amazon Translate | Neural machine translation service providing fast, accurate, and customizable language translation. | Translating customer support articles into multiple languages in real time for international users. |
| AWS Transform | Automated code modernization service using generative AI to refactor, upgrade, and migrate legacy software applications. | Refactoring and upgrading legacy Java application codebases to modern long-term support (LTS) versions. |

# Management and Governance

| AWS Service / Feature | Description | Example Use Case |
| :--- | :--- | :--- |
| AWS CloudTrail | Governance service that logs and records all user activity and API calls across AWS infrastructure for auditing. | Auditing all administrative and model invocation API calls (`InvokeModel`) for compliance tracking. |
| Amazon CloudWatch | Monitoring and observability service for collecting metrics, monitoring logs, and triggering automated alerts. | Tracking model inference latency, token usage metrics, and capturing operational invocation logs. |
| AWS Config | Service that continuously monitors and audits AWS resource configurations against defined security rules. | Automatically detecting and flagging unencrypted S3 buckets or public endpoints that drift from security baselines. |
| AWS Trusted Advisor | Automated tool that checks AWS environments against best practices for security, performance, and cost optimization. | Identifying idle SageMaker instances or unattached storage volumes to eliminate wasteful spending. |
| AWS Well-Architected Tool | Assessment tool that reviews workloads against AWS best practices (including the Machine Learning Lens). | Evaluating a generative AI application architecture against the security and cost pillars of the ML Lens. |

# Networking and Content Delivery

| AWS Service / Feature | Description | Example Use Case |
| :--- | :--- | :--- |
| Amazon CloudFront | Global content delivery network (CDN) that caches content and API responses for fast, low-latency delivery. | Accelerating static web frontend assets and caching public API responses for an AI web portal. |
| Amazon VPC | Isolated virtual network environment in the AWS Cloud to securely host resources and private endpoints. | Routing Bedrock API calls privately over AWS PrivateLink without exposing traffic to the public internet. |

# Security, Identity, and Compliance

| AWS Service / Feature | Description | Example Use Case |
| :--- | :--- | :--- |
| AWS Artifact | Compliance portal providing on-demand access to AWS security reports (SOC, ISO) and regulatory agreements. | Downloading AWS ISO/SOC compliance reports or signing a Business Associate Addendum (BAA) for HIPAA compliance. |
| AWS Identity and Access Management (IAM) | Access management service to securely control authentication and authorization for AWS resources. | Defining granular roles and least-privilege policies to grant applications access to invoke specific Bedrock models. |
| Amazon Inspector | Automated vulnerability management service that scans compute instances, container images, and Lambda functions for flaws. | Automatically scanning container images hosting ML inference code for software vulnerabilities before deployment. |
| AWS Key Management Service (AWS KMS) | Managed service to create and control cryptographic keys used to encrypt data at rest. | Encrypting S3 buckets, vector database indices, and SageMaker model artifacts with customer-managed keys. |
| Amazon Macie | Data security service that uses ML to discover, classify, and protect sensitive Personally Identifiable Information (PII) in S3. | Scanning S3 data lakes to identify and redact sensitive customer PII before indexing data for RAG. |
| AWS Secrets Manager | Service that helps store, rotate, and manage API keys, database passwords, and OAuth tokens securely. | Storing external API keys safely so AI agents can retrieve them during automated function calling. |

# Storage

| AWS Service / Feature | Description | Example Use Case |
| :--- | :--- | :--- |
| Amazon S3 | Highly durable object storage designed to store unstructured data, training files, model artifacts, and documents. | Storing raw PDF files, image datasets, and model weight artifacts used in Bedrock Knowledge Bases. |
| Amazon S3 Glacier | Ultra-low-cost storage class designed for long-term data archiving and regulatory data retention. | Archiving historical AI audit logs and training dataset snapshots for multi-year compliance retention. |