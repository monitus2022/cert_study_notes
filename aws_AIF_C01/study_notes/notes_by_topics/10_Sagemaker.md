# Amazon SageMaker — AIF-C01 Exam Preparation Notes

> **Exam context:** The AWS Certified AI Practitioner exam tests whether you understand the purpose, capabilities, and basic use cases of Amazon SageMaker. It does not generally require you to write SageMaker code or design highly specialized ML architectures.

Amazon SageMaker is a managed AWS service for building, training, tuning, deploying, monitoring, and governing machine learning models.

AWS documentation and product naming may refer to the service as **Amazon SageMaker**, **SageMaker AI**, or the broader **Amazon SageMaker platform**.

---

## 1. Key Amazon SageMaker Components

### High-level SageMaker machine learning lifecycle

```text
Collect data
    ↓
Store data in Amazon S3
    ↓
Prepare and label data
    ↓
Build or select a model
    ↓
Train and tune the model
    ↓
Evaluate and register the model
    ↓
Deploy for inference
    ↓
Monitor and retrain
```

---

## SageMaker component summary

| SageMaker component | Main purpose | Important exam concept |
|---|---|---|
| **SageMaker Studio** | Integrated development environment for machine learning | Central workspace for data scientists and ML developers |
| **SageMaker Notebooks** | Develop and experiment using Jupyter notebooks | Can use managed notebook instances or Studio environments |
| **SageMaker Canvas** | No-code or low-code machine learning | Business analysts can build predictions without writing code |
| **SageMaker JumpStart** | Pre-trained models, foundation models, built-in solutions, and example notebooks | Accelerates model development and deployment |
| **SageMaker Data Wrangler** | Data preparation and feature engineering | Provides visual data import, transformation, and analysis |
| **SageMaker Ground Truth** | Data labeling and annotation | Supports human labeling workflows |
| **SageMaker Autopilot** | Automated machine learning | Automatically explores algorithms and creates candidate models |
| **SageMaker training jobs** | Train models using AWS-managed compute | Supports built-in algorithms, frameworks, and custom containers |
| **SageMaker Automatic Model Tuning** | Hyperparameter optimization | Searches for better hyperparameter combinations |
| **SageMaker Processing Jobs** | Run data preprocessing, postprocessing, and evaluation jobs | Useful for managed batch data processing |
| **SageMaker Model Registry** | Catalog and manage model versions | Supports model approval and deployment workflows |
| **SageMaker Pipelines** | Automate ML workflows | Supports repeatable MLOps processes |
| **SageMaker Feature Store** | Store, share, and retrieve ML features | Helps maintain consistent features for training and inference |
| **SageMaker endpoints** | Host models for inference | Supports real-time, serverless, asynchronous, and other inference options |
| **SageMaker Batch Transform** | Run predictions on a batch of data | No continuously running endpoint is required |
| **SageMaker Model Monitor** | Monitor deployed models and data | Detects data quality, model quality, bias, and drift issues |
| **SageMaker Clarify** | Detect bias and explain model predictions | Supports responsible AI and explainability |
| **SageMaker Debugger** | Monitor training jobs | Helps identify training problems and inefficiencies |
| **SageMaker Inference Recommender** | Help select suitable inference instance types and configurations | Supports deployment optimization |

---

## 1.1 SageMaker Studio

**SageMaker Studio** is an integrated web-based environment for machine learning development.

It can provide access to:

- Notebooks
- Data preparation tools
- Training jobs
- Model deployment
- Model monitoring
- Model registry
- ML pipelines
- Experiments and model evaluation

### Exam point

SageMaker Studio is primarily a **development and management environment**. It is not itself a foundation model or a data storage service.

---

## 1.2 SageMaker Canvas

**SageMaker Canvas** enables users to build machine learning models with little or no code.

Typical users include:

- Business analysts
- Operations teams
- Marketing teams
- Financial analysts

Example uses:

- Customer churn prediction
- Sales forecasting
- Fraud risk prediction
- Demand forecasting
- Classification and regression

### Canvas versus Autopilot

| Capability | SageMaker Canvas | SageMaker Autopilot |
|---|---|---|
| Primary interface | Visual, no-code or low-code interface | Automated ML workflow |
| Typical user | Business analyst or non-developer | Data scientist or ML engineer |
| Main purpose | Build and use predictions easily | Automatically select and train candidate models |
| Coding required | Usually none | Can be used through APIs, SDKs, or Studio |

