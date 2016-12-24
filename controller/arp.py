from json import loads

import tornado.web

from layer.mac import ETHER
from layer.arp import ARP
from layer.layer import layer

class ARPHandler(tornado.web.RequestHandler):

    def post(self):
        mac_config = loads(self.get_argument('mac'))
        arp_config = loads(self.get_argument('arp'))
        mac = ETHER(mac_config)
        arp = ARP(arp_config)
        s = arp.send([mac, arp])
        print s
        # print s.recv(4096)
