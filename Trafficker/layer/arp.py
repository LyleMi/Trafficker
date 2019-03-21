#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket
import struct

from Trafficker.layer.layer import layer

ARPOP_REQUEST = 0x0001
ARPOP_REPLY = 0x0002
HARDWARE_TYPE = 0x0001
PRO_TYPE = 0x0800
HARDWARE_SIZE = 0x0006
PRO_SIZE = 0x0004


class ARP(layer):

    def __init__(self, arp=None):
        if arp is None:
            return
        self.arpop = arp["arpop"]
        self.srcmac = self.parseMac(arp["srcmac"])
        self.srcip = socket.inet_aton(arp["srcip"])
        self.dstmac = self.parseMac(arp["dstmac"])
        self.dstip = socket.inet_aton(arp["dstip"])

    def pack(self):
        arp = struct.pack('!HHBBH6s4s6s4s',
                          HARDWARE_TYPE,
                          PRO_TYPE,
                          HARDWARE_SIZE,
                          PRO_SIZE,
                          self.arpop,
                          self.srcmac,
                          self.srcip,
                          self.dstmac,
                          self.dstip,
                          )
        return arp

    @classmethod
    def unpack(cls, packet):
        data = struct.unpack('!HHBBH6s4s6s4s', packet)
        arp = ARP()
        arp.arpop = data[4]
        arp.srcmac = data[5]
        arp.srcip = data[6]
        arp.dstmac = data[7]
        arp.dstip = data[8]
        return arp

    @property
    def sip(self):
        return socket.inet_ntoa(self.srcip)

    @property
    def dip(self):
        return socket.inet_ntoa(self.dstip)

    @property
    def smac(self):
        return self.parseMac(self.srcmac, True)

    @property
    def dmac(self):
        return self.parseMac(self.srcmac, True)

    def json(self):
        return {
            "src ip": self.sip,
            "src mac": self.smac,
            "dst ip": self.dip,
            "dst mac": self.dmac,
        }

    def __repr__(self):
        return "<ARP %s(%s) -> %s(%s)>" % (
            self.sip,
            self.smac,
            self.dip,
            self.dmac,
        )


if __name__ == '__main__':
    arpConfig = {}
    arpConfig["arpop"] = ARPOP_REQUEST
    arpConfig["srcmac"] = 'ff:ff:ff:ff:ff:ff'
    arpConfig["srcip"] = '127.0.0.1'
    arpConfig["dstmac"] = 'ff:ff:ff:ff:ff:cc'
    arpConfig["dstip"] = '127.0.0.2'
    arp = ARP(arpConfig)
    packet = arp.pack()
    print(packet)
    print(repr(arp))
    print(ARP.unpack(packet))
