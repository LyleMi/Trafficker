#!/usr/bin/env python
# -*- coding: utf-8 -*-
# IGMPv2 https://www.ietf.org/rfc/rfc2236.txt
# IGMPv3 https://www.ietf.org/rfc/rfc3376.txt
import socket
import struct

from Trafficker.layer.layer import layer


class IGMP(layer):

    def __init__(self, igmp=None):
        if igmp is None:
            return

    def json(self):
        return {
            "type": self.type,
            "maxresptime": self.maxresptime,
            "checksum": self.checksum,
            "groupaddr": socket.inet_ntoa(self.groupaddr),
        }

    def pack(self):
        data = struct.pack(
            '!BBH',
            self.type,
            self.maxresptime,
            self.checksum
        )
        return data + self.groupaddr

    @classmethod
    def unpack(cls, packet):
        igmp = IGMP()
        data = struct.unpack('!BBH', packet[:4])
        igmp.type = data[0]
        igmp.maxresptime = data[1]
        igmp.checksum = data[2]
        igmp.groupaddr = packet[4:8]
        return igmp


if __name__ == '__main__':
    igmp = IGMP.unpack(b'\x16\x00\x09\x04\xe0\x00\x00\xfb')
    print(igmp.json())
    print(igmp)
