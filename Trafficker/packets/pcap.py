#!/usr/bin/env python
# -*- coding: utf-8 -*-

import struct

from Trafficker.packets.packet import Packet


def _defaultHandler(packetNum, layers, glob):
    print(packetNum, layers)
    return glob


class Pcap(object):

    """Pcap file reader"""

    def __init__(self, filepath, handlers=[_defaultHandler]):
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
        # send to handler, save some glob status
        self.glob = {}

        while True:
            header = fpcap.read(16)
            if len(header) < 16:
                break
            packetLen = struct.unpack('I', header[12:16])[0]
            try:
                packet = Packet(fpcap.read(packetLen), header)
                for handler in handlers:
                    self.glob = handler(packetNum, packet, self.glob)
            except Exception as e:
                print(e)
            packetNum += 1

        fpcap.close()
