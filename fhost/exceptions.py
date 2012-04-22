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


class BaseException(Exception):
    """Base Exception

    This is the base exception. All other exceptions from **fhost** module
    inherits from this one.

    Example:

    ::

        try:
            ...
        except BaseException:
            raise BaseException("base exception raised!")
            sys.exit(1)
    """


class InvalidHostnameException(BaseException):
    """Invalid Hostname

    This exception is raised when some part of **fhost** code validates a
    hostname format.

    As /etc/hosts file is quite delicated beacuse it can affect the whole
    system, **fhost** performs aggressive validations on all input and
    output data.

    A common string message is shown to the user if this exeption raises.

    Example:

    ::

        try:
            ...
        except InvalidHostnameException:
            raise InvalidHostnameException("invalid hostname exception raised")
            sys.exit(1)
    """


class InvalidIPException(BaseException):
    """Invalid IP

    This exception is raised when some part of **fhost** code validates an
    IP address format.

    As /etc/hosts file is quite delicated beacuse it can affect the whole
    system, **fhost** performs aggressive validations on all input and
    output data.

    A common string message is shown to the user if this exeption raises.

    Example:

    ::

        try:
            ...
        except InvalidIPException:
            raise InvalidIPException("invalid ip exception raised!")
            sys.exit(1)
    """
