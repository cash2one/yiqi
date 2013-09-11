# coding:utf-8
'''
Created on 2013-8-8

@author: Xen
'''
import urls
from modules import tools

'''
生成api文档
'''
ctrlSpace = []
apidocList = {}
for router in list(tools.group(urls.urls, 2)):
    url = router[0]
    controller = router[1]
    ctrlSpace.append(controller[:controller.find('.')])
    dot = controller.rfind('.')
    moduleName = controller[:dot]
    ctrlName = controller[dot + 1:]
    controlClass = tools.importName(moduleName, ctrlName)
    doc = controlClass.__doc__
    api = {
           'url':url,
           'controller':controller,
           'doc':''
           }
    if doc:
        docs = doc.split('\n')
        method = ''
        for d in docs:
            d = d.strip()
            if d.startswith('GET'):
                method = 'get'
                api['getargs'] = d[3:]
                api['getdoc'] = ''
            elif d.startswith('POST'):
                method = 'post'
                api['postargs'] = d[4:]
                api['postdoc'] = ''
            elif d != '':
                api[method + 'doc'] += d + '<br/>'
    if moduleName in apidocList:
        apidocList[moduleName].append(api)
    else:
        apidocList[moduleName] = [api]

ctrlSpace = list(set(ctrlSpace))
