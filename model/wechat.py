# coding:utf-8
'''
Created on 2012-12-27

@author: fenceer
'''
import web
import hashlib
from xml.dom import minidom
import config


msgDict = config.msgDict
db = web.config.db
URL = 'http://yiqi.hzedcm.com/wechat'
TOKEN = '123yiqi'

def getMsgObj(xdata):
    xobj = {}
    xdata = minidom.parseString(xdata)
    for node in xdata.getElementsByTagName('xml')[0].childNodes:
        if node.nodeName != '#text':
            xobj[node.nodeName] = getValue(xdata, node.nodeName)
    return xobj

def getValue(dom, key):
    child = dom.getElementsByTagName(key)[0].firstChild
    return child.data.strip() if child else ''

def checkSignature(data):
    ll = []
    ll.append(data.timestamp)
    ll.append(TOKEN)
    ll.append(data.nonce)
    ll.sort()
    ss = hashlib.sha1(''.join(ll)).hexdigest()
    return True if ss == data.signature else False

