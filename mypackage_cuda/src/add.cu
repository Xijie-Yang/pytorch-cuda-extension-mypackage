#include "add.h"

__global__ void add_kernel(const float* __restrict__ a,
                           const float* __restrict__ b, float* __restrict__ out,
                           int n) {
  const int i = blockIdx.x * blockDim.x + threadIdx.x;
  if (i < n) {
    out[i] = a[i] + b[i];
  }
}

void add_cpp(uintptr_t prt_a, uintptr_t prt_b, uintptr_t prt_result, int n) {
  printf("[CPP LOG] Enter add_cpp().\n");

  const float* a = reinterpret_cast<const float*>(prt_a);
  const float* b = reinterpret_cast<const float*>(prt_b);
  float* result = reinterpret_cast<float*>(prt_result);

  // for (int i = 0; i < n; i++) {
  //   result[i] = a[i] + b[i];
  // }

  // Simple launch config
  const int threads = 256;
  const int blocks = (n + threads - 1) / threads;

  cudaStream_t stream = 0;
  add_kernel<<<blocks, threads, 0, stream>>>(a, b, result, n);

  // Optional: surface launch errors immediately
  cudaError_t err = cudaGetLastError();
  if (err != cudaSuccess) {
    fprintf(stderr, "[CUDA ERR] Kernel launch failed: %s\n",
            cudaGetErrorString(err));
    return;
  }

  // Optional: sync here if you need completion before returning.
  // If you prefer async behavior, remove this and let the caller sync on the
  // stream.
  err = cudaStreamSynchronize(stream);
  if (err != cudaSuccess) {
    fprintf(stderr, "[CUDA ERR] Stream sync failed: %s\n",
            cudaGetErrorString(err));
  }
}
