## Chapter 4: AI Operations Excellence: Monitoring, Orchestration, and MLOps — Practice Questions

### Multiple Choice

**Q1.** Your data center team needs to monitor GPU health across 50 servers running AI training workloads. Which NVIDIA tool is specifically designed for datacenter-scale GPU monitoring and management?

A) NVIDIA Control Panel
B) NVIDIA Data Center GPU Manager (DCGM)
C) GeForce Experience
D) NVIDIA System Management Interface (nvidia-smi) only

<details>
<summary>Answer</summary>

**Correct: B**

NVIDIA Data Center GPU Manager (DCGM) is specifically designed for managing and monitoring GPUs in datacenter environments at scale. While nvidia-smi (D) is useful for basic GPU queries, DCGM provides comprehensive monitoring, health checks, and integration with enterprise monitoring systems. NVIDIA Control Panel (A) and GeForce Experience (C) are consumer-focused tools not designed for datacenter operations.

</details>

---

**Q2.** An AI operations engineer notices that training jobs are running slower than expected. Which GPU metric should they check FIRST to identify if the GPU is being fully utilized?

A) GPU serial number
B) Driver version
C) GPU utilization percentage
D) GPU manufacturing date

<details>
<summary>Answer</summary>

**Correct: C**

GPU utilization percentage shows how much of the GPU's compute capacity is being used. Low utilization during training often indicates bottlenecks elsewhere (CPU, storage, data loading). The serial number (A), driver version (B), and manufacturing date (D) are informational but don't directly indicate performance issues.

</details>

---

**Q3.** Which job scheduling system is most commonly used for managing AI and HPC workloads across clusters of GPU-equipped servers?

A) Windows Task Scheduler
B) Cron
C) Slurm
D) Apple Automator

<details>
<summary>Answer</summary>

**Correct: C**

Slurm (Simple Linux Utility for Resource Management) is the industry-standard workload manager for HPC and AI clusters. It handles job queuing, resource allocation (including GPUs), and scheduling across many nodes. Windows Task Scheduler (A), Cron (B), and Apple Automator (D) are designed for single-machine task scheduling and lack cluster management capabilities.

</details>

---

**Q4.** In a Kubernetes environment with NVIDIA GPUs, which component allows pods to request and use GPU resources?

A) NVIDIA Control Panel
B) NVIDIA Device Plugin for Kubernetes
C) Docker Desktop
D) VMware vSphere

<details>
<summary>Answer</summary>

**Correct: B**

The NVIDIA Device Plugin for Kubernetes enables GPU resource discovery and allocation to pods. It allows containers to request GPUs using standard Kubernetes resource specifications. NVIDIA Control Panel (A) is for desktop use, Docker Desktop (C) is a development tool, and VMware vSphere (D) is virtualization software that doesn't directly handle Kubernetes GPU scheduling.

</details>

---

**Q5.** A company wants to ensure their AI models can be retrained with exactly the same results. Which MLOps principle directly addresses this requirement?

A) Cost optimization
B) Reproducibility
C) Marketing alignment
D) Office layout planning

<details>
<summary>Answer</summary>

**Correct: B**

Reproducibility is the MLOps principle that ensures experiments and training runs can be repeated with identical results. This requires tracking code versions, data versions, hyperparameters, and environment configurations. Cost optimization (A) relates to efficiency, while marketing alignment (C) and office layout planning (D) are unrelated to MLOps principles.

</details>

---

### True / False

**Q6.** GPU temperature monitoring is unnecessary in modern data centers because newer GPUs cannot overheat. — **True / False**

<details>
<summary>Answer</summary>

**False**

GPU temperature monitoring is critical in data centers. While modern GPUs have thermal protection features, sustained high temperatures can trigger throttling (reducing performance), cause hardware degradation over time, or lead to unexpected shutdowns. Monitoring temperature helps identify cooling issues before they impact operations.

</details>

---

**Q7.** In MLOps, having separate development, staging, and production environments helps prevent untested changes from affecting live AI services. — **True / False**

<details>
<summary>Answer</summary>

**True**

Separating environments is a fundamental MLOps best practice. Development environments allow experimentation without risk, staging environments enable testing with production-like conditions, and production environments serve actual users. This separation ensures that bugs, misconfigurations, or poorly performing models are caught before impacting live services.

</details>

---

### Short Answer

**Q8.** List three key GPU metrics that should be monitored in a production AI environment.

<details>
<summary>Answer</summary>

Any three of the following are acceptable:
- GPU utilization (percentage of compute capacity in use)
- Memory usage (how much GPU memory is consumed)
- Temperature (thermal status of the GPU)
- Power draw (electrical power consumption)
- Error counts (ECC errors or other hardware issues)
- Clock speeds (current operating frequency)

</details>

---

**Q9.** What is the purpose of versioning in MLOps, and what types of artifacts should be versioned?

<details>
<summary>Answer</summary>

Versioning in MLOps tracks changes over time to enable reproducibility, rollback capabilities, and collaboration. Artifacts that should be versioned include:
- Training code and scripts
- Datasets (or references to specific data versions)
- Model weights and checkpoints
- Configuration files and hyperparameters
- Environment specifications (dependencies, container images)

</details>

---

### Scenario-Based

**Q10.** You are an AI operations engineer at a healthcare company. On Monday morning, you receive alerts that your production AI inference service is responding slowly. Initial investigation shows GPU utilization is only at 15%, memory usage is at 90%, and there are no temperature issues. Users report that the service was working fine on Friday.

Based on this scenario, answer the following:

a) What does the combination of low GPU utilization and high memory usage suggest?
b) What change might have occurred over the weekend to cause this issue?
c) What immediate action should you take, and what MLOps practice could have prevented this situation?

<details>
<summary>Answer</summary>

a) Low GPU utilization (15%) combined with high memory usage (90%) suggests a memory bottleneck. The GPU cannot process efficiently because it's nearly out of memory, causing it to wait for memory operations rather than computing.

b) Possible weekend changes include: a model update that uses more memory, a new software deployment with a larger model, a batch size configuration change, or memory leaks from accumulated requests over time.

c) Immediate actions:
- Rollback to the last known good configuration/model version
- Restart the service to clear any memory leaks
- Reduce batch size if applicable

MLOps practices that could have prevented this:
- Staging environment testing before production deployment
- Automated performance testing in CI/CD pipelines
- Model versioning with easy rollback capability
- Change management procedures requiring approval for weekend deployments

</details>

---