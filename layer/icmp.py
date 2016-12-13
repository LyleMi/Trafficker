# -*- coding: utf-8 -*-

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
        self.payload = icmp["payload"]

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
        # print self.payload.encode("hex")
        return icmp_header + self.payload.encode("hex")

    def unpack(self, packet):
        return struct.unpack("!BBHHH", packet)


if __name__ == '__main__':
    icmp_config = {}
    icmp_config["type"] = 0
    icmp_config["code"] = 8
    icmp_config["checksum"] = 0
    icmp_config["ident"] = 0
    icmp_config["seq"] = 0
    icmp_config["payload"] = ""
    icmp = ICMP(icmp_config)
    packet = icmp.pack()
    print packet
    print icmp.unpack(packet)
