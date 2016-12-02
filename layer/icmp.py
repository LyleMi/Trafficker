# -*- coding: utf-8 -*-
'''
RFC 792

 0                   1                   2                   3
 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|     Type      |      Code     |          Checksum             |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|           Identifier          |        Sequence Number        |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+

'''

import socket
import struct

from utils.utils import checksum
from layer import layer


class ICMP(layer):

    def __init__(self, icmp):
        self.type = icmp["type"]
        self.code = icmp["code"]
        self.checksum = icmp["checksum"]
        self.ident = icmp["ident"]
        self.seq = icmp["seq"]

    def pack(self):
        icmp_header = struct.pack("!BBHHH",
                                self.type,
                                self.code,
                                self.checksum,
                                self.ident,
                                self.seq)
        self.checksum = checksum(icmp_header)
        icmp_header = struct.pack("!BBHHH",
                                self.type,
                                self.code,
                                self.checksum,
                                self.ident,
                                self.seq)
        return icmp_header

    def unpack(self, packet):
        return struct.unpack("!BBHHH", packet)


if __name__ == '__main__':
    '''
    type 8, code 0：ping request
    type 0, code 0：ping reply
    type 11, code 0：timeout
    '''

    icmp_config = {}
    icmp_config["type"] = 0
    icmp_config["code"] = 8
    icmp_config["checksum"] = 0
    icmp_config["ident"] = 0
    icmp_config["seq"] = 0
    icmp = ICMP(icmp_config)
    packet = icmp.pack()
    print packet
    print icmp.unpack(packet)