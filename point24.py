#encoding:utf-8
import os,sys

import random
import time
import json

import tornado.ioloop
import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        n1 = int(self.get_argument('n1', '0'))
        n2 = int(self.get_argument('n2', '0'))
        n3 = int(self.get_argument('n3', '0'))
        n4 = int(self.get_argument('n4', '0'))

        ret = tw_get_24_point(n1,n2,n3,n4)
        resp = json.dumps(ret)
        self.write(resp)

    def post(self):
    	self.write("Hello, world")

        self.write(resp)

application = tornado.web.Application([
    (r"/get24", MainHandler),
])

# 获得24点
def tw_get_24_point(n1,n2,n3,n4):
	from xcx24 import get_24_point
	ret = get_24_point(n1,n2,n3,n4)
	return ret

if __name__ == '__main__':
	port = 8000
	application.listen(port)
	tornado.ioloop.IOLoop.instance().start()
