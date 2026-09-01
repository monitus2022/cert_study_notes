

# Content Domain 3: Deployment and Orchestration of ML Workflows
<a name="machine-learning-engineer-associate-01-domain3"></a>

**Topics**
- [Content Domain 3: Deployment and Orchestration of ML Workflows](#content-domain-3-deployment-and-orchestration-of-ml-workflows)
  - [Task 3.1: Select deployment infrastructure based on existing architecture and requirements](#task-31-select-deployment-infrastructure-based-on-existing-architecture-and-requirements)
  - [Task 3.2: Create and script infrastructure based on existing architecture and requirements](#task-32-create-and-script-infrastructure-based-on-existing-architecture-and-requirements)
  - [Task 3.3: Use automated orchestration tools to set up continuous integration and continuous delivery (CI/CD) pipelines](#task-33-use-automated-orchestration-tools-to-set-up-continuous-integration-and-continuous-delivery-cicd-pipelines)
  - [See also](#see-also)

## Task 3.1: Select deployment infrastructure based on existing architecture and requirements
<a name="machine-learning-engineer-associate-01-domain3-task1"></a>

Knowledge of:
+ Deployment best practices (for example, versioning, rollback strategies)
+ AWS deployment services (for example, Amazon SageMaker AI)
+ Methods to serve ML models in real time and in batches
+ How to provision compute resources in production environments and test environments (for example, CPU, GPU)
+ Model and endpoint requirements for deployment endpoints (for example, serverless endpoints, real-time endpoints, asynchronous endpoints, batch inference)
+ How to choose appropriate containers (for example, provided or customized)
+ Methods to optimize models on edge devices (for example, SageMaker Neo)

Skills in:
+ Evaluating performance, cost, and latency tradeoffs
+ Choosing the appropriate compute environment for training and inference based on requirements (for example, GPU or CPU specifications, processor family, networking bandwidth)
+ Selecting the correct deployment orchestrator (for example, Apache Airflow, SageMaker Pipelines)
+ Selecting multi-model or multi-container deployments
+ Selecting the correct deployment target (for example, SageMaker AI endpoints, Kubernetes, Amazon ECS, Amazon Elastic Kubernetes Service [Amazon EKS], AWS Lambda)
+ Choosing model deployment strategies (for example, real time, batch)

## Task 3.2: Create and script infrastructure based on existing architecture and requirements
<a name="machine-learning-engineer-associate-01-domain3-task2"></a>

Knowledge of:
+ Difference between on-demand and provisioned resources
+ How to compare scaling policies
+ Tradeoffs and use cases of infrastructure as code (IaC) options (for example, AWS CloudFormation, AWS CDK)
+ Containerization concepts and AWS container services
+ How to use SageMaker AI endpoint auto scaling policies to meet scalability requirements (for example, based on demand, time)

Skills in:
+ Applying best practices to enable maintainable, scalable, and cost-effective ML solutions (for example, automatic scaling on SageMaker AI endpoints, dynamically adding Spot Instances, by using Amazon EC2 instances, by using Lambda behind the endpoints)
+ Automating the provisioning of compute resources, including communication between stacks (for example, by using CloudFormation, AWS CDK)
+ Building and maintaining containers (for example, Amazon ECR, Amazon EKS, Amazon ECS, by using bring your own container [BYOC] with SageMaker AI)
+ Configuring SageMaker AI endpoints within the VPC network
+ Deploying and hosting models by using the SageMaker AI SDK
+ Choosing specific metrics for auto scaling (for example, model latency, CPU utilization, invocations per instance)

## Task 3.3: Use automated orchestration tools to set up continuous integration and continuous delivery (CI/CD) pipelines
<a name="machine-learning-engineer-associate-01-domain3-task3"></a>

Knowledge of:
+ Capabilities and quotas for AWS CodePipeline, AWS CodeBuild, and AWS CodeDeploy
+ Automation and integration of data ingestion with orchestration services
+ Version control systems and basic usage (for example, Git)
+ CI/CD principles and how they fit into ML workflows
+ Deployment strategies and rollback actions (for example, blue/green, canary, linear)
+ How code repositories and pipelines work together

Skills in:
+ Configuring and troubleshooting CodeBuild, CodeDeploy, and CodePipeline, including stages
+ Applying continuous deployment flow structures to invoke pipelines (for example, Gitflow, GitHub Flow)
+ Using AWS services to automate orchestration (for example, to deploy ML models, automate model building)
+ Configuring training and inference jobs (for example, by using Amazon EventBridge rules, SageMaker Pipelines, CodePipeline)
+ Creating automated tests in CI/CD pipelines (for example, integration tests, unit tests, end-to-end tests)
+ Building and integrating mechanisms to retrain models

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Certification. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query aws-certification` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).