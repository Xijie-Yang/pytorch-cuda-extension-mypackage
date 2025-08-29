import mypackage_cpp

import torch


# This file is a Python wrapper of the C++ package, for IntelliSense.


def add(a: torch.Tensor, b: torch.Tensor) -> torch.Tensor:
    """
    add two tensors and return their sum
    """

    assert a.ndim == 1 and b.ndim == 1
    assert a.shape == b.shape
    assert a.dtype == torch.float and b.dtype == torch.float

    n = a.shape[0]

    # `torch.Tensor.contiguous()`: https://docs.pytorch.org/docs/stable/generated/torch.Tensor.contiguous.html
    # `torch.Tensor.data_ptr()`: https://docs.pytorch.org/docs/stable/generated/torch.Tensor.data_ptr.html

    result = torch.zeros_like(a).contiguous()

    mypackage_cpp.add_cpp(
        a.contiguous().data_ptr(),
        b.contiguous().data_ptr(),
        result.data_ptr(),
        n,
    )

    return result
