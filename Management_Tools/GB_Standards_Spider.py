#coding=utf-8
import datetime
import random
from time import sleep
import requests
from requests.exceptions import RequestException
import re
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

def IP_Pool():
    HTTP_IP = []
    HTTPS_IP = []
    count = 20  #一次获取的IP数量
    HTTP_response = requests.get("http://zltiqu.pyhttp.taolop.com/getip?count=" + str(count) + "&neek=87070&type=1&yys=0&port=1&sb=*&mr=1&sep=6")
    HTTP_IP_List = HTTP_response.text.split("*")
    HTTP_IP_List = HTTP_IP_List[:-1]
    for i in range(len(HTTP_IP_List)):
        HTTP_IP_List[i] = HTTP_IP_List[i].replace(" ","").replace("\r","").replace("\n","")
        resp = requests.get("https://www.baidu.com", proxies={"http": "http://" + HTTP_IP_List[i]})
        if resp.status_code ==200:
            HTTP_IP.append(HTTP_IP_List[i])
    sleep(1)
    HTTPS_response = requests.get("http://zltiqu.pyhttp.taolop.com/getip?count=" + str(count) + "&neek=87070&type=1&yys=0&port=2&sb=*&mr=1&sep=6")
    HTTPS_IP_List = HTTPS_response.text.split("*")
    HTTPS_IP_List = HTTPS_IP_List[:-1]
    for i in range(len(HTTPS_IP_List)):
        HTTPS_IP_List[i] = HTTPS_IP_List[i].replace(" ","").replace("\r","").replace("\n","")
        resp = requests.get("https://www.baidu.com", proxies={"http": "http://" + HTTPS_IP_List[i]})
        if resp.status_code == 200:
            HTTPS_IP.append(HTTPS_IP_List[i])
    total_list = [HTTP_IP,HTTPS_IP]
    return total_list

class URL_Requests : #随机的请求头，后边也可以改成字段随机组合的
    def Random_headers():
        headers_list = [{'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.162 Safari/537.36'},
                        {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'},
                        {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36'},
                        {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 Edg/115.0.1901.188'}
                        ]
        num = len(headers_list)
        return headers_list[random.randint(0,num-1)]
    def Random_IP(IP_List): #返回一个二维LIST，0是HTTP的，1是HTTPS的
        HTTP_proxies_IP = IP_List[0][random.randint(0,len(IP_List[0])-1)]
        HTTPS_proxies_IP = IP_List[1][random.randint(0, len(IP_List[1]) - 1)]
        proxies = {
            "http": "http://" + HTTP_proxies_IP,
            "https": "https://" + HTTPS_proxies_IP
        }
        return proxies
def GB_get_all():
    def GuoBiao_get_PDF(GB_URL, Guid, IP_List):
        try:
            headers = URL_Requests.Random_headers()
            proxies = URL_Requests.Random_IP(IP_List)
            response = requests.get(GB_URL, headers=headers, proxies=proxies, timeout=10)
            html = response.content
            try:
                if response.status_code == 200:
                    try:
                        URL = "http://www.ccsn.org.cn/Zbbz/ShowFullText.aspx" + str(Guid)
                        response = requests.get(URL, headers=headers, proxies=proxies, timeout=10)
                        html = response.content
                        html = html.decode('GB2312')
                        if str("暂无全文") in str(html):
                            return "无下载地址"
                        link_pattern = r'href="(.*?)"></a>'
                        link_matches = re.findall(link_pattern, html, re.S)
                        return str(link_matches[0])
                    except RequestException:
                        return "无下载地址"
            except:
                return "无下载地址"
            return "无下载地址"
        except RequestException:
            return "无下载地址"
    Proxies_IP_List = IP_Pool()
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
        if len(S_Date) > 6:  # 清洗日期数据，格式化显示，if避免空白内容
            S_Date = str(str(S_Date).split("/")[0] + "年" + str(S_Date).split("/")[1] + "月" + str(S_Date).split("/")[2] + "日")
        dizhi = 'http://www.ccsn.org.cn/Zbbz/Show.aspx' + matches[i][0]
        dizhi = GuoBiao_get_PDF(dizhi,matches[i][0],Proxies_IP_List)
        # {代码，标准名，开始时间，截止时间，当前状态，下载链接，区域，headers，更新时间}
        total_list.append([ID, Name , S_Date , "" ,"", dizhi , "国标", "" ,str(datetime.datetime.now())])
        print("数据为：" + ID +","+ Name +","+ S_Date +","+ "" +","+"现行"+","+ dizhi +","+ "国标" +","+str(datetime.datetime.now()))

    for i in range(int(int(total_page)-1)):
        Proxies_IP_List = IP_Pool()
        print("当前正在爬取第" + str(i+2) + "页，共计" + str(total_page) + "页")
        button = driver.find_element(By.XPATH, "//a[@id='ID_ucZbbzList_ucPager1_btnNext']")
        button.click()
        html = driver.page_source
        matches = re.findall(standards_pattern, html, re.S)
        for i in range(len(matches)):
            ID = matches[i][2]
            Name = matches[i][1]
            S_Date = matches[i][4]
            if len(S_Date) > 6:  # 清洗日期数据，格式化显示，if避免空白内容
                S_Date = str(str(S_Date).split("/")[0] + "年" + str(S_Date).split("/")[1] + "月" + str(S_Date).split("/")[2] + "日")
            dizhi = 'http://www.ccsn.org.cn/Zbbz/Show.aspx' + matches[i][0]
            dizhi = GuoBiao_get_PDF(dizhi,matches[i][0],Proxies_IP_List)
            # {代码，标准名，开始时间，截止时间，当前状态，下载链接，区域，headers，更新时间}
            total_list.append([ID, Name, S_Date, "", "现行", dizhi, "国标", "" ,str(datetime.datetime.now())])
            print("数据为：" + ID + "," + Name + "," + S_Date + "," + "" + "," + "" + "," + dizhi + "," + "国标" + "," + str(datetime.datetime.now()))
    driver.quit()
    return total_list


