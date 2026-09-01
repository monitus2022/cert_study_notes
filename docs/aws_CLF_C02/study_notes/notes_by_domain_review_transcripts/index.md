# AWS Certified Cloud Practitioner (CLF-C02) Study Notes

These notes summarize the four CLF-C02 content domains and their task statements from the provided AWS exam review outline. The emphasis is on recognition, purpose, benefits, and appropriate useâ€”not implementation details.

---

# Domain 1: Cloud Concepts

## Task Statement 1.1: Define the Benefits of the AWS Cloud

### What is cloud computing?

Cloud computing is the on-demand delivery of IT resources over the internet with pay-as-you-go pricing.

AWS provides services such as:

- Compute
- Storage
- Databases
- Networking
- Security
- Analytics
- Machine learning
- Monitoring and management

### Key benefits of the AWS Cloud

| Benefit | Description |
|---|---|
| **Trade capital expense for variable expense** | Avoid large upfront hardware purchases and pay based on usage. |
| **Economies of scale** | AWS aggregates demand from many customers and can achieve lower costs. |
| **Stop guessing capacity** | Provision resources as needed instead of buying for maximum expected demand. |
| **Increase speed and agility** | Launch resources in minutes instead of waiting for hardware procurement. |
| **Stop spending money running and maintaining data centers** | AWS manages the underlying facilities and much of the infrastructure. |
| **Go global in minutes** | Deploy workloads in multiple Regions around the world. |
| **Benefit from massive economies of scale** | AWS can offer a broad range of services and infrastructure at scale. |
| **Elasticity** | Increase or decrease resources as demand changes. |
| **High availability and reliability** | Use multiple Availability Zones and Regions to reduce disruption. |
| **Security** | AWS provides security capabilities and infrastructure protections, while customers remain responsible for their configurations and data. |

### Scalability, elasticity, and agility

- **Scalability**: The ability to increase capacity to handle growth.
- **Elasticity**: The ability to automatically or manually add and remove capacity as demand changes.
- **Agility**: The ability to experiment, develop, and deploy quickly.

#### Example

An online store adds more compute capacity during a holiday sale and removes it afterward.

- Adding capacity for growth demonstrates **scalability**.
- Automatically removing unused capacity demonstrates **elasticity**.
- Quickly launching the solution demonstrates **agility**.

### AWS compared with on-premises infrastructure

| On premises | AWS Cloud |
|---|---|
| Large upfront hardware investment | Pay-as-you-go variable expense |
| Capacity planning required | Capacity can be provisioned when needed |
| Customer operates the data center | AWS operates the underlying facilities |
| Hardware procurement can take weeks or months | Resources can often be launched in minutes |
| Scaling may require purchasing hardware | Scaling can be performed programmatically |
| Geographic expansion is slower | Deploy across global AWS Regions |

### Exam tips and traps

- **High availability is not automatic for every workload.** Customers must often design across multiple Availability Zones.
- **AWS does not remove all operational responsibility.** The customer still manages configurations, identities, data, and application security.
- **Elasticity is not the same as scalability.** Elasticity emphasizes automatically adjusting resources with demand.
- **Pay-as-you-go does not mean free.** Unused or misconfigured resources can continue generating charges.
- **AWS Regions are not the same as Availability Zones.** A Region contains multiple isolated Availability Zones.

---

## Task Statement 1.2: Identify Design Principles of the AWS Cloud

### AWS Well-Architected Framework

The AWS Well-Architected Framework helps evaluate and improve cloud workloads. Its six pillars are:

1. **Operational Excellence**
   - Run and monitor systems effectively.
   - Continuously improve processes and procedures.
   - Use automation where appropriate.

2. **Security**
   - Protect data, systems, and assets.
   - Apply least privilege.
   - Enable traceability.
   - Automate security best practices.

3. **Reliability**
   - Recover from failures.
   - Dynamically acquire resources to meet demand.
   - Test recovery procedures.

4. **Performance Efficiency**
   - Use resources efficiently.
   - Select appropriate technologies.
   - Adopt new services and technologies as they become available.

5. **Cost Optimization**
   - Avoid unnecessary costs.
   - Select the correct resource types and pricing models.
   - Monitor and control spending.

6. **Sustainability**
   - Minimize environmental impact.
   - Use efficient resources.
   - Reduce idle capacity and unnecessary processing.

### Common AWS design principles

- Design for failure.
- Build loosely coupled systems.
- Automate wherever possible.
- Use services instead of managing infrastructure when appropriate.
- Implement elasticity.
- Use multiple Availability Zones for high availability.
- Monitor systems and improve continuously.
- Apply security at every layer.
- Use managed services to reduce operational overhead.

### High availability and fault tolerance

- **High availability**: A system remains accessible despite some failures.
- **Fault tolerance**: A system continues operating with little or no interruption when a component fails.
- **Disaster recovery**: The process of restoring operations after a major event.

#### Example

Deploying an application across multiple Availability Zones improves availability because a failure in one Availability Zone does not necessarily affect the others.

