# Motivation
Address new AI application requirements (fast, distributed, learn from the environment)
# Key Features (contributions)
* Unified framework for training, simulation, and serving
* Separate states to sharded control metadata store from stateless components
* Bottom-up distributed scheduling strategy for scalability
* Unify the actor and task-parallel abstractions on top of a dynamic task execution engine (?)
# Programming and Computation Model
## Programming Model
* Tasks: the execution of remote function on a stateless worker
* Actors: a stateful computation
## Computation Model
* Dynamic task graph computation model: execution of both remote functions and actor methods is automatically triggered by the system when their inputs become available
# Architecture
## Application layer
* Driver
* Worker 
* Actor
##  System layer
* Global Control Store
* Bottom-Up Distributed Scheduler
* In-Memory Distributed Object Store
# Programming and Compute Model

# Use Case, Evaluation
## RL Applications
* Evolution Strategies (ES)
* Proximal Policy Optimization (PPO)
# Ecosystem
* RaySGD, Ray Tune, Ray Serve, RLlib
* Ray on public cloud: [cluster launcher](https://docs.ray.io/en/latest/cluster/cloud.html) e.g. on AWS with EC2 instance
* Ray on cluster manager ([Kubernetes](https://docs.ray.io/en/latest/cluster/kubernetes.html)): Ray Operator and CRDs, Pods as nodes

Use [Ray client](https://docs.ray.io/en/latest/cluster/ray-client.html) to connect to a remote Ray cluster
# Reference
[1] [Ray: A Distributed Framework for Emerging AI Applications](https://arxiv.org/abs/1712.05889)

