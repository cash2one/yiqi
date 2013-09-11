# coding:utf-8
'''
Created on 2012-7-15

@author: Xen
'''

pre = 'controller.'
INTERCEPTOR = 'interceptor:'
local_interceptor = []

urls = [
        
        ''                                  , pre + 'user.Index',
        '/'                                 , pre + 'user.Index',
        '/product'                          , pre + 'spage.Product',
        '/school'                           , pre + 'spage.School',
        '/demo'                             , pre + 'spage.Demo',
        '/map'                              , pre + 'spage.Map',
        '/aboutUs'                          , pre + 'spage.AboutUs',
        
        '/wechat/bb'            , pre + 'wechat.Query',
        '/wechat'               , pre + 'wechat.Query',        
        
        '/mlogin'                           , 'manage.admin.Login',
        '/mlogout'                          , 'manage.admin.Logout',
        
        '/test'                             , pre + 'test.Test',
        '/apidoc'                           , pre + 'test.Apidoc',
        '/apidoc/(\w+)'                     , pre + 'test.Apidoc',
        '/apidoc/(\w+)/(\w+)'               , pre + 'test.Apidoc',
        
        '/upload'                           , pre + 'upload.LocalFile',
        '/code'                             , pre + 'verify.CodeNum'    

]
