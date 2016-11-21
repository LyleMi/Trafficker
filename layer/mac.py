import socket
import struct

from utils.utils import checksum
from layer import layer

ETH_P_IP = 0x0800  # Internet Protocol Packet
ETH_P_ARP = 0x0806

class ETHER(layer):

    def __init__(self, mac):
        self.src = mac['src']
        self.dst = mac['dst']
        self.type = mac['type']

    def pack(self):
        ethernet = struct.pack('!6s6sH',
                               self.dst,
                               self.src,
                               self.type)
        return ethernet

    def unpack(self, packet):
        ethernet = struct.pack('!6s6sH', packet)
        return ethernet
