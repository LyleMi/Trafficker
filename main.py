#!/usr/bin/env python
# -*- coding: utf-8 -*-


import sys

from packets.pcap import Pcap
from handlers.tcp import tcpHandler

if __name__ == '__main__':
    p = Pcap(sys.argv[1], [tcpHandler])
    '''
    for i in p.glob['tcpflow']:
        i.extract()
        for t in i.tcps:
            print(repr(t))
        for d in i.extract():
            print(d)
            print("=" * 50)
    '''
