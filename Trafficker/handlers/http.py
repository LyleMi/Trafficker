#!/usr/bin/env python
# -*- coding: utf-8 -*-


def httpHandler(packetNum, packet, glob):
    if packet.layers[-1].name != "http":
        return glob
    return glob
