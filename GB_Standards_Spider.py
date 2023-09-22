import datetime
import random
import urllib
from time import sleep
import requests
import chardet
from bs4 import BeautifulSoup
from requests.exceptions import RequestException
import re
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

def IP_Pool():
    pass

class URL_Requests : #随机的请求头，后边也可以改成字段随机组合的
    def Random_headers():
        headers_list = [{'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.162 Safari/537.36'},
                        {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'},
                        {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36'},
                        {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 Edg/115.0.1901.188'}
                        ]
        num = len(headers_list)
        return headers_list[random.randint(0,num-1)]

def GB_get_all():
    total_list = []
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    # 创建 WebDriver 实例，传入选项
    driver = webdriver.Chrome(options=chrome_options)
    url = "http://www.ccsn.org.cn/Zbbz/ZbbzList.aspx?"
    driver.get(url)
    html = driver.page_source
    pattern = r'<span id="ID_ucZbbzList_ucPager1_lbRecordCount" style="color:Red;">(.*?)</span></td>'
    page_pattern = r'<span id="ID_ucZbbzList_ucPager1_lbPage">1/(.*?)</span></td>'
    total_piece = re.findall(pattern, driver.page_source, re.S)[0]
    total_page = re.findall(page_pattern, driver.page_source, re.S)[0]
    print("总计条数：" + total_piece)

    print("正在爬取第1页，共计"+ total_page + "页")
    standards_pattern = r'hlShowDetail" title="点击查看详细信息" class="Title-a" href="Show.aspx?(.*?)" ' \
                        r'target="_blank">(.*?)' \
                        r'</a>.*?lbStandardCode" style="display:inline-block;width:100%;">(.*?)' \
                        r'</span>.*?lbApprovalDate" style="display:inline-block;width:100%;">(.*?)' \
                        r'</span>.*?lbPerformDate" style="display:inline-block;width:100%;">(.*?)' \
                        r'</span>'
    matches = re.findall(standards_pattern, html, re.S)
    for i in range(len(matches)):
        ID = matches[i][2]
        Name = matches[i][1]
        S_Date = matches[i][4]
        dizhi = 'http://www.ccsn.org.cn/Zbbz/Show.aspx' + matches[i][0]
        print(dizhi)
        dizhi = GuoBiao_get_PDF(dizhi,matches[i][0])
        print(dizhi)
        # {代码，标准名，开始时间，截止时间，当前状态，下载链接，区域，headers，更新时间}
        total_list.append([ID, Name , S_Date , "" ,"现行", dizhi , "国标" ,str(datetime.datetime.now())])
        print("数据为：" + ID +","+ Name +","+ S_Date +","+ "" +","+"现行"+","+ dizhi +","+ "国标" +","+str(datetime.datetime.now()))

    for i in range(int(int(total_page)-1)):
        print("当前正在爬取第" + str(i+2) + "页，共计" + str(total_page) + "页")
        button = driver.find_element(By.XPATH, "//a[@id='ID_ucZbbzList_ucPager1_btnNext']")
        button.click()
        html = driver.page_source
        matches = re.findall(standards_pattern, html, re.S)
        for i in range(len(matches)):
            ID = matches[i][2]
            Name = matches[i][1]
            S_Date = matches[i][4]
            dizhi = 'http://www.ccsn.org.cn/Zbbz/Show.aspx' + matches[i][0]
            print(dizhi)
            dizhi = GuoBiao_get_PDF(dizhi,matches[i][0])
            print(dizhi)
            # {代码，标准名，开始时间，截止时间，当前状态，下载链接，区域，headers，更新时间}
            total_list.append([ID, Name, S_Date, "", "现行", dizhi, "国标", str(datetime.datetime.now())])
            print("数据为：" + ID + "," + Name + "," + S_Date + "," + "" + "," + "现行" + "," + dizhi + "," + "国标" + "," + str(datetime.datetime.now()))
        sleep(1)
    driver.quit()
    return total_list

def GuoBiao_get_PDF(GB_URL,Guid):
    try:
        headers = URL_Requests.Random_headers()
        response = requests.get(GB_URL, headers=headers)
        html = response.content
        try:
            html = html.decode('GB2312')
            if response.status_code == 200:
                if str("暂无全文") in str(html):
                    return "无下载地址"
                else:
                    try:
                        URL = "http://www.ccsn.org.cn/Zbbz/ShowFullText.aspx" + str(Guid)
                        print(URL)
                        response = requests.get(URL, headers=headers)
                        html = response.content
                        html = html.decode('GB2312')
                        # print(html)
                        link_pattern = r'<a class="media" href="(.*?)"></a>'
                        link_matches = re.findall(link_pattern, html, re.S)
                        return str(link_matches[0])
                    except RequestException:
                        return "无下载地址"
        except:
            return "无下载地址"
        return "无下载地址"
    except RequestException:
        return "无下载地址"
