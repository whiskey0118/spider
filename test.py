from tasks.getHtml import parseComment,test2
import os

def test():
    mid = "4306001882880094"
    pageNiumber = "1"
    url = "http://weibo.com/aj/v6/comment/big?ajwvr=6&id={mid}&page={pageNiumber}".format(mid=mid,pageNiumber=pageNiumber)
    print(test2(url))

test()

