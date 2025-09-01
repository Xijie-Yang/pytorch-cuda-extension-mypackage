#include "add_gpu.h"

__global__ void add_kernel(const float* __restrict__ a,
                           const float* __restrict__ b, float* __restrict__ out,
                           int n) {
  const int i = blockIdx.x * blockDim.x + threadIdx.x;
  if (i < n) {
    out[i] = a[i] + b[i];
  }
}

void add_cuda(uintptr_t prt_a, uintptr_t prt_b, uintptr_t prt_result, int n) {
  printf("[C LOG] Enter add_cuda().\n");

  const float* a = reinterpret_cast<const float*>(prt_a);
  const float* b = reinterpret_cast<const float*>(prt_b);
  float* result = reinterpret_cast<float*>(prt_result);

  // Simple launch config
  const int threads = 256;
  const int blocks = (n + threads - 1) / threads;

  add_kernel<<<blocks, threads>>>(a, b, result, n);

  // Wait for GPU to finish before accessing on host
  cudaDeviceSynchronize();
}
