#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket
import struct

from Trafficker.layer.layer import layer


class ETHER(layer):

    IPv4 = 0x0800
    IPv6 = 0x86dd
    ARP = 0x0806
    VLAN = 0x8100

    def __init__(self, mac=None):
        if mac is None:
            return
        self.src = self.parseMac(mac["src"])
        self.dst = self.parseMac(mac["dst"])
        self.type = mac["type"]

    def pack(self):
        ethernet = struct.pack('!6s6sH',
                               self.dst,
                               self.src,
                               self.type)
        return ethernet

    @staticmethod
    def unpack(packet):
        m = ETHER()
        ethernet = struct.unpack('!6s6sH', packet)
        m.dst = ethernet[0]
        m.src = ethernet[1]
        m.type = ethernet[2]
        return m

    @property
    def stype(self):
        if self.type == self.IPv4:
            return "IPv4"
        elif self.type == self.ARP:
            return "ARP"
        elif self.type == self.IPv6:
            return "IPv6"
        elif self.type == self.VLAN:
            return "VLAN"
        return "unknown %d" % (self.type)

    @property
    def dstmac(self):
        return self.parseMac(self.dst, True)

    @property
    def srcmac(self):
        return self.parseMac(self.src, True)

    def __repr__(self):
        return "<MAC %s -> %s, %s>" % (
            self.parseMac(self.dst, True),
            self.parseMac(self.src, True),
            self.stype
        )


if __name__ == '__main__':
    mac = ETHER({
        "dst": "ff:ff:ff:ff:ff:ff",
        "src": "00:00:00:00:00:00",
        "type": 36864
    })
    packet = mac.pack()
    print(packet)
    print(mac.unpack(packet).pack())