### Exam trap

Canvas is not the same as Amazon QuickSight. QuickSight is primarily for business intelligence and visualization, while Canvas is for building machine learning models and predictions.

---

## 1.3 SageMaker JumpStart

**SageMaker JumpStart** provides:

- Pre-trained models
- Foundation models
- Open-source models
- Built-in algorithms
- Solution templates
- Example notebooks
- Model deployment options

JumpStart helps users quickly experiment with and deploy models without developing everything from scratch.

### Example

A developer can use a pre-trained image classification model from JumpStart, fine-tune it with the company’s data, and deploy it to a SageMaker endpoint.

### SageMaker JumpStart versus Amazon Bedrock

| Feature | SageMaker JumpStart | Amazon Bedrock |
|---|---|---|
| Main focus | ML development, model selection, customization, training, and deployment | Accessing foundation models through managed APIs |
| Typical use | Build, fine-tune, evaluate, and deploy models | Use generative AI foundation models in applications |
| Model customization | Can support fine-tuning and broader ML workflows | Supports selected model customization options |
| Infrastructure control | Generally offers more control over training and deployment | More abstracted and serverless from the application perspective |
| Common integration | SageMaker endpoints, training jobs, pipelines | Bedrock model invocation, Knowledge Bases, Agents, Guardrails |
| Best fit | Custom ML development and operationalization | Quickly adding generative AI capabilities to applications |

### Key distinction

- Choose **Amazon Bedrock** when you primarily want to consume foundation models through APIs without managing the underlying ML infrastructure.
- Choose **SageMaker** when you need an end-to-end ML development environment, custom training, extensive model control, or deployment and monitoring workflows.
- **JumpStart** is a SageMaker capability for discovering and using models; it is not a separate alternative to all SageMaker functionality.

> A business can use both services. For example, Bedrock could provide a generative AI application, while SageMaker could train a specialized predictive model.

---

## 1.4 SageMaker Data Wrangler

**Data Wrangler** helps users:

- Import data from sources such as Amazon S3
- Explore and visualize data
- Detect data quality issues
- Transform data
- Engineer features
- Create repeatable data preparation flows

Data preparation is often one of the largest parts of an ML project.

### Example transformations

- Handling missing values
- Encoding categorical variables
- Normalizing numerical values
- Removing duplicate records
- Splitting data into training and testing sets

### Exam distinction

Data Wrangler prepares data. It does not replace:

- Amazon S3 for durable object storage
- AWS Glue for general-purpose data cataloging and ETL
- SageMaker Ground Truth for human labeling

---

## 1.5 SageMaker Ground Truth

**SageMaker Ground Truth** helps create labeled datasets for supervised learning.

It can support labeling tasks such as:

- Image classification
- Object detection
- Text classification
- Sentiment analysis
- Semantic segmentation
- Named entity recognition

Ground Truth can use:

- Human workers
- Private workforces
- Third-party vendors
- Automated labeling assisted by machine learning

### Example

A company wants to identify defective products in factory images. Ground Truth can help workers label images as:

- Defective
- Non-defective
- Defective with a particular type of damage

### Exam trap

Ground Truth is associated with **data labeling**, not model training or model hosting.

---

## 1.6 SageMaker Autopilot

**SageMaker Autopilot** automates many steps of an ML workflow, including:

- Data analysis
- Algorithm selection
- Feature engineering
- Model training
- Model evaluation
- Candidate model generation

It is commonly associated with tabular data and supervised learning tasks such as:

- Classification
- Regression
- Forecasting

### Exam point

Autopilot is an **AutoML** capability. It does not mean that the business no longer needs to understand the data, define the problem, or evaluate the results.

---

## 1.7 SageMaker Training Jobs

A SageMaker training job runs model training on managed AWS infrastructure.

Training can use:

- SageMaker built-in algorithms
- Popular ML frameworks
- Custom Python code
- Custom Docker containers
- Distributed training configurations
- GPU or CPU instances

Training data is commonly stored in Amazon S3. The training job reads the data and writes model artifacts back to S3.

### Typical training flow

```text
Training data in Amazon S3
        ↓
SageMaker training job
        ↓
Trained model artifacts in Amazon S3
        ↓
Model deployment or registration
```

### Key exam concept

A SageMaker training job is different from an inference endpoint:

- **Training** creates or improves a model.
- **Inference** uses the trained model to generate predictions.

---

