from tasks.getHtml import parseComment
from tasks.comment import comment
import os
from tasks.commentSave import add_all

def test():
    mid = "4306001882880094"
    pageNiumber = "1"
    url = "http://weibo.com/aj/v6/comment/big?ajwvr=6&id={mid}&page={pageNiumber}".format(mid=mid,pageNiumber=pageNiumber)
    add_all(comment(url,mid))

test()

