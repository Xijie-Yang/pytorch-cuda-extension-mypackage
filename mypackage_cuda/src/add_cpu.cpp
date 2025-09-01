#include "add_cpu.h"

void add_cpp(uintptr_t prt_a, uintptr_t prt_b, uintptr_t prt_result, int n) {
  printf("[C LOG] Enter add_cpp().\n");

  const float* a = reinterpret_cast<const float*>(prt_a);
  const float* b = reinterpret_cast<const float*>(prt_b);
  float* result = reinterpret_cast<float*>(prt_result);

  for (int i = 0; i < n; i++) {
    result[i] = a[i] + b[i];
  }
}
