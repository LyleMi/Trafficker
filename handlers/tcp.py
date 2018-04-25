#!/usr/bin/env python
# -*- coding: utf-8 -*-

from handlers.tcpflow import TCPFlow


def tcpHandler(packetNum, layers, glob):
    tcp = None
    for l in layers:
        if l.name == "TCP":
            tcp = l
    if tcp is None:
        return glob
    # print(repr(tcp))
    if tcp.syn and not tcp.ack:
        if 'tcpflow' not in glob:
            glob['tcpflow'] = []
        glob['tcpflow'].append(TCPFlow(tcp))
    else:
        for t in glob['tcpflow']:
            if t.isNext(tcp):
                t.tcps.append(tcp)
                break
    return glob
