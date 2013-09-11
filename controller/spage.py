# coding:utf-8
'''
Created on 2013-6-13

@author: Eva
'''

import web

from modules import common

db = web.config.db
render = common.render('spage')


class Home:
    '''
    主页
    GET()
    return spage.home()
    '''
    def GET(self):
        pass
        return render.home()
    
class Product:
    '''
    公司产品
    GET()
    return spage.product()
    '''
    def GET(self):
        pass
        return render.product()
    
class School:
    '''
    校园导航
    GET()
    return spage.school()
    '''
    def GET(self):
        pass
        return render.school()
    
class Demo:
    '''
    经典案例
    GET()
    return spage.demo()
    '''
    def GET(self):
        pass
        return render.demo()

class Map:
    '''
    百度地图
    GET()
    return spage.addr()
    '''
    def GET(self):
        pass
        return render.addr()
    
class AboutUs:
    '''
    关于我们
    GET()
    return spage.aboutUs()
    '''
    def GET(self):
        pass
        return render.aboutUs()

    
