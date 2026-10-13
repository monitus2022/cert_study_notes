# AWS Certified Machine Learning Engineer - Associate (MLA-C02)
## Official Practice Question Set (20 Questions)

---

### Question 1

**Category:** MLA – Operating, Monitoring, and Securing ML and AI Solutions

A manufacturing company is training an experimental deep learning model for factory floor safety purposes. The model analyzes monitoring camera images to verify if workers are wearing safety helmets during work hours. Currently, the company trains the model on Amazon SageMaker AI by using On-Demand GPU Instances. The company wants to find methods to minimize model training costs without future financial commitment.

Which solution will meet these requirements?

* **A)** Use SageMaker AI Savings Plans.
* **B)** Use managed spot training in SageMaker AI.
* **C)** Use SageMaker Canvas for model training.
* **D)** Use Amazon Managed Workflows for Apache Airflow (Amazon MWAA) for model training.

??? note "Click to reveal Answer & Explanation"
    **Correct Answer:** **B**

    #### Correct Option Analysis
    * **B is Correct:** Managed spot training uses EC2 Spot Instances managed automatically by SageMaker AI to run training jobs using spare EC2 capacity at up to a 90% discount without any long-term financial commitment.

    #### Distractor Analysis
    * **A is Incorrect:** SageMaker Savings Plans require a 1-year or 3-year financial commitment.
    * **C is Incorrect:** SageMaker Canvas is a visual no-code tool for building ML models, not a cost-optimization feature for custom deep learning container jobs.
    * **D is Incorrect:** MWAA is an orchestration tool for Apache Airflow workflows, not a compute service for training models.

    > **Key Decision Rule:** Low cost + No financial commitment for training $
ightarrow$ **Managed Spot Training in SageMaker AI**.

---

### Question 2

**Category:** MLA – Deployment and Orchestration of ML and AI Workflows

A company built a deep learning model for climate modeling by using Amazon SageMaker AI. In each invocation, the model processes 400 MB of data for 30 minutes to return a prediction. The climate model is invoked automatically when a new climate event is detected. The company needs a deployment strategy to move the deep learning model to production. A cold start can be tolerated.

What is the MOST cost-effective solution?

* **A)** Deploy the model by using an asynchronous endpoint.
* **B)** Deploy the model by using a serverless endpoint.
* **C)** Deploy the model by using a batch transform.
* **D)** Deploy the model by using a real-time endpoint.

??? note "Click to reveal Answer & Explanation"
    **Correct Answer:** **A**

    #### Correct Option Analysis
    * **A is Correct:** SageMaker Asynchronous Inference is designed for large payloads (up to 1 GB) and long processing times (up to 1 hour) where requests are queued and processed asynchronously, and cold starts can be tolerated.

    #### Distractor Analysis
    * **B is Incorrect:** Serverless Inference has payload limits (6 MB) and timeout limits (60 seconds); a 30-minute processing run on 400 MB will time out.
    * **C is Incorrect:** Batch transform is for offline datasets, not event-driven live invocations triggered when a climate event occurs.
    * **D is Incorrect:** Real-time endpoints have a 6 MB payload limit and a 60-second response timeout.

    > **Key Decision Rule:** Large payload (>6 MB) + Long execution time (up to 1 hr) + Cold start tolerated $
ightarrow$ **SageMaker Asynchronous Endpoint**.

---

### Question 3

**Category:** MLA – Deployment and Orchestration of ML and AI Workflows

A company hosts many ML models that support unique use cases that have dynamic workloads. All the models were trained by using the same ML framework. The models are hosted on Amazon SageMaker dedicated endpoints that are underutilized. The company has a goal to optimize its environment for cost.

Which solution will meet these requirements MOST cost-effectively?

* **A)** Configure the dedicated endpoints by using smaller instances.
* **B)** Configure a SageMaker AI multi-container endpoint.
* **C)** Configure a SageMaker AI multi-model endpoint.
* **D)** Configure an inference pipeline behind a SageMaker AI endpoint.

