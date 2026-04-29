#!/usr/bin/env python3
"""
GPU Metrics Monitoring Basics

This example demonstrates how to monitor key GPU metrics that NVIDIA DCGM tracks.
We use pynvml (NVIDIA Management Library) which provides similar functionality
to what DCGM offers at a higher level.

Key metrics covered:
- GPU Utilization (how busy the GPU is)
- Memory Usage (how much VRAM is being used)
- Temperature (important for thermal management)
- Power Draw (energy consumption)
"""

import time
from datetime import datetime

# Note: In a real environment, install with: pip install pynvml
# For this example, we'll simulate the metrics for learning purposes

class GPUMetricsSimulator:
    """
    Simulates GPU metrics for learning purposes.
    In production, you would use pynvml or DCGM APIs.
    """
    
    def __init__(self, gpu_id=0):
        self.gpu_id = gpu_id
        self.gpu_name = "NVIDIA A100-SXM4-40GB"  # Simulated GPU
        
    def get_utilization(self):
        """Get GPU utilization percentage (0-100%)"""
        # Simulated value - in reality, this shows compute usage
        import random
        return random.randint(45, 95)
    
    def get_memory_info(self):
        """Get memory usage in MB"""
        # Simulated: total 40GB, used varies
        import random
        total_mb = 40960  # 40 GB in MB
        used_mb = random.randint(8000, 35000)
        return {
            'total': total_mb,
            'used': used_mb,
            'free': total_mb - used_mb
        }
    
    def get_temperature(self):
        """Get GPU temperature in Celsius"""
        import random
        return random.randint(55, 85)
    
    def get_power_draw(self):
        """Get power consumption in Watts"""
        import random
        return random.randint(200, 400)


def monitor_gpu_metrics(duration_seconds=30, interval_seconds=5):
    """
    Monitor GPU metrics over a period of time.
    
    This is similar to what DCGM does continuously in a data center.
    DCGM can collect over 1000 different metrics from GPUs!
    
    Args:
        duration_seconds: How long to monitor
        interval_seconds: Time between measurements
    """
    print("="*60)
    print("GPU METRICS MONITORING DASHBOARD")
    print("Similar to NVIDIA DCGM (Data Center GPU Manager)")
    print("="*60)
    
    # Initialize our GPU monitor (simulator for learning)
    gpu = GPUMetricsSimulator(gpu_id=0)
    
    # Store metrics for analysis
    metrics_history = []
    
    # Define thresholds for alerts (like DCGM policies)
    TEMP_WARNING = 80  # Celsius
    MEMORY_WARNING = 90  # Percent
    
    start_time = time.time()
    
    print(f"\nMonitoring GPU: {gpu.gpu_name}")
    print(f"Duration: {duration_seconds} seconds, Interval: {interval_seconds} seconds\n")
    
    while (time.time() - start_time) < duration_seconds:
        # Collect current metrics
        timestamp = datetime.now().strftime("%H:%M:%S")
        utilization = gpu.get_utilization()
        memory = gpu.get_memory_info()
        temperature = gpu.get_temperature()
        power = gpu.get_power_draw()
        
        # Calculate memory percentage
        memory_percent = (memory['used'] / memory['total']) * 100
        
        # Store metrics
        metrics_history.append({
            'timestamp': timestamp,
            'utilization': utilization,
            'memory_percent': memory_percent,
            'temperature': temperature,
            'power': power
        })
        
        # Display current metrics
        print(f"[{timestamp}] GPU Metrics:")
        print(f"  Utilization: {utilization}%")
        print(f"  Memory: {memory['used']:,} MB / {memory['total']:,} MB ({memory_percent:.1f}%)")
        print(f"  Temperature: {temperature}°C", end="")
        
        # Check for warnings (like DCGM health checks)
        if temperature >= TEMP_WARNING:
            print(" ⚠️  WARNING: High temperature!")
        else:
            print(" ✓")
            
        print(f"  Power Draw: {power}W")
        
        if memory_percent >= MEMORY_WARNING:
            print(f"  ⚠️  WARNING: Memory usage above {MEMORY_WARNING}%!")
        
        print("-" * 40)
        
        # Wait before next measurement
        time.sleep(interval_seconds)
    
    # Summary statistics (like DCGM reporting)
    print("\n" + "="*60)
    print("MONITORING SUMMARY")
    print("="*60)
    
    if metrics_history:
        avg_util = sum(m['utilization'] for m in metrics_history) / len(metrics_history)
        avg_temp = sum(m['temperature'] for m in metrics_history) / len(metrics_history)
        max_temp = max(m['temperature'] for m in metrics_history)
        avg_power = sum(m['power'] for m in metrics_history) / len(metrics_history)
        
        print(f"Samples collected: {len(metrics_history)}")
        print(f"Average Utilization: {avg_util:.1f}%")
        print(f"Average Temperature: {avg_temp:.1f}°C (Max: {max_temp}°C)")
        print(f"Average Power Draw: {avg_power:.1f}W")
        
        # Estimate energy consumption
        energy_wh = (avg_power * duration_seconds) / 3600
        print(f"Estimated Energy Used: {energy_wh:.3f} Wh")


if __name__ == "__main__":
    print("\nThis example demonstrates GPU monitoring concepts used in DCGM.")
    print("In a real data center, DCGM runs as a service collecting metrics")
    print("from all GPUs continuously for health monitoring and analytics.\n")
    
    # Run monitoring for 30 seconds with 5-second intervals
    monitor_gpu_metrics(duration_seconds=30, interval_seconds=5)