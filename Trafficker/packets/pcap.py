#!/usr/bin/env python
# -*- coding: utf-8 -*-

import struct

from Trafficker.packets.packet import Packet


class Pcap(object):

    """Pcap File Reader
    """

    def __init__(self, filepath):
        """Pcap file reader

        Args:
            filepath (str): Pcap file path
        """
        super(Pcap, self).__init__()
        self.filepath = filepath
        fpcap = open(filepath, 'rb')
        # pcap文件的数据包解析
        self.rawheader = fpcap.read(24)
        fpcap.close()
        header = {}
        header['magic_number'] = self.rawheader[:4]
        header['version_major'] = self.rawheader[4:6]
        header['version_minor'] = self.rawheader[6:8]
        header['thiszone'] = self.rawheader[8:12]
        header['sigfigs'] = self.rawheader[12:16]
        header['snaplen'] = self.rawheader[16:20]
        header['linktype'] = self.rawheader[20:24]
        self.header = header

    def parse(self, handlers=[], filters=[]):
        # send to handler, save some glob status
        fpcap = open(self.filepath, 'rb')
        fpcap.read(24)
        # pcap文件的数据包解析
        packetNum = 0
        while True:
            header = fpcap.read(16)
            if len(header) < 16:
                break
            packetLen = struct.unpack('I', header[12:16])[0]
            packet = Packet(fpcap.read(packetLen), header)
            yield packetNum, packet
            packetNum += 1
        fpcap.close()

    def parseWithCallback(self, handlers=[], filters=[]):
        """Parse pcap with callback

        Args:
            handlers (func, optional): packet handler
            filters (func, optional): packet filter
        """
        # send to handler, save some glob status
        glob = {}
        fpcap = open(self.filepath, 'rb')
        fpcap.read(24)
        # pcap文件的数据包解析
        packetNum = 0
        while True:
            header = fpcap.read(16)
            if len(header) < 16:
                break
            packetLen = struct.unpack('I', header[12:16])[0]
            packet = Packet(fpcap.read(packetLen), header)
            shouldFilter = False
            for f in filters:
                if f(packetNum, packet, glob):
                    shouldFilter = True
                    break
            if shouldFilter:
                continue
            for handler in handlers:
                glob = handler(packetNum, packet, glob)
            packetNum += 1
        fpcap.close()
