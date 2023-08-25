#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :standards_spider.py
# @Time      :2023/02/20 13:40:11
# @Author    :Hughie Wei

import codecs
import json
import random
import re
import urllib

import chardet
import lxml
import pandas as pd
import requests
from bs4 import BeautifulSoup
from requests.exceptions import RequestException
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


def csres_get(keyword):
    '''工标网数据获取'''
    keyword =str(keyword.encode('GB2312')).split("'")[1].replace(r'\x', '%').replace(' ','+')
    url = f'http://doc.csres.com/s.jsp?keyword={keyword}'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.49'
    }
    response = requests.get(url=url, headers=headers)
    if response.status_code == 200:
        matches = []
        pattern = r'共有.*?条符合状态条件的标准，共(.*?)页'
        Num = re.findall(pattern, response.text, re.S)
        pattern = r'title="编号：(.*?) &#xA;标题：(.*?)&#xA;英文标题.*?发布日期.*?发布日期：(.*?)">.*? <td align=.*?<td ><font color.*?</font></td>.*?font color=.*?</font></td>.*?<td ><font color.*?>(.*?)</font></td>'
        for pageNum in range(int(Num[0])):
            url =  f'http://doc.csres.com/s.jsp?keyword={keyword}&pageNum={pageNum+1}'
            matches += re.findall(pattern, response.text, re.S)
        print(matches)
        return matches
    else: 
        return 0

