import socket
import struct

from utils.utils import checksum
from layer import layer

ETH_P_IP = 0x0800  # Internet Protocol Packet
ETH_P_ARP = 0x0806


class ETHER(layer):

    def __init__(self, mac):
        # print type(mac)
        # print mac
        self.src = mac["src"].replace(':', '').decode('hex')
        self.dst = mac["dst"].replace(':', '').decode('hex')
        self.type = mac["type"]
        # print self.src
        # print self.dst

    def pack(self):
        ethernet = struct.pack('!6s6sH',
                               self.dst,
                               self.src,
                               self.type)
        return ethernet

    def unpack(self, packet):
        ethernet = struct.unpack('!6s6sH', packet)
        return ethernet

if __name__ == '__main__':
    mac = ETHER({"dst":"ff:ff:ff:ff:ff:ff","src":"00:00:00:00:00:00","type":36864})
    packet = mac.pack()
    print packet.encode('hex')
    print mac.unpack(packet)