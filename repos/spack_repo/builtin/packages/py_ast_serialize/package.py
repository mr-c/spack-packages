# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyAstSerialize(PythonPackage):
    """Python bindings for mypy AST serialization."""

    homepage = "https://github.com/mypyc/ast_serialize"
    pypi = "ast_serialize/ast_serialize-0.5.0.tar.gz"

    license("MIT")

    version("0.12.1", sha256="5285a390caf1c44368ae270f037f797b91427d138b7d43cad0f1fda4c83518d9")
    version("0.6.0", sha256="aadd3ffcf4858c9726bf3515f7b199c7eadbe504f96028e4a87172c0da65a8fe")
    version("0.5.0", sha256="5880091bfe6f4f986f22866375c2e884843e7a0b6343ae41aeea659613d879b6")

    depends_on("py-maturin@1.9", type="build")
