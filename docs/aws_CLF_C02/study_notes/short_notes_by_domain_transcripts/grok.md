**AWS Certified Cloud Practitioner (CLF-C02) Study Notes**  

---

### Task Statement 1.1: Define the benefits of the AWS Cloud

**Cloud Computing Definition (NIST 5 Characteristics)**  
AWS meets all five criteria of cloud computing:  
1. **On-demand self-service** – Provision compute, storage, databases via Console, CLI, or API without human intervention.  
2. **Broad network access** – Access over the internet (HTTPS, VPN, SSH, etc.).  
3. **Resource pooling** – Multi-tenant shared hardware; customer chooses Region (AWS chooses specific data center).  
4. **Rapid elasticity** – Scale resources up/down automatically to match demand.  
5. **Measured service** – Pay only for what you use; usage is metered and billed.

**Core Benefits**  
- **Agility** – Launch resources in minutes instead of weeks/months.  
- **Elasticity** – Automatically match capacity to demand (scale out/in).  
- **Cost savings** – Trade CapEx for OpEx; economies of scale passed to customers.  
- **Global reach** – Deploy worldwide in minutes.  
- **High availability & fault tolerance**.

**High Availability vs Fault Tolerance vs Disaster Recovery**  

| Concept              | Goal                              | Downtime Allowed? | Example Design                     |
|----------------------|-----------------------------------|-------------------|------------------------------------|
| High Availability    | Maximize uptime; recover quickly  | Brief possible    | Active + standby instance         |
| Fault Tolerance      | Continue operating through failure| None              | Two active instances + load balancer |
| Disaster Recovery    | Recover after major outage        | Planned RTO/RPO   | Multi-Region backup & restore     |

**Scaling**  
- **Vertical** – Bigger instance (more CPU/RAM). Causes reboot; higher cost; no app changes needed.  
- **Horizontal** – Add more same-size instances + load balancer. Cheaper; requires session management (sticky sessions).  
- **Elasticity** = Horizontal scaling + automation (Auto Scaling Groups).

**Exam Tips & Traps**  
- “Pay only for what you use” → measured service / OpEx.  
- “Scale capacity to demand automatically” → elasticity.  
- High availability still allows brief downtime; fault tolerance does not.  
- Vertical scaling is simple but not the preferred cloud pattern; horizontal + elasticity is.

**Keywords**  
On-demand, self-service, resource pooling, elasticity, pay-as-you-go, high availability, fault tolerance, vertical vs horizontal scaling.

---

### Task Statement 1.2: Identify design principles of the AWS Cloud

**AWS Well-Architected Framework**  
Best-practice guidance for designing and operating reliable, secure, efficient, cost-effective, and sustainable systems in the cloud. Six pillars:

| Pillar                  | Focus                                      | Key Design Principles (examples) |
|-------------------------|--------------------------------------------|----------------------------------|
| Operational Excellence  | Run & monitor systems, improve processes   | Perform operations as code; make small reversible changes; anticipate failure |
| Security                | Protect data, systems, assets              | Strong identity foundation; apply security at all layers; protect data in transit/at rest |
| Reliability             | Perform intended function correctly        | Automatically recover from failure; scale horizontally; stop guessing capacity |
| Performance Efficiency  | Use resources efficiently                  | Democratize advanced technologies; go global in minutes; use serverless |
| Cost Optimization       | Deliver business value at lowest price     | Adopt consumption model; measure efficiency; stop spending on undifferentiated heavy lifting |
| Sustainability          | Minimize environmental impact              | Maximize utilization; use managed services; anticipate efficient hardware |

**General Design Principles**  
- Stop guessing capacity → use Auto Scaling.  
- Test systems at production scale.  
- Automate to make experimentation easy.  
- Allow evolutionary architectures.  
- Drive architectures with data.  
- Improve through game days.

**AWS Well-Architected Tool**  
Free tool that reviews workloads against the Framework best practices and produces improvement recommendations.

**Exam Tips & Traps**  
- Questions often ask “Which pillar / design principle addresses X?”  
- Decoupling components and thinking parallel (break jobs into smaller parallel tasks) are core reliability & performance practices.  
- Sustainability is the newest pillar (added after original five); do not ignore it.  
- The Framework is not just theory — it is used in real architecture reviews and appears on both Cloud Practitioner and Solutions Architect exams.

