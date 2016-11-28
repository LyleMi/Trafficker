from json import loads

import tornado.web

from layer.mac import ETHER
from layer.ip import IP
from utils.utils import send

class IPHandler(tornado.web.RequestHandler):

    def post(self):
        mac_config = loads(str(self.get_argument('mac')))
        ip_config  = loads(self.get_argument('ip'))
        # print mac_config, ip_config
        dst = '192.168.217.128'
        mac = ETHER(mac_config)
        ip = IP(ip_config)
        s = send(mac/ip, dst)