??? note "Click to reveal Answer & Explanation"
    **Correct Answer:** **C**

    #### Correct Option Analysis
    * **C is Correct:** SageMaker Multi-Model Endpoints (MME) host thousands of models built on the same ML framework inside a single shared container on a single endpoint, dramatically reducing hosting costs for underutilized or dynamic models.

    #### Distractor Analysis
    * **A is Incorrect:** Using smaller instances still maintains separate dedicated endpoints per model, retaining high infrastructure overhead.
    * **B is Incorrect:** Multi-container endpoints are meant for models built on *different* ML frameworks (e.g., PyTorch + Scikit-Learn).
    * **D is Incorrect:** Inference pipelines pass data sequentially from one model to the next, which is incorrect for independent, unique use cases.

    > **Key Decision Rule:** Multiple models + Same framework + Intermittent traffic $
ightarrow$ **SageMaker Multi-Model Endpoint (MME)**.

---

### Question 4

**Category:** MLA – Operating, Monitoring, and Securing ML and AI Solutions

A company wants to manage team members' access to Amazon SageMaker Studio in a SageMaker domain. The company wants to restrict access to SageMaker Feature Store in the production account.

Which solution effectively restricts access?

* **A)** Use network access control lists (network ACLs) to block network traffic to the SageMaker Feature Store.
* **B)** Create an IAM policy that explicitly denies access to the SageMaker Feature Store. Associate the IAM policy with the team members' group.
* **C)** Disable the SageMaker Feature Store in the SageMaker Studio environment settings when creating the SageMaker domain.
* **D)** Configure Amazon CloudWatch to send alerts when an attempt is made to access the SageMaker Feature Store.

??? note "Click to reveal Answer & Explanation"
    **Correct Answer:** **B**

    #### Correct Option Analysis
    * **B is Correct:** AWS Identity and Access Management (IAM) controls service action permissions. An explicit `Deny` policy on SageMaker Feature Store API actions assigned to the user group enforces least-privilege security.

    #### Distractor Analysis
    * **A is Incorrect:** Network ACLs filter IP traffic at the subnet boundary; they cannot restrict API-level access to AWS services.
    * **C is Incorrect:** SageMaker domain environment settings do not feature a toggle to disable Feature Store APIs.
    * **D is Incorrect:** CloudWatch provides monitoring alerts after the fact; it does not block or prevent unauthorized access.

    > **Key Decision Rule:** Restrict access to specific AWS actions/services $
ightarrow$ **IAM Policy with Explicit Deny**.

---

### Question 5

**Category:** MLA – Data Preparation for ML and AI

A global automotive company wants to reduce the manual work of parsing information from scanned PDFs. The company wants a managed solution that automatically extracts information from scanned PDFs. The information includes addresses, names, and license plate numbers.

Which solution will meet these requirements?

* **A)** Use the DetectDocumentText API operation on Amazon Textract.
* **B)** Use the DetectText API operation on Amazon Rekognition.
* **C)** Use the custom entity recognition feature of Amazon Comprehend.
* **D)** Use the large language model (LLM) Mistral Large in Amazon Bedrock.

??? note "Click to reveal Answer & Explanation"
    **Correct Answer:** **A**

    #### Correct Option Analysis
    * **A is Correct:** **Amazon Textract** is specifically designed to extract printed text, handwriting, and structured data from scanned PDF documents and images via `DetectDocumentText` or `AnalyzeDocument`.

    #### Distractor Analysis
    * **B is Incorrect:** Amazon Rekognition detects text in standalone image/video formats, not multi-page scanned PDF documents.
    * **C is Incorrect:** Amazon Comprehend extracts entities from raw unstructured text strings, but does not extract raw text out of PDF files.
    * **D is Incorrect:** Mistral Large on Bedrock is a conversational text LLM, not a native OCR engine for parsing scanned PDF documents.

    > **Key Decision Rule:** Extract text / OCR from scanned PDFs $
ightarrow$ **Amazon Textract (`DetectDocumentText`)**.

---

### Question 6

**Category:** MLA – Operating, Monitoring, and Securing ML and AI Solutions

An ML engineer is using Amazon SageMaker Canvas to process a structured dataset. The dataset is stored in an Amazon S3 bucket and includes personally identifiable information (PII). To avoid leaks of the PII, the ML engineer must ensure that the data does not traverse the public internet.

