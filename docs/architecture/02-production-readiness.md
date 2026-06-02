# Production Readiness

This repository is a portfolio demo, but it includes production-oriented patterns that show platform engineering maturity.

## Workload Reliability

| Capability | Implementation |
|---|---|
| Health check | `/health` endpoint |
| Readiness check | `/ready` endpoint |
| Rolling update | Deployment strategy |
| Autoscaling | HPA template |
| Disruption handling | PodDisruptionBudget |
| Resource control | Requests and limits |

## Security Defaults

| Control | Implementation |
|---|---|
| Non-root runtime | Pod and container security context |
| Least privilege | Service account token disabled |
| Filesystem protection | Read-only root filesystem |
| Linux hardening | Drop all capabilities |
| Network segmentation | NetworkPolicy |
| Namespace guardrails | Pod security labels |

## Observability

| Signal | Implementation |
|---|---|
| Metrics | `/metrics` endpoint |
| Logs | Structured logging |
| Health | `/health` |
| Readiness | `/ready` |
| Scrape support | Prometheus annotations and optional ServiceMonitor |

## Governance

| Area | Implementation |
|---|---|
| Resource governance | ResourceQuota and LimitRange |
| Policy-as-code | Kyverno policy example |
| Architecture traceability | ADRs |
| Deployment repeatability | Helm and Kustomize |
| Environment separation | `environments/` folder |
