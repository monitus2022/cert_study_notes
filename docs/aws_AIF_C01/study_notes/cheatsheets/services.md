# AWS Certified AI Practitioner (AIF-C01) — 6-Layer AI System Architecture

========================================================================================
LAYER 1: INTERFACES, DEVELOPER TOOLS & APPLICATIONS
========================================================================================
- Enterprise AI & BI: Amazon Q, Amazon Quick
- Developer Workspaces & Refactoring: Kiro, Strands Agents, AWS Transform

                                  │
                                  ▼

========================================================================================
LAYER 2: MANAGED AI & GENERATIVE AI PLATFORM
========================================================================================
- Foundation Models & Agents: Amazon Bedrock, Amazon Bedrock AgentCore, Amazon Nova
- Vision & Document Intelligence: Amazon Rekognition, Amazon Textract
- Speech & Language APIs: Amazon Comprehend, Amazon Lex, Amazon Polly, Amazon Transcribe, Amazon Translate
- Personalization: Amazon Personalize

                                  │
                                  ▼

========================================================================================
LAYER 3: CUSTOM MACHINE LEARNING PLATFORM (SAGEMAKER ECOSYSTEM)
========================================================================================
- Core ML & Pre-built Models: Amazon SageMaker AI, Amazon SageMaker JumpStart
- Human-in-the-Loop Alignment: Amazon Augmented AI (Amazon A2I)

                                  │
                                  ▼

========================================================================================
LAYER 4: DATA FOUNDATION, VECTOR STORES & ANALYTICS PIPELINE
========================================================================================
- Primary Storage & Archival: Amazon S3, Amazon S3 Glacier
- Vector Databases & Knowledge Search:
    • Amazon OpenSearch Service (Default RAG Vector Engine)
    • Amazon Aurora / Amazon RDS (Relational + pgvector)
    • Amazon DocumentDB (JSON + Vector Search)
    • Amazon Neptune (Knowledge Graphs + Vector Search)
- In-Memory & Fast State Storage: Amazon DynamoDB (Session/Memory), Amazon ElastiCache (LLM Caching)
- Processing & Analytics Engines: AWS Glue, AWS Glue DataBrew, AWS Lake Formation, AWS Data Exchange, Amazon EMR, Amazon Redshift

                                  │
                                  ▼

========================================================================================
LAYER 5: COMPUTE, CONTAINERS & NETWORKING INFRASTRUCTURE
========================================================================================
- Execution Compute: AWS Lambda (Agent Function Calling), Amazon EC2 (GPU/AWS Silicon)
- Container Orchestration: Amazon ECS, Amazon EKS
- Network Isolation & Edge: Amazon VPC (AWS PrivateLink), Amazon CloudFront

========================================================================================
CROSS-CUTTING LAYER 6: SECURITY, COMPLIANCE, GOVERNANCE & COST MANAGEMENT
========================================================================================
- Access & Identity: AWS IAM, AWS KMS, AWS Secrets Manager
- Vulnerability & Data Protection: Amazon Macie (PII Detection), Amazon Inspector
- Auditing & Observability: AWS CloudTrail, Amazon CloudWatch, AWS Config, AWS Artifact, AWS Trusted Advisor, AWS Well-Architected Tool
- Financial Management: AWS Budgets, AWS Cost Explorer

# Service Interactions & Data Flow

[ User / Client Application ]
            │
            │  1. HTTPS Traffic / User Interface
            ▼
┌────────────────────────────────────────────────────────┐
│ Amazon CloudFront (Edge Delivery)                      │
└───────────────────────────┬────────────────────────────┘
                            │
                            │  2. Private Ingress
                            ▼
┌────────────────────────────────────────────────────────┐
│ Amazon VPC (Isolated Network Environment)              │
│                                                        │
│  AWS PrivateLink                                       │
│    ├── AWS IAM (Authentication & Authorization)        │
│    └── AWS Secrets Manager (API Credentials)           │
└───────────────────────────┬────────────────────────────┘
                            │
                            │  3. Model Request Invocation
                            ▼
┌────────────────────────────────────────────────────────┐
│ Amazon Bedrock (Serverless Generative AI Platform)     │
│                                                        │
│  ├── Guardrails for Amazon Bedrock (Safety & PII)      │
│  └── Amazon Bedrock AgentCore (Orchestration)          │
└───────────────┬────────────────────────┬───────────────┘
                │                        │
  4. Tool Calls │                        │ 5. Vector Context Retrieval
                ▼                        ▼
┌───────────────────────────────┐ ┌───────────────────────────────┐
│ AWS Lambda                    │ │ Amazon OpenSearch Service     │
│ (Executes Action APIs)        │ │ (Vector Search Engine)        │
└───────────────┬───────────────┘ └───────────────┬───────────────┘
                │                                │
                │ Write State                    │ Data Pipeline Source
                ▼                                ▼
┌───────────────────────────────┐ ┌───────────────────────────────┐
│ Amazon DynamoDB               │ │ Amazon S3 (Data Lake)         │
│ (Conversation Memory State)   │ │ ├── Amazon Macie (PII Audit)  │
└───────────────────────────────┘ │ └── AWS Glue (ETL Prep)       │
                                  └───────────────────────────────┘

========================================================================================
CONTINUOUS AUDITING & GOVERNANCE ENVELOPE (Applies to all calls above)
========================================================================================
• AWS CloudTrail  ──► Logs API invocations (e.g., InvokeModel, CreateAgent)
• Amazon CloudWatch ─► Captures latency metrics, token consumption, and runtime logs
• AWS Config      ──► Audits resource configurations for compliance drift
• AWS Cost Explorer ► Tracks real-time Bedrock token costs and compute spend