Which solution will meet these requirements?

* **A)** Configure the SageMaker AI domain in VPC only mode. Use Amazon Comprehend to identify and redact PII.
* **B)** Use server-side encryption with AWS KMS keys (SSE-KMS) to encrypt the S3 bucket. Specify an AWS KMS key.
* **C)** Configure the SageMaker AI domain in VPC only mode. Configure a VPC endpoint for Amazon S3.
* **D)** Configure an AWS Client VPN connection from the SageMaker AI domain to Amazon S3.

??? note "Click to reveal Answer & Explanation"
    **Correct Answer:** **C**

    #### Correct Option Analysis
    * **C is Correct:** Configuring the SageMaker domain in **VPC only mode** prevents SageMaker from accessing the public internet. Pairing this with a **VPC Endpoint for S3 (Gateway Endpoint)** keeps data traffic strictly inside the AWS internal network.

    #### Distractor Analysis
    * **A is Incorrect:** Without an S3 VPC endpoint, traffic leaving the VPC in VPC-only mode cannot reach S3. Redacting PII is not required when network isolation is implemented properly.
    * **B is Incorrect:** SSE-KMS protects data at rest in S3; it does not control network transit routing.
    * **D is Incorrect:** AWS Client VPN connects remote end-user laptops to a VPC, not a SageMaker domain to S3.

    > **Key Decision Rule:** Keep SageMaker traffic off the public internet to S3 $
ightarrow$ **VPC Only Mode + S3 VPC Endpoint**.

---

### Question 7

**Category:** MLA – ML Model and Foundation Model Development

A travel company is building a travel assistant solution in Amazon SageMaker AI to help travelers choose flights. The company wants to use ML to predict flight prices based on the travel dates, origin and destination airport, number of stops, and time of year.

Which SageMaker AI built-in algorithm should the company use to build the model?

* **A)** Linear learner algorithm
* **B)** Random Cut Forest (RCF) algorithm
* **C)** K-means algorithm
* **D)** Principal Component Analysis (PCA) algorithm

??? note "Click to reveal Answer & Explanation"
    **Correct Answer:** **A**

    #### Correct Option Analysis
    * **A is Correct:** Predicting a continuous numeric target variable (e.g., flight price) is a classic regression task. The SageMaker **Linear Learner** built-in algorithm supports linear regression.

    #### Distractor Analysis
    * **B is Incorrect:** Random Cut Forest (RCF) is an unsupervised algorithm for anomaly detection.
    * **C is Incorrect:** K-means is an unsupervised clustering algorithm.
    * **D is Incorrect:** PCA is an unsupervised dimensionality reduction algorithm.

    > **Key Decision Rule:** Predict continuous numerical target value $
ightarrow$ **SageMaker Linear Learner (Regression)**.

---

### Question 8

**Category:** MLA – Operating, Monitoring, and Securing ML and AI Solutions

An ML engineer developed an Amazon API Gateway API for file processing by using AWS Lambda functions. Some invocations have resulted in errors where users are not receiving the expected transformed files. The debugging process is time-consuming and complex. The ML engineer needs a solution that offers more granular details related to the invocation errors. Then, the ML engineer can identify and fix issues more quickly.

Which solutions will meet these requirements? (Select TWO.)

* **A)** Enable Amazon CloudWatch Lambda Insights.
* **B)** Set up Amazon CloudWatch alarms to detect API Gateway invocations.
* **C)** Separate workloads by testing new features on a development alias.
* **D)** Use AWS CloudTrail for all Lambda invocations.
* **E)** Enable AWS X-Ray tracing on API Gateway and Lambda.

??? note "Click to reveal Answer & Explanation"
    **Correct Answers:** **A** and **E**

    #### Correct Option Analysis
    * **A is Correct:** **CloudWatch Lambda Insights** provides system-level metrics (memory usage, CPU, cold starts, worker crashes) for serverless troubleshooting.
    * **E is Correct:** **AWS X-Ray** provides distributed tracing to visualize the request lifecycle across API Gateway and Lambda, highlighting performance bottlenecks and execution faults.

    #### Distractor Analysis
    * **B is Incorrect:** CloudWatch alarms notify when thresholds are breached; they do not collect granular execution traces or error root causes.
    * **C is Incorrect:** Lambda aliases route traffic between versions, but do not provide execution trace telemetry.
    * **D is Incorrect:** CloudTrail records control plane management API calls; it does not record internal application runtime errors or execution traces.

    > **Key Decision Rule:** Serverless microservice execution tracing & metrics $
