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
        self.sendermac = parseMac(arp["sendermac"])
        self.senderip =  socket.inet_aton(arp["senderip"])
        self.targetmac = parseMac(arp["targetmac"])
        self.targetip = socket.inet_aton(arp["targetip"])

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

    def send(self):
        packet = self.pack()
        hexdump(packet)
        s = socket.socket(socket.AF_INET, socket.SOCK_RAW)
        s.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)
        s.sendto(packet, (dst, 0))
        return s

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