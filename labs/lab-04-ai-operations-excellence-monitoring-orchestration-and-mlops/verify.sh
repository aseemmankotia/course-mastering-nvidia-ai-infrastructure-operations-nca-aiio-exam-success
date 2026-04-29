#!/bin/bash
# Verification script for Lab 4: AI Operations Excellence: Monitoring, Orchestration, and MLOps
set -e
echo "🔍 Verifying Lab 4: AI Operations Excellence: Monitoring, Orchestration, and MLOps..."
[ -f "gpu-metrics-monitoring-basics.py" ] && echo "✅ gpu-metrics-monitoring-basics.py found" || echo "❌ gpu-metrics-monitoring-basics.py missing"
echo ""
echo "✅ Lab 4 verification complete!"
