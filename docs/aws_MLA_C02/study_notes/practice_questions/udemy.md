# Udemy Full-Length Practice Exam (65 Questions)

**Overall Exam Score:** **59 / 65 (90.8%)** | **Status:** :white_check_mark: **PASS**

---

### Question 1

**Category:** Content Domain 1: Data Preparation for ML and AI  
**Status:** ✅ **Correct**

A university astronomy observatory's ML team receives nightly telescope observation metadata as nested JSON files in Amazon S3. A downstream training system expects flat CSV files in Amazon S3 and cannot read nested JSON, Parquet, or ORC. The team wants a managed batch process that can run on a schedule and avoid managing cluster infrastructure.

Which solution will meet these requirements with the LEAST operational overhead?

* **A)** Run a scheduled AWS Glue ETL job that reads the JSON files from Amazon S3, flattens the records, and writes CSV files to Amazon S3.
* **B)** Store the JSON files in Amazon EMR HDFS, run Spark SQL over the nested fields, and keep the transformed data on the cluster.
* **C)** Configure Amazon Data Firehose to buffer the JSON records, convert the delivery output to Parquet, and write the files to Amazon S3.
* **D)** Run an AWS Glue crawler that catalogs the JSON files in Amazon S3, creates table definitions, and exposes the data for Amazon Athena queries.

??? note "Click to reveal Answer & Explanation"
    **Correct Answer:** **A**

    #### Correct Option Analysis
    * **A is Correct:** This option uses AWS Glue for a managed batch ETL workflow that can read JSON from Amazon S3 and write transformed output back to Amazon S3. Writing CSV matches the downstream training system's stated access pattern and format requirement.

    #### Distractor Analysis
    * **B is Incorrect:** Amazon EMR can run Spark workloads that transform nested data. However, storing the result in HDFS ties the output to the cluster lifecycle and does not satisfy the requirement to write flat CSV files to Amazon S3 with minimal operations.
    * **C is Incorrect:** Amazon Data Firehose is useful for managed streaming delivery and can convert JSON to columnar formats for Amazon S3 delivery. However, this workload is a scheduled batch transformation, and Parquet is explicitly not accepted by the downstream system.
    * **D is Incorrect:** An AWS Glue crawler can discover schema information and populate the AWS Glue Data Catalog. However, a crawler does not flatten the records or write the required CSV files for the downstream training system.

    #### Overall Explanation
    AWS Glue ETL is a good fit when source data in Amazon S3 must be transformed into a different file format for a batch ML preparation workflow. In this scenario, the important access pattern is not analytical column pruning or long-term query optimization. The downstream training system can consume only flat CSV files, so the preparation job should flatten the nested JSON and write CSV output.
    
    Columnar formats such as Parquet and ORC are often better for Athena-style analytics because queries can scan fewer bytes when only a subset of columns is needed. That benefit does not help when the consuming system cannot read those formats. Choosing a format should follow the consumer's read pattern and compatibility requirements, not a general rule that columnar formats are always best.
    
    An AWS Glue crawler is useful for schema discovery and populating the Glue Data Catalog, but cataloging is not the same as writing a transformed dataset. Amazon Data Firehose is better aligned to continuous delivery of streaming records, while Amazon EMR can perform the transformation but introduces cluster management and HDFS lifecycle concerns. For AWS Glue format capabilities, see AWS Glue for Spark data format support [https://docs.aws.amazon.com/glue/latest/dg/aws-glue-programming-etl-format.html]. For the columnar analytics tradeoff, see Use columnar storage formats in Athena [https://docs.aws.amazon.com/athena/latest/ug/columnar-storage.html].

---

### Question 2

**Category:** Content Domain 3: Deployment and Orchestration of ML and AI  
**Status:** ✅ **Correct**

A wildlife conservation nonprofit's computer vision team trained a PyTorch image segmentation model in an on-premises GPU environment. The team wants to host the model in AWS without retraining it. Field biologists upload large drone images in bursts after surveys. Each inference request can take minutes, and the application can store completed predictions for later review rather than returning an immediate response.

Which deployment approach will meet these requirements with the LEAST client-side orchestration?

* **A)** Package the model artifacts with a compatible inference image and deploy a SageMaker AI asynchronous inference endpoint.
* **B)** Package the model artifacts with a compatible inference image and deploy a SageMaker AI real-time endpoint with autoscaling.
* **C)** Run scheduled SageMaker AI batch transform jobs that scan the upload bucket and write prediction files to Amazon S3.
* **D)** Import the model artifacts by using Amazon Bedrock Custom Model Import and invoke the model through the Bedrock API.

??? note "Click to reveal Answer & Explanation"
    **Correct Answer:** **A**

    #### Correct Option Analysis
    * **A is Correct:** SageMaker AI asynchronous inference is designed for requests that can be queued and processed without a live client connection. This approach lets the team bring an externally trained model by packaging artifacts with suitable inference code and returning results later, which matches bursty large image requests.

    #### Distractor Analysis
    * **B is Incorrect:** SageMaker AI real-time endpoints are appropriate for interactive workloads where clients wait for low-latency HTTPS responses. Autoscaling can adjust endpoint capacity, but it does not change the synchronous request pattern that the application is trying to avoid.
    * **C is Incorrect:** Batch transform is useful for offline scoring of datasets, but it is job oriented rather than an always-available inference endpoint. Scheduling scans of a bucket adds orchestration delay and operational work for per-upload predictions.
    * **D is Incorrect:** Amazon Bedrock Custom Model Import is intended for supported customized foundation models that are invoked through Amazon Bedrock. A PyTorch image segmentation model for drone imagery is better hosted through SageMaker AI with a compatible inference image.

    #### Overall Explanation
    SageMaker AI can host models that were not trained in SageMaker AI when the model artifacts and inference code are packaged for hosting. The SageMaker AI deployment overview [https://docs.aws.amazon.com/sagemaker/latest/dg/deploy-model-get-started.html] describes the model artifact and container image flow for creating hosted inference endpoints, and Use your own inference code [https://docs.aws.amazon.com/sagemaker/latest/dg/your-algorithms-inference-code.html] explains how custom inference code and containers support outside-trained models.
    
    For a workload that can wait for results, asynchronous inference trades immediate responses for managed queuing and later output handling. That design reduces client-side connection management while still letting the team use its externally trained PyTorch model.
    
    A real-time endpoint optimizes for low-latency HTTPS calls, so autoscaling does not change the synchronous invocation contract. Scheduled batch transform can score files, but it is an offline job pattern rather than an endpoint-style request interface. Amazon Bedrock Custom Model Import [https://docs.aws.amazon.com/bedrock/latest/userguide/model-customization-import-model.html] is valuable for supported customized foundation models, but the scenario describes a conventional computer vision model that fits SageMaker hosting.

---

### Question 3

**Category:** Content Domain 2: ML Model and Foundation Model (FM) Develop  
**Status:** ✅ **Correct**

A boutique language-learning platform's AI engineering team is selecting one of several Amazon Bedrock foundation models for an application that gives written feedback on student essays. The team has an evaluation dataset of prompts and SME-written ideal responses. Early trials show that the largest model gives the strongest feedback but has higher latency and token cost, while smaller models are faster and cheaper but may miss some feedback criteria. The team must make a release decision that balances quality, latency, and cost before production deployment.

Which solution will best meet these requirements?

* **A)** Choose the smallest candidate model from pricing data, increase retrieved context for answer quality, and measure failures after production release.
* **B)** Run Amazon Bedrock Model Evaluations for each candidate, combine scores with token-cost and latency data, and select a model that meets thresholds.
* **C)** Compare candidates by ROUGE-1 unigram overlap only, choose the highest-scoring model, and estimate token cost after the model is deployed.
* **D)** Deploy the largest candidate model first, cap generated output tokens, and use production feedback to decide whether latency and cost are acceptable.

??? note "Click to reveal Answer & Explanation"
    **Correct Answer:** **B**

    #### Correct Option Analysis
    * **B is Correct:** This approach measures model behavior against the team's own evaluation dataset before deployment. Combining quality scores with token-cost and latency measurements supports a defensible price-performance decision instead of choosing the largest or cheapest model by assumption.

    #### Distractor Analysis
    * **A is Incorrect:** Selecting only from pricing data prioritizes cost without confirming that the model meets the quality threshold. Increasing context can also raise input token cost and latency, and waiting until after release does not satisfy the need for a pre-production decision.
    * **C is Incorrect:** ROUGE-1 measures unigram overlap, which can be useful for some text-generation tasks but is limited for evaluating semantic feedback quality. This approach also delays cost estimation and latency assessment until after deployment, which does not support a balanced release decision.
    * **D is Incorrect:** The largest model might satisfy quality goals, but this approach assumes that the extra cost and latency are justified. Capping output length can reduce token usage, but it can also reduce completeness and does not provide a pre-release comparison across candidate models.

    #### Overall Explanation
    For generative AI model selection, the practical engineering question is not simply which model is best or cheapest. The better approach is to define quality thresholds with an evaluation dataset, measure candidate models against those thresholds, and then compare the models by latency and token-driven cost.
    
    Amazon Bedrock Model Evaluations can use automated metrics, human evaluation, or an LLM-as-a-judge approach to assess dimensions such as correctness, relevance, safety, and task-specific criteria. That quality signal should be paired with token counts or actual cost data, because prompts, retrieved context, and generated responses all contribute to inference cost.
    
    Latency should also be measured directly because smaller models are often faster, but a smaller model is not useful if it fails the workload's quality bar. AWS describes the same measurement-oriented mindset for generative inference tradeoffs in SageMaker AI generative inference recommendations [https://docs.aws.amazon.com/sagemaker/latest/dg/generative-ai-inference-recommendations.html]. If production requests later vary widely in complexity, Amazon Bedrock intelligent prompt routing [https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-routing.html] can be considered, but this scenario first requires a controlled comparison of candidate models before release.

---

### Question 4

**Category:** Content Domain 2: ML Model and Foundation Model (FM) Develop  
**Status:** ✅ **Correct**

An online grocery marketplace's ML platform team is validating a new product-ranking model on an Amazon SageMaker AI real-time endpoint. A shadow test sends a sample of live requests to the candidate model while shopper-facing results still come from the current model. The release criteria require the candidate to stay within the team's latency and error-rate bounds. After the test starts, production variant metrics remain healthy, but the shadow variant shows higher latency and more model errors than the production variant.

What should the ML engineer do next?

* **A)** Move both models to a multi-model endpoint and rerun the same production traffic.
* **B)** Promote the shadow variant because shopper-facing responses remained unchanged during the test.
* **C)** Increase the shadow traffic sample to 100% and continue returning production responses.
* **D)** Keep the current production variant and investigate the shadow variant before promotion.

??? note "Click to reveal Answer & Explanation"
    **Correct Answer:** **D**

    #### Correct Option Analysis
    * **D is Correct:** A shadow test is designed to reveal candidate model issues without returning candidate responses to users. Higher latency and more model errors on the shadow variant mean the candidate has not met the release criteria, so the current production variant should remain active while the candidate is investigated.

    #### Distractor Analysis
    * **A is Incorrect:** A multi-model endpoint can improve hosting efficiency for multiple models, but it is not the mechanism for deciding that a failing candidate is ready for promotion. Changing the hosting pattern does not resolve the observed latency and model errors from the shadow validation.
    * **B is Incorrect:** Stable shopper-facing responses are expected because the production variant still returns the response during a shadow test. That observation does not prove that the candidate model is ready, because the shadow metrics show latency and error problems.
    * **C is Incorrect:** Increasing the copied traffic can provide more observations, but it does not address the candidate's existing latency and error-rate issues. If the candidate already violates the release criteria, sending more replicated requests can add cost and load without making the model safer to promote.

    #### Overall Explanation
    In a SageMaker AI shadow test, production traffic is copied to a shadow variant so the team can observe how a candidate model behaves on real requests. The important design point is that only the production variant response is returned to the caller, so a clean user experience during the test does not mean the candidate is healthy.
    
    The engineer should compare operational signals such as invocations, latency, model errors, infrastructure utilization, and any captured input or output records against the acceptance criteria for the workload. If the shadow variant has worse latency or error behavior than the production variant, the safe decision is to keep the production variant in service and investigate before promotion. Shadow testing trades off extra inference cost for lower release risk, because it exposes the candidate to realistic traffic without letting candidate responses affect users. For more detail, see the SageMaker AI documentation on model validation with production and shadow variants [https://docs.aws.amazon.com/sagemaker/latest/dg/model-validation.html] and monitoring shadow test dashboards [https://docs.aws.amazon.com/sagemaker/latest/dg/shadow-tests-view-monitor-edit-dashboard.html].

---

### Question 5

**Category:** Content Domain 4: Operating, Monitoring, and Securing ML and  
**Status:** ✅ **Correct**

A pharmaceutical research lab's AI platform team runs a production summarization service as Amazon ECS tasks on EC2 instances. The service calls Amazon Bedrock by using a long-term Bedrock API key that is embedded in the task definition environment variables. The same ECS cluster hosts several unrelated backend services. A security scan reports the exposed bearer token, and the service starts receiving access denied errors after the IAM permissions of the IAM user associated with the long-term Bedrock API key are reduced.

Which TWO actions should the team take to remediate the issue while maintaining least privilege?

* **A)** Generate a long-term Amazon Bedrock API key from an administrator IAM user and redeploy the task.
* **B)** Remove the embedded API key and protect any remaining application secrets with AWS Secrets Manager.
* **C)** Enable CloudTrail Insights for Amazon Bedrock management events and continue using the existing key.
* **D)** Replace the Amazon Bedrock API key with an ECS task role that grants only required Bedrock actions.
* **E)** Attach Amazon Bedrock invoke permissions to the ECS container instance profile for the shared cluster.

??? note "Click to reveal Answer & Explanation"
    **Correct Answer:** **B, D**

    #### Correct Option Analysis
    * **B is Correct:** This option is correct because bearer tokens and other credentials should not be hard-coded in source code, container images, or task definitions. AWS Secrets Manager is appropriate for protecting application secrets that still need to be retrieved at runtime.
    * **D is Correct:** This option is correct because production AWS workloads should use IAM roles and temporary credentials instead of Bedrock API keys. An ECS task role scopes permissions to the specific task, which better supports least privilege than credentials shared across the cluster.

    #### Distractor Analysis
    * **A is Incorrect:** This option is incorrect because a long-term API key is intended for exploration or development rather than production workloads. Creating the key from an administrator IAM user also broadens the blast radius if the bearer token is exposed again.
    * **C is Incorrect:** This option is incorrect because CloudTrail and CloudTrail Insights help with auditing and anomaly detection, not with replacing unsafe credentials. Continuing to use the exposed key leaves the production service dependent on a bearer token and does not address least privilege.
    * **E is Incorrect:** This option is incorrect because the EC2 instance profile is used by the ECS agent and applies at the container instance level. Granting application permissions there can expose permissions to multiple services on the shared cluster and does not provide per-task least privilege.

    #### Overall Explanation
    For a production application running on AWS, the safer pattern is to rely on IAM roles with temporary credentials rather than embedding an Amazon Bedrock API key. Bedrock API keys are bearer-token-style credentials, so anyone who obtains the key can use it within the permissions associated with that key. Replacing the key with an ECS task role gives the application only the Bedrock permissions it needs, and removing the embedded key addresses the immediate secret exposure.
    
    The distinction between an ECS task role and an EC2 instance profile matters in shared clusters. The instance profile supports the ECS agent and host-level interactions, while the task role is the application identity for a specific task. Putting Bedrock permissions on the instance profile would make the permission boundary coarser and could grant access to unrelated workloads on the same cluster.
    
    CloudTrail remains useful during the investigation because it can show Bedrock API activity and the identities making requests, but auditing does not substitute for credential remediation. The team should use CloudTrail to verify what happened and to monitor future use, while changing the application to use a least-privilege runtime identity. For related AWS guidance, see Amazon Bedrock IAM troubleshooting [https://docs.aws.amazon.com/bedrock/latest/userguide/security_iam_troubleshoot.html] and Logging Amazon Bedrock API calls with AWS CloudTrail [https://docs.aws.amazon.com/bedrock/latest/userguide/logging-using-cloudtrail.html].

---

### Question 6

**Category:** Content Domain 3: Deployment and Orchestration of ML and AI  
**Status:** ✅ **Correct**

A precision agriculture startup's ML team trains crop disease classifiers in Amazon SageMaker AI. Each training run logs parameters, loss metrics, and model artifacts in MLflow. A recent audit found that the team could not consistently prove which artifact and evaluation metrics were approved before each production deployment. The team wants to keep experiment tracking and add a repeatable approval gate for future releases.

Which solution will meet these requirements?

* **A)** Register the selected MLflow model in SageMaker Model Registry, attach evaluation metadata, and let CI/CD deploy only approved versions.
* **B)** Copy the selected MLflow artifact to a timestamped Amazon S3 prefix, record metrics in a spreadsheet, and deploy the newest S3 object.
* **C)** Create a new SageMaker endpoint for each MLflow run, compare runtime metrics in CloudWatch, and route all traffic to the best endpoint.
* **D)** Package the selected MLflow artifact with the endpoint container image, tag the image with the run ID, and deploy the newest image tag.

??? note "Click to reveal Answer & Explanation"
    **Correct Answer:** **A**

    #### Correct Option Analysis
    * **A is Correct:** This solution keeps MLflow for experiment tracking while using SageMaker Model Registry to manage deployable model versions. Model Registry supports model metadata, approval status, and CI/CD promotion patterns that help establish an auditable release process.

    #### Distractor Analysis
    * **B is Incorrect:** Amazon S3 can store model artifacts, but timestamped prefixes and spreadsheets do not provide a managed approval workflow or reliable model release history. This is a manual tracking pattern that is prone to drift between the artifact, metrics, and deployed endpoint.
    * **C is Incorrect:** Separate endpoints can help test deployed candidates, but endpoints are not the right system of record for model lineage or release approval. Runtime metrics in CloudWatch do not prove which predeployment evaluation results were reviewed and approved.
    * **D is Incorrect:** Container image tags can help identify serving code, but they are not a governed model-version catalog with approval status. This approach also mixes model artifact versioning with image release management, which makes audits harder when models and containers change independently.

    #### Overall Explanation
    SageMaker Model Registry provides a managed place to catalog model versions, associate metadata such as evaluation results, track approval status, and connect approved versions to deployment automation. MLflow on SageMaker AI is useful for tracking experiments, parameters, metrics, and artifacts, but the release process still needs a governed registry when the question asks for repeatable production promotion and audits.
    
    The practical pattern is to keep MLflow as the experiment-tracking system, then register the selected model version in Model Registry with the relevant metrics and metadata. A CI/CD workflow can then use the model version's approval status as a promotion gate, so deployment depends on an explicit release decision rather than on whichever file, endpoint, or image tag appears newest. For more information, see Overview of SageMaker Model Registry capabilities [https://docs.aws.amazon.com/sagemaker/latest/dg/model-registry.html] and Register MLflow models with SageMaker Model Registry [https://docs.aws.amazon.com/sagemaker/latest/dg/mlflow-track-experiments-model-registration.html].

---

### Question 7

**Category:** Content Domain 4: Operating, Monitoring, and Securing ML and  
**Status:** ✅ **Correct**

An industrial robotics manufacturer's ML operations team runs a failure-prediction model on an Amazon SageMaker AI real-time endpoint. The application team already calculates nightly model-quality scores, such as recall and false-positive rate, after repair outcomes are available. The operations team wants a single dashboard that shows these delayed quality trends together with endpoint health indicators so engineers can investigate regressions after deployments.

Which solution will meet these requirements?

* **A)** Graph only SageMaker endpoint invocations, latency, errors, and utilization on a CloudWatch dashboard.
* **B)** Create a CloudTrail trail for SageMaker API calls and add management-event counts to an operations dashboard.
* **C)** Publish delayed quality scores as CloudWatch custom metrics and graph them with SageMaker endpoint metrics.
* **D)** Create AWS Config rules for SageMaker endpoint settings and use compliance status as the quality dashboard.

??? note "Click to reveal Answer & Explanation"
    **Correct Answer:** **C**

    #### Correct Option Analysis
    * **C is Correct:** This option combines application-specific model-quality measurements with SageMaker endpoint telemetry in the same monitoring view. CloudWatch supports dashboards for AWS service metrics and custom metrics, so the team can monitor both operational health and delayed quality signals.

    #### Distractor Analysis
    * **A is Incorrect:** Built-in endpoint metrics are important for infrastructure and serving health. This option omits the delayed label-based quality scores, so it does not meet the requirement to monitor model-quality trends with endpoint health.
    * **B is Incorrect:** CloudTrail records API activity, such as who changed a resource and when the change occurred. Management-event counts do not represent model recall, false-positive rate, endpoint latency, or other runtime performance signals.
    * **D is Incorrect:** AWS Config is useful for recording configuration changes and evaluating resources against compliance rules. Compliance status does not show model-quality trends or endpoint performance metrics that engineers need for regression investigation.

    #### Overall Explanation
    Production ML monitoring usually needs more than infrastructure telemetry. CloudWatch dashboards can show SageMaker AI endpoint metrics such as traffic, latency, errors, and resource health, and they can also include custom metrics that an application publishes for workload-specific signals. In this scenario, the delayed repair outcomes are the source of model-quality measurements, so publishing those scores as custom metrics lets the team trend quality beside serving health in one operational view.
    
    CloudTrail and AWS Config answer different operational questions. CloudTrail helps audit API calls and account activity, while AWS Config tracks resource configuration and compliance over time. Those services can help during an investigation, but they are not the primary mechanism for graphing model recall or false-positive-rate trends. For more information, see CloudWatch dashboards overview [https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.html] and SageMaker AI metrics in CloudWatch [https://docs.aws.amazon.com/sagemaker/latest/dg/monitoring-cloudwatch.html].

---

### Question 8

**Category:** Content Domain 4: Operating, Monitoring, and Securing ML and  
**Status:** ✅ **Correct**

A regional grocery delivery platform's ML operations team uses AWS CodePipeline to build a Python inference service, create a Docker image, and run Amazon Inspector vulnerability checks before deployment. A proposed implementation stores an IAM user's access key in repository secrets so the scan step can call AWS APIs. The security team requires the automated scans to continue, but the pipeline must not use long-lived AWS credentials and must follow least privilege.

How should the ML engineer provide AWS access to the vulnerability scanning step?

* **A)** Run the scan from a developer workstation that uses an IAM user's access keys outside the pipeline.
* **B)** Store an IAM user's access key in AWS Secrets Manager and inject the secret into the scan command.
* **C)** Attach AdministratorAccess to the pipeline role and rely on pipeline logs to audit the scan calls.
* **D)** Use a least-privilege pipeline or build service role for the Amazon Inspector scan step.

??? note "Click to reveal Answer & Explanation"
    **Correct Answer:** **D**

    #### Correct Option Analysis
    * **D is Correct:** This approach uses AWS service roles instead of long-lived access keys. The role can be scoped to the permissions needed for the scan step and related artifacts, which supports least privilege while keeping the scan automated.

    #### Distractor Analysis
    * **A is Incorrect:** This approach moves the vulnerability check out of the automated release workflow. It also continues to depend on IAM user access keys, which does not meet the requirement to avoid long-lived credentials.
    * **B is Incorrect:** This approach protects the secret better than storing it in source control, but it still relies on long-lived IAM user credentials. The requirement is to avoid long-lived AWS credentials in the pipeline, so an assumed service role is the better pattern.
    * **C is Incorrect:** This approach removes repository-stored credentials, but it grants far more access than the scan step needs. Auditing with logs does not compensate for violating least privilege in a CI/CD pipeline.

    #### Overall Explanation
    For AWS CI/CD workloads, the preferred security model is to let the pipeline or build service assume an IAM role that grants only the permissions required for the task. In this scenario, the vulnerability scan needs controlled access to Amazon Inspector and the relevant pipeline or image artifacts, not broad account access and not a static IAM user's access key.
    
    Amazon Inspector can be integrated into CI/CD workflows to scan artifacts and container images, and AWS CodePipeline also provides an Amazon Inspector scan action for managed pipeline-based scanning. The important security judgment is that the scanner should receive credentials through the AWS execution environment, such as a service role, rather than through repository secrets, build scripts, or developer workstations.
    
    Storing an access key in a secret store is better than hard-coding it, but it is still a long-lived credential that must be rotated and protected. Granting administrator access is an anti-pattern because it increases blast radius, and manual workstation scanning weakens the release gate. Use least privilege permissions and automated scanning so the release process remains both secure and repeatable. See Integrating Amazon Inspector scans into CI/CD pipelines [https://docs.aws.amazon.com/inspector/latest/user/scanning-cicd.html] and the CodePipeline Amazon Inspector scan action reference [https://docs.aws.amazon.com/codepipeline/latest/userguide/action-reference-InspectorScan.html].

---

### Question 9

**Category:** Content Domain 1: Data Preparation for ML and AI  
**Status:** ✅ **Correct**

An online gaming studio's telemetry team runs a self-managed Apache Kafka cluster on Amazon EC2 to collect player action events for ML pipelines. Existing producers and consumers use Kafka-compatible topic-based broker client libraries. The team wants to reduce cluster administration, keep the client applications largely unchanged, and run the ingestion layer inside the team's VPC across multiple Availability Zones.

Which solution will meet these requirements?

* **A)** Create an Amazon Kinesis Data Streams stream, and rewrite the applications to use Kinesis producer and consumer APIs.
* **B)** Migrate the broker cluster to Amazon MSK, and connect the existing producers and consumers to the managed cluster.
* **C)** Deploy an Amazon Managed Service for Apache Flink application, and connect the applications to the Flink job.
* **D)** Create an Amazon Data Firehose stream, and deliver the events directly to Amazon S3 or Amazon OpenSearch Service.

