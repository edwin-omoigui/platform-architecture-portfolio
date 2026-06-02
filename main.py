name: Validate Portfolio Repo

on:
  push:
    branches:
      - main
  pull_request:

jobs:
  app-tests:
    name: App tests
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: "3.12"
      - name: Install dependencies
        run: |
          pip install -r app/requirements.txt
      - name: Run tests
        run: |
          cd app
          pytest -q

  helm-validation:
    name: Helm validation
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: azure/setup-helm@v4
      - name: Helm lint
        run: |
          helm lint ./charts/platform-demo-app
      - name: Helm template
        run: |
          helm template platform-demo-app ./charts/platform-demo-app \
            --namespace platform-demo \
            -f environments/prod-like/values.yaml

  kustomize-validation:
    name: Kustomize validation
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: azure/setup-kubectl@v4
      - name: Build local overlay
        run: |
          kubectl kustomize environments/local
