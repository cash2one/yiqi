# coding:utf-8
'''
Created on Oct 25, 2012

@author: xen
'''
import re
import json
import time
import hashlib
import pymongo
from xml.dom import minidom
import datetime
from bson.objectid import ObjectId

from modules import util, rdbKey
import redis
import pprint 

mdb = pymongo.Connection('192.168.1.131', 27017)
db = mdb['tbwai']

rdb = redis.StrictRedis(host='192.168.1.131', port=6379, db=2)
pipe = rdb.pipeline()

# rdb.hset(rdbKey.cartHash(100000), '123457', 'value')
# 
# cart = rdb.hgetall(rdbKey.cartHash(100000))
# 
# print cart

# print db.user.update({}, {'$set':{'card':''}}, False, True)



'''模式匹配校验'''
# pattern = {
#            'phone'  : ur'^\d{10,15}$',
#            'name'   : ur'^[\u4e00-\u9fa5\w]{2,12}$',
#            'desc'   : ur'^.{0,4}$',
#            'type'   : None
#          }

# regex = ur'^.{2,12}$'
# value = '中国人%＆……%?0123'
# match = re.match(regex, value.decode('utf8'))
# if match:
#    print match
# else:
#    print 'n'

# print db.test.insert({'_id':123456, 'ii':123, 'value':'vv'})
# print db.test.update({'ii':12356699}, {'$set':{'value':'bb'}}, True)
# print db.test.find_and_modify({'ii':12344}, {'$set':{}}, True, new=True)
# m = hashlib.md5('')
# print m.hexdigest()

query = ''

vip = {
      'name':'aa',
      'aa':'bb'
      }

query = "&".join([k + '=' + str(v) for k, v in vip.items()])
print query
