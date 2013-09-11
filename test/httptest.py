# coding:utf-8
'''
Created on 2013-9-4

@author: Xen
'''
import urllib2
import json
path = 'http://calc100.cn/mem/index.php/minterface/isMember'
# user_agent = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/29.0.1547.62 Safari/537.36'
# values = {'card_num' : '000951', 'phone' : '15'}
# headers = { 'User-Agent' : user_agent }
# data = urllib.urlencode(values)
# req = urllib2.Request(url, data, headers)
response = urllib2.urlopen(path + '?card_num=%s&phone=%s' % ('000951', '15158113021')) 
the_page = response.read()
obj = json.loads(the_page) 
obj = dict(obj)
print obj['result'], obj
