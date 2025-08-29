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

## References

- https://docs.pytorch.org/tutorials/advanced/cpp_extension.html