## 1.8 SageMaker Automatic Model Tuning

Automatic Model Tuning, also called hyperparameter tuning, searches for better hyperparameter values.

Examples of hyperparameters include:

- Learning rate
- Number of trees
- Batch size
- Number of hidden layers
- Regularization parameters

The service can launch multiple training jobs with different configurations and compare their results.

### Exam trap

Hyperparameters are set before or during training. They are not the same as model parameters learned from the training data.

---

## 1.9 SageMaker Processing Jobs

**SageMaker Processing Jobs** run data processing workloads using managed compute.

Common uses include:

- Data preprocessing
- Feature engineering
- Data validation
- Model evaluation
- Batch postprocessing

Processing jobs can use frameworks such as Python, Spark, or custom containers.

### Processing jobs versus training jobs

| Job type | Purpose |
|---|---|
| Processing job | Prepare, validate, or evaluate data |
| Training job | Learn model parameters from training data |
| Batch Transform job | Generate predictions for a batch of input data |

---

## 1.10 SageMaker Model Registry

The **SageMaker Model Registry** helps organizations manage model versions.

It can support:

- Versioning
- Model approval states
- Model metadata
- Model package management
- Deployment workflows
- Governance and auditability

A model can have statuses such as:

- Pending approval
- Approved
- Rejected

### Example workflow

1. A data scientist trains a model.
2. The model is evaluated.
3. The model is registered.
4. A reviewer approves the model.
5. An automated pipeline deploys the approved version.

---

## 1.11 SageMaker Pipelines

**SageMaker Pipelines** is an orchestration service for ML workflows.

A pipeline may include:

1. Data preprocessing
2. Model training
3. Model evaluation
4. Conditional approval checks
5. Model registration
6. Deployment
7. Monitoring

### Why pipelines are useful

They help make ML workflows:

- Repeatable
- Automated
- Auditable
- Consistent
- Easier to update

### Exam distinction

SageMaker Pipelines orchestrates ML steps. It is not the same as:

- AWS Step Functions, which is a general workflow orchestration service
- Amazon EventBridge, which routes events
- AWS CodePipeline, which primarily supports software delivery pipelines

These services can be used together.

---

## 1.12 SageMaker Feature Store

The **SageMaker Feature Store** stores and manages ML features.

A feature is an input variable used by a model, such as:

- Customer age
- Average transaction amount
- Number of logins during the last 30 days
- Product category
- Account risk score

Feature Store supports the sharing and reuse of features across models and teams.

### Important concept

Feature Store can help reduce **training-serving skew**, where the features used during model training differ from the features used during production inference.

It can provide:

- An online store for low-latency access
- An offline store for historical data and training

---

## 1.13 SageMaker Inference Options

After training, a model must be used to make predictions. SageMaker offers several inference patterns.

### Real-time inference

Use a persistent endpoint for predictions that require low latency.

Best for:

- Interactive applications
- Fraud detection during a transaction
- Real-time recommendations
- Customer-facing APIs

### Serverless inference

Use a serverless endpoint for intermittent or unpredictable traffic.

Best for:

- Infrequent requests
- Workloads where paying for continuously provisioned instances is undesirable
- Applications that can tolerate startup latency

### Asynchronous inference

Use asynchronous inference for large payloads or requests that do not need an immediate response.

Best for:

- Large documents
- Long-running inference
- Image or video processing
- Requests that can be queued

### Batch Transform

Use Batch Transform to generate predictions for a batch of data.

Best for:

- Nightly scoring
- Large offline datasets
- Periodic customer segmentation
- Batch risk scoring

### Inference comparison

| Requirement | Suitable option |
|---|---|
| Low-latency online prediction | Real-time endpoint |
| Infrequent requests and variable traffic | Serverless inference |
| Large or long-running requests | Asynchronous inference |
| Scheduled scoring of a large dataset | Batch Transform |

### Exam trap

Do not choose a real-time endpoint automatically. If predictions are periodic and do not require immediate responses, Batch Transform is usually more appropriate and can avoid keeping an endpoint continuously active.

---

## 1.14 SageMaker Model Monitor

**SageMaker Model Monitor** helps monitor deployed models and their inputs or outputs.

It can help detect:

- Data quality problems
- Data drift
- Model quality degradation
- Bias drift
- Feature distribution changes

### Example

A credit risk model was trained when most applicants were between 25 and 45 years old. Over time, the production population changes significantly. Model Monitor can help detect changes in the input feature distributions.

