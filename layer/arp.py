import socket
import struct

from utils.utils import checksum, parseMac
from layer import layer

ARPOP_REQUEST = 0x0001
ARPOP_REPLY = 0x0002
HARDWARE_TYPE = 0x0001
PRO_TYPE = 0x0800
HARDWARE_SIZE = 0x0006
PRO_SIZE = 0x0004


class ARP(layer):

    def __init__(self, arp):
        self.arpop = arp["arpop"]
        self.sendermac = parseMac(arp["sender_mac"])
        self.senderip =  socket.inet_aton(arp["sender_ip"])
        self.targetmac = parseMac(arp["target_mac"])
        self.targetip = socket.inet_aton(arp["target_ip"])

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
        arp = struct.unpack('!HHBBH6s4s6s4s', packet)
        return arp

if __name__ == '__main__':
    arp_config = {}
    arp_config["arpop"] = ARPOP_REQUEST
    # 1 request
    # 2 reply
    arp_config["sender_mac"] = 'ff:ff:ff:ff:ff:ff'
    arp_config["sender_ip"] = '127.0.0.1'
    arp_config["target_mac"] = 'ff:ff:ff:ff:ff:ff'
    arp_config["target_ip"] = '127.0.0.1'
    arp = ARP(arp_config)
    packet = arp.pack()
    print packet
    print arp.unpack(packet)