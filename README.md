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
# only for RTX 4090, check https://developer.nvidia.com/cuda-gpus
TORCH_CUDA_ARCH_LIST=8.9 pip install . -v --no-build-isolation
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
[LOG] n=1000000 add_cpu_pytorch(): 0.002833 s
[C LOG] Enter add_cpp().
[LOG] n=1000000 mypackage_python.add_cpu_cpp(): 0.001371 s
[LOG] n=1000000 add_gpu_pytorch(): 0.009897 s
[C LOG] Enter add_cuda().
[LOG] n=1000000 mypackage_python.add_gpu_cuda(): 0.001682 s

---- n=10000000 ----
[LOG] n=10000000 add_cpu_pytorch(): 0.005089 s
[C LOG] Enter add_cpp().
[LOG] n=10000000 mypackage_python.add_cpu_cpp(): 0.010221 s
[LOG] n=10000000 add_gpu_pytorch(): 0.002089 s
[C LOG] Enter add_cuda().
[LOG] n=10000000 mypackage_python.add_gpu_cuda(): 0.000258 s

---- n=100000000 ----
[LOG] n=100000000 add_cpu_pytorch(): 0.017594 s
[C LOG] Enter add_cpp().
[LOG] n=100000000 mypackage_python.add_cpu_cpp(): 0.096648 s
[LOG] n=100000000 add_gpu_pytorch(): 0.016231 s
[C LOG] Enter add_cuda().
[LOG] n=100000000 mypackage_python.add_gpu_cuda(): 0.002885 s

---- n=1000000000 ----
[LOG] n=1000000000 add_cpu_pytorch(): 0.322058 s
[C LOG] Enter add_cpp().
[LOG] n=1000000000 mypackage_python.add_cpu_cpp(): 1.050182 s
[LOG] n=1000000000 add_gpu_pytorch(): 0.144807 s
[C LOG] Enter add_cuda().
[LOG] n=1000000000 mypackage_python.add_gpu_cuda(): 0.029351 s
```

## References

- https://docs.pytorch.org/tutorials/advanced/cpp_extension.html
