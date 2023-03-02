# IDS721_Project2
## Introduction
This is my project 2 for the IDS721, it is a flask microservices which can search information of pokemon by name. I used the Docker image to deploy this application and created a repository in DockerHub so that everyone could run it easily without cloning the whole project. Also, I depolyed this microservices on the Kubernetes by implementing Minikube.


## Implementation 
___Docker:___   

* After you clone this project, to build the Docker in local, you could type ``docker build -t xc200/721p2:latest .``, and then type ``docker image ls`` to verify the images you get, finally, typing ``docker run -p 8080:8080 xc200/721p2`` to run the application. Then I push it onto DockerHub by `` docker tag xc200/721p2:latest xc200/721p2:latest`` and ``then docker push xc200/721p2:latest``
* You could also run the Docker without cloning this project, you could pull the image from the **DockerHub** by typing ``docker pull xc200/721p2:latest``, and then typing ``docker run -p 8080:8080 xc200/721p2:latest`` to run the application.

___Kubernetes:___  

1. Start the minikube: `minikube start`
2. Create a deployment: `kubectl create deployment ids721p2 --image=registry.hub.docker.com/xc200/721p2`
4. Create service and expose it: `kubectl expose deployment ids721p2 --type=LoadBalancer --port=8080`
5. View services:  `kubectl get service ids721p2`
6. View URL: `minikube service ids721p2 --url`
7. Curl web service: i.e. `curl http://192.168.49.2:31174`
8. Cleanup and stop: 
```bash
kubectl delete service get-songs
kubectl delete deployment get-songs
minikube stop
````