### Loose coupling

Loose coupling reduces dependencies between components.

Common AWS services used to decouple applications include:

- **Amazon SQS** â€“ Message queuing
- **Amazon SNS** â€“ Pub/sub notifications
- **Amazon EventBridge** â€“ Event routing
- **AWS Lambda** â€“ Event-driven processing

### Monolithic versus microservices architectures

| Monolithic architecture | Microservices architecture |
|---|---|
| Components are tightly integrated | Components are independently deployable |
| A change may affect the entire application | Services can be updated independently |
| Scaling may require scaling the whole application | Individual services can scale separately |
| Often simpler initially | Better suited to independently evolving components |

### Exam tips and traps

- **Multi-AZ improves availability; Multi-Region improves geographic resilience.**
- **Backup and restore is not the same as high availability.**
- **Loose coupling does not mean no communication between components.**
- **Managed services reduce operational responsibility but do not eliminate security responsibility.**
- When a question asks for the pillar concerned with reducing cost, choose **Cost Optimization**, not Performance Efficiency.

---

## Task Statement 1.3: Understand Benefits of and Strategies for Migration to AWS

### Benefits of migration

Migrating to AWS can help organizations:

- Reduce data center and hardware costs
- Increase agility and deployment speed
- Improve scalability and elasticity
- Access global infrastructure
- Improve availability and disaster recovery
- Modernize applications
- Reduce undifferentiated heavy lifting
- Use managed services instead of maintaining infrastructure

### The AWS migration strategies: the â€œ7 Rsâ€

| Strategy | Meaning |
|---|---|
| **Retire** | Remove applications that are no longer needed. |
| **Retain** | Keep the workload in its current environment for now. |
| **Rehost** | Move the application with minimal changes; often called â€œlift and shift.â€ |
| **Relocate** | Move workloads to another AWS environment or platform with minimal modification. |
| **Repurchase** | Replace the existing system with a cloud-based product, often using a subscription or SaaS product. |
| **Replatform** | Make limited optimizations without changing the core architecture. |
| **Refactor / Re-architect** | Redesign the application to take full advantage of cloud-native capabilities. |

### Migration strategy comparison

| Strategy | Effort | Typical reason |
|---|---:|---|
| Retire | Low | Application is no longer needed |
| Retain | None initially | Migration is not currently justified |
| Rehost | Low | Move quickly with minimal changes |
| Relocate | Low to moderate | Move an entire environment or platform |
| Repurchase | Moderate | Replace with a new cloud product |
| Replatform | Moderate | Improve operations without major redesign |
| Refactor | High | Maximize cloud-native benefits |

### AWS migration services and resources

- **AWS Migration Hub**: Tracks migration progress across applications.
- **AWS Application Migration Service**: Helps migrate servers to AWS.
- **AWS Database Migration Service (AWS DMS)**: Migrates databases with minimal downtime.
- **AWS Snow Family**: Helps transfer large amounts of data when network transfer is impractical.
- **AWS Application Discovery Service**: Helps gather information about on-premises workloads.
- **AWS Prescriptive Guidance**: Provides migration and modernization guidance.

### Exam tips and traps

- **Rehost** means minimal changes.
- **Refactor** provides the greatest opportunity for cloud optimization but generally requires the most effort.
- **Replatform** is sometimes called â€œlift, tinker, and shift.â€
- **AWS DMS is for database migration**, not general server migration.
- **Snowball and related services are physical data transfer solutions**, not database engines.

---

## Task Statement 1.4: Understand Concepts of Cloud Economics

### Fixed costs and variable costs

| Cost model | Description |
|---|---|
| **Fixed cost** | A relatively predictable cost, such as purchasing data center hardware. |
| **Variable cost** | A cost that changes according to usage, such as AWS compute or storage consumption. |

AWS primarily uses a **variable expense model**.

### Total cost of ownership (TCO)

TCO compares the total cost of running a workload in different environments.

Costs to consider include:

- Hardware
- Software licensing
- Facilities
- Power and cooling
- Networking
- Administration
- Maintenance
- Security
- Disaster recovery
- Operational labor

### Cost optimization practices

- Right-size resources.
- Shut down development resources when not needed.
- Use Auto Scaling.
- Delete unused volumes, snapshots, load balancers, and elastic IP addresses.
- Select the right AWS Region.
- Use the appropriate pricing model.
- Use managed services where they reduce operational overhead.
- Monitor costs with AWS cost-management tools.
- Use tagging to allocate costs to teams or projects.

### Exam tips and traps

- **AWS pricing is not always the cheapest option for every workload.** Cost depends on architecture, usage, data transfer, and operational requirements.
- **Right-sizing means selecting an appropriately sized resource**, not always choosing the smallest one.
- **Data transfer charges may apply**, especially for data transferred out of AWS.
- Moving to AWS can reduce infrastructure costs but may introduce new costs, such as managed service usage and data transfer.

---

# Domain 2: Security and Compliance

