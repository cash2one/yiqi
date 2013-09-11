# coding:utf-8
'''
Created on 2012-6-25

@author: Administrator
项目工具
'''
import string
from random import choice

AVATAR_PATH = 'static/upload/avatar/'
ACTIVITY_PATH = 'static/upload/activity/'
PAR_LOGO_PATH = 'static/upload/partner/'


def genRandomStr(length=8, chars=string.letters + string.digits):
    return ''.join([choice(chars) for i in range(length)])

def getAvatarPath(uid, size=0):
    if size == 0:
        return AVATAR_PATH + str(uid) + '.jpg'
    else:
        return AVATAR_PATH + str(size) + '/' + str(uid) + '.jpg'
    
def getActivityFM(album_id, typ):
    return ACTIVITY_PATH + 'fm/' + str(album_id) + '_' + typ + '.jpg'

def getPartnerLogo(partner_id, typ):
    return PAR_LOGO_PATH + 'logo/' + str(partner_id) + '_' + typ + '.jpg'
