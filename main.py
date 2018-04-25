#!/usr/bin/env python
# -*- coding: utf-8 -*-


import sys

from packets.pcap import Pcap
from handlers.tcp import tcpHandler

if __name__ == '__main__':
    p = Pcap(sys.argv[1], [tcpHandler])
    t = p.glob['tcpflow'][-1]
    for tcp in t.tcps:
        print(repr(tcp))
