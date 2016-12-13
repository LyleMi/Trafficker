from json import loads

import tornado.web

from layer.mac import ETHER
from layer.ip import IP
from layer.udp import UDP
from layer.layer import layer

class UDPHandler(tornado.web.RequestHandler):

    def post(self):
        mac_config = loads(self.get_argument('mac'))
        ip_config  = loads(self.get_argument('ip'))
        udp_config = loads(self.get_argument('udp'))
        mac = ETHER(mac_config)
        ip  = IP(ip_config)
        udp = UDP(udp_config)
        s = layer.send([mac, ip, udp])
        print s
        print s.recv(4096)