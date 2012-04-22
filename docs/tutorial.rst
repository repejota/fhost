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