## Task Statement 2.1: Understand the AWS Shared Responsibility Model

### Basic model

AWS and the customer share responsibility for security.

### AWS responsibility: security *of* the cloud

AWS is responsible for protecting the infrastructure that runs AWS services, including:

- Data centers
- Physical facilities
- Physical hosts
- Networking infrastructure
- Hardware
- Virtualization layer

The exact AWS responsibility varies by service.

### Customer responsibility: security *in* the cloud

Customers are generally responsible for:

- Data
- Identity and access management
- Resource configuration
- Operating system patching for customer-managed instances
- Network configuration
- Encryption choices
- Application security
- Security group and firewall rules

### Service-specific responsibility

| Service type | Customer responsibility |
|---|---|
| **Amazon EC2** | Guest operating system, patches, applications, security groups, data |
| **Amazon S3** | Data, bucket policies, access permissions, encryption settings |
| **Amazon RDS** | Database configuration, users, data, access controls; AWS manages much of the underlying infrastructure |
| **AWS Lambda** | Function code, dependencies, permissions, and data; AWS manages servers and operating systems |

### Shared controls

Some controls are shared:

- Patch management
- Configuration management
- Security awareness and training
- Vulnerability management

### Exam tips and traps

- **AWS is responsible for the physical security of its data centers.**
- **Customers are always responsible for their data and access permissions.**
- Using a managed service does not mean the customer has no security responsibilities.
- For EC2, the customer manages the guest operating system.
- For serverless services such as Lambda, AWS manages the underlying servers, but customers secure code, permissions, and data.

---

## Task Statement 2.2: Understand AWS Cloud Security, Governance, and Compliance Concepts

### Security concepts

- **Least privilege**: Grant only the permissions required.
- **Defense in depth**: Use multiple layers of security.
- **Encryption at rest**: Protect stored data.
- **Encryption in transit**: Protect data moving across networks.
- **Traceability**: Record and monitor actions.
- **MFA**: Require an additional authentication factor.
- **Zero trust**: Do not automatically trust users or systems based only on network location.

### AWS compliance

AWS provides compliance certifications, reports, and frameworks that can help customers meet regulatory requirements.

Examples include:

- SOC
- PCI DSS
- ISO certifications
- HIPAA eligibility
- FedRAMP
- GDPR-related capabilities

AWS compliance does **not** automatically make every customer workload compliant. Customers must configure and operate their workloads appropriately.

### Governance

Governance helps organizations control:

- Accounts
- Resources
- Policies
- Costs
- Security
- Compliance
- Standardization

Important governance services and features include:

- **AWS Organizations** â€“ Centrally manage multiple AWS accounts.
- **Service Control Policies (SCPs)** â€“ Set permission guardrails across accounts.
- **AWS Control Tower** â€“ Helps establish and govern a multi-account landing zone.
- **AWS Config** â€“ Records and evaluates resource configurations.
- **AWS CloudTrail** â€“ Records API activity.
- **AWS Audit Manager** â€“ Helps collect evidence for audits.
- **AWS Artifact** â€“ Provides AWS compliance reports and agreements.

### Exam tips and traps

- **AWS Artifact provides compliance documentation**, not continuous resource monitoring.
- **AWS Config evaluates configuration and compliance**, while CloudTrail records API calls.
- **SCPs do not grant permissions.** They set maximum permissions for accounts in an organization.
- Compliance is a shared responsibility.

---

## Task Statement 2.3: Identify AWS Access Management Capabilities

### AWS Identity and Access Management (IAM)

IAM controls authentication and authorization.

- **Authentication**: Who are you?
- **Authorization**: What are you allowed to do?

IAM capabilities include:

- Users
- Groups
- Roles
- Policies
- Multi-factor authentication
- Identity federation

### IAM users, groups, roles, and policies

| IAM feature | Purpose |
|---|---|
| **User** | Represents a person or application requiring long-term credentials. |
| **Group** | Collection of IAM users with common permissions. |
| **Role** | Temporary permissions assumed by users, applications, or AWS services. |
| **Policy** | JSON document defining allowed or denied actions. |

### IAM best practices

- Do not use the root user for everyday tasks.
- Enable MFA for the root user and privileged users.
- Use least privilege.
- Use IAM roles instead of long-term access keys where possible.
- Rotate or remove unnecessary credentials.
- Use groups to assign permissions to users.
- Review permissions regularly.

### Related services

- **IAM Identity Center**: Centralized workforce access to multiple AWS accounts and applications.
- **Amazon Cognito**: Authentication and authorization for applications, especially customer-facing applications.
- **AWS Directory Service**: Managed directory capabilities.
- **AWS Organizations**: Multi-account management.
- **IAM Access Analyzer**: Helps identify unintended access.

### Exam tips and traps

- **IAM roles are preferred for applications running on AWS** instead of embedding access keys.
- **Groups contain users; roles are assumed.**
- **The root user has full account access** and should be protected with MFA.
- IAM is global and is not limited to a single Region.
- IAM policies can explicitly deny access. An explicit deny overrides an allow.

