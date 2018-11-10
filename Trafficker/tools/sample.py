#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

from Trafficker.packets.pcap import Pcap
from Trafficker.handlers.analysis import baseHandler


def main():
    if len(sys.argv) < 2:
        print("argv needed")
        return

    p = Pcap(sys.argv[1])

    for packetNum, packet in p.parse():
        pass

    p.parseWithCallback([baseHandler])


if __name__ == '__main__':
    main()
