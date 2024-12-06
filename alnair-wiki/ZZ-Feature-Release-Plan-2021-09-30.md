## 1. Intelligent GPU allocation
* **Team: Yaohui(owner), David**
* **Goal:** Tailor Kubernetes' scheduler for AI workloads, considering the cluster-wise GPU status and historical execution results
* **Functions**
  * Determine gpu counts, type, location(nodes), etc., for each given job
  * Resource allocation, reclaim, dynamic scaling (for already running job, not initialization, to-do in current elastic training framework) 
  * Multi-objective: maximize utilization, minimize fragmentation, mitigate workload interference to cover various allocation scenarios (multiple gpu, single gpu, fraction gpu, gpu+cpu)
  * Refer to historical execution records, using ML to find the better solutions 
  * Over-allocate/recycle/preempt/re-balance, hard/soft limit
  * Define metrics to evaluate scheduling results
* **Done**
  * Interference analysis on sharing GPU (6 workloads, 3 type of GPUs, titanX, k80, RTX2080)
  * Complete interference analysis report, maybe packing suggestions (GPU util no more than 70%), and interference metrics (throughput)
  * Get familiar with scheduling framework, e.g. Yoda scheduler, Kubernetes scheduling SIG
  * Modify score plugin with static metrics
  * Integrate co-scheduling plugin in the default scheduler and deploy to cluster env
* **To-do**
  * Integrate co-scheduling plugin to default scheduler and update elastic framework's scheduler and pod template to enable co-scheduling
  * Integrate customized score plugin, consider GPU type and Affinity in the score function 
* **Status**
  * **Investigation & Design (100%)--> Development & Test (50%)**
* **Questions**
  * Do we extend Kubernetes scheduler? or just modify pod yaml (be simple) A: two layers of scheduling, top: allocator, bottom: kubernetes default scheduler. Work on the bottom mainly.
  * Job Migration (3rd release)
  * GPU resolution (1)
  * Notes: scheduling policy conflicts (e.g. spread v.s. minimize resource fragmentation)

## 2. Workload-oriented profiling
* **Team: Zhaobo(owner), Ziyu**
* **Goal:** 
  * Collect workload resource utilization data, reflect resource availability of the cluster, for scheduler to make decisions based on availability
  * Collect workload behavior data, infer workload type, completion time, for scheduler to make decision based similarity, feedback (previous execution efficiency)  
* **Function**
  * report GPUs attributes and utilization on each node
  * monitor DLT jobs behavior, report resource utilization and workload characteristics on each job, store job execution data (start, complete time, no of GPUs used, etc.)
  * provide dry-run function to elastic horovod jobs and store structured execution results with various configurations
* **Done**
  * Explore metrics collection library (cadvisor, nvml, metrics-server, nvprof, dcgm)
  * Identify metrics that represent workload characteristics (cpu/gpu/memory/memcpy util, disk io, network bandwidth) (cuda API call distribution, input data location/size, model type, weight size)
  * Associate GPU process ID to k8s pod name, and annotate pod with "patch_namespaced_pod" 
  * Patched GPU mem_used to pod, remove annotation after job (GPU processes) is done
  * Dry-run (trial job) CRD and controller design
* **To-do** 
  * Aggregate pod level metrics to owner job, add DLT job annotation tagging (multiple components), results storing (Prometheus)
  * Complete the profiling trial job controller implementation
* **Future** 
  * Characterize jobs (infer job type, complete time, current iteration, execution stage, performance bottleneck, co-location, interference impact)

* **Status**
  * **Investigation & Design (100%)--> Development & Test (50%)**
* **Questions**
  * dry-run control before scheduling, how much extra time is allowed? (offline, collect training data, or customer choice, optional function, switch on/off)
  * the k8s resource used to run DLT, pod, job, or CRD? Q: CRD, modified Job
  * do we assume the logs of training jobs are accessible? current step and epoch, current accuracy/loss, Q: Yes
## 3. GPU sharing and isolation
* **Team: Hao(owner)**
* **Goal:** Limit memory and threads(computing resources) for container process using CUDA API intercept and MPS two solutions, stretchy goal: a complete Kubernetes device plugin that supports GPU sharing 

* **Functions**
  * CUDA API wrapper to intercept memory allocation/de-allocation and kernel launch functions
  * Utilization monitoring, grant/reject resource requests from processes
  * Compute resources isolation for AI inference workloads, fair share 
  * MPS solution: configure limits, investigate and mitigate interference 

* **Done**
  * Explore Gaia and KubeShare two GPU sharing implementation methods and principles
  * Complete smoke test of using LD_PRELOAD, solve segmentation fault caused by symbol missing.
  * Demo cuda api intercept with preloaded .so library in docker container, .so library is mounted from host to container.
  * Design the components and data flow for K8s GPU plugin to support GPU virtualization. including intercept library, vGPU registration server,
  * Implement TCP based registration server to support information sharing between host and its containers (local communication).  
  * Explore how CUDA driver API is used among different ML frameworks
* **To-do**
  * Complete the intercept lib function, to constraint container's GPU mem and compute resource usage in a couple of typical scenarios
  * Test the accuracy and stability of the intercept lib. e.g., if the container's GPU utilization is indeed within the requested range (50%)
* **Future**
  * Complete the entire GPU plugin to support fractional GPU request
  * nVidia kernel space reverse engineering
* **Status**
  * **Investigation & Design (70%)--> Development & Test (20%)**
* **Questions**
  * LD_PRELOAD limitation
  * pytorch and tensorflow(not clear use of cuda runtime lib) cuda call differences
  * if we need to wrap all APIs
  * What's ML framework's response when system/cude reject memory allocation (reach limits), whether training job can keep running with limited memory?