**Keywords**  
Well-Architected Framework, six pillars, operational excellence, security, reliability, performance efficiency, cost optimization, sustainability, design principles, stop guessing capacity.

---

### Task Statement 1.3: Understand the benefits of and strategies for migration to the AWS Cloud

**AWS Cloud Adoption Framework (CAF)**  
Organizes guidance into six perspectives that help organizations prepare for cloud transformation:  
Business, People, Governance, Platform, Security, Operations.  

**Benefits of CAF**  
- Reduced business risk (reliability, security).  
- Increased operational efficiency (lower cost, higher productivity).  
- Increased revenue (new products/markets).  
- Improved ESG performance (sustainability & transparency).

**Cloud Adoption Stages**  
1. Project – Evaluate suitability.  
2. Foundation – Initial landing zone / pilot.  
3. Migration – Define roles, establish CCoE, move workloads.  
4. Reinvention – All new work starts in the cloud.

**7 Rs Migration Strategies**  

| Strategy     | Also known as          | Description                              | When to use                          |
|--------------|------------------------|------------------------------------------|--------------------------------------|
| Retire       | –                      | Decommission                             | No longer needed                     |
| Retain       | –                      | Keep on-premises                         | Not ready or regulated               |
| Rehost       | Lift-and-shift         | Move as-is                               | Fast migration, minimal change       |
| Relocate     | –                      | Move large sets of servers (hypervisor)  | VMware Cloud on AWS style            |
| Repurchase   | Drop-and-shop          | Move to different product/SaaS           | Better value alternative exists      |
| Replatform   | Lift-tinker-and-shift  | Minor optimizations                      | Take some cloud advantage            |
| Refactor     | Re-architect           | Rebuild for cloud-native                 | Maximum agility, scalability, cost   |

**Supporting Services (exam examples)**  
- Database migration → AWS DMS + Schema Conversion Tool.  
- Large data transfer → Snow Family (Snowball, Snowball Edge, Snowmobile).  
- File storage low-latency → Amazon EFS.  
- Managed relational → Amazon RDS / Aurora.  
- NoSQL → Amazon DynamoDB.

**Exam Tips & Traps**  
- “Lift and shift” = Rehost.  
- “Take full advantage of cloud-native features” = Refactor.  
- CAF is about organizational readiness; Well-Architected is about workload architecture. Do not confuse the two.  
- Keywords: “database replication”, “large data migration”, “CCoE”.

---

### Task Statement 1.4: Understand concepts of cloud economics

**CapEx → OpEx Shift**  
On-premises = large Capital Expenditure (servers, buildings, cooling).  
AWS = Operational Expenditure (pay only for what you consume).  

**Total Cost of Ownership (TCO) Components**  
- CapEx (hardware, facilities).  
- OpEx (power, cooling, staffing, maintenance).  
- Labor (NOC technicians, admins).  
- Software licensing (BYOL vs included licenses).

**Key Economic Concepts**  
- **Economies of scale** – AWS buys massive capacity → lower unit cost passed to customers.  
- **Rightsizing** – Match instance size/type to actual workload (avoid over-provisioning).  
- **Automation** – Reduce human effort and error → lower cost.  
- **Managed services** – Offload undifferentiated heavy lifting (patching, backups, HA) → lower TCO.  
- **Variable vs fixed costs** – Cloud converts fixed costs into variable costs that scale with usage.

**Licensing Strategies**  
- Bring Your Own License (BYOL).  
- License-included (AWS-managed).  
- Choose the cheaper option that still meets compliance.

**Exam Tips & Traps**  
- “Trade capital expense for variable expense” is a classic correct answer.  
- Rightsizing + Auto Scaling + managed services are the main cost-optimization levers.  
- On-premises TCO almost always includes hidden costs (power, space, staff) that cloud eliminates.  
- Do not assume every workload is cheaper in the cloud without rightsizing and architecture changes.

**Keywords**  
CapEx, OpEx, TCO, economies of scale, rightsizing, consumption model, BYOL, managed services, automation.

---

### Task Statement 2.1: Understand the AWS shared responsibility model

**Core Principle**  
Security and compliance is a **shared** responsibility between AWS and the customer. The exact split depends on the service model (IaaS, PaaS, SaaS / managed).