??? note "Click to reveal Answer & Explanation"
    **Correct Answer:** **B**

    #### Correct Option Analysis
    * **B is Correct:** Amazon MSK provides a managed Apache Kafka environment, so applications that already use Kafka-compatible producer and consumer libraries can keep the same general integration model. MSK also runs in a VPC and can be deployed across multiple Availability Zones to reduce the operational burden of managing broker nodes.

    #### Distractor Analysis
    * **A is Incorrect:** Kinesis Data Streams is appropriate for real-time streaming ingestion and custom consumers. However, this approach requires changing applications to use Kinesis APIs, which does not preserve the existing broker client integration requirement.
    * **C is Incorrect:** Managed Service for Apache Flink is used to process and analyze streaming data from sources such as Kinesis data streams or Kafka topics. It is not a replacement for the ingestion broker itself, so it does not satisfy the need to preserve broker client applications.
    * **D is Incorrect:** Amazon Data Firehose is useful for fully managed delivery to destinations such as Amazon S3, Redshift, OpenSearch, or HTTP endpoints. It is not a managed event broker for existing topic-based producers and consumers, and it does not provide the same consumer application model.

    #### Overall Explanation
    Amazon MSK is the best fit when a team already has applications built around Apache Kafka-style topics, producers, and consumers but wants AWS to manage the broker infrastructure. The service is intended for creating, managing, and using managed Kafka clusters on AWS, which reduces operational work compared with running broker nodes on EC2. See the official What is Amazon MSK? [https://docs.aws.amazon.com/msk/latest/developerguide/what-is-msk.html] documentation.
    
    Kinesis Data Streams is also a real-time streaming service, but choosing it would usually require changing producer and consumer code to use Kinesis APIs and the Kinesis consumer model. Amazon Data Firehose is more delivery-oriented: it buffers and delivers streaming data to destinations such as S3 or OpenSearch, with optional transformation, but it is not a replayable topic broker for existing consumer applications. Managed Service for Apache Flink is a stream processing service that reads from streaming sources and writes processed results, so it complements an ingestion layer rather than replacing a managed broker. For related service roles, see What is Amazon Kinesis Data Streams? [https://docs.aws.amazon.com/streams/latest/dev/introduction.html], Amazon Data Firehose documentation [https://docs.aws.amazon.com/firehose/latest/dev/], and Sources for Managed Service for Apache Flink [https://docs.aws.amazon.com/managed-flink/latest/java/how-sources.html].

---

### Question 10

**Category:** Content Domain 2: ML Model and Foundation Model (FM) Develop  
**Status:** ✅ **Correct**

A pharmaceutical safety team is preparing a new prompt version for an Amazon Bedrock application that drafts responses to medication inquiries. Before promotion, pharmacists must review a representative evaluation set for accuracy, completeness, tone, and safe handling of sensitive information. In production, the application must also apply policy controls to every prompt and generated response, because user behavior and retrieved context can change over time.

Which solution will meet these requirements?

* **A)** Run a Bedrock human model evaluation with the safety reviewers, and attach Bedrock Guardrails to the application requests and responses.
* **B)** Deploy Bedrock Guardrails for the application flow, and skip pre-release expert review when the guardrail policies pass tests.
* **C)** Compare candidate responses by using ROUGE and BERTScore, and promote the prompt when both scores improve against references.
* **D)** Run a Bedrock automatic model evaluation with toxicity metrics, and let reviewers inspect only the CloudWatch invocation metrics.

??? note "Click to reveal Answer & Explanation"
    **Correct Answer:** **A**

    #### Correct Option Analysis
    * **A is Correct:** This solution separates pre-release evaluation from runtime enforcement. Human evaluation lets pharmacists judge workload-specific quality dimensions, while guardrails apply policy controls during each live interaction.

    #### Distractor Analysis
    * **B is Incorrect:** Guardrails are runtime safeguards, not a substitute for evaluation of model and prompt behavior against a representative dataset. Passing guardrail tests does not prove that responses are complete, clinically accurate, or useful for the intended task.
    * **C is Incorrect:** ROUGE and BERTScore can provide useful automated signals for text generation quality, but they are incomplete for high-risk, judgment-heavy reviews. Improved scores do not ensure that pharmacists agree the responses are safe, complete, and appropriate.
    * **D is Incorrect:** Automatic metrics can help measure selected quality or safety attributes, but they do not replace expert review for nuanced clinical correctness and tone. CloudWatch invocation metrics describe operational behavior, not whether generated medical responses are accurate or appropriate.

    #### Overall Explanation
    For generative AI systems, evaluation and runtime safeguards solve different problems. Human evaluation measures whether a candidate prompt or model behaves acceptably on an evaluation dataset, especially when correctness, completeness, tone, or safety require subject matter judgment. Bedrock Guardrails apply policy controls in the application flow for live prompts and responses, which helps manage changing user inputs, retrieved context, and model behavior after deployment.
    
    Amazon Bedrock supports model evaluations that can use automated metrics, LLM-as-a-judge, or human workers, as described in the Amazon Bedrock evaluations overview [https://docs.aws.amazon.com/bedrock/latest/userguide/evaluation.html]. For a workload that requires pharmacists to review generated answers, a human evaluation job with an appropriate work team is the integrated approach, and the setup process is covered in Create a model evaluation job that uses human workers [https://docs.aws.amazon.com/bedrock/latest/userguide/model-evaluation-jobs-management-create-human.html]. Automated metrics such as ROUGE or BERTScore are useful supporting signals, but they should not be treated as exact-output gates for nuanced text generation quality. Similarly, guardrails should not be used as the only release criterion, because runtime policy enforcement does not measure whether the prompt version produces high-quality answers across the evaluation dataset.

---

### Question 11

**Category:** Content Domain 3: Deployment and Orchestration of ML and AI  
**Status:** ✅ **Correct**

A municipal tax office's automation team uses Amazon Bedrock Knowledge Bases for a RAG assistant that answers employee questions about current tax filing rules. The source S3 bucket also contains old draft procedures, scanned payment receipts, and legacy training slide decks. The assistant sometimes retrieves unrelated passages, and the team wants to reduce embedding and vector store costs without reducing answer coverage for the current rules.

Which solution will meet these requirements with the LEAST operational overhead?

* **A)** Use a larger foundation model for generation and keep the full vector index in place.
* **B)** Increase the retrieved result count for each query and retain the full document source.
* **C)** Generate fresh embeddings for all source documents at query time before answering.
* **D)** Limit the knowledge base data source to current rule documents and resynchronize the index.

??? note "Click to reveal Answer & Explanation"
    **Correct Answer:** **D**

    #### Correct Option Analysis
    * **D is Correct:** This option keeps the vector index focused on the content that the assistant actually needs for retrieval. Reducing unrelated indexed content can lower embedding and vector store usage while improving the relevance of retrieved passages.

    #### Distractor Analysis
    * **A is Incorrect:** A larger foundation model might improve generation quality in some cases, but it does not fix irrelevant retrieval from the vector index. This option can increase inference cost and leaves the existing embedding and vector store footprint unchanged.
    * **B is Incorrect:** Increasing the number of retrieved results can add more context, but it can also return more irrelevant passages from unrelated documents. This option does not reduce embedding or vector store costs because the unnecessary content remains indexed.
    * **C is Incorrect:** Generating embeddings for the full document set on every query is an inefficient pattern for a knowledge base workload. Knowledge bases are designed to ingest, chunk, embed, and index documents ahead of retrieval, then synchronize the index when source content changes.

    #### Overall Explanation
    In a RAG workload, an Amazon Bedrock knowledge base retrieves relevant chunks from an indexed document collection before the foundation model generates an answer. The vector store is most useful when it contains content that matches the application's retrieval purpose, because unrelated documents increase storage, indexing, query, and context costs while making semantic search less precise.
    
    The practical optimization is to index only the content that retrieval actually needs. After narrowing the data source to the current rule documents, the team should synchronize the knowledge base so the ingestion process parses, chunks, embeds, and indexes the intended corpus. See Build a knowledge base in Amazon Bedrock [https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base-build.html] and Sync to ingest your data sources into your Amazon Bedrock knowledge base [https://docs.aws.amazon.com/bedrock/latest/userguide/kb-data-source-sync-ingest.html].
    
    Increasing the number of retrieved results treats the symptom by adding more context, but it can also increase token usage and bring in more irrelevant passages. Choosing a larger foundation model does not correct the retrieval index, and re-embedding all documents for every user query is an avoidable cost anti-pattern compared with maintaining an indexed knowledge base.

---

### Question 12

**Category:** Content Domain 4: Operating, Monitoring, and Securing ML and  
**Status:** ✅ **Correct**

A commercial real estate brokerage's AI team runs an AWS Lambda application that calls Amazon Bedrock to draft property listing summaries. During a security review, the team discovers a long-term Amazon Bedrock API key committed to the application repository and copied into multiple deployment environments. The team must reduce credential exposure, support least privilege, and avoid static bearer tokens in production.

Which solution will meet these requirements?

* **A)** Store the long-term Bedrock API key in AWS Secrets Manager, and let the function retrieve the secret at runtime.
* **B)** Encrypt the long-term Bedrock API key with AWS KMS, and decrypt the key into the function environment.
* **C)** Assign the Lambda execution role least-privilege Bedrock permissions, and remove API keys from code and configuration.
* **D)** Generate short-term Bedrock API keys for each release, and publish the newest key through the deployment pipeline.

??? note "Click to reveal Answer & Explanation"
    **Correct Answer:** **C**

    #### Correct Option Analysis
    * **C is Correct:** This solution uses AWS IAM permissions for a production AWS workload instead of a static bearer token. The Lambda execution role supplies temporary credentials to the function, and the permissions can be scoped to only the required Bedrock actions.

    #### Distractor Analysis
    * **A is Incorrect:** This solution improves storage of the secret compared with committing the key to source control. However, the production application still depends on a long-term bearer token instead of IAM-based temporary credentials.
    * **B is Incorrect:** AWS KMS can help protect secret material at rest, but the application would still use the same static API key after decryption. This approach does not provide IAM least privilege for the Bedrock calls or remove bearer-token exposure from the runtime.
    * **D is Incorrect:** Short-term API keys reduce the lifetime of a credential, but they still introduce bearer tokens into the deployment process. For production AWS workloads, IAM roles and temporary credentials are the safer operational pattern.

    #### Overall Explanation
    For a production workload that runs on AWS, the preferred pattern is to use an IAM role attached to the compute service and to grant only the permissions that the workload needs. In Lambda, the execution role is the identity that the function assumes, so the application can call Amazon Bedrock by using AWS SDK credential resolution without storing a Bedrock API key in source code, environment configuration, or a deployment artifact.
    
    Amazon Bedrock API keys are useful for simpler development or experimentation workflows, but they are bearer-token-style credentials. Moving such a key to Secrets Manager or encrypting it with AWS KMS can reduce accidental exposure, but those controls do not change the fact that the application still depends on a static secret for production authorization.
    
    The security tradeoff is about more than where the secret is stored. IAM roles provide temporary credentials, integrate with IAM policy evaluation for least privilege, and avoid distributing a reusable token across environments. AWS also recommends protecting credentials and using IAM controls for Bedrock workloads, as described in Data protection in Amazon Bedrock [https://docs.aws.amazon.com/bedrock/latest/userguide/data-protection.html].

---

### Question 13

**Category:** Content Domain 2: ML Model and Foundation Model (FM) Develop  
**Status:** ✅ **Correct**

A professional sports analytics group trains a neural network on Amazon SageMaker AI to predict player injury risk from time-series data. A recent training run met the target validation metric, but the job took much longer than expected and used more GPU hours than the budget allows. Some team members want to move directly to a larger multi-instance GPU configuration for the next run. The ML engineer needs to choose a practical next step that supports an informed tradeoff among model quality, training duration, and cost.

Which solution will meet these requirements?

* **A)** Increase the number of training epochs on the same instance type and review only the final validation metric after training.
* **B)** Run an instrumented baseline that logs validation metrics in MLflow and resource utilization in CloudWatch before changing the setup.
* **C)** Apply quantization and pruning to the trained model before starting the next training job with the same training configuration.
* **D)** Move the training job to a larger distributed GPU cluster and compare only the final validation metric when the run finishes.

??? note "Click to reveal Answer & Explanation"
    **Correct Answer:** **B**

    #### Correct Option Analysis
    * **B is Correct:** This is the correct approach because the team needs evidence about convergence behavior and compute utilization before spending more on larger infrastructure. MLflow can track training metrics and parameters across runs, while CloudWatch can show whether CPU, GPU, memory, or disk resources are bottlenecks.

    #### Distractor Analysis
    * **A is Incorrect:** This is incorrect because more epochs generally increase training time and cost. If the model already reached the target validation metric, adding epochs without checking convergence curves can waste compute or increase overfitting risk.
    * **C is Incorrect:** This is incorrect because quantization and pruning are mainly used to reduce model size and inference resource requirements. These techniques do not by themselves identify whether the current training job is slow because of underutilized hardware, inefficient data loading, or unnecessary training steps.
    * **D is Incorrect:** This is incorrect because a larger distributed configuration can reduce wall-clock time but can also increase total cost if the workload does not scale efficiently. Comparing only the final metric does not reveal whether the extra compute improved convergence speed enough to justify the expense.

    #### Overall Explanation
    When a training job is too slow or expensive, the first engineering step is usually to measure before optimizing. Tracking validation metrics, loss curves, hyperparameters, and artifacts with tools such as MLflow helps determine whether the model keeps improving, plateaus early, or regresses across runs. CloudWatch metrics add the infrastructure view, such as whether compute resources are saturated or idle.
    
    Scaling to larger or distributed GPU infrastructure can be the right answer for some workloads, but it is not automatically cost effective. The useful comparison is not only final accuracy; it is the relationship among accuracy, convergence time, resource utilization, and total training cost. AWS describes SageMaker AI training as a workflow where you choose resources, monitor training progress, and evaluate cost-related tradeoffs in Train a Model with Amazon SageMaker AI [https://docs.aws.amazon.com/sagemaker/latest/dg/train-model.html]. AWS also discusses how larger or distributed training configurations should be evaluated for speedup and cost/performance in Distributed training scenarios [https://docs.aws.amazon.com/sagemaker/latest/dg/distributed-training-scenarios.html].
    
    The larger cluster option is a plausible but premature optimization because it may reduce elapsed time while increasing spend. Increasing epochs biases the tradeoff toward longer training without evidence that validation performance will improve. Quantization and pruning are valuable compression techniques, especially for deployment efficiency, but they do not answer the training-time question unless the team has already identified a model-size or compute bottleneck that those techniques address.

---

### Question 14

**Category:** Content Domain 2: ML Model and Foundation Model (FM) Develop  
**Status:** ✅ **Correct**

A municipal permitting office's AI engineering team uses Amazon Bedrock to produce plain-language summaries of zoning decisions. The team has an evaluation dataset that contains representative prompts and expert-written reference summaries. Different phrasings are acceptable if they preserve the same meaning. The team wants to baseline the approved release and automatically detect semantic quality regressions during prompt or model updates.

Which solution will meet these requirements?

* **A)** Create a new SageMaker Model Monitor schedule that compares Bedrock prompts with baseline constraints.
* **B)** Run Amazon Bedrock Model Evaluations with BERTScore thresholds against the reference-answer dataset.
* **C)** Run ROUGE-2 scoring in the pipeline and require high bigram overlap with each saved answer.
* **D)** Run CI tests that compare each generated answer to the saved answer by exact string matching.

??? note "Click to reveal Answer & Explanation"
    **Correct Answer:** **B**

    #### Correct Option Analysis
    * **B is Correct:** BERTScore compares generated text with reference text by using contextual embeddings, so it is better suited for detecting semantic differences than exact wording differences. Amazon Bedrock Model Evaluations can run a repeatable evaluation dataset and provide scores that can be compared against release thresholds.

    #### Distractor Analysis
    * **A is Incorrect:** SageMaker Model Monitor is not the recommended new monitoring approach in this exam context. It also does not directly evaluate semantic similarity for an Amazon Bedrock text generation application.
    * **C is Incorrect:** ROUGE-2 measures overlap of two-word sequences between generated and reference text. It can be useful for some summarization checks, but it is still sensitive to paraphrasing and synonyms when semantic equivalence is the main concern.
    * **D is Incorrect:** Exact string matching is too brittle for generated summaries because valid answers can use different words and sentence structures. This approach would reject acceptable paraphrases and would not provide a useful semantic performance baseline.

    #### Overall Explanation
    For a generative AI application, a useful performance baseline is often a set of prompts, reference responses, and measured quality scores rather than a fixed expected output string. BERTScore is appropriate when wording can vary because it uses contextual embeddings to compare semantic similarity between the generated response and the reference response.
    
    Amazon Bedrock Model Evaluations supports evaluating foundation model behavior against prompt datasets by using automated, human, or LLM-as-a-judge methods, depending on the test objective. The team can treat the approved release's scores as a baseline and block or investigate future prompt or model updates when scores fall below thresholds. See Amazon Bedrock model evaluation [https://docs.aws.amazon.com/bedrock/latest/userguide/evaluation.html].
    
    Exact string matching is an anti-pattern for most GenAI regression testing because the same correct answer can be phrased many ways. ROUGE-style n-gram overlap can be helpful for some text tasks, but it is less reliable when the requirement is preserving meaning rather than preserving word order. SageMaker Model Monitor is also not the right choice for new Bedrock semantic-quality monitoring in this scenario.

---

### Question 15

**Category:** Content Domain 4: Operating, Monitoring, and Securing ML and  
**Status:** ✅ **Correct**

A university admissions office's AI engineering team is building an Amazon Bedrock application that drafts scholarship eligibility explanations from documents staged in Amazon S3 before retrieval indexing. The source bucket can contain student identifiers and other sensitive data. The team must find sensitive data in the source documents before ingestion and must enforce responsible AI policies during each production request. The team wants to minimize custom processing code.

Which solution will meet these requirements?

* **A)** Enable SSE-KMS on the S3 staging bucket. Add prompt instructions that require redaction in the system prompt.
* **B)** Run Amazon Macie on the S3 staging bucket. Configure Amazon Bedrock Guardrails in the production inference flow.
* **C)** Run Amazon Bedrock Model Evaluations on the S3 staging bucket. Store flagged records in Amazon DynamoDB for review.
* **D)** Create CloudTrail trails for the S3 staging bucket. Use Prompt Management to version the assistant instructions.

??? note "Click to reveal Answer & Explanation"
    **Correct Answer:** **B**

    #### Correct Option Analysis
    * **B is Correct:** Amazon Macie is designed to discover sensitive data in Amazon S3, so it addresses inspection of source documents before they are indexed for retrieval. Amazon Bedrock Guardrails apply safeguards during production inference, so the application can enforce policy controls on prompts and responses.

    #### Distractor Analysis
    * **A is Incorrect:** SSE-KMS protects objects at rest, but it does not identify sensitive content inside source documents. Prompt instructions can guide model behavior, but they are not a runtime safeguard that reliably enforces responsible AI policies.
    * **C is Incorrect:** Amazon Bedrock Model Evaluations measure model and application behavior against evaluation datasets. They do not scan an S3 bucket for sensitive data before ingestion, and storing records in DynamoDB does not enforce runtime policy on each request.
    * **D is Incorrect:** CloudTrail records AWS API activity for auditing, but it does not inspect document contents for sensitive data. Prompt Management helps create and version reusable prompts, but it does not replace runtime guardrails for safety and sensitive data controls.

    #### Overall Explanation
    The requirements involve two different control points: source-data discovery before retrieval indexing and runtime safeguards during inference. Amazon Macie is the appropriate managed service for discovering sensitive data in S3 objects, which helps the team identify documents that need remediation before they become part of the retrieval corpus.
    
    Amazon Bedrock Guardrails are designed for the production application flow, where safeguards can be applied to user prompts and model responses. Guardrails can enforce responsible AI policies such as harmful content controls, denied topics, and sensitive-information handling, as described in Overview of Amazon Bedrock Guardrails safeguards [https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails.html] and Sensitive information filters for Amazon Bedrock Guardrails [https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-sensitive-filters.html]. Encryption, auditing, and prompt versioning are valuable controls, but they solve different problems: they do not discover sensitive content in S3 and do not enforce model-output policy on every production request. Model evaluation is also important for responsible AI, but evaluation measures behavior before or between releases, while guardrails enforce policy at runtime.

---

### Question 16

**Category:** Content Domain 2: ML Model and Foundation Model (FM) Develop  
**Status:** ✅ **Correct**

A global hotel chain's guest experience team stores customer chat messages in an Amazon S3 data lake. The messages are plain text and can be written in English or Spanish. Before the messages are analyzed by downstream reporting jobs, the team must identify the language of each message and flag messages that contain personally identifiable information (PII). The team wants to use a managed AWS AI service with the least custom ML development.

Which solution will meet these requirements?

* **A)** Use Amazon Transcribe to process each message and create a transcript with speaker labels.
* **B)** Use Amazon Comprehend to detect the dominant language and identify PII entities in each message.
* **C)** Use Amazon Textract to analyze each message and extract form fields for downstream redaction.
* **D)** Use Amazon Rekognition to inspect each message and detect moderation labels before routing.

??? note "Click to reveal Answer & Explanation"
    **Correct Answer:** **B**

    #### Correct Option Analysis
    * **B is Correct:** Amazon Comprehend is a managed natural language processing service for analyzing text. It can detect insights such as dominant language and PII entities, which matches the requirements for English and Spanish plain-text messages.

    #### Distractor Analysis
    * **A is Incorrect:** Amazon Transcribe converts spoken audio into text and supports transcription-related features. The messages are already stored as text, so creating transcripts from audio does not address the language and PII analysis requirements.
    * **C is Incorrect:** Amazon Textract is designed to extract text and structured data from documents such as forms and tables. The input in this scenario is already plain text, and the required tasks are language identification and PII detection rather than document extraction.
    * **D is Incorrect:** Amazon Rekognition analyzes images and videos for visual content such as objects, faces, text in images, and unsafe content. The scenario requires analysis of plain-text chat messages, so an image and video analysis service is not appropriate.

    #### Overall Explanation
    Amazon Comprehend is the best fit when the source data is text and the task is to extract natural language insights. For this workflow, the important distinction is that the team does not need to train a custom NLP model or first convert another media type into text. Comprehend provides managed text analysis capabilities such as dominant language detection and PII entity detection for supported text inputs, which downstream jobs can use for filtering, reporting, or additional governance steps.
    
    The other managed AI services solve different input and task problems. Amazon Textract extracts text and structure from scanned documents, forms, and tables, but it is not the right starting point for plain-text chat messages. Amazon Rekognition is for image and video analysis, and Amazon Transcribe is for speech-to-text conversion. For more information, see the Amazon Comprehend documentation on Insights [https://docs.aws.amazon.com/comprehend/latest/dg/concepts-insights.html], the Amazon Textract overview [https://docs.aws.amazon.com/textract/latest/dg/what-is.html], the Amazon Rekognition overview [https://docs.aws.amazon.com/rekognition/latest/dg/what-is.html], and the Amazon Transcribe overview [https://docs.aws.amazon.com/transcribe/latest/dg/what-is.html].

---

### Question 17

**Category:** Content Domain 2: ML Model and Foundation Model (FM) Develop  
**Status:** ✅ **Correct**

An online education provider's ML team trains a neural network in Amazon SageMaker AI to score short-answer responses. The team is tuning model architecture and hyperparameters. Some candidate runs may memorize training examples, while other candidate runs may fail to learn enough signal from the data. The team wants to compare candidates and catch generalization problems before deployment, without adopting services in maintenance mode.

Which actions should the team take? (Select TWO)

* **A)** Use CloudWatch CPU, GPU, memory, and disk metrics alone to select the candidate with the lowest compute utilization.
* **B)** Use TensorBoard on SageMaker AI to inspect training and validation curves during candidate training runs.
* **C)** Adopt SageMaker Debugger tensor rules for new jobs as the main mechanism to approve model promotion.
* **D)** Promote the candidate run with the lowest final training loss after completing the maximum configured epochs.
* **E)** Log training and validation losses, hyperparameters, and artifacts in SageMaker AI with MLflow for run comparison.

