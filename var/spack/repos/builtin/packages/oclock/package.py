# Copyright 2013-2018 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class Oclock(AutotoolsPackage):
    """oclock is a simple analog clock using the SHAPE extension to make
    a round (possibly transparent) window."""

    homepage = "http://cgit.freedesktop.org/xorg/app/oclock"
    url      = "https://www.x.org/archive/individual/app/oclock-1.0.3.tar.gz"

    version('1.0.3', 'f25b05d987ef8ed6dd5a887c82eace62')

    depends_on('libx11')
    depends_on('libxmu')
    depends_on('libxext')
    depends_on('libxt')
    depends_on('libxkbfile')

    depends_on('pkgconfig', type='build')
    depends_on('util-macros', type='build')
