from tasks.getHtml import parseComment
from tasks.comment import comment
from tasks.getPagenumber import getPagenumber
import os
from tasks.commentSave import add_all

def test(mid,pageNiumber):
#     mid = "4306001882880094"
#     pageNiumber = "1"
    url = "http://weibo.com/aj/v6/comment/big?ajwvr=6&id={mid}&page={pageNiumber}".format(mid=mid,pageNiumber=pageNiumber)
    add_all(comment(url,mid))


mid = '4338464747095041'
pageNiumber = '1'
url = "http://weibo.com/aj/v6/comment/big?ajwvr=6&id={mid}&page={pageNiumber}".format(mid=mid,pageNiumber=pageNiumber)
pageNumber = getPagenumber(url)
for i in range(pageNumber):
    test(mid,i)

# getPagenumber(url)

