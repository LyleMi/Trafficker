#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket
import struct

from utils.utils import checksum
from layer import layer


class TCP(layer):

    def __init__(self, tcp=None):
        if tcp is None:
            return
        self.srcp = tcp['srcp']
        self.dstp = tcp['dstp']
        self.seqn = tcp['seqnumber']
        self.ackn = tcp['acknumber']
        self.offset = tcp['offset']  # Data offset: 5x4 = 20 bytes
        self.reserved = tcp['reserved']
        self.urg = tcp['urg']
        self.ack = tcp['ack']
        self.psh = tcp['psh']
        self.rst = tcp['rst']
        self.syn = tcp['syn']
        self.fin = tcp['fin']
        self.window = tcp['window']  # socket.htons(5840)
        self.checksum = tcp['checksum']
        self.urgp = tcp['urgp']
        self.payload = tcp['payload'].decode("hex")
        self.option = tcp['option'].decode("hex")
        self.src = ""
        self.destination = ""

    def pack(self):
        data_offset = (self.offset << 4) + 0
        flags = self.fin + (self.syn << 1) + (self.rst << 2) + \
            (self.psh << 3) + (self.ack << 4) + (self.urg << 5)
        tcp_header = struct.pack('!HHLLBBHHH',
                                 self.srcp,
                                 self.dstp,
                                 self.seqn,
                                 self.ackn,
                                 data_offset,
                                 flags,
                                 self.window,
                                 self.checksum,
                                 self.urgp)
        tcp_checksum = checksum(tcp_header)
        tcp_header = struct.pack("!HHLLBBH",
                                 self.srcp,
                                 self.dstp,
                                 self.seqn,
                                 self.ackn,
                                 data_offset,
                                 flags,
                                 self.window)
        tcp_header += struct.pack('H', tcp_checksum) + \
            struct.pack('!H', self.urgp)
        return tcp_header + self.option + self.payload

    @staticmethod
    def unpack(packet):
        cflags = {  # Control flags
            32: "U",
            16: "A",
            8: "P",
            4: "R",
            2: "S",
            1: "F"}
        tcp = TCP()
        tcp.thl = (ord(packet[12]) >> 4) * 4
        tcp.options = packet[20:tcp.thl]
        tcp.payload = packet[tcp.thl:]
        tcph = struct.unpack("!HHLLBBHHH", packet[:20])
        tcp.srcp = tcph[0]  # source port
        tcp.dstp = tcph[1]  # destination port
        tcp.seq = tcph[2]  # sequence number
        tcp.ack = hex(tcph[3])  # acknowledgment number
        tcp.flags = ""
        for f in cflags:
            if tcph[5] & f:
                tcp.flags += cflags[f]
        tcp.window = tcph[6]  # window
        tcp.checksum = hex(tcph[7])  # checksum
        tcp.urg = tcph[8]  # urgent pointer
        return tcp

if __name__ == '__main__':
    tcpConfig = {}
    tcpConfig['srcp'] = 13987
    tcpConfig['dstp'] = 12341
    # port 65536
    tcpConfig['seq'] = 65536
    # seq number < 2**32 - 1
    tcpConfig['ack'] = 65537
    # 序号：占4个字节，是本报文段所发送的数据项目组第一个字节的序号
    # 在TCP传送的数据流中，每一个字节都有一个序号。
    # 例如，一报文段的序号为300，而起数据供100字节，
    # 则下一个报文段的序号就是400；
    # 确认序号：占4字节，是期望收到对方下次发送的数据的第一个字节的序号，
    # 也就是期望收到的下一个报文段的首部中的序号
    tcpConfig['offset'] = 0
    # Data offset: 4 bytes
    tcpConfig['reserved'] = 0
    tcpConfig['urg'] = 0
    tcpConfig['ack'] = 0
    tcpConfig['psh'] = 0
    tcpConfig['rst'] = 0
    tcpConfig['syn'] = 0
    tcpConfig['fin'] = 0
    tcpConfig['window'] = 8192
    tcpConfig['checksum'] = 0
    tcpConfig['urgp'] = 0
    tcpConfig['payload'] = ''

    tcp = TCP(tcpConfig)
    print tcp.pack()
