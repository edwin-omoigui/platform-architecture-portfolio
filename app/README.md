# Platform Demo App

A small FastAPI service used to demonstrate cloud-native platform architecture patterns.

## Endpoints

| Endpoint | Purpose |
|---|---|
| `/` | Service overview and platform context |
| `/health` | Liveness endpoint |
| `/ready` | Readiness endpoint |
| `/platform-contract` | Shows expected platform service contracts |
| `/metrics` | Prometheus metrics endpoint |

## Environment Variables

| Variable | Purpose |
|---|---|
| `TENANT_NAME` | Tenant or application group |
| `ENVIRONMENT` | Environment name |
| `REGION` | Deployment region |
| `POSTGRES_HOST` | Database service endpoint |
| `S3_ENDPOINT` | Object storage endpoint |
| `OIDC_ISSUER_URL` | Identity provider issuer |
| `PLATFORM_OWNER` | Platform ownership metadata |