ightarrow$ **AWS X-Ray + CloudWatch Lambda Insights**.

---

### Question 9

**Category:** MLA – Deployment and Orchestration of ML and AI Workflows

An ML engineer has a model that recently finished testing and validation. The model is replacing an existing working model. To minimize costs during deployment, the ML engineer will turn off the servers that are not needed during testing. However, the ML engineer needs the ability to roll back if issues are identified during deployment.

Which deployment strategy will meet these requirements MOST cost-effectively?

* **A)** Rolling deployment
* **B)** Shadow deployment
* **C)** All-at-once deployment
* **D)** Canary deployment

??? note "Click to reveal Answer & Explanation"
    **Correct Answer:** **A**

    #### Correct Option Analysis
    * **A is Correct:** A **rolling deployment** gradually replaces instances of the old version with the new version in batches. It maintains necessary capacity without running two full parallel fleets simultaneously, minimizing cost while allowing rollback.

    #### Distractor Analysis
    * **B is Incorrect:** Shadow deployment duplicates 100% of live traffic to a full shadow fleet running in parallel, doubling infrastructure costs.
    * **C is Incorrect:** All-at-once deployment replaces the entire fleet at once, creating a window where both full fleets are active during baking, incurring higher cost.
    * **D is Incorrect:** Canary deployment provisions a full parallel green fleet upfront before routing a small percentage of traffic.

    > **Key Decision Rule:** Lowest cost deployment with rollback capability $
ightarrow$ **Rolling Deployment**.

---

### Question 10

**Category:** MLA – Deployment and Orchestration of ML and AI Workflows

An ecommerce company designed an ML recommendation system to suggest similar products to customers that visit a product page. The system was deployed by using an Amazon SageMaker AI endpoint. After the system deployment, traffic has increased sporadically throughout the day. An ML engineer must implement a solution that uses auto scaling policies to better handle the increasing traffic without compromising customer experience.

Which solution will meet these requirements?

* **A)** Use a target tracking scaling policy based on a custom metric and a target value to scale instance count.
* **B)** Use a target tracking scaling policy to specify different instance types based on a predefined metric.
* **C)** Use a schedule-based scaling policy to scale instance count at different times during the day.
* **D)** Use a step scaling policy to specify different instance types based on demand.

??? note "Click to reveal Answer & Explanation"
    **Correct Answer:** **A**

    #### Correct Option Analysis
    * **A is Correct:** **Target tracking scaling policies** adjust the instance count dynamically to maintain a specified metric (e.g., `InvocationsPerInstance` or custom CPU metrics) at a target value for sporadic workloads.

    #### Distractor Analysis
    * **B & D are Incorrect:** Auto scaling policies increase or decrease the *number* of instances; they cannot dynamically change the *instance type*.
    * **C is Incorrect:** Schedule-based scaling is designed for predictable, fixed time cycles, not sporadic real-time traffic spikes.

    > **Key Decision Rule:** Dynamic/sporadic traffic auto-scaling for SageMaker endpoints $
ightarrow$ **Target Tracking Scaling Policy (instance count)**.

---

### Question 11

**Category:** MLA – Data Preparation for ML and AI

A company uses ML models on Amazon SageMaker AI to guide marketing campaigns. Training data comes from Amazon Redshift. The data preparation steps require joins, transformations, and data imputation to obtain training features. Data lineage must be preserved. The data science team expects a new set of features to be stored and versioned in SageMaker Feature Store at the beginning of every month so that they can build new models.

Which combination of steps meets these requirements with the LEAST code? (Select TWO.)

