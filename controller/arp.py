import tornado.web

from layer.mac import ETHER
from layer.ip import ARP
from utils.utils import send

class ARPHandler(tornado.web.RequestHandler):

    def post(self):
        mac = self.get_argument('mac')
        ip = self.get_argument('ip')
        tcp = self.get_argument('tcp')
        print mac, ip
        dst = '192.168.217.128'
        mac = ETHER(src="asdfgh", dst="lkjhgh")
        arp = ARP(srcp = 233, dstp=422)
        s = send(arp/mac/ip, dst)