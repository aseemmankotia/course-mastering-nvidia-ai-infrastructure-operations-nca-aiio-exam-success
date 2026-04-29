## Chapter 3: Building the AI Data Center: Infrastructure Design and Scalability — Practice Questions

### Multiple Choice

**Q1.** A company is designing an AI data center and needs to choose a networking technology for training large language models across 256 GPUs. The workload requires extremely low latency and high bandwidth for frequent gradient synchronization. Which networking technology should they prioritize?

A) Standard 1 Gigabit Ethernet
B) InfiniBand
C) Wi-Fi 6E
D) 10 Gigabit Ethernet with TCP/IP

<details>
<summary>Answer</summary>

**Correct: B**

InfiniBand is specifically designed for high-performance computing environments and provides the ultra-low latency and high bandwidth required for distributed AI training workloads. Standard 1 Gigabit Ethernet (A) lacks sufficient bandwidth. While 10 Gigabit Ethernet (D) offers more bandwidth than 1 Gigabit, it still has higher latency than InfiniBand due to TCP/IP overhead. Wi-Fi 6E (C) is a wireless technology unsuitable for data center interconnects requiring consistent, high-performance connections.

</details>

---

**Q2.** What is the primary function of NVIDIA BlueField DPUs in a data center environment?

A) Increasing GPU memory capacity
B) Offloading infrastructure tasks from the CPU to accelerate data center operations
C) Providing additional display outputs for visualization
D) Replacing traditional hard drives for storage

<details>
<summary>Answer</summary>

**Correct: B**

NVIDIA BlueField DPUs (Data Processing Units) are designed to offload and accelerate infrastructure tasks such as networking, storage, and security functions from the CPU. This frees the CPU and GPU to focus on compute-intensive AI workloads. BlueField DPUs do not increase GPU memory (A), provide display outputs (C), or replace storage drives (D).

</details>

---

**Q3.** An AI team needs to load training datasets directly into GPU memory without involving the CPU, reducing data transfer bottlenecks. Which technology enables this capability?

A) Traditional SATA connections
B) GPUDirect Storage
C) USB 3.0 external drives
D) Network Attached Storage over SMB

<details>
<summary>Answer</summary>

**Correct: B**

GPUDirect Storage enables direct data transfers between storage devices and GPU memory, bypassing the CPU entirely. This significantly reduces latency and increases throughput for data-intensive AI workloads. SATA connections (A), USB drives (C), and NAS over SMB (D) all require CPU involvement in data transfers and introduce additional latency.

</details>

---

**Q4.** When calculating resource requirements for an AI training cluster, which combination of factors is MOST important to consider together?

A) Office space, employee count, and software licenses
B) GPU count, memory capacity, and network bandwidth
C) Monitor resolution, keyboard type, and mouse sensitivity
D) Building location, parking availability, and cafeteria size

<details>
<summary>Answer</summary>

**Correct: B**

GPU count, memory capacity, and network bandwidth are the three critical factors that directly impact AI training performance. The number of GPUs determines compute capacity, memory affects model size and batch processing, and network bandwidth impacts how efficiently multiple GPUs can communicate during distributed training. The other options (A, C, D) are unrelated to technical resource planning for AI workloads.

</details>

---

**Q5.** A startup is deciding between cloud-based and on-premises infrastructure for their AI workloads. They have unpredictable workloads that spike during product launches and minimal IT staff. Which deployment model would BEST suit their needs?

A) On-premises with custom-built servers
B) Cloud-based infrastructure
C) Colocation with no managed services
D) Personal workstations for each team member

<details>
<summary>Answer</summary>

**Correct: B**

Cloud-based infrastructure is ideal for organizations with unpredictable, variable workloads and limited IT staff because it offers elastic scaling (pay for what you use), managed services that reduce operational burden, and no upfront capital expenditure. On-premises (A) and colocation (C) require significant upfront investment and dedicated IT staff. Personal workstations (D) cannot handle enterprise AI workloads.

</details>

---

### True / False

**Q6.** Horizontal scaling in AI infrastructure means adding more powerful components to existing servers, such as upgrading to faster GPUs. — **True / False**

