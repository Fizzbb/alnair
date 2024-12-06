[Nvidia Blog, Even easier introduction CUDA](https://developer.nvidia.com/blog/even-easier-introduction-cuda/)

[Nvidia Blog CUDA refressher](https://developer.nvidia.com/blog/cuda-refresher-cuda-programming-model/)





* Add Specifier ```__global__``` to functions, which tells the CUDA C++ compiler that this is a function that runs on GPU and call be called from CPU, those ```__global__``` functions are know as kernels.

* CUDA kernel launches are specified using the triple angle bracket syntax ```<<<numBlocks, blockSize>>>```, execution configuration

* CUDA kernel launches don’t block the calling CPU thread, if need the CPU to wait until the kernel is done before it accesses the results, add cudaDeviceSynchronize()

* ```nvcc -x cu``` option allows us to write CUDA code directly in cpp file, Jupyter supports .cpp syntax hightlighting
```
!nvcc -x cu -arch=sm_70 -o monte_carlo_mgpu_cuda_peer exercises/monte_carlo_mgpu_cuda_peer.cpp
%%time
!./monte_carlo_mgpu_cuda_peer
```