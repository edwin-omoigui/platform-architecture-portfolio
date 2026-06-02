from fastapi import FastAPI
from fastapi.responses import PlainTextResponse
from prometheus_client import Counter, Histogram, generate_latest, CONTENT_TYPE_LATEST
import os
import time

app = FastAPI(
    title="Platform Demo App",
    description="A small cloud-native service used to demonstrate platform architecture patterns.",
    version="1.0.0",
)

REQUEST_COUNT = Counter(
    "platform_demo_requests_total",
    "Total HTTP requests handled by the platform demo app",
    ["endpoint"],
)

REQUEST_LATENCY = Histogram(
    "platform_demo_request_latency_seconds",
    "Request latency for the platform demo app",
    ["endpoint"],
)


def platform_context() -> dict:
    return {
        "tenant": os.getenv("TENANT_NAME", "demo-tenant"),
        "environment": os.getenv("ENVIRONMENT", "local"),
        "region": os.getenv("REGION", "local"),
        "platform_owner": os.getenv("PLATFORM_OWNER", "platform-engineering"),
        "database_host": os.getenv("POSTGRES_HOST", "not-configured"),
        "object_storage_endpoint": os.getenv("S3_ENDPOINT", "not-configured"),
        "identity_provider": os.getenv("OIDC_ISSUER_URL", "not-configured"),
    }


@app.get("/")
def root():
    start = time.time()
    REQUEST_COUNT.labels(endpoint="/").inc()
    response = {
        "service": "platform-demo-app",
        "message": "Cloud-native platform reference app is running.",
        "platform_context": platform_context(),
    }
    REQUEST_LATENCY.labels(endpoint="/").observe(time.time() - start)
    return response


@app.get("/health")
def health():
    REQUEST_COUNT.labels(endpoint="/health").inc()
    return {
        "status": "healthy",
        "service": "platform-demo-app",
    }


@app.get("/ready")
def ready():
    REQUEST_COUNT.labels(endpoint="/ready").inc()
    return {
        "status": "ready",
        "dependencies": {
            "database": os.getenv("POSTGRES_HOST", "not-configured"),
            "object_storage": os.getenv("S3_ENDPOINT", "not-configured"),
            "identity_provider": os.getenv("OIDC_ISSUER_URL", "not-configured"),
        },
    }


@app.get("/platform-contract")
def contract():
    REQUEST_COUNT.labels(endpoint="/platform-contract").inc()
    return {
        "description": "This endpoint shows the platform contracts the app expects from the platform layer.",
        "required_contracts": [
            "tenant-info config",
            "postgres connection",
            "s3 object storage config",
            "oidc identity provider config",
            "trust bundle config",
            "observability configuration",
        ],
        "current_context": platform_context(),
    }


@app.get("/metrics")
def metrics():
    REQUEST_COUNT.labels(endpoint="/metrics").inc()
    return PlainTextResponse(generate_latest(), media_type=CONTENT_TYPE_LATEST)
