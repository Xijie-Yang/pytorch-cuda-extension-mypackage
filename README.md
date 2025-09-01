# A Minimal Example Running C++ Functions from Python Through torch.utils.cpp_extension

## Create Environment

```sh
conda create -y -n 250830-pytorch-cuda python=3.11
conda activate 250830-pytorch-cuda
```

## Install PyTorch 2.7.1 (cu118)

```sh
# https://pytorch.org/get-started/previous-versions/
# pytorch cu version should match the nvcc version on the machine
pip install torch==2.7.1 torchvision==0.22.1 --index-url https://download.pytorch.org/whl/cu118
```

## Install This Package

```sh
pip install ninja
pip install . -v --no-build-isolation
# or first run
# rm -rf build
```

## Use This Package

```sh
python main.py
```

## Speed Analysis

```
---- n=1000000 ----
[LOG] n=1000000 add_cpu_pytorch(): 0.002204 s
[C LOG] Enter add_cpp().
[LOG] n=1000000 mypackage_python.add_cpu_cpp(): 0.001387 s
[LOG] n=1000000 add_gpu_pytorch(): 0.010462 s
[C LOG] Enter add_cuda().
[LOG] n=1000000 mypackage_python.add_gpu_cuda(): 0.001738 s

---- n=10000000 ----
[LOG] n=10000000 add_cpu_pytorch(): 0.006083 s
[C LOG] Enter add_cpp().
[LOG] n=10000000 mypackage_python.add_cpu_cpp(): 0.010207 s
[LOG] n=10000000 add_gpu_pytorch(): 0.002807 s
[C LOG] Enter add_cuda().
[LOG] n=10000000 mypackage_python.add_gpu_cuda(): 0.000259 s

---- n=100000000 ----
[LOG] n=100000000 add_cpu_pytorch(): 0.018145 s
[C LOG] Enter add_cpp().
[LOG] n=100000000 mypackage_python.add_cpu_cpp(): 0.112159 s
[LOG] n=100000000 add_gpu_pytorch(): 0.025093 s
[C LOG] Enter add_cuda().
[LOG] n=100000000 mypackage_python.add_gpu_cuda(): 0.002878 s

---- n=1000000000 ----
[LOG] n=1000000000 add_cpu_pytorch(): 0.611425 s
[C LOG] Enter add_cpp().
[LOG] n=1000000000 mypackage_python.add_cpu_cpp(): 1.358379 s
[LOG] n=1000000000 add_gpu_pytorch(): 0.231321 s
[C LOG] Enter add_cuda().
[LOG] n=1000000000 mypackage_python.add_gpu_cuda(): 0.029303 s
```

## References

- https://docs.pytorch.org/tutorials/advanced/cpp_extension.html
