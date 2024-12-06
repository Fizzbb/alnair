## Basic Steps

### 1. Install Golang (version 1.18.6)
```
curl -LO https://go.dev/dl/go1.18.6.linux-amd64.tar.gz
tar -C /usr/local -xzf go1.18.6.linux-amd64.tar.gz
```
Add the following Go environment to ```.bashrc``` and ```source .bashrc``` to apply
```
export GOROOT=/usr/local/go
export GOPATH=$HOME/go
export PATH=$GOPATH/bin:$GOROOT/bin:$PATH
```
### 2. Pick a module name and create the folder by its name
E.g., module name alnair-profiler, ```mkdir alnair-profiler```
### 3. Create the module
Create a go module [reference](https://go.dev/doc/tutorial/create-module).
```
cd alnair-profiler
go mod init alnair-profiler
```
### 4. Sample Directory Structure
Create sub-folder pkg for package source code, which can be sorted into multiple packages

Import external package, use ```go mod tidy``` automatically download the package and update the go.mod and go.sum file

Create sub-folder cmd to call the package as the main entry, [reference](https://go.dev/doc/tutorial/call-module-code)

In this way, package and cmd can be easily extended. 
```
alnair-profiler/
---pkg/
   ---profiler/
      server.go
---cmd/
   ---profiler/
      main.go
---go.mod
---go.sum
```
server.go example 
```
package profiler

import log

func SayHi(){
    log.Println("Hi")
}
```
main.go example
```
package main
import (
    "alnair-profiler/pkg/profiler"
)

func main() {
    profiler.SayHi()
}
```
To run the program ```go run cmd/profiler/main.go```. **Complete example module go can be found [here](https://github.com/Fizzbb/GoModuleExample)**

### 5. Use VScode as IDE, SSH to a remote server
Install **Go Nightly** extension to enable rich language support, e.g., auto list methods of structs, check unused library, etc.

### 6. Kubernetes client-go example

* Connect to the cluster 1: [in-cluster client configuration](https://github.com/kubernetes/client-go/blob/v0.25.1/examples/in-cluster-client-configuration/main.go)
* Connect to the cluster 2: [out-of-cluster client configuration](https://github.com/kubernetes/client-go/blob/v0.25.1/examples/out-of-cluster-client-configuration/main.go), download the kubeconfig file and provide absolute path to the file.


## Golang Conventions
1. Callable functions outside the package starts with Capital letters. Functions started with small letters are not callable outside package. 
