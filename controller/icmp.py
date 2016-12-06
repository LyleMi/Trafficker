from json import loads

import tornado.web

from layer.mac import ETHER
from layer.ip import IP
from layer.icmp import ICMP
from utils.utils import send

class ICMPHandler(tornado.web.RequestHandler):

    def post(self):
        mac_config = loads(self.get_argument('mac'))
        ip_config  = loads(self.get_argument('ip'))
        icmp_config = loads(self.get_argument('icmp'))
        mac = ETHER(mac_config)
        ip  = IP(ip_config)
        icmp = ICMP(icmp_config)
        s = send(icmp/mac/ip, dst)