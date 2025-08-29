# https://setuptools.pypa.io/en/latest/userguide/quickstart.html
import setuptools

# https://docs.pytorch.org/tutorials/advanced/cpp_extension.html
import torch.utils.cpp_extension


# https://setuptools.pypa.io/en/latest/references/keywords.html
setuptools.setup(
    # A string specifying the name of the package.
    name="mypackage",
    # A string specifying the version number of the package.
    version="0.0.1",
    # A list of strings specifying the packages that setuptools will manipulate.
    packages=["mypackage_python"],
    # https://setuptools.pypa.io/en/stable/userguide/ext_modules.html
    ext_modules=[
        # https://docs.pytorch.org/docs/stable/cpp_extension.html
        torch.utils.cpp_extension.CUDAExtension(
            name="mypackage_cpp",
            sources=["mypackage_cpp/ext.cpp", "mypackage_cpp/src/add.cpp"],
        )
    ],
    # https://docs.pytorch.org/tutorials/advanced/cpp_extension.html
    # `BuildExtension` is neccessary for pytorch to pass `TORCH_EXTENSION_NAME` into ext.cpp
    cmdclass={"build_ext": torch.utils.cpp_extension.BuildExtension},
)