* **A)** Use SageMaker Data Wrangler to load the data and run transformations. Store features in Feature Store.
* **B)** Use SageMaker Pipelines to load training data and run all transformations. Store features in Feature Store.
* **C)** Use a pre-built template to create an AWS Glue for Spark job to load training data and run all transformations. Store features in Feature Store.
* **D)** Define the data pre-processing as a SageMaker processing job. Schedule to run monthly.
* **E)** Define the data pre-processing as a SageMaker Pipeline run. Schedule to run monthly.

??? note "Click to reveal Answer & Explanation"
    **Correct Answers:** **A** and **D**

    #### Correct Option Analysis
    * **A is Correct:** **SageMaker Data Wrangler** provides a no-code visual interface with built-in Redshift connectors, transformation routines, feature store exporting, and automatic data lineage tracking.
    * **D is Correct:** Data Wrangler flows can be exported and scheduled directly as recurring **SageMaker Processing Jobs** with zero manual pipeline scripting.

    #### Distractor Analysis
    * **B, C, & E are Incorrect:** SageMaker Pipelines and AWS Glue PySpark jobs require writing custom ETL code, violating the "least code" requirement.

    > **Key Decision Rules:**
    > * **Redshift ETL + Feature Store export + No-Code:** **SageMaker Data Wrangler**.
    > * **Automate recurring Data Wrangler flows:** **Schedule as SageMaker Processing Jobs**.

---

### Question 12

**Category:** MLA – Data Preparation / Storage Optimization

A company collects images from cameras on busy streets around the world. The images are ingested, labeled, and then stored in Amazon S3. The images will be accessed quarterly for the first year. After the first year, the images are no longer accessed, but must be retained for at least seven years for compliance reasons.

Which solution meets these requirements the MOST cost-effectively?

* **A)** As soon as the data is uploaded to Amazon S3, schedule an AWS Batch job to delete the images in seven years.
* **B)** Store the data on an Amazon EBS volume. Attach the Amazon EBS volume to an Amazon EC2 instance whenever you need to access the images.
* **C)** Use lifecycle configuration rules to send the images to Amazon S3 Glacier Flexible Retrieval for storage for the first year, and then to Amazon S3 Glacier Deep Archive after one year.
* **D)** Use lifecycle configuration rules to send the images to Amazon S3 Glacier Instant Retrieval for storage for the first year, and then to Amazon S3 Glacier Deep Archive after one year.

??? note "Click to reveal Answer & Explanation"
    **Correct Answer:** **D**

    #### Correct Option Analysis
    * **D is Correct:** **S3 Glacier Instant Retrieval** is tailored for long-lived archive data accessed infrequently (e.g., quarterly) requiring millisecond access. Transitioning to **S3 Glacier Deep Archive** after 1 year satisfies 7-year compliance at the lowest cost.

    #### Distractor Analysis
    * **C is Incorrect:** Glacier Flexible Retrieval is for data accessed 1–2 times per year max with asynchronous retrieval delays.
    * **A is Incorrect:** AWS Batch is a compute service, not an S3 lifecycle storage rule.
    * **B is Incorrect:** EBS volumes incur high ongoing block storage fees compared to S3 Glacier.

    > **Key Decision Rule:** Quarterly access with millisecond latency $
ightarrow$ **S3 Glacier Instant Retrieval** (then **Deep Archive** for 7-yr compliance).

---

### Question 13

**Category:** MLA – ML Model and Foundation Model Development

An AI engineer uses an Amazon Nova Premier model for a specialized language understanding task. The model performs accurately. However, the AI engineer needs to reduce inference latency and cost.

Which solution will meet these requirements?

* **A)** Deploy a fine-tuned Amazon Nova Premier model.
* **B)** Deploy multiple instances of the model across different Availability Zones.
* **C)** Create and deploy a distilled version of the Amazon Nova Premier model.
* **D)** Create a Retrieval Augmented Generation (RAG) architecture by using Amazon Bedrock Knowledge Bases and the Amazon Nova Premier model.

