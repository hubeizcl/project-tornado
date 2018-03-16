# coding:utf-8
import tornado.web


class Basehandler(tornado.web.RequestHandler):
    def get_current_user(self):
        return self.get_secure_cookie("user")
