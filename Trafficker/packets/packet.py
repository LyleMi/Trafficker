#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time

from Trafficker.layer.mac import ETHER
from Trafficker.layer.ip import IP
from Trafficker.layer.udp import UDP
from Trafficker.layer.tcp import TCP
from Trafficker.layer.dns import DNS
from Trafficker.layer.smtp import SMTP
from Trafficker.layer.http import HTTP
from Trafficker.layer.pop import POP
from Trafficker.layer.vlan import VLAN

from Trafficker.packets.buffer import Buffer


class Packet(object):

    """traffic packet"""

    def __init__(self, data, header):

        super(Packet, self).__init__()
        header = Buffer(header)
        self.header = {}
        self.header['GMTtime'], self.header['MicroTime'], self.header['caplen'], self.header['len'] = header.unpack("IIII")
        data = Buffer(data)
        mac = ETHER.unpack(data.get(14))
        self.mac = mac
        self.layers = [mac]
        self.srcip = ""
        self.dstip = ""
        self.protocol = ""
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
                tcp = TCP.unpack(data, ip.tl - 40)
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
                self.protocol = "TCP"
            elif ip.protocol == IP.Protocol.UDP:
                udp = UDP.unpack(data.get(8))
                self.srcp = udp.src
                self.dstp = udp.dst
                self.layers.append(udp)
                if 53 in [udp.dst, udp.src]:
                    dns = DNS.unpack(data)
                    self.layers.append(dns)
                self.protocol = "UDP"
            elif ip.protocol == IP.Protocol.IGMP:
                self.protocol = "IGMP"
            else:
                print("unknown protocol %s" % ip.protocol)

    def __repr__(self):
        timearray = time.localtime(self.header['GMTtime'])
        timestr = time.strftime("%Y-%m-%d %H:%M:%S", timearray)
        return "<[%s] %s %s(%s):%s -> %s(%s):%s>" % (
            timestr,
            self.protocol,
            self.srcip,
            self.mac.srcmac,
            self.srcp,
            self.dstip,
            self.mac.dstmac,
            self.dstp
        )