---

## Task Statement 2.4: Identify Components and Resources for Security

### Common AWS security services

| Service | Main purpose |
|---|---|
| **Amazon GuardDuty** | Threat detection and suspicious activity monitoring |
| **AWS Security Hub** | Centralized view of security findings and security posture |
| **Amazon Inspector** | Vulnerability management for workloads |
| **Amazon Macie** | Discovers and helps protect sensitive data in Amazon S3 |
| **AWS WAF** | Protects web applications from common web exploits |
| **AWS Shield** | DDoS protection |
| **AWS Firewall Manager** | Centrally manages firewall rules across accounts |
| **AWS KMS** | Creates and manages encryption keys |
| **AWS Secrets Manager** | Stores, manages, and rotates secrets |
| **AWS Certificate Manager** | Manages SSL/TLS certificates |
| **Amazon CloudWatch** | Monitoring, metrics, logs, and alarms |
| **AWS CloudTrail** | API activity and account auditing |

### Network security controls

- **Security groups**: Stateful virtual firewalls associated with resources such as EC2 instances.
- **Network ACLs**: Stateless subnet-level traffic filters.
- **AWS WAF**: Layer 7 web application protection.
- **AWS Shield**: DDoS protection.
- **VPC endpoints**: Private connectivity from a VPC to supported AWS services.

### Security group versus network ACL

| Security group | Network ACL |
|---|---|
| Stateful | Stateless |
| Applies to network interfaces/resources | Applies at subnet level |
| Supports allow rules only | Supports allow and deny rules |
| Return traffic is automatically allowed | Return traffic must be explicitly allowed |

### Exam tips and traps

- **GuardDuty detects threats; it does not automatically fix them.**
- **Macie focuses on sensitive data in S3.**
- **Inspector identifies vulnerabilities; it is not a general network firewall.**
- **CloudTrail records API activity; CloudWatch monitors operational metrics and logs.**
- Security groups are **stateful**, while network ACLs are **stateless**.

---

# Domain 3: Cloud Technology and Services

## Task Statement 3.1: Define Methods of Deploying and Operating in AWS

### Ways to interact with AWS

- **AWS Management Console**: Browser-based graphical interface.
- **AWS Command Line Interface (CLI)**: Command-line access to AWS services.
- **AWS Software Development Kits (SDKs)**: Programmatic access from supported programming languages.
- **Infrastructure as Code**: Define infrastructure in templates.
- **AWS CloudFormation**: Deploy and manage AWS resources using templates.

### Cloud deployment models

| Model | Description |
|---|---|
| **Cloud** | Workloads run fully in the cloud. |
| **On premises** | Workloads run in privately owned infrastructure. |
| **Hybrid** | Combines on-premises infrastructure with cloud resources. |

### Connectivity options

- **AWS Direct Connect**: Dedicated private connection from an on-premises network to AWS.
- **Site-to-Site VPN**: Encrypted connection over the internet.
- **AWS Client VPN**: Managed VPN access for individual users.
- **AWS PrivateLink**: Private access to supported services and applications.
- **AWS Transit Gateway**: Connects multiple VPCs and on-premises networks through a central hub.

### Exam tips and traps

- **Direct Connect is a dedicated connection; it is not automatically encrypted.**
- **VPN uses encrypted tunnels over the internet.**
- The AWS Console is graphical; CLI and SDKs are programmatic.
- CloudFormation is infrastructure deployment and management, not a monitoring service.

---

## Task Statement 3.2: Define the AWS Global Infrastructure

### Regions

An AWS **Region** is a separate geographic area containing multiple Availability Zones.

Choose a Region based on:

- Latency
- Data residency requirements
- Service availability
- Pricing
- Compliance requirements
- Disaster recovery needs

### Availability Zones

An Availability Zone is one or more discrete data centers with redundant power, networking, and connectivity within an AWS Region.

Use multiple Availability Zones for:

- High availability
- Fault isolation
- Resilience against data center failures

### Edge locations

Edge locations support services such as Amazon CloudFront by caching content closer to users.

### Other infrastructure concepts

- **Local Zones**: Place AWS infrastructure closer to users in specific metropolitan areas.
- **Wavelength Zones**: Place AWS resources within telecommunications networks for very low-latency mobile applications.
- **AWS Outposts**: AWS infrastructure deployed at a customer location.
- **Global services**: Some services, such as IAM, are not Region-specific.
- **Regional services**: Many services and resources are created within a specific Region.

### Exam tips and traps

- A Region contains multiple Availability Zones.
- An Availability Zone can contain multiple data centers.
- Edge locations are not Availability Zones.
- Deploying across Availability Zones protects against localized failures.
- Deploying across Regions can help with geographic disasters and data residency requirements.

---

## Task Statement 3.3: Identify AWS Compute Services