??? note "Click to reveal Answer & Explanation"
    **Correct Answer:** **C**

    #### Correct Option Analysis
    * **C is Correct:** **Model distillation** transfers knowledge from a large teacher model (Nova Premier) into a smaller, faster student model, significantly lowering inference latency and serving costs while retaining task accuracy.

    #### Distractor Analysis
    * **A is Incorrect:** Fine-tuning adjusts weights for task accuracy but does not reduce model size, latency, or cost.
    * **B is Incorrect:** Multi-AZ deployment increases availability, but doubles infrastructure cost.
    * **D is Incorrect:** RAG adds retrieval lookup steps, which increases latency rather than reducing it.

    > **Key Decision Rule:** Reduce LLM inference latency and serving cost while maintaining accuracy $
ightarrow$ **Model Distillation**.

---

### Question 14

**Category:** MLA – Operating, Monitoring, and Securing ML and AI Solutions

A financial services company deploys a fine-tuned large language model (LLM) on an Amazon SageMaker AI endpoint. The model analyzes transaction descriptions and generates fraud risk assessments. An AI engineer develops a new version of the fine-tuned model to improve detection accuracy.

The company wants to evaluate the new model in a controlled manner in production. The company wants to use real transaction traffic in the evaluation before replacing the existing model. The AI engineer must be able to compare the performance of both models in real time.

Which solution will meet these requirements?

* **A)** Store predictions from both models in Amazon S3. Periodically analyze the results by using Amazon Athena.
* **B)** Deploy the new model to a new SageMaker AI endpoint. Compare prediction results from both endpoints by using test datasets.
* **C)** Deploy the new model as a separate production variant on the SageMaker AI endpoint. Use weighted traffic routing to perform A/B testing.
* **D)** Replace the existing model with the new model on the SageMaker AI endpoint. Monitor Amazon CloudWatch metrics to evaluate performance.

??? note "Click to reveal Answer & Explanation"
    **Correct Answer:** **C**

    #### Correct Option Analysis
    * **C is Correct:** SageMaker endpoints natively support **Production Variants** on a single endpoint. Configuring weighted traffic routing routes live production traffic between candidate model versions for real-time **A/B testing**.

    #### Distractor Analysis
    * **A & B are Incorrect:** Creating separate endpoints or running offline batch evaluations adds infrastructure overhead and lacks native live traffic splitting capabilities.
    * **D is Incorrect:** Replacing the existing model directly prevents side-by-side performance comparison on live traffic.

    > **Key Decision Rule:** Live A/B testing on real traffic with lowest overhead $
ightarrow$ **Production Variants on 1 SageMaker Endpoint**.

---

### Question 15

**Category:** MLA – Operating, Monitoring, and Securing ML and AI Solutions

A pharmaceutical company uses Amazon Bedrock Knowledge Bases to power a Retrieval Augmented Generation (RAG) based assistant. The assistant answers questions about drug interactions. The company verified that the assistant retrieves the correct documents from the knowledge base. Before releasing the assistant to a larger audience, the company wants to evaluate for hallucinations in the responses. The company will run an Amazon Bedrock knowledge base evaluation job.

Which evaluation job configuration will meet these requirements?

* **A)** Select the retrieval only evaluation type. Configure the context relevance and context coverage metrics.
* **B)** Select the retrieval and response generation evaluation type. Configure the citation coverage and completeness metrics.
* **C)** Select the retrieval and response generation evaluation type. Configure the helpfulness and correctness metrics.
* **D)** Select the retrieval and response generation evaluation type. Configure the faithfulness metric.

??? note "Click to reveal Answer & Explanation"
    **Correct Answer:** **D**

    #### Correct Option Analysis
    * **D is Correct:** To evaluate whether a model's generated response contains **hallucinations**, choose **Retrieval and Response Generation** evaluation with the **`faithfulness`** metric, which measures whether model outputs are grounded strictly in the retrieved context.

    #### Distractor Analysis
    * **A is Incorrect:** Retrieval-only evaluation evaluates search results, not downstream LLM generation hallucinations.
    * **B is Incorrect:** Citation coverage and completeness measure answer thoroughness, not ungrounded factual hallucinations.
    * **C is Incorrect:** Helpfulness and correctness measure general utility against user queries, not context hallucination.

    > **Key Decision Rule:** Detect GenAI / RAG hallucinations $
ightarrow$ **Retrieval and Response Generation + Faithfulness Metric**.

---

### Question 16

