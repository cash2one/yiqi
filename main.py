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


# 配置体系，整个web的所有资源全部在这里配置
web.config.session_parameters.timeout = 6000  # 100分钟
# web.config.session_parameters['cookie_domain'] = '.zobei.com'
pool = redis.ConnectionPool(host='192.168.1.131', port=6379, db=6)
web.config.redis = redis.StrictRedis(connection_pool=pool)
web.config.mongo = pymongo.Connection('192.168.1.131', 27017)
# web.config.mongo.admin.authenticate('zobei.mdb', 'mdb27017')
web.config.db = web.config.mongo['yiqi']

app = web.application(urls.urls, globals())

# store session for debug mode
if web.config.get('_session') is None:
#    web.config._session = web.session.Session(app, web.session.DiskStore('sessions'), {'count': 0})
    web.config._session = web.session.Session(app, rediswebpy.RedisStore(), initializer={'uid': 0})

import appinit
app.add_processor(appinit.my_processor)
# app.internalerror = appinit.internalerror
# app.notfound = appinit.notfound

if __name__ == "__main__":
#    web.wsgi.runwsgi = lambda func, addr=None: web.wsgi.runfcgi(func, addr)
    app.run()
