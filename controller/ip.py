import tornado.web

class IPHandler(tornado.web.RequestHandler):

    def post(self):
        self.write("Hello, world")