**Category:** MLA – ML Model and Foundation Model Development

During the training process of a deep neural network, a data scientist observes that the training loss decreases with each epoch. After many epochs, the data scientist observes that the validation loss increases.

What actions can the data scientist implement to mitigate this issue? (Select TWO.)

* **A)** Add more layers to the network.
* **B)** Increase the number of epochs.
* **C)** Implement early stopping.
* **D)** Use the dropout technique.
* **E)** Add more neurons to each layer.

??? note "Click to reveal Answer & Explanation"
    **Correct Answers:** **C** and **D**

    #### Correct Option Analysis
    * **C is Correct:** **Early stopping** halts training when validation loss degrades, preventing overfitting.
    * **D is Correct:** **Dropout** randomly deactivates neurons during training, acting as a regularization technique to improve generalization.

    #### Distractor Analysis
    * **A & E are Incorrect:** Adding layers or neurons increases model capacity, worsening overfitting.
    * **B is Incorrect:** Increasing epochs allows training to run further past divergence, exacerbating overfitting.

    > **Key Decision Rule:** Validation loss increases while training loss decreases (Overfitting) $
ightarrow$ **Early Stopping + Dropout**.

---

### Question 17

**Category:** MLA – ML Model and Foundation Model Development

An industrial company is exploring the use of generative AI to retrieve information from maintenance notes. The company currently uses a text-to-text foundation model (FM) on Amazon Bedrock. The company wants to optimize the model. The company wants to help the model better understand the terminology and abbreviations that maintenance technicians use.

What is the MOST cost-effective solution to help the model understand the company's data?

* **A)** Replace the model with a new model that has more parameters.
* **B)** Pre-train a new FM by using the Amazon SageMaker AI model parallelism library.
* **C)** Create an Amazon Bedrock Knowledge Base.
* **D)** Customize the model by using fine-tuning.

??? note "Click to reveal Answer & Explanation"
    **Correct Answer:** **D**

    #### Correct Option Analysis
    * **D is Correct:** **Fine-tuning** adapts a model's internal weights using domain-specific labeled examples. It is the most cost-effective method to teach a model **specialized terminology, abbreviations, and internal jargon**.

    #### Distractor Analysis
    * **C is Incorrect:** Amazon Bedrock Knowledge Bases (RAG) retrieves external document chunks, but does not adapt the base model's internal understanding of specialized jargon/shorthand.
    * **A is Incorrect:** Larger parameters do not guarantee knowledge of proprietary company abbreviations.
    * **B is Incorrect:** Pre-training from scratch requires massive data curation and compute cost compared to fine-tuning.

    > **Key Decision Rule:** Teach model specialized domain jargon, abbreviations, or style $
ightarrow$ **Fine-Tuning**.

---

### Question 18

**Category:** MLA – Operating, Monitoring, and Securing ML and AI Solutions

An AI engineer is building a generative AI (GenAI) application on Amazon Bedrock. The application will generate customer support responses. The AI engineer needs to ensure that the foundation model (FM) follows specific role-based instructions. The FM must comply with responsible AI policies. The FM must produce consistently formatted responses.

Which solution will meet these requirements?

* **A)** Use Amazon Bedrock Prompt Management to define role-based instructions. Use Amazon Bedrock AgentCore to enforce responsible AI policies. Create custom AWS Lambda functions for response formatting.
* **B)** Use Amazon Bedrock Knowledge Bases to define role-based instructions. Use prompt templates to enforce responsible AI policies. Set up Amazon Bedrock Guardrails for response formatting.
* **C)** Use Amazon Bedrock AgentCore to define role-based instructions. Set up an Amazon Bedrock knowledge base to enforce responsible AI policies. Use prompt templates for response formatting.
* **D)** Use Amazon Bedrock Prompt Management to define role-based instructions. Set up Amazon Bedrock Guardrails to enforce responsible AI policies. Use prompt templates to standardize response formatting.

