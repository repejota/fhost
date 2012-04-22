.. _tutorial:

========
Tutorial
========

This simple **fhost** usage session is enough to introduce you on this tool:

::

    usage: fhost [-h] [-v] {import,add,export,list,delete} ...

    Create, list, and modify local hostnames.

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

    fhost's epilog


Listing available hosts.

::

    Listing (4) host(s):
        127.0.0.1     -> localhost
        127.0.1.1     -> fhost.org
        192.168.56.101        -> fhost.org
        192.168.56.102        -> subcmd.org

Adding a new host.

::

    $ sudo fhost add 192.168.56.103 fake-host.com fake-host

    fhost list

    Listing (5) host(s):
        127.0.0.1     -> localhost
        127.0.1.1     -> fhost.org
        192.168.56.101        -> fhost.org
        192.168.56.102        -> subcmd.org
        192.168.56.103        -> fake-host.com

Remove a host.

::

    $ sudo fhost remove fake-host.com

    Listing (4) host(s):
        127.0.0.1     -> localhost
        127.0.1.1     -> fhost.org
        192.168.56.101        -> fhost.org
        192.168.56.102        -> subcmd.org
