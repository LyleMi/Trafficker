#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

from layer.mac import ETHER
from layer.ip import IP
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
            tcp = TCP.unpack(data)
            print tcp.seq
            if 80 not in [tcp.srcp, tcp.dstp]:
                print tcp.srcp, tcp.dstp
            if len(tcp.payload) > 0:
                with open(
                        os.path.join("re", str(packetNum)),
                        "wb"
                ) as f:
                    f.write(tcp.payload)
