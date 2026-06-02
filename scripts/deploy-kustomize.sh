#!/usr/bin/env bash
set -euo pipefail

kubectl apply -k environments/local
kubectl -n platform-demo get configmap,secret,resourcequota,limitrange
