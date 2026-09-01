# Certification Revision Portal

Welcome to my personal AWS certification study repository and revision hub.

---

## 🎯 Target Certifications

=== "AWS MLA-C01 (Primary Focus)"

    ### AWS Certified Machine Learning Engineer – Associate
    Focuses on MLOps pipelines, SageMaker feature engineering, model monitoring, and infrastructure cost optimization.

    *   **Status:** In Progress
    *   **Target Date:** Q3 2026
    *   **Key Topics:**
        *   [Task 1.2 – Transform Data & Feature Engineering](mla-c01/domain-1/task-1-2-transform-data.md)
        *   [Task 4.1 – Monitor Model Inference](mla-c01/domain-4/task-4-1-monitor-inference.md)
        *   [Task 4.2 – Infrastructure & Cost Optimization](mla-c01/domain-4/task-4-2-infrastructure-costs.md)

=== "AWS CLF-C02"

    ### AWS Certified Cloud Practitioner
    Foundational overview of core cloud concepts, AWS services, security, pricing, and support tiers.

    *   **Status:** Completed
    *   **Quick Review:**
        *   [CLF-C02 High-Yield Exam Notes](clf-c02/final-notes.md)

---

## 💡 Note Features & Structure

!!! tip "Hands-On Lab Rules"
    All lab exercises in these notes follow strict **cost-control hygiene**—using serverless options (Glue DataBrew, Lambda, CloudShell) or short-lived instances (`ml.m5.large`) deleted immediately after testing to keep overall spend under **$1–2 per exercise**.

Every study note in this portal is structured with:

1.  **Task Overview & Mental Models:** High-yield service definitions and architecture patterns.
2.  **Low-Cost Hands-On Steps:** Step-by-step CLI/Python walkthroughs to build real-world muscle memory.
3.  **Exam Traps & Distractors:** Common scenario tricks, misnomers, and wrong-answer patterns.
4.  **Quick-Reference Tables:** Decision trees for instant lookup during final revision.

---

## 🚀 Quick Navigation

| Resource | Description | Path |
| :--- | :--- | :--- |
| **Data Preparation** | Encoding, imputation, scaling, DataBrew & Data Wrangler | `mla-c01/domain-1/` |
| **Inference Monitoring** | Model Monitor, Clarify, CloudWatch alarms & drift metrics | `mla-c01/domain-4/` |
| **Cost & Infrastructure** | Instance families, Savings Plans, Inference Recommender | `mla-c01/domain-4/` |
| **Cloud Fundamentals** | Shared Responsibility, EC2 pricing, support plans cheat sheet | `clf-c02/` |