??? note "Click to reveal Answer & Explanation"
    **Correct Answer:** **D**

    #### Correct Option Analysis
    * **D is Correct:**
      1. **Bedrock Prompt Management:** Defines role-based system instructions for persona behavior.
      2. **Bedrock Guardrails:** Enforces responsible AI policies (filtering harmful content, PII, denied topics).
      3. **Prompt Templates:** Standardizes response formatting and output structure natively.

    #### Distractor Analysis
    * **A, B, & C are Incorrect:** Misassign Bedrock capabilities (e.g., using Knowledge Bases for role-based instructions or Guardrails for response formatting).

    > **Key Decision Rules:**
    > * **Role-based instructions:** **Prompt Management**.
    > * **Responsible AI policies & safety:** **Amazon Bedrock Guardrails**.
    > * **Standardized response structure:** **Prompt Templates**.

---

### Question 19

**Category:** MLA – Data Preparation for ML and AI

An ML engineer must identify pre-training bias in a dataset that contains thousands of rows. Given a particular feature, the ML engineer must be able to determine if one of the values is overrepresented. If bias is detected because of a class imbalance (CI), the ML engineer must be able to remediate the bias by using the appropriate transformation.

Which solution will meet these requirements with the LEAST operational overhead?

* **A)** Compute the CI between different facet values in an Amazon SageMaker AI notebook instance. If the values are spread away from 0, apply the SMOTE function in imblearn to remediate bias.
* **B)** Use Amazon Athena to query features in the Amazon SageMaker Feature Store to identify and remediate bias.
* **C)** Use Amazon SageMaker Profiler to build a profile of the raw dataset and identify bias. Use the SMOTE function in imblearn to remediate bias.
* **D)** Use Amazon SageMaker Data Wrangler to generate a bias report. Based on the results from the report, use the SageMaker Data Wrangler SMOTE transformation to remediate bias.

??? note "Click to reveal Answer & Explanation"
    **Correct Answer:** **D**

    #### Correct Option Analysis
    * **D is Correct:** **SageMaker Data Wrangler** provides built-in visual **Bias Reports** to compute pre-training bias metrics (Class Imbalance) and native **SMOTE transformations** to oversample minority classes with zero custom code.

    #### Distractor Analysis
    * **A is Incorrect:** Writing custom Python functions in a notebook introduces manual coding overhead.
    * **B is Incorrect:** Athena queries data in Feature Store; it does not compute ML bias metrics or perform SMOTE oversampling.
    * **C is Incorrect:** SageMaker Profiler monitors CPU/GPU resource utilization during model training, not dataset bias.

    > **Key Decision Rule:** Detect pre-training dataset bias + remediate via SMOTE with minimal code $
ightarrow$ **SageMaker Data Wrangler Bias Report + SMOTE Transformation**.

---

### Question 20

**Category:** MLA – ML Model and Foundation Model Development

An ML engineer wants to use Amazon SageMaker AI to train an image classification model. The model uses a large dataset that is stored in Amazon S3. The dataset consists of millions of small 4K files that store images. The ML engineer needs a solution that starts up quickly and reduces training times to run subsequent iterations.

Which solution will meet these requirements with the HIGHEST performance?

* **A)** Apply Principal Component Analysis (PCA) on the S3 training data to reduce the file size.
* **B)** Transfer the training data from Amazon S3 to Amazon EFS. Use Amazon EFS to store the training data.
* **C)** Use Amazon FSx for Lustre to store the S3 training data.
* **D)** Split the S3 training data into batches.

??? note "Click to reveal Answer & Explanation"
    **Correct Answer:** **C**

    #### Correct Option Analysis
    * **C is Correct:** **Amazon FSx for Lustre** is a high-performance parallel file system linked directly to Amazon S3. It eliminates S3 API request limits on millions of small files, providing high IOPS and throughput to maximize GPU training speed and minimize startup times.

    #### Distractor Analysis
    * **A is Incorrect:** PCA reduces feature dimensions on tabular data; it does not optimize image file I/O performance on S3.
    * **B is Incorrect:** Amazon EFS requires copying data to a NFS file system and does not offer the massive parallel throughput of FSx for Lustre.
    * **D is Incorrect:** Splitting data into manual batches increases overall training time and S3 request overhead.

    > **Key Decision Rule:** High-performance training on millions of small files in S3 $
ightarrow$ **Amazon FSx for Lustre**.