import requests
from login import cookieList
from bs4 import BeautifulSoup
import json

url = "http://weibo.com/aj/v6/comment/big?ajwvr=6&id=4191124690225260&page=1"
# url = "https://weibo.com/u/6460703487"

def getComment(url):
    # 在login获取cookie列表，抓取页面测试,返回一个respone字典
    header = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
        "Connection": "keep-alive",
        "Host": "weibo.com",
        "Referer": "https://d.weibo.com/?topnav=1&mod=logo&wvr=6",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.80 Safari/537.36"
    }

    cookieDict = dict()
    for i in cookieList:
        cookieDict[i["name"]] = i["value"]

    respone = requests.get(url,cookies = cookieDict,headers = header)
    result = respone.json().get('data')
    cont = result.get('html','')
    return cont

def parseComment(url):
    # with open('test.txt', 'r',encoding='utf-8') as f:
    #     cont = f.read()
    # cont = json.dumps(getComment(url), ensure_ascii=False)
    cont = getComment(url)
    soup = BeautifulSoup(cont,"lxml")
    # comment = page.find(attrs={"class": "WB_text"}).contents
    comment = soup.find(attrs={'node-type': 'comment_list'}).find_all(attrs={'class': 'list_li S_line1 clearfix'})
    return comment

# print(parseComment(url)[1])
# print(type(parseComment(url)))

# print(getComment(url))
# print(type(getComment(url)))

print(parseComment(url)[2].find(attrs={'class': 'WB_text'}).find('a').text)
for content in parseComment(url)[2].find(attrs={'class': 'WB_text'}).contents:
    first_colon = True
    if first_colon:
        if content.find('：') == 0:
            print(content.replace('：', '', 1))
            first_colon = False
    else:
        print(content)