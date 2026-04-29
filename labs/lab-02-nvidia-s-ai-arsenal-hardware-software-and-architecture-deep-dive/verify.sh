#!/bin/bash
# Verification script for Lab 2: NVIDIA's AI Arsenal: Hardware, Software, and Architecture Deep Dive
set -e
echo "🔍 Verifying Lab 2: NVIDIA's AI Arsenal: Hardware, Software, and Architecture Deep Dive..."
[ -f "cuda-device-properties.py" ] && echo "✅ cuda-device-properties.py found" || echo "❌ cuda-device-properties.py missing"
echo ""
echo "✅ Lab 2 verification complete!"