??? note "Click to reveal Answer & Explanation"
    **Correct Answer:** **B, E**

    #### Correct Option Analysis
    * **B is Correct:** This action is correct because TensorBoard is useful for visualizing training and validation curves and deeper training behavior. These curves help reveal patterns that suggest overfitting or underfitting before a model is promoted.
    * **E is Correct:** This action is correct because MLflow can track scalar metrics, parameters, hyperparameters, artifacts, and model lineage across training runs. Comparing these records helps the team identify which candidate generalizes better instead of relying on a single training metric.

    #### Distractor Analysis
    * **A is Incorrect:** This action is incorrect because CloudWatch infrastructure metrics help identify resource bottlenecks, throttling, and anomalous system behavior. These metrics do not measure whether the model is memorizing the training set or failing to learn the task.
    * **C is Incorrect:** This action is incorrect because SageMaker Debugger is in maintenance mode and should not be the go-forward choice for new monitoring workflows. Current practice is to use tools such as MLflow, TensorBoard, and CloudWatch for experiment tracking, model internals, and infrastructure metrics.
    * **D is Incorrect:** This action is incorrect because low training loss alone can indicate that the model fit the training examples too closely. The team must evaluate validation behavior and other generalization metrics before deciding that a candidate model is better.

    #### Overall Explanation
    Preventing overfitting and underfitting requires looking beyond the final training loss. A model that memorizes training examples can show excellent training performance while validation performance worsens, and a model that lacks capacity or is over-regularized can perform poorly on both training and validation data.
    
    MLflow in SageMaker AI helps preserve the context of each experiment, including losses, hyperparameters, parameters, artifacts, and lineage. That record makes it practical to compare candidate runs side by side and choose a model version based on reproducible evidence rather than intuition.
    
    TensorBoard complements MLflow by making training dynamics visible. Training and validation curves help engineers see when a run is converging, diverging, memorizing, or failing to learn enough signal, which supports earlier adjustment before deployment.
    
    CloudWatch is still useful, but for a different layer of the problem: CPU, GPU, memory, disk, latency, and error metrics describe infrastructure behavior, not model generalization. Choosing the lowest training loss or adopting maintenance-mode tooling as the primary new workflow misses the validation-based mental model described in the SageMaker AI guidance on using training and validation curves [https://docs.aws.amazon.com/sagemaker/latest/dg/train-valid-curve.html].

---

### Question 18

**Category:** Content Domain 4: Operating, Monitoring, and Securing ML and  
**Status:** ❌ **Incorrect**

A public transit agency's ML operations team runs a bus arrival delay model that receives route, stop, schedule, weather, and ridership features from several upstream systems. Recent deployments did not change the model code, but operators suspect that silent changes in the daily scoring data are affecting prediction quality. Ground-truth arrival outcomes are available only after operational reconciliation at the end of each week.

Which TWO actions should the team take to detect data distribution changes that can affect model performance?

* **A)** Enable KMS encryption on the scoring data and audit key usage events for abnormal access patterns.
* **B)** Track prediction-score distributions over time and investigate sustained shifts from an accepted baseline.
* **C)** Delay monitoring until labels arrive and evaluate only accuracy, precision, recall, and F1.
* **D)** Review CloudTrail API activity for endpoint changes and alert on unusual configuration writes.
* **E)** Check incoming records for missing fields, malformed values, unseen categories, and range violations.

??? note "Click to reveal Answer & Explanation"
    **Correct Answer:** **B, E**

    #### Correct Option Analysis
    * **B is Correct:** This action is correct because the model output distribution is a useful production signal when ground truth is delayed. A sustained shift in prediction scores does not prove model failure by itself, but it can reveal changes in the input population or upstream processing that warrant investigation.
    * **E is Correct:** This action is correct because input data issues are often the earliest observable signs that the production population no longer resembles the data used to validate the model. Missing features, malformed values, new categories, and unexpected ranges can change how the model interprets requests before labels are available.

    #### Distractor Analysis
    * **A is Incorrect:** This action is incorrect because AWS KMS helps protect data through encryption and access control. Encryption and key-use auditing do not measure whether the data values have shifted from the model's expected distribution.
    * **C is Incorrect:** This action is incorrect because outcome metrics are important but are not sufficient for early drift detection when labels arrive late. Waiting for labels can allow distribution changes to affect production predictions for days before the team notices.
    * **D is Incorrect:** This action is incorrect because CloudTrail is designed to record API activity and support auditing of user, role, and service actions. It can help identify who changed an endpoint configuration, but it does not analyze feature values or prediction distributions.

    #### Overall Explanation
    Detecting distribution changes in production requires signals that are available before business outcomes or labels arrive. For tabular prediction systems, useful signals include input data checks, such as missing or malformed features, unexpected ranges, and unseen categories, plus prediction or score distribution monitoring that shows whether model outputs are moving away from a known baseline.
    
    No single metric or threshold proves that every model is healthy. A shift in prediction scores might reflect seasonality, a legitimate change in ridership, or a broken upstream feed, so the monitoring system should trigger investigation rather than automatically assume retraining is required. Outcome metrics such as accuracy and F1 remain valuable after labels arrive, but they are lagging indicators in this scenario.
    
    CloudTrail and KMS solve different operational problems. CloudTrail helps audit API calls and configuration changes, while KMS helps encrypt and control access to data. These controls are important for operating secure ML systems, but they do not inspect the feature or output distributions that indicate data drift.
    
    AWS documentation describes these monitoring concepts in the context of SageMaker production monitoring, including comparing captured production data with baselines and surfacing drift-related results through reports and metrics. See Data quality monitoring [https://docs.aws.amazon.com/sagemaker/latest/dg/model-monitor-data-quality.html] and the SageMaker Model Monitor overview [https://docs.aws.amazon.com/sagemaker/latest/dg/model-monitor.html] for related monitoring patterns.

---

### Question 19

**Category:** Content Domain 1: Data Preparation for ML and AI  
**Status:** ✅ **Correct**

A municipal emergency response analytics team is preparing thousands of free-text incident notes for a traditional text classification model. The notes are stored in Amazon S3 and contain inconsistent casing, punctuation artifacts, and agency-specific radio call signs. The team wants a repeatable preprocessing workflow that converts the notes into numeric features for training and supports a small custom rule for splitting call signs. The team wants to avoid maintaining a custom Spark application.

Which solution will meet these requirements?

* **A)** Use Amazon QuickSight data preparation, and change field names, calculated fields, and data types before training.
* **B)** Use SageMaker Data Wrangler to lowercase and featurize text, and add a custom Python transform to split call signs.
* **C)** Use AWS Glue Studio to create a Spark ETL job, and hand-code tokenization, lowercasing, and vectorization in the job.
* **D)** Use Amazon Athena with the AWS Glue Data Catalog, and create SQL views that expose cleaned note columns for training.

??? note "Click to reveal Answer & Explanation"
    **Correct Answer:** **B**

    #### Correct Option Analysis
    * **B is Correct:** This option provides managed data preparation features for text featurization and supports custom transformations for rules that are specific to the team's domain. Lowercasing and text featurization address the inconsistent text representation, while the custom transform handles the radio call-sign pattern without requiring the team to maintain a full Spark application.

    #### Distractor Analysis
    * **A is Incorrect:** Amazon QuickSight data preparation is useful for preparing datasets for analysis and visualization tasks. It is not the right tool for creating a repeatable ML text preprocessing pipeline with tokenization, numeric text features, and custom token-splitting logic.
    * **C is Incorrect:** AWS Glue Studio can create managed ETL workflows, and Spark can implement text preprocessing logic. However, this approach requires the team to maintain the tokenization and vectorization code in a Spark job, which conflicts with the requirement to avoid maintaining a custom Spark application.
    * **D is Incorrect:** Athena and the AWS Glue Data Catalog are useful for querying data in Amazon S3 and managing table metadata. This approach does not provide a managed workflow for tokenization, text featurization, or custom call-sign splitting for model training.

    #### Overall Explanation
    Advanced text preprocessing usually has two related goals: make the raw text more consistent, and convert the text into a representation that a model can use. Normalization, such as lowercasing and handling unwanted characters, reduces unnecessary variation. Tokenization and featurization then turn text into model-ready features, such as token-based or vectorized representations.
    
    Amazon SageMaker Data Wrangler is a good fit when an ML engineer needs managed data preparation with text transformations and a limited amount of custom logic. The reference workflow here needs built-in text featurization plus a domain-specific rule for call signs, not a fully hand-built distributed text processing application. The Data Wrangler transform documentation describes text featurization and custom transforms: SageMaker Data Wrangler transforms [https://docs.aws.amazon.com/sagemaker/latest/dg/data-wrangler-transform.html].
    
    AWS Glue and Athena are common parts of data lake preparation, but they solve different problems. Glue crawlers and the Data Catalog help discover schemas and expose S3 data to query engines, while Athena helps query that data. They do not, by themselves, provide the ML-oriented text featurization workflow described in the scenario.
    
    QuickSight data preparation is aimed at dashboard and analysis preparation, such as calculated fields or data type changes. It is not intended to be the main tool for producing tokenized and vectorized training features. For ML text preprocessing, choose a tool that directly supports text featurization and custom transformation steps.

---

### Question 20

**Category:** Content Domain 3: Deployment and Orchestration of ML and AI  
**Status:** ❌ **Incorrect**

A pharmaceutical research platform team is deploying an agentic assistant on Amazon Bedrock. Researchers will ask the assistant to summarize cohort metadata and produce small derived tables. The assistant must decide when to call existing AWS Lambda functions, provide the required function inputs from the user request, and write short code snippets when calculations are needed. The team wants managed agentic infrastructure instead of building a custom tool router and code execution service.

Which solution will meet these requirements?

Your answer is incorrect

* **A)** Store tool instructions in Amazon Bedrock Prompt Management, and call the Lambda tools from the client application.
* **B)** Configure Amazon Bedrock Knowledge Bases for the Lambda tools, and run generated code in SageMaker notebooks.
* **C)** Deploy a SageMaker multi-container endpoint for the Lambda tools, and run generated code in the endpoint container.
* **D)** Configure Amazon Bedrock AgentCore Gateway for the Lambda tools, and enable the AgentCore Code Interpreter tool.

??? note "Click to reveal Answer & Explanation"
    **Correct Answer:** **D**

    #### Correct Option Analysis
    * **D is Correct:** This is correct because AgentCore Gateway exposes tools to agents and lets you define the parameters that a tool expects. AgentCore also provides a built-in Code Interpreter tool for agent workflows that need generated code for calculations or charts.

    #### Distractor Analysis
    * **A is Incorrect:** Prompt Management can version and reuse prompts, but it does not by itself expose tools to an agent through a managed gateway. Calling Lambda functions from the client application shifts tool routing logic into custom application code.
    * **B is Incorrect:** Knowledge Bases are used for retrieval-augmented generation from indexed data sources, not for exposing Lambda functions as callable tools. SageMaker notebooks can run code for development, but they do not provide a managed tool gateway for an agentic workflow.
    * **C is Incorrect:** A SageMaker multi-container endpoint is intended for hosting inference containers, not for giving an agent structured access to external tools. Running generated code inside an inference container is unnecessary custom infrastructure for this agentic use case.

    #### Overall Explanation
    Agentic workflow infrastructure separates the model's reasoning loop from the external capabilities that the agent can use. In Amazon Bedrock AgentCore, Gateway is the managed component that exposes tools to agents, including Lambda functions and API-based targets, with tool descriptions and input schemas that help the model decide when and how to call them. The Code Interpreter capability addresses the separate need to let an agent generate and execute short code for calculations or chart-like outputs without the team building its own execution service.
    
    Knowledge Bases solve a different problem: they add retrieval context from indexed documents for RAG. Prompt Management is useful for reusable and versioned prompts, but prompts alone do not provide a managed tool invocation layer. SageMaker endpoints are appropriate for model inference hosting, but using an endpoint container as an ad hoc tool router or generated-code environment is an operational anti-pattern for this requirement because it recreates capabilities that the agentic infrastructure already provides.
    
    For more information, see the Amazon Bedrock AgentCore overview in the Amazon Bedrock AgentCore Developer Guide [https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/what-is-bedrock-agentcore.html] and the Gateway concepts in Gateway core concepts [https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway-core-concepts.html].

---

### Question 21

**Category:** Content Domain 3: Deployment and Orchestration of ML and AI  
**Status:** ✅ **Correct**

A digital media studio's AI engineering team is building an Amazon Bedrock application that drafts localized marketing copy. The application must choose among approved prompt versions, call foundation models, and pass intermediate outputs through a managed workflow at request time. The team wants to build, test, and deploy the orchestration with the least custom coordination code.

Which solution will meet these requirements?

* **A)** Build the runtime orchestration in AWS CodePipeline, and promote prompt versions through deployment stages.
* **B)** Build the runtime orchestration as a SageMaker multi-container endpoint, and route prompts to separate containers.
* **C)** Build the runtime orchestration in Amazon Bedrock Flows, and invoke the deployed prompt versions from the flow.
* **D)** Build the runtime orchestration in Amazon SageMaker Pipelines, and invoke the prompt versions from pipeline steps.

??? note "Click to reveal Answer & Explanation"
    **Correct Answer:** **C**

    #### Correct Option Analysis
    * **C is Correct:** Amazon Bedrock Flows is designed for building, testing, and deploying generative AI workflows that connect prompts, foundation models, and other workflow steps. This approach keeps the request-time orchestration inside a managed Bedrock capability instead of requiring custom coordination code.

    #### Distractor Analysis
    * **A is Incorrect:** AWS CodePipeline can orchestrate CI/CD stages for application and artifact releases. It does not provide the request-time workflow execution that is needed to route prompts and call foundation models during each application interaction.
    * **B is Incorrect:** A SageMaker multi-container endpoint is a model hosting pattern for serving containers on a SageMaker endpoint. It does not natively orchestrate Amazon Bedrock prompt versions and foundation model calls as a managed GenAI workflow.
    * **D is Incorrect:** Amazon SageMaker Pipelines is intended for automating ML development workflows such as data processing, training, evaluation, and deployment. It is not the best fit for request-time orchestration of Bedrock prompts and foundation model calls in an interactive GenAI application.

    #### Overall Explanation
    Amazon Bedrock Flows is the best fit when the application needs managed, request-time orchestration for a generative AI workflow. A flow can connect Bedrock capabilities such as prompts and foundation model invocations so the team can build, test, and deploy the GenAI workflow without writing all of the control logic itself. See Amazon Bedrock Flows [https://docs.aws.amazon.com/en_en/bedrock/latest/userguide/flows.html].
    
    SageMaker Pipelines and AWS CodePipeline are orchestration tools, but they solve different problems. SageMaker Pipelines is purpose-built for ML development and deployment workflows, while CodePipeline coordinates software release stages. They are useful in CI/CD, but they are not the managed runtime path for choosing prompts and invoking Bedrock foundation models for each user request. See Amazon SageMaker Pipelines [https://docs.aws.amazon.com/sagemaker/latest/dg/pipelines.html] and SageMaker AI workflow orchestration [https://docs.aws.amazon.com/sagemaker/latest/dg/workflows.html].
    
    A SageMaker multi-container endpoint is a hosting strategy for model containers, not a Bedrock GenAI workflow orchestrator. Use SageMaker endpoint patterns when the main decision is how to host models for inference. Use Bedrock Flows when the main decision is how to coordinate prompts, model calls, and workflow logic in a Bedrock-based application.

---

### Question 22

**Category:** Content Domain 1: Data Preparation for ML and AI  
**Status:** ✅ **Correct**

A marine logistics operator's ML team is preparing historical maintenance notes in Amazon S3 for a text classification model. The team must lowercase text, remove boilerplate, tokenize or featurize the notes, and apply a small custom rule to preserve vessel codes before training. The team wants to stay within the SageMaker AI data preparation workflow and avoid building AWS Glue or Amazon EMR jobs.

Which actions will meet these requirements? (Select TWO)

* **A)** Use Amazon Data Firehose with Lambda transformation to process the historical notes into S3.
* **B)** Run an AWS Glue crawler on the S3 prefix to infer schema and tokenize notes in the Data Catalog.
* **C)** Prepare the dataset in Amazon QuickSight and publish the tokenized output as training data.
* **D)** Use SageMaker Data Wrangler text transforms to clean, featurize, and tokenize the maintenance notes.
* **E)** Add a SageMaker Data Wrangler custom transform for the vessel-code cleanup rule before export.

??? note "Click to reveal Answer & Explanation"
    **Correct Answer:** **D, E**

    #### Correct Option Analysis
    * **D is Correct:** SageMaker Data Wrangler includes transforms that are intended for cleaning, transforming, and featurizing data for ML preparation. For text data, this supports the required normalization and tokenization or featurization without requiring a separate ETL cluster.
    * **E is Correct:** SageMaker Data Wrangler supports custom transforms when built-in transforms do not cover a domain-specific rule. A custom transform is appropriate for preserving specialized vessel codes while keeping the workflow in SageMaker AI.

    #### Distractor Analysis
    * **A is Incorrect:** Amazon Data Firehose is designed for managed delivery of streaming data to destinations such as Amazon S3, with optional Lambda transformation. The requirement is to prepare existing historical text data inside a SageMaker AI data preparation workflow, so this service choice does not fit the stated workflow.
    * **B is Incorrect:** An AWS Glue crawler can discover schema information and populate the AWS Glue Data Catalog. The Data Catalog is a metadata repository, not a place to tokenize text or apply custom feature engineering logic.
    * **C is Incorrect:** Amazon QuickSight data preparation provides limited ETL for analytics datasets, such as changing field names, calculated fields, SQL queries, and data types. It is not the appropriate tool for ML-oriented text tokenization and feature preparation for SageMaker AI training.

    #### Overall Explanation
    SageMaker Data Wrangler is the best fit when the transformation work is part of ML data preparation and the team wants visual, SageMaker-native preprocessing. It can apply built-in transforms for cleaning and featurizing data, and it can also run custom transforms when domain rules are too specific for standard operations. See Transform data in Data Wrangler [https://docs.aws.amazon.com/sagemaker/latest/dg/data-wrangler-transform.html].
    
    The mental model is that Data Wrangler prepares model-ready datasets, while tools such as AWS Glue crawlers and the AWS Glue Data Catalog primarily help discover and organize schemas for query engines and ETL jobs. Amazon Data Firehose is useful for near real-time delivery and simple stream transformations, not for interactively preparing historical training text inside SageMaker AI. QuickSight preparation is aimed at analytics and visualization workflows, so it is not the right place to build tokenized training features.

---

### Question 23

**Category:** Content Domain 2: ML Model and Foundation Model (FM) Develop  
**Status:** ✅ **Correct**

A medical device manufacturer's ML team runs Amazon SageMaker AI automatic model tuning for an XGBoost classifier. The team has already configured validation AUC as the objective metric and has defined hyperparameter ranges. Some candidate configurations use many boosting rounds but show poor validation results early in training. Each training job is costly, and the team wants the tuning process to avoid spending full training time on trials that are unlikely to improve the best objective metric.

Which solution will meet these requirements with the least wasted training time?

* **A)** Set early stopping type to Auto and keep validation AUC as the tuning objective.
* **B)** Increase the maximum parallel training jobs and keep the same hyperparameter ranges.
* **C)** Reduce the maximum training jobs and compare CloudWatch metrics after completion.
* **D)** Switch the tuning objective to training accuracy and keep early stopping turned off.

??? note "Click to reveal Answer & Explanation"
    **Correct Answer:** **A**

    #### Correct Option Analysis
    * **A is Correct:** This option is correct because SageMaker AI automatic model tuning can use automatic early stopping to stop training jobs that are unlikely to produce a better objective metric. Keeping validation AUC as the objective preserves the team's stated selection criterion while reducing wasted time on weak trials.

    #### Distractor Analysis
    * **B is Incorrect:** This option is incorrect because increasing parallelism can make the tuning job finish sooner, but it does not reduce the amount of training performed by poor trials. This approach can also increase simultaneous resource usage without stopping unpromising training jobs early.
    * **C is Incorrect:** This option is incorrect because reducing the maximum number of jobs limits the search space but does not identify weak trials during training. Reviewing CloudWatch metrics after completion does not provide an automated way to stop poor training jobs before they finish.
    * **D is Incorrect:** This option is incorrect because training accuracy is not the metric that the team configured to evaluate model quality. Keeping early stopping turned off allows each trial to continue to its normal completion, which does not meet the goal of reducing wasted training time.

    #### Overall Explanation
    Amazon SageMaker AI automatic model tuning searches across configured hyperparameter ranges by launching training jobs and comparing their results against an objective metric. In this scenario, the team has already chosen validation AUC as the objective, so the optimization process should continue to rank candidates by validation performance rather than switching to a training-only metric.
    
    Automatic early stopping is appropriate when a trial is unlikely to improve the best objective metric and continuing the trial would consume training time without much expected value. The tradeoff is that the tuning job still explores the hyperparameter space, but SageMaker AI can spend less time on configurations that appear unpromising during training.
    
    Increasing parallelism can reduce wall-clock time, but it does not reduce the total training work for weak candidates. Reducing the maximum number of jobs may reduce cost, but it can cut off the search without using training progress to decide which trials should stop. For more information, see Perform automatic model tuning with SageMaker AI [https://docs.aws.amazon.com/sagemaker/latest/dg/automatic-model-tuning.html] and How hyperparameter tuning works [https://docs.aws.amazon.com/sagemaker/latest/dg/automatic-model-tuning-how-it-works.html].

---

### Question 24

**Category:** Content Domain 1: Data Preparation for ML and AI  
**Status:** ✅ **Correct**

A marine insurance analytics team is preparing a supervised training dataset from claim photos and adjuster notes. Human annotators assign damage categories and severity labels. The ML engineer must improve the integrity of the labeled dataset before training and reduce the risk that the model learns inconsistent or incorrect labels.

Which actions should the ML engineer take? (Select TWO.)

* **A)** Delete records from underrepresented classes whenever annotators disagree about a label.
* **B)** Create annotation instructions with examples and edge-case rules before labeling new records.
* **C)** Train immediately on the first completed labels and use validation accuracy to find bad records.
* **D)** Assign overlapping reviews to sampled items and adjudicate disagreements before training.
* **E)** Use Amazon Bedrock Guardrails as a substitute for label review and skip reviewing the labeled dataset.

??? note "Click to reveal Answer & Explanation"
    **Correct Answer:** **B, D**

    #### Correct Option Analysis
    * **B is Correct:** Clear annotation guidance reduces guesswork and makes labels more consistent across annotators. Examples and edge-case rules help workers apply the same decision criteria when claim evidence is ambiguous.
    * **D is Correct:** Multiple reviews make it possible to compare annotator agreement and identify labels that need correction. Adjudicating disagreements before training helps prevent inconsistent examples from becoming training signal.

    #### Distractor Analysis
    * **A is Incorrect:** Removing records only because they are difficult can distort the class distribution and may increase bias or class imbalance. Disagreements should be reviewed and resolved rather than automatically discarded.
    * **C is Incorrect:** Training first can hide data quality problems because incorrect labels may appear as model errors rather than dataset defects. Label validation should happen before training so the model does not learn avoidable mistakes.
    * **E is Incorrect:** Amazon Bedrock Guardrails can help evaluate or filter generative AI inputs and responses, and they can also be applied to text independently of model invocation. Guardrails do not replace supervised training-label validation, annotator agreement checks, or adjudication of disputed claim labels.

    #### Overall Explanation
    Training-data integrity is not only about file format. For supervised learning, the labels themselves must be semantically trustworthy, so the team should use clear annotation guidelines, examples, and a review process that can detect inconsistent labeling before model training begins.
    
    Overlapping review and adjudication trade additional cost and time for higher label quality. This is especially useful for ambiguous examples, low-confidence labels, or labels with business consequences. Training on the first completed labels is an anti-pattern because the model can learn bad labels, and later validation metrics may not clearly identify whether the root cause is model behavior or poor data. Amazon Bedrock Guardrails can help evaluate and filter generative AI inputs and outputs, including by using ApplyGuardrail independently of model invocation, but guardrails are not a substitute for validating human-provided supervised labels. AWS documentation discusses label verification and adjustment concepts in Label verification and adjustment [https://docs.aws.amazon.com/sagemaker/latest/dg/sms-verification-data.html], guardrail behavior in Amazon Bedrock Guardrails [https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails.html], and independent guardrail checks in Use the ApplyGuardrail API [https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-use-independent-api.html].

---

### Question 25

**Category:** Content Domain 4: Operating, Monitoring, and Securing ML and  
**Status:** ✅ **Correct**

A legal research publisher's AI operations team uses Amazon Bedrock foundation models to summarize new court opinions for subscribers. After launch, the team needs continuous production visibility into inference traffic, response latency, token consumption, throttling, and errors so engineers can set alarms when the workload changes. The team does not need to score generated answers against a benchmark dataset for this requirement.

Which solution will meet these requirements with the LEAST operational overhead?

* **A)** Record Amazon Bedrock API calls with AWS CloudTrail and enable CloudTrail Insights for unusual account management activity patterns.
* **B)** Monitor Amazon Bedrock runtime metrics in Amazon CloudWatch for inference traffic, response latency, token usage, throttles, and errors.
* **C)** Run Amazon Bedrock model evaluation jobs for a prompt dataset and review quality, safety, and bias reports as release gates.
* **D)** Export generated responses to Amazon S3 and query them with Amazon Athena to estimate token totals and latency trends from logs each night.

