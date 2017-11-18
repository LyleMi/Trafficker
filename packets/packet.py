#!/usr/bin/env python
# -*- coding: utf-8 -*-

from layer.mac import ETHER
from layer.ip import IP
from layer.udp import UDP
from layer.tcp import TCP
from layer.dns import DNS
from layer.smtp import SMTP
from layer.vlan import VLAN

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
        self.layers = [mac]
        
        ntype = mac.type

        if mac.type == ETHER.VLAN:
            vlan = VLAN.unpack(data.get(4))
            self.layers.append(vlan)
            ntype = vlan.type

        if ntype == ETHER.IPv4:
            ip = IP.unpack(data.get(20))
            self.layers.append(ip)
            if ip.protocol == IP.Protocol.TCP:
                tcp = TCP.unpack(data)
                self.layers.append(tcp)
                if 80 in [tcp.srcp, tcp.dstp]:
                    return
                if 25 in [tcp.srcp, tcp.dstp]:
                    smtp = SMTP.unpack(tcp.payload)
                    if smtp is None:
                        return
                    self.layers.append(smtp)
            elif ip.protocol == IP.Protocol.UDP:
                udp = UDP.unpack(data.get(8))
                self.layers.append(udp)
                if udp.dst == 53:
                    dns = DNS.unpack(data)
                    self.layers.append(dns)
