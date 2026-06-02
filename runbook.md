{{- if .Values.networkPolicy.enabled }}
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: {{ include "platform-demo-app.fullname" . }}
  labels:
    {{- include "platform-demo-app.labels" . | nindent 4 }}
spec:
  podSelector:
    matchLabels:
      {{- include "platform-demo-app.selectorLabels" . | nindent 6 }}
  policyTypes:
    - Ingress
    - Egress
  ingress:
    - from:
        {{- if .Values.networkPolicy.allowNamespaceIngress }}
        - namespaceSelector: {}
        {{- end }}
      ports:
        - protocol: TCP
          port: {{ .Values.service.targetPort }}
  egress:
    - to:
        - namespaceSelector: {}
    {{- if .Values.networkPolicy.allowInternetEgress443 }}
    - to:
        - ipBlock:
            cidr: 0.0.0.0/0
      ports:
        - protocol: TCP
          port: 443
        - protocol: TCP
          port: 80
    {{- end }}
{{- end }}
