# Office Bulletin App v2

## What’s Here

- **backend/** – Flask API and `requirements.txt`  
- **frontend/** – Static UI served by nginx  
- **k8s/** – Kubernetes/OpenShift manifests

## Deploying

1. Replace `<BASE64_ENCODED_PASSWORD>` in `k8s/postgres-secret.yaml`.  
2. Replace `<YOUR_REGISTRY>/…` image names.  
3. Commit & push to GitHub.  
4. In the OpenShift console: **+Add → From Git**, point at your repo, and click **Create**.

