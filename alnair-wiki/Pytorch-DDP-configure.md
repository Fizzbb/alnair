
## Overview

**1. master node**: the main gpu responsible for synchronizations, making copies, loading models, writing logs;

**2. process group**: if you want to train/test the model over K gpus, then the K process forms a group, which is supported by a backend (pytorch managed that for you, according to the [documentation](https://pytorch.org/docs/1.9.0/generated/torch.nn.parallel.DistributedDataParallel.html?highlight=distributeddataparallel#torch.nn.parallel.DistributedDataParallel), nccl is the most recommended backend);

**3. rank**: within the process group, each process is identified by its rank, from 0 to K-1;

**4. world size**: the number of processes in the group i.e. gpu number K.

**5. multi-processing**: all children processes together with the parent process run the same code. In PyTorch, torch.multiprocessing provides convenient ways to create parallel processes. As the official documentation says, the ```spawn``` function below addresses these concerns and takes care of error propagation, out of order termination, and will actively terminate processes upon detecting an error in one of them.

## Changes from single process/GPU
### Steps
1. init the process group in training function
```
def train(gpu, args):
    rank = args.nr * args.gpus + gpu	
    dist.init_process_group(
            backend="nccl",
            init_method='env://', # default use environment variable 
            world_size=world_size,
            rank=rank)
```
init method by default set up TCP connections between nodes. Just choose a free port, no need special configuration for the TCP connections.

2. split the dataloader to each process in the group, which can be achieved by torch.utils.data.DistributedSampler or any customized sampler;
```
 train_sampler = torch.utils.data.distributed.DistributedSampler(
    	train_dataset,
    	num_replicas=args.world_size,
    	rank=rank
    )
```
3. wrap the model with DDP
```
model = nn.parallel.DistributedDataParallel(model, device_ids=[gpu])
```
4. spawn processes in main
```
def  main():
	parser = argparse.ArgumentParser()
	parser.add_argument('-n', '--nodes', default=1, type=int, metavar='N',
	help='number of data loading workers (default: 4)')
	parser.add_argument('-g', '--gpus', default="", type=str, help='gpu number list of workers (starting with the master worker). For example, if you have two machines one with 2 gpus and the other one with 8 gpus, the list should be 2, 8')
	parser.add_argument('-i', '--id', default=0, type=int, help='id for each worker and this id should match with the gpu number list. For example, if the GPU list is 2, 8, the id of the machine with 2 gpus should be 0')
	parser.add_argument('--epochs', default=10, type=int, metavar='N', help='number of total epochs to run')
	args = parser.parse_args()
	gpu_list = [int(gpu) for gpu in args.gpus.split(',')]

    #########################################################
    args.world_size = sum(gpu_list)	                    #
    os.environ['MASTER_ADDR'] = '10.57.23.164'              #
    os.environ['MASTER_PORT'] = '8888'                      #
    mp.spawn(train, nprocs=args.gpus, args=(args,))         #
    #########################################################
```

### Launch
### 1. single node multiple GPUs
```
python mnist-distributed.py -n 1 -g 8 -i 0
```
**NOTES**: After a couple of successful run with different gpu counts(>1), the program failed at  ```-g 1```. 

Complains about **some cuda functions before calling NumCudaDevices() that might have already set an error? Error 101: invalid device ordinal (function operator())**

** torch.cuda.is_available() returned false. nvidia-smi shows 7 GPUs instead of 8. **

** Reboot server gpu counts back to 8, and rerun the commands, error did not reproduce. **

### 2. multiple(two) nodes multiple GPUs
on each node launch separately
```
python mnist-distributed.py -n 2 -g 8,2 -i 0
python mnist-distributed.py -n 2 -g 8,2 -i 1
```
In the above launch command, the first worker (master node) has 8 GPUs and the second worker machine has 2 GPUs.

## Catch
### 1. env MASTER_IP needs to be localhost IP, when use in the single node multiple card mode, so when you test out the script on different nodes, remember to change the IP address. Otherwise the program will keep waiting to join the MASTER IP's process.
### 2. If you multiple nodes, make sure use full amount of gpu. If both nodes have 8 cards, you only launch 4 gpu on each nodes, the rank/gpu device setup may mess up. currently only tested 2 nodes, and each nodes have 8 cards scenarios. If use partial GPUs from each node, may need to set CUDA_VISIBLE_DEVICE in the env.

## Backend
### 1. Gloo
### 2. NCCL
### 3. MPI


Reference
1. [code](https://github.com/yangkky/distributed_tutorial/blob/master/src/mnist-distributed.py), https://yangkky.github.io/2019/07/08/distributed-pytorch-tutorial.html
2. [code](https://github.com/The-AI-Summer/pytorch-ddp), https://theaisummer.com/distributed-training-pytorch/
3. https://medium.com/codex/a-comprehensive-tutorial-to-pytorch-distributeddataparallel-1f4b42bb1b51
4. [backend choice](https://pytorch.org/docs/stable/distributed.html)
5. https://www.youtube.com/watch?v=3XUG7cjte2U
6. https://ai.googleblog.com/2022/05/alpa-automated-model-parallel-deep.html


