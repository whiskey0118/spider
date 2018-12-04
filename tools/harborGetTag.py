import operator
from urllib import request
import ssl
import base64
import sys

#获取仓库中最新发布的tag标签

ssl._create_default_https_context = ssl._create_unverified_context
null=''

username = 'admin'
password = 'Zywl@123'
repoName=str(sys.argv[1])


def getAuth():
    a = username + ":" + password
    b = bytes(a.encode())
    return base64.b64encode(b)

#获取对应项目所有标签
def getTages(repoName):
    url = "https://harbor.zhiyingwl.java/api/repositories/"+repoName+"/tags?detail=1"
    header = {
        "Authorization": "Basic {}".format(getAuth().decode('utf-8')),
        "Content-Type": "application/json"
    }
    req = request.Request(url=url,headers=header)
    respone = request.urlopen(req)
    # print(type(respone.read()))
    tagList = respone.read().decode('utf-8')
    return eval(tagList)

#获取最新标签名
def getLastTagName(tagList):
    #按照时间排序
    s = sorted(taglist,key=operator.itemgetter('created'), reverse=True)
    for i in s:
        if i['name'] != 'latest':
            return i['name']

taglist = getTages(repoName)
name = getLastTagName(taglist)
print(name)