| Service | Primary use |
|---|---|
| **Amazon EC2** | Resizable virtual servers |
| **EC2 Auto Scaling** | Automatically adjusts EC2 capacity |
| **Elastic Load Balancing** | Distributes traffic across resources |
| **AWS Lambda** | Runs code without managing servers |
| **Amazon ECS** | Container orchestration |
| **Amazon EKS** | Managed Kubernetes |
| **AWS Fargate** | Serverless compute for containers |
| **AWS Elastic Beanstalk** | Platform for deploying applications without managing much underlying infrastructure |
| **Amazon Lightsail** | Simplified cloud resources for smaller applications |
| **Amazon Machine Images (AMIs)** | Templates used to launch EC2 instances |

### EC2 versus Lambda

| EC2 | Lambda |
|---|---|
| Customer manages the guest operating system | AWS manages servers and operating systems |
| Long-running workloads are supported | Event-driven function execution |
| More control and customization | Less infrastructure management |
| Charged for provisioned instance usage | Charged based on requests and execution duration |

### ECS, EKS, and Fargate

- **ECS**: AWS container orchestration service.
- **EKS**: Managed Kubernetes control plane.
- **Fargate**: Serverless compute engine that runs containers without managing EC2 instances.

### Exam tips and traps

- Lambda is **serverless**, but servers still exist underneath.
- Fargate is not a container orchestration service by itself; it provides the compute engine for containers.
- EC2 provides more control but more management responsibility.
- Elastic Load Balancing distributes traffic; it does not automatically create application capacity.

---

## Task Statement 3.4: Identify AWS Database Services

| Service | Database type or purpose |
|---|---|
| **Amazon RDS** | Managed relational databases |
| **Amazon Aurora** | AWS-compatible relational database engine |
| **Amazon DynamoDB** | Serverless NoSQL key-value and document database |
| **Amazon Redshift** | Data warehouse |
| **Amazon ElastiCache** | In-memory caching using engines such as Redis or Memcached |
| **Amazon Neptune** | Graph database |
| **Amazon DocumentDB** | Document database compatible with MongoDB workloads |
| **Amazon Timestream** | Time-series database |
| **Amazon MemoryDB** | Durable in-memory database |

### Relational versus NoSQL databases

| Relational | NoSQL |
|---|---|
| Tables, rows, and columns | Flexible key-value or document models |
| Structured schema | Flexible schema |
| SQL queries | Access patterns vary by service |
| Useful for relationships and transactions | Useful for high scale and flexible data models |

### RDS versus running a database on EC2

- **RDS** reduces database administration, including much of the provisioning, patching, backup, and maintenance work.
- **EC2 database hosting** provides greater control but requires the customer to manage the operating system and database software.

### Exam tips and traps

- **DynamoDB is NoSQL**, not a relational database.
- **Redshift is for analytics and data warehousing**, not typical transactional application workloads.
- **ElastiCache improves performance by caching frequently accessed data; it is not usually the primary system of record.**
- RDS is managed, but customers still manage database users, permissions, data, and configuration choices.

---

## Task Statement 3.5: Identify AWS Network Services

| Service | Primary use |
|---|---|
| **Amazon VPC** | Isolated virtual network in AWS |
| **Amazon Route 53** | DNS and domain name services |
| **Elastic Load Balancing** | Distributes incoming traffic |
| **Amazon CloudFront** | Content delivery network |
| **AWS Direct Connect** | Dedicated private network connection |
| **AWS VPN** | Encrypted connectivity |
| **NAT Gateway** | Allows private subnet resources to access the internet without accepting inbound internet connections |
| **Internet Gateway** | Connects a VPC to the internet |
| **Transit Gateway** | Centralized connectivity between VPCs and networks |
| **AWS PrivateLink** | Private access to supported services |
| **AWS Global Accelerator** | Improves global application availability and performance using the AWS global network |

### VPC components

- Subnets
- Route tables
- Internet gateways
- NAT gateways
- Security groups
- Network ACLs
- VPC endpoints

### CloudFront versus Route 53

- **CloudFront** delivers cached content and reduces latency.
- **Route 53** resolves domain names and can route DNS requests.

### Exam tips and traps

- A **private subnet** does not have a direct route to an internet gateway.
- A NAT gateway allows outbound internet access from private resources, but it does not normally allow unsolicited inbound connections.
- Route 53 is DNS; CloudFront is content delivery.
- Security groups protect resources; network ACLs protect subnets.

---

## Task Statement 3.6: Identify AWS Storage Services

| Service | Storage type and use |
|---|---|
| **Amazon S3** | Object storage |
| **S3 Glacier storage classes** | Low-cost archival object storage |
| **Amazon EBS** | Block storage for EC2 |
| **Amazon EFS** | Managed elastic file system |
| **Amazon FSx** | Managed file systems for specific workloads |
| **AWS Storage Gateway** | Hybrid cloud storage integration |
| **AWS Snow Family** | Physical data transfer and edge computing |

### Object, block, and file storage

| Type | AWS example | Typical use |
|---|---|---|
| **Object** | S3 | Backups, media, documents, data lakes |
| **Block** | EBS | EC2 operating systems and application disks |
| **File** | EFS, FSx | Shared file access |

