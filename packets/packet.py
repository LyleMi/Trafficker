#!/usr/bin/env python
# -*- coding: utf-8 -*-

from layer.mac import ETHER
from layer.ip import IP
from layer.udp import UDP
from layer.tcp import TCP
from layer.dns import DNS
from layer.smtp import SMTP
from layer.http import HTTP
from layer.pop import POP
from layer.vlan import VLAN

from packets.buffer import Buffer


class Packet(object):

    """traffic packet"""

    def __init__(self, data):

        super(Packet, self).__init__()
        data = Buffer(data)
        mac = ETHER.unpack(data.get(14))
        self.layers = [mac]
        self.srcip = ""
        self.dstip = ""
        self.srcp = 0
        self.dstp = 0
        ntype = mac.type

        if mac.type == ETHER.VLAN:
            vlan = VLAN.unpack(data.get(4))
            self.layers.append(vlan)
            ntype = vlan.type

        if ntype == ETHER.IPv4:
            ip = IP.unpack(data.get(20))
            self.srcip = ip.ssrc
            self.dstip = ip.sdst
            self.layers.append(ip)
            if ip.protocol == IP.Protocol.TCP:
                tcp = TCP.unpack(data)
                self.srcp = tcp.srcp
                self.dstp = tcp.dstp
                self.layers.append(tcp)
                if 80 in [tcp.srcp, tcp.dstp]:
                    http = HTTP.unpack(tcp.payload)
                    self.layers.append(http)
                elif 25 in [tcp.srcp, tcp.dstp]:
                    smtp = SMTP.unpack(tcp.payload)
                    self.layers.append(smtp)
                elif 110 in [tcp.srcp, tcp.dstp]:
                    pop = POP.unpack(tcp.payload)
                    self.layers.append(pop)
            elif ip.protocol == IP.Protocol.UDP:
                udp = UDP.unpack(data.get(8))
                self.srcp = udp.src
                self.dstp = udp.dst
                self.layers.append(udp)
                if 53 in [udp.dst, udp.src]:
                    dns = DNS.unpack(data)
                    self.layers.append(dns)

