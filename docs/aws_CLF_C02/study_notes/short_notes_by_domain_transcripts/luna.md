# AWS Certified Cloud Practitioner (CLF-C02) Complete Study Notes

## Table of Contents
- [AWS Certified Cloud Practitioner (CLF-C02) Complete Study Notes](#aws-certified-cloud-practitioner-clf-c02-complete-study-notes)
  - [Table of Contents](#table-of-contents)
  - [Domain 1: Cloud Concepts (24%)](#domain-1-cloud-concepts-24)
    - [Task Statement 1.1: Define the benefits of the AWS Cloud](#task-statement-11-define-the-benefits-of-the-aws-cloud)
    - [Task Statement 1.2: Identify design principles of the AWS Cloud](#task-statement-12-identify-design-principles-of-the-aws-cloud)
    - [Task Statement 1.3: Understand the benefits of and strategies for migration to the AWS Cloud](#task-statement-13-understand-the-benefits-of-and-strategies-for-migration-to-the-aws-cloud)
    - [Task Statement 1.4: Understand concepts of cloud economics](#task-statement-14-understand-concepts-of-cloud-economics)
  - [Domain 2: Security and Compliance (30%)](#domain-2-security-and-compliance-30)
    - [Task Statement 2.1: Understand the AWS shared responsibility model](#task-statement-21-understand-the-aws-shared-responsibility-model)
    - [Task Statement 2.2: Understand AWS Cloud security, governance, and compliance concepts](#task-statement-22-understand-aws-cloud-security-governance-and-compliance-concepts)
    - [Task Statement 2.3: Identify AWS access management capabilities](#task-statement-23-identify-aws-access-management-capabilities)
    - [Task Statement 2.4: Identify components and resources for security](#task-statement-24-identify-components-and-resources-for-security)
  - [Domain 3: Cloud Technology and Services (34%)](#domain-3-cloud-technology-and-services-34)
    - [Task Statement 3.1: Define methods of deploying and operating in the AWS Cloud](#task-statement-31-define-methods-of-deploying-and-operating-in-the-aws-cloud)
    - [Task Statement 3.2: Define the AWS global infrastructure](#task-statement-32-define-the-aws-global-infrastructure)
    - [Task Statement 3.3: Identify AWS compute services](#task-statement-33-identify-aws-compute-services)
    - [Task Statement 3.4: Identify AWS database services](#task-statement-34-identify-aws-database-services)
    - [Task Statement 3.5: Identify AWS network services](#task-statement-35-identify-aws-network-services)
    - [Task Statement 3.6: Identify AWS storage services](#task-statement-36-identify-aws-storage-services)
    - [Task Statement 3.7: Identify AWS artificial intelligence and machine learning (AI/ML) services and analytics services](#task-statement-37-identify-aws-artificial-intelligence-and-machine-learning-aiml-services-and-analytics-services)
    - [Task Statement 3.8: Identify services from other in-scope AWS service categories](#task-statement-38-identify-services-from-other-in-scope-aws-service-categories)
  - [Domain 4: Billing, Pricing, and Support (12%)](#domain-4-billing-pricing-and-support-12)
    - [Task Statement 4.1: Compare AWS pricing models](#task-statement-41-compare-aws-pricing-models)
    - [Task Statement 4.2: Understand resources for billing, budget, and cost management](#task-statement-42-understand-resources-for-billing-budget-and-cost-management)
    - [Task Statement 4.3: Identify AWS technical resources and AWS Support options](#task-statement-43-identify-aws-technical-resources-and-aws-support-options)

---

## Domain 1: Cloud Concepts (24%)

### Task Statement 1.1: Define the benefits of the AWS Cloud

**1. Core Concepts & Business Value**

- **Trade CapEx for OpEx:** Avoid large upfront investments in data centers and hardware; pay for cloud resources as consumed.
- **Economies of scale:** AWS aggregates demand across customers, helping reduce infrastructure costs.
- **Agility:** Provision and change resources quickly instead of waiting for hardware procurement and installation.
- **Speed of deployment:** Launch infrastructure globally in minutes, accelerating development and time to market.
- **Global reach:** Deploy applications closer to users around the world to improve user experience and support geographic expansion.
- **High availability (HA):** Design across multiple locations, especially **Availability Zones**, to reduce the impact of infrastructure failures.
- **Elasticity:** Automatically add or remove capacity as workload demand changes. Elasticity helps avoid both underprovisioning and paying for unused resources.
- **Scalability:** Increase or decrease capacity to handle changing workloads; scaling may be manual or automatic.
- **Flexibility:** Choose services, regions, and capacity based on changing business and technical requirements.
- **Reduced undifferentiated heavy lifting:** AWS manages much of the underlying infrastructure, allowing customers to focus on applications and business value.

**2. In-Scope Services & Key Functions**

| Service / Feature | Primary Function | Exam Use Case |
| :--- | :--- | :--- |
| **AWS Global Infrastructure** | Worldwide infrastructure made up of **Regions, Availability Zones, and edge locations** for deploying workloads near users and designing for resilience. | Choose when a scenario requires **global reach, lower latency, regional deployment, or high availability** across separate locations. |
| **AWS Auto Scaling** | Automatically adjusts compute capacity to match current demand and maintain performance. | Choose when a workload has **variable or unpredictable traffic** and must scale out or in automatically while controlling cost. |

**3. Exam Keywords & Common Traps**

- **Trigger Keywords:**
  - “Deploy close to customers,” “global users,” or “lower latency” -> **AWS Global Infrastructure / select an appropriate Region**
  - “Fault tolerance,” “resiliency,” or “survive a data-center failure” -> **Use multiple Availability Zones**
  - “Automatically add or remove capacity,” “demand fluctuates,” or “scale based on load” -> **AWS Auto Scaling**
  - “Avoid upfront hardware investment” or “pay only for what you use” -> **OpEx and cloud consumption model**
- **Common Traps:**
  - **Region != Availability Zone:** A Region is a geographic area; an AZ is an isolated location within a Region.
  - **High availability != elasticity:** HA focuses on continued operation; elasticity focuses on matching capacity to demand.
  - Auto Scaling does not automatically mean global deployment; it adjusts capacity for a workload.
  - Elasticity is not simply permanently overprovisioning resources.

**4. 60-Second Cheatsheet Summary**

- AWS replaces much **CapEx** with usage-based **OpEx**.
- Global infrastructure enables **speed, worldwide reach, lower latency, and resilience**.
- **High availability** uses independent locations; **elasticity** dynamically matches capacity to demand.
- **AWS Auto Scaling = automatic capacity adjustment** for changing workloads and cost-efficient performance.

---

### Task Statement 1.2: Identify design principles of the AWS Cloud

**1. Core Concepts & Business Value**

- The **AWS Well-Architected Framework (WAF)** helps evaluate workloads against AWS best practices and improve decisions over time.
- AWS Cloud design emphasizes:
  - **Trade CapEx for OpEx:** Replace large upfront data-center investments with pay-as-you-go operating expenses.
  - **Agility:** Provision resources quickly instead of waiting for hardware procurement.
  - **Elasticity:** Automatically scale resources up or down as demand changes.
  - **Global reach:** Deploy workloads across AWS **Regions** and **Availability Zones**.
  - **Managed services:** Reduce undifferentiated infrastructure-management work.
  - **Automation and measured usage:** Use monitoring, automation, and right-sizing to improve efficiency.
- The six Well-Architected pillars provide different lenses; a workload can optimize one pillar while creating trade-offs in another.

**2. In-Scope Services & Key Functions**

| Service / Feature | Primary Function | Exam Use Case |
| :--- | :--- | :--- |
| **AWS Well-Architected Tool** | Cloud-based tool used to review workloads against the six Well-Architected Framework pillars and identify risks and improvement opportunities. | Choose it when a scenario asks to **assess, review, document, or improve** a workload’s architecture using AWS best practices. |

**Well-Architected Framework Pillars**

| Pillar | Primary Focus |
| :--- | :--- |
| **Operational Excellence** | Run and monitor workloads effectively; continually improve processes and procedures. |
| **Security** | Protect information, systems, and assets through risk assessment and security controls. |
| **Reliability** | Recover from failures and meet demand consistently; includes resilient, fault-tolerant design. |
| **Performance Efficiency** | Use computing resources efficiently and select appropriate technologies as requirements change. |
| **Cost Optimization** | Avoid unnecessary costs and deliver business value at the lowest effective price. |
| **Sustainability** | Minimize environmental impacts, especially energy consumption and resource usage. |

**3. Exam Keywords & Common Traps**

- **Trigger Keywords:** “Well-Architected review,” “architecture assessment,” “identify risks,” “pillar-based review,” “improvement plan” -> **AWS Well-Architected Tool**.
- **Common Traps:**
  - **Operational Excellence** is not the same as **Reliability**: operations and continual improvement versus recovery and resilience.
  - **Performance Efficiency** is not **Cost Optimization**: resource effectiveness versus lowest appropriate cost.
  - **Security** protects workloads; **Sustainability** reduces environmental impact.
  - **Elasticity** means automatic capacity adjustment; **scalability** is the ability to handle growth.
  - The Tool provides recommendations; it does not automatically redesign or remediate workloads.

**4. 60-Second Cheatsheet Summary**

- Memorize all six pillars: **Operational Excellence, Security, Reliability, Performance Efficiency, Cost Optimization, Sustainability**.
- Use the **AWS Well-Architected Tool** for workload reviews and identifying risks.
- Distinguish pillars by their primary outcome: **operate, protect, recover, perform, save, sustain**.
- AWS cloud value: **pay-as-you-go, agility, elasticity, global reach, and reduced undifferentiated heavy lifting**.

---

### Task Statement 1.3: Understand the benefits of and strategies for migration to the AWS Cloud

**1. Core Concepts & Business Value**

- **Cloud adoption benefits:** Trade **CapEx for OpEx**, provision resources on demand, increase agility, scale globally, improve resilience, and reduce undifferentiated heavy lifting.
- **Elasticity vs. agility:** **Elasticity** automatically adds or removes resources as demand changes; **agility** enables faster experimentation and delivery.
- **AWS Cloud Adoption Framework (AWS CAF):** Guidance for organizing people, processes, and technology during cloud transformation.
  - **Business:** Improved revenue, business outcomes, and reduced business risk.
  - **People:** Workforce readiness, skills, and organizational change.
  - **Governance:** Portfolio, program, and risk management.
  - **Platform:** Cloud infrastructure, applications, and data foundations.
  - **Security:** Security, compliance, and risk controls.
  - **Operations:** Monitoring, management, and continual improvement.
- CAF supports **increased operational efficiency** and improved **environmental, social, and governance (ESG) performance**.
- **Common migration strategies (7 Rs):** Retire, retain, rehost, relocate, repurchase, replatform, and refactor/re-architect.
- **Database replication:** Continuously replicate data from a source database to AWS to reduce downtime during migration.

**2. In-Scope Services & Key Functions**

| Service / Feature | Primary Function | Exam Use Case |
| :--- | :--- | :--- |
| **AWS CAF** | Framework for planning and accelerating cloud adoption across six perspectives. | Organize a migration program and address people, process, technology, and business outcomes. |
| **AWS Application Discovery Service** | Collects information about on-premises servers, applications, and dependencies. | Discover inventory and dependencies before migration planning. |
| **AWS Application Migration Service (MGN)** | Automatically lifts and shifts physical, virtual, or cloud servers to AWS. | **Rehost** applications with minimal changes. |
| **AWS DMS** | Migrates and replicates databases with minimal downtime. | Move databases or maintain ongoing replication during cutover. |
| **Migration Evaluator** | Provides data-driven assessment and recommendations for AWS migration costs. | Build a business case and estimate expected cloud costs. |
| **AWS Migration Hub** | Central location to track application migration progress across AWS and partner tools. | Monitor migration status across multiple applications and services. |
| **AWS SCT** | Converts database schemas and code between database engines. | **Convert** from one database engine to another before using DMS. |

**3. Exam Keywords & Common Traps**

- **Trigger Keywords:**
  - “Inventory,” “dependencies,” “on-premises discovery” -> **Application Discovery Service**
  - “Lift and shift” -> **Application Migration Service**
  - “Continuous database replication,” “minimal downtime” -> **AWS DMS**
  - “Schema conversion,” “different database engine” -> **AWS SCT**
  - “Migration cost estimate/business case” -> **Migration Evaluator**
  - “Central migration tracking” -> **Migration Hub**
  - “Six perspectives/cloud transformation guidance” -> **AWS CAF**
- **Common Traps:**
  - **SCT converts schemas; DMS migrates/replicates data.**
  - **MGN migrates servers; DMS migrates databases.**
  - Migration Hub tracks progress; it does not perform the migration.
  - CAF is a guidance framework, not a migration execution service.

**4. 60-Second Cheatsheet Summary**

- Use **Discovery -> Evaluation -> Migration -> Tracking** to map common migration tooling.
- **MGN = servers**, **DMS = databases**, **SCT = schema conversion**.
- **Migration Evaluator** supports financial justification; **Migration Hub** provides centralized status.
- AWS CAF aligns migration with business value, workforce readiness, governance, platform, security, and operations.

---

### Task Statement 1.4: Understand concepts of cloud economics

**1. Core Concepts & Business Value**

- **CapEx -> OpEx:** Cloud shifts large upfront investments in data centers, hardware, and facilities (**capital expenditure**) to pay-as-you-go usage (**operational expenditure**).
- **Fixed vs. variable costs:**
  - **Fixed:** Costs remain relatively constant regardless of utilization, such as owned facilities, hardware, and long-term infrastructure contracts.
  - **Variable:** Costs change with consumption, such as compute hours, storage, and data transfer.
- **On-premises costs:** Hardware purchase and refresh, data-center space, power, cooling, physical security, maintenance, software licensing, support contracts, and IT labor.
- **Cost savings:** Avoid overprovisioning, reduce maintenance, pay only for consumed resources, and benefit from AWS purchasing at massive scale.
- **Economies of scale:** AWS aggregates demand across customers, gaining lower hardware, power, and operating costs that can be reflected in cloud pricing.
- **Rightsizing:** Select resource types and sizes that match actual workload requirements. Analyze utilization and adjust overprovisioned or underutilized resources.
- **Automation benefits:** Reduces manual labor, configuration errors, and idle resources; improves repeatability and enables rapid scaling.
- **Agility and elasticity:** Provision resources quickly and scale capacity up or down with demand, avoiding permanent capacity for peak workloads.
- **Licensing strategies:**
  - **BYOL:** Customer supplies an eligible existing software license; may reduce license costs but can involve eligibility and licensing restrictions.
  - **License included:** AWS service pricing includes the applicable software license; simpler procurement and license management.

**2. In-Scope Services & Key Functions**

| Service / Feature | Primary Function | Exam Use Case |
| :--- | :--- | :--- |
| **AWS Pricing Calculator** | Estimates AWS costs for planned architectures and workloads. | Compare design options or estimate costs before deployment. |
| **AWS Cost Explorer** | Visualizes, analyzes, and reports historical and current AWS spending and usage. | Identify spending trends, cost drivers, or optimization opportunities. |
| **AWS Budgets** | Creates customized cost or usage budgets and sends alerts when thresholds are reached or forecast. | Monitor spending and receive proactive budget notifications. |

**3. Exam Keywords & Common Traps**

- **Trigger Keywords:** “estimate before deployment” -> **Pricing Calculator**; “analyze spending trends/history” -> **Cost Explorer**; “threshold,” “alert,” or “forecast exceeds budget” -> **AWS Budgets**; “match capacity to utilization” -> **rightsizing**; “existing software license” -> **BYOL**.
- **Common Traps:**
  - Cloud is not automatically cheaper; savings depend on architecture, utilization, and optimization.
  - **Rightsizing** is not simply choosing the smallest instance; it means matching resources to workload demand.
  - **Cost Explorer** analyzes costs; **Budgets** monitors against targets; **Pricing Calculator** estimates future costs.
  - Variable cloud costs can still become high through idle or overprovisioned resources.

**4. 60-Second Cheatsheet Summary**

- Cloud economics trades **CapEx for variable OpEx** and reduces data-center ownership costs.
- AWS economies of scale, automation, elasticity, and rightsizing can reduce total cost.
- Choose **Pricing Calculator** for estimates, **Cost Explorer** for analysis, and **Budgets** for alerts.
- Know the difference between **BYOL** and **license-included** pricing.

---

## Domain 2: Security and Compliance (30%)

### Task Statement 2.1: Understand the AWS shared responsibility model

**1. Core Concepts & Business Value**

- The model divides security and compliance duties between **AWS** and the **customer**.
- **AWS security *of* the cloud:** AWS protects the infrastructure that runs AWS services—data centers, hardware, networking, physical facilities, and foundational services.
- **Customer security *in* the cloud:** Customers protect their data, identities, applications, configurations, operating systems, network controls, and access permissions.
- Responsibilities **shift by service abstraction**:
  - More customer control (such as EC2) means more customer security responsibility.
  - More AWS-managed infrastructure (such as Lambda) reduces infrastructure responsibility for the customer.
- Customers remain responsible for **proper configuration**, even when AWS operates the underlying service.
- The model supports cloud benefits such as **reduced infrastructure CapEx**, faster deployment, elasticity, and global reach—but does **not** eliminate customer security obligations.
- Some controls are shared, including **patch management, configuration management, awareness and training, and security monitoring**, with the exact split depending on the service.

**2. In-Scope Services & Key Functions**

| Service / Feature | Primary Function | Exam Use Case |
| :--- | :--- | :--- |
| **AWS Shared Responsibility Framework** | Defines which security and compliance tasks AWS performs and which tasks the customer performs. | Use to determine responsibility for infrastructure, data, IAM, patching, and configuration. |
| **Amazon EC2** | Provides virtual servers with customer-controlled operating systems and applications. | Customer manages the guest OS, patches, installed software, security groups, and data; AWS manages physical infrastructure. |
| **Amazon RDS** | Provides managed relational databases, including underlying infrastructure and database software maintenance. | AWS manages the host and much of the database platform; customer manages data, access, encryption choices, and database configuration. |
| **AWS Lambda** | Runs customer code without requiring server provisioning or management. | AWS manages servers, OS, runtime infrastructure, and scaling; customer secures code, dependencies, permissions, and data. |

**3. Exam Keywords & Common Traps**

- **Trigger Keywords:** “security *of* the cloud” -> AWS; “security *in* the cloud” -> customer; “physical data center security” -> AWS; “IAM users/permissions,” “data encryption,” or “resource configuration” -> customer.
- **Common Traps:**
  - AWS responsibility does **not** mean AWS secures customer data, identities, or configurations automatically.
  - **EC2:** customers patch and secure the guest OS.
  - **RDS/Lambda:** AWS manages more of the platform, but customers still secure data, code, IAM, and settings.
  - Moving to a managed service changes—not removes—customer responsibility.
  - Shared responsibility is **not** a complete transfer of risk or compliance obligations to AWS.

**4. 60-Second Cheatsheet Summary**

- **AWS = security of the cloud; customer = security in the cloud.**
- AWS protects physical facilities, hardware, networking, and managed-service infrastructure.
- Customers protect data, IAM, applications, configurations, and permissions.
- **EC2 -> most customer responsibility; RDS -> shared; Lambda -> least infrastructure responsibility, but code/data/IAM remain customer responsibilities.**

---

### Task Statement 2.2: Understand AWS Cloud security, governance, and compliance concepts

**1. Core Concepts & Business Value**

- **Shared responsibility:** AWS secures the infrastructure *of* the cloud; customers secure data, identities, configurations, and workloads *in* the cloud.
- **Compliance:** Requirements vary by **industry, country/Region, and AWS service**. Customers must verify that their architecture and selected services meet applicable requirements.
- **AWS Artifact:** Self-service portal for AWS compliance reports, certifications, and agreements.
- **Encryption:**  
  - **In transit:** Protects data moving between systems, commonly using TLS/HTTPS.  
  - **At rest:** Protects stored data; **AWS KMS** creates and manages encryption keys.
- **Governance:** Centralize accounts, policies, guardrails, configuration standards, and audit evidence.
- **Security operations:** Detect vulnerabilities, threats, suspicious activity, and configuration drift; retain logs for investigation and compliance.

**2. In-Scope Services & Key Functions**

| Service / Feature | Primary Function | Exam Use Case |
| :--- | :--- | :--- |
| **AWS Artifact** | Provides AWS compliance reports and agreements. | Find certifications or compliance documentation. |
| **Amazon Inspector** | Continuously assesses workloads for software vulnerabilities and unintended network exposure. | Identify vulnerabilities in supported compute resources. |
| **AWS Security Hub** | Centralizes and prioritizes security findings and compliance checks. | Obtain a consolidated security posture view. |
| **Amazon GuardDuty** | Threat-detection service analyzing AWS data sources for malicious or suspicious activity. | Detect compromised accounts, unusual API activity, or threats. |
| **AWS Shield** | Managed DDoS protection. | Protect applications from network and application-layer DDoS attacks. |
| **Amazon CloudWatch** | Collects and monitors metrics, logs, and events. | Monitor resources and centralize operational/security logs. |
| **AWS CloudTrail** | Records AWS account activity and API calls. | Audit *who did what, when, and from where*; deliver logs to S3/CloudWatch Logs. |
| **AWS Config** | Records resource configurations and evaluates compliance with rules. | Detect configuration changes, drift, and noncompliant resources. |
| **AWS KMS** | Creates and controls encryption keys. | Manage keys for encryption at rest and service integrations. |
| **AWS Organizations** | Centrally manages multiple AWS accounts, policies, and consolidated billing. | Apply governance across accounts. |
| **AWS Control Tower** | Automates a governed, multi-account AWS environment using landing zones and guardrails. | Establish compliant account structures and controls. |

**3. Exam Keywords & Common Traps**

- **Trigger Keywords:** “compliance reports” -> Artifact; “vulnerability assessment” -> Inspector; “centralized findings” -> Security Hub; “threat detection” -> GuardDuty; “DDoS” -> Shield; “API activity” -> CloudTrail; “configuration compliance/drift” -> Config; “encryption keys” -> KMS; “multi-account guardrails” -> Organizations/Control Tower.
- **Common Traps:** CloudTrail records API activity; CloudWatch monitors metrics/logs. **Inspector** finds vulnerabilities; **GuardDuty** detects threats. Artifact provides AWS evidence—it does not make a workload compliant. Encryption does not replace access control. Compliance responsibility remains shared.

**4. 60-Second Cheatsheet Summary**

- **Artifact = evidence; KMS = keys; CloudTrail = audit; Config = configuration compliance.**
- **GuardDuty detects threats; Inspector finds vulnerabilities; Security Hub aggregates findings; Shield mitigates DDoS.**
- **CloudWatch monitors metrics, logs, and events.**
- Compliance depends on the **service, location, industry, and customer configuration**.

---

### Task Statement 2.3: Identify AWS access management capabilities

**1. Core Concepts & Business Value**

- **IAM** controls authentication (who) and authorization (what actions, on which resources).
- Apply **least privilege**: grant only required permissions, for only as long as needed.
- **Root user** has unrestricted account access. Protect it with a strong password, **MFA**, no access keys, and limited use.
- Prefer **IAM roles and temporary credentials** over long-term access keys.
- **IAM users** represent people or applications; **groups** organize users; **policies** define permissions.
- **Managed policies** are AWS- or customer-maintained reusable policies; **custom/inline policies** provide tailored permissions.
- **Password policies** enforce requirements such as length, complexity, expiration, and reuse prevention.
- **Federated access** lets users authenticate through an external identity provider and obtain temporary AWS credentials.
- **IAM Identity Center** provides centralized workforce access to multiple AWS accounts and applications using permission sets.
- Store credentials and secrets securely; never hard-code access keys in source code or applications.

**2. In-Scope Services & Key Functions**

| Service / Feature | Primary Function | Exam Use Case |
| :--- | :--- | :--- |
| **AWS IAM** | Manages AWS identities, authentication credentials, and permissions. | Create users, groups, roles, policies, MFA, password policies, and access keys. |
| **IAM Identity Center** | Centrally manages workforce identities and access across AWS accounts and applications. | Give employees single sign-on and account access through permission sets. |
| **AWS Account Root User** | The original account identity with complete access to all AWS resources and account settings. | Perform root-only tasks; otherwise avoid routine use. |
| **AWS Secrets Manager** | Securely stores, retrieves, and rotates secrets such as database credentials and API keys. | Protect application secrets without embedding them in code. |
| **AWS Systems Manager** | Provides operational management, including Parameter Store for configuration data and secure parameters. | Store and retrieve application configuration or credentials using managed parameters. |

**3. Exam Keywords & Common Traps**

- **Trigger Keywords:**
  - “Centralized workforce access,” “single sign-on,” “multiple AWS accounts” -> **IAM Identity Center**
  - “Temporary credentials,” “cross-account access” -> **IAM role**
  - “Long-term programmatic access” -> **access key** (protect and rotate)
  - “Rotate database password/API key” -> **Secrets Manager**
  - “Configuration values/secure parameters” -> **Systems Manager Parameter Store**
  - “Original account identity,” “close account,” “change certain account settings” -> **root user**
- **Common Traps:**
  - Root user is **not** the same as an IAM administrator.
  - IAM policies grant permissions; **MFA authenticates** the identity but does not grant permissions.
  - Groups contain users, not roles; roles are assumed and provide temporary credentials.
  - Do not store secrets in code, plaintext files, or access-key variables.
  - Cross-account access normally uses a **role**, not shared IAM user credentials.

**4. 60-Second Cheatsheet Summary**

- Secure root: **MFA, no access keys, minimal use**.
- Use **least privilege**, IAM roles, and temporary credentials.
- **Identity Center** = centralized workforce SSO; **IAM** = identities and permissions.
- **Secrets Manager** protects and rotates secrets; **Systems Manager Parameter Store** stores configuration and secure parameters.

---

### Task Statement 2.4: Identify components and resources for security

**1. Core Concepts & Business Value**

- **Shared responsibility:** AWS secures the cloud infrastructure; customers secure data, identities, configurations, and workloads in the cloud.
- AWS provides managed security capabilities that improve **agility**, reduce operational overhead, and replace much security infrastructure **CapEx with OpEx**.
- Use layered security: preventive controls, detection, investigation, and response.
- **AWS security information:** AWS Knowledge Center (troubleshooting), AWS Security Center (security guidance/resources), and AWS Security Blog (best practices and updates).
- **AWS Marketplace:** Source third-party security products, such as firewalls, vulnerability scanners, and monitoring tools.
- **AWS Trusted Advisor:** Identifies security, performance, cost, fault-tolerance, and service-limit issues using best-practice checks.

**2. In-Scope Services & Key Functions**

| Service / Feature | Primary Function | Exam Use Case |
| :--- | :--- | :--- |
| **AWS WAF** | Filters and monitors HTTP(S) requests using web ACL rules. | Block SQL injection, cross-site scripting, or unwanted IPs. |
| **AWS Firewall Manager** | Centrally configures and manages firewall rules across accounts/resources. | Enforce organization-wide WAF or Shield policies. |
| **AWS Shield** | Managed DDoS protection; Standard is automatic, Advanced adds enhanced protection. | Protect applications from network and application-layer DDoS. |
| **Amazon GuardDuty** | Threat-detection service analyzing AWS logs and activity. | Identify compromised accounts, instances, or suspicious behavior. |
| **AWS Marketplace** | Catalog for purchasing third-party software and security products. | Obtain specialized security tools not provided natively by AWS. |
| **AWS Trusted Advisor** | Provides recommendations and checks against AWS best practices. | Find security weaknesses, exposed resources, or weak configurations. |
| **AWS Certificate Manager (ACM)** | Provisions, manages, and renews SSL/TLS certificates. | Enable HTTPS/TLS for integrated AWS services. |
| **AWS CloudHSM** | Provides dedicated, customer-controlled hardware security modules. | Meet strict key-control or regulatory requirements. |
| **Amazon Cognito** | Provides user sign-up, sign-in, and access control for applications. | Add customer identity and authentication to web/mobile apps. |
| **Amazon Detective** | Analyzes security data to investigate and determine root cause. | Investigate GuardDuty findings and suspicious activity. |
| **AWS Directory Service** | Provides managed directory services, including Microsoft Active Directory. | Support domain authentication and directory-aware applications. |
| **Amazon Macie** | Discovers and protects sensitive data, especially in Amazon S3. | Identify personally identifiable information (PII) and data exposure. |
| **AWS RAM** | Shares supported AWS resources across accounts or Organizations. | Centrally share resources without duplicating them. |

**3. Exam Keywords & Common Traps**

- **Trigger Keywords:** “web requests/SQL injection” -> WAF; “centralized policies across accounts” -> Firewall Manager; “DDoS” -> Shield; “threat findings” -> GuardDuty; “investigate/root cause” -> Detective; “sensitive data/PII in S3” -> Macie; “TLS certificate” -> ACM; “dedicated key hardware” -> CloudHSM.
- **Common Traps:** GuardDuty detects; Detective investigates. WAF filters Layer 7 traffic; Shield mitigates DDoS. ACM manages certificates but is not a general key-management/HSM service. CloudHSM provides dedicated hardware control. Trusted Advisor recommends; it does not automatically remediate every issue.

**4. 60-Second Cheatsheet Summary**

- **Prevent:** WAF, Shield, Firewall Manager, ACM, CloudHSM.
- **Detect:** GuardDuty, Macie, Trusted Advisor.
- **Investigate:** Detective.
- **Identity/resources:** Cognito, Directory Service, RAM; third-party tools come from Marketplace.

---

## Domain 3: Cloud Technology and Services (34%)

### Task Statement 3.1: Define methods of deploying and operating in the AWS Cloud

**1. Core Concepts & Business Value**

- **Cloud deployment models:**
  - **Cloud:** Workloads run fully in AWS.
  - **On-premises:** Workloads run in an organization’s own facilities.
  - **Hybrid:** Connected combination of on-premises infrastructure and AWS.
- **Provisioning and operating options:**
  - **AWS Management Console:** Web-based, visual access; best for learning, exploration, and one-time manual operations.
  - **AWS CLI:** Command-line, programmatic access; useful for scripting and repeatable administration.
  - **AWS SDKs:** Language-specific libraries for calling AWS APIs from applications and automation.
  - **Infrastructure as Code (IaC):** Define infrastructure in templates so it can be consistently, repeatedly, and version-controlled deployed.
- **One-time vs. repeatable operations:**
  - Use the **Console** for occasional or experimental changes.
  - Use **CLI, SDKs, or IaC** for repeatable, automated, auditable processes.
- Cloud adoption can trade **up-front CapEx** for variable **OpEx**, increase agility, provide elasticity, and enable global deployment without building physical data centers.

**2. In-Scope Services & Key Functions**

| Service / Feature | Primary Function | Exam Use Case |
| :--- | :--- | :--- |
| **AWS Management Console** | Browser-based graphical interface for accessing and managing AWS services. | Manually create, configure, monitor, or troubleshoot resources. |
| **AWS CLI** | Command-line tool for interacting with AWS services through commands and scripts. | Automate repeatable tasks or manage resources without the console. |
| **AWS SDKs** | Software development libraries that provide programmatic access to AWS services and APIs. | Build applications or custom automation that interacts with AWS. |
| **AWS CloudFormation** | IaC service that provisions and manages related AWS resources from templates. | Deploy consistent, repeatable infrastructure across environments or Regions. |
| **AWS Elastic Beanstalk** | Managed service that deploys and operates applications while handling infrastructure provisioning and management. | Quickly deploy supported applications without managing the underlying infrastructure directly. |
| **AWS Systems Manager** | Service for viewing, controlling, automating, and operating AWS and hybrid managed nodes. | Centralize operational tasks such as commands, patching, automation, and parameter management. |

**3. Exam Keywords & Common Traps**

- **Trigger Keywords:**
  - “Graphical interface” / “web browser” -> **Management Console**
  - “Command line” / “shell script” -> **AWS CLI**
  - “Application code” / “programmatic access” -> **AWS SDKs**
  - “Template” / “infrastructure as code” / “repeatable deployment” -> **CloudFormation**
  - “Deploy application without managing servers” -> **Elastic Beanstalk**
  - “Patch, run commands, automate operational tasks, hybrid nodes” -> **Systems Manager**
  - “AWS plus data center” -> **Hybrid deployment**
- **Common Traps:**
  - Console operations are generally manual; **IaC is repeatable and consistent**.
  - **SDKs** are libraries used in code; the **CLI** is command-line based.
  - Elastic Beanstalk deploys applications; CloudFormation defines and provisions broader infrastructure.
  - Hybrid means **both AWS and on-premises**, not simply multiple AWS Regions.

**4. 60-Second Cheatsheet Summary**

- **Console = visual/manual; CLI = commands/scripts; SDK = application code; CloudFormation = IaC.**
- Choose **repeatable automation** over manual actions for consistency and scale.
- **Elastic Beanstalk** simplifies application deployment; **Systems Manager** simplifies operations.
- Deployment models are **cloud, on-premises, and hybrid**.

---

### Task Statement 3.2: Define the AWS global infrastructure

**1. Core Concepts & Business Value**

- **AWS Region:** A separate geographic area containing multiple, isolated Availability Zones.
- **Availability Zone (AZ):** One or more discrete data centers with independent power, networking, and connectivity within a Region.
- **Edge location:** AWS site positioned close to end users to deliver content and services with lower latency.
- **High availability (HA):** Design applications across **multiple AZs** so an AZ failure does not interrupt service.
- **No shared single point of failure:** AZs are physically separate and do not share critical infrastructure such as power, cooling, or networking.
- **Multiple Regions** can provide:
  - **Disaster recovery (DR)** and business continuity if an entire Region becomes unavailable.
  - Lower latency for globally distributed users.
  - **Data sovereignty** by keeping data in a required geographic location.
- Edge infrastructure improves global reach and responsiveness without requiring applications to run entirely in every user’s location.

**2. In-Scope Services & Key Functions**

| Service / Feature | Primary Function | Exam Use Case |
| :--- | :--- | :--- |
| **AWS Regions** | Geographic areas containing multiple isolated AZs. | Choose for data residency, regional deployment, DR, or reducing user latency. |
| **Availability Zones** | Isolated locations within a Region with independent infrastructure. | Deploy across multiple AZs for high availability and fault tolerance. |
| **Edge Locations** | Sites near users that cache or deliver content and provide low-latency access. | Choose when users are geographically distributed or content must be delivered quickly. |
| **AWS Local Zones** | Extensions of AWS Regions placed near large population or industry centers. | Use for single-digit-millisecond latency to local users or on-premises applications. |
| **AWS Wavelength** | AWS infrastructure embedded within telecommunications providers’ 5G networks. | Use for ultra-low-latency applications connected to 5G mobile devices. |

**3. Exam Keywords & Common Traps**

- **Trigger Keywords:**
  - “Multiple isolated data centers” -> **Availability Zones**
  - “Separate geographic area” or “data sovereignty” -> **Region**
  - “Cache content close to users” -> **Edge location**
  - “Single-digit millisecond latency in a metro area” -> **Local Zones**
  - “5G mobile applications” or “telecommunications network” -> **Wavelength**
  - “Survive data center failure” -> **Multiple AZs**
  - “Survive an entire regional outage” -> **Multiple Regions**
- **Common Traps:**
  - A **Region is not an AZ**; a Region contains multiple AZs.
  - Edge locations are **not** Availability Zones.
  - One AZ does not provide the same resilience as multiple AZs.
  - Multiple AZs protect against localized failures; **multiple Regions** address regional disasters, sovereignty, or global latency.

**4. 60-Second Cheatsheet Summary**

- **Region = geographic area; AZ = isolated location inside a Region.**
- Use **multiple AZs** for high availability and no shared infrastructure failure.
- Use **multiple Regions** for DR, business continuity, data sovereignty, or global latency.
- **Edge Locations = content close to users; Local Zones = regional low latency; Wavelength = 5G edge computing.**

---

### Task Statement 3.3: Identify AWS compute services

**1. Core Concepts & Business Value**

- **Cloud compute:** Rent compute capacity instead of purchasing servers—trades **CapEx for variable OpEx** and improves agility.
- **Elasticity:** Automatically scale resources **out/in** or **up/down** as demand changes; avoid overprovisioning.
- **EC2 instance selection:** Match instance family to workload:
  - **General purpose:** Balanced compute, memory, and networking.
  - **Compute optimized:** CPU-intensive workloads, batch processing, high-performance web servers.
  - **Memory optimized:** Large in-memory datasets and caching.
  - **Storage optimized:** High sequential/random I/O and local storage needs.
- **Containers:** Package applications and dependencies consistently. **ECS** uses AWS-native orchestration; **EKS** provides managed Kubernetes.
- **Serverless compute:** AWS manages servers, provisioning, and much of the scaling. **Lambda** runs code; **Fargate** runs containers.
- **Load balancing:** Distributes incoming traffic across healthy targets, improving availability and fault tolerance.

**2. In-Scope Services & Key Functions**

| Service / Feature | Primary Function | Exam Use Case |
| :--- | :--- | :--- |
| **Amazon EC2** | Resizable virtual servers in the AWS Cloud. | Maximum control over OS, instance type, networking, and storage. |
| **AWS Lambda** | Runs code in response to events without managing servers. | Short-duration, event-driven, variable workloads; pay per use. |
| **Amazon ECS** | Fully managed container orchestration service. | Run and manage Docker containers using AWS-native tooling. |
| **Amazon EKS** | Managed Kubernetes control plane. | Use Kubernetes APIs, tools, and portability. |
| **AWS Fargate** | Serverless compute engine for containers. | Run ECS/EKS containers without managing EC2 instances. |
| **Amazon Lightsail** | Simplified virtual private server service with predictable pricing. | Small websites, blogs, and simple applications. |
| **AWS Batch** | Runs batch computing jobs at scale and provisions required resources. | Queue-based, scheduled, or large-volume batch workloads. |
| **AWS Outposts** | AWS infrastructure and services deployed on-premises. | Low latency, local processing, or data residency with hybrid AWS operations. |
| **AWS Auto Scaling** | Automatically adjusts capacity to maintain performance and optimize cost. | Match resources to demand; provide elasticity. |
| **Elastic Load Balancing (ELB)** | Distributes traffic across targets such as EC2 instances and containers. | Improve availability, scalability, and fault tolerance. |

**3. Exam Keywords & Common Traps**

- **Trigger Keywords:** “virtual server/control” -> **EC2**; “event-driven/no servers” -> **Lambda**; “containers/no servers to manage” -> **Fargate**; “Kubernetes” -> **EKS**; “simple VPS” -> **Lightsail**; “batch jobs/queue” -> **AWS Batch**; “on-premises AWS” -> **Outposts**; “distribute traffic/healthy targets” -> **ELB**; “automatically match demand” -> **Auto Scaling**.
- **Common Traps:** **Fargate is not a container orchestrator**; ECS/EKS orchestrate containers. Lambda is not suited to continuously running workloads or long-running processes. Auto Scaling changes capacity; ELB distributes traffic. Compute-optimized means CPU—not high storage performance.

**4. 60-Second Cheatsheet Summary**

- **EC2 = control; Lambda = functions; Fargate = serverless containers.**
- **ECS = AWS-native containers; EKS = Kubernetes.**
- **Auto Scaling = elasticity; ELB = traffic distribution and availability.**
- Choose instance families by bottleneck: **compute, memory, or storage**.

---

### Task Statement 3.4: Identify AWS database services

**1. Core Concepts & Business Value**

- **Managed databases** shift operational responsibility to AWS: provisioning, patching, backups, monitoring, and infrastructure maintenance.
- Compared with hosting a database on **Amazon EC2**, managed services improve agility and reduce administration; EC2 provides maximum OS/database control but requires customer-managed patching, backups, scaling, and high availability.
- Cloud databases trade **up-front CapEx for usage-based OpEx**, support elasticity, and can improve availability through Multi-AZ deployments and replication.
- **Relational databases** use tables, schemas, SQL, and transactions; choose for structured data and strong consistency.
- **NoSQL databases** support flexible schemas and highly scalable access patterns without traditional relational joins.
- **In-memory databases** provide very low-latency reads and are commonly used for caching, sessions, and real-time applications.
- **Database migration:** AWS DMS moves data; AWS SCT converts database schemas and code when migrating between unlike engines.

**2. In-Scope Services & Key Functions**

| Service / Feature | Primary Function | Exam Use Case |
| :--- | :--- | :--- |
| **Amazon RDS** | Managed relational database service supporting engines such as MySQL, PostgreSQL, MariaDB, Oracle, and SQL Server. | Need SQL, transactions, automated backups, patching, and managed high availability. |
| **Amazon Aurora** | AWS-built, cloud-optimized relational database compatible with MySQL and PostgreSQL. | Need higher performance, availability, and scalability than standard RDS engines. |
| **Amazon DynamoDB** | Fully managed, serverless NoSQL key-value and document database with single-digit-millisecond performance. | Need massive scale, flexible schema, and predictable low-latency access. |
| **Amazon ElastiCache** | Managed in-memory caching using Redis or Memcached. | Need to reduce database load and provide microsecond/millisecond-latency access. |
| **Amazon DocumentDB** | Managed document database compatible with MongoDB workloads. | Need JSON-like document storage and flexible schema. |
| **Amazon Neptune** | Managed graph database for highly connected data and relationship queries. | Use for knowledge graphs, recommendation engines, or fraud networks. |
| **AWS DMS** | Managed service for migrating and replicating databases with minimal downtime. | Ongoing replication or migration from source to target database. |
| **AWS SCT** | Converts schemas and database code between different database engines. | Heterogeneous migration, such as Oracle/SQL Server to PostgreSQL or Aurora. |

**3. Exam Keywords & Common Traps**

- **Trigger Keywords:** “SQL/transactions” -> RDS or Aurora; “MySQL/PostgreSQL-compatible, cloud-native” -> Aurora; “key-value,” “serverless,” “single-digit millisecond” -> DynamoDB; “cache/session data” -> ElastiCache; “documents/JSON/MongoDB compatibility” -> DocumentDB; “relationships/graph” -> Neptune; “continuous replication/minimal downtime” -> DMS; “convert schema/code” -> SCT.
- **Common Traps:**
  - DMS **moves data**; SCT **converts schemas/code**—they may be used together.
  - ElastiCache is a **cache**, not the primary durable database.
  - RDS is managed, but customers still manage database configuration, users, and some tuning.
  - Choose EC2-hosted databases only when unusual engine, OS, or administrative control is required.

**4. 60-Second Cheatsheet Summary**

- **RDS/Aurora = relational; DynamoDB = NoSQL; ElastiCache = in-memory.**
- **DocumentDB = documents; Neptune = graphs.**
- **DMS migrates/replicates data; SCT converts schemas/code.**
- Prefer managed services for reduced operations; use EC2 when maximum control or unsupported requirements matter.

---

### Task Statement 3.5: Identify AWS network services

**1. Core Concepts & Business Value**

- **Amazon VPC:** Logically isolated virtual network in an AWS **Region**; choose IP ranges, subnets, route tables, and gateways.
- **Subnets:** Subnet belongs to one **Availability Zone**. Public subnets route to an **Internet Gateway (IGW)**; private subnets do not.
- **NAT Gateway:** Allows private-subnet resources to make outbound internet connections; blocks unsolicited inbound connections.
- **Security groups:** Stateful, instance/ENI-level virtual firewalls; allow rules only.
- **Network ACLs (NACLs):** Stateless, subnet-level firewalls; support allow and deny rules, evaluated in rule-number order.
- **Amazon Inspector:** Finds software vulnerabilities and unintended network exposure; it is **not** a traffic-filtering firewall.
- Cloud networking enables global reach, agility, and elasticity while replacing much networking **CapEx** with usage-based **OpEx**.

**2. In-Scope Services & Key Functions**

| Service / Feature | Primary Function | Exam Use Case |
| :--- | :--- | :--- |
| **Amazon VPC** | Isolated virtual network with subnets, routes, and gateways. | Design AWS network boundaries and connectivity. |
| **Amazon Route 53** | Highly available DNS and domain service. | Route users to resources using DNS, health checks, and routing policies. |
| **AWS Direct Connect** | Dedicated private network connection to AWS. | Consistent, high-bandwidth hybrid connectivity; not encrypted by default. |
| **AWS Site-to-Site VPN** | Encrypted IPsec tunnels between networks over the internet. | Connect an on-premises network to a VPC quickly. |
| **AWS Client VPN** | Managed client-based VPN for remote users. | Secure employee access to AWS and on-premises resources. |
| **AWS VPN** | AWS-managed VPN connectivity, including Site-to-Site and Client VPN. | Select encrypted remote or network-to-network access. |
| **Amazon CloudFront** | Global content delivery network using edge locations and caching. | Reduce latency for websites, media, and APIs. |
| **AWS Transit Gateway** | Regional network transit hub. | Hub-and-spoke connectivity across many VPCs and on-premises networks. |
| **Amazon API Gateway** | Managed service for creating, publishing, securing, and monitoring APIs. | Expose REST, HTTP, or WebSocket APIs. |
| **AWS PrivateLink** | Private access to services through VPC interface endpoints. | Consume AWS, SaaS, or partner services without internet traversal. |
| **AWS Global Accelerator** | Uses static anycast IPs and the AWS global network. | Improve availability and performance for TCP/UDP applications. |

**3. Exam Keywords & Common Traps**

- **Trigger Keywords:** “dedicated private connection” -> Direct Connect; “encrypted tunnel over internet” -> Site-to-Site VPN; “remote employees” -> Client VPN; “DNS” -> Route 53; “cache at edge” -> CloudFront; “static anycast IP” -> Global Accelerator; “many VPCs hub” -> Transit Gateway; “private service endpoint” -> PrivateLink.
- **Common Traps:** Security groups are **stateful**; NACLs are **stateless**. Direct Connect is private but **not automatically encrypted**. CloudFront caches content; Global Accelerator generally does not. A subnet is tied to one AZ; a VPC spans a Region.

**4. 60-Second Cheatsheet Summary**

- **SG = stateful instance firewall; NACL = stateless subnet firewall.**
- **Direct Connect = dedicated; VPN = encrypted over internet.**
- **CloudFront = cached content; Global Accelerator = faster application traffic.**
- **Route 53 = DNS; Transit Gateway = VPC hub; PrivateLink = private service access.**

---

### Task Statement 3.6: Identify AWS storage services

**1. Core Concepts & Business Value**

- **Object storage:** Stores data as objects with metadata in buckets; highly scalable and accessed through APIs. Best for backups, media, logs, static websites, and data lakes.
- **Block storage:** Presents raw virtual disks to compute instances; suited to operating systems, databases, and applications requiring low-latency persistent disks.
- **File storage:** Shared hierarchical file systems accessed concurrently using standard file protocols.
- **Cached file systems:** Keep frequently accessed on-premises data locally while extending storage to AWS.
- **Lifecycle policies:** Automatically transition objects to lower-cost storage classes or expire/delete them based on age.
- **AWS Backup:** Centralizes and automates backups across supported AWS resources; supports retention, policy management, and recovery.
- **Cloud value:** Elastic capacity, global reach, durability, and pay-as-you-go **OpEx** instead of upfront **CapEx**.

**2. In-Scope Services & Key Functions**

| Service / Feature | Primary Function | Exam Use Case |
| :--- | :--- | :--- |
| **Amazon S3** | Durable, scalable object storage using buckets and objects. | Store backups, logs, media, static content, or data lakes. |
| **Amazon S3 Glacier** | Low-cost archival storage with retrieval options. | Long-term archives and compliance data accessed rarely. |
| **Amazon EBS** | Persistent block storage volumes attached to EC2 instances; AZ-scoped. | Boot volumes, databases, and applications needing block storage. |
| **Instance store** | Temporary, physically attached block storage. | High-speed temporary data, cache, or scratch space; data is lost when instance stops/terminates. |
| **Amazon EFS** | Fully managed, elastic shared NFS file system. | Shared Linux file storage across multiple AZs and instances. |
| **Amazon FSx** | Managed file systems for Windows, Lustre, NetApp ONTAP, and OpenZFS. | Specialized workloads requiring Windows SMB or high-performance file systems. |
| **AWS Storage Gateway** | Hybrid cloud storage connecting on-premises environments to AWS. | Cached files, volumes, or virtual tapes with cloud-backed storage. |
| **AWS Backup** | Centralized, policy-based backup and recovery service. | Automate backups, retention, and cross-account/Region protection. |
| **AWS Elastic Disaster Recovery** | Continuously replicates servers to AWS for recovery. | Minimize downtime and RPO/RTO during disasters. |

**3. Exam Keywords & Common Traps**

- **Trigger Keywords:** “object,” “bucket,” “static website” -> S3; “archive,” “retention,” “compliance” -> S3 Glacier; “attached disk,” “boot volume” -> EBS; “shared NFS” -> EFS; “SMB/Windows” -> FSx; “on-premises cache” -> Storage Gateway.
- **S3 classes:** Standard (frequent access), Intelligent-Tiering (unknown/changing access), Standard-IA (infrequent access, multi-AZ), One Zone-IA (infrequent, single AZ), Glacier Instant/Flexible/Deep Archive (archive with increasing retrieval delay and lower cost).
- **Common Traps:** EBS is not shared file storage; instance store is not persistent. EFS is primarily Linux/NFS; FSx provides specialized managed file systems. Lifecycle policies transition or expire S3 objects; they do not back up data.

**4. 60-Second Cheatsheet Summary**

- **S3 = objects; EBS = persistent blocks; EFS/FSx = shared files.**
- **Instance store is ephemeral; EBS survives instance stop.**
- **Glacier is for archival; lifecycle policies automate storage transitions and deletion.**
- **Storage Gateway is hybrid access; Backup protects resources; Elastic Disaster Recovery restores servers.**

---

### Task Statement 3.7: Identify AWS artificial intelligence and machine learning (AI/ML) services and analytics services

**1. Core Concepts & Business Value**

- **AI/ML services:** Use AWS-managed capabilities to build ML models, access foundation models, or add intelligence to applications without managing underlying infrastructure.
- **Analytics services:** Collect, prepare, query, process, search, visualize, and warehouse data for business insights.
- Choose services based on the task: **text, speech, images/video, documents, generative AI, streaming data, SQL, ETL, or dashboards**.
- Managed/serverless services reduce operational overhead and support rapid experimentation, scalability, and pay-as-you-use economics.

**2. In-Scope Services & Key Functions**

| Service / Feature | Primary Function | Exam Use Case |
| :--- | :--- | :--- |
| **Amazon SageMaker AI** | Build, train, and deploy ML models. | Custom ML lifecycle and predictions. |
| **Amazon Bedrock** | Access and build generative AI applications using foundation models. | GenAI without managing model infrastructure. |
| **Amazon Comprehend** | NLP for text analysis. | Sentiment, entities, key phrases, topics. |
| **Amazon Lex** | Build conversational chatbots using voice/text. | Customer-service chatbot. |
| **Amazon Polly** | Converts text to lifelike speech. | Text-to-speech applications. |
| **Amazon Q** | Generative AI assistant for answers and productivity. | Business/developer assistance. |
| **Amazon Rekognition** | Image and video analysis. | Objects, faces, labels, moderation. |
| **Amazon Textract** | Extracts text and data from documents. | Forms, tables, scanned documents. |
| **Amazon Transcribe** | Converts speech to text. | Call transcripts and captions. |
| **Amazon Translate** | Neural machine translation. | Localize text between languages. |
| **Amazon Athena** | Serverless interactive SQL queries. | Query data in Amazon S3. |
| **Amazon EMR** | Managed big-data processing frameworks. | Hadoop/Spark workloads. |
| **AWS Glue** | Serverless data integration and ETL; Data Catalog. | Discover, transform, and prepare data. |
| **Amazon Kinesis** | Ingests and processes streaming data in real time. | Logs, IoT, clickstreams. |
| **Amazon OpenSearch Service** | Managed search and analytics. | Log analysis, search, observability. |
| **Amazon QuickSight** | Business intelligence and visualization. | Dashboards and interactive reports. |
| **Amazon Redshift** | Managed cloud data warehouse. | Large-scale SQL analytics. |

**3. Exam Keywords & Common Traps**

- **Trigger Keywords:** “foundation models/generative AI” -> **Bedrock**; “custom model training” -> **SageMaker AI**; “SQL on S3” -> **Athena**; “ETL/data catalog” -> **Glue**; “real-time stream” -> **Kinesis**; “dashboard/BI” -> **QuickSight**; “data warehouse” -> **Redshift**.
- **Common Traps:** **Transcribe** = speech-to-text; **Polly** = text-to-speech; **Translate** = language translation. **Textract** extracts document data; **Rekognition** analyzes images/video. Athena queries S3 but is not a warehouse; OpenSearch is for search/log analytics, not general BI.

**4. 60-Second Cheatsheet Summary**

- **AI APIs:** Comprehend, Lex, Polly, Q, Rekognition, Textract, Transcribe, Translate.
- **ML/GenAI:** SageMaker AI = custom ML; Bedrock = foundation-model applications.
- **Analytics flow:** Kinesis (stream) -> Glue (prepare/catalog) -> Athena/EMR (query/process) -> QuickSight (visualize).
- **Redshift** = warehouse; **OpenSearch** = search and operational/log analytics.

---

### Task Statement 3.8: Identify services from other in-scope AWS service categories

**1. Core Concepts & Business Value**

- **Application integration:** Connect applications, route events, publish notifications, queue work, and orchestrate workflows.
- **Alerts and messaging:** Choose **SNS** for push/fanout notifications, **SQS** for durable asynchronous queues, and **EventBridge** for event-driven routing.
- **Business applications:** **Amazon Connect** provides cloud contact-center capabilities; **SES** sends and receives email.
- **Developer enablement:** Build and test with **CodeBuild**, automate releases with **CodePipeline**, and troubleshoot distributed applications with **X-Ray**.
- **End-user computing:** Deliver applications, desktops, or browser-based access without managing end-user infrastructure.
- **Frontend and IoT:** **Amplify** accelerates web/mobile frontend development; **IoT Core** securely connects and manages devices.
- Managed cloud services improve **agility**, scalability, and global reach while reducing infrastructure management and shifting spending from **CapEx to OpEx**.

**2. In-Scope Services & Key Functions**

| Service / Feature | Primary Function | Exam Use Case |
| :--- | :--- | :--- |
| **Amazon EventBridge** | Serverless event bus that routes events using rules. | Connect applications or react to AWS/SaaS/custom events. |
| **Amazon SNS** | Managed publish/subscribe messaging and notification service. | Broadcast alerts to email, SMS, endpoints, or subscribers. |
| **Amazon SQS** | Managed message queues for asynchronous decoupling. | Buffer work and reliably pass messages between components. |
| **AWS Step Functions** | Visual workflow orchestration using state machines. | Coordinate multi-step application processes. |
| **Amazon Connect** | Cloud-based contact center. | Provide customer service voice/chat contact-center functions. |
| **Amazon SES** | Scalable email sending and receiving service. | Send transactional, marketing, or notification email. |
| **AWS Support** | AWS technical assistance, guidance, and support plans. | Obtain help with AWS account, service, and operational issues. |
| **AWS CodeBuild** | Fully managed source-code build and test service. | Compile code and run automated tests. |
| **AWS CodePipeline** | Continuous integration and continuous delivery (CI/CD) workflow service. | Automate build, test, and deployment stages. |
| **AWS X-Ray** | Distributed application tracing and analysis. | Find performance bottlenecks and troubleshoot requests. |
| **Amazon AppStream 2.0** | Streams desktop applications to users’ browsers. | Present VM-hosted applications without local installation. |
| **Amazon WorkSpaces** | Managed, persistent virtual desktops. | Provide hosted desktops to end users. |
| **Amazon WorkSpaces Secure Browser** | Managed secure browser access to websites/apps. | Give controlled browser-based access to internal web resources. |
| **AWS Amplify** | Tools and services for building and deploying web/mobile apps. | Develop frontend experiences quickly. |
| **AWS IoT Core** | Securely connects devices to cloud applications and services. | Register, communicate with, and manage IoT devices. |

**3. Exam Keywords & Common Traps**

- **Trigger Keywords:** “event rules” -> **EventBridge**; “fanout,” “publish/subscribe,” “push notifications” -> **SNS**; “queue,” “decouple,” “worker” -> **SQS**; “workflow” -> **Step Functions**; “contact center” -> **Connect**; “email delivery” -> **SES**; “build” -> **CodeBuild**; “release pipeline” -> **CodePipeline**; “distributed tracing” -> **X-Ray**.
- **Common Traps:** SNS **pushes/broadcasts**; SQS **stores messages for consumers**. CodeBuild builds; CodePipeline orchestrates delivery. WorkSpaces is a full virtual desktop; AppStream streams individual applications. SES is email—not general pub/sub notifications.

**4. 60-Second Cheatsheet Summary**

- **EventBridge = events; SNS = notifications/fanout; SQS = queues.**
- **CodeBuild -> CodePipeline -> deploy; X-Ray -> trace and troubleshoot.**
- **AppStream = streamed apps; WorkSpaces = virtual desktops; Secure Browser = controlled web access.**
- **Connect = contact center; SES = email; Amplify = frontend/mobile; IoT Core = connected devices.**

---

## Domain 4: Billing, Pricing, and Support (12%)

### Task Statement 4.1: Compare AWS pricing models

**1. Core Concepts & Business Value**

- AWS pricing generally trades **upfront CapEx for variable OpEx**; pay only for resources consumed.
- **On-Demand Instances:** Highest flexibility; no commitment; best for short-term, unpredictable, or rapidly changing workloads.
- **Reserved Instances (RIs):** Commitment to a configuration/term for a discounted rate; typically **1 or 3 years**. Standard RIs offer the largest discount; Convertible RIs offer configuration flexibility.
- **Spot Instances:** Use spare EC2 capacity at deep discounts; workloads must tolerate interruption and possible termination.
- **Savings Plans:** Commit to a consistent **dollar-per-hour spend** for 1 or 3 years; more flexible than RIs.
- **Dedicated Hosts:** Physical server dedicated to one customer; useful for licensing or compliance requirements.
- **Dedicated Instances:** Instances run on hardware dedicated to one customer account, but host placement/control is less granular than Dedicated Hosts.
- **Capacity Reservations:** Reserve capacity in a specific Availability Zone; provide capacity assurance, but do not inherently provide a discount.
- **RI flexibility:** Regional RIs can apply across Availability Zones in a Region and may offer instance-size flexibility; Zonal RIs are tied to a specific AZ and reserve capacity.
- **AWS Organizations:** RI and Savings Plan discounts can be shared across consolidated billing accounts when discount sharing is enabled.
- **Data transfer:** Inbound data is generally free; Internet and cross-Region outbound transfer commonly incur charges. Same-Region transfers may be free between services, but **cross-AZ traffic can incur charges**.
- Storage pricing depends on **capacity, performance, retrieval, requests, and data transfer**. S3 tiers range from frequent-access Standard to archival Glacier classes; EBS pricing varies by volume type and provisioned capacity/IOPS.

**2. In-Scope Services & Key Functions**

| Service / Feature | Primary Function | Exam Use Case |
| :--- | :--- | :--- |
| **Amazon EC2 Pricing Options** | Provides On-Demand, Reserved, Spot, Dedicated Host/Instance, and Capacity Reservation purchasing models. | Match flexibility, discount, interruption tolerance, licensing, or capacity assurance requirements. |
| **AWS Savings Plans** | Offers discounted compute usage in exchange for a 1- or 3-year spend commitment. | Choose when predictable spend exists but compute type, Region, or workload may change. |

**3. Exam Keywords & Common Traps**

- **Trigger Keywords:** “no commitment” -> On-Demand; “spare capacity/deepest discount” -> Spot; “steady usage/1–3 years” -> RI or Savings Plan; “consistent hourly spend/flexibility” -> Savings Plan; “specific AZ capacity” -> Capacity Reservation; “bring-your-own-server license” -> Dedicated Host.
- **Common Traps:**
  - Spot Instances can be interrupted; they are not for interruption-intolerant workloads.
  - Capacity Reservations ensure capacity but are not the same as discounted RIs.
  - Standard RIs are less flexible than Convertible RIs.
  - RI discount sharing across Organizations depends on consolidated billing/sharing settings.
  - “Same Region” does not always mean free: cross-AZ transfer may be billed.

**4. 60-Second Cheatsheet Summary**

- **On-Demand = flexibility; RI/Savings Plans = commitment and savings; Spot = lowest cost with interruption risk.**
- **RI:** Configuration-based commitment; **Savings Plan:** Spend-based commitment.
- **Dedicated Host = physical host control/licensing; Capacity Reservation = guaranteed AZ capacity.**
- Inbound is generally free; **outbound and cross-Region transfer cost money**, and cross-AZ traffic may also incur charges.

---

### Task Statement 4.2: Understand resources for billing, budget, and cost management

**1. Core Concepts & Business Value**

- **AWS pricing:** Pay-as-you-go pricing, usage-based charges, volume discounts, and service-specific pricing models help trade **CapEx for variable OpEx**.
- **Billing information:** The AWS Billing console provides invoices, payment information, credits, charges, and service cost details.
- **Cost visibility:** Use tags, Cost Explorer, and the **AWS Cost and Usage Report (CUR)** to analyze spending by account, service, Region, resource, or project.
- **Cost control:** Use **AWS Budgets** to monitor costs, usage, reservations, and savings plans; configure alerts and supported actions.
- **Organizations:** Consolidated billing combines member-account charges into one payer account and can provide aggregated usage discounts.
- **Cost allocation:** Use activated **AWS-generated tags** and **user-defined cost allocation tags** to assign costs to teams, applications, environments, or departments.
- **Allocation reports:** Cost allocation tags can appear in billing reports such as CUR after activation; tagging is not automatically retroactive.

**2. In-Scope Services & Key Functions**

| Service / Feature | Primary Function | Exam Use Case |
| :--- | :--- | :--- |
| **AWS Budgets** | Sets custom cost or usage budgets and sends alerts when thresholds are reached. | Prevent or control unexpected spend; monitor forecasts and usage. |
| **AWS Cost and Usage Reports (CUR)** | Delivers the most detailed AWS billing and usage data to Amazon S3. | Perform granular analysis, chargeback, or import billing data into analytics tools. |
| **AWS Cost Explorer** | Provides interactive graphs, filtering, grouping, historical cost analysis, and forecasts. | Quickly investigate spending trends without building a reporting pipeline. |
| **AWS Marketplace** | Digital catalog for purchasing third-party software, data, and services. | Obtain vendor products with AWS billing, including eligible private offers. |
| **AWS Billing Conductor** | Creates customized **pro forma** billing views and rates for internal showback or chargeback. | Present customized costs to business units; does not change the actual AWS invoice. |
| **AWS Pricing Calculator** | Estimates expected AWS service costs before deployment. | Compare architectures and create a planned cost estimate. |
| **Organizations / Consolidated Billing** | Aggregates member-account billing under a management (payer) account. | Centralize payment, simplify billing, and potentially maximize volume discounts. |

**3. Exam Keywords & Common Traps**

- **Trigger Keywords:** “forecast or visualize spending” -> **Cost Explorer**; “alert when threshold is exceeded” -> **Budgets**; “detailed line-item data in S3” -> **CUR**; “estimate before deployment” -> **Pricing Calculator**; “custom internal chargeback” -> **Billing Conductor**; “single bill for multiple accounts” -> **Organizations consolidated billing**.
- **Common Traps:**
  - **Budgets** alerts; **Cost Explorer** analyzes; **CUR** supplies detailed raw billing data.
  - Pricing Calculator is an **estimate**, not an invoice.
  - Consolidated billing centralizes payment but does not merge accounts or remove account-level governance.
  - Cost allocation tags must be activated for billing use; tags do not reduce charges automatically.
  - Billing Conductor creates pro forma views, not the official AWS bill.

**4. 60-Second Cheatsheet Summary**

- **Estimate:** Pricing Calculator | **Analyze:** Cost Explorer | **Alert/control:** Budgets.
- **Detailed billing dataset:** CUR -> Amazon S3.
- **Centralize accounts and billing:** Organizations consolidated billing.
- **Allocate costs:** Activate AWS-generated or user-defined cost allocation tags.

---

### Task Statement 4.3: Identify AWS technical resources and AWS Support options

**1. Core Concepts & Business Value**

- **Official AWS resources:** Documentation, whitepapers, blogs, AWS Prescriptive Guidance, AWS Knowledge Center, and **AWS re:Post** provide architecture, implementation, troubleshooting, and best-practice guidance.
- **Support options:** AWS Support plans provide increasing levels of technical assistance, response priorities, and account guidance.
- **AWS Trusted Advisor:** Offers recommendations for **cost optimization, security, fault tolerance, performance, and service limits**.
- **AWS Health:** The **AWS Health Dashboard** shows account-specific and service events; the **AWS Health API** enables programmatic access and operational integration.
- **Trust and Safety:** Reports suspected abuse, such as spam, phishing, malware, or unauthorized use of AWS resources.
- **AWS Partners:** APN partners extend AWS capabilities. **Independent software vendors (ISVs)** provide software solutions; **system integrators (SIs)** design, migrate, and implement solutions.
- **Partner benefits:** Training and certification, partner events, technical/business enablement, and potential volume discounts.
- **AWS Professional Services and solutions architects:** Provide architecture, migration, implementation, and technical design assistance.

**2. In-Scope Services & Key Functions**

| Service / Feature | Primary Function | Exam Use Case |
| :--- | :--- | :--- |
| **AWS Support Plans** | Customer service, technical support, guidance, and case management. | Choose the support tier matching required response and guidance. |
| **AWS Trusted Advisor** | Checks environments and recommends optimization actions. | Identify cost, security, performance, resilience, or quota improvements. |
| **AWS Health Dashboard / API** | Displays AWS service and account health events; API provides programmatic access. | Monitor incidents, maintenance, and account-impacting events. |
| **AWS Prescriptive Guidance** | Provides strategies, patterns, and detailed implementation guidance. | Select migration, modernization, or architecture recommendations. |
| **AWS Knowledge Center** | AWS-authored troubleshooting articles and answers. | Resolve common service and configuration issues. |
| **AWS re:Post** | AWS community knowledge-sharing and Q&A platform. | Research issues or ask the community for solutions. |
| **AWS Marketplace** | Catalog for discovering, purchasing, governing, and managing third-party software. | Obtain ISV products and manage entitlements and costs. |
| **AWS Professional Services** | AWS experts assisting with complex cloud projects. | Obtain hands-on migration, architecture, or implementation help. |
| **AWS Partner Network (APN)** | Global network of AWS technology and consulting partners. | Use ISVs, SIs, or partner expertise beyond native AWS support. |

**3. Exam Keywords & Common Traps**

- **Trigger Keywords:** “best-practice guidance” -> Prescriptive Guidance; “troubleshooting article” -> Knowledge Center; “community answer” -> re:Post; “recommendations/checks” -> Trusted Advisor; “account-specific outage” -> Health Dashboard; “abuse report” -> Trust and Safety; “third-party software” -> Marketplace.
- **Common Traps:** Trusted Advisor is not a replacement for Support; Health Dashboard is not CloudWatch monitoring; re:Post is community-based, not guaranteed AWS case resolution; Professional Services is paid expert assistance, not a support plan.
- **Support tiers:** Developer, Business, Enterprise On-Ramp, and Enterprise provide progressively broader technical assistance; select based on required response time and guidance level.

**4. 60-Second Cheatsheet Summary**

- **Docs/whitepapers/blogs:** Learn | **Knowledge Center:** Troubleshoot | **re:Post:** Community solutions.
- **Trusted Advisor:** Optimize | **Health Dashboard/API:** Monitor AWS health and account events.
- **Marketplace:** Third-party software, governance, cost management, and entitlements.
- **APN:** ISVs and SIs; Professional Services and solutions architects provide specialized technical help.