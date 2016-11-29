from json import loads

import tornado.web

from layer.mac import ETHER
from layer.ip import IP
from layer.tcp import TCP
from utils.utils import send

class TCPHandler(tornado.web.RequestHandler):

    def post(self):
        mac_config = loads(self.get_argument('mac'))
        ip_config  = loads(self.get_argument('ip'))
        tcp_config = loads(self.get_argument('tcp'))
        mac = ETHER(mac_config)
        ip  = IP(ip_config)
        tcp = TCP(tcp_config)
        s = send(tcp/mac/ip, dst)