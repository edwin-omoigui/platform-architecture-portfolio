{{- if .Values.serviceAccount.create }}
apiVersion: v1
kind: ServiceAccount
metadata:
  name: {{ include "platform-demo-app.fullname" . }}
  labels:
    {{- include "platform-demo-app.labels" . | nindent 4 }}
  annotations:
    {{- toYaml .Values.serviceAccount.annotations | nindent 4 }}
automountServiceAccountToken: {{ .Values.serviceAccount.automountServiceAccountToken }}
{{- end }}
