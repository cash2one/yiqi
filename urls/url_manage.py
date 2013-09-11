# coding:utf-8
'''
Created on 2012-7-15

@author: Xen
'''

pre = 'manage.'
INTERCEPTOR = 'interceptor:'
local_interceptor = []

urls = [
        '/m/index'                              , pre + 'admin.Index',
        '/m/changepwd'                          , pre + 'admin.ChangePwd',
        
        '/m/user/list/(vip|mem)'                , pre + 'user.List',
        '/m/user/(\d+)'                         , pre + 'user.Detail',
        '/m/user/setcard'                       , pre + 'user.SetCard',
        '/m/user/(\d+)/records'                 , pre + 'record.List',
        
        '/m/partner/list/(wh|ms|ss|sm|sh|all)'      , pre + 'partner.List',
        '/m/partner/add'                        , pre + 'partner.Add',
        '/m/partner/edit/(\d+)'                 , pre + 'partner.Edit',
        '/m/partner/delete/(\d+)'               , pre + 'partner.Delete',
        '/m/partner/(\d+)'                      , pre + 'partner.Detail',
        '/m/partner/(top|untop)'                , pre + 'partner.Top',
        
        '/m/activity/list'                      , pre + 'activity.List',
        '/m/activity/add'                       , pre + 'activity.Add',
        '/m/activity/edit/(\d+)'                , pre + 'activity.Edit',
        '/m/activity/delete/(\d+)'              , pre + 'activity.Delete',
        '/m/activity/(\d+)'                     , pre + 'activity.Detail',
        
        '/m/banner/add'                         , pre + 'banner.Add',
        '/m/banner/del'                         , pre + 'banner.Delete',
        '/m/banner/list'                        , pre + 'banner.List',
        
        '/m/comment/list'                       , pre + 'comment.List',
        '/m/comment/delete/(\d+)'               , pre + 'comment.Delete'

]
