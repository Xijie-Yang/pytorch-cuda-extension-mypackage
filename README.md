# A Minimal Example Running C++ Functions from Python Through torch.utils.cpp_extension

## Create Environment

```sh
conda create -y -n 250829-pytorch-cuda python=3.11
conda activate 250829-pytorch-cuda
```

## Install pytorch 2.7.1 + cudatoolkit 11.8

```sh
# https://pytorch.org/get-started/previous-versions/
# pytorch cu version should match the nvcc version on the machine
pip install torch==2.7.1 torchvision==0.22.1 --index-url https://download.pytorch.org/whl/cu118
```

## Install This Package

```sh
pip install .
# or
# rm -rf build; pip install .
```

## Use This Package

```sh
python main.py
```

## References

- https://docs.pytorch.org/tutorials/advanced/cpp_extension.html
