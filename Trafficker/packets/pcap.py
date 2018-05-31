#!/usr/bin/env python
# -*- coding: utf-8 -*-

import struct

from Trafficker.packets.packet import Packet


def _defaultHandler(packetNum, packet, glob):
    """default packet handler
    
    Args:
        packetNum (int): packet number
        packet (obj): packet
        glob (dict): global dict
    
    Returns:
        dict: glob
    """
    print(packetNum, packet)
    return glob

def _defaultFilter(packetNum, packet, glob):
    '''Filter for Traffic
    
    Args:
        packetNum (int): packet number
        packet (obj): packet
        glob (dict): global dict
    
    Returns:
        bool: if True do not hanlde that packet
    '''
    return False


class Pcap(object):

    """Pcap File Reader
    """

    def __init__(self, filepath, handlers=[_defaultHandler], filters=[_defaultFilter]):
        """Pcap file reader
        
        Args:
            filepath (str): Pcap file path
            handlers (func, optional): packet handler
        """
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
            packet = Packet(fpcap.read(packetLen), header)
            shouldFilter = False
            for f in filters:
                if f(packetNum, packet, self.glob):
                    shouldFilter = True
                    break
            if shouldFilter:
                continue
            for handler in handlers:
                self.glob = handler(packetNum, packet, self.glob)
            packetNum += 1

        fpcap.close()