**High-Level Split**  

| Responsibility Area          | AWS (“of the cloud”)                  | Customer (“in the cloud”)                     |
|------------------------------|---------------------------------------|-----------------------------------------------|
| Physical security            | Data centers, hardware, networking    | –                                             |
| Hypervisor / host OS         | Yes                                   | –                                             |
| Guest OS / patches           | No (EC2)                              | Yes (EC2)                                     |
| Network configuration        | Foundation                            | Security groups, NACLs, VPC design            |
| Application & data           | –                                     | Encryption, IAM, application code, data classification |
| Identity & access            | IAM service itself                    | Users, policies, MFA, least privilege         |
| Managed services (RDS, Lambda, S3) | More of the stack (OS, patches, HA) | Data, configuration, access, encryption keys  |

**Service-Model Examples**  
- **EC2 (IaaS)** – Customer responsible for guest OS, applications, data, security groups.  
- **RDS / Lambda / S3 (PaaS/SaaS-like)** – AWS handles OS, patching, underlying infrastructure; customer still owns data, access control, encryption settings.

**Shared Areas**  
- Configuration of some services, encryption key management (customer can choose KMS CMKs), compliance evidence collection.

**Exam Tips & Traps**  
- “Who is responsible for patching the operating system on an EC2 instance?” → Customer.  
- “Who is responsible for the physical security of the data center?” → AWS.  
- The model shifts with the service; always ask “Is this a managed service?”  
- Root user and IAM are always customer responsibilities.

**Keywords**  
Shared responsibility model, of the cloud / in the cloud, IaaS vs PaaS, guest OS, physical security, encryption, IAM.

---

### Task Statement 2.2: Understand AWS Cloud security, governance, and compliance concepts

**Key Security Benefits of the Cloud**  
- Encryption everywhere (at rest & in transit) with AWS KMS / CloudHSM.  
- Automated compliance evidence.  
- Continuous monitoring and logging.  
- Inheritance of AWS’s global security posture.

**Governance & Compliance**  
- AWS is responsible for the security **of** the cloud and for maintaining many compliance certifications (SOC, PCI-DSS, ISO, HIPAA, FedRAMP, etc.).  
- Customer is responsible for configuring services to meet their own compliance requirements and for data residency.  
- **AWS Artifact** – Free portal to download compliance reports and agreements (BAA, SOC reports, etc.).  
- **AWS Config** – Tracks configuration changes and evaluates compliance against rules.  
- **AWS CloudTrail** – Records API activity (who did what, when, from where).  
- **Amazon CloudWatch** – Metrics, logs, alarms.  
- **AWS Organizations + SCPs** – Central governance and guardrails across accounts.

**Where Logs Live**  
- Management events → CloudTrail.  
- Resource configuration → Config.  
- Application & system metrics/logs → CloudWatch.  
- VPC flow logs, ELB access logs, S3 access logs, etc.

**Exam Tips & Traps**  
- “Where do I download the SOC 2 report?” → AWS Artifact.  
- “Which service records every API call?” → CloudTrail.  
- Encryption is a major security benefit; know that many services offer server-side encryption by default or with one click.  
- Compliance is shared: AWS provides the certifications; customer must use the services correctly.

**Keywords**  
AWS Artifact, CloudTrail, Config, CloudWatch, encryption at rest/in transit, compliance reports, shared compliance, SCPs.

---

### Task Statement 2.3: Identify AWS access management capabilities

**Core Identity Services**  
- **IAM (Identity and Access Management)** – Users, groups, roles, policies.  
- **IAM Identity Center (successor to AWS SSO)** – Central workforce identity, single sign-on to multiple accounts and applications.  
- **AWS Organizations** – Multi-account management + Service Control Policies (SCPs).  
- **Amazon Cognito** – Customer / end-user identity (sign-up, sign-in, federation).  
- **Federation** – SAML 2.0, OIDC, or IAM roles for external IdPs (Active Directory, Okta, etc.).

