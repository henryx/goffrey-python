#!/usr/bin/env python3

import argparse

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
    args = argparse.ArgumentParser(description="Goffrey")

    return args


def main():
    args = init_args().parse_args(sys.argv)

    print("Goffrey version {}".format(__version__))


if __name__ == "__main__":
    main()
