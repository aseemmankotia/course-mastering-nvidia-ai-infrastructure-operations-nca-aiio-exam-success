# Traditional Programming vs Machine Learning
# This example shows the fundamental difference between
# rule-based programming and learning from data

# ============================================
# TRADITIONAL PROGRAMMING APPROACH
# ============================================
# We explicitly write rules to classify fruits

def classify_fruit_traditional(weight_grams, color, diameter_cm):
    """
    Traditional approach: We define ALL the rules manually.
    Problem: What if we encounter a new fruit? We need to add more rules!
    """
    if color == "red" and weight_grams > 150 and diameter_cm > 7:
        return "apple"
    elif color == "yellow" and weight_grams < 150 and diameter_cm < 5:
        return "banana"
    elif color == "orange" and weight_grams > 100 and diameter_cm > 6:
        return "orange"
    else:
        return "unknown"

# Test traditional approach
print("=== Traditional Programming ===")
print(f"Red, 180g, 8cm -> {classify_fruit_traditional(180, 'red', 8)}")
print(f"Yellow, 120g, 4cm -> {classify_fruit_traditional(120, 'yellow', 4)}")
print(f"Green, 200g, 10cm -> {classify_fruit_traditional(200, 'green', 10)}")

# ============================================
# MACHINE LEARNING APPROACH (Simplified)
# ============================================
# The algorithm learns patterns from data instead of explicit rules

from collections import Counter
import math

class SimpleMLClassifier:
    """
    A simple K-Nearest Neighbors classifier.
    This LEARNS from examples instead of following hardcoded rules.
    """
    
    def __init__(self):
        self.training_data = []  # Where we store our examples
        
    def train(self, features, label):
        """
        TRAINING PHASE: Feed the model examples to learn from.
        In real ML, this is where the 'learning' happens.
        """
        self.training_data.append((features, label))
        print(f"  Learned: {features} -> {label}")
    
    def _calculate_distance(self, point1, point2):
        """Calculate how similar two data points are"""
        return math.sqrt(sum((a - b) ** 2 for a, b in zip(point1, point2)))
    
    def predict(self, features, k=3):
        """
        INFERENCE PHASE: Use what was learned to make predictions.
        This is where we use the trained model.
        """
        # Find the k most similar examples from training
        distances = []
        for train_features, label in self.training_data:
            dist = self._calculate_distance(features, train_features)
            distances.append((dist, label))
        
        # Sort by distance and get k nearest neighbors
        distances.sort(key=lambda x: x[0])
        k_nearest = [label for _, label in distances[:k]]
        
        # Return the most common label among neighbors
        return Counter(k_nearest).most_common(1)[0][0]

# Create and train our ML model
print("\n=== Machine Learning Approach ===")
print("Training phase (learning from examples):")
ml_classifier = SimpleMLClassifier()

# Training data: [weight, diameter] -> fruit
# The model learns patterns from these examples
ml_classifier.train([180, 8], "apple")
ml_classifier.train([190, 7.5], "apple")
ml_classifier.train([170, 8.2], "apple")
ml_classifier.train([120, 3], "banana")
ml_classifier.train([130, 3.5], "banana")
ml_classifier.train([110, 2.8], "banana")
ml_classifier.train([140, 7], "orange")
ml_classifier.train([150, 6.5], "orange")
ml_classifier.train([145, 7.2], "orange")

# Inference phase: Make predictions on new data
print("\nInference phase (making predictions):")
print(f"  [175, 7.8] -> {ml_classifier.predict([175, 7.8])}")
print(f"  [115, 3.2] -> {ml_classifier.predict([115, 3.2])}")
print(f"  [148, 6.8] -> {ml_classifier.predict([148, 6.8])}")

print("\n=== Key Takeaway ===")
print("Traditional: Programmer writes rules")
print("Machine Learning: Algorithm learns rules from data")