class DB_data_get():
    def Beijing():
        total_list = []
        total_html = ""
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        # 创建 WebDriver 实例，传入选项
        driver = webdriver.Chrome(options=chrome_options)
        url = "http://bjjs.zjw.beijing.gov.cn/eportal/ui?pageId=53613181"
        driver.get(url)
        total_html = total_html + driver.page_source
        pattern = r'总记录数:(.*?),'
        # print(total_html)
        total_page = int(re.findall(pattern, driver.page_source, re.S)[0])
        for i in range(int(total_page/10)):
            target_title = "下一页"
            element = driver.find_element("xpath", f"//*[@title='{target_title}']")
            element.click()
            # print(driver.page_source)
            total_html = total_html + driver.page_source
        driver.quit()
        total_html_pattern = r'<tr><td>(.*?)</td>.*?href="(.*?)" target="_blank" title=".*?">(.*?)</a></td>.*?<td>.*?</td>.*?<td>.*?</td>.*?<td>(.*?)</td>'
        matches = re.findall(total_html_pattern, total_html, re.S)
        for i in range(len(matches)):
            bianhao = matches[i][0]
            biaoti = matches[i][2]
            DownloadLink = matches[i][1]
            StartDate = matches[i][3]
            total_list.append([bianhao, biaoti, StartDate, '', '现行', DownloadLink])
        # print(total_page)
        return total_list

    def Tianjin():
        html = []
        total_list = []
        result_list = []
        url = "https://zfcxjs.tj.gov.cn/ztzl_70/bzgf/xxbz/xxbzgf/"
        headers = {
            'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 7_1_2 like Mac OS X) App leWebKit/537.51.2 (KHTML, like Gecko) Version/7.0 Mobile/11D257 Safari/9537.53'
        }
        response = requests.get(url, headers=headers, verify=False)
        html = response.content
        # print(response.status_code)
        if response.status_code == 200:
            html =  response.text.encode('raw_unicode_escape').decode().replace(" ", "").replace("\n", "").replace("	", "")
            print(html)
            # print(type(html))
            pattern = r'varitem_.*?SYBT:"(.*?)",BT:"(.*?)",FBT:".*?DOCPUBURL:"(.*?)",'
            matches = re.findall(pattern, html, re.S)
            # print(matches)
            for i in range(len(matches)):
                bianhao = matches[i][0]
                biaoti = matches[i][1]
                dizhi = matches[i][2]
                total_list.append([bianhao,biaoti,'','','',dizhi])
        else:
            return total_list

    def Hebei():
        chrome_options = Options() # 实例化option对象
        chrome_options.add_argument("--headless") # 把Chrome浏览器设置为静默模式
        chrome_options.add_argument('--disable-gpu') # 禁止加载图片
        chrome_options.add_argument('log-level=3')
        driver = webdriver.Chrome(options=chrome_options) 
        browser = webdriver.Chrome(options=chrome_options)
        base_url = 'http://zfcxjst.hebei.gov.cn/hbzjt/ztzl/jj/gcjsgf/'
        standard_list = []
        for item in ['fwjz/', 'szgc/', 'czjs/', 'sxjs/', 'zjbz/']:
            item_url = base_url + item
            driver.get(item_url)    
            try:
                max_page = re.findall('index_(.*?).html', driver.find_element(By.CSS_SELECTOR, '#page_nav_list > a.pb_end_page').get_attribute('href'))[0]
            except:
                max_page = 1
            for i in range(1, int(max_page)+1):
                url = item_url + f"index_{i}.html"
                driver.get(url)
                elements = driver.find_elements(By.CSS_SELECTOR, '#number > li')
                for element in elements: 
                    # 标准编号，标准标题，实施日期，作废日期，标准状态，下载链接
                    standard = []
                    standard.append(element.find_element(By.CSS_SELECTOR, '#number > li > div.bianhao.pso > span').text)
                    standard.append(element.find_element(By.CSS_SELECTOR, '#number > li > div.mingcheng > a').text)
                    try:
                        standard.append(element.find_element(By.CSS_SELECTOR, '#number > li > div.riqi.pso > span').text)
                        standard.append('')
                        standard.append('现行')
                        href = element.find_element(By.CSS_SELECTOR, '#number > li > div.yulan.pso > span > a').get_attribute('href')
                        
                        browser.get(href)
                        standard.append(browser.find_element(By.CSS_SELECTOR, '#yanse > div.p_nei > div > span > div > iframe').get_attribute('src'))
                    except:
                        standard.append('')
                        standard.append('')
                        standard.append('')
                        standard.append('')
                    standard_list.append(standard)
                print(f'获取河北省地方标准第{i}/{max_page}页')
        driver.quit()
        browser.quit()
        return standard_list

    def Sanxi():
        pass

    def Neimenggu():
        pass

    def Liaoning():
        pass

    def Jilin():
        pass

    def Heilongjiang():
        pass

    def Shanghai():
        pass

    def Jiangsu():
        pass
    
    def ZheJiang():
        '''
        已知问题：
        1.实施时间可能不太对，之后再调整
        '''
        chrome_options = Options() # 实例化option对象
        chrome_options.add_argument("--headless") # 把Chrome浏览器设置为静默模式
        chrome_options.add_argument('--disable-gpu') # 禁止加载图片
        chrome_options.add_argument('log-level=3')
        url = "https://bz.zjamr.zj.gov.cn/public/std/list/DB/1.html"
        driver = webdriver.Chrome(options=chrome_options) 
        driver.get(url)    
        driver.implicitly_wait(5)
        # pattern = r'查询到相关标准(.*?)条'
        # total_page = int(re.findall(pattern, driver.page_source, re.S)[0])
        # print(total_page)
        max_page = driver.find_element(By.CSS_SELECTOR, '#layui-laypage-1 > a.layui-laypage-last').text
        # print(max_page)
        standard_list = []
        for i in range(1, int(max_page)+1):
            url = "https://bz.zjamr.zj.gov.cn/public/std/list/DB/{}.html".format(i)
            driver.get(url)
            elements = driver.find_elements(By.CSS_SELECTOR, '#dbDiv > div > div > div > ul')
            for element in elements[:-1]: 
                # 标准编号，标准标题，实施日期，作废日期，标准状态，下载链接
                standard = []
                standard.append(element.find_element(By.CSS_SELECTOR, 'span.list-gb').text)
                standard.append(element.find_element(By.CSS_SELECTOR, 'li.std_title').text.split('：')[-1])
                try:
                    standard.append(element.find_element(By.CSS_SELECTOR, 'span.bztm').text.split('：')[-1])
                    standard.append('')
                    standard.append(element.find_element(By.CSS_SELECTOR, 'span.liat-time').text)
                    standard.append(re.search('https:.*?.pdf', element.find_element(By.CSS_SELECTOR, 'a.list-yl').get_attribute('onclick')).group().replace('\/', '/'))
                except:
                    standard.append('')
                    standard.append('')
                    standard.append('')
                    standard.append('')
                standard_list.append(standard)
            print(f'获取浙江省地方标准第{i}/{max_page}')
        driver.quit()
        return standard_list

    def Anhui():
        pass

    def Fujian():
        pass

    def Jiangxi():
        pass

    def Shandong():
        pass

    def Henan():
        pass

    def Hubei():
        pass

    def Hunan():
        pass

    def Guangdong():
        pass

    def Guangxi():
        pass

    def Hainan():
        pass

    def Chongqing():
        pass

    def Sichuan():
        # from requests.exceptions import RequestException
        # import urllib
        SiChuan_URL = "http://jst.sc.gov.cn/scjst/bzgf/zhuanlan.shtml"
        data_list = []
        name_num = []
        result_list = []
        total_html = ""
        try:
            url = "http://jst.sc.gov.cn/scjst/bzgf/2023/3/13/ded7b643735240758041911d7f30f084.shtml"
            response = requests.get(url)
            if response.status_code == 200:
                soup = BeautifulSoup(response.content, "html.parser")                # 定位表格元素
                table = soup.find("table")                # 遍历表格行并提取数据
                for row in table.find_all("tr"):
                    row_data = [cell.get_text(strip=True) for cell in row.find_all(["th", "td"])]
                    data_list.append(row_data)
                data_list.pop(0)
                for i in range(len(data_list)): #清洗掉序号列
                    if len(data_list[i][0]) < 4:
                        data_list[i].pop(0)
                for i in range(len(data_list)): #清洗掉审批号列
                    if "J1" in data_list[i][0]:
                        data_list[i].pop(0)
                for i in range(len(data_list)): #清洗掉空白列
                    if len(data_list[i][0]) < 4:
                        data_list[i].pop(0)
                for i in range(len(data_list)): #清洗掉废止项
                    if data_list[i][4] == "废止":
                        continue
                    else:
                        temp_list = [data_list[i][0],data_list[i][1]]
                        name_num.append(temp_list) #清洗掉废止项
                # 以上为获取总目录及规范编号，以下为获取所有的链接
            url = "http://jst.sc.gov.cn/scjst/bzgf/zhuanlan.shtml"
            response = requests.get(url)
            if response.status_code == 200:
                total_html = total_html + response.text
            for i in range(8):
                url = "http://jst.sc.gov.cn/scjst/bzgf/zhuanlan" + "_" + str(int(i)+2) + ".shtml"
                response = requests.get(url)
                if response.status_code == 200:
                    total_html = total_html + response.text
            pattern = r'title=".*?" href="(.*?)" target="_blank".*?【四川.*?标准】(.*?)</a>'
            SiChuan_URL = re.findall(pattern, total_html, re.S)
            for i in range(len(name_num)):
                for j in range(len(SiChuan_URL)):
                    if str(name_num[i][1]) in str(SiChuan_URL[j][1]):
                        result_temp_list = [name_num[i][0], name_num[i][1], '', '', '', str('http://jst.sc.gov.cn' + SiChuan_URL[j][0])[:-6] + "/files/" + urllib.parse.quote(name_num[i][1], safe='') + ".pdf"]
                        break
                    else:
                        result_temp_list = [name_num[i][0], name_num[i][1], "", "", "", ""]
                result_list.append(result_temp_list)
            return result_list
            print(result_list)
        except RequestException:
            return result_list

    def Guizhou():
        pass

    def Yunnan():
        pass
    
    def Xizang():
        pass

    def Shanxi():
        pass

    def Gansu():
        pass

    def Qinghai():
        pass

    def Ningxia():
        pass

    def Xinjiang():
        pass

    def Taiwan():
        pass

    def Hongkong():
        pass

    def Macau():
        pass
        
    

