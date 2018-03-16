# coding:utf-8
from url import url
import tornado.web
import os
import base64, uuid

settings = dict(
    template_path=os.path.join(os.path.dirname(__file__), "templates"),
    static_path=os.path.join(os.path.dirname(__file__), "static"),
    cookie_sercert=base64.b64encode(uuid.uuid4().bytes),
    xsrf_cookie=True,
    login_url='/',
)
application = tornado.web.Application(
    handlers=url,
    **settings
)
