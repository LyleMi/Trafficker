import socket
import struct

from utils.utils import checksum
from layer import layer


class ICMP(layer):

    def __init__(self, icmp):
        self.type = icmp["type"]
        self.code = icmp["code"]
        self.checksum = icmp["checksum"]
        self.unused = icmp["unused"]
        self.next_hop_mtu = icmp["next_hop_mtu"]

    def pack(self):
        return ''

    def unpack(self, packet):
        return []
