# coding:utf-8
import tornado.web
import methods.readdb as mrd
from handlers.base import Basehandler
import tornado.escape


class userHandler(Basehandler):
    @tornado.web.authenticated
    def get(self, *args, **kwargs):
        # username = self.get_argument("user")
        username = tornado.escape.json_decode(self.current_user)
        user_infos = mrd.select_table(table="users", column="*", condition="username", value=username)
        self.render("user.html", users=user_infos)
