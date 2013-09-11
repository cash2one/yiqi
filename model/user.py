# coding:utf-8
'''
Created on Oct 25, 2012

@author: xen
'''

import web
from modules import common, tools

db = web.config.db
rdb = web.config.redis
rpipe = rdb.pipeline()
render = common.render('user')
session = web.config._session
cookie_expires = 3 * 24 * 60 * 60

def login(user):
    if user:
        session.uid = user['_id']
        session.email = user['email']
        session.nick = user['nick']
        session.isVip = user['isVip']
        web.setcookie('al', tools.int2hex(user['_id']), cookie_expires)
    
def checkAuth(uid):
    if uid is not session.uid:
        return render.noAuth()
