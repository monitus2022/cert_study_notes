# S3 Event Notifications: Real-World Usage Patterns

In event-driven architectures, S3 Event Notifications eliminate the need for applications to constantly poll S3 buckets (`HeadObject` or `ListObjects`) to check if new files have arrived. Instead, S3 pushes a JSON event payload immediately when an event occurs (e.g., `s3:ObjectCreated:*` or `s3:ObjectRemoved:*`).

Here are four practical, real-world architecture examples ranging from data engineering pipelines to automated security workflows.

---

### 1. Automated ML Data Ingestion & Preprocessing (MLOps Pipeline)

* **The Problem:** Your application or crawler periodically dumps raw JSON or CSV trade logs into a "Landing Zone" S3 bucket. You need to validate, clean, and convert these files into Apache Parquet before inserting them into a Feature Store or Data Lake.
* **Architecture Flow:**

$$\text{S3 Landing Bucket} \xrightarrow{\text{ObjectCreated}} \text{SQS Queue} \xrightarrow{\text{Batching}} \text{AWS Lambda / Glue} \xrightarrow{} \text{S3 Curated Bucket}$$


* **How it works:**
1. A file lands in `s3://my-app-landing-zone/raw_logs/`.
2. S3 sends a notification directly to an **Amazon SQS Queue**.
3. SQS buffers the event messages. If 500 files arrive at once, SQS holds them safely without crashing downstream servers.
4. An **AWS Lambda** function (or AWS Batch job) polls SQS in batches of 10, validates the schema, transforms the data into Parquet, and writes it to `s3://my-app-curated/`.


* **Why SQS is crucial here:** SQS provides rate limiting, concurrency control, and a **Dead-Letter Queue (DLQ)** so corrupt or malformed files don't crash your pipeline and can be inspected later.

---

### 2. Multi-Service Fan-Out Media Processing (SNS + SQS Pattern)

* **The Problem:** When a user uploads an image to an e-commerce platform, three separate microservices must react:
1. Generate responsive thumbnail sizes.
2. Run Amazon Rekognition to detect explicit content or auto-tag product categories.
3. Update the item's status in an Amazon DynamoDB database.


* **Architecture Flow:**

$$\text{S3 Upload Bucket} \xrightarrow{\text{ObjectCreated}} \text{SNS Topic} \begin{cases} \rightarrow \text{SQS Queue A} \rightarrow \text{Thumbnail Lambda} \\ \rightarrow \text{SQS Queue B} \rightarrow \text{Rekognition Lambda} \\ \rightarrow \text{SQS Queue C} \rightarrow \text{DynamoDB Updater} \end{cases}$$


* **How it works:**
1. S3 publishes the `ObjectCreated` notification to an **Amazon SNS Topic** (Publish-Subscribe pattern).
2. The SNS Topic "fans out" the exact same message to three independent **SQS Queues**.
3. Each dedicated worker service processes its assigned queue independently at its own pace.


* **Why SNS + SQS is crucial here:** Loose coupling. If the Rekognition service fails or experiences a backlog, the Thumbnail generation service continues operating without any interruption or dependency.

---

### 3. File Scanning & Security Quarantine (Enterprise Ingestion)

* **The Problem:** A public-facing web portal allows job applicants or bank customers to upload PDF documents. You must ensure files are free of malware before moving them to internal storage.
* **Architecture Flow:**

$$\text{S3 Quarantine Bucket} \xrightarrow{\text{ObjectCreated}} \text{SQS Queue} \rightarrow \text{Fargate Scanner} \begin{cases} \xrightarrow{\text{Clean}} \text{S3 Production Bucket} \\ \xrightarrow{\text{Infected}} \text{S3 Isolation / Alert} \end{cases}$$


* **How it works:**
1. Users upload files directly to an isolated `s3://quarantine-bucket/`.
2. S3 triggers an event to SQS, which invokes an **AWS Fargate** container running an antivirus engine (like ClamAV) or Amazon GuardDuty Malware Protection.
3. The scanner inspects the S3 file:
* **If Clean:** Moves the object to `s3://production-data-bucket/` and grants read access.
* **If Infected:** Deletes the file immediately and fires an SNS notification to the security team's Slack channel.





---

### 4. Continuous Model Training (Automated Retraining Loop)

* **The Problem:** You want your SageMaker machine learning model to automatically retrain whenever ground-truth annotation labels reach a specific threshold in S3.
* **Architecture Flow:**

$$\text{S3 Ground Truth Bucket} \xrightarrow{\text{ObjectCreated}} \text{EventBridge Rule} \rightarrow \text{SageMaker Pipeline / Step Functions}$$


* **How it works:**
1. Human annotators or automated labeling pipelines upload new ground-truth dataset files to S3.
2. Using **Amazon EventBridge** (the modern evolution of S3 Event Notifications), an EventBridge rule filters for specific prefixes (`/ground-truth/v2/`).
3. EventBridge triggers an **AWS Step Functions** workflow that launches a **SageMaker Training Job** or executes a **SageMaker Pipeline** execution DAG.



---

### Key Exam / Architecture Rule: S3 Notifications vs. EventBridge

When designing these solutions on AWS, choose the event mechanism based on integration needs:

| Feature | S3 Event Notifications | Amazon EventBridge (S3 Event Notifications) |
| --- | --- | --- |
| **Destinations** | SQS, SNS, AWS Lambda only | 20+ AWS targets (Step Functions, Kinesis, ECS, API Destinations, etc.) |
| **Filtering** | Limited (Prefix and Suffix filtering like `.jpg` or `logs/`) | Advanced JSON payload pattern matching (e.g., filter by file size or specific tags) |
| **Cross-Account** | Requires complex resource policies | Native cross-account event routing via Event Bus |
| **Delivery Guarantee** | At-least-once delivery | At-least-once delivery with built-in retry policies and DLQs |