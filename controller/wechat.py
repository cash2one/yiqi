# coding:utf-8
'''
Created on Dec 27, 2012

@author: xen
微信接口
'''

import web
import time

import model
import config
from modules import common

render = common.render('wechat')
db = web.config.db
msgDict = config.msgDict
session = web.config._session


class Query():
    '''
    POST(query)
    RETURN String
    '''
    def GET(self):
        data = web.input()
        if model.wechat.checkSignature(data):
            return data.echostr
        else:
            return None
    
    def POST(self):
        data = web.input()
        if not model.wechat.checkSignature(data):return None
        wmsg = model.wechat.getMsgObj(web.ctx.data)
        db.wmsg.insert(wmsg)
        
        content = wmsg['Content'] if wmsg.get('Content', '') else wmsg.get('Event')
        if content == 'news':
            wmsg['Articles'] = ['a', 'b', '1', '2', '3']
            return render.news(wmsg=wmsg)
        if content == 'test':
            return render.test(wmsg=wmsg)
        
        text = 'hello world'

        wmsg['CreateTime'] = time.time()
        wmsg['MsgType'] = 'text'
        wmsg['Content'] = text
        return render.text(wmsg=wmsg)
