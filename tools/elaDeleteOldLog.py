import os
import re
import time
import sys
from urllib import request

def getLog(day):
    timeStr = ""
    req = request.Request(url='http://127.0.0.1:9200/_cat/indices')
    page = request.urlopen(req).readlines()
    timeNow = int(time.time())
    timeDay = int(day) * 86400
    timeList1 = []
    timeList2 = []
    restr1 = re.compile('\d{4}.\d+.\d+')
    restr2 = re.compile('\d{4}-\d+-\d+')
    for i in page:
        i = i.decode('utf-8')
        if i.split():
            name = i.split()[2]
            # print(name)
        if restr1.findall(i):
            timeFormat = restr1.findall(i)[0]
            if '.' in timeFormat:
                # print(timeFormat)
                timeStruct = time.strptime(timeFormat, '%Y.%m.%d')
                timeTimestamp = int(time.mktime(timeStruct))
                # print(timeTimestamp)
                if timeNow - timeTimestamp > timeDay :
                    timeList1.append(name)
            elif '-' in timeFormat:
                timeStruct = time.strptime(timeFormat, '%Y-%m-%d')
                timeTimestamp = int(time.mktime(timeStruct))
                # print(timeTimestamp)
                if timeNow - timeTimestamp > timeDay :
                    timeList2.append(name)
    return timeList1 + timeList2

getLog(30)

def deleteOldLog():
    name = getLog(30)
    for i in name:
        url = "http://127.0.0.1:9200/" + i
        req = request.Request(url=url, method='DELETE')
        respone = request.urlopen(req).read()
        print(respone)

