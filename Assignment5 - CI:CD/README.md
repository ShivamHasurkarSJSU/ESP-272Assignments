# CRUD Microservices Architecture using Kubernetes
This assignment demonstrates how we can deploy microservices using kubernets.

# Getting started
Clone this repository.

For each of the CRUD folders, repeat the following commands in separate terminals:

```shell
cd <microservice_directory>
docker build -t <microservice-image-name> .
kubectl apply -f <respective.yml>
kubectl port-forward pod/<respective_pod_name> <port> 
```

Afther all the microservices are port forwarded, you can run the Flask UI and use the application.

# Demo
https://github.com/AdityaKulkarni/sjsu/assets/25547842/e2ff8112-1c92-4602-8cc8-356a9c112976

