#
## BEGIN LICENSE BLOCK
#
# Copyright (c) <2012>, Raul Perez <repejota@gmail.com>
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

TOP=.

GREEN="\033[0;32m"
DARK_GRAY="\033[1;30m"
NOTHING="\033[0m"

CP=cp
RM=rm
MKDIR=mkdir
FIND=find
PYTHON = /usr/bin/env python
TEST = nosetests

PROJECT_NAME = fhost
PROJECT_SHORT_NAME = fhost
VERSION=`cat $(TOP)/VERSION`

SITE_PACKAGES = `python -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())"`

build:
	  @echo $(GREEN)"Building $(PROJECT_NAME) ..."$(NOTHING)
	  @$(PYTHON) setup.py $@

doc:
	  @echo $(GREEN)"Building $(PROJECT_NAME) documentation..."$(NOTHING)
	  @$(MAKE) -C docs html SPHINXOPTS=-Aonline=1

test:
	  @echo $(GREEN)"Running $(PROJECT_NAME) tests..."$(NOTHING)
	  @$(TEST) --quiet --with-coverage --cover-package=$(PROJECT_NAME)

dist: build
	  @echo $(GREEN)"Building distribution $(PROJECT_NAME) packages..."$(NOTHING)
	  @$(PYTHON) setup.py bdist sdist

install: build
	  @echo $(GREEN)"Installing $(PROJECT_NAME) packages..."$(NOTHING)
	  @$(PYTHON) setup.py $@

uninstall:
	  @echo $(GREEN)"Uninstalling $(PROJECT_NAME) packages..."$(NOTHING)

clean:
	  @echo $(GREEN)"Cleaning $(PROJECT_NAME) ..."$(NOTHING)
	  @$(FIND) . -name '*.swp' -delete
	  @$(FIND) . -name '*.py[co]' -delete
	  @$(FIND) . -name '*~' -delete

distclean: clean
	  @echo $(GREEN)"Cleaning $(PROJECT_NAME) packages..."$(NOTHING)
	  @$(RM) -rf dist

.PHONY: clean distclean build doc test dist install
