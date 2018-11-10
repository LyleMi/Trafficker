#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

from Trafficker.packets.pcap import Pcap


def main():
    if len(sys.argv) < 3:
        print("argument needed")
        return
    whitelist = []
    p = Pcap(sys.argv[1])
    newpcap = open(sys.argv[2], "wb")
    newpcap.write(p.rawheader)
    for packetNum, packet in p.parse():
        if packet.srcip in whitelist or packet.dstip in whitelist:
            continue
        newpcap.write(packet.raw)
    newpcap.close()


if __name__ == '__main__':
    main()
