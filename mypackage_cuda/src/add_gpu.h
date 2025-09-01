#ifndef ADD_GPU_H
#define ADD_GPU_H

#include <cuda_runtime.h>

#include <cstdint>
#include <cstdio>

void add_cuda(uintptr_t prt_a, uintptr_t prt_b, uintptr_t prt_result, int n);

#endif
