#!/usr/bin/env python
# -*- coding: utf-8 -*-

import struct

from packets.packet import Packet


class Pcap(object):

    """Pcap file reader"""

    def __init__(self, filepath):
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
            packet = Packet(header, fpcap.read(packetLen), packetNum)
            packetNum += 1

        fpcap.close()
