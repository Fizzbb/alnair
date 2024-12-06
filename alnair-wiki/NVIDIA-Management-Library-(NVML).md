A C-based API for monitoring and managing various states of the NVIDIA GPU devices. It provides a direct access to the queries and commands exposed via nvidia-smi. API reference is [here](https://docs.nvidia.com/deploy/nvml-api/index.html). Chapter 2.14 is about device query.

Python wrapper is available, **pip3 install pynvml**, github location and Enumerates are at [this page.](https://github.com/nicolargo/nvidia-ml-py3/blob/master/pynvml.py) 

****Query-able states includes:****

* ECC error counts: Both correctable single bit and detectable double bit errors are reported. Error counts are provided for both the current boot cycle and for the lifetime of the GPU.
* GPU utilization: Current utilization rates are reported for both the compute resources of the GPU and the memory interface.
* Active compute process: The list of active processes running on the GPU is reported, along with the corresponding process name/id and allocated GPU memory.
* Clocks and PState: Max and current clock rates are reported for several important clock domains, as well as the current GPU performance state.
* Temperature and fan speed: The current core GPU temperature is reported, along with fan speeds for non-passive products.
* Power management: For supported products, the current board power draw and power limits are reported.
* Identification: Various dynamic and static information is reported, including board serial numbers, PCI device ids, VBIOS/Inforom version numbers and product names.

