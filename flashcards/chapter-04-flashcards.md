## Chapter 4: AI Operations Excellence: Monitoring, Orchestration, and MLOps — Flashcards

| # | Front (Question) | Back (Answer) |
|---|-----------------|---------------|
| 1 | What is NVIDIA Data Center GPU Manager (DCGM)? | A suite of tools for managing and monitoring NVIDIA GPUs in cluster environments, providing health monitoring, diagnostics, and policy-based governance |
| 2 | What are the five key GPU metrics monitored by DCGM? | Utilization, memory usage, temperature, power draw, and errors (ECC/XID) |
| 3 | What is Slurm and what is it used for? | Simple Linux Utility for Resource Management - a job scheduler for HPC and AI workloads that allocates compute resources and manages job queues |
| 4 | What is the NVIDIA GPU Operator in Kubernetes? | An operator that automates the management of all NVIDIA software components needed to provision and manage GPUs in Kubernetes clusters |
| 5 | What does the NVIDIA Device Plugin for Kubernetes do? | Enables Kubernetes to discover, advertise, and schedule GPUs as resources to containers in pods |
| 6 | What are the three core MLOps principles for production AI? | Reproducibility, versioning, and continuous training |
| 7 | What are the three standard AI environments in a deployment pipeline? | Development, staging, and production |
| 8 | What ECC errors should trigger immediate attention in GPU monitoring? | Uncorrectable ECC errors (DBE - Double Bit Errors), as they indicate potential hardware failure |
| 9 | How does Slurm integrate with GPUs for AI workloads? | Through GRES (Generic RESource) configuration that allows requesting specific GPU types and quantities in job submissions |
| 10 | What is continuous training in MLOps? | The practice of automatically retraining models when new data becomes available or model performance degrades |
| 11 | What strategy minimizes downtime during driver updates on GPU clusters? | Rolling updates - updating nodes one at a time while workloads migrate to other nodes |
| 12 | What XID errors indicate GPU memory issues? | XID 48 (DBE - Double Bit ECC Error) and XID 63 (Row Remapping Failure) |
| 13 | What is the purpose of model versioning in MLOps? | To track model iterations, enable rollbacks, ensure reproducibility, and maintain audit trails for compliance |
| 14 | What Kubernetes resource request specifies GPU requirements? | `nvidia.com/gpu: N` in the container's resource limits/requests specification |
| 15 | What is the recommended approach for GPU virtualization in enterprise environments? | NVIDIA vGPU (Virtual GPU) technology, which allows multiple VMs to share a single physical GPU with guaranteed resources |

### Key Terms

| Term | Definition |
|------|-----------|
| DCGM | NVIDIA Data Center GPU Manager - comprehensive monitoring and management tool for datacenter GPUs |
| Slurm | Open-source job scheduler widely used in HPC for resource allocation and workload management |
| GPU Operator | Kubernetes operator that automates GPU driver, container runtime, and device plugin deployment |
| MLOps | Practices combining ML, DevOps, and data engineering to deploy and maintain ML systems in production |
| GRES | Generic RESource in Slurm - mechanism for scheduling consumable resources like GPUs |
| XID Error | NVIDIA GPU error code system that identifies specific hardware or software issues |
| vGPU | NVIDIA virtualization technology enabling GPU sharing across multiple virtual machines |

### Memory Tricks
- **DCGM metrics = "U-M-T-P-E"**: Utilization, Memory, Temperature, Power, Errors - think "You Must Track Performance Exactly"
- **Three MLOps R-V-C**: Reproducibility, Versioning, Continuous training - "Real Valuable Code" for production ML
- **Environment pipeline "D-S-P"**: Development → Staging → Production - "Don't Skip Production-readiness"
- **GPU Operator components = "DRDC"**: Driver, Runtime, Device plugin, Container toolkit - "Drivers Run Docker Containers"