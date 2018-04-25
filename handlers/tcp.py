#!/usr/bin/env python
# -*- coding: utf-8 -*-


def tcpHandler(packetNum, layers):
    tcp = None
    for l in layers:
        if l.name == "TCP":
            tcp = l
    if tcp is None:
        return
    print(repr(tcp))
