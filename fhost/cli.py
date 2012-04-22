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

from subcmd.app import App
from subcmd.decorators import arg

from fhost.hosts import Hosts


class Application(App):
    """fhost entry tool class.

    Implements a command-subcommand pattern wich is
    used as a main entry point of this tool.

    A very basic :abbr:`CRUD (Create, Read, Update and Delete)` is provided
    specifically create, list and remove commands to manage hosts.

    Example: ::

        usage: fhost [-h] [-v] {import,add,export,list,delete} ...

        optional arguments:
          -h, --help            show this help message and exit
          -v, --version

        subcommands:
          valid subcommands

          {import,add,export,list,delete}
                                additional help
            add                 Add new host
            delete              Delete existing hostname
            export              Export hosts as a backup
            import              Import hosts from a backup
            list                List available hosts

    The above message shows the usage message help that **fhost** prints if
    no command is executed.
    """
    name = "fhost"

    description = "Create, list, and modify local hostnames."

    version = "0.2"

    def do_list(self, options):
        """List available hosts command.

        No argument is required for this too.

        :Results: list - A list of triplets ( ip, host, alias) hostnames.
        """
        hosts = Hosts()
        print "Listing (%s) host(s):" % len(hosts)
        for host in hosts:
            print "  %s\t-> %s" % (host["ip_address"],
                                   host["canonical_hostname"])

    @arg('alias', help='Valid hostname as alias')
    @arg('hostname', help='Valid hostname')
    @arg('ip', help='Valid IP address')
    def do_add(self, options):
        """Add new host command.

        Each host is composed of three parts:

            * IP name
            * Main hostname
            * An alias to the main hostname.

        Both three arguments are requied.

        :Results: None
        """
        hosts = Hosts()
        try:
            hosts.add(options.ip, options.hostname, options.alias)
        except IOError as e:
            if e.errno == 13:
                print "You don't have permissions to write '%s'. %s" % (
                        hosts.hosts_file,
                        "Did you forgot 'sudo'?")
            else:
                raise IOError
            exit(1)

    @arg('hostname', help='Valid hostname')
    def do_delete(self, options):
        """Delete existing hostname.

        A valid hostname must be passed, no IP or alias are valid arguments.

        :Results: None
        """
        hosts = Hosts()
        try:
            hosts.delete(options.hostname)
        except IOError as e:
            if e.errno == 13:
                print "You don't have permissions to write '%s'. %s" % (
                        hosts.hosts_file,
                        "Did you forgot 'sudo'?")
            else:
                raise IOError
            exit(1)

application = Application()