??? note "Click to reveal Answer & Explanation"
    **Correct Answer:** **B**

    #### Correct Option Analysis
    * **B is Correct:** Amazon Bedrock publishes runtime metrics that are suitable for monitoring live inference behavior. CloudWatch dashboards and alarms can track traffic, latency, token usage, throttling, and errors without requiring a custom metrics pipeline.

    #### Distractor Analysis
    * **A is Incorrect:** CloudTrail is appropriate for auditing API activity and identifying unusual management activity patterns. It is not designed to provide operational inference metrics such as response latency, token usage, throttles, or runtime error rates.
    * **C is Incorrect:** Amazon Bedrock evaluations are useful for measuring model behavior against datasets, including quality and safety-related metrics. They do not provide continuous production monitoring of latency, throttling, errors, and token consumption for live inference traffic.
    * **D is Incorrect:** Application logs in Amazon S3 can support offline analysis if the application records the needed data. This approach adds custom operational work and does not provide the managed, near-real-time monitoring and alarm capability required for live workload changes.

    #### Overall Explanation
    For a production foundation model application, runtime monitoring and model evaluation answer different questions. CloudWatch runtime metrics help operators understand whether live inference is healthy, including traffic volume, latency, token consumption, throttling, and errors. This is the right fit when the requirement is continuous visibility and alarms rather than offline scoring of generated answers.
    
    Amazon Bedrock evaluations are still important, but they are primarily used to assess model or application behavior against prompt datasets, human judgments, automated metrics, or LLM-as-a-judge workflows. That makes evaluations useful for release validation, model comparison, safety checks, and regression testing, but not as the main mechanism for live operational alarms. CloudTrail complements these tools by recording API activity for audit and investigation, while custom S3 and Athena analysis can be useful later but usually has more delay and operational overhead than managed CloudWatch metrics.
    
    See the Amazon Bedrock documentation for monitoring runtime metrics [https://docs.aws.amazon.com/bedrock/latest/userguide/monitoring-runtime-metrics.html] and the overview of Amazon Bedrock evaluations [https://docs.aws.amazon.com/bedrock/latest/userguide/evaluation.html].

---

### Question 26

**Category:** Content Domain 1: Data Preparation for ML and AI  
**Status:** ✅ **Correct**

A mobile game studio's personalization team receives player events from match servers throughout the day. The team wants a managed feature repository that several models can reuse. The game API must retrieve the latest per-player feature values when it decides which in-game offer to show during an active match.

Which TWO actions will meet these requirements?

* **A)** Ingest updates with PutRecord, and retrieve current feature records with GetRecord at serving time.
* **B)** Enable the online store on a SageMaker Feature Store feature group for player feature records.
* **C)** Deliver events to Amazon Data Firehose, and run Spark consumers that read directly from Firehose.
* **D)** Maintain one S3 feature dataset per model, and use AWS Glue crawlers to publish schemas.
* **E)** Query the offline S3 store with Athena from the game API for every in-match offer decision.

??? note "Click to reveal Answer & Explanation"
    **Correct Answer:** **A, B**

    #### Correct Option Analysis
    * **A is Correct:** PutRecord and GetRecord are the Feature Store APIs used for streaming writes and reads of feature records. This action fits a serving path that needs current values during an active user interaction.
    * **B is Correct:** This action supports low-latency access to current feature values for serving use cases. A feature group also gives the team a managed place to organize and reuse feature definitions across models.

    #### Distractor Analysis
    * **C is Incorrect:** Amazon Data Firehose is a managed delivery service for destinations such as Amazon S3, Amazon Redshift, and Amazon OpenSearch Service. It is not a Feature Store serving interface, and Spark or KCL consumers do not read directly from Firehose.
    * **D is Incorrect:** AWS Glue crawlers can discover schemas and populate the AWS Glue Data Catalog for data in Amazon S3. This action does not provide a managed online feature repository or a low-latency record lookup path for the game API.
    * **E is Incorrect:** The offline store is useful for batch access and historical training datasets through S3-compatible analytics tools. Athena queries are not the right serving mechanism for retrieving current feature values during every API request.

    #### Overall Explanation
    SageMaker Feature Store is designed to manage, share, and serve features instead of leaving each model team to maintain separate feature files. A feature group can be configured with an online store for low-latency access to current feature records and an offline store for historical analysis and training data. For the serving requirement in this scenario, the online store and the PutRecord and GetRecord APIs are the appropriate fit.
    
    The offline store is valuable when data scientists need batch access through Amazon S3 based tools such as Athena, but it is not the right path for every real-time application request. Amazon Data Firehose, AWS Glue, and Athena can all be useful in data pipelines, but they do not replace Feature Store's managed feature serving capability. For more information, see Amazon SageMaker AI Feature Store [https://docs.aws.amazon.com/sagemaker/latest/dg/feature-store.html], Feature Store storage configurations [https://docs.aws.amazon.com/sagemaker/latest/dg/feature-store-storage-configurations.html], and Ingest data into Feature Store [https://docs.aws.amazon.com/sagemaker/latest/dg/feature-store-ingest-data.html].

---

### Question 27

**Category:** Content Domain 4: Operating, Monitoring, and Securing ML and  
**Status:** ✅ **Correct**

A legal aid nonprofit's AI engineering team operates a GenAI assistant on Amazon Bedrock that drafts client intake summaries. The service can generate different acceptable phrasings for the same intake details. After prompt changes, reviewers need objective evidence that the summaries remain accurate, safe, and unbiased. In production, the team also wants to detect drift as client questions and retrieved context change, and to alarm when trends move outside agreed thresholds.

Which TWO actions should the team take?

* **A)** Create exact-match unit tests for generated summaries and reject each prompt version when punctuation, synonyms, or sentence order changes.
* **B)** Run Amazon Bedrock Model Evaluations on a held-out prompt dataset with quality and safety criteria that allow semantically equivalent wording.
* **C)** Use CloudWatch generative AI observability and a drift pipeline to track invocation, latency, token, error, input, and output trends.
* **D)** Replace model evaluations with Amazon Bedrock Guardrails and treat every blocked or redacted response as an accuracy and bias score.
* **E)** Use CloudTrail Insights events for unusual write API activity and configure those account-level anomaly events as the primary drift alarms for the GenAI application.

??? note "Click to reveal Answer & Explanation"
    **Correct Answer:** **B, C**

    #### Correct Option Analysis
    * **B is Correct:** Amazon Bedrock Model Evaluations can assess model behavior against prompt datasets using automated metrics, human review, or LLM judges. Because GenAI output can vary, scoring semantic quality and safety against criteria is more appropriate than requiring identical wording.
    * **C is Correct:** CloudWatch generative AI observability provides operational visibility for model invocations and related runtime signals. A drift pipeline adds workload-specific comparisons of production inputs, retrieved context, and outputs against a baseline, and CloudWatch alarms can notify operators when metrics move outside thresholds.

    #### Distractor Analysis
    * **A is Incorrect:** This is an anti-pattern for GenAI regression testing because model responses can vary even when the output is acceptable. Exact matching can reject good paraphrases and does not measure safety, bias, or semantic correctness.
    * **D is Incorrect:** Amazon Bedrock Guardrails enforce runtime safety policies on prompts and responses. Blocked or redacted response counts can be useful operational signals, but they do not replace evaluation metrics for accuracy, relevance, safety, or bias.
    * **E is Incorrect:** CloudTrail Insights detects unusual patterns in management write events in an AWS account. It does not compare prompts, retrieved context, model outputs, or label-based quality measurements against production baselines.

    #### Overall Explanation
    For production GenAI monitoring, separate evaluation from runtime observability. Amazon Bedrock Model Evaluations give a repeatable way to score prompts or model versions against a prompt dataset by using automated evaluation, human review, or LLM-based judging. This approach fits nondeterministic text generation because the test should judge whether the response satisfies quality and safety criteria, not whether it matches one exact string. See Amazon Bedrock evaluations [https://docs.aws.amazon.com/bedrock/latest/userguide/evaluation.html].
    
    CloudWatch generative AI observability is the operational layer for production signals such as invocations, latency, token usage, errors, and traces. A drift detection pipeline complements those metrics by comparing production inputs, retrieved context, and output distributions with a baseline, then publishing workload-specific metrics that can drive dashboards and alarms. Guardrails are still valuable for runtime policy enforcement, but they are not a substitute for evaluation, and CloudTrail Insights focuses on API activity rather than model behavior. For more information, see CloudWatch generative AI observability [https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/GenAI-observability.html].

---

### Question 28

**Category:** Content Domain 3: Deployment and Orchestration of ML and AI  
**Status:** ✅ **Correct**

A legal publisher's research platform team runs a RAG assistant by using Amazon Bedrock Knowledge Bases. The source repository receives a controlled publishing batch each night that can write hundreds of files over several hours. Attorneys use the assistant during business hours and need low-latency responses from a stable retrieval index. The team wants the index to include the latest batch by the next morning without starting redundant refresh work for each file write.

Which orchestration approach will meet these requirements?

* **A)** Update the Bedrock prompt template after the nightly batch and leave the knowledge base refresh cycle outside the pipeline.
* **B)** Trigger a knowledge base refresh for every source file write event and allow the nightly batch to create many refresh requests at once.
* **C)** Schedule one knowledge base refresh after the nightly publish job and keep query handling separate from refresh orchestration.
* **D)** Start a knowledge base refresh inside each attorney query request and delay every generated answer until the refresh finishes successfully.

??? note "Click to reveal Answer & Explanation"
    **Correct Answer:** **C**

    #### Correct Option Analysis
    * **C is Correct:** This approach matches the update pattern because the source changes arrive as a predictable batch. Running one refresh after the batch completes avoids unnecessary refresh attempts during publishing and keeps inference requests from waiting on ingestion work.

    #### Distractor Analysis
    * **A is Incorrect:** Prompt changes can alter instructions or formatting, but they do not update the retrieval index. The knowledge base still needs an ingestion or synchronization step before newly added, modified, or deleted content can be reflected in retrieval.
    * **B is Incorrect:** This approach reacts to partial batch activity instead of the completed publishing cycle. It can create redundant refresh attempts while the repository is still changing, which does not provide a stable index during the batch.
    * **D is Incorrect:** This approach couples ingestion with interactive inference, which can increase latency for users. It also repeats refresh work even when many users ask questions against the same unchanged batch.

    #### Overall Explanation
    For a RAG system, the retrieval index is a separate operational artifact from the prompt and application code. Amazon Bedrock Knowledge Bases ingests source documents, chunks them, creates embeddings, and updates the backing vector store so retrieval can return current context for the model.
    
    When changes arrive as a predictable batch, a scheduled refresh after the publishing job is usually the right orchestration pattern. It avoids an anti-pattern where every file write or every user request initiates ingestion, which can waste capacity and introduce inconsistent behavior while the source repository is still being updated.
    
    The important design tradeoff is to decouple index maintenance from interactive inference. Attorneys can continue to use a stable retrieval index during business hours, while the pipeline refreshes the knowledge base outside the request path and makes the new content available after the nightly batch has been processed.
    
    Amazon Bedrock provides APIs for knowledge base ingestion jobs, including StartIngestionJob, which can be invoked by an external scheduler or workflow when the source update process is ready. See the official AWS documentation for StartIngestionJob [https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent_StartIngestionJob.html].

---

### Question 29

**Category:** Content Domain 4: Operating, Monitoring, and Securing ML and  
**Status:** ✅ **Correct**

A maritime shipping analytics team runs two Apache Spark workloads on Amazon EMR for ML feature generation. A nightly manifest-normalization workflow launches a transient cluster, writes durable outputs to Amazon S3, and can rerun failed work without missing service-level objectives. A separate analyst cluster stays online during business hours for repeated feature-history queries and has a steady baseline of EC2 usage. The team wants to reduce infrastructure costs by selecting purchasing options without rewriting Spark applications.

Which TWO actions should the team take?

* **A)** Use Spot Instance task nodes for transient EMR Spark jobs that can rerun failed work.
* **B)** Use On-Demand Instances for transient EMR clusters and only enable auto-termination.
* **C)** Use Reserved Instances for the stable EC2 capacity behind long-running EMR clusters.
* **D)** Purchase Bedrock Provisioned Throughput for the Spark jobs submitted to EMR.
* **E)** Use Spot Instances for all nodes in the long-running analyst EMR cluster.

??? note "Click to reveal Answer & Explanation"
    **Correct Answer:** **A, C**

    #### Correct Option Analysis
    * **A is Correct:** This option is correct because EMR task nodes can use Spot Instances for temporary capacity. The nightly workflow is transient and can rerun failed work, so interruption risk is acceptable for the cost savings.
    * **C is Correct:** This option is correct because the analyst cluster has a predictable baseline of EC2 usage. Reserved Instances are appropriate for long-running clusters where the team expects to keep capacity in use consistently.

    #### Distractor Analysis
    * **B is Incorrect:** This option is incorrect because auto-termination helps avoid idle cluster charges after work completes, but it does not reduce the running instance rate. For interruptible transient capacity, Spot task nodes provide a more cost-focused purchasing choice.
    * **D is Incorrect:** This option is incorrect because Bedrock Provisioned Throughput applies to foundation model inference capacity. It does not purchase or discount the EC2 compute that Amazon EMR uses to run Spark workloads.
    * **E is Incorrect:** This option is incorrect because Spot capacity is best suited to temporary or interruptible capacity. Using Spot for all nodes in a cluster that must remain available during business hours creates avoidable interruption risk.

    #### Overall Explanation
    For ML operations, selecting a purchasing option starts with separating steady baseline usage from interruptible burst capacity. Amazon EMR clusters run on EC2 instances, so a transient Spark workflow that can rerun failed work is a good fit for Spot task nodes, while a long-running cluster with predictable usage is a better fit for a commitment-based purchase such as Reserved Instances. This follows the same cost-optimization mental model AWS describes for ML services: use spare-capacity options for interruptible work, and use commitment purchases when utilization is predictable, as shown in SageMaker AI Managed Spot Training [https://docs.aws.amazon.com/sagemaker/latest/dg/model-managed-spot-training.html] and AWS Savings Plans types [https://docs.aws.amazon.com/savingsplans/latest/userguide/plan-types.html].
    
    Auto-termination is still useful for transient EMR clusters, but it only avoids paying for idle time; it does not change the instance purchase rate while the cluster is running. Amazon Bedrock Provisioned Throughput is a purchasing model for foundation model inference capacity, not for Apache Spark jobs on Amazon EMR. Choosing Spot for all capacity in a long-running analyst cluster increases interruption exposure for a workload that needs availability, so it is a poor match for the stated usage pattern.

---

### Question 30

**Category:** Content Domain 2: ML Model and Foundation Model (FM) Develop  
**Status:** ✅ **Correct**

A museum digitization lab is fine-tuning a text generation model in Amazon SageMaker AI to create catalog descriptions from curator notes. Training metrics in MLflow and TensorBoard show that training loss keeps decreasing, but validation loss reaches its minimum halfway through training and then increases during later passes over the dataset. The lab wants to reduce overfitting without increasing training cost.

Which adjustment should the ML engineer make for the next training run?

* **A)** Increase the epoch count or maximum training steps to keep reducing training loss.
* **B)** Reduce the epoch count or maximum training steps to stop near the lowest validation loss.
* **C)** Increase the batch size while keeping the epoch count unchanged for the next run.
* **D)** Decrease the batch size while keeping the epoch count unchanged for the next run.

??? note "Click to reveal Answer & Explanation"
    **Correct Answer:** **B**

    #### Correct Option Analysis
    * **B is Correct:** This adjustment is correct because the validation loss pattern indicates that the model begins to overfit after a certain point in training. Reducing epochs or training steps stops the run closer to the point where the model generalized best on validation data.

    #### Distractor Analysis
    * **A is Incorrect:** This adjustment is incorrect because additional passes over the data are likely to worsen the observed overfitting pattern. Training loss alone is not the right signal when validation loss is already increasing.
    * **C is Incorrect:** This adjustment is incorrect because batch size affects how many examples are used in each optimization update, but it does not directly address excessive training duration. Keeping the same epoch count would still expose the model to the same number of full passes over the dataset.
    * **D is Incorrect:** This adjustment is incorrect because a smaller batch size changes optimization behavior and can increase the number of updates per epoch. It does not directly stop training at the point where validation performance is best.

    #### Overall Explanation
    When training loss decreases while validation loss increases, the model is fitting the training examples more closely but generalizing worse to unseen data. In that situation, the practical hyperparameter adjustment is to reduce the number of epochs or maximum training steps so training ends closer to the validation-loss minimum.
    
    Epoch count controls how many complete passes the model makes over the training dataset, while step count limits the number of optimizer updates. Both can act as training-duration controls, so lowering either one can reduce overfitting and also reduce training cost. Batch size is important for memory use, convergence behavior, and update stability, but changing batch size while leaving training duration unchanged is not the most direct fix for a model that has already trained too long.
    
    In practice, teams often use MLflow or TensorBoard curves to identify the point where validation metrics stop improving, then update hyperparameters or add an early stopping strategy for future runs. For related AWS guidance on text generation fine-tuning hyperparameters such as epochCount, batchSize, and learningRate, see SageMaker text generation fine-tuning hyperparameters [https://docs.aws.amazon.com/sagemaker/latest/dg/autopilot-llms-finetuning-hyperparameters.html].

---

### Question 31

**Category:** Content Domain 3: Deployment and Orchestration of ML and AI  
**Status:** ✅ **Correct**

A city planning department's AI engineering team maintains an Amazon Bedrock application that answers zoning questions by using a knowledge base. The source documents change every night. The team needs an automated release test that confirms updated documents are reflected in retrieval and that answer quality has not regressed before the refreshed application is released.

Which approach should the team implement?

* **A)** Confirm knowledge base ingestion completes, then run a fixed retrieve-and-generate RAG evaluation before release.
* **B)** Run token counting on common prompts, reduce the response length, and release after estimated cost decreases.
* **C)** Deploy the refreshed application first, collect user feedback, and roll back if zoning answers are disputed.
* **D)** Publish a new prompt version, compare sample responses manually, and release after reviewers approve the wording.

??? note "Click to reveal Answer & Explanation"
    **Correct Answer:** **A**

    #### Correct Option Analysis
    * **A is Correct:** This approach keeps the retrieval index synchronized with changed source documents and treats ingestion completion as a prerequisite for testing. A retrieve-and-generate RAG evaluation exercises both the retrieved context and the final answer quality before the refreshed application is promoted.

    #### Distractor Analysis
    * **B is Incorrect:** Token counting is useful for cost estimation and can support price-to-performance decisions. However, lower token usage does not prove that the knowledge base is current or that retrieved context and generated answers remain accurate.
    * **C is Incorrect:** Releasing first and relying on user complaints is an anti-pattern for regression testing. This approach can expose users to stale or low-quality answers before the team validates retrieval and answer behavior.
    * **D is Incorrect:** Prompt versioning and manual review can help manage prompt changes, but they do not ensure that new, changed, or deleted source documents were processed into the retrieval index. This approach also relies on ad hoc review rather than a repeatable RAG evaluation set.

    #### Overall Explanation
    For a RAG-style application, the testing framework must validate both the retrieval layer and the generated answer. When source documents change, the knowledge base index must be synchronized, and the release process should wait for ingestion to finish before evaluating results.
    
    A practical workflow is to start an ingestion job, check that the job completed successfully, and then run a stable retrieve-and-generate RAG evaluation dataset that covers normal questions, edge cases, and important business scenarios. For a zoning assistant, that dataset should include prompts whose correct answers depend on recently changed ordinances, plus prompts that should continue to retrieve older but still valid documents.
    
    Prompt management, token counting, and human review can all be useful in the right context, but each addresses a different part of the system. Prompt versions manage reusable prompt artifacts, token counting estimates inference cost, and manual review can provide subjective judgment, but none of those steps by itself confirms that the vector index is current and that generated answers still meet quality thresholds.
    
    Amazon Bedrock supports evaluation workflows for assessing model and RAG application behavior, as described in Amazon Bedrock evaluations [https://docs.aws.amazon.com/bedrock/latest/userguide/evaluation.html]. Prompt artifacts can also be versioned and tested with Amazon Bedrock Prompt management, as described in Prompt management in Amazon Bedrock [https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-management.html].

---

### Question 32

**Category:** Content Domain 2: ML Model and Foundation Model (FM) Develop  
**Status:** ❌ **Incorrect**

A precision agriculture equipment maker's ML team trains an object detection model that depends on a proprietary camera decoding library and a custom CUDA extension. The same runtime must be used for both training and online inference in Amazon SageMaker AI. Managed framework containers and SageMaker AI built-in algorithms do not include the required runtime components. The team wants to keep using SageMaker managed jobs and endpoints.

Which solution will meet these requirements with the LEAST operational overhead?

Your answer is incorrect

* **A)** Use a SageMaker AI managed framework container, and install the decoding library from the training and inference scripts.
* **B)** Build a Docker image that includes the runtime components, and use the image for SageMaker AI training and hosting.
* **C)** Use a SageMaker AI built-in algorithm container, and upload the proprietary library with the training dataset.
* **D)** Run training on an Amazon EMR transient cluster, and invoke the model from a notebook instance for online inference.

??? note "Click to reveal Answer & Explanation"
    **Correct Answer:** **B**

    #### Correct Option Analysis
    * **B is Correct:** This approach keeps the team on SageMaker managed training and hosting while allowing the required libraries and custom CUDA extension to be packaged with the model code. A custom image is appropriate when built-in algorithms or managed framework containers do not provide the runtime components that the workload needs.

    #### Distractor Analysis
    * **A is Incorrect:** Managed framework containers are useful when the workload fits a supported framework and standard dependency pattern. In this scenario, the team needs a consistent runtime with proprietary and custom native components for both training and hosting, so relying on ad hoc script installation is not the best fit.
    * **C is Incorrect:** Built-in algorithm containers are designed for supported algorithm workflows, not for arbitrary runtime customization through the training data channel. Uploading a library with the dataset does not make the built-in algorithm container use a proprietary decoder or custom CUDA extension for training and inference.
    * **D is Incorrect:** Amazon EMR can run distributed data processing jobs, but this option moves away from SageMaker managed training and managed endpoints. A notebook instance is not an appropriate online inference serving layer for production requests.

    #### Overall Explanation
    SageMaker AI gives ML engineers several levels of abstraction for training and deployment. Use built-in algorithms when the algorithm and data format match the workload, use managed framework containers when standard libraries such as PyTorch, TensorFlow, or Scikit-learn are sufficient, and use a custom Docker image when the runtime itself must be controlled.
    
    In this scenario, the important constraint is not simply that the team has model code. The model depends on native runtime components that are absent from both managed framework images and built-in algorithm containers, and the same runtime is needed at inference time. Packaging those components in a Docker image lets SageMaker still manage jobs and endpoints while the team controls the execution environment.
    
    Uploading libraries as data is a poor fit because training data channels are not a mechanism for changing how a built-in algorithm container executes. Installing complex native dependencies from scripts can be fragile and does not provide the clean, repeatable runtime boundary that a container image provides. Running training on EMR or serving from a notebook is also an anti-pattern for this requirement because it avoids the SageMaker managed endpoint model rather than using the right SageMaker deployment abstraction.
    
    For more information, see the SageMaker AI guidance on choosing between built-in algorithms, framework implementations, and custom Docker images [https://docs.aws.amazon.com/sagemaker/latest/dg/algorithms-choose.html] and the documentation for pre-built containers for algorithms and frameworks [https://docs.aws.amazon.com/sagemaker/latest/dg/docker-containers-prebuilt.html].

---

### Question 33

**Category:** Content Domain 1: Data Preparation for ML and AI  
**Status:** ✅ **Correct**

A regional food delivery marketplace's ML team is preparing a training dataset for a promotion eligibility model. One value of a categorical facet appears much more often than the other values. Initial checks show that the target label proportions are similar across the facet values. The team wants to decide whether a balancing transformation is needed by using a managed visual preparation workflow with minimal custom code.

Which action should the ML engineer take?

* **A)** Generate a SageMaker Data Wrangler bias report and review DPL for the facet.
* **B)** Create an Athena query over Feature Store and compare average labels for the facet.
* **C)** Generate a SageMaker Data Wrangler bias report and review Class Imbalance for the facet.
* **D)** Run QuickSight anomaly detection and inspect top contributors for the facet.

