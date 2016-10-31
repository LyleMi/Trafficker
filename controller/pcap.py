import os
import tornado.web

class PCAPHandler(tornado.web.RequestHandler):

    def post(self):
        upload_path=os.path.join(os.path.dirname(__file__),'uploads')
        file = self.get_argument('file')
        filepath=os.path.join(upload_path,'test')
        with open(filepath,'wb') as up:
            up.write(meta['body'])
