import torch

import mypackage_python

n = 100

a = torch.rand((n,), dtype=torch.float, device="cuda")
b = torch.rand((n,), dtype=torch.float, device="cuda")

result = mypackage_python.add(a, b)

print(f"{a=}")
print(f"{b=}")
print(f"{result=}")
print(f"{(result-(a+b)).mean()=}")
