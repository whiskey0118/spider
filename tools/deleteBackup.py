#如果备份文件超过7个，删除时间较早的文件

import os
import sys

path = str(sys.argv[1])
#需要输入的参数为目录，如:/root/ssl

def tools():
    # getFile = 'etcd.csr  etcd-key.pem  etcd.pem  etcd-csr.json  ca.csr  ca-key.pem  ca.pem  ca-csr.json  ca-config.json'
    getFile = "ls -t {}".format(path)
    file = os.popen(getFile)
    file = file.read()
    rejectDir = ['','/proc','/','/bin','/usr/bin','/lib']
    a = file.split()
    if path in rejectDir:
        print("process are no allow running in {} path".format(path))
        return False
    else:
        if os.path.exists(path):
            while len(a) >7 :
                entireFile = "{path}/{name}".format(path=path,name = a[-1])
                print("Delete file {}".format(entireFile))
                os.popen('rm -rf {}'.format(entireFile))
                a.pop()

        else:
            print("{} no exist".format(path))
            return


tools()