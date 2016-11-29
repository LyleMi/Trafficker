#coding=utf-8

import socket
import struct

from utils.utils import checksum
from layer import layer

class TCP(layer):

    def __init__(self, tcp):
        self.srcp = tcp['srcp']
        self.dstp = tcp['dstp']
        self.seqn = tcp['seq']
        self.ackn = tcp['ack']
        self.offset = tcp['offset']  # Data offset: 5x4 = 20 bytes
        self.reserved = tcp['reserved']
        self.urg = tcp['urg']
        self.ack = tcp['ack']
        self.psh = tcp['psh']
        self.rst = tcp['rst']
        self.syn = tcp['syn']
        self.fin = tcp['fin']
        self.window = tcp['window']#socket.htons(5840)
        self.checksum = tcp['checksum']
        self.urgp = tcp['urgp']
        self.payload = tcp['payload']
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
        # pseudo header fields
        source_ip = self.source
        destination_ip = self.destination
        reserved = 0
        protocol = socket.IPPROTO_TCP
        total_length = len(tcp_header) + len(self.payload)
        # Pseudo header
        psh = struct.pack("!4s4sBBH",
                          source_ip,
                          destination_ip,
                          reserved,
                          protocol,
                          total_length)
        psh = psh + tcp_header + self.payload
        tcp_checksum = checksum(psh)
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
        return tcp_header

    def unpack(self, packet):
        cflags = {  # Control flags
            32: "U",
            16: "A",
            8: "P",
            4: "R",
            2: "S",
            1: "F"}
        _tcp = layer()
        _tcp.thl = (ord(packet[12]) >> 4) * 4
        _tcp.options = packet[20:_tcp.thl]
        _tcp.payload = packet[_tcp.thl:]
        tcph = struct.unpack("!HHLLBBHHH", packet[:20])
        _tcp.srcp = tcph[0]  # source port
        _tcp.dstp = tcph[1]  # destination port
        _tcp.seq = tcph[2]  # sequence number
        _tcp.ack = hex(tcph[3])  # acknowledgment number
        _tcp.flags = ""
        for f in cflags:
            if tcph[5] & f:
                _tcp.flags += cflags[f]
        _tcp.window = tcph[6]  # window
        _tcp.checksum = hex(tcph[7])  # checksum
        _tcp.urg = tcph[8]  # urgent pointer
        _tcp.list = [
            _tcp.srcp,
            _tcp.dstp,
            _tcp.seq,
            _tcp.ack,
            _tcp.thl,
            _tcp.flags,
            _tcp.window,
            _tcp.checksum,
            _tcp.urg,
            _tcp.options,
            _tcp.payload]
        return _tcp.list

if __name__ == '__main__':
    tcp_config = {}
    tcp_config['srcp'] = 13987
    tcp_config['dstp'] = 12341
    # port 65536
    tcp_config['seq']  = 65536
    # seq number < 2**32 - 1
    tcp_config['ack'] = 65537
    # 序号：占4个字节，是本报文段所发送的数据项目组第一个字节的序号
    # 在TCP传送的数据流中，每一个字节都有一个序号。
    # 例如，一报文段的序号为300，而起数据供100字节，
    # 则下一个报文段的序号就是400；
    # 确认序号：占4字节，是期望收到对方下次发送的数据的第一个字节的序号，
    # 也就是期望收到的下一个报文段的首部中的序号
    tcp_config['offset'] = 0
    # Data offset: 4 bytes
    tcp_config['reserved'] = 0
    tcp_config['urg'] = 0
    tcp_config['ack'] = 0
    tcp_config['psh'] = 0
    tcp_config['rst'] = 0
    tcp_config['syn'] = 0
    tcp_config['fin'] = 0
    tcp_config['window'] = 8192
    tcp_config['checksum'] = 0
    tcp_config['urgp'] = 0
    tcp_config['payload'] = ''

    tcp = TCP(tcp_config)
    print tcp.pack()