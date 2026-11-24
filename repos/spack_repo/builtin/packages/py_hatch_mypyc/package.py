# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyHatchMypyc(PythonPackage):
    """Hatch build hook plugin for Mypyc"""

    homepage = "https://github.com/ofek/hatch-mypyc"
    pypi = "hatch-mypyc/hatch_mypyc-0.16.0.tar.gz"

    license("MIT")

    version("0.16.0", sha256="6e3aa99634d81142cab993358698eaae823de91fe87ee85029a82f2e737c3ded")

    with default_args(type=("build", "run")):
        depends_on("python@3.9:", when="@0.5:")
        depends_on("python@3.7:")
        depends_on("py-hatchling@1.12.2:")
        depends_on("py-mypy@0.971:")
        depends_on("py-pathspec")
        depends_on("py-setuptools")
