{{- define "platform-demo-app.name" -}}
{{- default .Chart.Name .Values.nameOverride | trunc 63 | trimSuffix "-" -}}
{{- end -}}

{{- define "platform-demo-app.fullname" -}}
{{- printf "%s" (include "platform-demo-app.name" .) -}}
{{- end -}}
