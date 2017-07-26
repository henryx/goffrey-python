#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Copyright (C) 2017 Enrico Bianchi (enrico.bianchi@gmail.com)
# Project       Goffrey
# Description   A simple IPAM
# License       GPL version 2 (see GPL.txt for details)

import argparse
import configparser
import sys

__author__ = "Enrico Bianchi"
__copyright__ = "Copyright 2017, Enrico Bianchi"
__credits__ = ["Enrico Bianchi", ]
__license__ = "GPLv2"
__maintainer__ = "Enrico Bianchi"
__email__ = "enrico.bianchi@gmail.com"
__status__ = "Development"
__version__ = "0.0.0"


def init_args():
    """
    Argument parser initialization
    :return: An object that parse arguments passed from command line
    """

    args = argparse.ArgumentParser(description="Goffrey")

    # Global arguments
    args.add_argument("-c", "--cfg", metavar="<file>", help="Use the specified configuration file")

    # Commands
    sub = args.add_subparsers(description="Commands", dest="command")
    register = sub.add_parser("register", description="Register a network")
    unregister = sub.add_parser("unregister", description="Unregister a network")
    assign = sub.add_parser("assign", description="Associate an address")
    remove = sub.add_parser("remove", description="Remove association for address")

    # Register
    register.add_argument("-n", "--name", help="Set the name of the network")
    register.add_argument("-N", "--network", help="Set the network addresses")
    register.add_argument("-M", "--netmask", help="Set the network mask")

    # Unregister
    unregister.add_argument("-n", "--name", help="Name of the network to unregister")

    # Assign
    assign.add_argument("-n", "--name", help="Name of the network to assign host")
    assign.add_argument("-H", "--host", help="Name of the host to assign IP")

    # Remove
    remove.add_argument("-n", "--name", help="Name of the network to remove host")
    remove.add_argument("-H", "--host", help="Name of the host to remove IP")

    return args


def main():
    """
    Main function
    :return:
    """

    args = init_args().parse_args(sys.argv[1:])

    if not args.cfg:
        # TODO: check correct location if you are on Windows or on Linux
        cfgfile = "goffrey.cfg"
    else:
        cfgfile = args.cfg

    cfg = configparser.ConfigParser()
    try:
        cfg.read(cfgfile)
    except:
        print("Cannot open the configuration file {}: not found".format(args.cfg))
        args.print_help()
        sys.exit(1)

    if args.command == "register":
        pass
    elif args.command == "register":
        pass
    elif args.command == "assign":
        pass
    elif args.command == "remove":
        pass

    print("Goffrey version {}".format(__version__))


if __name__ == "__main__":
    main()
