#coding:utf-8
'''
Created on Nov 18, 2012

@author: xen
'''


import re

pattern = r'^(add|rem)$'

match = re.match(pattern, 'addr')
if match:
    print match.group()
else:
    print None
