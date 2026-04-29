# Exploring NVIDIA GPU Properties with CUDA
# This example shows how to query GPU information using Python
# Demonstrates understanding of GPU architectures and their capabilities

import subprocess
import sys

# First, let's check if we can access GPU info via nvidia-smi
def get_gpu_info_nvidia_smi():
    """
    Use nvidia-smi to get basic GPU information.
    nvidia-smi is NVIDIA's System Management Interface - 
    a command-line tool for monitoring and managing NVIDIA GPUs.
    """
    try:
        # Run nvidia-smi command to get GPU details
        result = subprocess.run(
            ['nvidia-smi', '--query-gpu=name,memory.total,compute_cap,driver_version', 
             '--format=csv,noheader'],
            capture_output=True, 
            text=True
        )
        if result.returncode == 0:
            return result.stdout.strip()
        else:
            return "nvidia-smi not available or no GPU detected"
    except FileNotFoundError:
        return "nvidia-smi not found - NVIDIA drivers may not be installed"

# Try using PyTorch to get GPU information (if available)
def get_gpu_info_pytorch():
    """
    Use PyTorch's CUDA interface to explore GPU properties.
    PyTorch provides a Python-friendly way to access CUDA functionality.
    """
    try:
        import torch
        
        if not torch.cuda.is_available():
            return "CUDA not available through PyTorch"
        
        gpu_info = []
        
        # Get number of available GPUs
        num_gpus = torch.cuda.device_count()
        gpu_info.append(f"Number of GPUs available: {num_gpus}")
        
        for i in range(num_gpus):
            props = torch.cuda.get_device_properties(i)
            gpu_info.append(f"\n--- GPU {i}: {props.name} ---")
            gpu_info.append(f"  Total Memory: {props.total_memory / 1024**3:.2f} GB")
            gpu_info.append(f"  Compute Capability: {props.major}.{props.minor}")
            gpu_info.append(f"  Multi-Processor Count: {props.multi_processor_count}")
            
            # Compute capability tells us the GPU generation:
            # 8.0 = Ampere (A100), 8.6 = Ampere (RTX 30xx)
            # 9.0 = Hopper (H100)
            # Higher compute capability = newer architecture with more features
            
            arch_name = "Unknown"
            if props.major == 7:
                arch_name = "Volta/Turing"
            elif props.major == 8:
                arch_name = "Ampere"
            elif props.major == 9:
                arch_name = "Hopper"
            elif props.major >= 10:
                arch_name = "Blackwell or newer"
            
            gpu_info.append(f"  Architecture: {arch_name}")
        
        return "\n".join(gpu_info)
        
    except ImportError:
        return "PyTorch not installed"

# Main execution
if __name__ == "__main__":
    print("=" * 60)
    print("NVIDIA GPU Information Explorer")
    print("=" * 60)
    
    print("\n[Method 1: Using nvidia-smi]")
    print(get_gpu_info_nvidia_smi())
    
    print("\n[Method 2: Using PyTorch CUDA]")
    print(get_gpu_info_pytorch())
    
    print("\n" + "=" * 60)
    print("Key Concepts:")
    print("- CUDA Cores: Parallel processors for general computation")
    print("- Tensor Cores: Specialized for matrix operations (AI/ML)")
    print("- Compute Capability: Indicates GPU generation and features")
    print("=" * 60)