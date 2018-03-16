# coding:utf-8
from handlers.base import Basehandler
import time
import tornado.web


class SleepHandler(Basehandler):
    @tornado.web.asynchronous
    def get(self):
        time.sleep(17)
        self.render("sleep.html")


class SeeHandler(Basehandler):
    def get(self):
        self.render("see.html")
