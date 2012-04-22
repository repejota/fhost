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

import re


def isValidHostname(hostname):
    """Check if this is a valid hostname

    Example:

    ::

        hostname = "example.com"
        if isValidHostName(hostname):
            print "Valid Hostname!"
        else:
            print "Invalid Hostname"

    :Results: Boolean value that indicates if the hostname is valid.
    """
    regepx = """^(([a-zA-Z]|[a-zA-Z][a-zA-Z0-9\-]*[a-zA-Z0-9])\.)
                 *
                 ([A-Za-z]|[A-Za-z][A-Za-z0-9\-]*[A-Za-z0-9])$"""
    return re.match(regexp, hostname)


def isValidIP(ip):
    """Check if this is a valid IP

    Example:

    ::

        hostname = "173.194.34.208"
        if isValidIP(hostname):
            print "Valid IP!"
        else:
            print "Invalid IP"

    :Results: Boolean value that indicates if the IP address is valid.
    """
    regexp = """^(([0-9]|[1-9][0-9]|1[0-9]
             {2}
             |2[0-4][0-9]|25[0-5])\.)
             {3}
             ([0-9]|[1-9][0-9]|1[0-9]
             {2}
             |2[0-4][0-9]|25[0-5])$"""
    return re.match(regexp, ip)