**Key Concepts**  
- **Principle of least privilege** – Grant only the permissions required.  
- **IAM Policy types** – Identity-based (attached to user/role), resource-based (on the resource, e.g., S3 bucket policy), SCPs (organization-wide guardrails), permission boundaries.  
- **Managed vs customer-managed policies** – AWS managed (ready-made) vs customer-managed (custom).  
- **Roles** – Temporary credentials; preferred over long-lived access keys. Use for EC2, Lambda, cross-account, federation.  
- **Root user** – Full power; protect with MFA; use only for account-level tasks (change account settings, close account, etc.). Never use for daily work.  
- **MFA** – Strongly recommended for all privileged users and required for root.

**Exam Tips & Traps**  
- “Temporary credentials / no long-term keys” → IAM Role.  
- “Centralized login for multiple AWS accounts” → IAM Identity Center.  
- Root user tasks are very limited; almost everything else uses IAM.  
- SCPs can only deny; they cannot grant permissions.  
- “Federated access” or “external identity provider” → federation / IAM Identity Center / Cognito.

**Keywords**  
IAM, least privilege, roles vs users, MFA, root user, SCPs, IAM Identity Center, Cognito, federation, policy types.

---

### Task Statement 2.4: Identify components and resources for security

**Key Security Services**  

| Service                  | Purpose                                      | Exam Keyword / When to Choose                |
|--------------------------|----------------------------------------------|----------------------------------------------|
| AWS WAF                  | Protect web apps from common exploits        | SQL injection, XSS, web ACL                  |
| AWS Shield (Standard/Advanced) | DDoS protection                           | DDoS, volumetric attacks                     |
| AWS Firewall Manager     | Centrally manage WAF, Shield, security groups| Multi-account firewall rules                 |
| Amazon GuardDuty         | Intelligent threat detection                 | Anomalous API activity, compromised instances|
| Amazon Inspector         | Vulnerability assessment                     | CVE scanning of EC2/ECR                      |
| Amazon Macie             | Discover & protect sensitive data in S3      | PII, sensitive data discovery                |
| AWS Security Hub         | Centralized security findings dashboard      | Aggregate findings from multiple services    |
| AWS Trusted Advisor      | Best-practice checks (security category)     | Security recommendations, open ports         |
| AWS KMS / CloudHSM       | Key management & HSM                        | Encryption keys, CMKs                        |
| AWS Secrets Manager / Parameter Store | Secrets & config management         | Database credentials, API keys               |

**Additional Resources**  
- AWS Security Center / Security Blog / Knowledge Center.  
- AWS Marketplace – Third-party security products (firewalls, CASB, etc.).  
- AWS Trusted Advisor security checks and AWS Health Dashboard.

**Exam Tips & Traps**  
- “DDoS protection” → Shield.  
- “Web application firewall” → WAF.  
- “Threat detection using machine learning” → GuardDuty.  
- “Find PII in S3” → Macie.  
- Trusted Advisor is free for basic checks; Business/Enterprise Support unlocks full set.  
- Security is never “set and forget”; continuous monitoring (GuardDuty + Security Hub + Config) is expected.

**Keywords**  
WAF, Shield, GuardDuty, Inspector, Macie, Security Hub, Firewall Manager, Trusted Advisor, KMS, least privilege.

---

### Task Statement 3.1: Define methods of deploying and operating in the AWS Cloud

**Ways to Access & Provision AWS**  
1. **AWS Management Console** – Web UI (good for learning & one-off tasks).  
2. **AWS CLI** – Command-line.  
3. **AWS SDKs / APIs** – Programmatic access from code.  
4. **Infrastructure as Code (IaC)** – CloudFormation, AWS CDK, Terraform (repeatable, version-controlled).  
5. **AWS CloudShell** – Browser-based shell with CLI pre-installed.

**Deployment Models**  
- **Cloud** – Fully in AWS.  
- **Hybrid** – On-premises + AWS (e.g., Direct Connect, Storage Gateway, Outposts).  
- **On-premises** – Traditional data center (not AWS, but still compared).

**One-time vs Repeatable**  
- One-time / manual → Console or simple CLI.  
- Repeatable / production → IaC (CloudFormation templates, CDK apps). IaC enables version control, peer review, and consistent environments.

**Exam Tips & Traps**  
- “Infrastructure as code” or “repeatable deployments” → CloudFormation / CDK.  
- “Programmatic access” → SDK / CLI / API.  
- Hybrid connectivity keywords: Direct Connect (dedicated), Site-to-Site VPN (encrypted over internet), Outposts (AWS hardware on-premises).  
- Prefer IaC for anything beyond a simple experiment.

