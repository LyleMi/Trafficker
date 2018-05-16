#!/usr/bin/env python
# -*- coding: utf-8 -*-


def freqHandler(packetNum, packet, glob):
    if 'freq' not in glob:
        glob['freq'] = []
    glob['freq'].append({
        "srcip": packet.srcip,
        "dstip": packet.dstip,
        "srcp": packet.srcp,
        "dstp": packet.dstp,
        "timestamp": packet.header['GMTtime']
    })
    return glob
