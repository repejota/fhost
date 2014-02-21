#
## BEGIN LICENSE BLOCK
#
# Copyright (c) <2012-2014>, Raul Perez <repejota@gmail.com>
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#     * Redistributions of source code must retain the above copyright
#       notice, this list of conditions and the following disclaimer.
#     * Redistributions in binary form must reproduce the above copyright
#       notice, this list of conditions and the following disclaimer in the
#       documentation and/or other materials provided with the distribution.
#     * Neither the name of the <organization> nor the
#       names of its contributors may be used to endorse or promote products
#       derived from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED. IN NO EVENT SHALL <COPYRIGHT HOLDER> BE LIABLE FOR ANY
# DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
# (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
# ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
# SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#
## END LICENSE BLOCK
#

from setuptools import setup, find_packages

PROJECT = "fhost"

with open('README.rst') as f:
    README = f.read()

with open('LICENSE') as f:
    LICENSE = f.read()

with open('VERSION') as f:
    VERSION = f.read()

setup(
    name=PROJECT,
    version=VERSION,
    description="""A Python module that allows you to create,
                   list, and modify local hosts file entries.""",
    long_description=README,
    author='Raul Perez',
    author_email='repejota@gmail.com',
    url='http://repejota.github.com/fhost',
    download_url='http://repejota.github.com/fhost/install',
    license=LICENSE,
    packages=find_packages(exclude=('tests', 'docs')),
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: End Users/Desktop',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
    ],
    entry_points={
        'console_scripts': [
            'fhost = fhost.cli:application.cmdline'
        ]
    },
    platforms=['Any'],
    scripts=[],
    provides=['fhost'],
    install_requires=['subcmd'],
    namespace_packages=[],
    zip_safe=False,
)
