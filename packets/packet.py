#!/usr/bin/env python
# -*- coding: utf-8 -*-

from layer.mac import ETHER
from layer.ip import IP

class Packet(object):
    
    """pcap packet"""
    
    def __init__(self, header, data):
    
        super(Packet, self).__init__()
        self.header = {}
        self.header['GMTtime'] = header[:4]
        self.header['MicroTime'] = header[4:8]
        self.header['caplen'] = header[8:12]
        self.header['len'] = header[12:16]

        mac = ETHER.unpack(data[:14])
        print mac.stype

        