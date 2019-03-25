import socket
import struct

from Trafficker.layer.layer import layer


class ETHER(layer):

    # /etc/ethertypes
    ethertypes = {
        'IPv4': 0x0800,
        'X25': 0x0805,
        'ARP': 0x0806,
        'FR_ARP': 0x0808,
        'BPQ': 0x08ff,
        'DEC': 0x6000,
        'DNA_DL': 0x6001,
        'DNA_RC': 0x6002,
        'DNA_RT': 0x6003,
        'LAT': 0x6004,
        'DIAG': 0x6005,
        'CUST': 0x6006,
        'SCA': 0x6007,
        'TEB': 0x6558,
        'RAW_FR': 0x6559,
        'AARP': 0x80F3,
        'ATALK': 0x809B,
        'VLAN': 0x8100,
        'IPX': 0x8137,
        'NetBEUI': 0x8191,
        'IPv6': 0x86DD,
        'PPP': 0x880B,
        'ATMMPOA': 0x884C,
        'PPP_DISC': 0x8863,
        'PPP_SES': 0x8864,
        'ATMFATE': 0x8884,
        'LOOP': 0x9000,
    }
    
    ethertypesR = {v: k for k, v in ethertypes.items()}

    def __init__(self, mac=None):
        if mac is None:
            return
        self.src = self.parseMac(mac['src'])
        self.dst = self.parseMac(mac['dst'])
        self.type = mac['type']

    def pack(self):
        ethernet = struct.pack('!6s6sH',
                               self.dst,
                               self.src,
                               self.type)
        return ethernet

    def json(self):
        return {
            'name': self.name,
            'src': self.srcmac,
            'dst': self.dstmac,
            'type': self.stype,
        }

    @staticmethod
    def unpack(packet):
        m = ETHER()
        ethernet = struct.unpack('!6s6sH', packet)
        m.dst = ethernet[0]
        m.src = ethernet[1]
        m.type = ethernet[2]
        return m

    @property
    def stype(self):
        return self.ethertypesR.get(self.type, 'unknown %d' % (self.type))

    @property
    def dstmac(self):
        return self.parseMac(self.dst, True)

    @property
    def srcmac(self):
        return self.parseMac(self.src, True)

    def __repr__(self):
        return '<MAC %s -> %s, %s>' % (
            self.srcmac,
            self.dstmac,
            self.stype
        )


if __name__ == '__main__':
    mac = ETHER({
        'dst': 'ff:ff:ff:ff:ff:ff',
        'src': '00:00:00:00:00:00',
        'type': 36864
    })
    packet = mac.pack()
    print(packet)
    print(mac.unpack(packet).pack())
