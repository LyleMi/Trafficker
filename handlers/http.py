#!/usr/bin/env python
# -*- coding: utf-8 -*-

def httpHandler(packetNum, layers):
    if layers[-1].name != "http":
        return