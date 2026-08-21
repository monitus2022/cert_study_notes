# AWS Pricing Model Decision Guide

## Core decision principle

Choose a pricing model **after** you have:

1. Rightsized the workload.
2. Determined whether demand is steady, variable, or unpredictable.
3. Identified whether interruptions are acceptable.
4. Decided whether you need dedicated tenancy or capacity guarantees.
5. Estimated the expected duration of usage.

## Pricing model decision flowchart

```mermaid
flowchart TD
    A([START]) --> B{Have you rightsized the workload<br/>and enabled elasticity?}

    B -- No --> B1[Rightsize resources<br/>and configure Auto Scaling first]
    B1 --> B

    B -- Yes --> C{Is dedicated physical hardware<br/>or single-tenant infrastructure required?}

    C -- Yes --> D{Do you need control and visibility<br/>over the physical server?}
    D -- Yes --> D1["Dedicated Host<br/><br/>• Host dedicated to you<br/>• Pay for the host<br/>• Useful for licensing or compliance"]
    D -- No --> D2["Dedicated Instance<br/><br/>• Runs on single-tenant hardware<br/>• Pay per instance-hour"]

    C -- No --> E{Do you need guaranteed EC2 capacity<br/>in a specific Availability Zone?}

    E -- Yes --> E1["Capacity Reservation<br/><br/>• Reserves capacity in a specific AZ<br/>• Useful when capacity must be available<br/>• Does not automatically provide a discount<br/>• Charges apply while reserved"]

    E -- No --> F{Can the workload tolerate<br/>interruption or termination?}

    F -- Yes --> G{Is the workload flexible and able<br/>to use spare capacity?}
    G -- Yes --> G1["Spot Instances<br/><br/>• Lowest EC2 price<br/>• Up to 90% below On-Demand<br/>• Can be interrupted by AWS<br/>• Suitable for fault-tolerant,<br/>  flexible workloads"]
    G -- No --> G2["On-Demand Instances<br/><br/>• No long-term commitment<br/>• Flexible start and end time<br/>• Suitable for short-term or<br/>  unpredictable workloads"]

    F -- No --> H{Is usage expected to be<br/>steady and predictable?}

    H -- No --> H1["On-Demand Instances<br/><br/>• Best for uncertain requirements<br/>• No commitment<br/>• Can be combined with other models"]

    H -- Yes --> I{Do you want flexibility across compute<br/>services, instance families, operating systems, or Regions?}

    I -- Yes --> I1["Savings Plans<br/><br/>• Commit to a consistent amount<br/>  of compute usage per hour<br/>• Lower prices than On-Demand<br/>• More flexible than Standard RIs<br/>• Applies to eligible compute usage<br/>  such as EC2, Lambda, and Fargate"]

    I -- No --> J{Do you need a specific EC2 configuration<br/>and can commit for 1 or 3 years?}

    J -- Yes --> K{Need to change instance family,<br/>operating system, or tenancy?}
    K -- Yes --> K1["Convertible Reserved Instance<br/><br/>• More flexibility<br/>• Usually lower discount than<br/>  Standard Reserved Instance"]
    K -- No --> K2["Standard Reserved Instance<br/><br/>• Predictable, steady-state EC2 usage<br/>• 1-year or 3-year term<br/>• Up to 72% discount<br/>• Largest RI discount<br/>• Least flexibility"]

    J -- No --> J1["Savings Plans or<br/>On-Demand Instances"]

    K2 --> L{Does usage occur on a predictable<br/>recurring schedule?}
    K1 --> L
    L -- Yes --> L1["Scheduled Reserved Instance*<br/><br/>• Discounted during a predictable<br/>  recurring schedule"]
    L -- No --> L2["Standard or Convertible<br/>Reserved Instance"]

    classDef start fill:#14532d,stroke:#86efac,color:#f0fdf4,stroke-width:2px;
    classDef decision fill:#713f12,stroke:#fcd34d,color:#fffbeb,stroke-width:1.5px;
    classDef result fill:#123b63,stroke:#7dd3fc,color:#f0f9ff,stroke-width:1.5px;
    classDef action fill:#581c87,stroke:#d8b4fe,color:#faf5ff,stroke-width:1.5px;

    class A start;
    class B,C,D,E,F,G,H,I,J,K,L decision;
    class D1,D2,E1,G1,G2,H1,I1,J1,K1,K2,L1,L2 result;
    class B1 action;
```

