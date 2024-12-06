## Definition
Three critical distinctions between serverless and serverful computing [1]:
1. Decoupled computation and storage. The storage and computation scale separately and are
provisioned and priced independently. In general, the storage is provided by a separate cloud
service and the computation is stateless.
2. Executing code without managing resource allocation. Instead of requesting resources, the
user provides a piece of code and the cloud automatically provisions resources to execute that
code.
3. Paying in proportion to resources used instead of for resources allocated. Billing is by some
dimension associated with the execution, such as execution time, rather than by a dimension
of the base cloud platform, such as size and number of VMs allocated.

Serverless simplifies application development by making cloud resources
easier to use. In the cloud context, serverful computing is like programming in low-level assembly
language whereas serverless computing is like programming in a higher-level language such as
Python. The serverless layer sits between applications and the
base cloud platform, simplifying cloud programming.

Serverless vs FaaS
## Common Use Cases
1. web & API serving
2. batch processing

## Serverless Platform on top of Kubernetes
**Note:Inherit Kubernetes limitations (e.g., 110 pods per node, 5000 nodes per cluster)**
1. OpenFaaS
2. Knative
4. Fission
5. Nuclio

## Serverless AI training example

## Serverless AI inference example

## Challenges
1. storage service
2. start-up time
3. coordination/signaling service
4. network/communication
5. security

## Reference
[1]. [Cloud Programming Simplified: A Berkeley View on Serverless Computing](https://www2.eecs.berkeley.edu/Pubs/TechRpts/2019/EECS-2019-3.pdf), 2019 Feb.

[2]. [Performance Evaluation of Open-Source Serverless Platforms for Kubernetes](https://www.mdpi.com/1999-4893/15/7/234/pdf)

[3]. [KubeML github](https://github.com/DiegoStock12/kubeml)