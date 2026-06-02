apiVersion: kyverno.io/v1
kind: ClusterPolicy
metadata:
  name: require-secure-pod-defaults
  annotations:
    policies.kyverno.io/title: Require Secure Pod Defaults
    policies.kyverno.io/category: Platform Security
spec:
  validationFailureAction: Audit
  background: true
  rules:
    - name: require-non-root
      match:
        any:
          - resources:
              kinds:
                - Pod
      validate:
        message: "Pods should run as non-root."
        pattern:
          spec:
            securityContext:
              runAsNonRoot: true
    - name: disallow-privilege-escalation
      match:
        any:
          - resources:
              kinds:
                - Pod
      validate:
        message: "Containers should not allow privilege escalation."
        pattern:
          spec:
            containers:
              - securityContext:
                  allowPrivilegeEscalation: false