> **Exam note:** Scheduled Reserved Instances are a historical EC2 pricing concept and may not be available for new purchases in all AWS contexts. For CLF-C02 questions, recognize the concept as a commitment for predictable recurring schedules, but follow the specific wording of the question.

---

## Pricing model comparison

| Pricing model | Commitment | Discount level | Can be interrupted? | Best for |
|---|---:|---:|---:|---|
| **On-Demand Instances** | None | Baseline price | No AWS interruption because of the pricing model | Short-term, unpredictable, or interruption-intolerant workloads |
| **Reserved Instances** | 1 or 3 years | Up to 72% below On-Demand | No AWS interruption because of the pricing model | Steady-state, predictable EC2 usage |
| **Standard Reserved Instances** | 1 or 3 years | Highest RI discount | No | Stable EC2 configuration with little need for change |
| **Convertible Reserved Instances** | 1 or 3 years | Lower than Standard RI, generally | No | Long-term usage with expected changes to instance family, OS, or tenancy |
| **Scheduled Reserved Instances** | Recurring schedule | Discounted during schedule | No | Predictable recurring workloads |
| **Savings Plans** | 1 or 3 years | Discounted compute usage | No | Predictable compute spending with flexibility across eligible compute services |
| **Spot Instances** | No long-term commitment | Up to 90% below On-Demand | **Yes** | Fault-tolerant, flexible, interruptible workloads |
| **Dedicated Hosts** | Varies | Usually more expensive | No shared-tenancy interruption | Licensing, compliance, and physical-server visibility requirements |
| **Dedicated Instances** | Usually usage-based | Generally higher than shared tenancy | No shared-tenancy interruption | Single-tenant hardware without host-level control |
| **Capacity Reservations** | Reservation-based | Does not inherently provide a discount | Capacity is reserved | Guaranteeing EC2 capacity in a specific Availability Zone |

---

## Practical workload patterns

A cost-optimized architecture commonly combines pricing models:

```mermaid
flowchart LR
    A[Application capacity] --> B[Production baseline]
    A --> C[Variable demand]
    A --> D[Interruptible workloads]

    B --> B1["Reserved Instances or Savings Plans<br/><br/>Predictable, always-running workload"]
    C --> C1["On-Demand Instances<br/><br/>Unplanned or temporary additional capacity"]
    D --> D1["Spot Instances<br/><br/>Flexible batch jobs, testing, analytics,<br/>or workloads that tolerate interruption"]

    classDef source fill:#14532d,stroke:#86efac,color:#f0fdf4,stroke-width:2px;
    classDef category fill:#713f12,stroke:#fcd34d,color:#fffbeb,stroke-width:1.5px;
    classDef result fill:#123b63,stroke:#7dd3fc,color:#f0f9ff,stroke-width:1.5px;

    class A source;
    class B,C,D category;
    class B1,C1,D1 result;
```

### Example

A company runs an application with:

- A stable baseline of four EC2 instances.
- Variable traffic during business hours.
- Batch processing that can restart if interrupted.

A suitable approach is:

- **Reserved Instances or a Savings Plan** for the stable baseline.
- **On-Demand Instances** for unexpected demand.
- **Spot Instances** for interruptible batch processing.
- **Auto Scaling** to match capacity with demand.

---

## Reserved Instance payment options

Reserved Instances can generally be purchased using:

- **All Upfront** — highest payment at the beginning; typically the lowest effective cost.
- **Partial Upfront** — part of the cost paid initially, with the remainder paid periodically.
- **No Upfront** — no initial payment, but usually a higher effective cost than upfront options.

Important points:

- The commitment is charged whether or not the instance is running.
- A **3-year term** is generally more cost-effective than a 1-year term.
- **Regional Reserved Instances** can apply across Availability Zones within a Region.
- Reserved Instance benefits can be shared across accounts through **consolidated billing** in AWS Organizations, subject to applicable billing rules.

