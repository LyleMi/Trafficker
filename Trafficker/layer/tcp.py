import socket
import struct

from Trafficker.layer.layer import layer

'''
TCP Header Format

0                   1                   2                   3
0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|          Source Port          |       Destination Port        |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|                        Sequence Number                        |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|                    Acknowledgment Number                      |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|  Data |           |U|A|P|R|S|F|                               |
| Offset| Reserved  |R|C|S|S|Y|I|            Window             |
|       |           |G|K|H|T|N|N|                               |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|           Checksum            |         Urgent Pointer        |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|                    Options                    |    Padding    |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|                             data                              |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+

CWR Congestion Window Reduced
ECE ECN Echo
URG Urgent
ACK Acknowledgment
PSH Push
RST Reset the connection
SYN Synchronize sequence numbers to initiate a connection
FIN The sender of the segment is finished sending data to its peer

The TCP option values

1 byte kind, 1 byte length, n byte info

Kind    Length      Name
0       1           EOL
1       1           NOP
2       4           MSS
3       3           WSOPT 
4       2           SACK-Permitted
5       Var.        SACK
8       10          TSOPT
28      4           UTO
29      Var.        TCP-AO
253     Var.        Experimental
254 Var. Experimental
'''


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
        self.payload = tcp['payload']
        self.option = tcp['option']
        self.src = ""
        self.destination = ""

    def pack(self):
        data_offset = (self.offset << 4) + 0
        flags = self.fin + (self.syn << 1) + (self.rst << 2) + \
            (self.psh << 3) + (self.ack << 4) + (self.urg << 5)
        tcpHeader = struct.pack('!HHLLBBHHH',
                                self.srcp,
                                self.dstp,
                                self.seqn,
                                self.ackn,
                                data_offset,
                                flags,
                                self.window,
                                self.checksum,
                                self.urgp)
        tcpChecksum = self.calChecksum(tcpHeader)
        tcpHeader = struct.pack('!HHLLBBH',
                                self.srcp,
                                self.dstp,
                                self.seqn,
                                self.ackn,
                                data_offset,
                                flags,
                                self.window)
        tcpHeader += struct.pack('H', tcpChecksum) + \
            struct.pack('!H', self.urgp)
        return tcpHeader + self.option + self.payload

    @staticmethod
    def unpack(packet, datalen=0):
        cflags = {  # Control flags
            32: 'urg',
            16: 'ack',
            8: 'psh',
            4: 'rst',
            2: 'syn',
            1: 'fin'
        }
        tcp = TCP()
        tcph = packet.unpack('!HHLLBBHHH')
        tcp.srcp = tcph[0]  # source port
        tcp.dstp = tcph[1]  # destination port
        tcp.seqn = tcph[2]  # sequence number
        tcp.ackn = tcph[3]  # acknowledgment number
        tcp.thl = tcph[4] >> 2
        tcp.flags = []
        tcp.offset = 0
        tcp.urg = tcph[5] & 32
        tcp.ack = tcph[5] & 16
        tcp.psh = tcph[5] & 8
        tcp.rst = tcph[5] & 4
        tcp.syn = tcph[5] & 2
        tcp.fin = tcph[5] & 1
        for f in cflags:
            if tcph[5] & f:
                tcp.flags += [cflags[f]]
        tcp.window = tcph[6]  # window
        tcp.checksum = hex(tcph[7])  # checksum
        tcp.urgp = tcph[8]  # urgent pointer
        tcp.options = packet.get(tcp.thl - 20)
        tcp.payload = packet.get(datalen - (tcp.thl - 20))
        tcp.padding = packet.getremain()
        return tcp

    def json(self):
        return {
            'name': self.name,
            'src port': self.srcp,
            'dst port': self.dstp,
            'seq': self.seqn,
            'ack': self.ackn,
            'thl': self.thl,
            'flags': self.flags,
            'offset': self.offset,
            'window': self.window,
            'checksum': self.checksum,
            'urgp': self.urgp,
            'options': self.options,
            'payload': self.payload,
            'padding': self.padding,
        }

    def __repr__(self):
        return '<TCP %s -> %s, flags: [%s], seq=%s, ack=%s>' % (
            self.srcp,
            self.dstp,
            ", ".join(self.flags),
            self.seqn,
            self.ackn
        )


if __name__ == '__main__':
    tcpConfig = {}
    tcpConfig['srcp'] = 13987
    tcpConfig['dstp'] = 12341
    # port 65536
    tcpConfig['seq'] = 65536
    # seq number < 2**32 - 1
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
    tcpConfig['seqnumber'] = 0
    tcpConfig['acknumber'] = 0
    tcpConfig['option'] = b''
    tcpConfig['payload'] = b''

    tcp = TCP(tcpConfig)
    print(tcp.pack())
