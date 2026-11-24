# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PySchemaSalad(PythonPackage):
    """Schema Annotations for Linked Avro Data (SALAD)"""

    homepage = "https://github.com/common-workflow-language/schema_salad"
    pypi = "schema-salad/schema_salad-8.7.20241021092521.tar.gz"

    license("Apache-2.0")
    version(
        "8.10.20261106141337",
        sha256="cf13b3dafce841c8426899f204ef033c8270148bce3d4e181c44182c35605e7c",
    )
    with default_args(deprecated=True):
        # https://github.com/lepture/mistune/security
        version(
            "8.10.20260825112551",
            sha256="426af8bae86b1b8026469968bcd0802e6c61fd6c44c6b1f77d48467164a6ac74",
        )
        version(
            "8.9.20260417192335",
            sha256="5ad4599231dcf7ae8ae2fc841a677db9c120544b36a6d6347ae87875b2c1b083",
        )
        version(
            "8.8.20250205075315",
            sha256="444a45509fb048347e0ec205b2af6390f0bb145f7183716ba6af2f75a22b8bdd",
        )
        version(
            "8.7.20241021092521",
            sha256="287b27adff70e55dd715bfbea18bb1a58fd73de14b4273be4038559308089cdf",
        )
        version(
            "8.3.20221209165047",
            sha256="d97cc9a4d7c4255eb8000bcebaa8ac0d1d31801c921fd4113ab3051c1e326c7c",
        )

    depends_on("python@3.6:", type=("build", "run"))
    depends_on("python@3.8:", when="@8.4.20230927144413:", type=("build", "run"))
    depends_on("python@3.9:", when="@8.7.20241021092521:", type=("build", "run"))
    depends_on("python@3.10:", when="@8.9.20260327095315:", type=("build", "run"))

    with default_args(type="build"):
        depends_on("py-hatchling", when="@8.10.20261106141337:")
        depends_on("py-hatch-vcs", when="@8.10.20261106141337:")
        depends_on("py-hatch-mypyc", when="@8.10.20261106141337:")
        depends_on("py-setuptools@45:", when="@:8.10.20260825112551")
        depends_on("py-setuptools@50:", when="@8.4.20231117150958:8.10.20260825112551")
        depends_on("py-setuptools-scm@6.2:+toml", when="@:8.10.20260825112551")
        depends_on("py-setuptools-scm@8.0.4:8+toml", when="@8.4.20231024070348:8.8")
        depends_on("py-setuptools-scm@8.0.4:10+toml", when="@8.9.20260417192335:8.10.20260825112551")
        depends_on("py-mypy@0.961", when="@8.3.20220717184004:8.3.20221028160159")
        depends_on("py-mypy@0.991", when="@8.3.20221209165047:8.4.20230201194352")
        depends_on("py-mypy@1.12.1", when="@8.7.20241021092521")
        depends_on("py-mypy@1.15.0", when="@8.8.20250205075315")
        depends_on("py-mypy@1.20.1", when="@8.9.20260417192335")
        depends_on("py-mypy@2.3.1", when="@8.8.10.20260825112551")
        depends_on("py-mypy@2.4.1", when="@8.10.20261106141337:")
        depends_on("py-black@19.10b0:")
        depends_on(
            "py-black@19.10b0:24.10", when="@8.7.20241021092521:8.8.20250205075315"
        )
        depends_on("py-black@19.10b0:26.3", when="@:8.9.20260417192335")
        depends_on("py-black@19.10b0:26.4", when="@8.10.20260825112551:")
        depends_on("py-types-pkg-resources", when="@:8.4.20231117150958")
        depends_on("py-types-requests")
        depends_on("py-types-dataclasses")
        depends_on("py-types-setuptools")
        depends_on("py-rich-argparse", when="@8.9.20260417192335:")

    with default_args(type=("build", "run")):
        depends_on("py-requests@1:")
        depends_on("py-ruamel-yaml@0.17.6:0.17.21", when="@8.3.20221209165047")
        depends_on(
            "py-ruamel-yaml@0.17.6:0.18",
            when="@8.4.20231113094720:8.8.20250205075315",
        )
        depends_on("py-ruamel-yaml@0.17.6:0.19", when="@8.9.20260327095315:")
        depends_on("py-rdflib@4.2.2:6", when="@8.3.20221209165047")
        depends_on("py-rdflib@4.2.2:7", when="@8.4.20230927144413:")
        depends_on("py-mistune@2.0.3:2.0", when="@8.3.20221209165047")
        depends_on(
            "py-mistune@3:3.1", when="@8.7.20241021092521:8.8.20250205075315"
        )
        depends_on("py-mistune@3:3.2", when="@8.9.20260417192335")
        depends_on("py-mistune@3.3:3.3", when="@8.10.20260825112551")
        depends_on("py-mistune@3.4:3.4", when="@8.10.20261106141337:")
        depends_on(
            "py-cachecontrol@0.11.7:0.12+filecache", when="@:8.7.20240718183047"
        )
        depends_on(
            "py-cachecontrol@0.13.1:0.14+filecache",
            when="@8.7.20240820070935:8.7.20241021092521",
        )
        depends_on(
            "py-cachecontrol@0.14+filecache", when="@8.8.20241204110045:"
        )
    def url_for_version(self, version):
        url = "https://files.pythonhosted.org/packages/source/s/{0}/{0}-{1}.tar.gz"
        if version >= Version("8.5.20240503091721"):
            name = "schema_salad"
        else:
            name = "schema-salad"
        return url.format(name, version)
