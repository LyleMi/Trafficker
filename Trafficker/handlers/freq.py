#!/usr/bin/env python
# -*- coding: utf-8 -*-


def freqHandler(packetNum, packet, glob):
    if 'freq' not in glob:
        glob['freq'] = []
    glob['freq'].append([
        packet.srcip,
        packet.srcp,
        packet.dstip,
        packet.dstp,
        packet.header['GMTtime'],
        packet.len
    ])
    return glob
