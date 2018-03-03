#!/usr/bin/env python
# -*- coding: utf-8 -*-

import struct

from packets.packet import Packet


def _defaultHandler(packetNum, layers):
    print packetNum, layers


class Pcap(object):

    """Pcap file reader"""

    def __init__(self, filepath, handler=_defaultHandler):
        super(Pcap, self).__init__()
        self.filepath = filepath
        fpcap = open(filepath, 'rb')
        packetNum = 0

        # pcap文件的数据包解析
        header = {}
        header['magic_number'] = fpcap.read(4)
        header['version_major'] = fpcap.read(2)
        header['version_minor'] = fpcap.read(2)
        header['thiszone'] = fpcap.read(4)
        header['sigfigs'] = fpcap.read(4)
        header['snaplen'] = fpcap.read(4)
        header['linktype'] = fpcap.read(4)

        self.header = header

        while True:
            header = fpcap.read(16)
            if len(header) < 16:
                break
            packetLen = struct.unpack('I', header[12:16])[0]
            '''
            header = {}
            header['GMTtime'] = header[:4]
            header['MicroTime'] = header[4:8]
            header['caplen'] = header[8:12]
            header['len'] = header[12:16]
            '''
            try:
                packet = Packet(fpcap.read(packetLen))
                handler(packetNum, packet.layers)
            except Exception as e:
                print(e)
            packetNum += 1

        fpcap.close()
