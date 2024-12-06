
(!)  If you're here to remedy our cluster, visit [this section](https://github.com/CentaurusInfra/alnair/wiki/Alluxio-Cluster-Installation-and-Speed-Test-Results#quick-steps-to-check-and-remedy-our-alluxio-cluster).

- [Why Data Orchestration](#why-data-orchestration)
  * [Data Orchestration Research](#data-orchestration-research)
- [Introduction to Alluxio](#introduction-to-alluxio)
  * [The Challenges Being Addressed By Data Orchestration Layer](#the-challenges-being-addressed-by-data-orchestration-layer)
  * [Noteworthy Feature: Lineage and Checkpointing](#noteworthy-feature--lineage-and-checkpointing)
  * [Alluxio User-base](#alluxio-user-base)
  * [Alluxio Owners and Managers](#alluxio-owners-and-managers)
- [How To Installation Alluxio Cluster](#how-to-installation-alluxio-cluster)
  * [Downloads](#downloads)
  * [Docker](#docker)
  * [MacOS Homebrew](#macos-homebrew)
  * [Cloning & Building Code From Github](#cloning---building-code-from-github)
- [Alnair Alluxio Performance Tests](#alnair-alluxio-performance-tests)
  * [Our Alluxio Cluster Setup](#our-alluxio-cluster-setup)
  * [Performance Expectations and Underlying Math](#performance-expectations-and-underlying-math)
  * [Using "dd" utility to copy files and measure speeds](#using--dd--utility-to-copy-files-and-measure-speeds)
  * [Running network-speed.py to Measure Data Transfer Speeds](#running-network-speedpy-to-measure-data-transfer-speeds)
  * [Alluxio Test Setup](#alluxio-test-setup)
  * [Test Results](#test-results)
- [Quick Steps to Check and Remedy Our Alluxio Cluster](#quick-steps-to-check-and-remedy-our-alluxio-cluster)
  * [Step 1: Stopping Alluxio Cluster](#step-1--stopping-alluxio-cluster)
  * [Step 2: Starting Alluxio Cluster](#step-2--starting-alluxio-cluster)
- [Other Helpful Bundled Scripts & Their Purpose](#other-helpful-bundled-scripts---their-purpose)
- [This is all Great. But, How Do I Use Alluxio??](#this-is-all-great-but--how-do-i-use-alluxio--)
- [Helpful Notes](#helpful-notes)
- [References](#references)

# Why Data Orchestration
Large-scale analytics and AI/ML applications require efficient data access, with data increasingly distributed across multiple data stores in private data centers and clouds. Data platform teams also need the flexibility to introduce new data sources and move to new storage options with minimal changes or downtime for their applications. This paper delves further into what’s driving the need for--and what problems are solved with—an Alluxio data orchestration layer as part of a modern data platform.

## Data Orchestration Research

* Please read the Alluxio Whitepaper here: https://www.alluxio.io/app/uploads/2019/09/Whitepaper-Why-Data-Orchestration.pdf
* Please review the original Alluxio thesis here: https://escholarship.org/uc/item/4n80320w

# Introduction to Alluxio
Alluxio is an open-source virtual distributed file system (VDFS). It started as a research project "Tachyon" at UC Berkeley's AMPLab as Haoyuan Li's Ph.D. Thesis. Alluxio sits between computation and storage in the big data analytics stack. It provides a *data abstraction layer for computation frameworks, enabling applications to connect to numerous storage systems through a common interface*. Alluxio serves as a high performance Cache for the large data to the computation frameworks.

The software is published under the Apache License. At the time of this writing, it's stable version is 2.8.0.

In a nutshell, Alluxio is World’s first cloud native, hybrid, Data Orchestration and Caching Service compatible with many clouds and many storages. Alluxio is a clustered system, with the master managing the API interface, and the workers pooling in memory. The total memory available for all data is equal to the sum of RAM exposed to Alluxio by all the workers combined.

## The Challenges Being Addressed By Data Orchestration Layer
The increasing complexity in the stack creates challenges in multi-fold. Data is siloed in various storage systems, making it difficult for users and applications to find and access the data efficiently. For example, for system developers, it requires more work to integrate a new compute or storage component as a building block to work with the existing ecosystem. For data application developers, understanding and managing the correct way to access different data stores becomes more complex. For end users, accessing data from various and often remote data stores often results in performance penalty and semantics mismatch. For system admins, adding, removing, or upgrading an existing compute or data store or migrating data from one store to another can be arduous if the physical storage has been deeply coupled with all applications.
To address these challenges, this dissertation proposes an architecture to have a Virtual Distributed File System (VDFS) as a new layer between the compute layer and the storage layer. Adding VDFS into the stack brings many benefits.
1. Improved Data Read Performance
1. Improved Data Write Performance
1. No silos - stay with _your preferred_ big-data system

People have been trying to solve the above challenges by taking the following two approaches: a) create a better (faster, cheaper, or easier to use) storage system, which becomes yet another data silo, or b) create a better (faster, easier to program, or more generic) computation framework, which is either and try to convince the ecosystem that a single framework can address all workloads. However, over the past four decades, we have seen that neither of the two approaches have worked.


![image](https://user-images.githubusercontent.com/105383186/171272488-c8cb42b7-efc1-4ddf-989f-2163d8921752.png)
> > > High Level System Interface Architecture of Alluxio

## Noteworthy Feature: Lineage and Checkpointing
In addition to providing high performance caching for large datasets, Alluxio also utilizes the concept of Checkpointing, termed as "Lineage". Alluxio allows every job in a DAG of jobs to submit a "lineage" (similar to a dependency) information describing how to produce the ouptut for that particular job from the given input. If the job is lost, the lineage automatically guarantees that Alluxio can recompute by re-executing the lost job. This also makes Alluxio fault-tolerant as long as the scheduled jobs are *deterministic*.

The Alluxio provides a FUSE (File System in User Space) POSIX interface and POSIX API, which is a generic solution for the many storage systems supported by Alluxio. Data orchestration and caching features from Alluxio speed up I/O access to frequently used data.

Alluxio can be deployed on-premise, in the cloud (e.g. [Microsoft Azure](https://en.wikipedia.org/wiki/Microsoft_Azure), [AWS](https://en.wikipedia.org/wiki/Amazon_Web_Services), [Google Compute Engine](https://en.wikipedia.org/wiki/Google_Compute_Engine)), or a hybrid cloud environment. It can run on bare-metal or in a containerized environments such as [Kubernetes](https://en.wikipedia.org/wiki/Kubernetes), [Docker](https://en.wikipedia.org/wiki/Docker_(software)), [Apache Mesos](https://en.wikipedia.org/wiki/Apache_Mesos).

More information can be found [here](https://escholarship.org/uc/item/4n80320w).

## Alluxio User-base
Alluxio is used in production to manage Petabytes of data in many leading companies, with the largest deployment exceeding 3,000 nodes. You can find more use cases at [Powered by Alluxio](https://www.alluxio.io/powered-by-alluxio) or visit our first community conference ([Data Orchestration Summit](https://www.alluxio.io/data-orchestration-summit-2019/)) to learn from other community members!

## Alluxio Owners and Managers
Alluxio Open Source Foundation is the owner of Alluxio project. Project operation is done by Alluxio Project Management Committee (PMC). You can checkout more details in its structure and how to join Alluxio PMC [here](https://github.com/Alluxio/alluxio/wiki/Alluxio-Project-Management-Committee-(PMC)).

# How To Installation Alluxio Cluster
## Downloads

Prebuilt binaries are available to download at [https://www.alluxio.io/download](https://www.alluxio.io/download).

## Docker

Download and start an Alluxio master and a worker. More details can be found in [documentation](https://docs.alluxio.io/os/user/stable/en/deploy/Running-Alluxio-On-Docker.html).

```
# Create a network for connecting Alluxio containers
$ docker network create alluxio_nw
# Create a volume for storing ufs data
$ docker volume create ufs
# Launch the Alluxio master
$ docker run -d --net=alluxio_nw \
    -p 19999:19999 \
    --name=alluxio-master \
    -v ufs:/opt/alluxio/underFSStorage \
    alluxio/alluxio master

# Launch the Alluxio worker
$ export ALLUXIO_WORKER_RAMDISK_SIZE=1G
$ docker run -d --net=alluxio_nw \
    --shm-size=${ALLUXIO_WORKER_RAMDISK_SIZE} \
    --name=alluxio-worker \
    -v ufs:/opt/alluxio/underFSStorage \
    -e ALLUXIO_JAVA_OPTS="-Dalluxio.worker.ramdisk.size=${ALLUXIO_WORKER_RAMDISK_SIZE} -Dalluxio.master.hostname=alluxio-master" \
    alluxio/alluxio worker
```

## MacOS Homebrew
`$ brew install alluxio`

## Cloning & Building Code From Github

`git clone https://github.com/Alluxio/alluxio.git`

Please note that Alluxio can be deployed using all of the below methods. An in-depth description is beyond the scope of this page, but the user is encouraged to follow these links -
1. [Single Node Local Experimental Deployment](https://docs.alluxio.io/ee/user/stable/en/deploy/Running-Alluxio-Locally.html)
1. [Running on a Bare-metal Cluster](https://docs.alluxio.io/ee/user/stable/en/deploy/Running-Alluxio-On-a-Cluster.html)
1. [Deploying on Kubernetes](https://docs.alluxio.io/ee/user/stable/en/deploy/Running-Alluxio-On-Kubernetes.html)
1. [Deploying a Cluster With HA](https://docs.alluxio.io/ee/user/stable/en/deploy/Running-Alluxio-On-a-HA-Cluster.html)

# Alnair Alluxio Performance Tests
## Our Alluxio Cluster Setup

Feel free to checkout the web interface of our Alluxio Cluster at [Alluxio Cluster Overview Dashboard](http://10.145.41.28:19999/overview). This interface is provisioned by the Master. The dashboard interface allows monitoring of the workers, an overview of the cluster usage, the ability to view various worker and master logs and a live view and control of the metrics and configurations, respectively.

Our current cluster consists of a single master node at IP address 10.145.41.28, i.e., node v2r2-dfx8, serving port 19999 and below set of workers:

Node IP | FQDN | Role | Worker Capacity
-- | -- | -- | --
10.145.41.28 | v2r2-dfx-8 | Master | -
10.145.41.31 | blue4 | Worker | 100.00GB
10.145.83.34 | titan34 | Worker | 100.00GB
10.145.41.35 | fw0013513 | Worker | 62.51GB
10.145.41.36 | fw0013512 | Worker | 62.51GB
10.145.41.37 | fw0013511 | Worker | 62.51GB
| | **TOTAL** | All Workers | **387.54 GB**

## Performance Expectations and Underlying Math

Before evaluating and confirming Alluxio integration as our data orchestration platform, we wanted to compute mathematically and also measure the performances of various means of serving data for our AI platform needs. To do that, we measured below data transfer speeds using the indicated methods:

1. NETWORK: We used `iperf3 -s` to measure our network's bandwidth and found that our network is capable to transfer data up to 1 GBPS Read and several 100 MBPS Write speeds, but with caching in place.
2. LOCAL HDD: We also measured the performance of local hard drives and depending on the type (HDD, SSD..) the performance was "good". This was measured using `sudo hdparm -Tt /dev/sdc`.
3. Please note that "good" here is an oversimplification to convey that - read and write access into cloud storages will be the slowest possible way to serve data because a large volume of data is being served over the internet, such as from S3 or Azure Storage. In contrast, the volume data accesses using NFS mounts will be an order of magnitude faster, but will be an order of magnitude slower than bulk data accesses into local disks. Also an SSD (Solid State Drive) will offer much after access times than HDD (magnetic hard disks).
4. The fastest way to serve volume data is to keep it all in memory either on the GPU, in the GPU memory on which the training is being run OR be served by an always-in-memory zero-copy data orchestration system, such as Alluxio.

So, we certainly expect robust performance gains from our Alluxio based data orchestration, 1000s of times faster than other alternatives mentioned above.

In order to measure the performance, two methods were used:

## Using "dd" utility to copy files and measure speeds
It'd be prudent to explain with an example to convey the test setup:

```
$ time dd oflag=direct if=/mnt/fuse2/dd-test-0.5k-128k-of of=/tmp/foo bs=512 count=128k
131072+0 records in
131072+0 records out
67108864 bytes (67 MB, 64 MiB) copied, 3.8003 s, 17.7 MB/s <-----------------

real    0m3.844s
user    0m0.129s
sys     0m1.161s
```
This indicates that the **READ** speed from Alluxio is ~ 17.7 MBPS. The option **oflag=direct** forces DIRECT data transfer, and skips kernel buffers, forcing true throughput tests. Similar command without the oflag=direct renders MUCH better throughput but is **not the appropriate experiment for Alluxio setup, because we cannot presume kernel buffering unconditionally**.

```
$ time dd  if=/mnt/fuse2/dd-test-0.5k-128k-of of=/tmp/foo bs=512 count=128k
131072+0 records in
131072+0 records out
67108864 bytes (67 MB, 64 MiB) copied, 0.354625 s, 189 MB/s <--------------------

real    0m0.357s
user    0m0.084s
sys     0m0.273s
```

## Running network-speed.py to Measure Data Transfer Speeds
We also measured volume data transfer speeds programmatically. Please find the code here: <tbd>

```
$ python3 network-speed.py
Enter Drive Path: /mnt/fuse2/dd-test-0.5k-128k-of
Enter Block Size in Bytes: 512
Enter Number of blocks: 131072
Writing: 0.39 %  # <------------ This counter counts to 100% and provides below report after
...
Writing: 100.00 %
Write Speed: 118.88MB/s
Read Speed: 235799.15MB/S
```
The programmatic approach however does exploit and benefit from kernel buffering, *and the numbers do not seem trustworthy, as you can imagine.


* Below data is collected from a series of above two experiments - with `dd oflag=direct` and with `network-speed.py`.
* Reading and writing smaller blocks (512 bytes as opposed to 512KB) is 20x slower (18 MBPS instead of 400+MBPS), but this is not the right test, because "data" volumes designed for large sized data files have LARGER filesystem block sizes. For example, default block size on S3 is 64MB and HDFS is 128MB, not 0.5 or 1KB or even 64KB !

(All data is in MBPS)
|                 | Read (dd, 512K blocks of size 512K) | Write(dd, 512K blocks of size 512K) |
|-----------------|--------------------|--------------------|
| Alluxio         |       374          |        423         |
| local disk(HDD) |       210          |        202         |
| NFS disk (HDD)  |       117          |         85         |

## Alluxio Test Setup

After deploying Alluxio on the above cluster, 

* Alluxio is mounted using FUSE file system in a folder.
* Alluxio FUSE folder is then mounted as shared volume as a volumeMount in Kubernetes Pod of our test runs

## Test Results

* Each row here represents about a 40+ test runs and the numbers are averaged rounded off to two digits.

Jobs | Mask-RCNN | Load time | Cifar10-Classifier | Load time
-- | -- | -- | -- | --
NFS | 4m50s | 28s | 1m43s | 5.0s + 3.0 sec
Local Dir | 4m8s | 2m (~47mbps) | 1m34s | 5.0s + 2.5 sec
Alluxio | 4m20s | 24s | 1m41s | 5.0s + 1 sec

_Note that scheduling the pod on to a node, mounting volumes and pulling docker image takes time. These are considerable sometimes and are excluded from the above data._

# Quick Steps to Check and Remedy Our Alluxio Cluster

(This section is being improved and will be awesome by end of this week.)

First visit the Alluxio Overview dashboard at <master-ip-address-or-fqdn>:19999, and if that does not load, pleae follow below steps:

## Step 1: Stopping Alluxio Cluster
Note: Replace <installed-version> with the version of Alluxio you're currently running or planning to run next.

```
ssh <master>  # In our case, master is v2r2-dfx-8, or 10.145.41.28
cd ~nikunj/alluxio-<installed-version>
export PATH=`pwd`/bin:$PATH
alluxio-stop.sh all  # This may take 3-5 mins

for worker in `cat ~/alluxio-<installed-version>/conf/workers | grep -v "^#"`; do
  ssh $worker "cd alluxio-<installed-version> && ./integration/fuse/bin/alluxio-fuse mount";
done | awk '{print $2}' | sort -u > /tmp/alluxio-fuse-mounts

for worker in `cat ~/alluxio-<installed-version>/conf/workers | grep -v "^#"`; do
  for mountpoint in `cat /tmp/alluxio-fuse-mounts`; do
    ssh $worker "cd alluxio-<installed-version> && ./integration/fuse/bin/alluxio-fuse umount $mountpoint"
  done
  echo "Worker $worker cleaned"
done
# You may want to ignore any errors in above loop / command. The goal is to stop every JVM related to Alluxio so that we get a clean stop of the cluster. So, you might need to force kill any processes (JVMs), or not, depending on errors, if there were any.

# Keep this file if you'd restart the same mounts later. If existing mounts no longer mater, delete this file.
rm -f /tmp/alluxio-fuse-mounts
```

## Step 2: Starting Alluxio Cluster

```
cd ~nikunj/alluxio-<installed-version>
export PATH=`pwd`/bin:$PATH
alluxio-start.sh all  SudoMount # This may take 5-7 mins

# Please note that if file /tmp/alluxio-fuse-mounts from 
for worker in `cat ~/alluxio-<installed-version>/conf/workers | grep -v "^#"`; do
  for mountpoint in `cat /tmp/alluxio-fuse-mounts`; do
    ssh $worker "cd alluxio-<installed-version> && ./integration/fuse/bin/alluxio-fuse mount -o allow_other,nonempty $mountpoint"
  done
  echo "Worker $worker cleaned"
done

# DO NOT ignore any errors.
# If there are errors now, please share with me (nparekh@futurewei.com) or research or debug them.
The goal is to bring up the Alluxio cluster up in a clean manner, free of all errors. At this point, often any errors may point to systemic issues - disk full, /tmp full, network issues, **unintended workers in the cluster, or desired workers not reachable, etc.**. If you notice, the file ~/alluxio-<installed-version>/conf/workers contains the list of FQDNs or IP addresses of the desired workers in the Alluxio cluster.
```

# Other Helpful Bundled Scripts & Their Purpose
|   |Bundled Alluxio Script &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp; &nbsp;  &nbsp; &nbsp; |  Purpose  &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;
|  --  | --------------------------  |  --
|    1  |  `alluxio` |  Manage core extensions of the system - try "alluxio", or "alluxio fs"
|    2  |  `alluxio-common.sh`  |  Internal utility not directlyl used
|    3  |  `alluxio-masters.sh`  |  Takes a shell command as argument and executes it as a task on all masters. Output stored in logs/task.log
|    4  |  `alluxio-workers.sh`  |  Takes a shell command as argument and executes it as a task on all masters. Output stored in logs/task.log
|    5  |  `alluxio-monitor.sh`  |  Accepts arguments to start various helper processes on cluster - the masters, job_masters, workers, job_workers, peoxies, hub_agent, hub_manager, etc
|    6  |  `alluxio-mount.sh`  |  Utiilty to Mount/Unmount/SudoMount/SudoUnmount the mounts on all workers or local machine. (I personally perfer a shell loop as explained in above section.)
|   7  |  `alluxio-start.sh`  |  Start various cluster processes and cluster modes depending on arguments
|    8  |  `alluxio-stop.sh`  |  Stop various cluster processes and cluster modes depending on arguments
|    9  |  `launch-process`  |  Launches an Alluxio processes in foreground, like master, job_master, hub_agent, secondary_master etc

# This is all Great. But, How Do I Use Alluxio??

A helpful tool will be provided for this. For now consider following below steps:

1. **Load Your Data Into Alluxio:** Login to any of the Alluxio cluster workers and create a new "FUSE mount" to store your data. Use a path similar to example below. You can also house your data anywhere else as long as your directories are accessible over the NFS mount with any one of the Alluxio workers.
```
sudo mkdir -p /mnt/fuse2/rockstar-user/my-rock-concert-experiment/data/
sudo chown rockstar-user.rockstar-user /mnt/fuse2/rockstar-user/my-rock-concert-experiment/data/
chmod 0755 /mnt/fuse2/rockstar-user/my-rock-concert-experiment/data/
```
Now, copy your data into that directory
`cp -r <source of data> /mnt/fuse2/rockstar-user/my-rock-concert-experiment/data/`

2. **Add FUSE Mount:** Add this directory as a new FUSE mount into Alluxio
```
for worker in `cat ~/alluxio-<installed-version>/conf/workers | grep -v "^#"`; do
    ssh $worker "hostname ;
        echo "^^^^^";
        cd alluxio-<installed-version>/ && ./integration/fuse/bin/alluxio-fuse mount -o allow_other,nonempty /mnt/fuse2/rockstar-user/my-rock-concert-experiment/data/ /alluxio-data/rockstar-user/my-rockstar-concern-experiment/data";
    echo -----;
done
```
This is a one-time operation per new data (and I am trying to see if we can make it one-time-operation-ever. Once the above operation successfully completes, all the data has been hosted "in-memory", in Alluxio and will be served by Alluxio at a high performance, with a high throughput Read and Write speeds, using the FUSE filesystem mount.

Please verify Alluxio Dashboard to ensure all te data has been persisted, because that can take a long time. However, data is served as soon as above operation has completed without any errors.

(!) If you notice any failed copy operations, please verify that the cluster is indicated to be in a "Healthy" condition on the dashboard, and that no workers are missing and no unintended workers are present in the Workers tab as well as the workers file.

3. Mount the directory in your Kubernetes Job / Pod as a **hostPath volumeMount**, as shown below:

```
...
spec:
  containers:
  - name: ...
    image: ...
    command: ...
    volumeMounts:
    - mountPath: <container dir ...>
      name: rockstar-data

  volumes:
  - name: rockstar-data
    hostPath:  # <-- Use hostPath mount. Alluxio will magically provision your data on all GPUs in the Alluxio cluster
      path: /mnt/fuse2/rockstar-user/my-rock-concert-experiment/data/
      type: DirectoryOrCreate  # <-- Use this type
...
```

(A tool will be provided to automatically generate this.)

Consider reading up on FUSE filesystem from links in Reference section!

***


# Helpful Notes
1. **Access privilege requirements:** The only time root user access is required is for mounting the data (creating /mnt/fuse2/ dirs)
2. **Node discovery through host name:** If only a certain GPU nodes can be added as Alluxio workers, then that is a "special case" configuration and appropriate Node Affinity needs to be defined on the Job/Pod spec in order for the deployment to select that node.

# References
1. [Monitor Our Alluxio Cluster: Overview](http://10.145.41.28:19999/overview)
1. [Alluxio.io](https://www.alluxio.io/)
1. [Wikipedia: FUSE](https://en.wikipedia.org/wiki/Filesystem_in_Userspace)
1. [FUSE: The Linux Kernel Docs](https://www.kernel.org/doc/html/latest/filesystems/fuse.html)
1. [Alluxio FUSE-based POSIX API](https://docs.alluxio.io/os/user/stable/en/api/POSIX-API.html)
1. [Alluxio FUSE Daemon Docker Image](https://hub.docker.com/r/alluxio/alluxio-fuse/)
1. [Original Alluxio Thesis](https://escholarship.org/uc/item/4n80320w)
1. [Data Orchestration Whitepaper](https://www.alluxio.io/app/uploads/2019/09/Whitepaper-Why-Data-Orchestration.pdf)