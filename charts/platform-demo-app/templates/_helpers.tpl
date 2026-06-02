{{- define "platform-demo-app.name" -}}
{{- .Chart.Name | trunc 63 | trimSuffix "-" -}}
{{- end -}}

{{- define "platform-demo-app.fullname" -}}
{{- include "platform-demo-app.name" . -}}
{{- end -}}

{{- define "platform-demo-app.labels" -}}
app.kubernetes.io/name: {{ include "platform-demo-app.name" . }}
app.kubernetes.io/instance: {{ .Release.Name }}
app.kubernetes.io/version: {{ .Chart.AppVersion | quote }}
app.kubernetes.io/component: api
app.kubernetes.io/part-of: platform-architecture-portfolio
app.kubernetes.io/managed-by: {{ .Release.Service }}
{{- end -}}

{{- define "platform-demo-app.selectorLabels" -}}
app.kubernetes.io/name: {{ include "platform-demo-app.name" . }}
app.kubernetes.io/instance: {{ .Release.Name }}
{{- end -}}
