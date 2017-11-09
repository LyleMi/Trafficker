#!/usr/bin/env python
# -*- coding: utf-8 -*-

from layer.mac import ETHER
from layer.ip import IP
from layer.udp import UDP
from layer.tcp import TCP


class Packet(object):

    """pcap packet"""

    def __init__(self, header, data, packetNum):

        super(Packet, self).__init__()
        self.header = {}
        self.header['GMTtime'] = header[:4]
        self.header['MicroTime'] = header[4:8]
        self.header['caplen'] = header[8:12]
        self.header['len'] = header[12:16]
        mac = ETHER.unpack(data[:14])
        data = data[14:]
        if mac.type == ETHER.IPv4:
            ip = IP.unpack(data)
            data = data[20:]
            if ip.protocol == IP.Protocol.TCP:
                tcp = TCP.unpack(data)
                if 80 in [tcp.srcp, tcp.dstp]:
                    return
            elif ip.protocol == IP.Protocol.UDP:
                UDP.unpack(data[:8])
                data = data[8:]
