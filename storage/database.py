# Copyright (C) 2017 Enrico Bianchi (enrico.bianchi@gmail.com)
# Project       Goffrey
# Description   A simple IPAM
# License       GPL version 2 (see GPL.txt for details)


class Database(object):
    _conn = None

    @property
    def conn(self):
        return self._conn

    def __init__(self, cfg):
        pass

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        try:
            if self._conn:
                self._conn.commit()
                self._conn.close()
        except:
            pass