??? note "Click to reveal Answer & Explanation"
    **Correct Answer:** **C**

    #### Correct Option Analysis
    * **C is Correct:** This action matches the stated issue because Class Imbalance measures whether one facet value is overrepresented or underrepresented compared with another. SageMaker Data Wrangler provides managed data preparation and analysis capabilities, which reduces the need to write custom metric code before choosing a balancing transform.

    #### Distractor Analysis
    * **A is Incorrect:** Difference in Proportions of Labels is useful when positive or negative outcome rates differ across facet values. The target label proportions are already similar, so this metric does not directly measure the representation imbalance described in the dataset.
    * **B is Incorrect:** Athena can query data that is cataloged or stored for analysis, and SageMaker Feature Store can expose offline data through S3 and the Glue Data Catalog. However, this action focuses on label averages rather than a managed pre-training bias check for representation imbalance, and it assumes a Feature Store workflow that is not required.
    * **D is Incorrect:** QuickSight anomaly detection is intended for finding unusual changes in business metrics and contributors in dashboards. It is not the appropriate managed data preparation workflow for measuring pre-training class representation across facet values.

    #### Overall Explanation
    When the problem is that one facet value has many more records than another, the relevant pre-training bias concept is Class Imbalance. This metric focuses on representation in the dataset, not on whether the model target has different positive or negative outcome rates across groups.
    
    Difference in Proportions of Labels answers a different question: whether label outcomes differ between facet values. In this scenario, the label proportions are similar, so DPL would not be the best first check for deciding whether to rebalance the training data.
    
    SageMaker Data Wrangler is designed for visual data preparation and analysis, including generating reports that help inspect data quality and bias before model training. After confirming a representation imbalance, the team can choose an appropriate training-only balancing technique while keeping evaluation data representative of production.
    
    For more information, see Analyze and visualize data in Amazon SageMaker Data Wrangler [https://docs.aws.amazon.com/sagemaker/latest/dg/data-wrangler-analyses.html] and the SageMaker guide to Measure pretraining bias [https://docs.aws.amazon.com/sagemaker/latest/dg/clarify-measure-data-bias.html].

---

### Question 34

**Category:** Content Domain 4: Operating, Monitoring, and Securing ML and  
**Status:** ✅ **Correct**

An electric utility's customer operations team uses an Amazon Bedrock generative AI assistant to summarize outage reports and draft customer notifications. Most requests involve short, standardized outage updates, but some requests require detailed reasoning about unusual restoration plans. The team currently sends every request to its highest-capability FM. Latency must remain suitable for an interactive application, and the team wants to reduce inference spend without changing the user workflow.

Which solution will meet these requirements MOST cost-effectively?

* **A)** Move Amazon Bedrock invocations to batch processing and return generated notifications after each scheduled batch job finishes.
* **B)** Enable Amazon Bedrock prompt caching for all assistant requests and continue using the strongest FM for every request.
* **C)** Purchase Amazon Bedrock Provisioned Throughput for the strongest FM and continue sending every assistant request to that FM.
* **D)** Use Amazon Bedrock intelligent prompt routing to send routine prompts to a lower-cost FM and complex prompts to a stronger FM.

??? note "Click to reveal Answer & Explanation"
    **Correct Answer:** **D**

    #### Correct Option Analysis
    * **D is Correct:** This option is correct because it matches model capability to request complexity instead of using the most expensive model for every request. The assistant can preserve quality for difficult cases while reducing spend on routine prompts that do not need the strongest FM.

    #### Distractor Analysis
    * **A is Incorrect:** Batch processing can reduce cost for non-interactive workloads that can wait for asynchronous completion. This assistant must remain suitable for interactive use, so scheduled batch completion does not meet the latency requirement.
    * **B is Incorrect:** Prompt caching can help when requests reuse the same prompt prefix and the selected model and API support caching. However, continuing to use the strongest FM for all routine and complex requests misses the larger cost optimization opportunity in this scenario.
    * **C is Incorrect:** Provisioned Throughput can be appropriate for steady, high-volume workloads that need consistent performance. However, continuing to use the strongest FM for every request does not reduce unnecessary model usage for routine prompts.

    #### Overall Explanation
    For FM applications, a practical cost-control pattern is to avoid treating every prompt as if it needs the most capable model. Intelligent prompt routing, also called tiered model usage, sends simpler requests to a lower-cost model and reserves a stronger model for prompts that require more reasoning or higher quality. This works well when the workload has a mix of routine and difficult requests, because the application can reduce average token cost without forcing users into a different workflow.
    
    Provisioned Throughput changes the capacity and performance economics for a selected model, but it does not by itself reduce waste if every request still goes to the largest model. Batch processing is useful when latency is not important, but an interactive assistant usually needs near-real-time responses. Prompt caching can be a useful complementary optimization for repeated prompt prefixes, but it is not a substitute for choosing an appropriately sized model for each request.
    
    Amazon Bedrock provides intelligent prompt routing for optimizing quality and cost among models, as described in Amazon Bedrock intelligent prompt routing [https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-routing.html]. For broader cost and capacity tradeoffs, see Amazon Bedrock capacity and performance options [https://docs.aws.amazon.com/bedrock/latest/userguide/capacity-limits-cost-optimization.html].

---

### Question 35

**Category:** Content Domain 1: Data Preparation for ML and AI  
**Status:** ❌ **Incorrect**

An insurance claims analytics team stores monthly Parquet claim extracts in an Amazon S3 data lake. The team does not need to transform the files immediately, but must discover schema changes, keep table metadata available for Athena queries, and run repeatable checks for completeness and valid value ranges before ML jobs consume the data.

Which TWO actions should the team take?

* **A)** Configure an AWS Glue crawler to update the Glue Data Catalog table and partitions for the S3 prefix.
* **B)** Create an AWS Glue Data Quality ruleset for the catalog table, and run it after each delivery.
* **C)** Use Amazon Data Firehose to convert the files to Parquet, and treat failed delivery records as quality results.
* **D)** Create an Amazon QuickSight dataset from the S3 files, and rely on data preparation steps for validation.
* **E)** Store the claims files on HDFS in an Amazon EMR cluster, and validate them before terminating the cluster.

??? note "Click to reveal Answer & Explanation"
    **Correct Answer:** **A, B**

    #### Correct Option Analysis
    * **A is Correct:** This action discovers schemas and updates table and partition metadata for data stored in Amazon S3. Athena can use the Glue Data Catalog as the metadata store, so this action supports queryable data discovery without moving the source files.
    * **B is Correct:** This action applies reusable validation rules to the dataset that is represented in the Glue Data Catalog. Completeness and valid range checks are typical data quality gates before downstream analytics or ML training jobs use a newly delivered dataset.

    #### Distractor Analysis
    * **C is Incorrect:** Amazon Data Firehose is designed for managed delivery of streaming data to destinations such as Amazon S3, Amazon Redshift, and Amazon OpenSearch Service. It can perform format conversion and Lambda transformations, but failed delivery handling is not a substitute for validating existing batch datasets against quality rules.
    * **D is Incorrect:** QuickSight data preparation can perform limited changes such as renaming fields, changing data types, and adding calculated fields. It is not the best fit for maintaining shared data lake metadata and enforcing repeatable data quality rules before ML jobs run.
    * **E is Incorrect:** HDFS on Amazon EMR is useful for distributed processing and intermediate data, but the storage is tied to the lifecycle of the cluster. This action adds unnecessary cluster management and does not maintain Athena-accessible table metadata for the S3 data lake.

    #### Overall Explanation
    For data lake validation, separate the metadata discovery concern from the data quality concern. An AWS Glue crawler can discover the layout and schema of files in Amazon S3 and update the Glue Data Catalog, which gives Athena and other analytics tools a shared view of the dataset. AWS Glue Data Quality can then apply rulesets to the cataloged table so the team can check conditions such as completeness and acceptable ranges before ML jobs depend on the data.
    
    This design avoids converting a validation problem into an unnecessary ETL or cluster-management problem. QuickSight is useful for dashboards and light preparation, but it is not the control point for repeatable ML data quality gates. EMR and HDFS can process large data, but HDFS is not the durable metadata layer for an S3 data lake. Amazon Data Firehose is valuable for streaming ingestion and delivery, not for validating monthly batch extracts that already exist in S3.
    
    For more information, see AWS Glue Data Quality overview [https://docs.aws.amazon.com/glue/latest/dg/glue-data-quality.html] and Getting started with AWS Glue Data Quality [https://docs.aws.amazon.com/glue/latest/dg/data-quality-getting-started.html].

---

### Question 36

**Category:** Content Domain 2: ML Model and Foundation Model (FM) Develop  
**Status:** ✅ **Correct**

A maritime logistics platform's AI engineering team uses a large general-purpose foundation model to classify support emails into routing categories and extract shipment identifiers. The team has a stable set of approved labeled examples for the task. Prompt engineering with the large model meets the accuracy target, but inference latency and token cost are too high for peak traffic. The team wants to preserve task quality while reducing ongoing inference cost.

Which fine-tuning strategy should the team use?

* **A)** Continue pre-training the current large FM on the email archive. Compare routing accuracy and token cost with the current prompt.
* **B)** Use a knowledge base to retrieve similar past emails at inference. Compare routing accuracy and token cost with the current prompt.
* **C)** Fine-tune a smaller supported FM on the labeled email examples. Compare quality and token cost with the current large FM.
* **D)** Add more few-shot examples to the current large FM prompt. Compare routing accuracy and token cost with the shorter prompt.

??? note "Click to reveal Answer & Explanation"
    **Correct Answer:** **C**

    #### Correct Option Analysis
    * **C is Correct:** This option is correct because the task is narrow, stable, and backed by labeled examples. A smaller model that is fine-tuned for the specific routing and extraction task can often meet the accuracy requirement with lower latency and token cost than a larger general-purpose model.

    #### Distractor Analysis
    * **A is Incorrect:** This option is incorrect because continued pre-training is better suited to adapting a model to broad domain language, especially when using unlabeled text. It does not directly optimize the model for the labeled classification and extraction behavior, and it keeps the same large model cost profile.
    * **B is Incorrect:** This option is incorrect because retrieval is most useful when the model needs external or frequently changing knowledge. For a stable supervised routing and extraction task, retrieval can add context tokens and operational complexity without directly reducing model size or inference cost.
    * **D is Incorrect:** This option is incorrect because adding examples to the prompt can improve behavior, but it increases input tokens for every request. The scenario already states that prompt engineering meets accuracy, so increasing prompt length works against the cost and latency objective.

    #### Overall Explanation
    When a workload is narrow, stable, and has approved labeled examples, fine-tuning a smaller supported FM is a practical way to trade broad general capability for task-specific efficiency. The smaller model does not need to solve every possible language task; it needs to reliably classify emails and extract fields that follow known patterns.
    
    This is different from continued pre-training, which teaches a model more about a domain's language distribution but does not necessarily teach the exact desired input-output behavior. It is also different from adding more few-shot prompt examples, which may improve accuracy but increases input tokens on every call. Retrieval augmented generation is valuable when answers depend on changing external content, but it is not the main lever for reducing cost on a stable labeled classification task.
    
    The team should still measure the tradeoff instead of assuming the smallest model is good enough. Amazon Bedrock supports model customization for selected models and use cases, and Amazon Bedrock model evaluation can compare candidate models on workload-specific prompts and metrics. For more information, see Customize your model to improve its performance for your use case [https://docs.aws.amazon.com/bedrock/latest/userguide/model-customization.html] and Evaluate model performance using Amazon Bedrock [https://docs.aws.amazon.com/bedrock/latest/userguide/model-evaluation.html].

---

### Question 37

**Category:** Content Domain 4: Operating, Monitoring, and Securing ML and  
**Status:** ✅ **Correct**

A smart-grid utility's ML engineering team runs a containerized inference API on Amazon ECS. Each request validates meter readings, invokes an Amazon SageMaker AI endpoint, writes the prediction to Amazon DynamoDB, and publishes a follow-up message to Amazon SQS. Amazon CloudWatch shows intermittent high latency, but aggregate endpoint metrics do not show whether the delay occurs before inference, during inference, or after inference. The team needs request-level visibility across the downstream calls with minimal code changes.

Which solution will meet these requirements?

* **A)** Create an AWS CloudTrail trail for SageMaker AI, DynamoDB, and Amazon SQS management events, and review the audit records for failed API calls.
* **B)** Configure AWS Config rules for the ECS service, SageMaker AI endpoint, DynamoDB table, and SQS queue, and review configuration timelines.
* **C)** Instrument the inference API with the AWS X-Ray SDK, enable an X-Ray daemon or service integration, and grant the task role permission to send traces.
* **D)** Build an Amazon CloudWatch dashboard for ECS CPU, endpoint latency, DynamoDB capacity, and SQS queue depth, and inspect correlated metrics.

??? note "Click to reveal Answer & Explanation"
    **Correct Answer:** **C**

    #### Correct Option Analysis
    * **C is Correct:** This option is correct because X-Ray traces a request as it moves through supported AWS service calls, HTTP requests, database calls, and queue calls. The SDK requires only limited application changes, and the workload needs permission to publish trace data.

    #### Distractor Analysis
    * **A is Incorrect:** CloudTrail is used to record API activity for auditing, especially management actions such as configuration changes. It is not designed to show the timing of each downstream call within a single inference request path.
    * **B is Incorrect:** AWS Config records resource configurations and configuration changes over time. It can help with compliance and change tracking, but it does not provide per-request latency tracing across application dependencies.
    * **D is Incorrect:** CloudWatch metrics are useful for monitoring infrastructure health and service-level trends. Aggregate metrics can show that latency or errors increased, but they do not identify the exact downstream segment that delayed an individual request.

    #### Overall Explanation
    When an inference workflow spans an application container, a model endpoint, a database, and a queue, aggregate metrics alone often show that latency increased but not where the request spent time. AWS X-Ray is designed for distributed tracing: the application SDK can capture supported AWS service calls, HTTP or HTTPS requests, database calls, and queue calls, then send trace segments through the X-Ray daemon or an AWS service integration.
    
    CloudWatch still matters for operational monitoring because it provides metrics, logs, dashboards, and alarms for SageMaker AI endpoints and related jobs. For example, SageMaker AI workloads can publish logs that help debug component-level behavior, as described in CloudWatch Logs for SageMaker AI [https://docs.aws.amazon.com/sagemaker/latest/dg/logging-cloudwatch.html]. The tradeoff is that CloudWatch metrics and logs usually describe a component or event stream, while tracing links the components together for a single request path. CloudTrail and AWS Config are valuable for audit and configuration history, but they are not request-tracing tools and would not isolate whether the latency occurred before, during, or after model inference.

---

### Question 38

**Category:** Content Domain 4: Operating, Monitoring, and Securing ML and  
**Status:** ✅ **Correct**

A regional video moderation platform runs a neural network on an Amazon SageMaker AI real-time endpoint. The endpoint uses GPU instances to classify uploaded clips as part of an interactive review workflow. Recent load tests show that the endpoint meets the latency target, but GPU utilization remains low and cost per inference is higher than the team's budget. The model is used only for inference, and the team wants to choose an instance family to evaluate first for better price performance.

Which action should the ML engineer take?

* **A)** Move the endpoint to larger general purpose CPU instances before changing production traffic.
* **B)** Evaluate AWS Inferentia based instances for the endpoint before changing production traffic.
* **C)** Move the endpoint to memory optimized CPU instances before changing production traffic.
* **D)** Evaluate AWS Trainium based instances for the endpoint before changing production traffic.

??? note "Click to reveal Answer & Explanation"
    **Correct Answer:** **B**

    #### Correct Option Analysis
    * **B is Correct:** AWS Inferentia is designed to deliver ML inference at high performance and low cost. Because the workload is inference only and the current GPU instances are underutilized, evaluating an inference-optimized instance family is the best first action.

    #### Distractor Analysis
    * **A is Incorrect:** Larger general purpose CPU instances could reduce accelerator spending, but they do not directly address high-throughput neural network inference. This approach might also miss the latency target if the model benefits from accelerated inference hardware.
    * **C is Incorrect:** Memory optimized CPU instances are useful when memory capacity or memory bandwidth is the limiting factor. The scenario describes low accelerator utilization and high cost per inference, not memory pressure, so this choice is not the best starting point.
    * **D is Incorrect:** AWS Trainium is designed for deep learning training workloads, especially very large models. The endpoint in this scenario does not train models, so choosing a training-optimized family is not the best fit for inference cost optimization.

    #### Overall Explanation
    For SageMaker AI real-time inference, instance family selection should match the dominant workload and the measured bottleneck. AWS Inferentia is built for inference at high throughput and lower cost, while AWS Trainium is built for training deep learning models. When an endpoint serves only predictions and GPU capacity is underutilized, an inference-optimized accelerator family is a sensible family to benchmark before shifting production traffic.
    
    The important operating principle is to avoid changing capacity based only on labels such as CPU, GPU, or accelerator. Measure latency, throughput, utilization, and cost per inference, then choose the smallest configuration that satisfies the workload. SageMaker AI guidance covers inference deployment choices and instance optimization in Deploy models for inference [https://docs.aws.amazon.com/sagemaker/latest/dg/deploy-model-options.html] and Optimize inference costs [https://docs.aws.amazon.com/sagemaker/latest/dg/inference-cost-optimization.html].
    
    The other choices do not fit the stated inference profile as well. Trainium aligns with training, not a production inference endpoint. General purpose and memory optimized CPU families can be valid for some models, but they are weaker first choices when the goal is better price performance for an accelerated neural network inference workload. The EC2 instance family naming model is summarized in Amazon EC2 instance type names [https://docs.aws.amazon.com/ec2/latest/instancetypes/instance-type-names.html].

---

### Question 39

**Category:** Content Domain 1: Data Preparation for ML and AI  
**Status:** ✅ **Correct**

A wildlife conservation research group is preparing a multimodal dataset for a model that classifies animal rescue cases. Each record includes numeric sensor readings, ranger notes, and camera-trap images. The records include a community-stewardship facet that the group wants to audit for bias and a multiclass triage label such as observe, treat, relocate, or release. Before training, an ML engineer must compare the full triage-label distribution between facet values for each modality-specific slice. The engineer needs a metric that captures the overall absolute difference across all label categories, not only representation counts or the rate of one label.

Which approach will meet these requirements?

* **A)** Calculate Total Variation Distance across triage-label distributions for each audited facet and modality slice, then rebalance or add meaning-preserving examples where divergence is high.
* **B)** Calculate Class Imbalance across record counts for each audited facet and modality slice, then oversample smaller facet groups without comparing category-level outcomes.
* **C)** Calculate BERTScore between ranger notes and reference summaries for each audited facet and modality slice, then rewrite low-scoring notes and reuse the score for image assets.
* **D)** Calculate Difference in Proportions of Labels for each audited facet and modality slice, then rebalance the favorable class while leaving other categories unchanged.

??? note "Click to reveal Answer & Explanation"
    **Correct Answer:** **A**

    #### Correct Option Analysis
    * **A is Correct:** Total Variation Distance is half the L1-norm difference between outcome distributions for facet values. It sums the absolute differences across label categories and applies the 1/2 factor, so it can compare multiclass distributions across numeric, text, and image slices.

    #### Distractor Analysis
    * **B is Incorrect:** Class Imbalance identifies whether one facet value has fewer or more records than another. Equalizing record counts alone can miss biased triage outcomes, because two facet groups can have similar sample sizes but very different label distributions.
    * **C is Incorrect:** BERTScore evaluates semantic similarity between generated text and reference text by using contextual embeddings. It is not a pre-training bias metric for comparing numeric, text, and image label distributions, and rewriting notes can compromise training-data integrity.
    * **D is Incorrect:** Difference in Proportions of Labels focuses on imbalance in positive outcomes between facet values. That approach can be useful for a favorable versus unfavorable label comparison, but it does not measure the full multiclass label distribution requested here.

    #### Overall Explanation
    For this scenario, the important distinction is between representation bias and outcome distribution bias. Class Imbalance tells you whether facet values are overrepresented or underrepresented in the dataset, but it does not tell you whether the labels attached to those examples are distributed differently. Difference in Proportions of Labels is narrower because it focuses on differences in positive outcome rates, which is not enough when the target has several meaningful categories.
    
    Total Variation Distance is appropriate when the engineer needs an aggregate absolute difference between categorical outcome distributions. In a multimodal preparation workflow, the same metric should be applied consistently to modality-specific slices, such as records dominated by numeric measurements, text notes, or image evidence. If a high divergence is found, the safer remediation is to add valid samples, rebalance, or use domain-preserving augmentation rather than changing the intended meaning of existing records. AWS documents these pre-training bias metrics in the SageMaker bias measurement guidance, including how different metrics answer different fairness questions: Measure pretraining bias [https://docs.aws.amazon.com/sagemaker/latest/dg/clarify-measure-data-bias.html].

---

### Question 40

**Category:** Content Domain 3: Deployment and Orchestration of ML and AI  
**Status:** ✅ **Correct**

A precision agriculture software team's ML engineers trained a TensorFlow image classifier in Amazon SageMaker AI. The model uses common TensorFlow operations and does not require extra operating system packages or a custom serving protocol. The team needs to deploy the model to a SageMaker AI real-time endpoint through a repeatable release process while minimizing container maintenance.

Which action should the team take?

* **A)** Use a SageMaker AI pre-built TensorFlow inference image and package the model artifacts with an entry script.
* **B)** Deploy the model on a SageMaker AI multi-container endpoint with separate TensorFlow and routing containers.
* **C)** Import the TensorFlow model into Amazon Bedrock Custom Model Import and invoke it through Bedrock APIs.
* **D)** Build an Ubuntu-based Docker image with TensorFlow and a custom web server, then publish the image to Amazon ECR.

??? note "Click to reveal Answer & Explanation"
    **Correct Answer:** **A**

    #### Correct Option Analysis
    * **A is Correct:** This approach uses a managed framework container that already includes the common TensorFlow serving and SageMaker integration components. The team can keep the release process repeatable by versioning the model artifacts and deployment configuration without maintaining a custom base image.

    #### Distractor Analysis
    * **B is Incorrect:** A multi-container endpoint is useful when a deployment needs multiple containers, such as different frameworks or separate components. The scenario describes one standard TensorFlow model, so adding multiple containers increases complexity without addressing a stated need.
    * **C is Incorrect:** Amazon Bedrock Custom Model Import is intended for supported custom foundation model use cases in Bedrock. The workload is a TensorFlow image classifier that needs a SageMaker AI real-time endpoint, so this does not match the deployment target.
    * **D is Incorrect:** Building a full custom container can work when a workload needs custom dependencies or a custom serving stack. In this scenario, that approach adds unnecessary build, patching, and runtime maintenance for a standard TensorFlow workload.

    #### Overall Explanation
    For containerized ML workloads on SageMaker AI, the practical decision is usually whether to use a pre-built framework image, extend an existing image, or build a fully custom image. When a model uses a common framework and does not need nonstandard libraries or a custom serving protocol, a pre-built framework inference image reduces operational overhead because AWS maintains the framework container integration and expected runtime behavior.
    
    Extending or building a custom image is valuable when the workload needs extra native dependencies, specialized preprocessing inside the container, or a serving stack that the pre-built image does not provide. Starting from a generic operating system image and writing the server layer is an anti-pattern for a routine TensorFlow deployment because it shifts security patching, dependency compatibility, and serving behavior onto the ML team without a clear benefit. Multi-container endpoints solve a different problem, isolating multiple containers behind one endpoint, and Bedrock Custom Model Import is not the normal path for hosting a standard TensorFlow classifier on a SageMaker AI real-time endpoint. For more information, see SageMaker AI container overview and decision guidance [https://docs.aws.amazon.com/sagemaker/latest/dg/docker-containers.html] and SageMaker AI pre-built Docker images [https://docs.aws.amazon.com/sagemaker/latest/dg/docker-containers-prebuilt.html].

---

### Question 41

**Category:** Content Domain 2: ML Model and Foundation Model (FM) Develop  
**Status:** ✅ **Correct**

A pharmaceutical safety team is evaluating a generative AI application that drafts adverse event summaries from case notes. The team has reference summaries written by subject matter experts. Valid model outputs often use different wording from the references, but the evaluation should reward outputs that preserve the same meaning.

Which evaluation approach will best meet these requirements?

* **A)** Evaluate generated responses with exact-match scoring against the SME reference responses.
* **B)** Evaluate generated responses with ROUGE-2 against the SME reference responses.
* **C)** Evaluate generated responses with ROUGE-L against the SME reference responses.
* **D)** Evaluate generated responses with BERTScore against the SME reference responses.