### S3 storage classes

- **S3 Standard**: Frequently accessed data.
- **S3 Standard-IA**: Infrequently accessed data requiring rapid access.
- **S3 One Zone-IA**: Infrequently accessed data stored in one Availability Zone.
- **S3 Glacier Instant Retrieval**: Archive data requiring immediate retrieval.
- **S3 Glacier Flexible Retrieval**: Archive data retrieved in minutes to hours.
- **S3 Glacier Deep Archive**: Lowest-cost long-term archival storage.

### EBS versus EFS

| EBS | EFS |
|---|---|
| Block storage | File storage |
| Typically attached to EC2 resources | Shared file system |
| Generally associated with a single Availability Zone | Designed for regional, multi-AZ access |
| Used for boot and application volumes | Used when multiple resources need shared file access |

### Exam tips and traps

- S3 stores **objects**, not traditional mounted file systems.
- EBS is generally associated with EC2; EFS provides shared file access.
- Glacier is not a separate database or compute serviceâ€”it is an S3 storage class family.
- **S3 One Zone-IA has lower resilience** than multi-AZ S3 storage classes.
- Storage class selection should consider access frequency, retrieval time, durability, and cost.

---

## Task Statement 3.7: Identify AWS AI/ML and Analytics Services

### AI and machine learning services

| Service | Primary use |
|---|---|
| **Amazon SageMaker AI** | Build, train, and deploy machine learning models |
| **Amazon Rekognition** | Image and video analysis |
| **Amazon Transcribe** | Speech-to-text |
| **Amazon Polly** | Text-to-speech |
| **Amazon Translate** | Language translation |
| **Amazon Lex** | Conversational interfaces and chatbots |
| **Amazon Comprehend** | Natural language processing and text analysis |
| **Amazon Textract** | Extracts text and data from documents |
| **Amazon Bedrock** | Build generative AI applications using foundation models |

### Analytics services

| Service | Primary use |
|---|---|
| **Amazon Athena** | Query data in S3 using SQL |
| **Amazon Redshift** | Data warehousing and analytics |
| **Amazon EMR** | Big data processing frameworks |
| **Amazon Kinesis** | Collect and process streaming data |
| **AWS Glue** | Serverless data integration and ETL |
| **Amazon OpenSearch Service** | Search, log analytics, and observability |
| **Amazon QuickSight** | Business intelligence and dashboards |

### Exam tips and traps

- **Athena queries data in S3** and is serverless.
- **Redshift is a data warehouse**, while DynamoDB is a NoSQL operational database.
- **Transcribe converts speech to text; Polly converts text to speech.**
- **Rekognition analyzes images and videos.**
- **Textract extracts text and structured data from documents.**
- SageMaker is for developing and deploying machine learning models; it is not simply a data warehouse.

---

## Task Statement 3.8: Identify Services from Other In-Scope AWS Categories

### Management and monitoring

- **Amazon CloudWatch**: Metrics, logs, alarms, and dashboards.
- **AWS CloudTrail**: API activity and audit history.
- **AWS Config**: Resource configuration history and compliance evaluation.
- **AWS Systems Manager**: Operational management of resources.
- **AWS Trusted Advisor**: Recommendations for cost, security, performance, fault tolerance, and service limits.
- **AWS Service Health Dashboard**: Public information about AWS service status.
- **AWS Health Dashboard**: Personalized information about account and AWS service events.

### Application integration

- **Amazon SQS**: Queue messages between application components.
- **Amazon SNS**: Publish/subscribe messaging and notifications.
- **Amazon EventBridge**: Event bus for routing events.
- **AWS Step Functions**: Coordinates workflows and stateful processes.
- **Amazon API Gateway**: Creates, publishes, and manages APIs.

### Developer and deployment services

- **AWS CodeBuild**: Builds and tests code.
- **AWS CodeDeploy**: Automates application deployments.
- **AWS CodePipeline**: Automates CI/CD workflows.
- **Amazon ECR**: Stores container images.
- **AWS CloudFormation**: Infrastructure as code.

### Exam tips and traps

- CloudWatch is for monitoring; CloudTrail is for API auditing.
- SQS is queue-based; SNS is publish/subscribe.
- Trusted Advisor provides recommendations; it is not a replacement for a security operations team.
- Service Health Dashboard provides general AWS service status; the AWS Health Dashboard provides account-specific events.

---

# Domain 4: Billing, Pricing, and Support

## Task Statement 4.1: Compare AWS Pricing Models

### On-Demand pricing

- Pay for compute capacity by usage.
- No long-term commitment.
- Useful for unpredictable workloads or short-term workloads.
- Usually has a higher effective rate than commitment-based options.

### Reserved Instances and Savings Plans

- Offer reduced pricing in exchange for a commitment.
- Suitable for predictable, steady usage.
- Savings Plans generally provide flexibility across eligible compute usage.
- Reserved Instances are more closely associated with specific resource configurations and terms.

