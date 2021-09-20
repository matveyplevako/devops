# Kubernetes

## App deployment

```
# kubectl create deployment app-node --image=matveyplevako/app_python
# kubectl expose deployment app-node --type=LoadBalancer --port=8000
```

## Report for manual deploy

```
# kubectl get pods,svc
NAME                            READY   STATUS    RESTARTS   AGE
pod/app-node-78955456d4-lxgp4   1/1     Running   0          91s

NAME                 TYPE           CLUSTER-IP      EXTERNAL-IP   PORT(S)          AGE
service/app-node     LoadBalancer   10.110.44.176   localhost     8000:32375/TCP   46s
service/kubernetes   ClusterIP      10.96.0.1       <none>        443/TCP          5m48s

```

## Report for automatic deploy

```
# kubectl get pods,svc
NAME                                     READY   STATUS    RESTARTS   AGE
pod/app-python-deploy-64859fd66b-8g4s7   1/1     Running   0          15s
pod/app-python-deploy-64859fd66b-m8j52   1/1     Running   0          15s
pod/app-python-deploy-64859fd66b-ttqj2   1/1     Running   0          15s

NAME                 TYPE           CLUSTER-IP       EXTERNAL-IP   PORT(S)          AGE
service/app-python   LoadBalancer   10.103.241.114   localhost     8888:31436/TCP   15s
service/kubernetes   ClusterIP      10.96.0.1        <none>        443/TCP          26m

```

## Kubernetes terms

- **Ingress** is a resource for adding rules for routing traffic from external sources to services inside the kubernetes
  cluster.
- **Ingress controller** is an application inside the kubernetes cluster that does the actual routing defined with
  ingress.
- **StatefulSet** is a set of tools that provide interface for managing persistent stateful applications.
- **DaemonSet** is a daemon that ensures each node runs a pod and garbage collects them after remove
- **PersistentVolumes** is an abstraction for managing physical storages and provide storage for kubernetes cluster. 

## Helm deploy
```
# kubectl get pods,svc
NAME                            READY   STATUS    RESTARTS   AGE
pod/app-python-9d947d8d-7xrtf   1/1     Running   0          15s
pod/app-python-9d947d8d-crswg   1/1     Running   0          15s
pod/app-python-9d947d8d-kzvv9   1/1     Running   0          15s

NAME                 TYPE           CLUSTER-IP      EXTERNAL-IP   PORT(S)          AGE
service/app-python   LoadBalancer   10.107.213.33   localhost     8000:32031/TCP   15s
service/kubernetes   ClusterIP      10.96.0.1       <none>        443/TCP          90m

```