### Related terms

- **Data drift:** The distribution of input data changes.
- **Model drift:** Model performance changes over time.
- **Concept drift:** The relationship between input features and the target changes.
- **Data quality issue:** Input data violates expected constraints or schemas.

Monitoring may require baseline statistics, ground-truth labels, and appropriate metrics.

---

## 1.15 SageMaker Clarify

**SageMaker Clarify** supports responsible AI by helping with:

- Bias detection in datasets and models
- Explainability of model predictions
- Feature importance analysis
- Monitoring for bias drift

### Example

A bank can use Clarify to investigate whether a loan approval model produces significantly different outcomes for different demographic groups.

### Exam distinction

- **Clarify:** Bias detection and explainability
- **Model Monitor:** Monitoring deployed models and data over time
- **Ground Truth:** Creating labeled data

These capabilities are related but not interchangeable.

---

## 1.16 SageMaker Debugger

**SageMaker Debugger** helps inspect and debug model training.

It can help identify:

- Vanishing gradients
- Overfitting indicators
- Poor convergence
- Unused resources
- Training bottlenecks

### Exam scope

For AIF-C01, understand that Debugger helps with **training-job analysis and debugging**. Detailed implementation knowledge is generally unnecessary.

---

## 1.17 SageMaker Security and Governance

Important security concepts include:

- IAM controls access to SageMaker resources.
- Amazon S3 stores training data and model artifacts.
- AWS KMS can encrypt data and model artifacts.
- VPC configuration can help keep traffic within private network boundaries.
- CloudTrail records API activity.
- CloudWatch can collect logs and metrics.
- Resource-based and identity-based permissions can restrict access.

### Exam trap

SageMaker does not automatically make all data public or private in every scenario. Data access depends on the configured IAM roles, bucket policies, network configuration, and encryption settings.

---

# 2. Example Business Use Case and SageMaker Workflow

## Use case: Predicting customer churn

A telecommunications company wants to identify customers who are likely to cancel their subscriptions within the next 30 days.

### Business objective

The customer retention team wants to:

- Identify high-risk customers
- Contact them with relevant offers
- Reduce customer churn
- Measure the effectiveness of retention campaigns

---

## End-to-end architecture

```text
Customer and billing systems
            ↓
Amazon S3 data lake
            ↓
SageMaker Data Wrangler / Processing Job
            ↓
SageMaker Feature Store
            ↓
SageMaker training job or Autopilot
            ↓
Model evaluation and SageMaker Clarify
            ↓
SageMaker Model Registry
            ↓
SageMaker endpoint or Batch Transform
            ↓
CRM system / retention application
            ↓
SageMaker Model Monitor
```

---

## Step 1: Store historical data

Customer records, billing information, usage data, and support history are exported to **Amazon S3**.

Example data:

- Customer tenure
- Monthly bill
- Number of support calls
- Data usage
- Contract type
- Whether the customer churned

The historical churn field is the **target label**.

---

## Step 2: Prepare the data

Use **SageMaker Data Wrangler** or a **SageMaker Processing Job** to:

- Remove duplicate records
- Handle missing values
- Convert categorical values into numeric features
- Create a feature such as average monthly usage
- Split data into training, validation, and test datasets

The resulting datasets can be written back to Amazon S3.

---

## Step 3: Store reusable features

Frequently used features can be stored in **SageMaker Feature Store**.

For example:

- Average monthly spending
- Number of support tickets
- Recent usage trend
- Days since the last customer interaction

This allows multiple models and applications to reuse consistent features.

---

## Step 4: Train a model

The company can use:

- A SageMaker built-in algorithm
- A custom model using a supported ML framework
- SageMaker Autopilot for an automated ML approach

The training job reads the training data from Amazon S3 and writes the trained model artifacts back to S3.

---

## Step 5: Evaluate and explain the model

The company evaluates the model using appropriate metrics, such as:

- Precision
- Recall
- F1 score
- Area under the ROC curve
- Confusion matrix

The company can use **SageMaker Clarify** to:

- Examine feature importance
- Detect potential bias
- Explain why predictions are being made

For churn prediction, recall may be important because missing a customer who is likely to churn could be costly.

---

## Step 6: Register the model

The approved model is stored in the **SageMaker Model Registry**.

The registry can record:

- Model version
- Training data version
- Evaluation metrics
- Approval status
- Deployment metadata

