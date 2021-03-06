# Copyright 2013-2018 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class Isl(AutotoolsPackage):
    """isl (Integer Set Library) is a thread-safe C library for manipulating
    sets and relations of integer points bounded by affine constraints."""

    homepage = "http://isl.gforge.inria.fr"
    url      = "http://isl.gforge.inria.fr/isl-0.19.tar.bz2"

    version('0.19', sha256='d59726f34f7852a081fbd3defd1ab2136f174110fc2e0c8d10bb122173fa9ed8')
    version('0.18', sha256='6b8b0fd7f81d0a957beb3679c81bbb34ccc7568d5682844d8924424a0dadcb1b')
    version('0.15', sha256='8ceebbf4d9a81afa2b4449113cee4b7cb14a687d7a549a963deb5e2a41458b6b')
    version('0.14', sha256='7e3c02ff52f8540f6a85534f54158968417fd676001651c8289c705bd0228f36')

    depends_on('gmp')

    def configure_args(self):
        return [
            '--with-gmp-prefix={0}'.format(self.spec['gmp'].prefix)
        ]