### Spot Instances

- Use spare AWS capacity at a discount.
- AWS can interrupt the workload when capacity is needed.
- Suitable for fault-tolerant and flexible workloads, such as batch jobs.

### Dedicated options

- **Dedicated Hosts**: Physical server dedicated to one customer; useful for licensing and compliance requirements.
- **Dedicated Instances**: Instances running on hardware dedicated to a single customer account, without the same level of host visibility and control.
- **On-Demand Capacity Reservations**: Reserve capacity in a specific Availability Zone; reservations do not necessarily provide a discount.

### Free Tier

The AWS Free Tier provides limited free usage for eligible services and usage types. Limits and eligibility rules apply.

### Exam tips and traps

- Spot Instances can be interrupted.
- Reserved pricing and Savings Plans require a commitment.
- On-Demand does not require a commitment but can cost more for steady workloads.
- A Capacity Reservation is primarily about **capacity availability**, not automatically discounted pricing.
- Free Tier usage can still result in charges if limits are exceeded or non-eligible resources are used.

---

## Task Statement 4.2: Understand Resources for Billing, Budget, and Cost Management

### AWS billing and cost tools

| Tool | Purpose |
|---|---|
| **AWS Pricing Calculator** | Estimate expected AWS costs before deployment |
| **AWS Cost Explorer** | Analyze historical and current spending |
| **AWS Budgets** | Set custom cost or usage budgets and alerts |
| **AWS Billing Console** | View bills, invoices, payment methods, and account charges |
| **Cost and Usage Reports** | Detailed billing and usage data |
| **AWS Cost Categories** | Group and organize costs for reporting |
| **Resource tags** | Identify and allocate costs to projects, teams, or environments |
| **AWS Organizations consolidated billing** | Combine billing across multiple accounts |

### Cost allocation

Tags can be used to classify resources, such as:

- `Environment=Production`
- `Department=Finance`
- `Project=Website`

Cost allocation tags help organizations understand who or what generated costs.

### Ways to control costs

- Use budgets and alerts.
- Apply service quotas and governance.
- Use Auto Scaling.
- Remove unused resources.
- Right-size resources.
- Select appropriate storage classes.
- Use Savings Plans or Reserved Instances for steady workloads.
- Use Spot Instances for interruptible workloads.
- Monitor data transfer and NAT gateway usage.
- Use consolidated billing for multiple accounts.

### Exam tips and traps

- **Pricing Calculator estimates future costs.**
- **Cost Explorer analyzes actual historical/current usage and costs.**
- **Budgets alert you when thresholds are reached; they do not automatically prevent all spending.**
- Tags do not automatically reduce costs; they help track and allocate them.
- Consolidated billing can combine invoices and may provide volume pricing benefits, but it does not make resources free.

---

## Task Statement 4.3: Identify AWS Technical Resources and Support Options

### AWS Support resources

- **AWS documentation**: Service concepts, usage guidance, and reference material.
- **AWS Knowledge Center**: Troubleshooting articles and frequently asked questions.
- **AWS re:Post**: Community-based technical questions and answers.
- **AWS Support Center**: Create and manage support cases.
- **AWS Trusted Advisor**: Recommendations for improving AWS environments.
- **AWS Health Dashboard**: Account-specific and service health information.
- **AWS Service Health Dashboard**: Public AWS service status.
- **AWS Prescriptive Guidance**: Architecture and migration recommendations.
- **AWS whitepapers and architecture center**: Best practices and design guidance.

### AWS Support Plans

AWS Support offerings differ in areas such as:

- Technical support availability
- Response times
- Number and type of support cases
- Access to trusted advisors and proactive guidance
- Architectural and operational assistance

At the CLF-C02 level, understand that:

- **Basic Support** is included for AWS customers.
- Higher support plans provide more technical assistance and faster response options.
- The appropriate plan depends on business and operational requirements.
- Account and billing assistance is available through AWS support resources.

### Trusted Advisor categories

Trusted Advisor can provide recommendations related to:

- Cost optimization
- Performance
- Security
- Fault tolerance
- Service limits

### Exam tips and traps

- **AWS Support is not the same as AWS Professional Services.**
  - Support helps with technical issues and guidance.
  - Professional Services provides consulting and implementation assistance.
- **re:Post is a community resource**, not the same as opening a formal AWS Support case.
- **CloudTrail is not a support service**; it records API activity.
- The Health Dashboard is used to identify AWS service events and account-specific impacts.

---

# Mixed Practice Questions

## Question 1

A company wants to avoid purchasing enough physical servers to handle its maximum expected demand. Which AWS Cloud benefit addresses this requirement?

A. Global reach  
B. Stop guessing capacity  
C. Dedicated infrastructure  
D. Fixed monthly pricing  

**Answer: B â€” Stop guessing capacity**

AWS allows resources to be provisioned and scaled as demand changes.

---

## Question 2

Which Well-Architected Framework pillar focuses on protecting systems, data, and assets?

