# coding:utf-8
'''
Created on Oct 24, 2012

@author: xen
'''

import os
import web

import model
from modules import base, common

db = web.config.db
render = common.render('test')
session = web.config._session

class Test:
    '''
    测试类
    GET(id)
        return render.test(user,ss)
    POST(username,pwd)
        return json(user)
    '''
    def GET(self):
        data = web.input()
        user = db.test.find_one({'_id':int(data.get('id', 0))})
        if user is None:
            raise web.notfound('the user is not found')
        return render.test(user=user, ss=model.test.getSession())

    def POST(self):
        data = web.input()
        user = {
              '_id':base.getLastID('test'),
              'username':data.username,
              'pwd':data.pwd
              }
        db.test.insert(user)
        return base.rtjson(user=user)


class Apidoc:
    def GET(self, space='controller', module=None):
        from modules import ctrldoc
        apidoc = []
        modules = []
        ctrlSpace = ctrldoc.ctrlSpace
        apidocList = ctrldoc.apidocList
        for f in os.listdir(os.path.dirname(__import__(space).__file__)):
            module_name, ext = os.path.splitext(f)
            if not module_name.startswith('__') and ext == '.py':
                modules.append(module_name)
        
        moduleName = space + '.' + module if module else space
        if moduleName in apidocList:
            apidoc = apidocList[moduleName] 
        else:
            for api in apidocList:
                if api.startswith(space):
                    apidoc += apidocList[api]
        
        return render.apidoc(ctrlSpace=ctrlSpace, modules=modules, apidoc=apidoc, space=space, module=module)
        
    
