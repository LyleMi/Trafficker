import socket
import struct

from utils.utils import checksum
from layer import layer

class UDP(layer):

    def __init__(self, udp):
        self.src = udp['src']
        self.dst = udp['dst']
        self.payload = udp['payload']
        self.checksum = 0
        self.length = 8  # UDP Header length

    def pack(self, src, dst, proto=socket.IPPROTO_UDP):
        length = self.length + len(self.payload)
        pseudo_header = struct.pack('!4s4sBBH',
                                    socket.inet_aton(src),
                                    socket.inet_aton(dst), 0,
                                    proto, length)
        self.checksum = checksum(pseudo_header)
        packet = struct.pack('!HHHH', self.src, self.dst, length, 0)
        return packet
