import requests
from login import cookieList
import json

def getPagenumber(url):
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

    respone = requests.get(url, cookies=cookieDict, headers=header)
    page = json.loads(respone.text)
    number = page.get('data','').get('page','').get('totalpage',1)
    return number