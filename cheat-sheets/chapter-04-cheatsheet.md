## Chapter 4: AI Operations Excellence: Monitoring, Orchestration, and MLOps — Quick Reference

### Core Concepts
| Concept | One-line explanation |
|---------|---------------------|
| NVIDIA DCGM | Centralized tool for monitoring, managing, and collecting telemetry from data center GPUs |
| GPU Metrics | Key indicators: utilization %, memory usage, temperature, power draw, ECC errors |
| Slurm | HPC workload manager for scheduling and managing jobs across GPU clusters |
| Kubernetes GPU Operator | Automates deployment of NVIDIA software components for GPU support in K8s |
| NVIDIA Device Plugin | Enables Kubernetes to discover and schedule GPUs as resources |
| MLOps | Practices for reliable, reproducible, and maintainable production AI systems |
| Environment Management | Separate dev/staging/prod environments with consistent configurations |

### Key Syntax / Commands
```bash
# DCGM monitoring
dcgmi discovery -l                    # List all GPUs
dcgmi dmon -e 203,204,1001           # Monitor utilization, memory, temp
dcgmi health -c                       # Check GPU health status
dcgmi diag -r 3                       # Run diagnostic (level 1-3)

# Slurm GPU scheduling
srun --gres=gpu:2 ./train.sh         # Request 2 GPUs
sbatch --gres=gpu:a100:4 job.slurm   # Submit job with 4 A100s

# Kubernetes GPU resources
kubectl describe node | grep nvidia   # Check GPU allocation
kubectl logs -n gpu-operator <pod>    # Debug GPU Operator
```

### Common Patterns
**Pattern 1: GPU Resource Request (Kubernetes)**
```yaml
resources:
  limits:
    nvidia.com/gpu: 1
```

**Pattern 2: DCGM + Prometheus Integration**
Deploy `dcgm-exporter` as DaemonSet → Prometheus scrapes metrics → Grafana dashboards

**Pattern 3: Environment Promotion Pipeline**
Dev (experiment) → Staging (validate) → Production (deploy with rollback capability)

### Things to Remember
✅ DCGM provides health checks, diagnostics, and policy-based management at scale
✅ GPU Operator manages driver, runtime, device plugin, and monitoring as a stack
✅ MLOps requires version control for code, data, models, AND environments
✅ Always test driver updates in staging before production rollout
❌ Don't schedule GPU workloads without resource limits—causes contention
❌ Don't ignore ECC errors—they indicate potential hardware failure

### Quick Quiz
1. What DCGM command runs GPU diagnostics? → `dcgmi diag -r <level>`
2. How do you request GPUs in Slurm? → `--gres=gpu:<type>:<count>`
3. What component lets K8s see GPUs? → NVIDIA Device Plugin
4. Three MLOps pillars? → Reproducibility, versioning, continuous training