Only approved model versions should be deployed to production.

---

## Step 7: Deploy the model

The deployment option depends on the business requirement.

### Option A: Real-time inference

A customer service application sends a customer ID or feature vector to a SageMaker real-time endpoint and receives a churn score immediately.

Use this if:

- A retention agent needs an immediate prediction
- The application requires low latency

### Option B: Batch Transform

Every night, the company sends a large list of customers to SageMaker Batch Transform.

The resulting churn predictions are stored in Amazon S3 and loaded into the CRM system.

Use this if:

- Predictions are generated once per day
- Immediate responses are unnecessary
- The company wants to avoid maintaining a continuously running endpoint

---

## Step 8: Monitor the model

After deployment, the company uses **SageMaker Model Monitor** to detect:

- Changes in customer behavior
- Missing or malformed features
- Changes in the distribution of input data
- Decreasing model quality after labels become available

If performance declines, a SageMaker Pipeline can trigger retraining.

---

# 3. SageMaker Compared with Other AWS Services

## SageMaker versus Amazon Bedrock

| Question | More likely service |
|---|---|
| Need a managed API to call foundation models for generative AI | Amazon Bedrock |
| Need to train a custom ML model | SageMaker |
| Need a full ML development and MLOps platform | SageMaker |
| Need to use a foundation model with minimal infrastructure management | Amazon Bedrock |
| Need extensive control over training jobs and inference infrastructure | SageMaker |
| Need model bias detection and ML model monitoring | SageMaker |
| Need managed generative AI agents or knowledge bases | Amazon Bedrock |
| Need to experiment with available models and deploy them through SageMaker | SageMaker JumpStart |

---

## SageMaker versus Amazon Comprehend

| Service | Main purpose |
|---|---|
| **Amazon Comprehend** | Pre-trained natural language processing, such as sentiment analysis and entity detection |
| **SageMaker** | Build, train, customize, deploy, and monitor ML models |

Choose Comprehend when a pre-built NLP API meets the requirement. Choose SageMaker when more customization or full ML lifecycle control is needed.

---

## SageMaker versus Amazon Rekognition

| Service | Main purpose |
|---|---|
| **Amazon Rekognition** | Pre-trained computer vision APIs |
| **SageMaker** | Custom model development and deployment |

Choose Rekognition for ready-to-use image and video analysis. Choose SageMaker when training or customizing a model is required.

---

## SageMaker versus Amazon Forecast

Amazon Forecast historically provided managed time-series forecasting capabilities. For exam questions involving an organization building and managing a broader custom ML workflow, SageMaker is generally the more comprehensive platform.

Always consider the exact business requirement and current AWS service availability.

---

## SageMaker versus AWS Glue

| Service | Main purpose |
|---|---|
| **AWS Glue** | Serverless data integration, ETL, and data cataloging |
| **SageMaker Data Wrangler or Processing Jobs** | ML-oriented data preparation and feature engineering |

These services can be used together. For example, AWS Glue can discover and catalog data, while SageMaker prepares features for model training.

---

## SageMaker versus Amazon QuickSight

| Service | Main purpose |
|---|---|
| **Amazon QuickSight** | Business intelligence, dashboards, and visualization |
| **SageMaker Canvas** | No-code machine learning and predictions |

A dashboard showing churn trends is a QuickSight use case. Building a churn prediction model is a SageMaker Canvas use case.

---

# 4. AIF-C01 Exam Tips and Traps

## High-value exam tips

1. **Identify the ML lifecycle stage.**  
   Is the question about data labeling, training, deployment, monitoring, or explainability?

2. **Match the inference type to the latency requirement.**
   - Immediate response: real-time inference
   - Periodic large-scale scoring: Batch Transform
   - Large or long-running requests: asynchronous inference
   - Irregular low-volume traffic: serverless inference

3. **Remember that Amazon S3 is commonly used for SageMaker data and artifacts.**  
   Training data and trained model artifacts are frequently stored in S3.

4. **Distinguish SageMaker from Bedrock.**
   - SageMaker: custom ML lifecycle and infrastructure control
   - Bedrock: managed access to foundation models through APIs

5. **Know the difference between JumpStart and Bedrock.**  
   JumpStart is a SageMaker model and solution hub. Bedrock is a managed foundation model service.

6. **Connect Ground Truth with labeling.**

7. **Connect Clarify with bias and explainability.**

8. **Connect Model Monitor with production monitoring and drift.**

