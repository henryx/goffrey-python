# -*- coding: utf-8 -*-

# Copyright (C) 2017 Enrico Bianchi (enrico.bianchi@gmail.com)
# Project       Goffrey
# Description   A simple IPAM
# License       GPL version 2 (see GPL.txt for details)
import sqlite3
from contextlib import closing

from storage import Database


class SQLite(Database):
    def __init__(self, cfg):
        super().__init__(cfg)

        self._conn = sqlite3.connect(cfg["sqlite"]["location"])

        if not self.checkschema():
            self.createschema()

    def checkschema(self):
        query = "SELECT count(*) FROM sqlite_master"
        with closing(self._conn.cursor()) as cur:
            cur.execute(query)
            val = cur.fetchone()[0]

        if val == 0:
            return False
        else:
            return True

    def createschema(self):
        pass