# Improvements
## 1. Unified Training Framework 
Owner: David
* Unified job template for distributed/elastic/simple training jobs
* Dynamic job resize with a centralized GPU allocator
* Unified interface for different framework implementation, clear state transition and control

**Design choices**

**1) how to aggregate logs, launcher pod**

**2) multiple gpu per pod or one gpu per pod**

**3) stateful set or individual pod**

## 2. GPU Sharing 
Owner: Hao
* Process level GPU memory usage control through intercept CUDA driver API 
* GPU thread usage control, explore different methods and evaluate delay brought by usage control

**Evaluate LD_PRELOAD setting conflicts between platform and user script, with environment variable or binary**

**Time kernel launch function start and end, sleep on overused thread**
 
## 3. Profiler 
Owner: Ziyu
* MongoDB stored fine-grained job execution record, e.g. no of workers, worker resource utilization distribution etc.
* Persist data with local persist volume

**Failed/Duplicate job records collection, Running job records update**

**ML Framework and CUDA level metrics exporter design**

## 4. Intelligent GPU Scheduler 
Owner: Yaohui
* New score function, and synthetic device ID management, support Alnair vGPU resources
* Scheduling with forecast (GPU utilization and job completion time)

# New
## 1. Test Framework 
Owner: Zhaobo
* MLPerf benchmark
* Average job completion time benchmark (Group of jobs), cluster resource utilization

**[Ali AI Matrix](https://github.com/alibaba/ai-matrix/blob/master/README.md)**

**[Nvidia DeepLearning Example](https://github.com/NVIDIA/DeepLearningExamples)**

**[Amazon SageMaker Example](https://github.com/aws/amazon-sagemaker-examples/)**
## 2. Workload Performance Monitoring 
Owner: Steven
* Track and report Pytorch/Tensorflow/Horovod job execution performance and bottleneck with Nsight and Tensorboard
* Optimize ML Framework and job placement 
