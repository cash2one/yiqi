#coding:utf-8
'''
Created on Oct 26, 2012

@author: xen
'''

from modules.renren import APIClient

APP_KEY = '0d67727289964ca5acb9e0315c34796b' # app key
APP_SECRET = '18560c0e05cd461884fd5884b0344fe2' # app secret
REDIRECT_URI = 'http://www.zobei.com/snslogin/renren' # callback url

client = APIClient(app_key=APP_KEY, app_secret=APP_SECRET, redirect_uri=REDIRECT_URI)

#print client.get_authorize_url(REDIRECT_URI)
url = 'https://graph.renren.com/oauth/authorize?client_id=0d67727289964ca5acb9e0315c34796b&redirect_uri=http://www.zobei.com/snslogin/renren&response_type=code&scope=status_update'


r = client.request_access_token('zI9bDprtLZHrDFSqNH6Jl1Q1h7sKFfvi')
#token = {'access_token': u'213871|6.b86851270c5837aacf8e9b3674982c79.2592000.1354111200-264228456', 'scope': u'read_user_status status_update', 'expires_in': 1354111203, 'user': {'id': 264228456, 'name': u'\u6c88\u94b0\u950b/\u807f', 'avatar': [{'url': u'http://hdn.xnimg.cn/photos/hdn111/20090411/22/40/head_6u0B_8635i204236.jpg', 'type': u'avatar'}, {'url': u'http://hdn.xnimg.cn/photos/hdn511/20090411/22/40/tiny_SBmk_8925d204236.jpg', 'type': u'tiny'}, {'url': u'http://hdn.xnimg.cn/photos/hdn111/20090411/22/40/main_KMIf_8635i204236.jpg', 'type': u'main'}, {'url': u'http://hdn.xnimg.cn/photos/hdn111/20090411/22/40/large_QAUb_8744c204236.jpg', 'type': u'large'}]}, 'refresh_token': u'213871|0.99o1DhQ6OYb4KmxE0ASyoIEgzeI1qUiL.264228456.1351340336889'}
access_token = r.access_token 
expires_in = r.expires_in 
# TODO: 在此可保存access token
client.set_access_token(access_token, expires_in)
snsUser = client.post.users__getInfo()
print snsUser
print client.post.status__set(status='人人api测试')



#client.set_access_token('213871|6.b86851270c5837aacf8e9b3674982c79.2592000.1354111200-264228456', 1354111203)

#print client.post.status__set(status='人人api测试')



