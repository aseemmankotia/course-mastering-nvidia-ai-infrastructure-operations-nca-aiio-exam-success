## Chapter 3: Building the AI Data Center: Infrastructure Design and Scalability — Quick Reference

### Core Concepts
| Concept | One-line explanation |
|---------|---------------------|
| InfiniBand | High-bandwidth, low-latency fabric preferred for AI training clusters (400Gb/s+) |
| GPUDirect Storage | Enables direct data path between NVMe/storage and GPU memory, bypassing CPU |
| GPUDirect RDMA | Allows direct GPU-to-GPU communication across network without CPU involvement |
| BlueField DPU | Data Processing Unit that offloads networking, security, and storage tasks from CPU |
| vGPU | NVIDIA virtualization technology allowing multiple VMs to share a single GPU |
| Parallel File Systems | Distributed storage (Lustre, GPFS, WekaFS) for high-throughput AI workloads |
| Power Density | Modern GPU racks require 40-100+ kW per rack vs traditional 5-10 kW |

### Key Specifications
```
Power Per GPU:        H100 SXM = 700W, A100 = 400W, H200 = 700W
InfiniBand Speeds:    HDR = 200Gb/s, NDR = 400Gb/s, XDR = 800Gb/s
NVLink Bandwidth:     900 GB/s (H100), enables GPU-to-GPU within node
Cooling Options:      Air, Direct Liquid Cooling (DLC), Immersion
Typical PUE Target:   1.2-1.4 for AI data centers
```

### Common Patterns
**Pattern 1: Training Cluster Design**
InfiniBand fabric → NVLink within nodes → GPUDirect RDMA between nodes → Parallel file system backend

**Pattern 2: Inference Deployment**
Ethernet networking acceptable → Kubernetes + GPU operator → vGPU for multi-tenancy → NVMe local storage

### Things to Remember
✅ InfiniBand for training (latency-sensitive), Ethernet acceptable for inference
✅ Plan 1.5-2x power headroom for future GPU generations
✅ BlueField DPUs free CPU cores by offloading network/storage/security functions
✅ GPUDirect technologies eliminate CPU bottlenecks in data movement
❌ Don't underestimate cooling—liquid cooling often required for dense GPU deployments

### Quick Quiz
1. When to choose InfiniBand over Ethernet? → Training clusters requiring low latency and high collective operation performance
2. What does GPUDirect Storage eliminate? → CPU involvement in storage-to-GPU data transfers
3. Horizontal vs Vertical scaling? → Horizontal = more nodes; Vertical = more GPUs/resources per node