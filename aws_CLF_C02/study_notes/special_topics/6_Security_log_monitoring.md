# AWS Security, Governance & Compliance Cheatsheet (Task Statement 2.2)

---

## 1. Core AWS Security Services

| Service | Category | Core Function | Exam Keyword Triggers |
| :--- | :--- | :--- | :--- |
| **AWS WAF** | App Security | Filters Layer 7 (HTTP/S) web traffic to protect against web exploits. | SQL Injection, Cross-Site Scripting (XSS), HTTP rate limiting, block specific IP ranges. |
| **AWS Shield** | DDoS Protection | Safeguards applications against Distributed Denial of Service attacks. | **Standard:** Free, auto-enabled for all customers.<br>**Advanced:** Paid 24/7 DDoS Response Team (DRT), cost protection against scaling spikes. |
| **Amazon GuardDuty** | Threat Detection | Continuous intelligent threat detection analyzing logs using machine learning. | Analyzes CloudTrail, VPC Flow Logs, DNS logs; identifies compromised EC2 instances or crypto-mining. |
| **Amazon Inspector** | Vulnerability Scan | Automated security assessment for software vulnerabilities and network exposure. | Scans **EC2 instances**, **ECR container images**, and **AWS Lambda** against known CVEs. |
| **Amazon Macie** | Data Privacy | Uses ML to discover, classify, and protect sensitive data. | Finds **PII** (personally identifiable information) and credit card data stored inside **Amazon S3 buckets**. |
| **AWS KMS** | Encryption | Managed service to create, control, and manage cryptographic keys. | **Encryption at rest** / **in transit**, envelope encryption, hardware security modules (HSM). |
| **AWS Secrets Manager** | Credential Lifecycle | Securely stores, retrieves, and automatically rotates credentials. | Auto-rotates **database credentials**, API keys, and OAuth tokens on a schedule. |
| **AWS Security Hub** | Security Posture | Central dashboard aggregating security alerts and compliance checks. | Consolidated view of findings across GuardDuty, Inspector, Macie, and AWS Config. |

---

## 2. Logging, Monitoring, Auditing & Configuration Management

Understanding the distinction between these four operational tools is heavily tested on the **CLF-C02** exam:

| Service | Primary Purpose | Key Question Answered | Core Exam Keywords |
| :--- | :--- | :--- | :--- |
| **Amazon CloudWatch** | **Performance Monitoring** | *"How are my resources performing right now?"* | Operational metrics, performance CPU/memory logs, alarms, Auto Scaling triggers, dashboards. |
| **AWS CloudTrail** | **API Auditing & Governance** | *"WHO made WHAT API call, WHEN, and from WHERE?"* | Track user activity, API request history, security auditing, forensic investigation, account governance. |
| **AWS Config** | **Configuration & Compliance** | *"How has my resource configuration changed over time?"* | Resource inventory, configuration history, compliance rules (e.g., *"Is S3 public?"*), rollbacks. |
| **AWS Audit Manager** | **Compliance Evidence** | *"Am I meeting my industry compliance standards?"* | Automate evidence collection for audit reports (e.g., PCI-DSS, SOC 2, HIPAA). |

---

## 3. AWS Artifact: Compliance Portal

**AWS Artifact** is a self-service portal providing on-demand access to AWS’s security, compliance, and legal documentation.

* **AWS Artifact Reports:** Download official third-party audit reports, ISO certifications, SOC 1/2/3 reports, and PCI-DSS attestations.
* **AWS Artifact Agreements:** Review, accept, and manage legal agreements with AWS for an entire organization (e.g., Business Associate Addendum [BAA] for HIPAA compliance).
* **Exam Trigger:** *"Need to provide an auditor with AWS security compliance reports or ISO certifications"* $\rightarrow$ **AWS Artifact**.

---

## 4. Top Exam Traps & Distractors

* **CloudWatch vs. CloudTrail:**  
  * **CloudWatch:** Focuses on **Performance & Metrics** (CPU utilization, application logs, alerts).  
  * **CloudTrail:** Focuses on **Account Actions & API Calls** (who logged in, created a VPC, or deleted an S3 bucket).
* **CloudTrail vs. AWS Config:**  
  * **CloudTrail:** Records the **API event/action** (e.g., `UpdateSecurityGroup`).  
  * **AWS Config:** Records the **resulting state change of the resource** over time (e.g., Security Group now opens port 22 to `0.0.0.0/0`).
* **GuardDuty vs. Inspector:**  
  * **GuardDuty:** Actively monitors **network and event logs for suspicious behavior/threats**.  
  * **Inspector:** Actively scans **installed software packages and OS configurations for known security vulnerabilities**.
* **WAF vs. Security Groups:**  
  * **AWS WAF:** Operates at **Layer 7** (inspects HTTP request body, header, SQL injection, XSS).  
  * **Security Group:** Operates at **Layer 4** (inspects source/destination IP addresses and TCP/UDP ports).
* **Secrets Manager vs. Systems Manager Parameter Store:**  
  * **Secrets Manager:** Includes **built-in automatic credential rotation**.  
  * **Parameter Store:** Plain key-value store; requires writing custom Lambda code to handle rotation.