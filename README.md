# Learning k8s

### Flask

```bash
flask --app garden run
```


### Docker

```bash
# build
docker build -t garden .

# run
docker container run -p 127.0.0.1:5000:5000 -t garden
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

docker build -t $APP apps/$APP

# deploy service with local docker image
kubectl apply -f deployments/garden.yaml

# check if pod is running
kubectl get pods

# in a separate terminal run:
minikube service garden --url
# then the URL of the service can be curl'ed to test service availability
curl http://127.0.0.1:64652
 ```
