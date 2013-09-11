#coding:utf-8
'''
Created on Oct 26, 2012

@author: xen
'''

from modules.qqweibo import APIClient

APP_KEY = '801246007' # app key
APP_SECRET = '5f76e3594632bc6caba8aa0e4dc037c0' # app secret
REDIRECT_URI = 'http://www.zobei.com/snslogin/qq' # callback url

client = APIClient(app_key=APP_KEY, app_secret=APP_SECRET, redirect_uri=REDIRECT_URI)
'''
第一步
'''
#print client.get_authorize_url()
#https://open.t.qq.com/cgi-bin/oauth2/authorize?redirect_uri=http%3A//www.zobei.com/snslogin/qq&response_type=code&client_id=801246007
'''
回调得
http://www.zobei.com/snslogin/qq?code=7060ec71ca77ebab2ce383c59936afba&openid=BF58E540BD6261C8C9B547252CE02966&openkey=115A2CA546A0D316D1443CE7405723C1&state=
'''

'''
第二步 根据回调获得code
访问获得 access_token
'''
#utl = 'https://open.t.qq.com/cgi-bin/oauth2/access_token?client_secret=5f76e3594632bc6caba8aa0e4dc037c0&client_id=801246007&redirect_uri=http://www.zobei.com/snslogin/qq&grant_type=authorization_code&code=3271e154ceebe8e68cf0e07a2380c24e'
#access_token=9fbda6e251a9374167449e420777c51b&expires_in=604800&refresh_token=98f58dfd97663217c5227b05283b345c&openid=bf58e540bd6261c8c9b547252ce02966&name=fenceer&nick=沈钰锋&state=

r = client.request_access_token('4ca41ac2dc996aca784d225a010895a0')
#{'openid': 'bf58e540bd6261c8c9b547252ce02966', 'name': 'fenceer', 'access_token': 'f8c24ba0e064ebd6907cb0f356ba3579', 'expires_in': 1356093690, 'nick': '\xe6\xb2\x88\xe9\x92\xb0\xe9\x94\x8b', 'state': '', 'refresh_token': 'bb97d2353c4db485ab1817e273f715a4'}
access_token = r.access_token # 新浪返回的token，类似abc123xyz456
expires_in = r.expires_in # token过期的UNIX时间
openid=r.openid
client.set_access_token(access_token, openid, expires_in)
print client.get.user__info(format='json')
#https://open.t.qq.com/api/user/info.json?access_token=5ee299162e2826be242508820b5daf56&openid=BF58E540BD6261C8C9B547252CE02966&oauth_consumer_key=801246007&scope=all&oauth_version=2.a?format=json
#client.set_access_token('f8c24ba0e064ebd6907cb0f356ba3579', 'bf58e540bd6261c8c9b547252ce02966', 1356093690)
#print client.post.t__add(format='json',content='腾讯微薄测试好但疼')

#https://open.t.qq.com/api/user/info?format=json&oauth_consumer_key=801246007&access_token=e03a9f20398f32afcc8d36dc0c899969&openid=BF58E540BD6261C8C9B547252CE02966&oauth_version=2.a&scope=all
#https://open.t.qq.com/api/user/info?format=json&access_token=e03a9f20398f32afcc8d36dc0c899969&openid=BF58E540BD6261C8C9B547252CE02966&oauth_consumer_key=801246007&scope=all&oauth_version=2.a


