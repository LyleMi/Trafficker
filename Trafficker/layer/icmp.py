#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket
import struct

from Trafficker.layer.layer import layer


class ICMP(layer):

    def __init__(self, icmp):
        self.type = icmp["type"]
        self.code = icmp["code"]
        self.checksum = icmp["checksum"]
        self.ident = icmp["ident"]
        self.seq = icmp["seq"]
        self.payload = icmp["payload"]

    def pack(self):
        icmpHeader = struct.pack("!BBHHH",
                                 self.type,
                                 self.code,
                                 self.checksum,
                                 self.ident,
                                 self.seq)
        self.checksum = self.calChecksum(icmpHeader)
        icmpHeader = struct.pack("!BBHHH",
                                 self.type,
                                 self.code,
                                 self.checksum,
                                 self.ident,
                                 self.seq)
        return icmpHeader + self.payload

    def unpack(self, packet):
        return struct.unpack("!BBHHH", packet)


if __name__ == '__main__':
    icmpConfig = {}
    icmpConfig["type"] = 0
    icmpConfig["code"] = 8
    icmpConfig["checksum"] = 0
    icmpConfig["ident"] = 0
    icmpConfig["seq"] = 0
    icmpConfig["payload"] = b""
    icmp = ICMP(icmpConfig)
    packet = icmp.pack()
    print(packet)
    print(icmp.unpack(packet))
