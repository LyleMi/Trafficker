#!/usr/bin/env python
# -*- coding: utf-8 -*-


def httpHandler(packetNum, layers, glob):
    if layers[-1].name != "http":
        return glob
    return glob
