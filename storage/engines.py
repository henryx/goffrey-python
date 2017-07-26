# -*- coding: utf-8 -*-

# Copyright (C) 2017 Enrico Bianchi (enrico.bianchi@gmail.com)
# Project       Goffrey
# Description   A simple IPAM
# License       GPL version 2 (see GPL.txt for details)
import sqlite3

from storage import Database


class SQLite(Database):
    def __init__(self, cfg):
        super().__init__(cfg)

        self._conn = sqlite3.connect(cfg["sqlite"]["location"])

        if not self.checkschema():
            self.createschema()

    def checkschema(self):
        return True

    def createschema(self):
        pass