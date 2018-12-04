import os
import sys

#kubernetes 中deployment的name
deploymentName = sys.argv[1]
#harbor中仓库的名字，如：java/api
repositoryName = sys.argv[2]
#yaml 文件的路径和名字
yamlDir = sys.argv[3]

cmd1 = "python36 /opt/jenkins/harborGetTag.py " + repositoryName
tag = os.popen(cmd1).read().strip()
# print(tag)
cmd2 = "kubectl get pods | grep " + deploymentName + " >/dev/null"
#命令执行成功返回0，不成功返回非0数字，即项目已经发布返回0，只需要更新版本。没有发布返回非0任意数字，需要找到路径新发布
projExist = os.system(cmd2)

deployCmd = "kubectl apply -f " + yamlDir
updateCmd = "kubectl set image deployment/"+ deploymentName + " " + deploymentName + "=harbor.zhiyingwl.java/"+ repositoryName + ":" + tag +" --record"
# print(updateCmd)
# print(deployCmd)
if projExist :
    os.system(deployCmd)
else:
    os.system(updateCmd)
