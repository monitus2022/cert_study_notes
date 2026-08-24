# AWS Site-to-Site VPN vs. AWS Direct Connect (Exam & Architectural Guide)

---

## 1. Overview & Technical Comparison

AWS Site-to-Site VPN creates an encrypted IPsec tunnel over the public internet, whereas AWS Direct Connect (DX) establishes a dedicated physical network link from an on-premises facility directly into AWS, bypassing the public internet entirely.

| Feature | AWS Site-to-Site VPN | AWS Direct Connect (DX) |
| :--- | :--- | :--- |
| **Connection Path** | Public internet via encrypted IPsec tunnel | Dedicated private fiber circuit |
| **Bandwidth Limits** | Up to 1.25 Gbps per tunnel (scalable via ECMP) | 1 Gbps, 10 Gbps, 100 Gbps (or Hosted 50 Mbps–10 Gbps) |
| **Latency & Stability** | Variable; subject to public internet congestion | Consistent, deterministic, ultra-low latency |
| **Provisioning Time** | Minutes to hours | Weeks to months (requires telecom circuit setup) |
| **Encryption** | IPsec encryption enabled by default | None by default (optional MACsec or IPsec over DX) |
| **Data Egress Cost** | Standard AWS internet egress pricing | Discounted data egress pricing |
| **Initial Investment** | Zero upfront cost; pay per connection-hour/data | Fixed port-hour fee + telecom circuit charges |

### Key Architectural Considerations
* **Performance & Scale:** Use VPN for dev/test environments, small offices, or low-volume workloads. Use Direct Connect for high-throughput production applications, database migrations, or real-time analytics requiring consistent latency.
* **Security & Compliance:** VPN automatically encrypts data at Layer 3. Direct Connect isolates traffic to a private circuit; for private + encrypted transport, run an **IPsec VPN over Direct Connect** or enable **MACsec** (Layer 2) on dedicated 10/100 Gbps ports.
* **Total Cost of Ownership (TCO):** Direct Connect has higher upfront costs, but heavily discounted Data Transfer Out (DTO) fees. For high volume (over 10–20 TB/month), DX is often cheaper overall.
* **High Availability Pattern:** Production architectures often use Direct Connect as the primary link with an automated **Site-to-Site VPN connection as a low-cost backup**.

---

## 2. Exam Scenario Decision Matrix

| Scenario Requirement in Question Stem | Correct AWS Service | Key Keywords to Look For |
| :--- | :--- | :--- |
| Quick setup / immediate connection needed | **AWS Site-to-Site VPN** | "Establish connection quickly", "immediate requirement", "setup in minutes" |
| Predictable performance & low latency | **AWS Direct Connect** | "Bypass public internet", "consistent latency", "high/predictable throughput" |
| Dedicated, private physical connection | **AWS Direct Connect** | "Private fiber", "cross-connect", "dedicated connection" |
| Encrypted traffic over public internet | **AWS Site-to-Site VPN** | "Encrypted tunnel", "IPsec", "public internet" |
| Cost optimization for massive data transfer | **AWS Direct Connect** | "Heavy data egress", "terabytes of daily transfer", "reduce bandwidth costs" |
| Cost-effective backup for primary connection | **AWS Site-to-Site VPN** | "Failover link", "secondary backup", "cost-effective redundancy" |

---

## 3. Top Exam Traps & Distractors

1. **"Is Direct Connect encrypted by default?"**
   * **Fact:** **No.** Direct Connect is private, but data travels unencrypted across the physical wire. If an exam prompt requires *private AND encrypted* traffic, select **VPN over Direct Connect** or **MACsec**.
2. **"Which service is cheaper?"**
   * **Fact:** VPN has no upfront cost and is cheaper for low traffic volumes. However, Direct Connect substantially lowers **Data Transfer Out (DTO)** fees for heavy datasets (10+ TB/month).
3. **Implementation Speed**
   * **Fact:** VPN provisions in minutes. Direct Connect takes **weeks to months** due to physical cabling and telecom provider coordination.
4. **Transit Gateway Integration**
   * **Fact:** Both integrate with AWS Transit Gateway, but Direct Connect requires a **Direct Connect Gateway (DXGW)** with a **Transit Virtual Interface (Transit VIF)**.


---

# Understanding AWS Networking Provisioning Time

**Provisioning time** refers to the total elapsed time required to go from scratch to a fully functional connection between an on-premises network and AWS. 

The primary difference between services comes down to **software configuration versus physical infrastructure deployment**.

---

## Provisioning Time Breakdown

| Service | AWS Setup Time | Local / Telecom Setup Time | Total Elapsed Time |
| :--- | :--- | :--- | :--- |
| **AWS Site-to-Site VPN** | **~5 minutes**<br>Creating Virtual Private Gateway and Customer Gateway in AWS. | **~15–30 minutes**<br>Applying AWS-generated configuration to an on-premises firewall/router. | **Minutes to Hours** |
| **AWS Direct Connect** | **1–2 days**<br>AWS approves request and generates a Letter of Authorization (LOA-CFA). | **Weeks to Months**<br>Laying physical fiber, wiring datacenter cross-connects, and provisioning hardware. | **2 to 3 Months** |

---

## Why Direct Connect Takes Weeks to Months

The delay for Direct Connect is driven by real-world physical logistics, not software configuration on the AWS side:

* **Facility Cross-Connects:** Datacenter technicians at an AWS Direct Connect location (e.g., Equinix) must physically run fiber optic cables from AWS's rack to the customer's equipment rack.
* **Telecom Provider Lead Times:** If the on-premises facility is not in the same building as the Direct Connect location, a telecom carrier (e.g., AT&T, Verizon, Lumen) must lease or lay a dedicated physical fiber circuit.
* **Hardware Procurement:** Specialized network routers capable of handling 1 Gbps to 100 Gbps line rates must be ordered, physically installed, and powered on.

---

## AWS Exam Decision Rules

* **Scenario:** *"The company needs an immediate connection within 24–48 hours..."*  
  -> **AWS Site-to-Site VPN** (Physical fiber circuits cannot be provisioned in 24 hours).
* **Scenario:** *"The company has a planned 3-month migration strategy requiring dedicated bandwidth..."*  
  -> **AWS Direct Connect** (Sufficient lead time is available for circuit delivery).