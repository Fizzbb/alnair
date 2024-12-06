## Current software versions already installed on our setup
Nvidia driver: 510.39.01<br>
CUDA Toolkit: CUDA 11.4
### to install the above driver
0. you may want to upgrade ubuntu version, **NOTE OS upgrade requires interactive response, if network disconnect, may require KVM reboot**
```
sudo apt-get update
sudo apt-get upgrade -y
sudo apt-get dist-upgrade
sudo do-release-upgrade
```
if some package kept upgrade incomplete, purge it and reinstall
1. install nvidia driver
```
sudo apt-get install nvidia-driver-510 -y
sudo reboot
```
2. install cuda toolkit
```
sudo apt-get install cuda-toolkit-11-6
```
3. Add cuda path to your .bashrc, and source .bashrc
```
export CUDA_HOME=/usr/local/cuda-11.6
PATH="${CUDA_HOME}/bin:$PATH"
```
4. Verify
```
nvcc --version
```
```
nvcc: NVIDIA (R) Cuda compiler driver
Copyright (c) 2005-2022 NVIDIA Corporation
Built on Tue_Mar__8_18:18:20_PST_2022
Cuda compilation tools, release 11.6, V11.6.124
Build cuda_11.6.r11.6/compiler.31057947_0
```
## Per user setup
In order to use the CUDA toolkit, each user simply needs to add the following to his/her .profile or .bashrc:

>export CUDA_HOME=/usr/local/cuda<br>
PATH="${CUDA_HOME}/bin:$PATH"<br>
export LD_LIBRARY_PATH="${CUDA_HOME}/lib64"