---

## High-value CLF-C02 decision rules

### Choose On-Demand when:

- The workload is short-term.
- Requirements are uncertain.
- Start and end times are flexible.
- The application cannot tolerate interruption.
- You do not want a long-term commitment.

### Choose Reserved Instances when:

- EC2 usage is steady and predictable.
- The workload will run for 1 or 3 years.
- You want a discount in exchange for commitment.
- You can accept less flexibility than Savings Plans.
- The exam asks for the **largest Reserved Instance discount**: choose **Standard Reserved Instances**.

### Choose Savings Plans when:

- You have predictable compute spending.
- You want a commitment-based discount.
- You need more flexibility across eligible compute usage.
- The workload may move between services such as EC2, Lambda, and Fargate.

### Choose Spot Instances when:

- The workload can tolerate interruption.
- The workload is fault tolerant or restartable.
- You want the lowest possible EC2 price.
- Examples include batch processing, big data processing, CI workloads, and stateless flexible applications.

### Choose Dedicated Hosts when:

- You need an entire physical server dedicated to your organization.
- You need host-level visibility or control.
- You have software licensing requirements based on physical sockets or cores.
- The question emphasizes **paying for the host**, not individual instances.

### Choose Dedicated Instances when:

- You need single-tenant hardware.
- You do not require control over the physical host.
- The question emphasizes paying **per instance-hour**.

### Choose Capacity Reservations when:

- You must guarantee EC2 capacity.
- The requirement is tied to a specific Availability Zone.
- The question emphasizes capacity availability rather than a pricing discount.

---

## Pricing model selection summary

```mermaid
flowchart TD
    A{Need the lowest possible price?}
    A -- Yes --> B{Can tolerate interruptions?}
    B -- Yes --> B1[Spot Instances]
    B -- No --> C[Continue evaluating commitment]

    C --> D{Need no commitment and<br/>maximum flexibility?}
    D -- Yes --> D1[On-Demand Instances]
    D -- No --> E{Have predictable EC2 usage<br/>for 1 or 3 years?}

    E -- Yes --> F{Need maximum discount and<br/>stable configuration?}
    F -- Yes --> F1[Standard Reserved Instance]
    F -- No --> G{Need to change configuration<br/>over time?}
    G -- Yes --> G1[Convertible Reserved Instance]
    G -- No --> H{Need flexible coverage across<br/>compute services?}
    H -- Yes --> H1[Savings Plan]
    H -- No --> F1

    E -- No --> I[Savings Plans or<br/>On-Demand Instances]

    J{Need dedicated physical hardware?}
    J -- Yes --> K{Need host-level control<br/>or licensing support?}
    K -- Yes --> K1[Dedicated Host]
    K -- No --> K2[Dedicated Instance]

    L{Need guaranteed EC2 capacity<br/>in a particular AZ?}
    L -- Yes --> L1[Capacity Reservation]

    classDef decision fill:#713f12,stroke:#fcd34d,color:#fffbeb,stroke-width:1.5px;
    classDef result fill:#123b63,stroke:#7dd3fc,color:#f0f9ff,stroke-width:1.5px;

    class A,B,C,D,E,F,G,H,J,K,L decision;
    class B1,D1,F1,G1,H1,I,K1,K2,L1 result;
```

## Key exam traps

- **Spot Instances are the cheapest, but they can be interrupted.**
- **On-Demand is not always the cheapest; it is chosen for flexibility and lack of commitment.**
- **Reserved Instances require a 1-year or 3-year commitment.**
- **You pay for a Reserved Instance commitment even when the instance is not running.**
- **Standard Reserved Instances provide the greatest RI discount.**
- **Convertible Reserved Instances provide more flexibility than Standard Reserved Instances.**
- **Capacity Reservations guarantee capacity but are not primarily a discount mechanism.**
- **Dedicated Hosts are billed for the host; Dedicated Instances are billed per instance.**
- **Auto Scaling and rightsizing should be considered before selecting a pricing model.**
- **Multiple pricing models can be used together in the same environment.**