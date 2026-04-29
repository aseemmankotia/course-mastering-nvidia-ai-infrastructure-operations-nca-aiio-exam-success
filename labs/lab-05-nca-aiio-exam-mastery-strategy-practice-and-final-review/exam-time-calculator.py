# NCA-AIIO Exam Time Management Calculator
# Helps you understand time allocation for the 60-minute exam

# Exam constants
TOTAL_QUESTIONS = 50
TOTAL_TIME_MINUTES = 60

# Calculate time per question
seconds_per_question = (TOTAL_TIME_MINUTES * 60) / TOTAL_QUESTIONS

print("=" * 50)
print("NCA-AIIO EXAM TIME MANAGEMENT GUIDE")
print("=" * 50)
print(f"\nTotal Questions: {TOTAL_QUESTIONS}")
print(f"Total Time: {TOTAL_TIME_MINUTES} minutes")
print(f"Average Time per Question: {seconds_per_question:.0f} seconds (~72 seconds)")

# Time allocation strategy
print("\n--- RECOMMENDED TIME STRATEGY ---")

# Easy questions (should be faster)
easy_time = 45  # seconds
medium_time = 72  # seconds  
hard_time = 120  # seconds

# Assume distribution of question difficulty
easy_questions = 15
medium_questions = 25
hard_questions = 10

total_estimated_time = (
    (easy_questions * easy_time) + 
    (medium_questions * medium_time) + 
    (hard_questions * hard_time)
) / 60  # Convert to minutes

print(f"\nEstimated breakdown:")
print(f"  Easy questions ({easy_questions}): ~{easy_time} seconds each")
print(f"  Medium questions ({medium_questions}): ~{medium_time} seconds each")
print(f"  Hard questions ({hard_questions}): ~{hard_time} seconds each")
print(f"\nTotal estimated time needed: {total_estimated_time:.1f} minutes")

# Review time
review_time = TOTAL_TIME_MINUTES - total_estimated_time
print(f"Time remaining for review: {review_time:.1f} minutes")

# Milestone checkpoints
print("\n--- TIME CHECKPOINTS ---")
checkpoints = [
    (15, 12),   # Question 15 at 12 minutes
    (25, 24),   # Question 25 at 24 minutes
    (35, 38),   # Question 35 at 38 minutes
    (45, 50),   # Question 45 at 50 minutes
    (50, 55),   # Finish at 55 minutes (5 min review)
]

for question, time_mark in checkpoints:
    print(f"  Question {question}: Should be at ~{time_mark} minutes")