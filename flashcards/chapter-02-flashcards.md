## Chapter 2: NVIDIA's AI Arsenal: Hardware, Software, and Architecture Deep Dive — Flashcards

| # | Front (Question) | Back (Answer) |
|---|-----------------|---------------|
| 1 | What are the three main NVIDIA GPU architecture generations for AI workloads? | Ampere (A100), Hopper (H100), and Blackwell (B100/B200) - each generation improving performance, memory, and efficiency |
| 2 | What is the primary function of CUDA cores in NVIDIA GPUs? | CUDA cores handle general-purpose parallel computing tasks, executing thousands of threads simultaneously for computational workloads |
| 3 | What do Tensor Cores specifically accelerate? | Tensor Cores accelerate deep learning matrix operations (mixed-precision matrix multiply-and-accumulate), dramatically speeding up training and inference |
| 4 | What is Multi-Instance GPU (MIG) and what problem does it solve? | MIG partitions a single GPU into up to 7 isolated instances, enabling secure multi-tenancy and workload isolation on shared infrastructure |
| 5 | What is NVLink and what bandwidth does it provide? | NVLink is a high-speed GPU-to-GPU interconnect providing up to 900 GB/s bidirectional bandwidth (4th gen), far exceeding PCIe speeds |
| 6 | What is the role of NVSwitch in NVIDIA systems? | NVSwitch enables all-to-all GPU communication in multi-GPU systems, connecting up to 8 GPUs with full NVLink bandwidth between any pair |
| 7 | What is a DGX system and what is it designed for? | DGX is NVIDIA's integrated AI supercomputing system, purpose-built for enterprise AI training and inference with pre-configured hardware and software |
| 8 | What is the purpose of TensorRT in the NVIDIA software stack? | TensorRT optimizes trained neural networks for inference, applying techniques like layer fusion, precision calibration, and kernel auto-tuning |
| 9 | What is Triton Inference Server used for? | Triton Inference Server deploys and serves AI models at scale, supporting multiple frameworks and enabling dynamic batching and model versioning |
| 10 | What does the NGC Catalog provide? | NGC Catalog offers GPU-optimized containers, pre-trained models, and SDKs for AI workflows, eliminating complex environment setup |
| 11 | What is NVIDIA AI Enterprise? | A production-ready software platform providing enterprise support, security, and certified AI tools for deploying AI in business environments |
| 12 | How does HGX differ from DGX? | HGX is a GPU baseboard/reference design for OEMs to build custom systems, while DGX is NVIDIA's complete turnkey AI system |
| 13 | When should you choose training-focused hardware vs inference hardware? | Training requires maximum compute and memory (H100/A100 with NVLink); inference prioritizes efficiency, latency, and cost (L4, L40S, or MIG partitions) |
| 14 | What is cuDNN and why is it important? | cuDNN is a GPU-accelerated library of primitives for deep neural networks, providing optimized implementations of convolutions, pooling, and activations |
| 15 | What are RT cores designed for? | RT cores accelerate ray tracing operations, primarily for graphics but also useful for physics simulations and certain AI visualization tasks |

### Key Terms

| Term | Definition |
|------|-----------|
| Tensor Core | Specialized processing units designed to accelerate matrix math operations used in deep learning training and inference |
| MIG (Multi-Instance GPU) | Technology allowing a single GPU to be partitioned into multiple isolated instances for secure multi-tenant workloads |
| NVLink | High-bandwidth, low-latency direct GPU-to-GPU interconnect technology surpassing PCIe performance |
| NVSwitch | Chip enabling full-bandwidth NVLink connections between all GPUs in a multi-GPU configuration |
| Triton Inference Server | Open-source inference serving software for deploying trained AI models with support for multiple frameworks |
| NGC Catalog | NVIDIA's repository of GPU-optimized containers, pre-trained models, and AI development tools |
| TensorRT | Deep learning inference optimizer and runtime delivering low latency and high throughput |

### Memory Tricks
- **"CTR" for GPU cores**: **C**UDA (general compute), **T**ensor (deep learning), **R**T (ray tracing) - ordered by AI relevance
- **"MIG = Multiple Isolated GPUs"**: Remember MIG creates virtual separate GPUs from one physical GPU for multi-tenancy
- **"NVLink is the LINK, NVSwitch is the SWITCH"**: Link connects pairs, Switch connects ALL GPUs like a network switch
- **"DGX = Done, HGX = Homebrew"**: DGX is complete/turnkey, HGX is for building your own system
- **"Train with TANKS (big), Infer with TANKS (efficient)"**: Training needs maximum power, inference needs optimization