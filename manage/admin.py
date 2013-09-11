# coding:utf-8
'''
Created on 2013-8-8

@author: Xen
'''
import web

from modules import common, base, rdbKey
import hashlib

db = web.config.db
rdb = web.config.redis
pipe = rdb.pipeline()
render = common.render('admin')
session = web.config._session

class Index:
    '''
    管理后台首页
    GET()
        return manage.index()
    '''
    def GET(self):
        pass
        return render.index();

class Login:
    '''
    用户登录
    GET(#call)
        return user.login()
    POST(username,password)
        return json()
    '''
    def GET(self):
        data = web.input()
        admin = db.manage.find_one({'username':'admin'})
        if admin is None:
            mpwd = hashlib.md5('admin').hexdigest() 
            db.manage.save({'username':'admin', 'password':mpwd});
        return render.login(call=data.get('call', ''))
    
    def POST(self):
        data = web.input()
        mpwd = hashlib.md5(data.password.strip()).hexdigest()
        user = db.manage.find_one({'username':data.username.strip(), 'password':mpwd})
        
        if user is None:
            return base.rtjson(100001)
        else:
            session.token = 'xqit'

        return base.rtjson()
        
class Logout:
    def GET(self):
        session.kill();
        raise web .seeother('/mlogin')
    

class ChangePwd:
    '''
    修改密码
    GET()
        return render.changePwd()
    POST(oldPwd,newPwd)
        return  json(20012-密码错误)
    '''
    def GET(self):
        pass
        return render.changePwd()
    def POST(self):
        data = web.input()
        m = hashlib.md5(data.oldPwd)
        password = m.hexdigest()
        user = db.manage.find_one({'username':'admin'})

        if user['password'] != password:
            return base.rtjson(20012)
        else:
            m = hashlib.md5(data.newPwd.strip())
            newPwd = m.hexdigest()
            print newPwd
            db.manage.update({'username':'admin'}, {'$set' : {'password' :newPwd}})
            return base.rtjson()

class Setting:
    def GET(self):
        setting = rdb.hgetall(rdbKey.globalHash())
        print 'setting..........', setting
        return render.setting(setting=setting)
    def POST(self):
        data = web.input()
        pipe.hset(rdbKey.globalHash(), 'amc', data.amc)
        pipe.hset(rdbKey.globalHash(), 'pmc', data.pmc)
        pipe.hset(rdbKey.globalHash(), 'wju', data.wju)
        pipe.execute()
        return base.rtjson()
