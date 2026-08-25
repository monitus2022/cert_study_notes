# AWS Security Components & Resources Cheatsheet (Task Statement 2.4)

---

## 1. Network Security Boundary Comparison

Understanding where and how network security operates is a core focus area for the **CLF-C02** exam:

| Feature / Control | Security Group (SG) | Network ACL (NACL) | AWS WAF |
| :--- | :--- | :--- | :--- |
| **Operating Layer** | Resource / ENI level (EC2, RDS) | Subnet level boundary | Layer 7 (Application / HTTP/HTTPS) |
| **Statefulness** | **Stateful:** Inbound allowed traffic automatically permits return outbound traffic. | **Stateless:** Inbound and outbound traffic rules must be configured separately. | **Stateful:** Inspects web request streams. |
| **Rule Types** | **ALLOW rules only** (Implicit deny for everything else) | **ALLOW and DENY rules** | **ALLOW, BLOCK, and COUNT rules** |
| **Traffic Scope** | Filters traffic arriving at or leaving an individual instance. | Filters traffic entering or leaving a subnet boundary (does not affect intra-subnet traffic). | Filters web requests targeting CloudFront, ALB, API Gateway, or AppSync. |
| **Rule Targets / References** | IP addresses, CIDR blocks, or **other Security Group IDs**. | IP addresses and CIDR blocks only. | HTTP headers, URI paths, IP sets, SQL injection patterns, XSS scripts. |

---

## 2. Security Assessments, Pen Testing & Third-Party Tools

### A. AWS Security Assessment Tools
* **AWS Trusted Advisor:** Provides high-level security health checks (e.g., checks for missing MFA on root account, unattached Elastic IPs, or publicly accessible S3 buckets/ports).
* **Amazon Inspector:** Conducts automated software vulnerability scans on EC2 instances, container images in ECR, and Lambda functions against known CVEs.

### B. AWS Penetration Testing Policy
* **Rule:** You **can** conduct security assessments and penetration testing against your AWS resources **without prior approval** for specific permitted services.
* **Permitted Services:** Amazon EC2, Amazon RDS, Amazon CloudFront, Amazon Aurora, AWS Lambda, Amazon API Gateway, Amazon Lightsail, and Amazon ECS/Fargate.
* **Prohibited:** Pen testing against AWS infrastructure, control planes, or DDoS attack simulation without explicit authorization.

### C. AWS Marketplace
* **What it is:** A digital catalog of thousands of third-party software listings (AMIs, SaaS, CloudFormation templates).
* **Exam Trigger:** Use **AWS Marketplace** when you need third-party security software (e.g., custom Palo Alto/Fortinet virtual firewalls, hardened security OS images) deployed directly into your AWS account.

---

## 3. AWS Security Research & Guidance Resources

When looking for official security guidance, compliance frameworks, or troubleshooting steps:

* **AWS Knowledge Center:** Searchable database of FAQ answers and step-by-step technical guides created by AWS Support.
* **AWS Security Center / Security Documentation:** Official portal for AWS security whitepapers, threat-modeling guides, and security best practices.
* **AWS Security Whitepapers:** In-depth architectural whitepapers detailing compliance alignment, encryption strategies, and risk management.
* **AWS Security Blog & Security Forum:** Official news and community discussions covering newly discovered security patterns, updates, and mitigation techniques.

---

## 4. CLF-C02 Exam Keyword Triggers & Traps

* **Trigger: "Need an explicit DENY rule to block a specific IP address"**  
  $\rightarrow$ **Network ACL (NACL)** *(Security Groups cannot explicitly deny)*.

* **Trigger: "Instance-level firewall with automatic return traffic approval"**  
  $\rightarrow$ **Security Group** *(Stateful, operates at ENI level)*.

* **Trigger: "Protect web app against SQL Injection or Cross-Site Scripting (XSS)"**  
  $\rightarrow$ **AWS WAF**.

* **Trigger: "Allow traffic between instances using Security Group references"**  
  $\rightarrow$ **Security Group** *(NACLs cannot reference Security Group IDs)*.

* **Trigger: "Where to purchase third-party security software to run on AWS"**  
  $\rightarrow$ **AWS Marketplace**.

* **Trap Alert: Intra-Subnet Traffic**  
  NACLs only inspect traffic **crossing the subnet boundary**. Communication between two EC2 instances sitting inside the *same* subnet never touches the NACL.