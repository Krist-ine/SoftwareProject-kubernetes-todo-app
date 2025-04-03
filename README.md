# Scalable To-Do List Application Deployment on Kubernetes

This repository contains all necessary files to deploy and manage a scalable To-Do List web application using Kubernetes. The application is containerized using Docker and deployed on a Kubernetes cluster. It supports features like auto-scaling, rolling updates, persistent storage, logging, and self-healing.

## Project Overview

The To-Do List web application is built using Python Flask and provides the following APIs:

- `GET /tasks`: Retrieve all tasks
- `POST /tasks`: Add a new task
- `DELETE /tasks/<task_id>`: Delete a task by ID

This project is designed to meet the following requirements:

- Deploy a web application using Kubernetes with at least 3 replicas
- Implement Horizontal Pod Autoscaler (HPA) for scaling based on CPU usage
- Use ConfigMaps and Secrets for environment variables and sensitive data
- Simulate rolling updates and rollbacks
- Implement persistent storage (optional)
- Test application availability, scaling, rolling updates, self-healing, persistent storage, and logging

## Folder Structure
todo-list-app/
├── app/
│ ├── app.py # Python Flask application code
│ ├── requirements.txt # Dependencies for Flask
├── docker/
│ └── Dockerfile # Docker configuration
├── manifests/
│ ├── deployment.yaml # Deployment configuration
│ ├── service.yaml # Service configuration
│ ├── configmap.yaml # ConfigMap for environment variables
│ ├── secret.yaml # Secret for sensitive data
│ ├── hpa.yaml # Horizontal Pod Autoscaler configuration
│ ├── pvc.yaml # Persistent Volume Claim configuration
├── README.md # Project documentation


## Prerequisites

### Tools Required

- Docker
- Kubernetes CLI (kubectl)
- Google Cloud SDK (for GKE) or Minikube (for local deployment)

### Environment Setup

- A Kubernetes cluster with at least 2 worker nodes
- Metrics Server enabled for auto-scaling

## Steps to Deploy

### Step 1: Build and Push Docker Image

Build the Docker image locally:
bash
docker build -t gcr.io/<PROJECT_ID>/todo-app:v1 -f docker/Dockerfile .

Replace <PROJECT_ID> with your Google Cloud Project ID.

Push the image to Google Artifact Registry or Docker Hub:
docker push gcr.io/<PROJECT_ID>/todo-app:v1

### Step 2: Deploy Kubernetes Resources
bash
kubectl apply -f manifests/configmap.yaml
kubectl apply -f manifests/secret.yaml
kubectl apply -f manifests/deployment.yaml
kubectl apply -f manifests/service.yaml
kubectl get pods -w
kubectl get services todo-app-service

### Step 3: Configure Horizontal Pod Autoscaler (HPA)
bash
kubectl apply -f manifests/hpa.yaml
kubectl get hpa -w

### Step 4: Persistent Storage Setup 
bash
kubectl apply -f manifests/pvc.yaml
kubectl apply -f manifests/deployment.yaml

### Step 5: Rolling Updates and Rollbacks
bash
kubectl set image deployment/todo-app todo-app-container=gcr.io/<PROJECT_ID>/todo-app:v2 --record=true
kubectl rollout status deployment/todo-app
kubectl rollout undo deployment/todo-app --to-revision=1

## Validation Tests

### Service Connectivity Verification
Validate that the application endpoints are properly exposed and responding:

bash
curl http://<external-ip>
Anticipated Response: "Welcome to your To-Do List !".

### Autoscaling Performance Evaluation
Test the cluster's ability to automatically scale under load:

bash
kubectl run --rm -it load-generator --image=busybox -- /bin/sh -c "while true; do wget -q -O- http://todo-app-service; done"
Observe scaling behavior in real-time:

bash
kubectl get hpa -w
kubectl get pods -w
Successful scaling will demonstrate increasing pod count as CPU load rises.

### Deployment Update Validation
Verify seamless version upgrades:

bash
kubectl set image deployment/todo-app todo-app-container=gcr.io/<PROJECT_ID>/todo-app:v2 --record=true
If issues arise, restore previous version:

bash
kubectl rollout undo deployment/todo-app
The system should maintain availability during updates and properly revert when necessary.

### Fault Tolerance Assessment
Test the system's automatic recovery capabilities:

Terminate a running instance:

bash
kubectl delete pod <POD_NAME>
Monitor cluster response:

bash
kubectl get pods -w
The control plane should immediately initiate replacement pod creation.

Data Persistence Verification
Validate storage durability across pod lifecycles:

### Create test artifact:

bash
kubectl exec -it <POD_NAME> -- /bin/bash -c "echo 'Test Data' > /data/test-file.txt"
Simulate pod failure and verify data retention:

bash
kubectl delete pod <POD_NAME>
kubectl exec -it <NEW_POD_NAME> -- cat /data/test-file.txt
The stored information should persist through pod recreation.

### Operational Logging Inspection
Examine application runtime output:

bash
kubectl logs <POD_NAME>
The output should display operational details including API transaction records.



The following test cases validate all core Kubernetes functionality:

1. **Service Availability** - Verified application accessibility
2. **Horizontal Scaling** - Confirmed automatic pod scaling under load
3. **Rolling Updates** - Tested zero-downtime deployments
4. **Rollback Capability** - Validated version recovery
5. **Self-Healing** - Demonstrated automatic pod recovery
6. **Data Persistence** - Confirmed storage durability

The project meets all specified requirements for building and managing a scalable, resilient web application on Kubernetes.


