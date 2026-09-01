

# Content Domain 1: Data Preparation for Machine Learning (ML)
<a name="machine-learning-engineer-associate-01-domain1"></a>

**Topics**

- [Content Domain 1: Data Preparation for Machine Learning (ML)](#content-domain-1-data-preparation-for-machine-learning-ml)
  - [Task 1.1: Ingest and store data](#task-11-ingest-and-store-data)
  - [Task 1.2: Transform data and perform feature engineering](#task-12-transform-data-and-perform-feature-engineering)
  - [Task 1.3: Ensure data integrity and prepare data for modeling](#task-13-ensure-data-integrity-and-prepare-data-for-modeling)
  - [See also](#see-also)

## Task 1.1: Ingest and store data
<a name="machine-learning-engineer-associate-01-domain1-task1"></a>

Knowledge of:

+ Data formats and ingestion mechanisms (for example, validated and non-validated formats, Apache Parquet, JSON, CSV, Apache ORC, Apache Avro, RecordIO)
+ How to use the core AWS data sources (for example, Amazon S3, Amazon EFS, Amazon FSx for NetApp ONTAP)
+ How to use AWS streaming data sources to ingest data (for example, Amazon Kinesis, Apache Flink, Apache Kafka)
+ AWS storage options, including use cases and tradeoffs

Skills in:

+ Extracting data from storage (for example, Amazon S3, Amazon EBS, Amazon EFS, Amazon RDS, Amazon DynamoDB) by using relevant AWS service options (for example, Amazon S3 Transfer Acceleration, Amazon EBS Provisioned IOPS)
+ Choosing appropriate data formats (for example, Parquet, JSON, CSV, ORC) based on data access patterns
+ Ingesting data into Amazon SageMaker Data Wrangler and SageMaker Feature Store
+ Merging data from multiple sources (for example, by using programming techniques, AWS Glue, Apache Spark)
+ Troubleshooting and debugging data ingestion and storage issues that involve capacity and scalability
+ Making initial storage decisions based on cost, performance, and data structure

## Task 1.2: Transform data and perform feature engineering
<a name="machine-learning-engineer-associate-01-domain1-task2"></a>

Knowledge of:

+ Data cleaning and transformation techniques (for example, detecting and treating outliers, imputing missing data, combining, deduplication)
+ Feature engineering techniques (for example, data scaling and standardization, feature splitting, binning, log transformation, normalization)
+ Encoding techniques (for example, one-hot encoding, binary encoding, label encoding, tokenization)
+ Tools to explore, visualize, or transform data and features (for example, SageMaker Data Wrangler, AWS Glue, AWS Glue DataBrew)
+ Services that transform streaming data (for example, AWS Lambda, Spark)
+ Data annotation and labeling services that create high-quality labeled datasets

Skills in:

+ Transforming data by using AWS tools (for example, AWS Glue, DataBrew, Spark running on Amazon EMR, SageMaker Data Wrangler)
+ Creating and managing features by using AWS tools (for example, SageMaker Feature Store)
+ Validating and labeling data by using AWS services (for example, SageMaker Ground Truth, Amazon Mechanical Turk)

## Task 1.3: Ensure data integrity and prepare data for modeling
<a name="machine-learning-engineer-associate-01-domain1-task3"></a>

Knowledge of:

+ Pre-training bias metrics for numeric, text, and image data (for example, class imbalance [CI], difference in proportions of labels [DPL])
+ Strategies to address CI in numeric, text, and image datasets (for example, synthetic data generation, resampling)
+ Techniques to encrypt data
+ Data classification, anonymization, and masking
+ Implications of compliance requirements (for example, personally identifiable information [PII], protected health information [PHI], data residency)

Skills in:

+ Validating data quality (for example, by using DataBrew and AWS Glue Data Quality)
+ Identifying and mitigating sources of bias in data (for example, selection bias, measurement bias) by using AWS tools (for example, SageMaker Clarify)
+ Preparing data to reduce prediction bias (for example, by using dataset splitting, shuffling, and augmentation)
+ Configuring data to load into the model training resource (for example, Amazon EFS, Amazon FSx)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Certification. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query aws-certification` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).