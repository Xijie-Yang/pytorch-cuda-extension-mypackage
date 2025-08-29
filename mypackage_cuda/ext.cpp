#include <torch/extension.h>

#include "src/add.h"

// https://docs.pytorch.org/tutorials/advanced/cpp_extension.html
// The torch extension build will define `TORCH_EXTENSION_NAME` as the name you
// give your extension in the `setup.py` script.
PYBIND11_MODULE(TORCH_EXTENSION_NAME, m) { m.def("add_cpp", &add_cpp); }
