# coding:utf-8
'''
Created on Aug 11, 2012

@author: fenceer
'''
import os
import web

from modules import common, base, tools

render = common.render('test')
UPLOAD_DIR = 'static/upload/'
        
class LocalFile:
    '''
    上传文件
    GET()
        return test.upload()
    POST(Filename,Filedata,#dir)
        return json(filePath)
    '''
    def GET(self):
        return render.upload()
    def POST(self):
        data = web.input()
        upload_dir = UPLOAD_DIR + data.get('dir', 'temp') + '/'
        filePath = upload_dir + data.get('fname', tools.uniqueName()) + data.Filename[data.Filename.find('.'):]
        
        fileDir = filePath[:filePath.rfind('/')]
        if not os.path.exists(fileDir):os.makedirs(fileDir)
        
        fout = open(filePath, 'wb')
        fout.write(data.Filedata)
        fout.close()
        return base.rtjson(url='/' + filePath, state='SUCCESS')
