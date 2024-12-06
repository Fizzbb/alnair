## Original Paper
NeRF stands for Neural Radiance Fields and it was first introduced by  "NeRF: Representing Scenes as Neural Radiance Fields for View Synthesis" in the ECCV 2020 and it received an honorable mention for best paper and has a huge impact in the computer vision field.

## Introduction

### Task: 
NeRF is a view synthesis algorithm. It learns from a set of 2D views of a scene to conduct novel view synthesis (i.e., generating new views).

### Key Idea:  
NeRF is an implicit neural representation approach. Specifically, NeRF is inspired by an optics concept called radiance fields/light fields and NeRF learns a radiance field function approximator (i.e., a neural network) of a 3D scene. After training, people can query an arbitrary view direction of this 3D scene from the neural network and get the corresponding rendering result.

## Why NeRF
NeRF has several nice properties.

<!---
- **Novel view synthesis:** NeRF not only saves the existing limited views from training data but is also able to synthesize new views never seen before.
--->
- **High-resolution 3D rendering:** Thanks to the concept of radiance fields, NeRF is able to build a continuous representation of the scene which allows for very thin and complex structures, and thus provides better renderings than previously-dominant approach of learning a discretized voxel representations.

- **3D scene compression:** Compared with previously-dominant approach of training deep convolutional networks, the original NeRF is implemented with a fully connected neural network with few layers  (5-10 MB), which is much smaller than traditional 3D mesh model size, or even raw images. As a result, NeRF can be considered as a promising technique to compress 3D data.

## NeRF Architecture
A radiance field function $f_\theta(\mathbf{p}, \mathbf{d})$ is approximated by a neural network which  takes an 5D input $(\mathbf{x}, \mathbf{d})$, where  $\mathbf{x} = (x, y, z)$ is a 3D location of a pixel and $\mathbf{d} = (\theta, \phi)$ is a 2D camera direction. The neural network predicts a 4D output $(\mathbf{c}, \mathbf{\sigma})$, where  $\mathbf{c}$  is a 3D RGB color vector and  $\mathbf{\sigma}$ is a density scalar (i.e., the probability density that there is an object at this location). The output later can be used to build a 2D image pixel by using the classic volume rendering techniques.




### Optimization
In order to achieve state-of-the-art rendering quality, the authors used the following two improvements:

- Positional encoding: fitting image contains high frequency variation better

- Hierarchical volume sampling: increasing rendering efficiency

### Video Explanation

A good YouTube video explanation can be found at https://www.youtube.com/watch?v=CRlN-cYFxTk.

### Online Tutorials

https://pyimagesearch.com/2021/11/17/computer-graphics-and-deep-learning-with-nerf-using-tensorflow-and-keras-part-2/


## NeRF Implementation


### Dataset
In order to train a NeRF model for a scene, you need to prepare images of a same scene from different viewing directions. You can also find dataset used in the original paper at https://drive.google.com/drive/folders/128yBriW1IG_3NJ5Rp7APSTZsJqdJdfc1

### Implementation

Official Tensorflow Implementation: https://github.com/bmild/nerf

Pytorch NeRF Implementation: https://github.com/yenchenlin/nerf-pytorch

Pytorch Lighting Implemetation: https://github.com/kwea123/nerf_pl

Simiplifed NeRF (Tiny-NeRF) Implementation: https://github.com/krrish94/nerf-pytorch



## Limitations
The limitations of NeRF are summarized below.

- Each NeRF model can only represent a scene. Therefore, you need to train a model for every scene. You can not re-use the model you trained from another scene to a new scene.

- Even through the NeRF model size is small, training a NeRF model is relatively slow since each training image will lead to millions of training data points (i.e., image width * image height  * number of depth samples). It could take 1-2 days on one V100 and use thousands of images of a scene.

- Rendering is time-consuming. NeRF requires hundreds of MLP invocations per pixel to compute the samples needed by volume rendering. Therefore, it is hard to use NeRF to conduct real-time rendering.

- NeRF only works for the static scene.


## Works in NeRF Acceleration

