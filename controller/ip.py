import tornado.web

from layer.mac import ETHER
from layer.ip import IP
from utils.utils import send

class IPHandler(tornado.web.RequestHandler):

    def post(self):
        mac = self.get_argument('mac')
        ip = self.get_argument('ip')
        print mac, ip
        dst = '192.168.217.128'
        ip = IP(source='127.0.0.1', destination='192.168.217.128')
        mac = ETHER(src="asdfgh", dst="lkjhgh")
        s = send(mac/ip, dst)