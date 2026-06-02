apiVersion: v1
kind: ConfigMap
metadata:
  name: observability-config
  namespace: platform-demo
  labels:
    platform.example.com/contract: observability
data:
  OTEL_EXPORTER_OTLP_ENDPOINT: http://otel-collector.observability.svc.cluster.local:4317
  METRICS_PATH: /metrics
  LOG_FORMAT: json
