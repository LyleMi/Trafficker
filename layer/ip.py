import socket
import struct

from random import randint

from utils.utils import checksum
from layer import layer


class IP(layer):

    def __init__(self, ip):
        self.version = ip['version']
        self.ihl = ip['ihl']  # Internet Header Length
        self.tos = ip['tos']  # Type of Service
        self.tl = 20 + len(ip['payload'])
        self.id = ip['id']  # random.randint(0, 65535)
        self.flags = ip['flags']  # Don't fragment
        self.offset = ip['offset']
        self.ttl = ip['ttl']
        self.protocol = ip['proto']
        self.checksum = ip['checksum']  # will be filled by kernel
        self.source = socket.inet_aton(ip['src'])
        self.destination = socket.inet_aton(ip['dst'])

    def pack(self):
        ver_ihl = (self.version << 4) + self.ihl
        flags_offset = (self.flags << 13) + self.offset
        ip_header = struct.pack("!BBHHHBBH4s4s",
                                ver_ihl,
                                self.tos,
                                self.tl,
                                self.id,
                                flags_offset,
                                self.ttl,
                                self.protocol,
                                self.checksum,
                                self.source,
                                self.destination)
        self.checksum = checksum(ip_header)
        ip_header = struct.pack("!BBHHHBBH4s4s",
                                ver_ihl,
                                self.tos,
                                self.tl,
                                self.id,
                                flags_offset,
                                self.ttl,
                                self.protocol,
                                socket.htons(self.checksum),
                                self.source,
                                self.destination)
        return ip_header

    def unpack(self, packet):
        _ip = layer()
        _ip.ihl = 20
        iph = struct.unpack("!BBHHHBBH4s4s", packet[:_ip.ihl])
        _ip.ver = iph[0] >> 4
        _ip.tos = iph[1]
        _ip.length = iph[2]
        _ip.ids = iph[3]
        _ip.flags = iph[4] >> 13
        _ip.offset = iph[4] & 0x1FFF
        _ip.ttl = iph[5]
        _ip.protocol = iph[6]
        _ip.checksum = hex(iph[7])
        _ip.src = socket.inet_ntoa(iph[8])
        _ip.dst = socket.inet_ntoa(iph[9])
        _ip.list = [
            _ip.ihl,
            _ip.ver,
            _ip.tos,
            _ip.length,
            _ip.ids,
            _ip.flags,
            _ip.offset,
            _ip.ttl,
            _ip.protocol,
            _ip.src,
            _ip.dst]
        return _ip.list

if __name__ == '__main__':

    ip_config = {}
    ip_config["version"] = 4 # version 4 or 6
    ip_config["ihl"] = 20 # header length
    ip_config["tos"] = 0 # type of service
    ip_config['payload'] = ''
    ip_config['id']  = randint(0, 65535)
    ip_config['flags'] = 2 # Don't fragment
    # three bit
    # bit 0 => reserved, must be zero
    # bit 1 => may fragment, 1 = don't fragment
    # bit 2 => last fragment, 1 = more fragment
    ip_config['offset'] = 0
    ip_config['ttl'] = 64 # 8 < ttl < 255
    ip_config['proto'] = 6
    ip_config['checksum']  = 0 # will be filled by kernel
    ip_config['src'] = '127.0.0.1'
    ip_config['dst'] = '127.0.0.1'
    ip = IP(ip_config)
    packet = ip.pack()
    print packet.encode('hex')
    print ip.unpack(packet)