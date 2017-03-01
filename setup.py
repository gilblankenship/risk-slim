#! /usr/bin/env python
#
# Copyright (C) 2017 Berk Ustun

import os
import sys
from setuptools import setup, find_packages
from setuptools.extension import Extension

DISTNAME = 'riskslim'
DESCRIPTION = "optimized risk scores on large-scale datasets"
AUTHOR = 'Berk Ustun'
AUTHOR_EMAIL = 'ustunb@mit.edu'
URL = 'https://github.com/ustunb/risk-slim'
LICENSE = 'new BSD'
DOWNLOAD_URL = 'https://github.com/ustunb/risk-slim'
VERSION = '0.0.0'

#read requirements as listed in txt file
with open('requirements.txt') as f:
    INSTALL_REQUIRES = [l.strip() for l in f.readlines() if l]

try:
    import numpy
except ImportError:
    print('numpy is required during installation')
    sys.exit(1)

try:
    import scipy
except ImportError:
    print('scipy is required during installation')
    sys.exit(1)

try:
    from Cython.Build import cythonize
except ImportError:
    print('Cython is required during installation')
    sys.exit(1)

#fast log loss
extensions =[
    Extension(
        DISTNAME + ".loss_functions." + "fast_log_loss",
        [DISTNAME + "/loss_functions/fast_log_loss.pyx"],
        include_dirs=[numpy.get_include(), scipy.get_include()],
        libraries=["m"],
        extra_compile_args=["-ffast-math"]
    ),
    Extension(
        DISTNAME + ".loss_functions." + "lookup_log_loss",
        [DISTNAME + "/loss_functions/lookup_log_loss.pyx"],
        include_dirs=[numpy.get_include(), scipy.get_include()],
        libraries=["m"],
        extra_compile_args = ["-ffast-math"])
]


if __name__ == "__main__":

    old_path = os.getcwd()
    local_path = os.path.dirname(os.path.abspath(sys.argv[0]))

    os.chdir(local_path)
    sys.path.insert(0, local_path)

    setup(
        name=DISTNAME,
        packages=find_packages(),
        ext_modules=cythonize(extensions),
        author=AUTHOR,
        author_email=AUTHOR_EMAIL,
        description=DESCRIPTION,
        install_requires=INSTALL_REQUIRES,
        license=LICENSE,
        url=URL,
        version=VERSION,
        download_url=DOWNLOAD_URL,
        zip_safe=False,
    )
