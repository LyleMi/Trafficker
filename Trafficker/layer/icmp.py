import socket
import struct

from Trafficker.layer.layer import layer


class ICMP(layer):

    def __init__(self, icmp=None):
        if icmp is None:
            return
        self.type = icmp['type']
        self.code = icmp['code']
        self.checksum = icmp['checksum']
        self.ident = icmp['ident']
        self.seq = icmp['seq']
        self.payload = icmp['payload']

    def pack(self):
        icmpHeader = struct.pack('!BBHHH',
                                 self.type,
                                 self.code,
                                 0,
                                 self.ident,
                                 self.seq)
        self.checksum = self.calChecksum(icmpHeader)
        icmpHeader = struct.pack('!BBHHH',
                                 self.type,
                                 self.code,
                                 self.checksum,
                                 self.ident,
                                 self.seq)
        return icmpHeader + self.payload

    def json(self):
        return {
            'name': self.name,
            'type': self.type,
            'code': self.code,
            'ident': self.ident,
            'seq': self.seq
        }

    @classmethod
    def unpack(cls, packet):
        icmp = ICMP()
        packet, icmp.payload = packet[:8], packet[8:]
        data = struct.unpack('!BBHHH', packet)
        icmp.type = data[0]
        icmp.code = data[1]
        icmp.checksum = data[2]
        icmp.ident = data[3]
        icmp.seq = data[4]
        return icmp


if __name__ == '__main__':
    icmpConfig = {}
    icmpConfig['type'] = 0
    icmpConfig['code'] = 8
    icmpConfig['checksum'] = 0
    icmpConfig['ident'] = 0
    icmpConfig['seq'] = 0
    icmpConfig['payload'] = b''
    icmp = ICMP(icmpConfig)
    packet = icmp.pack()
    print(packet)
    print(icmp)
    print(ICMP.unpack(packet))
