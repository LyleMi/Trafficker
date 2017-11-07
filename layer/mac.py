#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket
import struct

from utils.utils import checksum, parseMac
from layer import layer

# Internet Protocol Packet
ETH_P_IP = 0x0800
ETH_P_ARP = 0x0806


class ETHER(layer):

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

    @staticmethod
    def unpack(packet):
        ethernet = struct.unpack('!6s6sH', packet)
        return ethernet

if __name__ == '__main__':
    mac = ETHER({
        "dst": "ff:ff:ff:ff:ff:ff",
        "src": "00:00:00:00:00:00",
        "type": 36864
    })
    packet = mac.pack()
    print packet.encode('hex')
    print mac.unpack(packet)
