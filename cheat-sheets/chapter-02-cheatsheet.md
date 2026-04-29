## Chapter 2: NVIDIA's AI Arsenal: Hardware, Software, and Architecture Deep Dive — Quick Reference

### Core Concepts
| Concept | One-line explanation |
|---------|---------------------|
| CUDA Cores | Parallel processors handling general-purpose GPU computations |
| Tensor Cores | Specialized cores accelerating matrix operations for deep learning (mixed-precision) |
| RT Cores | Ray tracing cores for graphics workloads (not AI-focused) |
| MIG (Multi-Instance GPU) | Partitions single GPU into isolated instances for multi-tenancy |
| NVLink | High-bandwidth direct GPU-to-GPU interconnect (up to 900 GB/s on Hopper) |
| NVSwitch | Fabric switch enabling all-to-all GPU communication in multi-GPU systems |
| DGX Systems | Turnkey AI supercomputers with integrated hardware, software, and support |
| NGC Catalog | Repository of GPU-optimized containers, models, and AI software |
| NVIDIA AI Enterprise | Production-grade, enterprise-supported AI software platform |

### Key Syntax / Commands
```
# MIG Management
nvidia-smi mig -cgi 9,9,9 -C          # Create 3 MIG instances
nvidia-smi mig -lgi                    # List GPU instances
nvidia-smi mig -dci && nvidia-smi mig -dgi  # Destroy instances

# NGC Container Pull
docker pull nvcr.io/nvidia/pytorch:24.01-py3
```

### Common Patterns
**Pattern 1: Training Workload Selection**
Large models → DGX/HGX with NVLink for multi-GPU scaling; prioritize memory bandwidth

**Pattern 2: Inference Workload Selection**
Production inference → TensorRT optimization + Triton Server; consider MIG for consolidation

### Things to Remember
✅ Ampere → Hopper → Blackwell: each generation increases Tensor Core performance & memory
✅ MIG requires Ampere+ (A100, H100); enables up to 7 isolated instances per GPU
✅ NVLink for training scalability; PCIe often sufficient for single-GPU inference
❌ Don't use MIG for workloads requiring full GPU memory—partitioning reduces per-instance resources

### Quick Quiz
1. Which core type accelerates matrix math in neural networks? → **Tensor Cores**
2. What technology isolates GPU resources for multi-tenancy? → **MIG (Multi-Instance GPU)**
3. DGX vs HGX: which is a complete system vs reference design? → **DGX = complete system; HGX = board/reference for OEMs**