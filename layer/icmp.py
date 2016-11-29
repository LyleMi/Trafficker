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
        icmp_header = struct.pack("!BBHHHBBH4s4s",
                                self.type,
                                self.code,
                                self.checksum,
                                self.unused,
                                self.next_hop_mtu)
        self.checksum = checksum(icmp_header)
        icmp_header = struct.pack("!BBHHHBBH4s4s",
                                self.type,
                                self.code,
                                self.checksum,
                                self.unused,
                                self.next_hop_mtu)
        return icmp_header

    def unpack(self, packet):
        return []


if __name__ == '__main__':
    icmp_config = {}
    icmp_config["type"] = 2
    icmp_config["code"] = 'ff:ff:ff:ff:ff:ff'
    icmp_config["checksum"] = '127.0.0.1'
    icmp_config["unused"] = 'ff:ff:ff:ff:ff:ff'
    icmp_config["next_hop_mtu"] = '127.0.0.1'
    icmp = icmp(icmp_config)
    print icmp.pack()