##############################################################################
# Copyright (c) 2013-2018, Lawrence Livermore National Security, LLC.
# Produced at the Lawrence Livermore National Laboratory.
#
# This file is part of Spack.
# Created by Todd Gamblin, tgamblin@llnl.gov, All rights reserved.
# LLNL-CODE-647188
#
# For details, see https://github.com/spack/spack
# Please also see the NOTICE and LICENSE files for our notice and the LGPL.
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License (as
# published by the Free Software Foundation) version 2.1, February 1999.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the IMPLIED WARRANTY OF
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the terms and
# conditions of the GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307 USA
##############################################################################
from spack import *


class XercesC(AutotoolsPackage):
    """Xerces-C++ is a validating XML parser written in a portable subset of
    C++. Xerces-C++ makes it easy to give your application the ability to read
    and write XML data. A shared library is provided for parsing, generating,
    manipulating, and validating XML documents using the DOM, SAX, and SAX2
    APIs."""

    homepage = "https://xerces.apache.org/xerces-c"
    url      = "https://archive.apache.org/dist/xerces/c/3/sources/xerces-c-3.2.1.tar.bz2"

    version('3.2.1', '8f98a81a3589bbc2dad9837452f7d319')
    version('3.1.4', 'd04ae9d8b2dee2157c6db95fa908abfd')

    variant('pic', default=True,
            description='Produce position-independent code (for shared libs)')
    variant('static', default=True,
            description='Enables the build of static libraries.')
    variant('shared', default=True,
            description='Enables the build of shared libraries.')

    depends_on('libiconv')

    def setup_environment(self, spack_env, run_env):
        spack_env.append_flags('LDFLAGS', self.spec['libiconv'].libs.ld_flags)
        if '+pic' in self.spec:
            spack_env.append_flags('CFLAGS', self.compiler.pic_flag)

    def configure_args(self):
        args = ['--disable-network']
        if not '+shared' in self.spec:
            args += ['--disable-shared', '--enable-static']
        elif '+static' in self.spec:
            args += ['--enable-static']
        return args


