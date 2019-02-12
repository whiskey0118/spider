# from db import metadata,engine,session
# from login.cookie import weiboLogin
from tasks.comment import commentSaveToFile
#
# getPagenumber('http://weibo.com/aj/v6/comment/big?ajwvr=6&id=4338464747095041&page=1')
# # weiboLogin()

mid = '4306001882880094'
pageNiumber = '1'
url = "http://weibo.com/aj/v6/comment/big?ajwvr=6&id={mid}&page={pageNiumber}".format(mid=mid,pageNiumber=pageNiumber)
commentSaveToFile(url,mid)
