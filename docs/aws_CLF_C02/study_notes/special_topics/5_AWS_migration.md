# AWS Cloud Migration: CAF, 7 Rs & Migration Services Cheatsheet

---

## 1. AWS Cloud Adoption Framework (AWS CAF) – 6 Perspectives

The AWS CAF helps organizations assess cloud readiness and build a structured roadmap for digital transformation. It divides capabilities into **Business** and **Technical** perspectives.

| Perspective | Category | Primary Focus | Key Stakeholders & Capabilities |
| :--- | :--- | :--- | :--- |
| **Business** | Business | Align cloud investments with business goals and drive value realization. | Business managers, finance, strategy; Data monetization, portfolio management |
| **People** | Business | Bridge technology and business by driving organizational change and cloud fluency. | HR, leadership; Culture evolution, cloud skills, change acceleration |
| **Governance** | Business | Coordinate cloud initiatives while managing risks, budgets, and compliance. | CIO, CFO, risk managers; Cloud financial management (FinOps), risk assessment |
| **Platform** | Technical | Architect scalable enterprise platforms and modernize existing workloads. | CTO, architects; CI/CD, IaC, modern app development, platform engineering |
| **Security** | Technical | Ensure data confidentiality, integrity, and availability in the cloud. | CISO, security team; Identity/access management, threat detection, data protection |
| **Operations** | Technical | Deliver and maintain cloud services to meet operational business requirements. | IT operations, site reliability engineers; Observability, patch management, incident management |

---

## 2. The 7 Migration Strategies (The 7 Rs)

| Strategy | Alias / Description | Effort & Cost | Ideal Use Case & Exam Keyword Triggers |
| :--- | :--- | :--- | :--- |
| **Rehost** | *"Lift and Shift"* | Low | Move servers/VMs to AWS as-is without architectural changes. **Trigger:** "Move quickly", "minimal code changes", "tight datacenter exit deadline". |
| **Relocate** | *"Hypervisor Lift & Shift"* | Low | Move a cluster of VMs (e.g., VMware) or containers to AWS without changing code or OS. **Trigger:** "VMware Cloud on AWS", "no host re-configuration". |
| **Replatform** | *"Lift, Tinker, and Shift"* | Medium | Make minor optimizations to leverage managed services without changing core code. **Trigger:** "Move self-hosted DB to Amazon RDS", "use managed platform". |
| **Repurchase** | *"Drop and Shop"* | Variable | Replace an existing application with a third-party SaaS product. **Trigger:** "Switch to SaaS", "buy commercial software from AWS Marketplace". |
| **Refactor / Re-architect** | *"Cloud-Native Rewrite"* | Highest | Completely redesign application code to use cloud-native features. **Trigger:** "Microservices", "serverless (Lambda)", "maximum agility & scalability". |
| **Retain** | *"Keep As-Is"* | Zero | Keep applications in the source on-premises environment. **Trigger:** "Not ready for migration", "recently upgraded", "legacy compliance block". |
| **Retire** | *"Decommission"* | Zero | Turn off applications that are no longer needed or providing business value. **Trigger:** "Identify unused IT assets", "decommission legacy system". |

---

## 3. AWS Migration Tools & Target Storage Services

### Migration Tools
* **AWS Application Migration Service (AWS MGN):** Primary tool for **Rehosting** physical, virtual, or cloud servers to EC2 with block-level replication and minimal downtime.
* **AWS Database Migration Service (AWS DMS):** Migrates databases to AWS with zero downtime. 
  * *Homogeneous Migration:* Same DB engine (e.g., MySQL to MySQL) $\rightarrow$ Use **AWS DMS** alone.
  * *Heterogeneous Migration:* Different DB engines (e.g., Oracle to Aurora) $\rightarrow$ Use **AWS Schema Conversion Tool (SCT)** first, then **AWS DMS**.
* **AWS Snow Family (Snowcone, Snowball Edge, Snowmobile):** Physical hardware devices for offline, petabyte/exabyte-scale data transfers where internet bandwidth is limited.
* **AWS DataSync:** Automated online data transfer between on-premises storage (NFS/SMB) and AWS storage (S3, EFS, FSx).
* **AWS Migration Hub:** Single dashboard to track and monitor migration progress across multiple AWS and partner tools.

### Common Target Workload Selection
* **Relational Database (SQL):** **Amazon RDS** or **Amazon Aurora** (Note: Aurora only supports MySQL & PostgreSQL; SQL Server on EC2 is often used for custom licensing/cost tuning).
* **NoSQL Database:** **Amazon DynamoDB** (Key-value / JSON document store).
* **Low-Latency Shared Files:** **Amazon EFS** (Linux file system) or **Amazon FSx**.
* **Low-Cost Data Archiving:** **Amazon S3 Glacier** (designed for long-term cold storage; incurs retrieval fees and lead times).

---

## 4. Top Exam Traps & Distractors

* **CAF vs. Well-Architected Framework:**
  * **AWS CAF:** Focuses on **organizational readiness, capabilities, and strategy** (6 Perspectives).
  * **Well-Architected Framework:** Focuses on **technical architecture best practices** for workloads (6 Pillars).
* **Rehost vs. Replatform vs. Refactor:**
  * Moving a VM as-is to EC2 $\rightarrow$ **Rehost**.
  * Moving a DB to RDS without rewriting the app $\rightarrow$ **Replatform**.
  * Rewriting a monolithic app into Lambda functions $\rightarrow$ **Refactor**.
* **AWS DMS + AWS SCT:** If converting database engines during migration, you **must** use the **Schema Conversion Tool (SCT)** to convert the schema before using DMS to replicate the data.