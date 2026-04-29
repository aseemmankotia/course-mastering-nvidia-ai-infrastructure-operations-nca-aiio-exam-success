# Data Center Power and Cooling Calculator for AI Infrastructure
# This tool helps estimate power consumption and cooling needs for GPU environments

class GPUPowerCalculator:
    """
    Calculate power requirements for AI data center planning.
    Understanding power consumption is critical for infrastructure design.
    """
    
    # Common NVIDIA GPU power specifications (TDP in Watts)
    GPU_POWER_SPECS = {
        'A100_40GB': 400,      # NVIDIA A100 40GB
        'A100_80GB': 400,      # NVIDIA A100 80GB
        'H100_SXM': 700,       # NVIDIA H100 SXM (high-performance)
        'H100_PCIe': 350,      # NVIDIA H100 PCIe
        'L40S': 350,           # NVIDIA L40S
        'RTX_4090': 450,       # GeForce RTX 4090
    }
    
    def __init__(self, gpu_type, gpu_count):
        """
        Initialize the calculator with GPU type and count.
        
        Args:
            gpu_type: Type of GPU (e.g., 'H100_SXM')
            gpu_count: Number of GPUs in the deployment
        """
        self.gpu_type = gpu_type
        self.gpu_count = gpu_count
        self.gpu_power = self.GPU_POWER_SPECS.get(gpu_type, 400)
    
    def calculate_gpu_power(self):
        """Calculate total GPU power consumption in kW."""
        total_watts = self.gpu_power * self.gpu_count
        return total_watts / 1000  # Convert to kW
    
    def calculate_total_system_power(self):
        """
        Calculate total system power including overhead.
        
        In real data centers, you need to account for:
        - CPU power
        - Memory power
        - Storage power
        - Networking equipment
        - Power distribution losses
        
        A common rule: Total system power ≈ GPU power × 1.5 to 2.0
        """
        gpu_power_kw = self.calculate_gpu_power()
        # Using 1.7x multiplier for supporting infrastructure
        overhead_multiplier = 1.7
        return gpu_power_kw * overhead_multiplier
    
    def calculate_cooling_requirement(self, pue=1.4):
        """
        Calculate cooling requirements using PUE (Power Usage Effectiveness).
        
        PUE = Total Facility Power / IT Equipment Power
        - PUE of 1.0 = perfect efficiency (impossible)
        - PUE of 1.4 = good efficiency for GPU data centers
        - PUE of 2.0 = older/less efficient facility
        
        Args:
            pue: Power Usage Effectiveness ratio (default 1.4)
        """
        it_power = self.calculate_total_system_power()
        total_facility_power = it_power * pue
        cooling_power = total_facility_power - it_power
        return {
            'it_power_kw': round(it_power, 2),
            'total_facility_power_kw': round(total_facility_power, 2),
            'cooling_overhead_kw': round(cooling_power, 2),
            'pue': pue
        }
    
    def calculate_rack_density(self, gpus_per_server=8, servers_per_rack=4):
        """
        Calculate power density per rack.
        
        High-density GPU racks can exceed 30-40 kW per rack,
        requiring specialized cooling solutions like liquid cooling.
        """
        power_per_server = (self.gpu_power * gpus_per_server * 1.7) / 1000
        power_per_rack = power_per_server * servers_per_rack
        return {
            'power_per_server_kw': round(power_per_server, 2),
            'power_per_rack_kw': round(power_per_rack, 2),
            'cooling_recommendation': self._get_cooling_recommendation(power_per_rack)
        }
    
    def _get_cooling_recommendation(self, rack_power_kw):
        """Recommend cooling solution based on rack power density."""
        if rack_power_kw < 15:
            return "Standard air cooling sufficient"
        elif rack_power_kw < 30:
            return "Enhanced air cooling with hot/cold aisle containment"
        elif rack_power_kw < 50:
            return "Rear-door heat exchangers or in-row cooling recommended"
        else:
            return "Direct liquid cooling (DLC) required for this density"


# Example usage - Planning a small AI training cluster
print("=" * 60)
print("AI Data Center Power Planning Calculator")
print("=" * 60)

# Scenario: Planning a cluster with 32 H100 GPUs
calculator = GPUPowerCalculator('H100_SXM', gpu_count=32)

print(f"\nScenario: {calculator.gpu_count}x {calculator.gpu_type} GPUs")
print(f"GPU TDP: {calculator.gpu_power}W each")

# Calculate power requirements
gpu_power = calculator.calculate_gpu_power()
print(f"\n1. GPU Power Only: {gpu_power} kW")

total_power = calculator.calculate_total_system_power()
print(f"2. Total IT Equipment Power (with overhead): {round(total_power, 2)} kW")

# Calculate cooling with different PUE values
print("\n3. Cooling Requirements by PUE:")
for pue in [1.2, 1.4, 1.6]:
    cooling = calculator.calculate_cooling_requirement(pue)
    print(f"   PUE {pue}: Total={cooling['total_facility_power_kw']} kW, "
          f"Cooling overhead={cooling['cooling_overhead_kw']} kW")

# Calculate rack density
print("\n4. Rack Density Analysis (8 GPUs/server, 4 servers/rack):")
rack_info = calculator.calculate_rack_density()
print(f"   Power per server: {rack_info['power_per_server_kw']} kW")
print(f"   Power per rack: {rack_info['power_per_rack_kw']} kW")
print(f"   Recommendation: {rack_info['cooling_recommendation']}")

# Calculate number of racks needed
racks_needed = calculator.gpu_count / (8 * 4)  # GPUs / (GPUs per server * servers per rack)
print(f"\n5. Infrastructure Summary:")
print(f"   Racks needed: {int(racks_needed)} racks")
print(f"   Total facility power: {round(total_power * 1.4, 2)} kW")
print(f"   Annual energy cost (at $0.10/kWh): ${round(total_power * 1.4 * 24 * 365 * 0.10, 2):,.2f}")