def read_cell_data(sheet, i, j):
    try:
        value = sheet.iat[i, j]
        if value != None:
            return value, i, j
        else:
            return None
    except:
        pass

def wash_data(data):
    soup = BeautifulSoup(data, 'lxml')
    print(type(soup))
    # with open('soup.text', 'w+', encoding='utf-8') as fp:
    #     fp.write(str(soup))
    print(soup.find_all('.*?<font color="#000000">(.*?)</font>.*?'))
    



if __name__ == "__main__":
    # keyword_make
    # keyword = '信息技术'
    # keyword_str = str(keyword.encode('GB2312')).split("'")[1].replace(r'\x', '%').replace(' ', '+')
    # # 1.获取标准id
    # # 1.1.读取文件数据
    # # filename = input('请指定文件路径：')
    # filename = r'D:\Users\Hughi\OneDrive - hrbeu.edu.cn\Work2023\04.行政管理\01.标准更新\规范、规程、标准和图集资料\《2022年度现行规范、规程、标准和图集清单》.xls'
    # df = pd.ExcelFile(filename)
    # # sheet_name = input('请确认表格名称{}：'.format(df.sheet_names))
    # sheet_name = '施工标准'
    # sheet = df.parse(sheet_name)
    # # cell_loc = input('请输入单元格位置，如C6：')
    # # i = int(re.findall('[0-9]', cell_loc)[0])-1
    # # ord('A')=65
    # # j = ord(re.findall('[A-Za-z]', cell_loc)[0].upper())-65
    # # i,j = 5,2
    # # print(sheet.iat[i,j])
    # # 1.2 读取单元格数据
    # # count = 0
    # # id_list = {}
    # # while count <= 3:
    # #     if read_cell_data(sheet, i, j) != None:
    # #         value,i,j = read_cell_data(sheet, i, j)
    # #         id_list[value] = [i,j]
    # #     else:
    # #         count += 1
    # #     i += 1
    # # print(id_list)
    # id_list = {'GB50202-2018': [6, 2], 'GB50203-2011': [7, 2]}
    # for value, loc in id_list.items():
    #     # print(value,loc)
    #     data = csres_get(value)
    #     # print(data)
    #     wash_data(data)
    #     # with open('./standards/standerds.html', 'w+', encoding='utf-8') as fp:
    #     #     fp.write(data)
    #     break
    print(DB_data_get.Hebei())

