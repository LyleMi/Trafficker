#!/usr/bin/env python
# -*- coding: utf-8 -*-


def udpHandler(packetNum, packet, glob):
    names = map(lambda i: i.name.lower(), packet.layers)
    if "udp" not in names:
        return glob
    return glob
