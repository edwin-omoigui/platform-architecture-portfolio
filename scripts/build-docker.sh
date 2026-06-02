#!/usr/bin/env bash
set -euo pipefail

IMAGE_NAME="${IMAGE_NAME:-platform-demo-app:local}"

docker build -t "$IMAGE_NAME" ./app

echo "Built image: $IMAGE_NAME"
