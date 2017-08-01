# -*- coding: utf-8 -*-

# Copyright (C) 2017 Enrico Bianchi (enrico.bianchi@gmail.com)
# Project       Goffrey
# Description   A simple IPAM
# License       GPL version 2 (see GPL.txt for details)
import sqlite3
from contextlib import closing

import mysql.connector

from storage import Database


class SQLite(Database):
    def __init__(self, cfg, autocommit=False):
        super().__init__(cfg, autocommit)

        if autocommit:
            self._conn = sqlite3.connect(cfg["sqlite"]["location"], isolation_level=None)
        else:
            self._conn = sqlite3.connect(cfg["sqlite"]["location"])

        self._paramstyle = sqlite3.paramstyle

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
        tables = [" ".join(["CREATE TABLE sections(",
                            "section VARCHAR(30),",
                            "network VARCHAR(15),",
                            "netmask VARCHAR(15),",
                            "PRIMARY KEY(section))"]),
                  " ".join(["CREATE TABLE addresses(",
                            "section VARCHAR(30),",
                            "address VARCHAR(15),",
                            "hostname VARCHAR(255),",
                            "assigned TIMESTAMP)"])
                  ]

        with closing(self._conn.cursor()) as cur:
            for table in tables:
                cur.execute(table)


class MySQL(Database):
    def __init__(self, cfg, autocommit=False):
        super().__init__(cfg, autocommit)

        dsn = {
            "user": cfg["mysql"]["user"],
            "password": cfg["mysql"]["password"],
            "database": cfg["mysql"]["database"],
            "host": cfg["mysql"]["host"],
            "port": cfg["mysql"]["port"],
            "autocommit": autocommit
        }

        self._conn = mysql.connector.connect(**dsn)

        if not self.checkschema():
            self.createschema()

    def checkschema(self):
        return True

    def createschema(self):
        pass
