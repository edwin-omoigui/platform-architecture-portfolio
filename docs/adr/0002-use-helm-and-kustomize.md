# ADR 0002: Use Helm and Kustomize

## Status

Accepted

## Context

The repo needs reusable application packaging and environment-specific configuration.

## Decision

Use Helm for workload packaging and Kustomize for platform contracts and namespace configuration.

## Consequences

- Helm shows reusable delivery.
- Kustomize shows GitOps-friendly overlays.
- The repo remains simple and practical.
