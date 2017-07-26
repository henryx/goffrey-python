# -*- coding: utf-8 -*-

# Copyright (C) 2017 Enrico Bianchi (enrico.bianchi@gmail.com)
# Project       Goffrey
# Description   A simple IPAM
# License       GPL version 2 (see GPL.txt for details)
import storage.engines
from operations import Operation

_author__ = "Enrico Bianchi"
__copyright__ = "Copyright 2017, Enrico Bianchi"
__credits__ = ["Enrico Bianchi", ]
__license__ = "GPLv2"
__maintainer__ = "Enrico Bianchi"
__email__ = "enrico.bianchi@gmail.com"
__status__ = "Development"
__version__ = "0.0.0"

class Register(Operation):
    def __init__(self, cfg):
        super().__init__(cfg)

    def start(self, name, network, netmask):
        if self._cfg["general"]["database"] == "sqlite":
            db = storage.engines.SQLite(self._cfg)
        else:
            raise ValueError("Database engine not supported: {}".format(self._cfg["general"]["database"]))

        db.register(name, network, netmask)
        print("Registered section")
