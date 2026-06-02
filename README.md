# Platform Architecture Portfolio - Working Code

This repository demonstrates a small but deployable cloud-native platform reference pattern.

It is intentionally generic and does not include confidential company, customer, network, or production environment details.

## What This Demonstrates

- Kubernetes platform engineering
- GitOps-friendly repository layout
- Helm-based application packaging
- Kustomize environment overlays
- Platform service contracts
- Observability-ready application design
- Secure-by-default Kubernetes manifests
- Internal Developer Platform concepts
- Architecture portfolio artifacts

## Repository Structure

```text
.
├── app/                         # Demo API service
├── charts/platform-demo-app/     # Helm chart
├── platform/
│   ├── contracts/                # Platform contracts: tenant, DB, S3, trust, observability
│   └── base/                     # Shared Kubernetes platform resources
├── environments/
│   └── local/                    # Kustomize local deployment
├── docs/                         # Architecture documentation
├── diagrams/                     # Mermaid diagrams
├── scripts/                      # Deployment helpers
└── .github/workflows/            # CI workflow
```

## Quick Start

### Option 1: Run locally with Python

```bash
cd app
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn main:app --host 0.0.0.0 --port 8080
```

Open:

```text
http://localhost:8080
http://localhost:8080/health
http://localhost:8080/metrics
```

### Option 2: Run with Docker

```bash
docker build -t platform-demo-app:local ./app
docker run -p 8080:8080 platform-demo-app:local
```

### Option 3: Deploy to Kubernetes with Helm

```bash
helm upgrade --install platform-demo-app ./charts/platform-demo-app \
  --namespace platform-demo \
  --create-namespace
```

Validate:

```bash
kubectl -n platform-demo get pods,svc
kubectl -n platform-demo port-forward svc/platform-demo-app 8080:80
```

### Option 4: Deploy Local Platform Contracts with Kustomize

```bash
kubectl apply -k environments/local
```

## Portfolio Narrative

This working example represents a simplified Internal Developer Platform pattern:

```text
Developer
  ↓
Git Repository
  ↓
Helm / Kustomize / GitOps
  ↓
Kubernetes Platform
  ↓
Platform Services
  ↓
Application Workloads
  ↓
Observability / Security / Governance
```

## Platform Architect Value

This repo shows the ability to design and package a reusable platform pattern that combines:

- Application runtime
- Kubernetes deployment
- Platform service dependencies
- Environment configuration
- Security posture
- Observability readiness
- GitOps compatibility
