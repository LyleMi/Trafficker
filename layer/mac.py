import socket
import struct

from utils.utils import checksum
from layer import layer

ETH_P_IP = 0x0800  # Internet Protocol Packet


class ETHER(layer):

    def __init__(self, src, dst, type=ETH_P_IP):
        self.src = src
        self.dst = dst
        self.type = type

    def pack(self):
        ethernet = struct.pack('!6s6sH',
                               self.dst,
                               self.src,
                               self.type)
        return ethernet
