# coding:utf-8
'''
Created on 2012-7-21

@author: Xen
'''
import re
import web
import json
from bson.objectid import ObjectId

import config
db = web.config.db

errorDesc = config.errorDesc

def getLastID(name):
    # 获取某个集合的自增ID
    ids = db['ids'].find_and_modify(query={'name':name}, update={'$inc':{'id':1}})
    if ids:
        return ids['id']
    else:
        db['ids'].insert({'name':name, 'id':100000})
        return db['ids'].find_and_modify(query={'name':name}, update={'$inc':{'id':1}})['id']
    
def rtjson(code=1, **args):
    '''return json'''
    if code == 1:
        args['status'] = 1
    else:
        args['status'] = 0
        args['error_code'] = code
        args['msg'] = errorDesc.get(code)
        
    return json.dumps(args)

def rtjsonp(callback, **args):
    '''return jsonp'''
    # web.header('Access-Control-Allow-Origin', '*') 
    return callback + '(' + json.dumps(args) + ');'

def checkData(data, pattern):
    '''数据正则校验'''
    errorValue = []
    for key, regex in pattern.items():
        value = data.get(key)
        if value is None:
            errorValue.append((key, 'null'))
        elif regex:
            match = re.match(regex, value.decode('utf8'))
            if match is None:
                errorValue.append((key, 'error'))
                
    return errorValue

def cpage(total, pagenum=1, pagesize=20):
    pagenum = int(pagenum)
    ptotal = 0
    if total % pagesize != 0:
        ptotal = total / pagesize + 1
    else:
        ptotal = total / pagesize
    re = {
          'pagesize': pagesize,
          'pagenum' : pagenum,  # 请求页码
          'total'   : total,  # 记录总数
          'ptotal'  : int(ptotal),  # 页数 
          'start'   : (pagenum - 1) * pagesize,
          'end'     : pagenum * pagesize - 1
          }
    return re

def pageList(docs, pagenum=1, pagesize=20):
    pager = cpage(docs.count(), pagenum, pagesize)
    docList = list(docs.skip(pager['start']).limit(pager['pagesize']))
    return docList, pager

def pageList_bak(data, collection, query, pagesize=20):
    pageSize = int(pagesize)
    pid = data.get('pid')
    pagenum = int(data.get('pagenum', 1))  # 请求页码
    curnum = int(data.get('curnum', 1)) if pid else 1  # 如果没有ID 则当前页为1
    
    pager = cpage(collection.find(query).count(), pagenum, pageSize)
    if pagenum < curnum:
        skip = (curnum - pagenum - 1) * pageSize
        query['_id'] = {'$gt':ObjectId(pid)}
        cs = collection.find(query).sort('_id', 1).skip(skip).limit(pageSize)
        cList = list(cs)[::-1]
    else:
        skip = (pagenum - curnum) * pageSize
        query['_id'] = {'$lte':ObjectId(pid)}
        cs = collection.find(query).sort('_id', -1).skip(skip).limit(pageSize)
        cList = list(cs)
        
    if len(cList) > 0:
        pager['pid'] = cList[0]['_id']
    
    return cList, pager
