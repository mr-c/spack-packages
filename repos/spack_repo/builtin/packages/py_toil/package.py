# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

# ----------------------------------------------------------------------------
# If you submit this package back to Spack as a pull request,
# please first remove this boilerplate and all FIXME comments.
#
# This is a template package file for Spack.  We've put "FIXME"
# next to all the things you'll want to change. Once you've handled
# them, you can save this file and test your package like this:
#
#     spack install py-toil
#
# You can edit this file again by typing:
#
#     spack edit py-toil
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyToil(PythonPackage):
    """Pipeline management software for clusters."""

    homepage = "https://github.com/DataBiosphere/toil"
    pypi = "toil/toil-9.5.0.tar.gz"

    # FIXME: Uncomment and add the upstream supplier (organization or author).
    # If unknown or inapplicable, remove this entire block.
    # supplier = organization_or_author

    maintainers("mr-c")
    license("Apache-2.0", checked_by="mr-c")

    version("9.5.0", sha256="dae9a12b0f277355170129be38406c831da47054758e64d6693e18d7e5b45d3f")

    # FIXME: Only add the python/pip/wheel dependencies if you need specific versions
    # or need to change the dependency type. Generic python/pip/wheel dependencies are
    # added implicitly by the PythonPackage base class.
    # depends_on("python@2.X:2.Y,3.Z:", type=("build", "run"))
    # depends_on("py-pip@X.Y:", type="build")
    # depends_on("py-wheel@X.Y:", type="build")

    with default_args(type="build"):
         depends_on("py-setuptools@64:")
         depends_on("py-setuptools-scm@8:")

    # FIXME: Add additional dependencies if required.
    # with default_args(type=("build", "run")):
    #     depends_on("py-foo")

    def config_settings(self, spec, prefix):
        # FIXME: Add configuration settings to be passed to the build backend
        # FIXME: If not needed, delete this function
        settings = {}
        return settings