??? note "Click to reveal Answer & Explanation"
    **Correct Answer:** **D**

    #### Correct Option Analysis
    * **D is Correct:** BERTScore compares generated text with reference text by using contextual embeddings and semantic similarity. This approach is less sensitive to synonyms and paraphrasing than metrics that rely on exact word overlap.

    #### Distractor Analysis
    * **A is Incorrect:** Exact-match scoring requires the generated response to match the reference text precisely. This is too strict for natural language generation tasks where multiple semantically valid summaries can use different wording.
    * **B is Incorrect:** ROUGE-2 measures overlap of bigrams between generated text and reference text. This can be useful for some summarization checks, but it can penalize acceptable paraphrases that do not share the same two-word sequences.
    * **C is Incorrect:** ROUGE-L uses the longest common subsequence to evaluate overlap and ordering between generated and reference text. It is still based on shared lexical sequences, so it is not the best fit when preserving meaning with different wording is the main goal.

    #### Overall Explanation
    For content quality validation in generative AI, the metric should match the evaluation goal. BERTScore is designed to compare a candidate response with a reference response by using contextual embeddings, so it can capture semantic similarity even when the wording differs. That makes it a better choice when SMEs care about whether the generated summary preserves the intended meaning rather than whether it repeats the same words.
    
    ROUGE metrics are useful and interpretable for many summarization tasks, but they are based on overlapping units such as words, n-grams, or subsequences. ROUGE-2 focuses on bigram overlap, and ROUGE-L focuses on the longest common subsequence. These metrics can under-score a valid paraphrase because the surface text differs from the reference.
    
    Amazon Bedrock model evaluation supports evaluating model behavior with prompt datasets and quality-related metrics, and it can be used as part of a broader evaluation workflow for foundation model applications. For more information, see Overview of Amazon Bedrock evaluations [https://docs.aws.amazon.com/bedrock/latest/userguide/evaluation.html] and Model evaluation metrics [https://docs.aws.amazon.com/bedrock/latest/userguide/model-evaluation-metrics.html].

---

### Question 42

**Category:** Content Domain 3: Deployment and Orchestration of ML and AI  
**Status:** ✅ **Correct**

A freight railroad's operations automation team is building a generative AI assistant for dispatchers. The assistant must answer questions from internal operating manuals and must also submit a dispatch-review request by using an existing AWS Lambda function when a dispatcher asks for an exception review. The assistant should choose whether to retrieve manual content, call the function, or ask for missing request details, with the least custom orchestration code.

Which solution will meet these requirements?

* **A)** Query a vector store from a custom Lambda function, append matching passages to the prompt, and route every request through that function.
* **B)** Build the assistant with Amazon Bedrock AgentCore, expose the Lambda function as a Gateway tool, and connect the knowledge base for retrieval.
* **C)** Call RetrieveAndGenerate from the application, then invoke the Lambda function for every dispatcher request after the generated response is returned.
* **D)** Store the manuals as Bedrock prompt versions, add dispatch-field variables, and invoke the model with the latest approved prompt version.

??? note "Click to reveal Answer & Explanation"
    **Correct Answer:** **B**

    #### Correct Option Analysis
    * **B is Correct:** This option is correct because Amazon Bedrock AgentCore can expose tools to an agent through AgentCore Gateway and can support retrieval from knowledge sources. Tool descriptions and parameter schemas help the foundation model decide when to call the tool and what details are required.

    #### Distractor Analysis
    * **A is Incorrect:** This option is incorrect because a custom retrieval function can implement RAG, but it requires the team to build more orchestration logic. The requirement asks for the least custom orchestration code while also supporting retrieval, tool invocation, and missing-parameter handling.
    * **C is Incorrect:** This option is incorrect because RetrieveAndGenerate supports retrieval-augmented responses, but it does not by itself orchestrate conditional tool use. Invoking the Lambda function for every request would add unnecessary actions and would not handle missing request details appropriately.
    * **D is Incorrect:** This option is incorrect because Prompt Management is useful for reusable and versioned prompts, including prompts with variables. It is not a retrieval pipeline for keeping a searchable document corpus available to the model.

    #### Overall Explanation
    Amazon Bedrock Knowledge Bases provide managed retrieval-augmented generation for use cases such as answering questions from internal manuals, runbooks, or policy documents. The knowledge base handles the retrieval side of the pipeline by using indexed document content to provide relevant context to the foundation model.
    
    When the workflow must also perform actions, such as calling an existing Lambda function, Amazon Bedrock AgentCore is the appropriate current pattern for new agent development. AgentCore can expose tools through AgentCore Gateway and use tool descriptions and schemas so the model can decide whether to retrieve context, invoke a tool, or ask the user for missing information. This matches the operational need without forcing the application team to write all routing logic itself.
    
    RetrieveAndGenerate is appropriate when an application needs a direct RAG response, but it is not a complete tool-orchestration pattern. Prompt versions help standardize reusable prompts, and a custom vector-search Lambda can work, but those approaches either omit retrieval management or increase custom orchestration effort. For more information, see Overview of Amazon Bedrock Knowledge Bases [https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base.html] and Retrieve from knowledge bases [https://docs.aws.amazon.com/bedrock/latest/userguide/kb-how-retrieval.html].

---

### Question 43

**Category:** Content Domain 4: Operating, Monitoring, and Securing ML and  
**Status:** ✅ **Correct**

A clinical documentation vendor's AI platform team uses Amazon Bedrock to generate draft visit summaries. Engineers are testing several prompt templates that vary in system instructions, conversation history, and retrieved context length. The team wants to estimate the input-token cost impact before sending every candidate prompt to a foundation model. After deployment, the team also wants to compare actual token usage patterns in production.

Which solution will BEST meet these requirements?

* **A)** Configure Amazon Bedrock Provisioned Throughput for every evaluated FM, apply Model Unit pricing, and track total spend in Cost Explorer.
* **B)** Invoke each candidate prompt against the largest FM, apply average request latency, and track infrastructure metrics in Amazon CloudWatch.
* **C)** Use the Amazon Bedrock CountTokens API on candidate prompts, apply model token rates, and track token metrics in Amazon CloudWatch.
* **D)** Deploy the prompt tests to Amazon SageMaker Serverless Inference, apply instance-hour pricing, and track API changes in AWS CloudTrail.

??? note "Click to reveal Answer & Explanation"
    **Correct Answer:** **C**

    #### Correct Option Analysis
    * **C is Correct:** This approach estimates token usage for candidate requests without performing full inference, which helps avoid unnecessary model calls during prompt testing. CloudWatch token metrics can then help the team compare actual production usage patterns after deployment.

    #### Distractor Analysis
    * **A is Incorrect:** Provisioned Throughput can be useful for steady high-volume workloads or required cases such as some customized model usage, but it is not the best way to estimate prompt token impact during testing. It adds fixed capacity cost and does not avoid unnecessary evaluations of candidate prompts.
    * **B is Incorrect:** Running full inference for every prompt candidate increases the cost that the team is trying to estimate and control. Latency and infrastructure metrics can help with performance monitoring, but they do not directly estimate token-based FM inference cost.
    * **D is Incorrect:** SageMaker Serverless Inference is a hosting option for SageMaker models, not a way to estimate Amazon Bedrock prompt token usage. CloudTrail records API activity for auditing, but it is not the primary tool for comparing token consumption or estimating FM inference charges.

    #### Overall Explanation
    For many foundation models, production inference cost is driven heavily by input and output tokens. Prompt text, conversation history, retrieved context, and response length all affect cost, so prompt changes should be evaluated as cost changes, not only quality changes. The Amazon Bedrock CountTokens API is useful because it lets an engineer estimate the token count of a request before running inference, which reduces waste during prompt iteration.
    
    After deployment, the team still needs operational visibility because actual output length and user behavior can differ from test assumptions. CloudWatch token metrics and cost attribution reports help connect application behavior to spend, while the Bedrock pricing model explains why token volume and model choice matter. See the Amazon Bedrock pricing [https://aws.amazon.com/bedrock/pricing/] page and the Amazon Bedrock cost management best practices [https://docs.aws.amazon.com/bedrock/latest/userguide/cost-mgmt-best-practices.html] documentation for the relevant cost management context.

---

### Question 44

**Category:** Content Domain 1: Data Preparation for ML and AI  
**Status:** ✅ **Correct**

A wind farm operations team receives turbine telemetry as CSV records from field gateways. The team must transform each record to JSON, drop records that fail validation, and load the curated output into Amazon S3 within a few minutes for downstream feature engineering. The team does not need record replay or multiple custom consumers, and wants to minimize operational overhead.

Which solution will meet these requirements?

* **A)** Configure Kinesis Data Streams with an AWS Lambda consumer and custom code that writes curated records to Amazon S3.
* **B)** Schedule an AWS Glue batch ETL job that transforms raw S3 objects and writes curated records to another Amazon S3 prefix.
* **C)** Run an Amazon EMR Spark Streaming application that transforms the gateway records and writes curated records to Amazon S3.
* **D)** Configure Amazon Data Firehose with an AWS Lambda transformation and an Amazon S3 destination for curated records.

??? note "Click to reveal Answer & Explanation"
    **Correct Answer:** **D**

    #### Correct Option Analysis
    * **D is Correct:** Amazon Data Firehose is a fully managed service that can buffer streaming records, invoke Lambda for transformation, and deliver the results to Amazon S3. This approach supports simple streaming ETL such as CSV-to-JSON conversion and filtering without requiring the team to operate a stream-processing application.

    #### Distractor Analysis
    * **A is Incorrect:** Kinesis Data Streams is appropriate when applications need custom producers or consumers, replay, or multiple consumers. The scenario does not require those capabilities, so this approach adds unnecessary stream management and delivery logic compared with Data Firehose.
    * **B is Incorrect:** A scheduled batch job can transform data after the raw files have landed in S3, but it is not the most direct way to transform records in the streaming ingestion path. The requirement is to process incoming records within minutes while minimizing operational work, which fits a managed Firehose delivery stream with Lambda transformation better.
    * **C is Incorrect:** Spark Streaming can transform streaming data, but an EMR application introduces cluster or job operations that are not needed for this simple delivery pipeline. This option is better suited for more complex analytics or reusable Spark logic, not the lowest-overhead CSV-to-JSON stream delivery case.

    #### Overall Explanation
    Amazon Data Firehose is designed for managed, near-real-time ingestion into destinations such as Amazon S3, Amazon Redshift, Amazon OpenSearch Service, and HTTP endpoints. When the transformation is straightforward, such as converting CSV to JSON, enriching records, or filtering invalid records, Firehose can invoke an AWS Lambda function before delivering the records to the destination.
    
    The important tradeoff is capability versus operational overhead. Kinesis Data Streams gives more control, including replay and multiple consumers, but it also requires consumer-side processing and destination-writing logic. Spark Streaming on Amazon EMR or AWS Glue is useful for more complex streaming analytics and feature calculations, but it is more than the scenario requires for a simple buffered transform and load pipeline.
    
    For this use case, Firehose handles buffering, scaling, delivery, and integration with S3, while Lambda handles the record-level transformation. See Transform source data in Amazon Data Firehose [https://docs.aws.amazon.com/firehose/latest/dev/data-transformation.html] for how Firehose invokes Lambda during delivery, and Data transformation status model [https://docs.aws.amazon.com/firehose/latest/dev/data-transformation-status-model.html] for the expected transformation response structure.

---

### Question 45

**Category:** Content Domain 1: Data Preparation for ML and AI  
**Status:** ✅ **Correct**

A clinical genomics lab's ML engineering team stores de-identified sequencing metadata and fine-tuning JSONL files in Amazon S3. The security team requires encryption at rest, control over the encryption key policy, and an audit trail of key use. The data must remain in the S3 data lake for Athena exploration and SageMaker AI training.

Which storage configuration should the team use?

* **A)** Copy the dataset to an encrypted Amazon EFS file system and mount it from training jobs inside the VPC.
* **B)** Enable default bucket encryption on the S3 bucket with SSE-S3 and Amazon S3 managed keys.
* **C)** Transition the S3 objects to S3 Standard-IA with a lifecycle policy after ingestion.
* **D)** Enable default bucket encryption on the S3 bucket with SSE-KMS and a customer managed KMS key.

??? note "Click to reveal Answer & Explanation"
    **Correct Answer:** **D**

    #### Correct Option Analysis
    * **D is Correct:** This option encrypts objects at rest while allowing the team to control access through a customer managed KMS key policy. AWS KMS key usage can be audited, which supports the requirement for a key-use audit trail while keeping the data in Amazon S3.

    #### Distractor Analysis
    * **A is Incorrect:** This option moves the primary dataset out of the S3 data lake, which conflicts with the requirement to keep the data available in Amazon S3 for Athena and SageMaker AI workflows. Amazon EFS can be useful for shared file access, but it is not the best fit for retaining an S3-centered lake architecture.
    * **B is Incorrect:** This option encrypts objects at rest, but the keys are managed by Amazon S3 rather than controlled through a customer managed KMS key policy. It does not provide the same level of key policy control or KMS key-use auditing required by the security team.
    * **C is Incorrect:** This option can reduce storage cost for objects that are accessed less frequently, but it does not address customer control over encryption keys. A storage class transition is a cost and access-pattern decision, not a replacement for an encryption configuration.

    #### Overall Explanation
    For an S3 data lake that must satisfy encryption-at-rest and key governance requirements, SSE-KMS with a customer managed KMS key is the appropriate configuration. It keeps the data in Amazon S3 for services such as Athena and SageMaker AI, while using AWS KMS for key policy control and key-use auditing.
    
    SSE-S3 is still server-side encryption, but it uses keys managed by Amazon S3, so it does not provide the same customer-managed key policy control. Storage class changes such as S3 Standard-IA address cost optimization for infrequently accessed data, but they do not satisfy key governance requirements by themselves. Moving the data to a file system such as Amazon EFS changes the storage architecture and is unnecessary when the workload is centered on an S3 data lake.
    
    The broader decision pattern is to separate storage access pattern from compliance controls. Use S3 storage classes and lifecycle policies for cost and access-frequency tradeoffs, and use S3 encryption settings with AWS KMS when compliance requires customer-managed keys and auditability. For more information, see Using server-side encryption with Amazon S3 [https://docs.aws.amazon.com/AmazonS3/latest/userguide/UsingEncryption.html] and Choosing the right Amazon S3 storage class [https://docs.aws.amazon.com/AmazonS3/latest/userguide/storage-class-intro.html].

---

### Question 46

**Category:** Content Domain 1: Data Preparation for ML and AI  
**Status:** ✅ **Correct**

A media post-production studio's ML team trains a computer vision model in Amazon SageMaker AI on millions of small image files. The training job currently reads from Amazon S3 by using the default input behavior. As the team increases the number of training instances, GPU utilization remains low because workers spend too much time waiting on random file reads. The training code expects filesystem paths, and the team can use a storage source that requires VPC access.

Which solution will best address the storage scalability bottleneck?

* **A)** Increase the EBS volume size and continue using S3 File mode.
* **B)** Use Amazon FSx for Lustre as the SageMaker AI training data source.
* **C)** Stream the dataset by using Pipe mode from the existing S3 bucket.
* **D)** Move the dataset to Amazon EFS as the SageMaker AI training data source.

??? note "Click to reveal Answer & Explanation"
    **Correct Answer:** **B**

    #### Correct Option Analysis
    * **B is Correct:** Amazon FSx for Lustre is suited for high-throughput, low-latency training workloads that need filesystem-style access. SageMaker AI can use FSx for Lustre as a training data source, and the VPC requirement aligns with the stated constraint.

    #### Distractor Analysis
    * **A is Incorrect:** Increasing the attached volume can help when local training storage capacity is too small. The described problem is read throughput and random-access scaling across workers, not primarily a lack of local disk space.
    * **C is Incorrect:** Pipe mode streams data from Amazon S3 and can reduce local staging time for sequential access patterns. The workload requires random file reads through filesystem paths, so streaming from S3 does not match the access pattern as well.
    * **D is Incorrect:** Amazon EFS can be used with SageMaker AI training jobs when the data already resides in EFS and the job runs in a VPC. However, FSx for Lustre is the better fit for very high-throughput and high-IOPS ML training access patterns.

    #### Overall Explanation
    For large-scale training, the storage path can become the bottleneck even when compute capacity increases. Amazon FSx for Lustre is designed for high-performance file workloads and is commonly used when training jobs need low-latency, high-throughput access with filesystem semantics.
    
    The default S3 File mode copies data from Amazon S3 to local storage before training, which can be inefficient for very large datasets or many small files. Increasing EBS capacity addresses a different failure mode, local disk exhaustion, but it does not fundamentally change the read pattern or provide a shared high-performance file system.
    
    Amazon EFS is useful for shared file access, but for throughput-heavy ML training workloads, FSx for Lustre is the more appropriate SageMaker AI storage choice. Pipe mode and Fast File mode can improve S3-based access for some workloads, but streaming is a poor match when the training code depends on random file access through paths. See the SageMaker AI guidance on choosing training data input modes and storage sources [https://docs.aws.amazon.com/sagemaker/latest/dg/model-access-training-data-best-practices.html] and training storage behavior [https://docs.aws.amazon.com/sagemaker/latest/dg/model-train-storage-tips-considerations.html].

---

### Question 47

**Category:** Content Domain 3: Deployment and Orchestration of ML and AI  
**Status:** ✅ **Correct**

A travel insurance provider's AI engineering team fine-tunes a custom foundation model in Amazon Bedrock with newly reviewed claims conversations each month. The application also uses an Amazon Bedrock knowledge base for policy excerpts, but the policy documents are not changing during this retraining cycle. The team needs the CI/CD process to block poor retrained model versions before traffic moves to the new custom model. Because generated wording can vary between runs, the check must judge response quality for normal cases, edge cases, and key business scenarios rather than require identical text.

Which approach will meet these requirements?

* **A)** Run a fixed Bedrock Evaluations prompt set after each fine-tuning job, and promote the custom model only when quality thresholds pass.
* **B)** Run CountTokens on the evaluation prompts after each fine-tuning job, and promote the custom model only when estimated token use decreases.
* **C)** Run StartIngestionJob for the application knowledge base after each fine-tuning job, and promote the custom model only when ingestion completes.
* **D)** Run unit tests that compare every response with a stored answer string, and promote the custom model only when all strings match.

??? note "Click to reveal Answer & Explanation"
    **Correct Answer:** **A**

    #### Correct Option Analysis
    * **A is Correct:** This approach treats retraining as a versioned model change and adds a quality gate before promotion. A fixed evaluation dataset with threshold-based scoring is appropriate for generative outputs because valid responses can differ in wording while still meeting the required criteria.

    #### Distractor Analysis
    * **B is Incorrect:** Token counting is useful for estimating or controlling inference cost. It does not measure whether the retrained model gives accurate, safe, or business-appropriate responses for the required scenarios.
    * **C is Incorrect:** A knowledge base ingestion job refreshes the retrieval index when source documents change. The scenario requires judging the quality of a newly fine-tuned custom model, and the policy documents are not changing during this retraining cycle.
    * **D is Incorrect:** Exact string comparison is a brittle anti-pattern for generative AI regression testing. A retrained model can produce an acceptable answer with different wording, so this approach can reject good model versions or encourage overly rigid prompts.

    #### Overall Explanation
    Retraining a generative AI model should be treated as a controlled artifact change in the deployment process. The important mechanism is not to prove that the new model repeats old text exactly, but to verify that the new model meets measurable quality criteria on a stable set of prompts that represent routine cases, edge cases, and business-critical scenarios.
    
    Amazon Bedrock model customization supports creating custom models from training data, and those custom model versions should be evaluated before production promotion. See Custom models in Amazon Bedrock [https://docs.aws.amazon.com/bedrock/latest/userguide/custom-models.html] and Submit a model customization job [https://docs.aws.amazon.com/bedrock/latest/userguide/model-customization-submit.html]. In a CI/CD workflow, a threshold-based evaluation gate aligns with how foundation model responses behave, since semantically correct answers can vary in phrasing.
    
    Token counting is valuable for cost and prompt-size management, but it is not a substitute for quality evaluation. Knowledge base ingestion is the right mechanism when retrieval source documents are added, modified, or deleted, but it does not retrain the foundation model or validate the newly customized model. If the retraining process is orchestrated as a repeatable workflow, services such as SageMaker Pipelines can organize processing, training, evaluation, registration, and deployment steps as a DAG, as described in Define a pipeline [https://docs.aws.amazon.com/sagemaker/latest/dg/define-pipeline.html].

---

### Question 48

**Category:** Content Domain 3: Deployment and Orchestration of ML and AI  
**Status:** ✅ **Correct**

A university admissions office's automation team is building an Amazon Bedrock AgentCore assistant that helps applicants estimate financial aid. The assistant can call an AWS Lambda tool through AgentCore Gateway. The tool needs the applicant's program, residency status, and household size. Applicants often provide only some of these values in the first message. The team wants the assistant to gather the missing values during the same conversation, avoid calling the tool with incomplete input, and avoid retaining applicant details after the conversation ends.

Which solution will meet these requirements?

* **A)** Define required fields in the tool input schema, and prompt the agent to ask for missing values before invoking the aid-estimate tool.
* **B)** Index example aid forms in a Bedrock knowledge base, and retrieve similar completed forms before invoking the aid-estimate tool.
* **C)** Configure the Lambda function with default placeholder fields, and let users correct the estimate after the tool returns a result.
* **D)** Write each provided field to AgentCore Memory as long-term records, and retrieve the records before invoking the aid-estimate tool.

??? note "Click to reveal Answer & Explanation"
    **Correct Answer:** **A**

    #### Correct Option Analysis
    * **A is Correct:** This approach lets the agent recognize which tool parameters are required and gather missing values before the Lambda tool is called. The values can remain part of the active conversation context without being saved as durable memory after the interaction ends.

    #### Distractor Analysis
    * **B is Incorrect:** A knowledge base supports retrieval-augmented generation from external documents. It does not manage per-applicant tool parameters or ensure that required fields have been collected before a tool invocation.
    * **C is Incorrect:** Calling the tool with placeholder inputs is an anti-pattern because the result can be misleading and may trigger downstream actions with invalid state. The agent should collect the required values before invoking the tool instead of repairing an avoidable bad call.
    * **D is Incorrect:** AgentCore Memory is useful when an agent needs durable information across sessions or future interactions. The requirement is limited to the current conversation and explicitly avoids retaining applicant details after the conversation ends.

    #### Overall Explanation
    For an agent that calls tools, state management often starts with keeping track of the parameters required for the next action. The tool definition should describe the expected inputs, mark the necessary values as required, and give descriptions that help the model extract those values from the user's messages.
    
    When a required value is missing, the agent can use the conversation context to ask a follow-up question before calling the tool. This is different from using AgentCore Memory, which is intended for state that must persist beyond the current interaction, as described in Amazon Bedrock AgentCore Memory [https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/memory.html]. For transient conversation context, the runtime session model is a better fit because session context is isolated to the active interaction, as discussed in Amazon Bedrock AgentCore Runtime sessions [https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/runtime-sessions.html].
    
    A knowledge base is designed for retrieval from documents, not for validating that a specific user's tool arguments are complete. Supplying placeholder values is also unsafe because it moves an incomplete state into the tool layer and forces the application to recover after producing a potentially incorrect result.

---

### Question 49

**Category:** Content Domain 3: Deployment and Orchestration of ML and AI  
**Status:** ❌ **Incorrect**

A retail pharmacy chain's ML platform team deploys an image classification model on an Amazon SageMaker AI serverless endpoint. The workload has long idle periods, but customers expect low latency during store opening hours. The team enables provisioned concurrency for the endpoint and wants Application Auto Scaling to add and remove provisioned concurrency as traffic changes.

Which scaling signal should the team use?

* **A)** Configure target tracking based on CPU utilization of the serving compute.
* **B)** Configure target tracking based on concurrent requests per deployed model.
* **C)** Configure target tracking based on invocations per hosting instance for the endpoint.
* **D)** Configure target tracking based on utilization of the endpoint's provisioned concurrency.

