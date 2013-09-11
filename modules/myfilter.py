# coding:utf-8
'''
Created on 2012-9-21

@author: fenceer
'''

import web
import time
from datetime import datetime
from modules import util


db = web.config.db
rdb = web.config.redis
rpipe = rdb.pipeline()
session = web.config._session

def ftime(timestamp, fromat='%Y-%m-%d %H:%M:%S', short=True):
    timestamp = float(timestamp)
    if not short:
        return datetime.fromtimestamp(timestamp).strftime(fromat)

    fdate = ''
    diff = (time.time() - timestamp)
    if diff < (60 * 1):
        fdate = '刚刚'
    elif diff < (60 * 60 * 1):
        fdate = str(int(diff / 60)) + '分钟前'
    elif diff < (60 * 60 * 24 * 1):
        fdate = str(int(diff / (60 * 60))) + '小时前'
    elif diff < (60 * 60 * 24 * 7):
        fdate = str(int(diff / (60 * 60 * 24))) + '天前'
    else:
        fdate = datetime.fromtimestamp(timestamp).strftime(fromat)
    return fdate


def activityFM(album_id, typ):
    return '/' + util.getActivityFM(album_id, typ)

def partner(partner_id, typ):
    return '/' + util.getPartnerLogo(partner_id, typ)

filters = {
            'ftime':ftime,

            'activityFM':activityFM,
            
            'partner':partner
            
            }
