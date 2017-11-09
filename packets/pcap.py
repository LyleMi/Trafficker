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
        data = fpcap.read(24)
        packetNum = 0
        
        # pcap文件的数据包解析
        header = {}
        header['magic_number'] = data[0:4]
        header['version_major'] = data[4:6]
        header['version_minor'] = data[6:8]
        header['thiszone'] = data[8:12]
        header['sigfigs'] = data[12:16]
        header['snaplen'] = data[16:20]
        header['linktype'] = data[20:24]
        self.header = header

        while True:
            header = fpcap.read(16)
            if len(header) < 16:
                break
            packetLen = struct.unpack('I', header[12:16])[0]
            packet = Packet(header, fpcap.read(packetLen), packetNum)
            packetNum += 1

        fpcap.close()