**Keywords**  
Console, CLI, SDK, API, CloudFormation, CDK, IaC, hybrid, cloud deployment model, Outposts, Direct Connect.

---

### Task Statement 3.2: Define the AWS global infrastructure

**Hierarchy**  
- **Region** – Geographic area (e.g., us-east-1). Fully independent; choose for latency, compliance, data residency.  
- **Availability Zone (AZ)** – One or more discrete data centers with redundant power, networking, connectivity. AZs in a Region are isolated but connected by low-latency links.  
- **Edge Location / Point of Presence** – Used by CloudFront, Route 53, Global Accelerator, AWS WAF for low-latency content delivery and DNS. Far more numerous than Regions.

**High Availability Design**  
- Deploy across **multiple AZs** in the same Region → survives single AZ failure.  
- Multi-Region → disaster recovery, global low latency, data sovereignty.

**Key Facts for Exam**  
- AZs do **not** share single points of failure.  
- Regions are isolated (no automatic replication between Regions unless you configure it).  
- Edge locations are for caching and edge services, not for running general EC2 workloads.

**Exam Tips & Traps**  
- “Lowest latency for end users worldwide” → CloudFront + edge locations or multi-Region.  
- “Survive an Availability Zone failure” → Multi-AZ.  
- “Data residency / sovereignty” → Specific Region.  
- “Disaster recovery with low RPO/RTO” → Multi-Region active-active or pilot-light / warm-standby.

**Keywords**  
Region, Availability Zone, edge location, multi-AZ, multi-Region, high availability, data residency, CloudFront.

---

### Task Statement 3.3: Identify AWS compute services

**Core Compute Services**  

| Service              | Type                  | When to Choose / Keywords                          |
|----------------------|-----------------------|----------------------------------------------------|
| Amazon EC2           | Virtual servers       | Full control of OS, custom apps, long-running      |
| AWS Lambda           | Serverless functions  | Event-driven, short-lived, no server management   |
| Amazon ECS           | Containers (AWS orchestrator) | Docker containers, AWS-native                 |
| Amazon EKS           | Containers (Kubernetes) | Standard Kubernetes, portability                 |
| AWS Fargate          | Serverless containers | Run ECS/EKS tasks without managing servers         |
| AWS Elastic Beanstalk| PaaS                  | Upload code, AWS handles infrastructure            |
| Amazon Lightsail     | Simple VPS            | Simple workloads, predictable low price            |
| AWS Batch            | Batch computing       | Large-scale batch jobs                             |
| EC2 Auto Scaling     | Elasticity            | Automatically adjust capacity                      |
| Elastic Load Balancing | Traffic distribution | Distribute traffic across instances/containers     |

**EC2 Instance Families (high-level)**  
- General purpose, Compute optimized, Memory optimized, Storage optimized, Accelerated computing.

**Exam Tips & Traps**  
- “No servers to manage” + short tasks → Lambda.  
- “Containers without managing servers” → Fargate.  
- “Kubernetes” → EKS.  
- “Auto Scaling provides elasticity”.  
- Load balancer types: Application (HTTP/HTTPS), Network (TCP/UDP), Gateway, Classic (legacy).

**Keywords**  
EC2, Lambda, ECS, EKS, Fargate, Auto Scaling, Elastic Load Balancing, serverless, containers, instance types.

---

### Task Statement 3.4: Identify AWS database services

**Relational vs Non-Relational**  

| Service            | Type              | Keywords / Use Case                              |
|--------------------|-------------------|--------------------------------------------------|
| Amazon RDS         | Relational (managed) | MySQL, PostgreSQL, MariaDB, Oracle, SQL Server; Multi-AZ, read replicas |
| Amazon Aurora      | Relational (MySQL/PostgreSQL compatible) | Higher performance, serverless option, global databases |
| Amazon DynamoDB    | NoSQL (key-value & document) | Single-digit ms, massive scale, serverless     |
| Amazon Redshift    | Data warehouse    | Analytics, OLAP, columnar                        |
| Amazon ElastiCache | In-memory         | Redis / Memcached caching                        |
| Amazon DocumentDB  | Document (MongoDB compatible) | JSON documents                               |
| Amazon Neptune     | Graph             | Social networks, recommendation engines          |
| Amazon Keyspaces   | Wide-column (Cassandra) | –                                              |
| Amazon MemoryDB    | Redis-compatible durable | –                                            |

