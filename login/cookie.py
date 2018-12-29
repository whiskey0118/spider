from http import cookiejar
from urllib import request
from requests.cookies import RequestsCookieJar
import requests
import json


def saveCookie():
    url = "https://www.zhiyingwl.com/elp/"
    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:64.0) Gecko/20100101 Firefox/64.0",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
        "Accept-Encoding": "gzip, deflate, br",
        "Connection": "keep-alive",
    }
    cookieFilename = "cookie.txt"
    cookie = cookiejar.LWPCookieJar(filename=cookieFilename)
    handler = request.HTTPCookieProcessor(cookie)
    opener = request.build_opener(handler)

    req = request.Request(url=url,headers=header)
    respone = opener.open(req)
    cookie.save(ignore_discard=True, ignore_expires=True)
    for item in cookie:
        print('Name = ' + item.name)
        print('Value = ' + item.value)

# saveCookie()

def seleniumCookieTest():
    url = "http://www.zhiyingwl.com/elp/user/account-info"
    header = {
        "Host": "www.zhiyingwl.com",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:64.0) Gecko/20100101 Firefox/64.0",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
        "Accept-Encoding": "gzip, deflate, br",
        "Referer": "https://www.zhiyingwl.com/lcs/",
        "Connection": "keep-alive"
    }
    cookie = RequestsCookieJar
    cookieDict = dict()
    with open('seleniumCookie.txt','r') as f:
        cookies = json.load(f)
        for i in cookies:
            cookieDict[i["name"]] = i["value"]

    respone = requests.get(url,cookies = cookieDict,headers = header)
    respone.encoding='utf-8'
    print(respone.text)

seleniumCookieTest()