A. Reliability  
B. Security  
C. Cost Optimization  
D. Operational Excellence  

**Answer: B â€” Security**

---

## Question 3

A company wants to move an application to AWS with minimal changes. Which migration strategy should it use?

A. Refactor  
B. Repurchase  
C. Rehost  
D. Retire  

**Answer: C â€” Rehost**

Rehosting is commonly called â€œlift and shift.â€

---

## Question 4

Who is responsible for configuring IAM permissions in an AWS account?

A. AWS only  
B. The customer  
C. The internet service provider  
D. The AWS data center operator  

**Answer: B â€” The customer**

Customers are responsible for access management and permissions.

---

## Question 5

Which service records API calls made in an AWS account?

A. Amazon CloudWatch  
B. AWS CloudTrail  
C. AWS Config  
D. Amazon GuardDuty  

**Answer: B â€” AWS CloudTrail**

CloudTrail records API activity for auditing and governance.

---

## Question 6

A company needs to run code in response to events without managing servers. Which service should it use?

A. Amazon EC2  
B. AWS Lambda  
C. Amazon EBS  
D. Amazon Redshift  

**Answer: B â€” AWS Lambda**

Lambda runs code without requiring customers to manage servers.

---

## Question 7

Which AWS service is a managed NoSQL database?

A. Amazon RDS  
B. Amazon Redshift  
C. Amazon DynamoDB  
D. Amazon Aurora  

**Answer: C â€” Amazon DynamoDB**

DynamoDB is a managed key-value and document database.

---

## Question 8

Which service provides object storage?

A. Amazon EBS  
B. Amazon EFS  
C. Amazon S3  
D. Amazon EC2  

**Answer: C â€” Amazon S3**

S3 stores data as objects in buckets.

---

## Question 9

Which service is designed to query data stored in Amazon S3 using SQL?

A. Amazon Athena  
B. Amazon Neptune  
C. Amazon Polly  
D. Amazon ElastiCache  

**Answer: A â€” Amazon Athena**

---

## Question 10

Which pricing option uses spare EC2 capacity and can be interrupted?

A. On-Demand Instances  
B. Reserved Instances  
C. Spot Instances  
D. Dedicated Hosts  

**Answer: C â€” Spot Instances**

Spot Instances provide discounts but may be interrupted.

---

## Question 11

Which service helps estimate AWS costs before deploying a workload?

A. AWS Cost Explorer  
B. AWS Budgets  
C. AWS Pricing Calculator  
D. AWS CloudTrail  

**Answer: C â€” AWS Pricing Calculator**

---

## Question 12

A company wants to receive an alert when its monthly AWS spending exceeds a threshold. Which service should it use?

A. AWS Budgets  
B. Amazon Macie  
C. AWS Artifact  
D. AWS Shield  

**Answer: A â€” AWS Budgets**

AWS Budgets can monitor cost or usage against configured thresholds and send alerts.

---

# High-Value Exam Comparisons

| If the question asks about... | Consider... |
|---|---|
| API activity and auditing | AWS CloudTrail |
| Metrics, logs, and alarms | Amazon CloudWatch |
| Resource configuration compliance | AWS Config |
| Threat detection | Amazon GuardDuty |
| Sensitive data discovery in S3 | Amazon Macie |
| Vulnerability scanning | Amazon Inspector |
| Web application protection | AWS WAF |
| DDoS protection | AWS Shield |
| DNS | Amazon Route 53 |
| Cached global content delivery | Amazon CloudFront |
| Object storage | Amazon S3 |
| Block storage for EC2 | Amazon EBS |
| Shared file storage | Amazon EFS |
| Relational database | Amazon RDS or Aurora |
| NoSQL database | Amazon DynamoDB |
| Data warehouse | Amazon Redshift |
| Querying S3 with SQL | Amazon Athena |
| Serverless code execution | AWS Lambda |
| Dedicated private network connection | AWS Direct Connect |
| Encrypted connection over the internet | AWS Site-to-Site VPN |
| Cost estimation | AWS Pricing Calculator |
| Cost analysis | AWS Cost Explorer |
| Cost threshold alerts | AWS Budgets |
| AWS compliance reports | AWS Artifact |
| Community technical questions | AWS re:Post |

# Final Exam Strategy

1. Focus on identifying the correct service from its primary purpose.
2. Distinguish customer responsibility from AWS responsibility.
3. Memorize the Well-Architected Framework pillars.
4. Know the differences between Regions, Availability Zones, and edge locations.
5. Understand object, block, and file storage.
6. Learn the differences between CloudWatch, CloudTrail, and Config.
7. Understand the purposeâ€”not implementation detailsâ€”of major security services.
8. Be careful with words such as:
   - **Automatically**
   - **Managed**
   - **Dedicated**
   - **Highly available**
   - **Encrypted**
   - **Lowest cost**
9. Remember that the cheapest option depends on workload requirements, usage patterns, and data transfer.
10. When two answers seem possible, choose the service that most directly matches the requirement with the least operational overhead.