**Migration**  
- AWS Database Migration Service (DMS) + Schema Conversion Tool (SCT).

**Exam Tips & Traps**  
- “Relational / SQL / joins” → RDS or Aurora.  
- “NoSQL / key-value / single-digit millisecond” → DynamoDB.  
- “Data warehouse / analytics” → Redshift.  
- “Managed” means AWS handles patching, backups, Multi-AZ.  
- Aurora is still relational but faster and more cloud-native than classic RDS.

**Keywords**  
RDS, Aurora, DynamoDB, Redshift, ElastiCache, DMS, relational vs NoSQL, Multi-AZ, read replica.

---

### Task Statement 3.5: Identify AWS network services

**Core Networking Services**  

| Service                  | Purpose                                      | Exam Keywords                              |
|--------------------------|----------------------------------------------|--------------------------------------------|
| Amazon VPC               | Isolated virtual network                     | Subnets, route tables, IGW, NAT            |
| Security Groups          | Instance-level firewall (stateful)           | Allow rules, stateful                      |
| Network ACLs             | Subnet-level firewall (stateless)            | Stateless, allow/deny                      |
| AWS Direct Connect       | Dedicated private connection                 | Consistent low latency, hybrid             |
| AWS Site-to-Site VPN     | Encrypted tunnel over internet               | Quick hybrid connectivity                  |
| Amazon Route 53          | DNS + health checks + routing policies       | Latency-based, failover, geolocation       |
| Elastic Load Balancing   | Distribute traffic                           | ALB, NLB, GLB                              |
| Amazon CloudFront        | CDN                                          | Edge caching, low latency content          |
| AWS Global Accelerator   | Anycast IPs + AWS backbone                   | Improve global application performance     |
| AWS PrivateLink          | Private connectivity to services             | Keep traffic on AWS network                |
| AWS Transit Gateway      | Hub-and-spoke connectivity                   | Connect many VPCs & on-premises            |

**Classic VPC Architecture (exam favorite)**  
Public subnet (IGW) → ALB → Private subnet (app/EC2) → Private subnet (RDS). NAT Gateway for outbound from private subnets.

**Exam Tips & Traps**  
- Security Groups = stateful; NACLs = stateless.  
- “Dedicated connection” → Direct Connect.  
- “DNS failover / latency routing” → Route 53.  
- “Content delivery / edge” → CloudFront.  
- Never put a database in a public subnet.

**Keywords**  
VPC, subnet, Security Group, NACL, Direct Connect, VPN, Route 53, CloudFront, Transit Gateway, PrivateLink.

---

### Task Statement 3.6: Identify AWS storage services

**Object / Block / File Storage**  

| Service              | Type     | Keywords / Use Case                                      |
|----------------------|----------|----------------------------------------------------------|
| Amazon S3            | Object   | Unlimited, durable, static website, data lake, Glacier classes for archive |
| Amazon EBS           | Block    | Persistent disk for EC2, snapshots                       |
| Amazon EFS           | File (NFS) | Shared file system for multiple EC2/containers, elastic  |
| Amazon FSx           | File     | Windows (FSx for Windows), Lustre (HPC), NetApp, OpenZFS |
| AWS Storage Gateway  | Hybrid   | On-premises to AWS (file, volume, tape)                  |
| AWS Backup           | Centralized backup | Policy-based backup across services                    |
| S3 Glacier / Deep Archive | Archive | Lowest cost, retrieval times minutes to hours          |

**S3 Storage Classes (high-level)**  
Standard → Intelligent-Tiering → Standard-IA → One Zone-IA → Glacier Instant → Glacier Flexible → Glacier Deep Archive.

**Exam Tips & Traps**  
- “Object storage / unlimited / 11 9s durability” → S3.  
- “Block storage for EC2” → EBS.  
- “Shared file system / NFS” → EFS.  
- “Archive / rarely accessed / lowest cost” → Glacier.  
- “Hybrid storage” → Storage Gateway.  
- S3 is not a file system; do not treat it like one for low-latency shared access.

