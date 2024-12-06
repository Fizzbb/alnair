# Prerequisites
* CX-5 and driver (ofed 5.4)
* GPU and driver (510)
* linux kernel version (5.15)


# Basic Procedure and Commands
### 1. Install drivers and dependent libraries
* [Install Mellanox ofed driver](https://enterprise-support.nvidia.com/s/article/howto-install-mlnx-ofed-driver), check version ```ofed_info```
* Install Nvidia GPU driver, ```apt-get install nvidia-driver-510```
* Install Nvidia container runtime, [add nvidia repo addr and keyring](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/install-guide.html), and install ```apt-get install nvidia-docker2``` 


### 2. Device check up
* ```ibstats```

### 3. Config IP on CX-5 device

### 4. Smoke test
* ```ib_send_bw -a -b -R -d mlx5_2```

### 5. NCCL and Pytorch software stack, rebuild, nccl>=2.14

### 6. Pytorch distributed training test
* change docker default runtime to nvidia, and reload daemon and restart docker, if not done yet

### 7. RDMA packages and speed verification under pytorch application
* Mellanox tcpudump special container

### 8. Training time comparison with and without RDMA

# Advanced, multiple docker container sharing one CX-5 adapter
### MacVlan Configuration