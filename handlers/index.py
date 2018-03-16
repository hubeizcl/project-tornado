# coding:utf-8
import tornado.web
import methods.readdb as mrd
from handlers.base import Basehandler
import tornado.escape


class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        username = mrd.select_table(table="users", column="username")
        one_user = username[0][0]
        self.render("index.html", user=one_user)

    def post(self, *args, **kwargs):
        username = self.get_argument("username")
        password = self.get_argument("password")
        user_infos = mrd.select_table(table="users", column="*", condition="username", value=username)
        if user_infos:
            db_pwd = user_infos[0][2]
            if db_pwd == password:
                self.set_secure_cookie(username, db_pwd, httpOnly=True, secure=True)
                self.write(username)
            else:
                self.write("you password was not right")
        else:
            self.write("There is not user.")

    def set_current_user(self, user):
        if user:
            self.set_secure_cookie('user', tornado.escape.json_encode(user))
        else:
            self.clear_cookie("user")


class Errorhandler(Basehandler):
    def get(self):
        self.render("error.html")
