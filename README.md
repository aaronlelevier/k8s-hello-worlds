# Learning k8s

### Flask

```bash
flask --app apps/alpha/app run
```

### Docker

```bash
# build
docker build apps/alpha -t alpha

# run
docker container run -p 127.0.0.1:5000:5000 -t alpha
```

### minikube and Docker

```bash
# clear all minikube state
minikube delete

minikube start

# set to build docker images inside of minikube VM
eval $(minikube docker-env)

# verify docker commands are running inside of minikube
docker ps
# should seem minikube processes

# set app name
APP=alpha

# build in minikube
docker build -t $APP apps/$APP

# deploy service with local docker image
kubectl apply -f deployments/$APP.yaml

# check if pod is running
kubectl get pods

# in a separate terminal run:
minikube service $APP --url
# then the URL of the service can be curl'ed to test service availability
curl http://127.0.0.1:64652
 ```

### minikube and kubectl commands

```bash
# run command on pod
kubectl exec -it $POD -- cat /etc/resolv.conf

# ssh to pod
# ref: https://kubernetes.io/docs/tasks/debug/debug-application/get-shell-running-container/
kubectl exec --stdin --tty $POD -- /bin/bash

# port forward
kubectl port-forward $POD 5000
```
