from http import cookiejar
from urllib import request
from requests.cookies import RequestsCookieJar
import requests
import json
from selenium import webdriver
import time
from lxml import etree


def saveCookie():
    url = "https://www.zhiyingwl.com/lcs/#/study/course"
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


def seleniumCookieTest():
    url = "https://www.zhiyingwl.com/lcs/#/study/homework"
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

def weiboLogin():
    url = "https://weibo.com/login"
    url2 = "https://weibo.com/6460703487/profile?topnav=1&wvr=6&is_all=1"
    driver = webdriver.Firefox()
    driver.get(url)
    driver.find_element_by_xpath('//input[@id="loginname"]').send_keys("whiskey0118@sina.com")
    driver.find_element_by_xpath('//input[@type="password"]').send_keys("Maozedong@123")
    driver.find_element_by_xpath('//span[@node-type="submitStates"]').click()
    time.sleep(10)
    driver.get(url=url2)
    cookie = driver.get_cookies()
    driver.close()
    with open("weiboCookie.txt",'w+') as f:
        json.dump(cookie,f)
    return json.dumps(cookie)



def weiboLoginTest():
    url = "https://weibo.com/u/6460703487/home"
    header = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
        "Connection": "keep-alive",
        "Host": "account.weibo.com",
        "Referer": "https://weibo.com/6460703487/profile?topnav=1&wvr=6&is_all=1",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.80 Safari/537.36"
    }
    cookie = RequestsCookieJar
    cookieDict = dict()

    with open("weiboCookie.txt",'r') as f:
        cookies = json.load(f)
        for i in cookies:
            cookieDict[i["name"]] = i["value"]

    # cookies = json.loads(weiboLogin())
    # for i in cookies:
    #     cookieDict[i["name"]] = i["value"]

    respone = requests.get(url,cookies = cookieDict,headers = header)
    respone.encoding='utf-8'
    print(respone.text)


weiboLogin()
# weiboLoginTest()