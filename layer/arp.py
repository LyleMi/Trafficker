import socket
import struct

from utils.utils import checksum
from layer import layer

bcast_mac = 0xFFFFFFFFFFFF
zero_mac  = 0x000000000000
ARPOP_REQUEST = 0x0001
ARPOP_REPLY = 0x0002
HARDWARE_TYPE = 0x0001
PRO_TYPE = 0x0800
HARDWARE_SIZE = 0x0006
PRO_SIZE = 0x0004


class ARP(layer):

    def __init__(self, arp):
        self.arpop = arp["arpop"]
        self.sendermac = arp("sender_mac")
        self.senderip = arp("sender_ip")
        self.targetmac = arp("target_mac")
        self.targetip = arp("target_ip")

    def pack(self):
        arp = struct.pack('!HHBBH6s4s6s4s',
                               HARDWARE_TYPE,
                               PRO_TYPE,
                               HARDWARE_SIZE,
                               PRO_SIZE,
                               self.arpop,
                               self.sendermac,
                               self.senderip,
                               self.targetmac,
                               self.targetip,
                               )
        return arp

    def unpack(self, packet):
        arp = struct.pack('!HHBBH6s4s6s4s', packet)
        return arp