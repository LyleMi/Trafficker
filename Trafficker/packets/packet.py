#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time

from Trafficker.layer.arp import ARP
from Trafficker.layer.cldap import CLDAP
from Trafficker.layer.dns import DNS
from Trafficker.layer.http import HTTP
from Trafficker.layer.icmp import ICMP
from Trafficker.layer.igmp import IGMP
from Trafficker.layer.ip import IP
from Trafficker.layer.ipv6 import IPv6
from Trafficker.layer.mac import ETHER
from Trafficker.layer.tcp import TCP
from Trafficker.layer.udp import UDP
from Trafficker.layer.smtp import SMTP
from Trafficker.layer.pop import POP
from Trafficker.layer.vlan import VLAN
from Trafficker.layer.ntp import NTP

from Trafficker.packets.buffer import Buffer


class Packet(object):

    """traffic packet"""

    def __init__(self, data, header=None):
        super(Packet, self).__init__()
        self.raw = data
        self.header = {}
        if header is not None:
            self.raw = header + self.raw
            header = Buffer(header)
            self.header['GMTtime'], self.header['MicroTime'], self.header['caplen'], self.header['len'] = header.unpack("IIII")
        print(self.header)
        data = Buffer(data)
        mac = ETHER.unpack(data.get(14))
        self.len = len(data)
        self.mac = mac
        self.layers = [mac]
        self.srcip = ""
        self.dstip = ""
        self.protocol = ""
        self.srcp = 0
        self.dstp = 0
        ntype = mac.type

        if mac.type == ETHER.ethertypes["VLAN"]:
            vlan = VLAN.unpack(data.get(4))
            self.layers.append(vlan)
            ntype = vlan.type

        if ntype == ETHER.ethertypes["IPv4"]:
            ip = IP.unpack(data.get(20))
            self.srcip = ip.ssrc
            self.dstip = ip.sdst
            self.layers.append(ip)
            self.protocol = ip.sprotocol
            if ip.protocol == IP.Protocol.TCP:
                tcp = TCP.unpack(data, ip.tl - 40)
                self.srcp = tcp.srcp
                self.dstp = tcp.dstp
                self.layers.append(tcp)
                if 80 in [tcp.srcp, tcp.dstp]:
                    self.protocol = "HTTP"
                    # http = HTTP.unpack(tcp.payload)
                    http = HTTP()
                    self.layers.append(http)
                elif 25 in [tcp.srcp, tcp.dstp]:
                    self.protocol = "SMTP"
                    smtp = SMTP.unpack(tcp.payload)
                    self.layers.append(smtp)
                elif 110 in [tcp.srcp, tcp.dstp]:
                    self.protocol = "POP"
                    pop = POP.unpack(tcp.payload)
                    self.layers.append(pop)
            elif ip.protocol == IP.Protocol.UDP:
                udp = UDP.unpack(data.get(8))
                self.srcp = udp.src
                self.dstp = udp.dst
                self.layers.append(udp)
                if 53 in [udp.dst, udp.src]:
                    self.protocol = "DNS"
                    dns = DNS.unpack(data)
                    self.layers.append(dns)
                elif 389 in [udp.dst, udp.src]:
                    self.protocol = "CLDAP"
                    cldap = CLDAP.unpack(data)
                    self.layers.append(cldap)
                elif 123 in [udp.dst, udp.src]:
                    self.protocol = "NTP"
                    ntp = NTP.unpack(data)
                    self.layers.append(ntp)
                else:
                    udp.payload = data.getremain()
            elif ip.protocol == IP.Protocol.ICMP:
                icmp = ICMP.unpack(data.getremain())
                self.layers.append(icmp)
            elif ip.protocol == IP.Protocol.IGMP:
                igmp = IGMP.unpack(data.getremain())
                self.layers.append(igmp)
        elif ntype == ETHER.ethertypes["ARP"]:
            self.protocol = "ARP"
            arp = ARP.unpack(data.get(28))
            self.layers.append(arp)
            self.srcip = arp.sip
            self.dstip = arp.dip
        elif ntype == ETHER.ethertypes["IPv6"]:
            self.protocol = "IPv6"
            ipv6 = IPv6.unpack(data.get(40))
            self.layers.append(ipv6)
            self.srcip = ipv6.sip
            self.dstip = ipv6.dip
        elif ntype not in ETHER.ethertypes.values():
            print('Unsupport type %s' % ntype)
        else:
            for etype in ETHER.ethertypes:
                if ntype == ETHER.ethertypes[etype]:
                    self.protocol = etype
                    break

    def json(self):
        ret = {}
        ret['raw'] = self.raw.hex()
        ret['srcip'] = self.srcip
        ret['dstip'] = self.dstip
        ret['protocol'] = self.protocol
        ret['layers'] = []
        for l in self.layers:
            ret['layers'].append(l.json())
        return ret

    def __repr__(self):
        if 'GMTtime' in self.header:
            timearray = time.localtime(self.header['GMTtime'])
            timestr = time.strftime("%Y-%m-%d %H:%M:%S", timearray)
        else:
            timestr = ''
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
