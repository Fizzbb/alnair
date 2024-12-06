**Profiler**
* Collect multidimensional data (GPU, CPU, Network). Fine-grained (process level)
* Collect/infer job related data (model size, data set, completion time, current progress, resource utilization)
* Anomaly detection (job freeze)

**Elastic Framework**
* Framework comparison: Horovod vs Torch Elastic vs Kungfu, across server communication overhead evaluation
* New network protocol for gradients exchange
* Hyper-parameter auto adjustment during scaling
* Auto data partition during scaling
* Design pattern of elastic framework on resource management system (Horovod on Ray)

**GPU Sharing/Virtualization**
* MPS-based solution, packing performance analysis, interference mitigation/isolation improvment
* CUDA API solution, memory allocation, multiprocessing
* Job migration, checkpoint, snapshot

**Scheduling Algorithms**
* Heterogeneous resource scheduling CPU + GPU for reinforcement learning
* Fairness for all users, topology/locality aware
* Continuously re-balance 
* Learning base solution using job execution history 

**Ray**
* Architecture of using Ray, Ray within Kubernetes
* Ecosystem activities

**ML Framework and Engine**
* Reduce memory usage, Reduce resolution
* Model parallelism
* Hyper-parameter tuning, fast search, early termination  
* DeepSpeed/Zero-Infinity  