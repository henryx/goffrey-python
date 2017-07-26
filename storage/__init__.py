# -*- coding: utf-8 -*-

# Copyright (C) 2017 Enrico Bianchi (enrico.bianchi@gmail.com)
# Project       Goffrey
# Description   A simple IPAM
# License       GPL version 2 (see GPL.txt for details)

_author__ = "Enrico Bianchi"
__copyright__ = "Copyright 2017, Enrico Bianchi"
__credits__ = ["Enrico Bianchi", ]
__license__ = "GPLv2"
__maintainer__ = "Enrico Bianchi"
__email__ = "enrico.bianchi@gmail.com"
__status__ = "Development"
__version__ = "0.0.0"

__all__ = ["engines"]


class Database(object):
    _conn = None
    _autocommit = None
    _paramstyle = None

    @property
    def autocommit(self):
        return self._autocommit

    @property
    def conn(self):
        return self._conn

    @property
    def paramstyle(self):
        if self._paramstyle == "qmark":
            return "?"
        elif self._paramstyle == "format":
            return "%s"

    def __init__(self, cfg, autocommit=False):
        self._autocommit = autocommit

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

    def close(self):
        try:
            if self._conn:
                self._conn.commit() if not self._autocommit else None
                self._conn.close()
        except:
            pass

    def register(self, name, ipnetwork):
        pass
