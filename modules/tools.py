# coding:utf-8
'''
Created on 2013-8-8

@author: Xen
'''

import time
import random

def int2hex(num):
    return str(hex(int(num))).replace('0x', '').replace('L', '')

def hex2int(shex):
    return int('0x' + shex, 16)

def str2intList(strList):
    intList = [int(s) for s in strList]
    return intList

def hex2intList(hexList):
    intList = [hex2int(shex) for shex in hexList]
    return intList

def group(lst, block):
    return [lst[i:i + block] for i in range(0, len(lst), block)]

def uniqueName():
    t = time.time()
    r = random.randint(1, 10000)
    s1 = str(hex(int(t * 1000))).replace('0x', '').replace('L', '')
    s2 = str(hex(r)).replace('0x', '')
    name = s2 + s1
    return name

def importName(modulename, name):
    try:
        module = __import__(modulename, fromlist=[name])
    except ImportError, e:
        print 'import', modulename, e
        return None
    return getattr(module, name)