9. **Connect Model Registry with model versions and approvals.**

10. **Connect Pipelines with repeatable ML workflows and MLOps.**

11. **Connect Feature Store with reusable features and training-serving consistency.**

12. **Do not assume every workload requires model training.**  
    If a pre-trained AI service meets the requirement, an AWS AI service such as Rekognition or Comprehend may be more appropriate.

---

## Common exam traps

### Trap 1: Choosing real-time inference for every prediction workload

A real-time endpoint may be unnecessary for a nightly batch of predictions.

- Nightly customer scoring: **Batch Transform**
- Immediate application response: **real-time endpoint**

---

### Trap 2: Confusing training data with model artifacts

- Training data: input used to learn the model
- Model artifact: output generated by the training job

Both are commonly stored in Amazon S3, but they have different purposes.

---

### Trap 3: Confusing SageMaker Clarify and Model Monitor

- Bias and explainability: **Clarify**
- Data drift and production monitoring: **Model Monitor**

---

### Trap 4: Confusing Ground Truth and Data Wrangler

- Label images or text: **Ground Truth**
- Clean and transform data: **Data Wrangler**

---

### Trap 5: Assuming Autopilot eliminates all human decisions

Autopilot automates model development steps, but the user still needs to:

- Define the target
- Provide suitable data
- Select meaningful evaluation metrics
- Validate the results
- Consider fairness, privacy, and business impact

---

### Trap 6: Choosing SageMaker when an AWS AI service is sufficient

If the requirement is simply to detect objects in images using a pre-trained API, **Amazon Rekognition** may be simpler than building a custom SageMaker model.

If the requirement is sentiment analysis using a managed NLP API, **Amazon Comprehend** may be more appropriate.

---

### Trap 7: Believing JumpStart is only for foundation models

JumpStart also provides:

- Traditional ML models
- Pre-trained models
- Solution templates
- Example notebooks
- Deployment options

---

### Trap 8: Confusing a model endpoint with a model registry

- Endpoint: serves predictions
- Model Registry: stores and manages model versions

---

### Trap 9: Ignoring data leakage

Data leakage occurs when training data contains information that would not be available at prediction time.

Example:

- Using a customer cancellation date to predict whether the customer will cancel.

SageMaker provides tools for ML workflows, but the user is still responsible for proper feature and target design.

---

### Trap 10: Ignoring IAM and encryption

SageMaker access is governed by AWS security controls. Exam questions may expect awareness of:

- IAM roles
- S3 bucket permissions
- KMS encryption
- VPC networking
- CloudTrail logging

---

# 5. Practice Multiple-Choice Questions

> These are original practice questions written in the style of foundational AWS certification questions. They are not reproduced official exam questions.

---

## Question 1: Selecting an inference option

A retail company trains a SageMaker model to predict demand for all products. The company needs to generate predictions once every night for millions of product records. The predictions do not need to be returned immediately to an application.

Which SageMaker option is most appropriate?

A. Real-time inference endpoint  
B. SageMaker Batch Transform  
C. SageMaker Serverless Inference  
D. SageMaker Ground Truth  

**Answer: B. SageMaker Batch Transform**

**Explanation:** Batch Transform is designed for generating predictions for large datasets without maintaining a continuously running endpoint.

---

## Question 2: Foundation model selection

A developer wants to add a generative AI chatbot to an application. The developer wants to call a foundation model through an API and does not want to manage model training infrastructure.

Which AWS service is generally the best choice?

A. Amazon Bedrock  
B. SageMaker Ground Truth  
C. SageMaker Model Monitor  
D. Amazon QuickSight  

**Answer: A. Amazon Bedrock**

**Explanation:** Amazon Bedrock provides managed access to foundation models through APIs and supports generative AI application development without requiring the customer to manage the underlying model infrastructure.

---

## Question 3: Data labeling

A company has thousands of unlabeled images of manufactured parts. The company needs workers to label each image as either defective or non-defective before training a computer vision model.

Which SageMaker capability should the company use?

A. SageMaker Ground Truth  
B. SageMaker Clarify  
C. SageMaker Feature Store  
D. SageMaker Model Registry  

**Answer: A. SageMaker Ground Truth**

**Explanation:** Ground Truth supports human-assisted data labeling and annotation.

---

## Question 4: Bias and explainability

A financial services company wants to determine whether its loan approval model produces biased outcomes and wants to understand which features influence individual predictions.