**Keywords**  
S3, EBS, EFS, FSx, Glacier, Storage Gateway, object vs block vs file, storage class, durability.

---

### Task Statement 3.7: Identify AWS AI/ML and analytics services

**AI / ML Services**  

| Service                | Purpose                                      | Exam Keywords                              |
|------------------------|----------------------------------------------|--------------------------------------------|
| Amazon Bedrock         | Foundation models / GenAI                    | Foundation model, generative AI, LLMs      |
| Amazon SageMaker       | Build, train, deploy ML models               | Full ML lifecycle                          |
| Amazon Rekognition     | Image & video analysis                       | Facial recognition, object detection       |
| Amazon Comprehend      | NLP                                          | Sentiment, entity extraction               |
| Amazon Transcribe      | Speech-to-text                               | –                                          |
| Amazon Polly           | Text-to-speech                               | –                                          |
| Amazon Translate       | Language translation                         | –                                          |
| Amazon Lex             | Chatbots                                     | Conversational interfaces                  |
| Amazon Forecast        | Time-series forecasting                      | –                                          |
| Amazon Personalize     | Recommendations                              | –                                          |
| Amazon Textract        | Extract text from documents                  | OCR + forms                                |
| Amazon Kendra          | Intelligent search                           | Enterprise search                          |

**Analytics Services**  
- Amazon Athena – Serverless SQL on S3.  
- Amazon Redshift – Data warehouse.  
- Amazon EMR – Big data (Spark, Hadoop).  
- Amazon Kinesis / Managed Service for Apache Flink – Real-time streaming.  
- AWS Glue – ETL / data catalog.  
- Amazon QuickSight – BI dashboards.  
- Amazon OpenSearch Service – Search & log analytics.

**Exam Tips & Traps**  
- “Foundation model / generative AI” → Bedrock.  
- “Build and train your own models” → SageMaker.  
- “SQL queries directly on S3” → Athena.  
- “Real-time streaming data” → Kinesis.  
- “ETL / data catalog” → Glue.

**Keywords**  
Bedrock, SageMaker, Rekognition, Comprehend, Athena, Redshift, Kinesis, Glue, QuickSight, generative AI, foundation model.

---

### Task Statement 3.8: Identify services from other in-scope AWS service categories

**Selected High-Frequency Services by Category**  

| Category                | Key Services                                      | Exam Keywords                              |
|-------------------------|---------------------------------------------------|--------------------------------------------|
| Application Integration | SNS, SQS, EventBridge, Step Functions            | Pub/sub, queue, event bus, orchestration  |
| Management & Governance | CloudWatch, CloudFormation, Config, Systems Manager, Organizations, Control Tower | Monitoring, IaC, compliance, multi-account |
| Migration & Transfer    | DMS, SCT, Snow Family, DataSync, Transfer Family  | Database migration, large data transfer    |
| Developer Tools         | CodeCommit, CodeBuild, CodeDeploy, CodePipeline, Cloud9, X-Ray | CI/CD, source control                      |
| Customer Engagement     | Amazon Connect, Pinpoint, SES                     | Contact center, email, push notifications  |
| Business Applications   | WorkSpaces, AppStream 2.0, WorkDocs               | Virtual desktop, application streaming     |
| IoT                     | IoT Core, IoT Greengrass, IoT Analytics           | Device connectivity, edge computing        |
| Containers / Serverless | (already covered) + App Runner, Amplify           | Simple containerized web apps              |

**Exam Tips & Traps**  
- “Decouple applications / message queue” → SQS.  
- “Pub/sub notifications” → SNS.  
- “Orchestrate multiple AWS services” → Step Functions.  
- “Infrastructure as code” → CloudFormation.  
- “Virtual desktop” → WorkSpaces.  
- Focus on purpose, not deep configuration.

**Keywords**  
SNS, SQS, EventBridge, Step Functions, CloudFormation, Systems Manager, DMS, Snowball, CodePipeline, WorkSpaces.

---

### Task Statement 4.1: Compare AWS pricing models

**EC2 Pricing Models**  
- **On-Demand** – Pay by the second/hour; no commitment. Highest flexibility, highest unit cost.  
- **Reserved Instances / Savings Plans** – 1- or 3-year commitment → significant discount.  
- **Spot Instances** – Spare capacity; up to 90% discount; can be interrupted.  
- **Dedicated Hosts / Instances** – Physical server isolation (licensing, compliance).

