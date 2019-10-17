#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Trafficker.handlers.tcpflow import TCPFlow


def tcpHandler(packetNum, packet, glob):
    tcp = None
    for l in packet.layers:
        if l.name == "TCP":
            tcp = l
    if tcp is None:
        return glob
    # print(repr(tcp))
    if 'tcpflow' not in glob:
        glob['tcpflow'] = []
    if tcp.syn and not tcp.ack:
        glob['tcpflow'].append(TCPFlow(tcp))
    else:
        for t in glob['tcpflow']:
            if t.isNext(tcp):
                t.tcps.append(tcp)
                break
    return glob
