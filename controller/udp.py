import tornado.web

from layer.mac import ETHER
from layer.ip import IP
from layer.udp import UDP
from utils.utils import send

class UDPHandler(tornado.web.RequestHandler):

    def post(self):
        mac = self.get_argument('mac')
        ip = self.get_argument('ip')
        tcp = self.get_argument('tcp')
        print mac, ip
        dst = '192.168.217.128'
        mac = ETHER(src="asdfgh", dst="lkjhgh")
        ip = IP(source='127.0.0.1', destination='192.168.217.128')
        udp = UDP(srcp = 233, dstp=422)
        s = send(udp/mac/ip, dst)