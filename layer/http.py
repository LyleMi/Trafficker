#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket
import struct

from layer import layer


class HTTP(layer):

    def __init__(self):
        pass

    def pack(self):
        pass

    @classmethod
    def unpack(cls, packet):
        self.content = packet

if __name__ == '__main__':
    print HTTP().name
