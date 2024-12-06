## Alnair Profiler Scope
### 1. Target

Node, Pod, Job (customized training jobs) --> Based on keys (PodName+NodeName+StartTime), save raw utils results in the same format(tabular data), and aggregate later according to different needs.

### 2. Metrics

1. CPU/memory util, GPU/mem/mem_cpy util, disk io, network util
2. CUDA-level metrics
3. Python-level metrics, e.g., framework, model architecture, ...

### 3. Library

1. Nvml (GPU attributes and metrics), linux system files, e.g. procs (cpu/memory/io metrics)
2. Custom intercept library, spit out metrics to log files

### 4. Action

1. Continuous resource utilization monitoring, and store cluster pods' max utilization data
2. Self-trigger short-term trial jobs with different placement configuration --> Switch to Alnair Job controller function with enable profiling flag
3. Job performance bottleneck analysis


## [Nvidia Nsight Systems](https://developer.nvidia.com/nsight-systems)

### 1. Setup
In a containerized environment install cuda toolkit, so ```nsys``` command is available.
```
FROM pytorch/pytorch:1.11.0-cuda11.3-cudnn8-devel
RUN apt-get update && apt-get install -y cuda-toolkit-11-4
```
### 2. Command to profiling
To Collect a profiling report

**```nsys nvprof python XXX.py```**

More nsys command are from this [Nvidia Nsight-systems User Guide](https://docs.nvidia.com/nsight-systems/UserGuide/index.html)

### 3. Results
Sample output includes
```
Exported successfully to
/tmp/nsys-report-fdb7-af55-7315-c31c.sqlite


CUDA API Statistics:

 Time(%)  Total Time (ns)  Num Calls  Average (ns)  Minimum (ns)  Maximum (ns)  StdDev (ns)               Name
 -------  ---------------  ---------  ------------  ------------  ------------  -----------  -------------------------------
    38.8       4657677341     523848        8891.3          3352      18555196      45882.5  cudaLaunchKernel
    37.7       4521928840          1  4521928840.0    4521928840    4521928840          0.0  cudaMemGetInfo

CUDA Kernel Statistics:

 Time(%)  Total Time (ns)  Instances  Average (ns)  Minimum (ns)  Maximum (ns)  StdDev (ns)                                                  Name
 -------  ---------------  ---------  ------------  ------------  ------------  -----------  ----------------------------------------------------------------------------------------------------
     6.2       1078398020     145039        7435.2          3008         83777      11407.4  void at::native::vectorized_elementwise_kernel<(int)4, at::native::BinaryFunctor<float, float, floa…
     5.2        899943893       5061      177819.4         77825        286819      66300.8  volta_scudnn_128x64_stridedB_splitK_medium_nn_v1
     5.0        864861126       5543      156027.6        106338        202018      27548.5  void wgrad_alg0_engine<float, (int)128, (int)6, (int)7, (int)3, (int)3, (int)5, (bool)0, (int)512>(…

CUDA Memory Operation Statistics (by time):

 Time(%)  Total Time (ns)  Count  Average (ns)  Minimum (ns)  Maximum (ns)  StdDev (ns)      Operation
 -------  ---------------  -----  ------------  ------------  ------------  -----------  ------------------
    78.7        421996974   1048      402668.9          1759       1814834     713867.9  [CUDA memcpy HtoD]
    21.3        114288548  28205        4052.1          1664         16480       1771.9  [CUDA memset]
     0.0            51136     24        2130.7          1984          3040        301.5  [CUDA memcpy DtoH]



CUDA Memory Operation Statistics (by size):

 Total (MB)  Count  Average (MB)  Minimum (MB)  Maximum (MB)  StdDev (MB)      Operation
 ----------  -----  ------------  ------------  ------------  -----------  ------------------
  18596.704  28205         0.659         0.000         3.981        0.834  [CUDA memset]
   4232.271   1048         4.038         0.000        17.165        7.193  [CUDA memcpy HtoD]
      0.000     24         0.000         0.000         0.000        0.000  [CUDA memcpy DtoH]
```

And complete timeline view are saved to the file and can be viewed from nsight system.
```
Report file moved to "/root/scripts/report2.qdrep"
Report file moved to "/root/scripts/report2.sqlite"
```
### 4. Visualization 
Copy the report out from the container to your host machine and then download/scp to your PC

```kubectl cp sharing-pytorch:/root/scripts/report2.qdrep report2.qdrep```

Ignore the ```tar: Removing leading `/' from member names``` complains. File can be copied out.

View .qdreq timeline file with [Nsight System](https://developer.nvidia.com/gameworksdownload#?dn=nsight-systems-2022-3)

View .sqlite database file with [DB browser](https://sqlitebrowser.org/dl/)
