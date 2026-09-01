# AWS Exam Guide: EC2 Self-Hosted vs. Amazon RDS vs. Amazon Aurora (MySQL)

---

## 1. Summary Comparison Table

| Feature / Dimension | Self-Hosted MySQL on EC2 | Amazon RDS MySQL | Amazon Aurora MySQL |
| :--- | :--- | :--- | :--- |
| **Service Category** | **IaaS** (Infrastructure as a Service) | **PaaS** (Platform as a Service) | **Cloud-Native PaaS** |
| **OS / Root Access** | **YES** (Full root access to host OS) | **NO** (AWS manages underlying OS) | **NO** (AWS manages underlying OS) |
| **Management Overhead** | **Highest** (Customer manages everything) | **Low** (AWS manages OS/patching/backups) | **Lowest** (AWS manages OS/patching/storage scaling) |
| **Performance** | Standard (depends on EC2/EBS selection) | Standard (native MySQL performance) | **High Performance** (Up to **5x** standard MySQL) |
| **Storage Architecture** | Manual EBS volume management | Pre-provisioned EBS storage (auto-expand available) | **Auto-scaling storage** (grows in 10 GB increments up to 128 TiB) |
| **High Availability (HA)** | Manual setup (EC2 replication, scripts) | **Multi-AZ synchronous replication** (Standby in 2nd AZ) | **Automatic 6 copies across 3 AZs** (Fault-tolerant, self-healing) |
| **Read Replicas** | Manual setup | Up to 5 Read Replicas | Up to **15 Read Replicas** (ultra-fast, low replication lag) |

---

## 2. Shared Responsibility Model Breakdown

Understanding who handles what is a primary focus for the **CLF-C02** exam:

### A. Self-Hosted MySQL on Amazon EC2 (Customer Managed)
* **AWS manages:** Physical hardware, host virtualization, facility security.
* **Customer manages:** Guest OS installation & patching, database software installation & tuning, database patching, automated backups, disaster recovery, and Multi-AZ replication setup.

### B. Amazon RDS MySQL & Amazon Aurora (AWS Managed)
* **AWS manages:** OS installation & security patching, database software provisioning & patching, hardware maintenance, automated backups, point-in-time recovery, and underlying storage replication.
* **Customer manages:** Database schema design, table creation, user authentication/permissions, query optimization, and network access rules (Security Groups).

---

## 3. CLF-C02 Exam Keywords & Decision Triggers

### 1. Self-Hosted MySQL on EC2
* **Keywords:** *"Full control over OS"*, *"root access required"*, *"unsupported database version"*, *"custom database extensions/plugins"*.
* **Exam Rule:** If a question mentions needing OS root access or installing custom third-party kernel modules alongside the database, choose **EC2**.

### 2. Amazon RDS MySQL
* **Keywords:** *"Managed relational database"*, *"offload OS maintenance and backups"*, *"standard open-source MySQL engine"*, *"Multi-AZ for high availability"*.
* **Exam Rule:** Choose **RDS** when a standard relational database is required without OS administration overhead, but cloud-native enterprise performance is not specifically demanded.

### 3. Amazon Aurora MySQL
* **Keywords:** *"Up to 5x performance of MySQL"*, *"cloud-native relational database"*, *"auto-scaling storage up to 128 TiB"*, *"6 copies of data across 3 AZs"*, *"serverless relational DB"*.
* **Exam Rule:** Choose **Aurora** when maximum performance, high availability, fast failover, or auto-scaling relational storage is required.

---

## 4. Top Exam Traps & Distractors

* **Trap 1: OS Root Access**
  * Neither **Amazon RDS** nor **Amazon Aurora** provides SSH or root access to the underlying OS. If a question states that the database administrator *must* have OS access, the answer is always **Self-Hosted on EC2**.
* **Trap 2: Performance Multipliers**
  * AWS specifically quantifies Aurora performance: **Up to 5x faster than standard MySQL** and **up to 3x faster than standard PostgreSQL**.
* **Trap 3: Storage Scaling**
  * Standard RDS requires choosing or configuring EBS volumes. **Aurora automatically scales storage** in increments as data grows, requiring no storage pre-provisioning.
* **Trap 4: Multi-AZ vs. Read Replicas**
  * **Multi-AZ:** Used for **High Availability (HA) and Disaster Recovery (DR)**. Writes go to primary; standby is synchronous.
  * **Read Replicas:** Used for **Read Scaling** (offloading read-heavy workloads from the primary DB). Writes do not go directly to read replicas.