**Other Common Models**  
- **S3** – Pay for storage + requests + data transfer out.  
- **Lambda** – Pay per request + duration (GB-seconds).  
- **Data Transfer** – In is usually free; out is charged (except within AZ or to CloudFront in many cases).  
- **Free Tier** – 12-month, always-free, and trial offers.

**Savings Plans vs Reserved Instances**  
- Savings Plans – More flexible (compute usage commitment).  
- Reserved Instances – Can be instance-family or regional; convertible or standard.

**Exam Tips & Traps**  
- “No upfront commitment / unpredictable workload” → On-Demand.  
- “Steady-state / predictable” → Reserved / Savings Plans.  
- “Flexible / interruptible / lowest cost” → Spot.  
- Data transfer **out** to the internet is a common cost center; design to minimize it.

**Keywords**  
On-Demand, Reserved Instances, Savings Plans, Spot, Free Tier, data transfer out, pay-as-you-go.

---

### Task Statement 4.2: Understand resources for billing, budget, and cost management

**Key Tools**  

| Tool / Feature              | Purpose                                      | Exam Keywords                              |
|-----------------------------|----------------------------------------------|--------------------------------------------|
| AWS Cost Explorer           | Visualize & analyze historical costs         | Cost analysis, trends, forecasts           |
| AWS Budgets                 | Set custom budgets & alerts                  | Budget alerts, cost/usage thresholds       |
| AWS Pricing Calculator      | Estimate costs before deployment             | “How much will this cost?”                 |
| AWS Cost and Usage Report   | Detailed raw billing data                    | Most granular data                         |
| Cost Allocation Tags        | Tag resources for chargeback / showback      | User-defined or AWS-generated tags         |
| AWS Organizations Consolidated Billing | Single bill for multiple accounts     | Volume discounts, centralized payment      |
| AWS Free Tier               | Track free-tier usage                        | –                                          |

**Best Practices**  
- Tag everything with cost-allocation tags.  
- Use Budgets + SNS alerts.  
- Regularly review Cost Explorer for anomalies and rightsizing opportunities.  
- Consolidated billing gives you the combined usage volume discounts.

**Exam Tips & Traps**  
- “Alert me when costs exceed $X” → AWS Budgets.  
- “Estimate monthly cost of a proposed architecture” → Pricing Calculator.  
- “Detailed billing data for analysis” → Cost and Usage Report.  
- Tags must be activated in the Billing console to appear in cost reports.

**Keywords**  
Cost Explorer, Budgets, Pricing Calculator, Cost and Usage Report, cost allocation tags, consolidated billing, Organizations.

---

### Task Statement 4.3: Identify AWS technical resources and AWS Support options

**Support Plans (increasing capability & cost)**  
1. **Basic** – Free; Customer Service, documentation, forums.  
2. **Developer** – Business-hours email support, general guidance.  
3. **Business** – 24/7 phone/chat/email, Trusted Advisor full checks, Infrastructure Event Management (extra fee).  
4. **Enterprise On-Ramp** – Pool of Technical Account Managers, faster response.  
5. **Enterprise** – Dedicated TAM, highest response times, Well-Architected Reviews, etc.

**Technical Resources**  
- AWS Documentation, Whitepapers, Architecture Center.  
- AWS Knowledge Center / re:Post (community Q&A).  
- AWS Prescriptive Guidance.  
- AWS Health Dashboard / Personal Health Dashboard.  
- AWS Trusted Advisor (cost, security, performance, fault tolerance, service limits).  
- AWS Professional Services & Partner Network (consulting, system integrators, ISVs).  
- AWS Marketplace – Third-party software with simplified billing.

**Exam Tips & Traps**  
- “24/7 support + full Trusted Advisor” → Business or higher.  
- “Dedicated Technical Account Manager” → Enterprise.  
- “Best-practice recommendations across five categories” → Trusted Advisor.  
- Free resources (docs, whitepapers, re:Post) are available to everyone; paid support adds human assistance and deeper tooling.

**Keywords**  
Support plans (Basic, Developer, Business, Enterprise), Trusted Advisor, TAM, Health Dashboard, Knowledge Center, re:Post, Professional Services, AWS Partner Network, Marketplace.