### Faster Training
-  Depth-supervised NeRF: Fewer Views and Faster Training for Free
    - Repo: https://github.com/dunbar12138/DSNeRF
    - Key idea: additional supervision from depth data recovered from the view pose estimation algorithm. 
    - Results highlight: rendering better images given fewer training views (e.g., 2-5) while training 2-3x faster
-  Direct Voxel Grid Optimization: Super-fast Convergence for Radiance Fields Reconstruction
    - Repo: https://github.com/sunset1995/DirectVoxGO
    - Key idea: using a dense voxel grid to directly model the 3D geometry (volume density) used in NeRF.
    - Insight: a scene is dominated by free space (i.e., unoccupied space). Motivated by this fact, this paper proposed an efficient method to find the coarse 3D areas of interest before reconstructing the fine detail and view-dependent effect that require more computation resources.
    - Results highlight: reducing training time from 10−20 hours to 15 minutes on a machine with a single NVIDIA RTX 2080 Ti GPU
- Instant Neural Graphics Primitives with a Multiresolution Hash Encoding
    - Repo: https://nvlabs.github.io/instant-ngp/
    - Key idea: using an efficient and trainable input encoding component 
    - Results highlight: enabling training of high-quality neural graphics primitives in a matter of seconds, and rendering in tens of milliseconds at a resolution of 1920×1080


### Faster Rendering
- Neural Sparse Voxel Fields
    - Repo: https://lingjie0206.github.io/papers/NSVF/
    - Key idea: A hybrid scene representation that combines neural implicit fields with an explicit sparse voxel structure. Instead of representing the entire scene as a single implicit field, they used a set of voxel-bounded implicit fields organized in a sparse voxel octree. 
    - Insight:  preventing sampling of points in empty space without relevant scene content as much as possible. 
    - Result Highlight:  10 times faster than the first NeRF at inference time while achieving higher quality results
- PlenOctrees for Real-time Rendering of Neural Radiance Fields
    - Repo: https://alexyu.net/plenoctrees/
    - Key idea: pretrain a NeRF and then extract it into a different data structure (i.e., PlenOctree) that can support fast inference.
    - Insight: Efficient storage and pre-calculation
    - Result Highlight: rendering 800×800 images at more than 150 FPS, which is over 3000 times faster than conventional NeRFs
- DeRF: Decomposed Radiance Fields
    - Key idea:  The idea is to spatially decompose  a scene and dedicate smaller networks for each decomposed part. The whole scene can be rendered by rendering each part independently (i.e., using multiple smaller NeRF models), and compositing the final image.
    - Result Highlight:  3x times faster and same or better quality
- KiloNeRF: Speeding up Neural Radiance Fields with Thousands of Tiny MLPs
    - Repo: https://github.com/creiser/kilonerf
    - Key idea: Utilizing thousands of tiny MLPs instead of one single large MLP.
   <!---  - Insight: we first train a regular NeRF as teacher model. KiloNeRF is then trained such that its outputs (density and color) match those of the teacher model for any position and view direction. It is a three-stage training method. --->
    - Result Highlight: three orders of magnitude rendering speed compared to the original NeRF model without incurring high storage costs.
- FastNeRF: High-Fidelity Neural Rendering at 200FPS
    - Repo: https://microsoft.github.io/FastNeRF/
    - Key idea: caching
- Variable Bitrate Neural Fields
    - Key idea: Vector-Quantization






### Parallelization 
- Alpa: Automating Inter- and Intra-Operator Parallelism for Distributed Deep Learning
    - Key idea: enable processing parallelism
    - Result Highlight: Alpa automates model-parallel training of large deep learning  models by generating execution plans that unify data, operator, and pipeline parallelism

- Efficient Large-Scale Language Model Training on GPU Clusters Using Megatron-LM

- PipeDream: Fast and Efficient Pipeline Parallel DNN Training


## Extensions

- Dynamic Neural Radiance Fields for Monocular 4D Facial Avatar Reconstruction

- https://github.com/yenchenlin/awesome-NeRF