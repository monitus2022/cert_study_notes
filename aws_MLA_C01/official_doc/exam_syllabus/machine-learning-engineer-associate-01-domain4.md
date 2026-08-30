

# Content Domain 4: ML Solution Monitoring, Maintenance, and Security
<a name="machine-learning-engineer-associate-01-domain4"></a>

**Topics**
- [Content Domain 4: ML Solution Monitoring, Maintenance, and Security](#content-domain-4-ml-solution-monitoring-maintenance-and-security)
  - [Task 4.1: Monitor model inference](#task-41-monitor-model-inference)
  - [Task 4.2: Monitor and optimize infrastructure and costs](#task-42-monitor-and-optimize-infrastructure-and-costs)
  - [Task 4.3: Secure AWS resources](#task-43-secure-aws-resources)
  - [See also](#see-also)

## Task 4.1: Monitor model inference
<a name="machine-learning-engineer-associate-01-domain4-task1"></a>

Knowledge of:
+ Drift in ML models
+ Techniques to monitor data quality and model performance
+ Design principles for ML lenses relevant to monitoring

Skills in:
+ Monitoring models in production (for example, by using Amazon SageMaker Model Monitor)
+ Monitoring workflows to detect anomalies or errors in data processing or model inference
+ Detecting changes in the distribution of data that can affect model performance (for example, by using SageMaker Clarify)
+ Monitoring model performance in production by using A/B testing

## Task 4.2: Monitor and optimize infrastructure and costs
<a name="machine-learning-engineer-associate-01-domain4-task2"></a>

Knowledge of:
+ Key performance metrics for ML infrastructure (for example, utilization, throughput, availability, scalability, fault tolerance)
+ Monitoring and observability tools to troubleshoot latency and performance issues (for example, AWS X-Ray, Amazon CloudWatch Lambda Insights, Amazon CloudWatch Logs Insights)
+ How to use AWS CloudTrail to log, monitor, and invoke re-training activities
+ Differences between instance types and how they affect performance (for example, memory optimized, compute optimized, general purpose, inference optimized)
+ Capabilities of cost analysis tools (for example, AWS Cost Explorer, AWS Billing and Cost Management, AWS Trusted Advisor)
+ Cost tracking and allocation techniques (for example, resource tagging)

Skills in:
+ Configuring and using tools to troubleshoot and analyze resources (for example, CloudWatch Logs, CloudWatch alarms)
+ Creating CloudTrail trails
+ Setting up dashboards to monitor performance metrics (for example, by using Amazon Quick Sight, CloudWatch dashboards)
+ Monitoring infrastructure (for example, by using Amazon EventBridge events)
+ Rightsizing instance families and sizes (for example, by using SageMaker AI Inference Recommender and AWS Compute Optimizer)
+ Monitoring and resolving latency and scaling issues
+ Preparing infrastructure for cost monitoring (for example, by applying a tagging strategy)
+ Troubleshooting capacity concerns that involve cost and performance (for example, provisioned concurrency, service quotas, auto scaling)
+ Optimizing costs and setting cost quotas by using appropriate cost management tools (for example, AWS Cost Explorer, AWS Trusted Advisor, AWS Budgets)
+ Optimizing infrastructure costs by selecting purchasing options (for example, Spot Instances, On-Demand Instances, Reserved Instances, SageMaker AI Savings Plans)

## Task 4.3: Secure AWS resources
<a name="machine-learning-engineer-associate-01-domain4-task3"></a>

Knowledge of:
+ IAM roles, policies, and groups that control access to AWS services (for example, IAM, bucket policies, SageMaker Role Manager)
+ SageMaker AI security and compliance features
+ Controls for network access to ML resources
+ Security best practices for CI/CD pipelines

Skills in:
+ Configuring least privilege access to ML artifacts
+ Configuring IAM policies and roles for users and applications that interact with ML systems
+ Monitoring, auditing, and logging ML systems to ensure continued security and compliance
+ Troubleshooting and debugging security issues
+ Building VPCs, subnets, and security groups to securely isolate ML systems

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Certification. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query aws-certification` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).