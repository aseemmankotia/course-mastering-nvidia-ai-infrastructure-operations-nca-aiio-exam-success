# NCA-AIIO Domain Weight Study Planner
# Allocate study time based on exam domain weights

# Domain weights from the exam blueprint
domains = {
    "AI Infrastructure": {
        "weight": 40,
        "topics": [
            "NVIDIA GPU architecture (A100, H100)",
            "DGX systems and clusters",
            "Networking (InfiniBand, NVLink)",
            "Storage solutions (GPFS, Lustre)",
            "Container orchestration (Kubernetes)"
        ],
        "expected_questions": 20  # 40% of 50 questions
    },
    "Essential AI": {
        "weight": 38,
        "topics": [
            "Deep learning frameworks (PyTorch, TensorFlow)",
            "CUDA basics",
            "Model training concepts",
            "NVIDIA software stack (NGC, TensorRT)",
            "AI/ML workflow understanding"
        ],
        "expected_questions": 19  # 38% of 50 questions
    },
    "Operations": {
        "weight": 22,
        "topics": [
            "Monitoring GPU health",
            "Job scheduling (SLURM)",
            "Troubleshooting common issues",
            "Performance optimization",
            "Security best practices"
        ],
        "expected_questions": 11  # 22% of 50 questions
    }
}

def create_study_plan(total_study_hours):
    """Create a study plan based on domain weights."""
    print("\n" + "=" * 60)
    print(f"NCA-AIIO STUDY PLAN - {total_study_hours} Total Hours")
    print("=" * 60)
    
    for domain_name, domain_info in domains.items():
        # Calculate study hours based on weight
        study_hours = (domain_info["weight"] / 100) * total_study_hours
        
        print(f"\n📚 {domain_name}")
        print(f"   Weight: {domain_info['weight']}%")
        print(f"   Expected Questions: ~{domain_info['expected_questions']}")
        print(f"   Recommended Study Time: {study_hours:.1f} hours")
        print(f"   Key Topics:")
        
        for topic in domain_info["topics"]:
            print(f"      • {topic}")
    
    # Priority recommendation
    print("\n" + "-" * 60)
    print("📌 STUDY PRIORITY (based on weight):")
    sorted_domains = sorted(domains.items(), 
                           key=lambda x: x[1]["weight"], 
                           reverse=True)
    
    for i, (name, info) in enumerate(sorted_domains, 1):
        print(f"   {i}. {name} ({info['weight']}%)")

# Create a 40-hour study plan
create_study_plan(40)

# Quick reference for passing
print("\n" + "=" * 60)
print("PASSING SCORE REMINDER")
print("=" * 60)
print("Passing typically requires ~70% correct answers")
print("That means correctly answering ~35 out of 50 questions")
print("Focus on AI Infrastructure - it's 40% of your score!")