import os
from fastapi import FastAPI
from fastapi.responses import PlainTextResponse
from prometheus_client import Counter, generate_latest, CONTENT_TYPE_LATEST

app = FastAPI(title="Platform Demo App", version="1.0.0")
REQUESTS = Counter("platform_demo_requests_total", "Total requests", ["endpoint"])

def context():
    return {
        "tenant": os.getenv("TENANT_NAME", "demo"),
        "identity": os.getenv("OIDC_ISSUER_URL", "not-configured"),
        "database": os.getenv("POSTGRES_HOST", "not-configured"),
        "storage": os.getenv("S3_ENDPOINT", "not-configured"),
        "observability": os.getenv("OTEL_ENDPOINT", "not-configured"),
    }

@app.get("/")
def root():
    REQUESTS.labels(endpoint="/").inc()
    return {"service": "platform-demo-app", "platform_context": context()}

@app.get("/health")
def health():
    REQUESTS.labels(endpoint="/health").inc()
    return {"status": "healthy"}

@app.get("/platform-contract")
def platform_contract():
    REQUESTS.labels(endpoint="/platform-contract").inc()
    return {"contracts": ["identity", "data", "storage", "observability", "trust"], "context": context()}

@app.get("/metrics")
def metrics():
    REQUESTS.labels(endpoint="/metrics").inc()
    return PlainTextResponse(generate_latest(), media_type=CONTENT_TYPE_LATEST)
