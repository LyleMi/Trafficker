#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket
import struct

from utils.utils import checksum, parseMac
from layer import layer


class ETHER(layer):

    IPv4 = 0x0800
    IPv6 = 0x86dd
    ARP = 0x0806

    def __init__(self, mac):
        self.src = parseMac(mac["src"])
        self.dst = parseMac(mac["dst"])
        self.type = mac["type"]

    def pack(self):
        ethernet = struct.pack('!6s6sH',
                               self.dst,
                               self.src,
                               self.type)
        return ethernet
    
    @property
    def stype(self):

        if self.type == ETHER.IPv4:
            return "IPv4"
        elif self.type == ETHER.ARP:
            return "ARP"
        elif self.type == ETHER.IPv6:
            return "IPv6"
        return "unknown"

    @staticmethod
    def unpack(packet):
        ethernet = struct.unpack('!6s6sH', packet)
        ethernet = {
            "dst": ethernet[0].encode("hex"),
            "src": ethernet[1].encode("hex"),
            "type": ethernet[2],
        }
        return ETHER(ethernet)

if __name__ == '__main__':
    import os
    import sys
    sys.path.append(os.path.abspath(".."))
    mac = ETHER({
        "dst": "ff:ff:ff:ff:ff:ff",
        "src": "00:00:00:00:00:00",
        "type": 36864
    })
    packet = mac.pack()
    print packet.encode('hex')
    print mac.unpack(packet).pack().encode('hex')
