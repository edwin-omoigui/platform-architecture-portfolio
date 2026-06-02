from fastapi import FastAPI, Request
from fastapi.responses import PlainTextResponse, JSONResponse
from prometheus_client import Counter, Histogram, generate_latest, CONTENT_TYPE_LATEST
import time
import structlog

from platform_demo.config import settings

logger = structlog.get_logger()

REQUEST_COUNT = Counter(
    "platform_demo_http_requests_total",
    "Total HTTP requests handled by the platform demo app",
    ["method", "endpoint", "status"],
)

REQUEST_LATENCY = Histogram(
    "platform_demo_http_request_duration_seconds",
    "HTTP request duration in seconds",
    ["method", "endpoint"],
)

app = FastAPI(
    title="Platform Demo App",
    description="Production-style demo service for platform architecture portfolio.",
    version="1.0.0",
)


@app.middleware("http")
async def metrics_and_logging(request: Request, call_next):
    start = time.time()
    response = await call_next(request)
    duration = time.time() - start

    route = request.url.path
    REQUEST_COUNT.labels(request.method, route, response.status_code).inc()
    REQUEST_LATENCY.labels(request.method, route).observe(duration)

    logger.info(
        "request_completed",
        method=request.method,
        path=route,
        status_code=response.status_code,
        duration_seconds=round(duration, 4),
        tenant=settings.tenant_name,
        environment=settings.environment,
    )
    return response


def platform_context() -> dict:
    return {
        "tenant": settings.tenant_name,
        "environment": settings.environment,
        "region": settings.region,
        "platform_owner": settings.platform_owner,
        "database_host": settings.postgres_host,
        "object_storage_endpoint": settings.s3_endpoint,
        "identity_provider": settings.oidc_issuer_url,
        "otel_endpoint": settings.otel_exporter_otlp_endpoint,
    }


@app.get("/")
def root():
    return {
        "service": settings.service_name,
        "message": "Cloud-native platform reference app is running.",
        "platform_context": platform_context(),
    }


@app.get("/health")
def health():
    return {"status": "healthy", "service": settings.service_name}


@app.get("/ready")
def ready():
    return {
        "status": "ready",
        "dependencies": {
            "database": settings.postgres_host,
            "object_storage": settings.s3_endpoint,
            "identity_provider": settings.oidc_issuer_url,
            "observability": settings.otel_exporter_otlp_endpoint,
        },
    }


@app.get("/platform-contract")
def contract():
    return {
        "description": "Platform contracts expected by a cloud-native workload.",
        "required_contracts": [
            "tenant-info",
            "postgres-connection",
            "s3-config",
            "oidc-config",
            "trust-bundle",
            "observability-config",
            "resource-guardrails",
            "network-policy",
        ],
        "current_context": platform_context(),
    }


@app.get("/architecture")
def architecture():
    return {
        "pattern": "Internal Developer Platform golden path",
        "flow": [
            "developer",
            "gitops",
            "kubernetes",
            "platform contracts",
            "secure workload",
            "observability",
            "business value",
        ],
        "value": [
            "faster delivery",
            "standardized onboarding",
            "secure defaults",
            "operational readiness",
            "audit-friendly controls",
        ],
    }


@app.get("/metrics")
def metrics():
    return PlainTextResponse(generate_latest(), media_type=CONTENT_TYPE_LATEST)


@app.exception_handler(Exception)
async def generic_exception_handler(request: Request, exc: Exception):
    logger.error("unhandled_exception", path=request.url.path, error=str(exc))
    return JSONResponse(status_code=500, content={"detail": "Internal server error"})