Which SageMaker capability should the company use?

A. SageMaker Clarify  
B. SageMaker Batch Transform  
C. SageMaker Autopilot  
D. SageMaker Processing Jobs only  

**Answer: A. SageMaker Clarify**

**Explanation:** SageMaker Clarify supports bias detection and model explainability.

---

## Question 5: No-code machine learning

A business analyst wants to create a customer churn prediction model but has limited programming experience.

Which SageMaker capability is most appropriate?

A. SageMaker Canvas  
B. SageMaker Debugger  
C. SageMaker Model Registry  
D. SageMaker Ground Truth only  

**Answer: A. SageMaker Canvas**

**Explanation:** Canvas provides a visual, no-code or low-code experience for building and using machine learning models.

---

## Question 6: Model version management

A machine learning team wants to maintain multiple versions of a model, record evaluation metrics, and require approval before production deployment.

Which SageMaker capability should the team use?

A. SageMaker Model Registry  
B. SageMaker Data Wrangler  
C. SageMaker Serverless Inference  
D. SageMaker Feature Store  

**Answer: A. SageMaker Model Registry**

**Explanation:** Model Registry supports model versioning, metadata, approval states, and controlled deployment workflows.

---

## Question 7: Production drift

A model is deployed to a SageMaker endpoint. Over time, the distribution of the model’s input data changes significantly compared with the training data.

Which capability can help detect this issue?

A. SageMaker Model Monitor  
B. SageMaker Ground Truth  
C. SageMaker JumpStart  
D. SageMaker Canvas  

**Answer: A. SageMaker Model Monitor**

**Explanation:** Model Monitor can detect data quality issues and changes in production data distributions, including data drift.

---

## Question 8: Automated model development

A data scientist wants SageMaker to automatically try multiple algorithms and configurations for a tabular classification problem and produce candidate models.

Which capability should be used?

A. SageMaker Autopilot  
B. SageMaker Clarify  
C. SageMaker Feature Store  
D. SageMaker Model Monitor  

**Answer: A. SageMaker Autopilot**

**Explanation:** Autopilot automates many steps of the machine learning model development process, including algorithm and configuration exploration.

---

## Question 9: Reusable features

Several teams need to use the same customer risk features for both model training and low-latency production predictions.

Which SageMaker capability is most appropriate?

A. SageMaker Feature Store  
B. SageMaker Ground Truth  
C. SageMaker JumpStart  
D. SageMaker Debugger  

**Answer: A. SageMaker Feature Store**

**Explanation:** Feature Store helps teams store, manage, reuse, and retrieve ML features consistently for training and inference.

---

## Question 10: ML workflow automation

A company wants to automate a workflow that preprocesses data, trains a model, evaluates it, registers the model if it meets a quality threshold, and deploys the approved model.

Which SageMaker capability is most appropriate?

A. SageMaker Pipelines  
B. SageMaker Canvas  
C. SageMaker Batch Transform only  
D. Amazon Rekognition  

**Answer: A. SageMaker Pipelines**

**Explanation:** SageMaker Pipelines supports automated, repeatable ML workflows, including processing, training, evaluation, registration, and deployment.

---

# 6. Final AIF-C01 SageMaker Memory Guide

| If the question says… | Think of… |
|---|---|
| No-code ML | SageMaker Canvas |
| Automated machine learning | SageMaker Autopilot |
| Pre-trained and foundation models in SageMaker | SageMaker JumpStart |
| Label images or text | SageMaker Ground Truth |
| Prepare and transform ML data | SageMaker Data Wrangler |
| Train a custom model | SageMaker training job |
| Optimize hyperparameters | Automatic Model Tuning |
| Store reusable ML features | Feature Store |
| Manage model versions and approvals | Model Registry |
| Automate ML steps | SageMaker Pipelines |
| Low-latency prediction | Real-time endpoint |
| Infrequent, variable traffic | Serverless inference |
| Large or long-running inference request | Asynchronous inference |
| Periodic bulk predictions | Batch Transform |
| Detect bias or explain predictions | SageMaker Clarify |
| Detect drift in production | SageMaker Model Monitor |
| Debug training behavior | SageMaker Debugger |
| Use foundation models through managed APIs | Amazon Bedrock |
| Pre-built image analysis | Amazon Rekognition |
| Pre-built NLP analysis | Amazon Comprehend |
| BI dashboards | Amazon QuickSight |

