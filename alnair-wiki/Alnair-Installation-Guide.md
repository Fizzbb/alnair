# Install a vanilla Kubernetes cluster
### 1. Prepare two linux nodes (at least one gpu node as worker), install [docker engine](https://docs.docker.com/engine/install/ubuntu/)
* in the ```/etc/docker/daemon.json``` add ```{"exec-opts": ["native.cgroupdriver=systemd"]}```, Then ```systemctl daemon-reload```, ```systemctl restart docker``` this is because kubelet's default driver is systemd, different from docker's default cgroupfs, kubelet cannot start with this difference 
### 2. On the master node, install 1.23 version with [kubeadm](https://kubernetes.io/docs/hsetup/production-environment/tools/kubeadm/install-kubeadm/), and then [create cluster with kubeadm](https://kubernetes.io/docs/setup/production-environment/tools/kubeadm/create-cluster-kubeadm/)
```
 apt-mark unhold kubeadm && apt-get install --allow-downgrades kubeadm=1.23.0-00 &&  apt-mark hold kubeadm
 apt-mark unhold kubelet && apt-get install --allow-downgrades kubelet=1.23.0-00 &&  apt-mark hold kubelet
 apt-mark unhold kubectl && apt-get install --allow-downgrades kubectl=1.23.0-00 &&  apt-mark hold kubectl
```
```
 kubeadm init --pod-network-cidr=10.244.0.0/16  
```
* _in ```kubeadm init``` add network cidr, otherwise later flannel [fails](https://stackoverflow.com/questions/60940447/is-there-a-way-to-assign-pod-network-cidr-in-kubeadm-after-initialization)_
* _after k8s 1.24, you need to install cri-dockerd. Docker Engine does not implement the [CRI](https://kubernetes.io/docs/concepts/architecture/cri/) which is a requirement for a container runtime to work with Kubernetes. For that reason, an additional service [cri-dockerd](https://github.com/Mirantis/cri-dockerd) has to be installed. cri-dockerd is a project based on the legacy built-in Docker Engine support that was [removed](https://kubernetes.io/dockershim) from the kubelet in version 1.24._

### 3. On the master node, Install network plugin [flannel](https://github.com/flannel-io/flannel)
### 4. On the worker node, disable memory swap on the worker nodes ```swapoff -a```
### 5. On the worker node, install ```apt-get install nvidia-docker2``` and set nvidia docker runtime as default runtime
```
{
    "default-runtime":"nvidia",
    "exec-opts": ["native.cgroupdriver=systemd"],
    "runtimes": {
        "nvidia": {
            "path": "nvidia-container-runtime",
            "runtimeArgs": []
        }
    }
}

```
### 6. On the worker node, join the worker nodes to the master
join command can be printed on master node with ```kubeadm token create --print-join-command```
### 7. On the master, Install [nvidia device plugin](https://github.com/NVIDIA/k8s-device-plugin)
### 8. New users add authorization
```
  mkdir -p $HOME/.kube
  sudo cp -i /etc/kubernetes/admin.conf $HOME/.kube/config
  sudo chown $(id -u):$(id -g) $HOME/.kube/config

```
# Install Alnair components
### 1. Install Alnair profiler
### 2. Install CRD and Controller for Elastic Horovod
### 3. Install CRD and Controller for Torch Elastic
### 4. Install vGPU device plugin
### 5. Install vGPU scheduler