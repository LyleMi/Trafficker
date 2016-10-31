import tornado.web

class IPHandler(tornado.web.RequestHandler):

    def post(self):
        mac = self.get_argument('mac')
        self.write(mac)
        ip = self.get_argument('ip')
        self.write(ip)