<details>
<summary>Answer</summary>

**False**

This statement describes vertical scaling, not horizontal scaling. Horizontal scaling means adding more servers or nodes to distribute the workload across multiple machines. Vertical scaling involves upgrading individual components (like replacing GPUs with more powerful ones) within existing servers. Understanding this distinction is important for scalability planning in AI infrastructure.

</details>

---

**Q7.** High-density GPU environments typically require specialized cooling solutions because GPUs generate significantly more heat than traditional data center equipment. — **True / False**

<details>
<summary>Answer</summary>

**True**

Modern AI GPUs can consume 300-700 watts each, generating substantial heat in concentrated areas. High-density GPU racks may require 30-50+ kW of cooling per rack, compared to 5-10 kW for traditional server racks. This necessitates specialized cooling solutions such as liquid cooling, rear-door heat exchangers, or direct-to-chip cooling to maintain safe operating temperatures and prevent thermal throttling.

</details>

---

### Short Answer

**Q8.** Explain the difference between vGPU technology and using Kubernetes with GPU support for AI workloads.

<details>
<summary>Answer</summary>

vGPU (virtual GPU) technology allows a single physical GPU to be partitioned into multiple virtual GPUs, enabling multiple virtual machines to share GPU resources simultaneously. Each VM receives a dedicated portion of GPU memory and compute capability.

Kubernetes with GPU support orchestrates containerized AI workloads across a cluster, scheduling entire physical GPUs (or portions via technologies like MIG) to containers. It focuses on workload orchestration, scaling, and management rather than hardware virtualization.

vGPU is typically used in virtualized environments where multiple users need isolated GPU access, while Kubernetes is preferred for container-based microservices and scalable AI inference deployments.

</details>

---

**Q9.** What is a parallel file system and why is it important for AI storage architectures?

<details>
<summary>Answer</summary>

A parallel file system distributes data across multiple storage servers and allows simultaneous read/write operations from many clients. Examples include Lustre, GPFS, and BeeGFS.

It is important for AI storage because:
1. AI training requires feeding large datasets to multiple GPUs simultaneously
2. Single storage servers cannot provide enough bandwidth for dozens or hundreds of GPUs
3. Parallel file systems aggregate bandwidth from multiple servers, enabling throughput of hundreds of gigabytes per second
4. This prevents storage from becoming a bottleneck during data-intensive training operations

</details>

---

### Scenario-Based

**Q10.** DataTech Corporation is experiencing performance issues with their newly deployed AI training cluster. The cluster consists of 64 NVIDIA A100 GPUs across 8 servers, connected via 100 Gigabit Ethernet. Training jobs that should complete in 4 hours are taking 12+ hours. Monitoring shows GPU utilization averaging only 35%, while network utilization spikes to 100% during gradient synchronization phases. Storage throughput appears adequate.

Based on this scenario, answer the following:

a) What is the most likely cause of the performance bottleneck?
b) What infrastructure change would you recommend to address this issue?
c) What metric should they monitor after implementing the change to verify improvement?

<details>
<summary>Answer</summary>

**a) Most likely cause:** The network is the bottleneck. The symptoms clearly indicate this: GPU utilization is low (35%) because GPUs are waiting idle during network-bound gradient synchronization, while network utilization hits 100%. During distributed training, GPUs must frequently exchange gradient information, and insufficient network bandwidth creates a chokepoint that leaves expensive GPUs underutilized.

**b) Recommended infrastructure change:** Upgrade to InfiniBand networking (such as HDR InfiniBand at 200 Gbps or NDR at 400 Gbps). InfiniBand provides significantly higher bandwidth and lower latency than Ethernet, which is critical for the frequent, synchronization-heavy communication patterns in distributed AI training. Alternatively, if staying with Ethernet, upgrade to 200 or 400 Gigabit Ethernet with RDMA over Converged Ethernet (RoCE).

**c) Metrics to monitor:** After implementing the change, monitor:
- GPU utilization (should increase significantly, ideally above 80%)
- Training throughput (samples processed per second)
- Network utilization (should show headroom rather than constant 100%)
- Training job completion times (should approach the expected 4-hour target)

</details>

---