??? note "Click to reveal Answer & Explanation"
    **Correct Answer:** **D**

    #### Correct Option Analysis
    * **D is Correct:** This scaling signal matches the capacity unit that the team wants Application Auto Scaling to adjust. It helps scale provisioned concurrency according to how much of the initialized serverless capacity is being used.

    #### Distractor Analysis
    * **A is Incorrect:** CPU utilization can be useful as a custom signal for some instance-based deployments. For serverless inference, the underlying compute is abstracted, so CPU utilization is not the right signal for provisioned concurrency usage. Your answer is incorrect
    * **B is Incorrect:** Concurrent request signals can be useful in some SageMaker AI hosting patterns. For autoscaling serverless provisioned concurrency, the scaling signal should represent use of provisioned concurrency.
    * **C is Incorrect:** This scaling signal fits an instance-based SageMaker AI endpoint model. A serverless endpoint does not expose capacity as a customer-managed fleet of hosting instances.

    #### Overall Explanation
    For SageMaker AI serverless inference, provisioned concurrency keeps serving capacity initialized so requests can avoid cold-start latency. When Application Auto Scaling changes that capacity, the scaling signal should describe how heavily the provisioned concurrency is being used.
    
    Instance-oriented signals, such as invocations per hosting instance or CPU utilization, use the wrong mental model for serverless hosting. The team is not scaling a visible fleet of endpoint instances; the team is scaling a serverless concurrency setting. Concurrent request signals can be useful in other SageMaker AI hosting configurations, but they are not the best fit when the operational goal is to adjust provisioned concurrency.
    
    See the SageMaker AI documentation for autoscaling provisioned concurrency on serverless endpoints [https://docs.aws.amazon.com/sagemaker/latest/dg/serverless-endpoints-autoscale.html] and the broader guidance on choosing scaling policy metrics [https://docs.aws.amazon.com/sagemaker/latest/dg/endpoint-auto-scaling-add-code-define.html].

---

### Question 50

**Category:** Content Domain 1: Data Preparation for ML and AI  
**Status:** ✅ **Correct**

A mortgage servicing firm's ML team is creating JSONL prompt-completion records from historical support emails to fine-tune a generative AI model. The emails include customer names, addresses, and account numbers in both prompts and completions. Security policy prohibits sensitive values from becoming part of the training dataset. The team will use separate runtime safeguards after deployment.

Which approach should the ML engineer use during data preparation?

* **A)** Remove duplicate and malformed JSONL records during curation and preserve sensitive values to improve domain fidelity.
* **B)** Preprocess the JSONL dataset to validate records and replace sensitive values with anonymized placeholders before fine-tuning.
* **C)** Encrypt the JSONL dataset in Amazon S3 with SSE-KMS and use the original prompt-completion text directly for fine-tuning.
* **D)** Configure Bedrock Guardrails for the deployed application and keep the original prompt-completion text in the fine-tuning dataset.

??? note "Click to reveal Answer & Explanation"
    **Correct Answer:** **B**

    #### Correct Option Analysis
    * **B is Correct:** This approach prevents sensitive values from being learned from the fine-tuning dataset. Data preparation should include format validation, prompt-completion quality checks, and screening or anonymization of sensitive content before training begins.

    #### Distractor Analysis
    * **A is Incorrect:** Removing malformed or duplicate records is a useful training-data integrity step, but the approach leaves prohibited sensitive values in the dataset. Domain fidelity does not justify training on values that policy requires the team to anonymize or redact.
    * **C is Incorrect:** SSE-KMS protects objects at rest in Amazon S3, but encryption does not remove sensitive values from the text that the training job reads. The model could still learn or reproduce sensitive content if the original records are used for fine-tuning.
    * **D is Incorrect:** Runtime guardrails help enforce policy during application requests and responses. Runtime safeguards do not clean the training dataset and do not prevent sensitive values from being included in fine-tuning records.

    #### Overall Explanation
    For fine-tuning and other supervised training workflows, sensitive content should be handled as part of training-data integrity, not only as a runtime policy problem. A good preparation pipeline validates required fields, checks that prompt-completion pairs are useful and consistent, removes bad records, and masks, redacts, or anonymizes sensitive values before the curated dataset is used for training.
    
    Encryption with AWS KMS is important for protecting data at rest, but encryption preserves the original plaintext for authorized processing. If a training job reads records that still contain account numbers or addresses, the model can learn from those values. Runtime controls such as Amazon Bedrock Guardrails are valuable for deployed applications, but evaluation and runtime safeguards do not replace cleaning the dataset before fine-tuning.
    
    A practical implementation can use preprocessing code or managed data preparation features that detect PII and apply masking or removal before outputting the curated dataset. For examples of AWS capabilities in this area, see Amazon Comprehend PII overview [https://docs.aws.amazon.com/comprehend/latest/dg/pii.html], AWS Glue Detect PII transform [https://docs.aws.amazon.com/glue/latest/dg/detect-PII.html], and Amazon Bedrock Guardrails sensitive information filters [https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-sensitive-filters.html].

---

### Question 51

**Category:** Content Domain 3: Deployment and Orchestration of ML and AI  
**Status:** ✅ **Correct**

An event-ticketing platform's ML engineering team hosts a fraud scoring model for checkout transactions. The checkout service must receive a prediction while the customer is waiting, and latency must remain low during busy onsale periods. Traffic volume changes throughout the day, but the model receives requests continuously enough that keeping inference capacity online is acceptable.

Which deployment target best meets these requirements?

* **A)** Deploy the model to SageMaker Serverless Inference, and accept cold starts after idle traffic periods.
* **B)** Run the model in recurring SageMaker Processing jobs, and have the app read prediction files from Amazon S3.
* **C)** Deploy the model to a SageMaker AI real-time endpoint, and enable endpoint autoscaling for traffic changes.
* **D)** Deploy the model to a SageMaker AI asynchronous endpoint, and have the app poll for completed outputs.

??? note "Click to reveal Answer & Explanation"
    **Correct Answer:** **C**

    #### Correct Option Analysis
    * **C is Correct:** A SageMaker AI real-time endpoint is intended for interactive inference when an application needs an immediate response. Endpoint autoscaling lets the hosted capacity adjust as request volume changes, while keeping the model available for online calls.

    #### Distractor Analysis
    * **A is Incorrect:** SageMaker Serverless Inference is useful when workloads have idle periods or uneven traffic and can tolerate cold starts. The checkout service needs consistently low latency while users are waiting, so cold-start behavior is a poor fit.
    * **B is Incorrect:** SageMaker Processing jobs are designed for managed data processing, feature engineering, and model evaluation workloads. Running recurring jobs and reading files from Amazon S3 would not provide immediate predictions for live checkout requests.
    * **D is Incorrect:** Asynchronous Inference queues requests and returns results later, which is useful for long-running processing when the caller can be notified or poll. The checkout flow needs the prediction before the transaction can continue, so a queued pattern does not meet the interactive requirement.

    #### Overall Explanation
    For an online application that must make a decision in the user's request path, a SageMaker AI real-time endpoint is the appropriate deployment target. Real-time endpoints keep inference infrastructure available so the application can invoke the model and receive a response synchronously.
    
    Autoscaling addresses the separate issue of variable demand by adjusting endpoint capacity as traffic changes. This trades some ongoing compute cost for lower and more predictable latency, which is usually the right tradeoff for checkout, fraud scoring, recommendations, and other interactive workloads.
    
    Serverless Inference is better when traffic is intermittent and occasional cold starts are acceptable. Asynchronous Inference is better when requests can be queued and completed later. SageMaker Processing is for managed processing and evaluation jobs, not for serving live predictions to a waiting application. For more deployment target guidance, see SageMaker AI inference deployment options [https://docs.aws.amazon.com/sagemaker/latest/dg/deploy-model-options.html].

---

### Question 52

**Category:** Content Domain 2: ML Model and Foundation Model (FM) Develop  
**Status:** ✅ **Correct**

A healthcare payer's member-services AI team is choosing an Amazon Bedrock foundation model for a GenAI application that summarizes appeal documents and drafts short explanations for reviewers. The team has a representative prompt dataset with SME-written expected answers. The selected model must meet minimum correctness, relevance, and safety thresholds while keeping inference cost reasonable. The team wants a repeatable selection process before promotion.

Which approach will best meet these requirements?

* **A)** Choose the FM with the lowest token price in Amazon Bedrock. Review several ad hoc prompts manually, and promote the model if the sample responses seem usable.
* **B)** Evaluate each candidate FM in Amazon Bedrock on the prompt dataset. Compare quality and safety scores with token usage, and choose the lowest-cost FM that meets the thresholds.
* **C)** Test each candidate FM by requiring exact string matches to the SME answers. Choose the highest pass rate, and reject paraphrased answers with different wording.
* **D)** Choose the largest available FM in the required AWS Region. Validate the choice after release by monitoring CloudWatch invocation counts, latency, and application errors.

??? note "Click to reveal Answer & Explanation"
    **Correct Answer:** **B**

    #### Correct Option Analysis
    * **B is Correct:** This approach is correct because it uses a representative evaluation dataset to measure whether each candidate model meets the application's quality and safety requirements. Comparing those scores with token usage supports a practical price-to-performance decision instead of assuming the largest or cheapest model is best.

    #### Distractor Analysis
    * **A is Incorrect:** Token price alone does not show whether the model can meet the required quality and safety thresholds. A small ad hoc review is not a repeatable evaluation process and might miss failures that appear in the representative prompt dataset.
    * **C is Incorrect:** Exact string matching is too brittle for generative AI outputs because valid answers can use different wording while preserving the same meaning. A better quality gate evaluates dimensions such as correctness, relevance, and safety against thresholds instead of requiring identical text.
    * **D is Incorrect:** Choosing the largest model is an anti-pattern when a smaller model can meet the task requirements at lower cost. CloudWatch operational metrics are useful in production, but invocation counts, latency, and errors do not prove correctness, relevance, or safety before promotion.

    #### Overall Explanation
    For FM selection, the useful mental model is price-to-performance, not simply model size or list price. Amazon Bedrock model evaluation workflows can test candidate models against prompts that reflect the real workload and can use automatic metrics, human evaluation, or LLM-as-a-judge methods to assess model behavior. See Amazon Bedrock model evaluation [https://docs.aws.amazon.com/bedrock/latest/userguide/evaluation.html] and Model evaluation metrics [https://docs.aws.amazon.com/bedrock/latest/userguide/model-evaluation-metrics.html].
    
    The selected model should be the least expensive model that still satisfies the required thresholds for the task, such as correctness, relevance, and safety. Token usage matters because FM inference cost is affected by input tokens, output tokens, prompt length, retrieved context, and response length. The AWS model selection guidance also treats capabilities, cost, throughput, API compatibility, and Region as model selection criteria, as described in Supported foundation models in Amazon Bedrock [https://docs.aws.amazon.com/bedrock/latest/userguide/models.html].
    
    Monitoring after release is still important, but operational metrics do not replace evaluation of model quality before promotion. Exact output-string checks are also a poor fit for GenAI regression testing because semantically correct paraphrases can fail even when they are acceptable to users. A repeatable evaluation set with thresholds gives the team a controlled way to compare models and block promotion when quality meaningfully regresses.

---

### Question 53

**Category:** Content Domain 3: Deployment and Orchestration of ML and AI  
**Status:** ✅ **Correct**

A sports analytics firm's ML platform team must score millions of historical player-event records that are stored in Amazon S3. The scoring job runs once after each game day, and downstream analysts need the prediction files in Amazon S3 before the next morning. No application needs interactive predictions, and the team wants to avoid paying for an inference endpoint when no scoring job is running.

Which inference strategy will meet these requirements MOST cost-effectively?

* **A)** Deploy an Amazon SageMaker AI real-time endpoint for the S3 records.
* **B)** Run an Amazon SageMaker AI batch transform job for the S3 records.
* **C)** Deploy an Amazon SageMaker AI asynchronous endpoint for the S3 records.
* **D)** Deploy an Amazon SageMaker AI serverless endpoint for the S3 records.

??? note "Click to reveal Answer & Explanation"
    **Correct Answer:** **B**

    #### Correct Option Analysis
    * **B is Correct:** This option is correct because batch transform is designed for offline inference on datasets, such as files stored in Amazon S3. It does not require a persistent inference endpoint, which fits a scheduled scoring workload that has no interactive latency requirement.

    #### Distractor Analysis
    * **A is Incorrect:** A real-time endpoint is appropriate when applications need low-latency interactive predictions. Keeping an endpoint available for a once-daily offline job adds unnecessary cost when no requests are being served.
    * **C is Incorrect:** Asynchronous inference is suitable for queued requests that take longer to process or have larger payloads than typical real-time requests. The scenario describes a recurring bulk scoring job with results written to Amazon S3, so batch transform better matches the workload pattern.
    * **D is Incorrect:** Serverless inference can be useful for workloads with idle periods and uneven traffic that can tolerate cold starts. However, the workload is a large scheduled dataset scoring job, so an offline batch strategy is a better fit than invoking an endpoint for many records.

    #### Overall Explanation
    For inference strategy selection, start with the workload shape. Real-time inference is for interactive applications that need low latency, while batch transform is for offline scoring of datasets when predictions can be produced as files rather than returned immediately to a caller.
    
    In this scenario, the records already reside in Amazon S3, the job runs on a schedule, and there is no requirement to serve live requests. A SageMaker AI batch transform job can process the dataset and write predictions back to Amazon S3 without keeping an endpoint running between jobs.
    
    Serverless inference and asynchronous inference both reduce some operational burden compared with managing fixed endpoint capacity, but they still represent endpoint-based invocation patterns. They are useful for different serving needs: serverless for intermittent endpoint traffic, and asynchronous inference for queued request processing when immediate responses are not required.
    
    See the SageMaker AI guidance on deployment options for inference [https://docs.aws.amazon.com/sagemaker/latest/dg/deploy-model-options.html] and the documentation for batch transform [https://docs.aws.amazon.com/sagemaker/latest/dg/batch-transform.html].

---

### Question 54

**Category:** Content Domain 1: Data Preparation for ML and AI  
**Status:** ❌ **Incorrect**

An online learning provider's ML platform team is preparing training data for a course recommendation model. The raw inputs include clickstream JSON files in Amazon S3, course catalog Parquet files in Amazon S3, and instructor attributes exposed through a JDBC source. The team must merge the sources, compute session-level features with custom transformations, and run the preparation on a schedule without administering servers.

Which solution will meet these requirements?

* **A)** Create a scheduled AWS Glue ETL job in PySpark to read the S3 and JDBC sources, run the joins and session logic, and write the merged dataset to Amazon S3.
* **B)** Create an Amazon Data Firehose delivery stream with a Lambda transform to combine incoming records, buffer the data, and deliver the merged dataset to Amazon S3.
* **C)** Create an Amazon QuickSight dataset to read the S3 and JDBC sources, add calculated fields for sessions, and use the analysis output as the training dataset.
* **D)** Create a SageMaker notebook with pandas to download the S3 and JDBC sources, run the joins and session logic, and upload the merged dataset to Amazon S3.

??? note "Click to reveal Answer & Explanation"
    **Correct Answer:** **A**

    #### Correct Option Analysis
    * **A is Correct:** This option supports serverless ETL, scheduled execution, and custom code for transformations that go beyond simple visual preparation. AWS Glue jobs can use Apache Spark to process larger-than-memory datasets and write the prepared training data back to Amazon S3. Your answer is incorrect

    #### Distractor Analysis
    * **B is Incorrect:** Amazon Data Firehose is designed for near-real-time delivery of streaming data to destinations such as Amazon S3, Amazon Redshift, and Amazon OpenSearch Service. It is not designed to read existing S3 files and a JDBC source, perform a batch join across those sources, and compute session-level features.
    * **C is Incorrect:** QuickSight is primarily for analysis and visualization, and its data preparation capabilities are limited compared with an ETL job. It is not the right service for a scheduled custom data engineering pipeline that produces a reusable training dataset in Amazon S3.
    * **D is Incorrect:** A pandas notebook can be useful for exploration or small datasets, but it depends on a single compute environment and local memory. The scenario requires a scheduled, larger-scale preparation workflow without server administration, which is a better fit for a managed Spark-based ETL job.

    #### Overall Explanation
    AWS Glue ETL jobs are a practical fit when a training-data preparation task needs to combine multiple sources, apply custom transformations, and run repeatedly without managing a cluster. Glue jobs use a managed Apache Spark-based processing environment, so the engineer can express joins and feature logic in code while AWS handles the underlying infrastructure. The visual and code-based authoring paths are described in Authoring jobs in AWS Glue [https://docs.aws.amazon.com/glue/latest/dg/author-job-glue.html], and Glue programming abstractions for combining datasets are covered in AWS Glue DynamicFrame programming [https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-crawler-pyspark-extensions-dynamic-frame.html].
    
    The important tradeoff is between interactive analysis, streaming delivery, and repeatable ETL. QuickSight can prepare data for dashboards, but it is not a scheduled feature engineering pipeline for ML training data. Amazon Data Firehose can transform and deliver streaming records, but it does not perform batch joins across existing files and JDBC sources. A pandas notebook gives flexibility, but a single notebook environment is a poor fit when the data exceeds local memory and the workflow must run reliably on a schedule.

---

### Question 55

**Category:** Content Domain 3: Deployment and Orchestration of ML and AI  
**Status:** ✅ **Correct**

A city transit authority's ML operations team has a trained PyTorch ridership anomaly model packaged with an inference container. The model will support an internal dashboard that sends synchronous prediction requests only during occasional planning reviews. Traffic is idle most of the week and bursty during reviews. The dashboard can tolerate cold starts. The team wants deployment automation and wants to avoid provisioning endpoint instances.

Which TWO deployment approaches would each meet these requirements?

* **A)** Deploy the model to a SageMaker real-time endpoint by using the SageMaker Python SDK with endpoint auto scaling.
* **B)** Deploy the model to a SageMaker Serverless Inference endpoint by using the SageMaker Python SDK.
* **C)** Deploy the model to a SageMaker Asynchronous Inference endpoint by using Boto3 and have the dashboard retrieve results from Amazon S3.
* **D)** Create the SageMaker model, serverless endpoint configuration, and endpoint by using Boto3 or AWS CLI.
* **E)** Deploy a pre-trained SageMaker JumpStart model to a managed endpoint instead of deploying the packaged model.

??? note "Click to reveal Answer & Explanation"
    **Correct Answer:** **B, D**

    #### Correct Option Analysis
    * **B is Correct:** This option is correct because SageMaker Serverless Inference is a good fit for workloads with idle periods and uneven traffic that can tolerate cold starts. The SageMaker Python SDK provides a programmatic deployment path, including deployment settings from code.
    * **D is Correct:** This option is correct because Boto3 and the AWS CLI can automate the SageMaker hosting workflow. Using a serverless endpoint configuration avoids selecting and maintaining endpoint instances for the sporadic synchronous workload.

    #### Distractor Analysis
    * **A is Incorrect:** This option is incorrect because real-time endpoints are designed for low-latency interactive workloads that use provisioned endpoint capacity. Auto scaling can adjust capacity based on traffic, but it does not match the requirement to avoid provisioning endpoint instances for an idle-heavy workload.
    * **C is Incorrect:** This option is incorrect because asynchronous inference queues requests and returns results asynchronously, commonly through Amazon S3. The dashboard sends synchronous prediction requests, so changing the interaction pattern to retrieve results later does not meet the requirement.
    * **E is Incorrect:** This option is incorrect because SageMaker JumpStart is primarily used to deploy pre-trained models to preconfigured endpoints. It is not the appropriate deployment mechanism for hosting this team's already packaged custom model while also avoiding endpoint instance provisioning.

    #### Overall Explanation
    SageMaker Serverless Inference is designed for inference workloads that have intermittent or unpredictable traffic and can tolerate cold starts. It removes the need to choose and manage endpoint instances, which makes it a strong match when an application is idle for long periods but still needs synchronous invocations when users are active.
    
    Programmatic deployment can be done through the SageMaker Python SDK or through service APIs exposed by Boto3 and the AWS CLI. The general SageMaker deployment choices are summarized in Deploy models for inference [https://docs.aws.amazon.com/sagemaker/latest/dg/deploy-model.html], and the serverless endpoint creation path is described in Create a serverless endpoint [https://docs.aws.amazon.com/sagemaker/latest/dg/serverless-endpoints-create.html].
    
    Real-time endpoints remain useful when consistently low latency and provisioned capacity are required, and endpoint auto scaling helps adjust that provisioned capacity as traffic changes. Asynchronous inference is better when requests can be queued and processed later, especially for longer-running jobs, but it changes the application contract from synchronous responses to asynchronous result retrieval. JumpStart simplifies deployment of pre-trained models, but it is not the right fit for this custom packaged model and the stated hosting pattern.

---

### Question 56

**Category:** Content Domain 3: Deployment and Orchestration of ML and AI  
**Status:** ✅ **Correct**

A regional public transit agency's analytics team is deploying an Amazon Bedrock AgentCore assistant for operations planners. Planners will ask the assistant to analyze small CSV excerpts pasted into a chat session, calculate summary values, and return simple charts. The team does not want to build or operate a Lambda function or REST API for these ad hoc analysis tasks. The assistant should still use normal agent instructions to decide when the analysis capability is needed.

Which solution will meet these requirements with the LEAST operational overhead?

* **A)** Enable the AgentCore built-in Code Interpreter tool, and add instructions that tell the agent when to use it.
* **B)** Create a Bedrock knowledge base from the CSV excerpts, and instruct the agent to use semantic search.
* **C)** Store a reusable Bedrock prompt template, and pass the CSV excerpt through prompt variables.
* **D)** Configure an AgentCore Gateway Lambda target, and define parameters for each requested statistic and chart.

??? note "Click to reveal Answer & Explanation"
    **Correct Answer:** **A**

    #### Correct Option Analysis
    * **A is Correct:** This approach gives the agent a managed analysis capability for calculations and chart generation without requiring a separately maintained tool backend. Agent instructions can describe when the agent should use the tool, which lets the model decide whether the user request needs computation.

    #### Distractor Analysis
    * **B is Incorrect:** A knowledge base is useful for retrieval-augmented generation over indexed content. It is not the right mechanism for executing calculations or producing charts from newly pasted tabular data.
    * **C is Incorrect:** Prompt templates help standardize instructions and reuse prompts across applications. They do not provide an execution environment for reliable calculations or chart creation, so they are insufficient for the analysis task.
    * **D is Incorrect:** AgentCore Gateway can expose Lambda-backed tools to agents, but this approach requires the team to build and maintain the function logic. That additional backend work does not satisfy the requirement for the least operational overhead for ad hoc analysis.

    #### Overall Explanation
    Agent-based applications combine instructions with tools that the model can choose when a user request requires an external capability. For ad hoc numerical analysis and chart creation, the built-in Code Interpreter capability is a better fit than creating a custom Lambda function or REST API, because the managed tool handles the computation pattern without a separate integration layer.
    
    AgentCore Gateway is useful when an agent needs to access existing tools or resources through protocols such as MCP, especially for Lambda functions or REST APIs that already implement business actions. In this scenario, however, there is no existing operational API to call, and building one solely for pasted CSV analysis would add avoidable maintenance. Knowledge bases address retrieval use cases, and prompt templates address prompt reuse and versioning, but neither supplies a tool execution capability for calculations and charts.
    
    For related service behavior, see the Amazon Bedrock AgentCore Runtime overview [https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/agents-tools-runtime.html] and the AgentCore Gateway creation documentation [https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway-create.html].

---

### Question 57

**Category:** Content Domain 4: Operating, Monitoring, and Securing ML and  
**Status:** ✅ **Correct**

A precision agriculture analytics provider runs several containerized ML utilities on the same Amazon ECS cluster by using the EC2 launch type. One evaluator service must invoke an approved Amazon Bedrock foundation model and read an evaluation prompt dataset from a single Amazon S3 prefix. Other services on the cluster must not receive these Bedrock or S3 permissions. The team must avoid embedding long-lived credentials in containers.

Which solution best meets these requirements?

* **A)** Attach the AmazonSageMakerFullAccess managed policy to the evaluator task role and rely on application code checks.
* **B)** Assign an ECS task role to the evaluator task with scoped Bedrock invoke access and S3 read access to the prefix.
* **C)** Add the same Bedrock and S3 permissions to the ECS container instance profile used by all shared cluster nodes.
* **D)** Store a Bedrock API key in Secrets Manager and let the evaluator task read the key at container startup.

