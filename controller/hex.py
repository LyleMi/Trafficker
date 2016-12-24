import tornado.web

from layer.layer import layer


class HEXHandler(tornado.web.RequestHandler):

    def post(self):
        data = self.get_argument('hex')
        l = layer(data.decode('hex'))
        s = layer.send([l])
        print s
        # print s.recv(4096)
