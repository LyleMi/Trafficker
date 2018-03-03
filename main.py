#!/usr/bin/env python
# -*- coding: utf-8 -*-


import sys

from packets.pcap import Pcap

if __name__ == '__main__':
    Pcap(sys.argv[1])
