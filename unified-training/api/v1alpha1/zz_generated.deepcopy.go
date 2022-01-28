// +build !ignore_autogenerated

/*


Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
*/

// Code generated by controller-gen. DO NOT EDIT.

package v1alpha1

import (
	runtime "k8s.io/apimachinery/pkg/runtime"
)

// DeepCopyInto is an autogenerated deepcopy function, copying the receiver, writing into out. in must be non-nil.
func (in *UnifiedJob) DeepCopyInto(out *UnifiedJob) {
	*out = *in
	out.TypeMeta = in.TypeMeta
	in.ObjectMeta.DeepCopyInto(&out.ObjectMeta)
	in.Spec.DeepCopyInto(&out.Spec)
	out.Status = in.Status
}

// DeepCopy is an autogenerated deepcopy function, copying the receiver, creating a new UnifiedJob.
func (in *UnifiedJob) DeepCopy() *UnifiedJob {
	if in == nil {
		return nil
	}
	out := new(UnifiedJob)
	in.DeepCopyInto(out)
	return out
}

// DeepCopyObject is an autogenerated deepcopy function, copying the receiver, creating a new runtime.Object.
func (in *UnifiedJob) DeepCopyObject() runtime.Object {
	if c := in.DeepCopy(); c != nil {
		return c
	}
	return nil
}

// DeepCopyInto is an autogenerated deepcopy function, copying the receiver, writing into out. in must be non-nil.
func (in *UnifiedJobList) DeepCopyInto(out *UnifiedJobList) {
	*out = *in
	out.TypeMeta = in.TypeMeta
	in.ListMeta.DeepCopyInto(&out.ListMeta)
	if in.Items != nil {
		in, out := &in.Items, &out.Items
		*out = make([]UnifiedJob, len(*in))
		for i := range *in {
			(*in)[i].DeepCopyInto(&(*out)[i])
		}
	}
}

// DeepCopy is an autogenerated deepcopy function, copying the receiver, creating a new UnifiedJobList.
func (in *UnifiedJobList) DeepCopy() *UnifiedJobList {
	if in == nil {
		return nil
	}
	out := new(UnifiedJobList)
	in.DeepCopyInto(out)
	return out
}

// DeepCopyObject is an autogenerated deepcopy function, copying the receiver, creating a new runtime.Object.
func (in *UnifiedJobList) DeepCopyObject() runtime.Object {
	if c := in.DeepCopy(); c != nil {
		return c
	}
	return nil
}

// DeepCopyInto is an autogenerated deepcopy function, copying the receiver, writing into out. in must be non-nil.
func (in *UnifiedJobReplicaSpec) DeepCopyInto(out *UnifiedJobReplicaSpec) {
	*out = *in
	if in.TargetReplicas != nil {
		in, out := &in.TargetReplicas, &out.TargetReplicas
		*out = make(map[string]int64, len(*in))
		for key, val := range *in {
			(*out)[key] = val
		}
	}
	if in.MinReplicas != nil {
		in, out := &in.MinReplicas, &out.MinReplicas
		*out = new(int64)
		**out = **in
	}
	if in.MaxReplicas != nil {
		in, out := &in.MaxReplicas, &out.MaxReplicas
		*out = new(int64)
		**out = **in
	}
}

// DeepCopy is an autogenerated deepcopy function, copying the receiver, creating a new UnifiedJobReplicaSpec.
func (in *UnifiedJobReplicaSpec) DeepCopy() *UnifiedJobReplicaSpec {
	if in == nil {
		return nil
	}
	out := new(UnifiedJobReplicaSpec)
	in.DeepCopyInto(out)
	return out
}

// DeepCopyInto is an autogenerated deepcopy function, copying the receiver, writing into out. in must be non-nil.
func (in *UnifiedJobSpec) DeepCopyInto(out *UnifiedJobSpec) {
	*out = *in
	in.ReplicaSpec.DeepCopyInto(&out.ReplicaSpec)
	in.JobSpec.DeepCopyInto(&out.JobSpec)
}

// DeepCopy is an autogenerated deepcopy function, copying the receiver, creating a new UnifiedJobSpec.
func (in *UnifiedJobSpec) DeepCopy() *UnifiedJobSpec {
	if in == nil {
		return nil
	}
	out := new(UnifiedJobSpec)
	in.DeepCopyInto(out)
	return out
}

// DeepCopyInto is an autogenerated deepcopy function, copying the receiver, writing into out. in must be non-nil.
func (in *UnifiedJobStatus) DeepCopyInto(out *UnifiedJobStatus) {
	*out = *in
}

// DeepCopy is an autogenerated deepcopy function, copying the receiver, creating a new UnifiedJobStatus.
func (in *UnifiedJobStatus) DeepCopy() *UnifiedJobStatus {
	if in == nil {
		return nil
	}
	out := new(UnifiedJobStatus)
	in.DeepCopyInto(out)
	return out
}

// DeepCopyInto is an autogenerated deepcopy function, copying the receiver, writing into out. in must be non-nil.
func (in *UnifiedJobWorkersSpec) DeepCopyInto(out *UnifiedJobWorkersSpec) {
	*out = *in
	if in.UnifiedArgs != nil {
		in, out := &in.UnifiedArgs, &out.UnifiedArgs
		*out = make([]string, len(*in))
		copy(*out, *in)
	}
}

// DeepCopy is an autogenerated deepcopy function, copying the receiver, creating a new UnifiedJobWorkersSpec.
func (in *UnifiedJobWorkersSpec) DeepCopy() *UnifiedJobWorkersSpec {
	if in == nil {
		return nil
	}
	out := new(UnifiedJobWorkersSpec)
	in.DeepCopyInto(out)
	return out
}