apiVersion: v1
kind: ConfigMap
metadata:
  name: {{ include "platform-demo-app.fullname" . }}-config
  labels:
    {{- include "platform-demo-app.labels" . | nindent 4 }}
data:
  SERVICE_NAME: {{ .Values.app.serviceName | quote }}
  TENANT_NAME: {{ .Values.app.tenantName | quote }}
  ENVIRONMENT: {{ .Values.app.environment | quote }}
  REGION: {{ .Values.app.region | quote }}
  PLATFORM_OWNER: {{ .Values.app.platformOwner | quote }}
  POSTGRES_HOST: {{ .Values.platformContracts.postgresHost | quote }}
  S3_ENDPOINT: {{ .Values.platformContracts.s3Endpoint | quote }}
  OIDC_ISSUER_URL: {{ .Values.platformContracts.oidcIssuerUrl | quote }}
  OTEL_EXPORTER_OTLP_ENDPOINT: {{ .Values.platformContracts.otelExporterOtlpEndpoint | quote }}
