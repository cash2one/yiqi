#coding:utf-8
'''
Created on Aug 11, 2012

@author: fenceer
'''
import os
import web
from bson.objectid import ObjectId

from modules import imgUtil, util

db = web.config.db

def usePicture(imgs):
    for img in imgs:
        db.picture.update({'_id':ObjectId(img['picId'])}, {'$set':{'use':1}})
        
        
def cutAvatar(filePath, uid, box=None):
    img = imgUtil.imgCut(filePath, box)
    filePath = ''
    fileDir = ''
    for size in [(200, 200), (80, 80), (40, 40)]:
        filePath = util.getAvatarPath(uid, size[0])
        fileDir = filePath[:filePath.rfind('/')]
        if not os.path.exists(fileDir):os.makedirs(fileDir)
        imgUtil.resizeImg(img, size , filePath)        
        
        
