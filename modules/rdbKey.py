# coding:utf-8
'''
Created on Nov 15, 2012

@author: xen
redis Key 管理
'''
from modules import tools



def globalHash():
    '''
    globalHash对象
        amc    上午接单数
        pmc    下午接单数
        wju    问卷调查url
    '''
    return 'GLOBAL'

def cartHash(uid):
    '''
    cartHash    用户购物车
        aid    商品标题
    '''
    return 'CART:' + tools.int2hex(uid)
