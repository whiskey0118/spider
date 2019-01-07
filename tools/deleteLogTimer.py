import os
import re
import time
import sys


#删除多少天前的文件，不删除目录，path是文件的目录，day是删除多少天前的文件

path=str(sys.argv[1])
#第一个输入的参数是目录，如：/root/web/web
day=int(sys.argv[2])
#第二个输入的参数需要删除多少天前的文件   如：7

def reTest(path,day):
    cmd = "ls -lt --time-style '+%s'" + ' ' + path
    file = os.popen(cmd=cmd)
    result = []
    for line in file.readlines():
        lineList=line.split()
        if len(lineList) >= 6 :
            timestampFile = int(line.split()[5])
            timestampNow = int(time.time())
            timestampTotal = int(day) * 86400
            num=timestampNow - timestampFile
            if num > timestampTotal :
                result.append(lineList[6])
    return result

def deleteFile(path):
    log = []
    if reTest(path, day):
        for file in reTest(path, day):
            fileName = path + '/' + file
            if os.path.isfile(fileName):
                cmd = 'rm -rf ' + fileName
                os.popen(cmd)
                log.append(fileName)
        return log
                # print('{file} already delete'.format(file = fileName))
    else:
        sys.exit(0)

# deleteFile(path)

notAllowDir = ['','/proc','/','/bin','/usr/bin','/lib']
if path.strip() in notAllowDir :
    print('输入的参数不能为空！！！,或者不能是{a}目录,有删除系统文件的风险！！'.format(a = path.strip()))
    sys.exit(1)
else:
    log=deleteFile(path)
    time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    if log:
        with open('/opt/deleteOldFile/deleteFileLog.txt','a+') as f:
            for i in log:
                line = time + ' 删除 ' +str(i) + ' ' + '\n'
                f.write(line)
    else:
        print("没有文件被删除")