??? note "Click to reveal Answer & Explanation"
    **Correct Answer:** **B**

    #### Correct Option Analysis
    * **B is Correct:** This approach gives only the evaluator task the permissions that the evaluator service needs. ECS task roles provide temporary credentials to a specific task, which avoids hard-coded credentials and supports least privilege across services on the same cluster.

    #### Distractor Analysis
    * **A is Incorrect:** A broad managed policy grants more permissions than the evaluator service needs and is not targeted to the stated Bedrock and S3 access pattern. Application code checks are not a substitute for IAM enforcement because other code paths or future changes could bypass those checks.
    * **C is Incorrect:** The container instance profile is intended for the ECS agent and host-level operations, not for per-application authorization. Adding application permissions to the shared instance profile can expose the permissions to other workloads on the same cluster, which does not meet least privilege.
    * **D is Incorrect:** Secrets Manager can protect a secret at rest and control who can retrieve it, but this approach still distributes a bearer credential to the workload. For production AWS workloads, IAM roles with temporary credentials are preferred over API keys for least-privilege authorization.

    #### Overall Explanation
    Least privilege means granting the minimum AWS permissions to the identity that actually performs the work. In this scenario, the evaluator container is the workload that needs access, so the access should be attached to the workload identity, not to every EC2 container instance in the cluster.
    
    For ECS tasks, a task role lets each task receive AWS temporary credentials for its own role. That design separates application permissions from the instance profile that the ECS agent uses for host-level actions such as pulling images or publishing logs. The result is a cleaner security boundary when multiple services share the same cluster.
    
    Amazon Bedrock production applications should use IAM authorization with scoped permissions instead of embedding API keys or broad managed policies. AWS provides examples for controlling Bedrock model access with IAM in Amazon Bedrock identity-based policy examples [https://docs.aws.amazon.com/bedrock/latest/userguide/security_iam_id-based-policy-examples.html]. For AWS ML workloads that need artifact access in S3, the same principle applies: grant access only to the needed bucket or prefix, as illustrated in SageMaker AI execution roles [https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-roles.html].

---

### Question 58

**Category:** Content Domain 1: Data Preparation for ML and AI  
**Status:** ✅ **Correct**

An e-discovery software team's ML engineers are preparing legal contract excerpts to train a model that extracts the parties, effective dates, governing-law jurisdictions, and payment amounts from each document. The training labels must identify the exact words or phrases that contain each value, not only the document's overall category.

Which annotation approach should the team use?

* **A)** Tag each relevant text span with the entity type that the span represents.
* **B)** Draw bounding boxes around rendered document regions that contain clauses.
* **C)** Assign one primary document category based on the contract's business purpose.
* **D)** Assign all applicable topic labels to the document without marking spans.

??? note "Click to reveal Answer & Explanation"
    **Correct Answer:** **A**

    #### Correct Option Analysis
    * **A is Correct:** This is the correct approach because the model needs to learn which words or phrases correspond to specific entity types. Named entity recognition annotations identify spans in text and label them as entities such as organizations, dates, locations, or amounts.

    #### Distractor Analysis
    * **B is Incorrect:** Bounding boxes are appropriate when the model needs visual locations in an image or rendered page. The requirement is to identify exact text spans and entity types, not to localize larger visual regions.
    * **C is Incorrect:** This approach describes text classification, which labels a whole document or passage. It would not identify the exact words or phrases that contain the extracted values.
    * **D is Incorrect:** This approach describes multi-label classification, where several labels can apply to the same item. It can indicate topics present in a document, but it does not teach a model where entities appear in the text.

    #### Overall Explanation
    For this labeling task, the important distinction is the unit being labeled. Document classification labels the entire document, multi-label classification assigns multiple document-level tags, and object detection labels visual regions. The requirement is different: each relevant phrase in the contract must be tagged with what that phrase represents.
    
    Named entity recognition is the annotation pattern that fits this need. Annotators mark spans of text and assign entity classes, so a model can learn that a particular phrase is a party name, date, jurisdiction, or payment amount. This kind of training data is useful when the goal is structured extraction from unstructured text rather than routing, categorization, or visual detection.
    
    Human labeling workflows should also include clear instructions and quality checks so annotators mark spans consistently. Amazon SageMaker Ground Truth documentation describes human-in-the-loop labeling concepts, input and output data, and annotation consolidation in labeling workflows: Overview of SageMaker Ground Truth human-in-the-loop labeling [https://docs.aws.amazon.com/sagemaker/latest/dg/sms.html] and Annotation consolidation [https://docs.aws.amazon.com/sagemaker/latest/dg/sms-annotation-consolidation.html].

---

### Question 59

**Category:** Content Domain 2: ML Model and Foundation Model (FM) Develop  
**Status:** ✅ **Correct**

An aerospace maintenance vendor's AI team is building a retrieval-augmented generation assistant on Amazon Bedrock. The assistant answers technician questions by using approved service manuals as external context. Technicians must be able to verify which manual excerpts influenced each generated answer before they act on the response. The team does not need visibility into model weights or token probabilities.

Which action should the AI engineer take to help explain each generated answer?

* **A)** Compute ROUGE-L scores for each answer to compare sequence overlap with technician-written references.
* **B)** Apply Amazon Bedrock Guardrails for each request to filter unsafe topics and sensitive information.
* **C)** Run Amazon Bedrock Model Evaluations with BERTScore to compare responses with technician-written answers.
* **D)** Use Amazon Bedrock Knowledge Bases to retrieve manual passages and include source citations in the response.

??? note "Click to reveal Answer & Explanation"
    **Correct Answer:** **D**

    #### Correct Option Analysis
    * **D is Correct:** This option is correct because a knowledge base can retrieve relevant source chunks for a prompt and use those chunks as context for generation. Returning the sources with the answer helps technicians understand which documents influenced the generated output.

    #### Distractor Analysis
    * **A is Incorrect:** ROUGE-L measures overlap based on the longest common subsequence between generated and reference text. This metric can help evaluate summarization quality, but it does not provide source attribution for an individual generated answer.
    * **B is Incorrect:** Guardrails help enforce runtime safety policies such as content filtering, denied topics, and sensitive-information controls. Guardrails do not explain which retrieved documents or passages influenced a generated answer.
    * **C is Incorrect:** BERTScore is useful for evaluating semantic similarity between generated text and reference text. However, this approach evaluates model quality across prompts and does not show which manual excerpts supported a specific runtime answer.

    #### Overall Explanation
    For a retrieval-augmented generation application, the most useful explanation for many users is often source attribution: showing the retrieved passages that were provided to the foundation model as context. Amazon Bedrock Knowledge Bases can retrieve relevant chunks from configured data sources and use them during generation, so returning citations or source references gives technicians a practical way to verify the answer against approved manuals. See Amazon Bedrock Knowledge Bases retrieval and RetrieveAndGenerate [https://docs.aws.amazon.com/bedrock/latest/userguide/kb-how-retrieval.html].
    
    Evaluation metrics such as BERTScore and ROUGE-L are useful in development and CI/CD because they compare generated responses against reference outputs. They help measure quality, but they do not explain the evidence behind a single live response. Amazon Bedrock model evaluation can also use judge-based approaches to score generated responses, as described in Amazon Bedrock model evaluation with an LLM-as-a-judge [https://docs.aws.amazon.com/bedrock/latest/userguide/evaluation-judge.html].
    
    Guardrails address a different requirement: enforcing responsible AI policies at runtime. They can filter or block content, but they are not a replacement for citations when users need to verify the retrieved facts that influenced an answer.

---

### Question 60

**Category:** Content Domain 1: Data Preparation for ML and AI  
**Status:** ✅ **Correct**

An insurance underwriting analytics team standardizes claim risk features in Amazon SageMaker Feature Store. The team produces transformed feature records every hour and needs analysts to query historical feature values with Amazon Athena. The team wants to avoid maintaining a separate Hive metastore or running crawlers for these feature records. The team does not need low-latency feature lookups for real-time inference.

Which approach should the team use?

* **A)** Store the transformed records directly in Amazon S3, run an AWS Glue crawler on the bucket, and query the crawler-created table with Athena instead.
* **B)** Create the feature group with an offline store in Amazon S3, ingest the transformed records, and query the automatically created AWS Glue Data Catalog table with Athena.
* **C)** Stream the transformed records to Amazon Data Firehose, deliver them to Amazon S3, and query the delivered objects with Athena after creating an external table.
* **D)** Create the feature group with only an online store, ingest the transformed records, and query the feature records by using Athena through a JDBC connection.

??? note "Click to reveal Answer & Explanation"
    **Correct Answer:** **B**

    #### Correct Option Analysis
    * **B is Correct:** This approach matches a batch analytics workload that needs historical feature values rather than real-time feature retrieval. SageMaker Feature Store can use an offline store in Amazon S3, and the offline store is designed for access by tools such as Athena through catalog metadata.

    #### Distractor Analysis
    * **A is Incorrect:** This approach can make S3 data queryable in Athena, but it bypasses SageMaker Feature Store. The requirement is to standardize features in Feature Store and avoid maintaining separate catalog discovery for the feature records.
    * **C is Incorrect:** Amazon Data Firehose is useful for managed delivery to destinations such as Amazon S3, but this approach does not ingest the features into a Feature Store feature group. It also requires separate table setup for Athena rather than using the Feature Store offline store integration.
    * **D is Incorrect:** An online store is intended for low-latency record retrieval by applications, not historical analytical querying with Athena. This approach also omits the S3-backed offline store that supports batch access patterns.

    #### Overall Explanation
    SageMaker Feature Store supports different access patterns for feature data. The online store is for low-latency access to current feature values, while the offline store stores historical feature records in Amazon S3 for training, batch analysis, and queries from tools such as Athena.
    
    For an hourly batch feature workflow that does not need real-time inference lookups, the offline store is the better fit. It preserves historical feature values and integrates with the AWS Glue Data Catalog so analytics tools can discover and query the feature data without a separately managed crawler workflow. This is the practical tradeoff: the team gives up the fast application lookup pattern of the online store because the stated requirement is historical analytics, not serving-time retrieval.
    
    Storing data directly in S3 or using Amazon Data Firehose can support data lake ingestion, but those choices do not meet the requirement to ingest into SageMaker Feature Store. Creating only an online store also misses the Athena-oriented batch access pattern. For more information, see the SageMaker documentation for Amazon SageMaker Feature Store [https://docs.aws.amazon.com/sagemaker/latest/dg/feature-store.html] and ingesting data into Feature Store [https://docs.aws.amazon.com/sagemaker/latest/dg/feature-store-ingest-data.html].

---

### Question 61

**Category:** Content Domain 2: ML Model and Foundation Model (FM) Develop  
**Status:** ✅ **Correct**

A robotics manufacturer’s ML team is training a deep neural network in Amazon SageMaker AI to classify sensor sequences. The training loss and validation loss remain nearly flat after many steps. The team suspects that gradients or weights might be unstable, but the training instances show normal CPU, GPU, memory, and disk utilization. Which action should the team take to investigate the convergence issue?

* **A)** Use SageMaker AI with MLflow to compare run parameters, artifacts, lineage, and scalar loss metrics across experiments.
* **B)** Use TensorBoard on SageMaker AI to inspect loss curves, gradient distributions, and weight histograms during training.
* **C)** Use SageMaker Debugger built-in rules as the go-forward tool to detect convergence failures in new training jobs.
* **D)** Use Amazon CloudWatch to graph CPU, GPU, memory, and disk utilization and configure alarms for the training job.

??? note "Click to reveal Answer & Explanation"
    **Correct Answer:** **B**

    #### Correct Option Analysis
    * **B is Correct:** This option is correct because TensorBoard is designed to visualize model-training internals, including scalar loss curves and distributions for gradients and weights. These views help the team investigate whether the model is failing to learn because of issues such as unstable gradients or ineffective weight updates.

    #### Distractor Analysis
    * **A is Incorrect:** MLflow is useful for experiment tracking, reproducibility, and comparing scalar metrics across runs. However, MLflow alone is not the best fit when the team specifically needs to inspect gradient distributions and weight histograms inside the training process.
    * **C is Incorrect:** SageMaker Debugger historically provided rules for training issues, but it is now in maintenance mode and should not be the go-forward choice for new debugging workflows. Current workflows should use tools such as TensorBoard for model internals, MLflow for experiment tracking, and CloudWatch for infrastructure metrics.
    * **D is Incorrect:** CloudWatch is appropriate for infrastructure and system monitoring during training. The scenario already states that those resource metrics appear normal, and CloudWatch does not provide the model-internal gradient and weight visualizations needed for this investigation.

    #### Overall Explanation
    When a model is not converging, the first step is to separate infrastructure symptoms from model-training symptoms. Normal CPU, GPU, memory, and disk utilization reduces the likelihood that the flat loss curves are caused by a resource bottleneck, so the team should inspect the training dynamics inside the model.
    
    TensorBoard on SageMaker AI is the best fit for visualizing scalars, gradients, weights, and related training behavior. Loss curves show whether learning is progressing, while gradient distributions and weight histograms can reveal deeper issues such as vanishing gradients, exploding gradients, or ineffective updates. For more information, see SageMaker AI with TensorBoard [https://docs.aws.amazon.com/sagemaker/latest/dg/tensorboard-on-sagemaker.html] and SageMaker AI overview of debugging model performance and convergence issues [https://docs.aws.amazon.com/sagemaker/latest/dg/train-debug-and-improve-model-performance.html].
    
    MLflow, CloudWatch, and TensorBoard are complementary rather than interchangeable. MLflow helps compare experiments, parameters, metrics, and artifacts across runs, while CloudWatch focuses on infrastructure metrics and alarms. SageMaker Debugger is a less appropriate go-forward choice for new workflows because current exam guidance treats its historical responsibilities as covered by MLflow, TensorBoard, and CloudWatch.

---

### Question 62

**Category:** Content Domain 1: Data Preparation for ML and AI  
**Status:** ✅ **Correct**

A renewable energy operator's ML team is preparing turbine telemetry for a failure-risk classifier in Amazon SageMaker Data Wrangler. One input column is an ISO 8601 event_time value. Historical failures show recurring calendar and shift-related patterns, but the training algorithm expects numeric or categorical features rather than raw timestamp strings.

Which feature engineering approach should the ML engineer use?

* **A)** Convert event_time to Unix epoch seconds, then standardize the single numeric timestamp column.
* **B)** Derive calendar fields such as hour and weekday from event_time, then encode those fields for training.
* **C)** Hash the full event_time string into buckets, then use the bucket ID as a categorical feature.
* **D)** Remove event_time from the dataset, then rely on remaining telemetry values during training.

??? note "Click to reveal Answer & Explanation"
    **Correct Answer:** **B**

    #### Correct Option Analysis
    * **B is Correct:** This approach turns a raw timestamp into features that represent recurring operational patterns the model can learn. Encoding the derived fields makes the values suitable for algorithms that expect numeric or categorical inputs.

    #### Distractor Analysis
    * **A is Incorrect:** This approach makes the timestamp numeric, but it treats time as one continuous value. That representation can hide recurring patterns such as shifts, weekdays, or daily operating cycles.
    * **C is Incorrect:** This approach converts the timestamp string into a categorical value, but the buckets do not preserve meaningful calendar relationships. Hashing full timestamps can also create sparse, arbitrary categories that generalize poorly.
    * **D is Incorrect:** This approach avoids passing an unsupported raw timestamp string to the algorithm. However, it discards potentially useful signal about recurring calendar or operational patterns.

    #### Overall Explanation
    Feature engineering is the process of using knowledge of the data and the model to create more useful input features. A raw timestamp string is usually not a useful model feature by itself because many algorithms cannot interpret the date format or infer recurring business patterns from it.
    
    Splitting the timestamp into derived fields such as hour, weekday, month, or shift can expose patterns that repeat over time. The exact fields should match the operational behavior being modeled, then the fields should be encoded in a way the training algorithm can consume.
    
    Converting the timestamp to epoch seconds and standardizing it may be appropriate when the absolute passage of time is the important signal. It is less suitable when the important signal is periodic, because a continuous timestamp does not naturally represent recurring daily or weekly cycles. Dropping the field loses signal, and hashing the full timestamp tends to obscure useful relationships rather than express them.
    
    Amazon SageMaker Data Wrangler is used for preparing and transforming ML datasets, including creating transformed features before training. For related SageMaker documentation, see Prepare ML data with Amazon SageMaker Data Wrangler [https://docs.aws.amazon.com/sagemaker/latest/dg/data-wrangler.html].

---

### Question 63

**Category:** Content Domain 2: ML Model and Foundation Model (FM) Develop  
**Status:** ✅ **Correct**

An online education provider's AI platform team is choosing a foundation model for a tutoring assistant. The assistant will answer course questions from prompts that include retrieved lesson context. The team has a representative prompt dataset and wants to choose the model that provides the best quality for the expected operating cost before releasing the assistant.

Which TWO actions should the team take?

* **A)** Choose the FM with the highest public benchmark score, then measure cost after production release.
* **B)** Use token counting with expected context and response limits to estimate inference cost for each FM.
* **C)** Compare each generated answer with a reference by exact string match, then promote the cheapest FM.
* **D)** Apply Amazon Bedrock Guardrails to each FM, then use blocked responses as the only quality metric.
* **E)** Run Amazon Bedrock Model Evaluations to compare the candidate FMs on the team’s prompt dataset.

??? note "Click to reveal Answer & Explanation"
    **Correct Answer:** **B, E**

    #### Correct Option Analysis
    * **B is Correct:** Foundation model inference cost is driven largely by input and output tokens, and retrieved context can materially increase token usage. Estimating token usage lets the team compare quality scores against expected cost and make a price-performance decision.
    * **E is Correct:** Amazon Bedrock Model Evaluations can assess foundation model behavior against a prompt dataset by using automated metrics, human evaluation, or LLM-as-a-judge methods. This action helps the team compare models on workload-specific quality dimensions instead of relying only on generic results.

    #### Distractor Analysis
    * **A is Incorrect:** Public benchmarks can be useful for initial screening, but they might not reflect the team’s prompt format, retrieval context, or tutoring quality requirements. Deferring cost analysis until after release does not meet the need to choose based on expected operating cost before deployment.
    * **C is Incorrect:** Exact string matching is brittle for generative AI because acceptable answers can use different wording while preserving the same meaning. Choosing only the cheapest model ignores whether the model satisfies the workload’s quality requirements.
    * **D is Incorrect:** Amazon Bedrock Guardrails are runtime safeguards that enforce policies such as safety controls and denied topics. Guardrails do not replace model evaluation across correctness, relevance, helpfulness, or other quality dimensions.

    #### Overall Explanation
    For a GenAI application, model selection should be based on workload-specific evaluation and cost analysis together. Amazon Bedrock Model Evaluations can compare candidate foundation models against the team’s own prompts by using programmatic evaluation, human evaluation, or LLM-as-a-judge approaches, as described in Amazon Bedrock model evaluation [https://docs.aws.amazon.com/bedrock/latest/userguide/evaluation.html].
    
    Cost is not separate from evaluation for foundation models. Prompts, conversation history, retrieved context, and response length all contribute tokens, so token estimates help the team understand whether a higher-scoring model is worth its higher operating cost. The goal is a price-performance decision, not simply choosing the largest model or the cheapest model.
    
    Guardrails are important runtime controls, but they enforce policy during application flow rather than measuring overall model capability. Public leaderboards and exact string comparisons are also incomplete: leaderboards might not match the tutoring workload, and exact string checks are too rigid for valid paraphrases. Bedrock evaluation metrics such as correctness, completeness, helpfulness, and relevance are examples of quality dimensions that can be considered, as shown in Model evaluation metrics for Amazon Bedrock [https://docs.aws.amazon.com/bedrock/latest/userguide/model-evaluation-metrics.html].

---

### Question 64

**Category:** Content Domain 4: Operating, Monitoring, and Securing ML and  
**Status:** ✅ **Correct**

A public radio network's ML platform team runs Amazon SageMaker AI endpoints for audio classification and uses Amazon Bedrock models for transcript summarization. The workloads have predictable recurring usage, but recent experiments caused several requests for larger service capacity. Finance wants the team to find savings opportunities for recurring ML usage and keep capacity growth aligned with approved operational limits. Which actions should the ML engineer take? (Select TWO)

* **A)** Use AWS Config rules to enforce monthly spend limits and automatically approve larger SageMaker AI endpoint quotas.
* **B)** Use AWS Service Quotas to review applied quotas and request SageMaker AI or Bedrock quota changes only when justified.
* **C)** Use AWS CloudTrail Insights to detect unusual API write activity and calculate discounts for recurring inference traffic.
* **D)** Use AWS Cost Explorer to analyze usage trends and review Savings Plans recommendations for recurring SageMaker AI usage.
* **E)** Use Amazon CloudWatch dashboards to group endpoint CPU metrics and purchase commitments based only on utilization graphs.

??? note "Click to reveal Answer & Explanation"
    **Correct Answer:** **B, D**

    #### Correct Option Analysis
    * **B is Correct:** Service Quotas helps teams view applied quota values, understand capacity limits, and manage quota increase requests. This supports operational guardrails for growth, although it is not a substitute for a budget that measures dollar spend.
    * **D is Correct:** Cost Explorer is appropriate for analyzing cost and usage patterns over time and forecasting spend. For predictable recurring usage, Savings Plans recommendations can help evaluate whether a commitment could reduce compute costs.

    #### Distractor Analysis
    * **A is Incorrect:** AWS Config records resource configurations and evaluates resources against compliance rules. It does not enforce monthly cost limits or automatically approve service quota changes for SageMaker AI endpoints.
    * **C is Incorrect:** CloudTrail Insights is useful for detecting unusual account activity patterns in management events. It does not calculate cost savings opportunities or provide Savings Plans recommendations for ML workloads.
    * **E is Incorrect:** CloudWatch is useful for monitoring operational metrics such as latency, errors, invocations, and resource utilization. CPU graphs alone do not provide the cost and usage analysis needed to evaluate savings commitments.

    #### Overall Explanation
    Cost optimization for ML operations starts with measuring actual usage and spend before changing infrastructure. AWS Cost Explorer helps teams analyze trends, filter and group costs, forecast future usage, and evaluate savings opportunities such as Savings Plans for predictable recurring usage. This fits a workload with steady SageMaker AI endpoint usage better than making commitment decisions from operational metrics alone.
    
    Service Quotas is the right tool for capacity governance. Quotas do not directly cap dollars, but they help control how much service capacity can be consumed before someone requests an increase. For SageMaker AI and Amazon Bedrock, reviewing applied quotas and approving increases only when utilization and business need justify them helps prevent uncontrolled growth while still allowing normal operations.
    
    CloudWatch, CloudTrail, and AWS Config remain important operational and governance services, but they solve different problems. CloudWatch monitors workload health, CloudTrail records API activity, and AWS Config tracks configuration and compliance state. None of those services replaces Cost Explorer for cost trend analysis or Service Quotas for service capacity controls. For more information, see AWS Cost Explorer [https://docs.aws.amazon.com/cost-management/latest/userguide/ce-what-is.html], AWS Service Quotas [https://docs.aws.amazon.com/servicequotas/latest/userguide/intro.html], Amazon Bedrock quotas [https://docs.aws.amazon.com/bedrock/latest/userguide/quotas.html], and Amazon SageMaker AI quotas [https://docs.aws.amazon.com/sagemaker/latest/dg/regions-quotas.html].

---

### Question 65

**Category:** Content Domain 1: Data Preparation for ML and AI  
**Status:** ✅ **Correct**

A subscription fitness app's analytics team is preparing profile and activity data for a churn model. A categorical feature named preferred_workout_type is missing for many members, and the team has only a limited amount of historical data. The missing values appear related to other profile attributes and signup behavior, so the team wants to preserve as many rows as possible while using those relationships during cleaning.

Which approach should the team use?

* **A)** Impute the missing workout categories with a model-based method trained from related profile features.
* **B)** Replace the missing workout categories with the arithmetic mean calculated from the column values.
* **C)** Drop every record with a missing workout category to prevent model-based imputation errors.
* **D)** Impute the missing workout categories by averaging nearest numerical neighbors from KNN distances.

??? note "Click to reveal Answer & Explanation"
    **Correct Answer:** **A**

    #### Correct Option Analysis
    * **A is Correct:** This approach preserves rows and uses relationships in the available data to estimate missing categorical values. Model-based imputation is appropriate when simple deletion would waste limited training data and the missing feature is not purely random.

    #### Distractor Analysis
    * **B is Incorrect:** An unordered category such as a workout type does not have a meaningful arithmetic mean. This action would either fail during preprocessing or create an invalid representation of the feature.
    * **C is Incorrect:** Dropping rows is simple, but it conflicts with the need to preserve limited historical data. If missingness is related to signup behavior or profile attributes, complete-row deletion can also change the training distribution.
    * **D is Incorrect:** KNN imputation commonly averages values from similar rows, which fits numerical data better than unordered categories. The option does not provide a valid way to produce categorical values from the averaged neighbors.

    #### Overall Explanation
    Missing-data cleaning should match the type of feature and the business constraint. KNN-style averaging is a common imputation idea for numerical values because an average has meaning for numbers, but unordered categories need a method that can predict or assign a category rather than compute a numeric mean.
    
    When many rows contain missing categorical values and those missing values are related to other fields, a model-based imputation approach can preserve data while using signals from related features. This approach is more complex than dropping rows or using a simple constant, but it is often the better tradeoff when the dataset is small and the missingness is informative. Amazon SageMaker Data Wrangler and SageMaker Canvas include practical cleaning workflows for handling missing values and reviewing data quality, as described in SageMaker Data Wrangler transforms [https://docs.aws.amazon.com/sagemaker/latest/dg/data-wrangler-transform.html] and Prepare data in SageMaker Canvas [https://docs.aws.amazon.com/sagemaker/latest/dg/canvas-prepare-data.html].

---

### Disclaimer

This quiz is included in Udemy MLA-C02 Course by Frank Kane and Stephane Maarek. Enclosed quiz is included in course and for exam review purpose only and is fully non-profitable. All materials are copyright from their original author and AWS. If it is involved in any copyright issue, please contact site owner.