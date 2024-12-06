## Popular tools
1. kubeBuilder
2. operator SDK

## Controller Key Ideas
**Reconcile**: bring current states to desire states. 

**Conflict**: when multiple actors update one resource, based on resource version, if reconcile fails, requeue and update again. 

## Steps with operator SDK
*  Install / Upgrade golang to > 1.17.5:
```
Download:
curl -OL https://go.dev/dl/go1.19.2.linux-amd64.tar.gz  # OR go to parent page, get whatever is latest version
Install:
sudo tar -C /usr/local -xvf go1.19.2.linux-amd64.tar.gz
```
* Install [operator sdk](https://sdk.operatorframework.io/docs/installation/)
*  ```mkdir alnair-pod && cd alnair-pod```
* ```operator-sdk init --domain=centaurusinfra.io --repo=alnair-pod``` 

   repo (module root path) can be a github link e.g., ```--repo=github.com/CentaurusInfra/alnair/alnair-pod```

* ``` operator-sdk create api --group alnair --version=v1alpha1 --kind=AlnairPod --controller=true --resource=true```. Auto generated files and folders are as below.
```
.
├── api/
│   └── v1alpha1/
│       ├── alnairpod_types.go
│       ├── groupversion_info.go
│       └── zz_generated.deepcopy.go
├── bin/
│   └── controller-gen*
├── config/
│   ├── crd/
│   │   ├── kustomization.yaml
│   │   ├── kustomizeconfig.yaml
│   │   └── patches/
│   │       ├── cainjection_in_alnairpods.yaml
│   │       └── webhook_in_alnairpods.yaml
│   ├── default/
│   │   ├── kustomization.yaml
│   │   ├── manager_auth_proxy_patch.yaml
│   │   └── manager_config_patch.yaml
│   ├── manager/
│   │   ├── controller_manager_config.yaml
│   │   ├── kustomization.yaml
│   │   └── manager.yaml
│   ├── manifests/
│   │   └── kustomization.yaml
│   ├── prometheus/
│   │   ├── kustomization.yaml
│   │   └── monitor.yaml
│   ├── rbac/
│   │   ├── alnairpod_editor_role.yaml
│   │   ├── alnairpod_viewer_role.yaml
│   │   ├── auth_proxy_client_clusterrole.yaml
│   │   ├── auth_proxy_role_binding.yaml
│   │   ├── auth_proxy_role.yaml
│   │   ├── auth_proxy_service.yaml
│   │   ├── kustomization.yaml
│   │   ├── leader_election_role_binding.yaml
│   │   ├── leader_election_role.yaml
│   │   ├── role_binding.yaml
│   │   └── service_account.yaml
│   ├── samples/
│   │   ├── alnair_v1alpha1_alnairpod.yaml
│   │   └── kustomization.yaml
│   └── scorecard/
│       ├── bases/
│       │   └── config.yaml
│       ├── kustomization.yaml
│       └── patches/
│           ├── basic.config.yaml
│           └── olm.config.yaml
├── controllers/
│   ├── alnairpod_controller.go
│   └── suite_test.go
├── Dockerfile
├── go.mod
├── go.sum
├── hack/
│   └── boilerplate.go.txt
├── main.go
├── Makefile
├── PROJECT
└── README.md

```
4. Design the spec and status for the custom resource in ```api/v1alpha1/alnairpod_types.go```. In the spec, every key needs to be explicitly defined in a struct. A nested struct is a typical way to describe a complex resource. Often time, we can reuse structs already defined in k8s coreV1 API. For example,
   ```
   type AlnairPodSpec struct {
       Containers []corev1.Container `json:"containers" patchStrategy:"merge" patchMergeKey:"name" protobuf:"bytes,2,rep,name=containers"`
       Volumes []corev1.Volume `json:"volumes,omitempty"`
   }
   ```
   
   Refer to Kubernetes [PodSpec](https://github.com/kubernetes/api/blob/master/core/v1/types.go#L3068).

   **Important: Run "make" to regenerate code after modifying alnairpod_types.go** This file ```api/v1alpha1/zz_generated.deepcopy.go``` will regenerated based on the new spec of custom resources.

5. Fill up the controller logic in controller/alnairpod_controller.go. Refer to [an example](https://kubernetes.io/blog/2021/06/21/writing-a-controller-for-pod-labels/) on Reconcile and SetupWithManager functions. The ```Reconcile``` method is called whenever the AlnairPod is created, updated, or deleted. The ```SetupWithManager``` method is called when the operator starts. It serves to tell the operator framework what types our reconciler needs to watch.

6. Reconcile template includes get the resource under watch, ignore the delete event, implement the create/update logic. When update status, use subresource r.status.update(), instead of r.update(). Otherwise trigger the infinite loops.

7. SetupWithManager, set the owner for the underlining pod. You can also filter events with predicate, so the reconcile logic won't be triggered by unrelated events. Also the cache can be specified so only certain pods (selected by label) are cached not all.

## Reference
1. [Example: pod label controller](https://kubernetes.io/blog/2021/06/21/writing-a-controller-for-pod-labels/)
2. [10 things to know before writing controller](https://medium.com/@gallettilance/10-things-you-should-know-before-writing-a-kubernetes-controller-83de8f86d659)
3. [k8s operators best practices](https://cloud.redhat.com/blog/kubernetes-operators-best-practices)
4. [Kubernetes API convention](https://github.com/kubernetes/community/blob/master/contributors/devel/sig-architecture/api-conventions.md#typical-status-properties)
5. [Operator Hub.io](https://operatorhub.io/?category=AI%2FMachine+Learning)

