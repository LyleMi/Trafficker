from json import loads

import tornado.web

from layer.mac import ETHER
from layer.ip import IP
from layer.tcp import TCP
from layer.layer import layer

class TCPHandler(tornado.web.RequestHandler):

    def post(self):
        mac_config = loads(self.get_argument('mac'))
        ip_config  = loads(self.get_argument('ip'))
        tcp_config = loads(self.get_argument('tcp'))
        mac = ETHER(mac_config)
        ip  = IP(ip_config)
        tcp = TCP(tcp_config)
        s = layer.send([mac,tcp,ip])        
        print s
        print s.recv()