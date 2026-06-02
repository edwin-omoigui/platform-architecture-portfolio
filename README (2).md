#!/usr/bin/env bash
set -euo pipefail

NAMESPACE="${NAMESPACE:-platform-demo}"
RELEASE="${RELEASE:-platform-demo-app}"

helm upgrade --install "$RELEASE" ./charts/platform-demo-app \
  --namespace "$NAMESPACE" \
  --create-namespace \
  -f environments/prod-like/values.yaml

kubectl -n "$NAMESPACE" get deploy,pod,svc,hpa,pdb,networkpolicy
