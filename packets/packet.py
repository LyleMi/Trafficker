#!/usr/bin/env python
# -*- coding: utf-8 -*-

from layer.mac import ETHER
from layer.ip import IP
from layer.udp import UDP
from layer.tcp import TCP
from layer.dns import DNS

from packets.buffer import Buffer


class Packet(object):

    """pcap packet"""

    def __init__(self, header, data, packetNum):

        super(Packet, self).__init__()
        self.header = {}
        self.header['GMTtime'] = header[:4]
        self.header['MicroTime'] = header[4:8]
        self.header['caplen'] = header[8:12]
        self.header['len'] = header[12:16]
        data = Buffer(data)
        mac = ETHER.unpack(data.get(14))
        if mac.type == ETHER.IPv4:
            ip = IP.unpack(data.get(20))
            if ip.protocol == IP.Protocol.TCP:
                tcp = TCP.unpack(data)
                if 80 in [tcp.srcp, tcp.dstp]:
                    return
                if 25 in [tcp.srcp, tcp.dstp]:
                    print tcp.payload
                    return
            elif ip.protocol == IP.Protocol.UDP:
                udp = UDP.unpack(data.get(8))
                if udp.dst == 53:
                    dns = DNS.unpack(data)
                    print dns.queries[0].qname
