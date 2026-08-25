# AWS Well-Architected Framework: 6 Pillars Cheatsheet & Exam Guide

---

## 1. The 6 Pillars Overview & Exam Triggers

| Pillar | Core Focus | Key Design Principles | Exam Keyword Triggers |
| :--- | :--- | :--- | :--- |
| **Operational Excellence** | Run/monitor systems and continually improve supporting processes. | • Perform operations as code (IaC)<br>• Make small, frequent, reversible changes<br>• Refine procedures frequently<br>• Anticipate and learn from failures | Automation, CI/CD, Infrastructure as Code (CloudFormation), runbooks, playbooks, post-mortems |
| **Security** | Protect information, systems, and assets while delivering business value. | • Implement a strong identity foundation (Least Privilege)<br>• Enable traceability (Logging & Auditing)<br>• Apply security at all layers (Defense-in-Depth)<br>• Protect data in transit and at rest | Encryption (KMS), IAM least privilege, compliance, data protection, audit trails (CloudTrail) |
| **Reliability** | Recover from disruptions, dynamically acquire capacity, and mitigate outages. | • Automatically recover from failure<br>• Test recovery procedures<br>• Scale horizontally to increase availability<br>• Stop guessing capacity | Auto Scaling, Multi-AZ failover, backup/restore, disaster recovery, fault tolerance, self-healing |
| **Performance Efficiency** | Use computing resources efficiently and maintain efficiency as demand/technology changes. | • Democratize advanced technologies (Use managed services)<br>• Go global in minutes<br>• Use serverless architectures<br>• Experiment more often | Serverless (Lambda), picking optimal EC2 instance types, global latency, CloudFront caching |
| **Cost Optimization** | Run systems to deliver maximum business value at the lowest price point. | • Adopt a consumption model (Pay for what you use)<br>• Measure overall efficiency<br>• Stop spending money on undifferentiated heavy lifting<br>• Analyze and attribute expenditure | Rightsizing, Reserved Instances / Savings Plans, Cost Explorer, tagging, reducing idle resources |
| **Sustainability** | Minimize environmental impacts of running cloud workloads. | • Understand your environmental impact<br>• Maximize utilization to minimize resources<br>• Adopt new, more efficient hardware/software options<br>• Reduce downstream impact | Reducing carbon footprint, energy consumption, maximizing hardware utilization |

---

## 2. Top Exam Traps & Distractors

* **Reliability vs. Performance Efficiency:**  
  * **Reliability:** Auto Scaling used to **survive an outage or maintain availability**.  
  * **Performance Efficiency:** Auto Scaling used to **handle sudden traffic spikes without performance degradation**.
* **Operational Excellence vs. Cost Optimization:**  
  Replacing manual provisioning with automated scripts improves **Operational Excellence**, even if it indirectly saves labor hours.
* **AWS Well-Architected Tool:**  
  AWS provides a free console service called the **AWS Well-Architected Tool** to review your workloads against these 6 pillars and receive actionable architectural recommendations.