#!/usr/bin/env python
# -*- coding: utf-8 -*-


import socket
import struct

from Trafficker.layer.layer import layer


class CLDAP(layer):

    def __init__(self):
        self.payload = ""

    @classmethod
    def unpack(cls, packet):
        o = CLDAP()
        return o
