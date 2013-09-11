# coding:utf-8
'''
Created on 2012-9-29

@author: fenceer
'''

'''
class Interceptor:
    def intercept(self, nextIntercept):
        if string:
            return string
        if json
            return json
        if ok
            return nextIntercept()
'''
import  web
import  model
from modules import   base, tools

db = web.config.db
session = web.config._session

class AutoLogin:
    '''
    自动登录
    '''
    def intercept(self, nextIntercept):
#        自动登录  所有非ajax请求过来 都要能够自动登录
#        ajax 请求必须先从页面登录
#        has uid?
#            yes - ->next
#                
#            no - ->cookie is  AutoLogin?
#                    yes - ->get cookie sessionid - ->login
#                    no - ->next

        environ = web.ctx.environ
        if environ.get('HTTP_X_REQUESTED_WITH') is None:
            if web.ctx.path in ['/login', '/logout', '/apidoc', '/register', '/mlogin']:
                web.setcookie('al', '', -1)
            elif not session.get('uid') and web.cookies().get('al') :
                uid = tools.hex2int(web.cookies().get('al'))
                user = db.user.find_one({'_id':uid})
                if user:
                    model.user.login(user)
                else:
                    raise web.seeother('/mlogin')
        
        return nextIntercept()
            
    
class CheckAuthority:
    '''
    权限认证
    '''
    def intercept(self, nextIntercept):
        if session.get('token') == 'xqit':
            return nextIntercept()
        else:
            environ = web.ctx.environ
            if environ.get('HTTP_X_REQUESTED_WITH') is None:
                raise web.seeother('/mlogin?call=' + web.ctx.path)
            else:
                return base.rtjson(20001, call=web.ctx.path)
    


