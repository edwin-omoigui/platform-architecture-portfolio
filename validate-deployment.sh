#!/usr/bin/env bash
set -euo pipefail

IMAGE="${IMAGE:-platform-demo-app:1.0.0}"

docker build -t "$IMAGE" ./app

echo "Built image: $IMAGE"
