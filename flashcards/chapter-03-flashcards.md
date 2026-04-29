## Chapter 3: Building the AI Data Center: Infrastructure Design and Scalability — Flashcards

| # | Front (Question) | Back (Answer) |
|---|-----------------|---------------|
| 1 | Why is InfiniBand preferred over Ethernet for AI training clusters? | InfiniBand provides lower latency (sub-microsecond), higher bandwidth (up to 400 Gb/s), and RDMA capabilities essential for GPU-to-GPU communication in distributed training workloads |
| 2 | What is GPUDirect Storage and what problem does it solve? | GPUDirect Storage enables direct data transfer between NVMe storage and GPU memory, bypassing the CPU and system memory to eliminate bottlenecks and reduce latency |
| 3 | What is the role of NVIDIA BlueField DPUs in AI data centers? | BlueField DPUs offload infrastructure tasks (networking, security, storage) from CPUs, freeing compute resources for AI workloads and accelerating data center operations |
| 4 | What is the typical power consumption range for a high-density GPU server? | Modern high-density GPU servers can consume 10-20+ kW per server, with individual GPUs like H100 drawing 700W TDP |
| 5 | What is the difference between vertical and horizontal scaling for AI infrastructure? | Vertical scaling adds more resources to existing nodes (more GPUs per server); horizontal scaling adds more nodes to the cluster |
| 6 | What is RDMA and why is it critical for AI workloads? | Remote Direct Memory Access allows direct memory access between systems without CPU involvement, enabling ultra-low latency communication essential for distributed training |
| 7 | What are the three main components of power distribution in AI data centers? | Uninterruptible Power Supply (UPS), Power Distribution Units (PDUs), and facility transformers/switchgear |
| 8 | What cooling approach is increasingly necessary for high-density AI racks? | Liquid cooling (direct-to-chip or immersion cooling) because air cooling cannot adequately dissipate 30-50+ kW per rack densities |
| 9 | What is a parallel file system and why is it used for AI storage? | A distributed file system (like Lustre, GPFS, or VAST) that stripes data across multiple servers for high throughput and concurrent access needed by multi-GPU training |
| 10 | How does vGPU technology enable GPU virtualization? | vGPU partitions a physical GPU into multiple virtual GPUs, allowing multiple VMs to share GPU resources with isolated memory and compute |
| 11 | What Kubernetes component enables GPU scheduling for AI workloads? | NVIDIA GPU Operator and Device Plugin, which discover GPUs and expose them as schedulable resources to the Kubernetes scheduler |
| 12 | What are the key metrics for calculating AI cluster network bandwidth requirements? | Model size, batch size, number of GPUs, gradient synchronization frequency, and chosen parallelism strategy (data/model/pipeline) |
| 13 | What is the purpose of GPUDirect RDMA? | Enables direct data transfer between GPUs across different nodes via network adapters, bypassing host CPU and memory for faster multi-node communication |
| 14 | What factors favor on-premises over cloud for AI workloads? | Consistent high utilization, data sovereignty requirements, predictable long-term costs, and need for specialized hardware configurations |
| 15 | What are common performance bottleneck indicators in AI infrastructure? | GPU utilization below 80%, high PCIe bus wait times, network congestion alerts, storage I/O wait states, and thermal throttling |

### Key Terms

| Term | Definition |
|------|-----------|
| InfiniBand | High-performance networking technology providing low latency and high bandwidth for HPC and AI clusters |
| BlueField DPU | Data Processing Unit that offloads networking, storage, and security tasks from CPUs in data centers |
| GPUDirect | Suite of technologies enabling direct data paths to/from GPUs, bypassing CPU bottlenecks |
| RDMA | Remote Direct Memory Access - enables direct memory-to-memory transfers between systems |
| NVMe | Non-Volatile Memory Express - high-speed storage protocol designed for SSDs |
| PUE | Power Usage Effectiveness - ratio of total facility power to IT equipment power (lower is better) |
| vGPU | Virtual GPU technology allowing GPU sharing across multiple virtual machines |

### Memory Tricks
- **IB for AI**: **I**nfini**B**and = **I**ncredible **B**andwidth for training clusters
- **DPU = Data's Personal Uber**: DPU takes infrastructure work off the CPU's hands, like a dedicated driver
- **GPUDirect trio**: Storage, RDMA, P2P - think "**S**peedy **R**oads for **P**arallel" data movement
- **Cooling rule of thumb**: "Liquid for Limits" - when air hits its limits, liquid cooling takes over