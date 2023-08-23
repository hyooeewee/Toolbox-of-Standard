#coding:utf-8
import random
import urllib
import ssl
import requests
import chardet
from bs4 import BeautifulSoup
from requests.exceptions import RequestException
import re
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

url = 'http://www.ccsn.org.cn/Zbbz/Show.aspx?Guid=fd20cb8b-3b1d-4dd5-90b1-cf20e22ac9f7'
headers = {
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Encoding':'gzip, deflate',
    'Accept-Language':'zh-CN,zh;q=0.9',
    'Cache-Control':'max-age=0',
    'Cookie':'ASP.NET_SessionId=r4i0fou0fqit00fn0ljeeznv',
    'Dnt':'1',
    'Host':'www.ccsn.org.cn',
    'Proxy-Connection':'keep-alive',
    'Sec-Gpc':'1',
    'Upgrade-Insecure-Requests':'1',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36 Edg/117.0.0.0'
}



if __name__ == "__main__":
    # T = requests.get(url).text
    # print(T)
    # print(str('爱你'.encode('GB2312')).split("'")[1].replace(r'\x', '%'))
    # print(BeiJing_get_all())
    ssl._create_default_https_context = ssl._create_unverified_context
    url = "https://zfcxjs.tj.gov.cn/ztzl_70/bzgf/xxbz/xxbzgf/"
    data = requests.get(url)
    print(data.status_code)