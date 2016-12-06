from json import loads

import tornado.web

from layer.mac import ETHER
from layer.ip import IP

class IPHandler(tornado.web.RequestHandler):

    def post(self):
        mac_config = loads(self.get_argument('mac'))
        ip_config  = loads(self.get_argument('ip'))
        # print mac_config, ip_config
        mac = ETHER(mac_config)
        ip = IP(ip_config)
        s = send(mac/ip, ip_config['dst'])
        print s
