# coding:utf-8
'''
Created on 2012-7-15

@author: Xen
'''

pre = 'controller.'
INTERCEPTOR = 'interceptor:'
local_interceptor = []

urls = [
        '/baseinfo'                         , pre + 'user.BaseInfo',
        '/vip/editInfo'                     , pre + 'user.VipEditInfo',
        '/huiyuan'                          , pre + 'user.Huiyuan',
        '/vip/activate'                     , pre + 'user.VipActivate',
        
        '/pay/page'                         , pre + 'netpay.PayPage',
]
