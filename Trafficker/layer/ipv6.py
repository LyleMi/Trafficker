import socket
import struct
from Trafficker.layer.layer import layer


class IPv6(layer):

    @classmethod
    def unpack(cls, packet):
        ipv6 = IPv6()
        iph = struct.unpack('!BBBBHBB16s16s', packet[:40])
        ipv6.version = iph[0] >> 4
        ipv6.length = iph[4]
        ipv6.nextHeader = iph[5]
        ipv6.hopLimit = iph[6]
        ipv6.srcip = iph[7]
        ipv6.dstip = iph[8]
        return ipv6

    @property
    def sip(self):
        return socket.inet_ntop(socket.AF_INET6, self.srcip)

    @property
    def dip(self):
        return socket.inet_ntop(socket.AF_INET6, self.dstip)
        return self.dstip

    def json(self):
        return {
            'version': self.version,
            'length': self.length,
            'src': self.sip,
            'dst': self.dip,
        }
