#ifndef ADD_H
#define ADD_H

#include <cstdint>
#include <cstdio>

#include <cuda_runtime.h>

void add_cpp(uintptr_t prt_a, uintptr_t prt_b, uintptr_t prt_result, int n);

#endif  // ADD_H
