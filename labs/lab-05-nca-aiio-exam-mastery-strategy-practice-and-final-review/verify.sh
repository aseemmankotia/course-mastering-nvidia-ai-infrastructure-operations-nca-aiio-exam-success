#!/bin/bash
# Verification script for Lab 5: NCA-AIIO Exam Mastery: Strategy, Practice, and Final Review
set -e
echo "🔍 Verifying Lab 5: NCA-AIIO Exam Mastery: Strategy, Practice, and Final Review..."
[ -f "exam-time-calculator.py" ] && echo "✅ exam-time-calculator.py found" || echo "❌ exam-time-calculator.py missing"
[ -f "domain-weight-study-planner.py" ] && echo "✅ domain-weight-study-planner.py found" || echo "❌ domain-weight-study-planner.py missing"
echo ""
echo "✅ Lab 5 verification complete!"
