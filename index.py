#!/usr/bin/env python
# coding:utf-8
'''
Created on Sep 21, 2012

@author: xen
project: tbwai
'''
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import web
import redis
import pymongo

import urls
from modules import rediswebpy

web.config.debug = False
# web.config.session_parameters.timeout = 6000 #100 Minutes
pool = redis.ConnectionPool(host='127.0.0.1', port=6379, db=1)
web.config.redis = redis.StrictRedis(connection_pool=pool)
web.config.mongo = pymongo.Connection('127.0.0.1', 27017)
# web.config.mongo.admin.authenticate('zobei.mdb', 'mdb27017')
web.config.db = web.config.mongo['yiqi']

app = web.application(urls.urls, globals())
web.config._session = web.session.Session(app, rediswebpy.RedisStore(), initializer={'uid': 0})

import appinit
app.add_processor(appinit.my_processor)
app.internalerror = appinit.internalerror
app.notfound = appinit.notfound

if __name__ == "__main__":
    web.wsgi.runwsgi = lambda func, addr = None: web.wsgi.runfcgi(func, addr)
    app.run()
