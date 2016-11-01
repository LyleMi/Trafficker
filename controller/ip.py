import tornado.web

class IPHandler(tornado.web.RequestHandler):

    def post(self):
        mac = self.get_argument('mac')
        ip = self.get_argument('ip')
        print mac, ip
        ip = IP()