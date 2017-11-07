#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket
import struct

from utils.utils import checksum
from layer import layer

class UDP(layer):

    def __init__(self, udp):
        self.src = udp['srcp']
        self.dst = udp['dstp']
        self.payload = udp['payload']
        self.checksum = 0
        self.length = 8  # UDP Header length

    def pack(self):
        length = self.length + len(self.payload)
        pseudo_header = struct.pack('!HHBBH',
                                    self.src,
                                    self.dst, 0,
                                    socket.IPPROTO_UDP, self.length)
        self.checksum = checksum(pseudo_header)
        packet = struct.pack('!HHHH', self.src, self.dst, length, self.checksum)
        return packet + self.payload.encode('hex')

if __name__ == '__main__':
    udp_config = {}
    udp_config['srcp'] = 13987
    udp_config['dstp'] = 1234
    udp_config['payload'] = ''
    udp = UDP(udp_config)
    print udp.pack()