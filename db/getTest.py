from urllib import request
from http import cookiejar
from selenium import webdriver
import time
from lxml import etree
from requests.cookies import RequestsCookieJar
import requests
import json

# cookie = cookiejar.CookieJar()
# handler=request.HTTPCookieProcessor(cookie)
# print(type(handler))
# opener = request.build_opener(handler)
url = "https://www.zhiyingwl.com/passport/login"

def login(url):
    url = "https://www.zhiyingwl.com/passport/login"
    url2 = "https://www.zhiyingwl.com/lcs/#/study/course"
    driver = webdriver.Firefox()
    driver.get(url)
    driver.find_element_by_xpath('//input[@data-test = "test-account"]').send_keys("13138752530")
    driver.find_element_by_xpath('//input[@data-test = "test-password"]').send_keys("123456")
    driver.find_element_by_xpath('//button[@id="loginBtn"]').click()
    # print(driver.get_cookies())
    time.sleep(10)
    driver.get(url=url2)
    cookie = driver.get_cookies()
    with open('seleniumCookie.txt','w+') as f:
        json.dump(cookie,f)
    driver.close()

def weiboLogin():
    url = "https://weibo.com/login"
    driver = webdriver.Firefox()
    driver.get(url)
    driver.find_element_by_xpath('//input[@id="loginname"]').send_keys("whiskey0118@sina.com")
    driver.find_element_by_xpath('//input[@type="password"]').send_keys("Maozedong@123")
    driver.find_element_by_xpath('//span[@node-type="submitStates"]').click()
    print(driver.get_cookies())
    time.sleep(15)

# weiboLogin()
# zywlLogin()

login(url)
def xpathTest():
    # page = request.urlopen(url)
    # page = page.read().decode('utf-8')

    with open('test.html','r',encoding='utf-8') as f:
        # f.write(page)
        # f.close()
        page = f.read()
        f.close()
        selector = etree.HTML(page)
        print(selector.xpath('/'))

