from setuptools import setup, find_packages
from distutils.core import Extension

DISTNAME = 'art-python'
VERSION = '0.0.1'
PACKAGES = ['art']
EXTENSIONS = []
DESCRIPTION = 'Python package'
LONG_DESCRIPTION = open('README.md').read()
AUTHOR = 'ART Developers'
MAINTAINER_EMAIL = 'cbirkjones@gmail.com'
LICENSE = 'MIT'
URL = 'https://github.com/cbirkj/art-python'

setuptools_kwargs = {
    'zip_safe': False,
    'install_requires': ['numpy >= 1.10.4',
                         'pandas >= 0.18.0'],
    'scripts': [],
    'include_package_data': True
}

setup(name=DISTNAME,
      version=VERSION,
      packages=PACKAGES,
      ext_modules=EXTENSIONS,
      description=DESCRIPTION,
      long_description=LONG_DESCRIPTION,
      author=AUTHOR,
      maintainer_email=MAINTAINER_EMAIL,
      license=LICENSE,
      url=URL,
      **setuptools_kwargs)