import os
from fastapi import FastAPI
from fastapi.responses import PlainTextResponse
from prometheus_client import Counter, generate_latest, CONTENT_TYPE_LATEST

app = FastAPI(title="Platform Demo App", version="1.0.0")

REQUESTS = Counter(
    "platform_demo_requests_total",
    "Total requests served by the platform demo app",
    ["endpoint"],
)


def platform_context():
    return {
        "tenant": os.getenv("TENANT_NAME", "demo"),
        "environment": os.getenv("ENVIRONMENT", "portfolio"),
        "identity_provider": os.getenv("OIDC_ISSUER_URL", "not-configured"),
        "database": os.getenv("POSTGRES_HOST", "not-configured"),
        "object_storage": os.getenv("S3_ENDPOINT", "not-configured"),
        "observability": os.getenv("OTEL_ENDPOINT", "not-configured"),
    }


@app.get("/")
def root():
    REQUESTS.labels(endpoint="/").inc()
    return {
        "service": "platform-demo-app",
        "purpose": "Lightweight workload for platform architecture portfolio",
        "platform_context": platform_context(),
    }


@app.get("/health")
def health():
    REQUESTS.labels(endpoint="/health").inc()
    return {"status": "healthy"}


@app.get("/ready")
def ready():
    REQUESTS.labels(endpoint="/ready").inc()
    return {"status": "ready", "platform_context": platform_context()}


@app.get("/platform-contract")
def platform_contract():
    REQUESTS.labels(endpoint="/platform-contract").inc()
    return {
        "contracts": [
            "tenant metadata",
            "identity provider",
            "database endpoint",
            "object storage endpoint",
            "observability endpoint",
            "trust bundle",
        ],
        "context": platform_context(),
    }


@app.get("/metrics")
def metrics():
    REQUESTS.labels(endpoint="/metrics").inc()
    return PlainTextResponse(generate_latest(), media_type=CONTENT_TYPE_LATEST)
