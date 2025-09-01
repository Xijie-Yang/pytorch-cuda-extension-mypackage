import time

import torch

import mypackage_python

# ---


def add_cpu_python(a: torch.Tensor, b: torch.Tensor, result: torch.Tensor, n: int):
    for i in range(n):
        result[i] = a[i] + b[i]


def add_cpu_pytorch(a: torch.Tensor, b: torch.Tensor) -> torch.Tensor:
    return a + b


def add_gpu_pytorch(a: torch.Tensor, b: torch.Tensor) -> torch.Tensor:
    return a + b


# ---

for n in [
    1_000_000,
    10_000_000,
    100_000_000,
    1_000_000_000,
]:
    print()
    print(f"---- {n=} ----")

    if False:
        a = torch.rand((n,), dtype=torch.float, device="cpu")
        b = torch.rand((n,), dtype=torch.float, device="cpu")
        result = torch.zeros((n,), dtype=torch.float, device="cpu")

        start = time.perf_counter()
        add_cpu_python(a, b, result, n)
        end = time.perf_counter()
        assert (result - (a + b)).mean() < 1e-8
        print(f"[LOG] {n=} add_cpu_python(): {end-start:.6f} s")

    if True:
        a = torch.rand((n,), dtype=torch.float, device="cpu")
        b = torch.rand((n,), dtype=torch.float, device="cpu")

        start = time.perf_counter()
        result = add_cpu_pytorch(a, b)
        end = time.perf_counter()
        assert (result - (a + b)).mean() < 1e-8
        print(f"[LOG] {n=} add_cpu_pytorch(): {end-start:.6f} s")

    if True:
        a = torch.rand((n,), dtype=torch.float, device="cpu")
        b = torch.rand((n,), dtype=torch.float, device="cpu")

        start = time.perf_counter()
        result = mypackage_python.add_cpu_cpp(a, b)
        end = time.perf_counter()
        assert (result - (a + b)).mean() < 1e-8
        print(f"[LOG] {n=} mypackage_python.add_cpu_cpp(): {end-start:.6f} s")

    # ----

    if True:
        a = torch.rand((n,), dtype=torch.float, device="cuda")
        b = torch.rand((n,), dtype=torch.float, device="cuda")

        start = time.perf_counter()
        result = add_gpu_pytorch(a, b)
        end = time.perf_counter()
        assert (result - (a + b)).mean() < 1e-8
        print(f"[LOG] {n=} add_gpu_pytorch(): {end-start:.6f} s")

    if True:
        a = torch.rand((n,), dtype=torch.float, device="cuda")
        b = torch.rand((n,), dtype=torch.float, device="cuda")

        start = time.perf_counter()
        result = mypackage_python.add_gpu_cuda(a, b)
        end = time.perf_counter()
        assert (result - (a + b)).mean() < 1e-8
        print(f"[LOG] {n=} mypackage_python.add_gpu_cuda(): {end-start:.6f} s")
