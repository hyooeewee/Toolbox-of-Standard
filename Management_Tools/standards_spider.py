# -*- coding:utf-8 -*-
# @FileName  :standards_spider.py
# @Time      :2023/02/20 13:40:11
# @Author    :Hughie Wei

import codecs
import json
import random
import re
import time
import urllib
import datetime
import chardet
import lxml
import pandas as pd
import requests
from bs4 import BeautifulSoup
from requests.exceptions import RequestException
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import locale
locale.setlocale(locale.LC_ALL, 'zh_CN.UTF-8')

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
    def Beijing():  #按照新格式更新完成，日期已格式化
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
        total_page = int(re.findall(pattern, driver.page_source, re.S)[0])
        for i in range(int(total_page/10)):
            target_title = "下一页"
            element = driver.find_element("xpath", f"//*[@title='{target_title}']")
            element.click()
            total_html = total_html + driver.page_source
        driver.quit()
        total_html_pattern = r'<tr><td>(.*?)</td>.*?href="(.*?)" target="_blank" title=".*?">(.*?)</a></td>.*?<td>.*?</td>.*?<td>.*?</td>.*?<td>(.*?)</td>'
        matches = re.findall(total_html_pattern, total_html, re.S)
        for i in range(len(matches)):
            bianhao = matches[i][0]
            biaoti = matches[i][2]
            DownloadLink = matches[i][1]
            StartDate = matches[i][3]
            if len(StartDate) > 8:  # 清洗日期数据，格式化显示，if避免空白内容
                StartDate = str(datetime.datetime.strptime(StartDate, "%Y-%m-%d").strftime("%Y年%m月%d日"))
            if len(bianhao) > 10:
                bianhao = format_data.F_Beijing(bianhao)
            total_list.append([bianhao, biaoti, StartDate, '', '现行', DownloadLink,"北京","",str(datetime.datetime.now())])
        return total_list

    def Tianjin():  #按照新格式更新完成，日期已格式化
        print("正在爬取天津地方标准...")
        html = []
        total_list = []
        result_list = []
        url = "https://zfcxjs.tj.gov.cn/ztzl_70/bzgf/xxbz/xxbzgf/"
        headers = {
            'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 7_1_2 like Mac OS X) App leWebKit/537.51.2 (KHTML, like Gecko) Version/7.0 Mobile/11D257 Safari/9537.53'
        }
        requests.packages.urllib3.disable_warnings()
        response = requests.get(url, headers=headers, verify=False)
        html = response.content
        if response.status_code == 200:
            html =  response.text.encode('raw_unicode_escape').decode().replace(" ", "").replace("\n", "").replace("	", "")
            print(html)
            pattern = r'varitem_.*?SYBT:"(.*?)",BT:"(.*?)",FBT:".*?SBT:"(.*?)",.*?DOCPUBURL:"(.*?)",'
            matches = re.findall(pattern, html, re.S)
            print(matches)
            for i in range(len(matches)):
                bianhao = matches[i][0]
                biaoti = matches[i][1]
                s_data = matches[i][2]
                e_data = ''
                status = '现行'
                dizhi = matches[i][3]
                if "废止" in s_data:
                    e_data = s_data
                    s_data = ''
                    status = '废止'
                if len(s_data) > 8: #清洗日期数据，格式化显示，if避免空白内容
                    s_data = str(datetime.datetime.strptime(s_data, "%Y年%m月%d日").strftime("%Y年%m月%d日"))
                total_list.append([bianhao,biaoti,s_data,e_data,status,dizhi,"天津","",str(datetime.datetime.now())])
            return total_list

    def Hebei():    #按照新格式更新完成，日期已格式化
        print("正在爬取河北省地方标准")
        total_list = []
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
        for i in range(len(standard_list)):
            if len(standard_list[i][2]) > 8:  # 清洗日期数据，格式化显示，if避免空白内容
                standard_list[i][2] = str(datetime.datetime.strptime(standard_list[i][2], "%Y-%m-%d").strftime("%Y年%m月%d日"))
            standard_list[i][0] = format_data.F_Hebei(standard_list[i][0])
            total_list.append([standard_list[i][0],standard_list[i][1],standard_list[i][2],standard_list[i][3],standard_list[i][4],standard_list[i][5],"河北","",str(datetime.datetime.now())])
        return total_list

    def Shanghai(): #按照新格式更新完成，日期已格式化
        total_list = []
        headers = {
            "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 Edg/115.0.1901.203"
        }
        standard_list = []
        def change_data(data: list):
            data = list(data)
            data.insert(3, '')
            if item in ['xxbz', 'xxsj']:
                data.insert(4, '现行')
            else:
                data.insert(4, '废止')
            if data[5]:
                data[5] = 'https://zjw.sh.gov.cn/'+data[5]
            return data
        for item in ['xxbz', 'xxbzsj', 'fzbz', 'fzbzsj']:
            url = f'https://zjw.sh.gov.cn/{item}/index.html'
            response = requests.get(url, headers=headers).text
            total_page = re.findall(' totalPage: ([0-9]*?),', response)[0]
            for i in range(1, int(total_page)+1):
                if i != 1:
                    url = f'https://zjw.sh.gov.cn/{item}/index_{i}.html'
                response = requests.get(url, headers=headers).text
                data_list = re.findall('<td width="15%">(.*?)</td>.*?<td width="32%">(.*?)</td>.*?<td width="10%">(.*?)</td>.*?<td width="8%"><a href="(.*?)" title="">', response, re.S)
                standard_list += list(map(change_data, data_list))
        for i in range(len(standard_list)):
            if len(standard_list[i][2]) > 6:  # 清洗日期数据，格式化显示，if避免空白内容
                standard_list[i][2] = str(datetime.datetime.strptime(standard_list[i][2].replace(" ",""), "%Y-%m-%d").strftime("%Y年%m月%d日"))
            standard_list[i][0] = format_data.F_Shanghai(standard_list[i][0])
            total_list.append([standard_list[i][0],standard_list[i][1],standard_list[i][2],standard_list[i][3],standard_list[i][4],standard_list[i][5],"上海","",str(datetime.datetime.now())])
        return total_list

    def Sichuan():  #按照新格式更新完成，日期已格式化
        total_list = []
        SiChuan_URL = "http://jst.sc.gov.cn/scjst/bzgf/zhuanlan.shtml"
        data_list = []
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
                for i in range(len(data_list)): #因为表格的原因，如果有缺少一列的情况，从此循环遍历补齐
                    if len(data_list[i]) == 6:
                        data_list[i] = [""] + data_list[i]
                for i in range(len(data_list)): #状态空白的补充”现行“
                    if len(data_list[i][6]) == 0:
                        data_list[i][6] = '现行'
                for i in range(len(data_list)):
                    result_list.append([data_list[i][2],data_list[i][3],data_list[i][5],'',data_list[i][6],''])
                # 以上为获取总目录及规范编号，以下为获取所有的下载链接
            url = "http://jst.sc.gov.cn/scjst/bzgf/zhuanlan.shtml"
            response = requests.get(url)
            if response.status_code == 200:
                total_html = total_html + response.text
            for i in range(8):
                url = "http://jst.sc.gov.cn/scjst/bzgf/zhuanlan" + "_" + str(i+2) + ".shtml"
                response = requests.get(url)
                if response.status_code == 200:
                    total_html = total_html + response.text
            pattern = r'title="【四川省.*?】(.*?)" href="(.*?)" target='
            SiChuan_URL = re.findall(pattern, total_html, re.S)
            for i in range(len(result_list)):
                for j in range(len(SiChuan_URL)):
                    if str(result_list[i][1]) in str(SiChuan_URL[j][0]):
                        result_list[i][5] = str('http://jst.sc.gov.cn' + "/" + SiChuan_URL[j][1])[:-6] + "/files/" + urllib.parse.quote(result_list[i][1], safe='') + ".pdf"
                        break
            for i in range(len(result_list)):
                result_list[i][0] = format_data.F_Sichuan(result_list[i][0])
                if len(result_list[i][2]) > 4: #清洗日期数据，格式化显示，if避免空白内容
                    result_list[i][2] = str(datetime.datetime.strptime(result_list[i][2], "%Y.%m.%d").strftime("%Y年%m月%d日"))
                total_list.append([result_list[i][0],result_list[i][1],result_list[i][2],result_list[i][3],result_list[i][4],result_list[i][5],"四川","",str(datetime.datetime.now())])
            return total_list
        except RequestException:
            return total_list

    def Guangdong():
        chrome_options = Options() # 实例化option对象
        chrome_options.add_argument("--headless") # 把Chrome浏览器设置为静默模式
        chrome_options.add_argument('--disable-gpu') # 禁止加载图片
        chrome_options.add_argument('log-level=3')
        driver = webdriver.Chrome(options=chrome_options)
        driver.implicitly_wait(10)
        url = 'https://bzgl.gdcic.net/#/home/tabsBZ'
        driver.get(url)
        driver.find_element(By.XPATH, '//*[@id="app"]/div/div[3]/div/div[5]/div/div/div/ul/li[11]/div/div').click()
        driver.find_element(By.XPATH, '/html/body/div[1]/div/div[3]/div/div[5]/div/div/div/ul/li[11]/div[2]/div/div/div/ul/li[4]').click()
        time.sleep(1)
        max_num = driver.find_element(By.XPATH, '//*[@id="app"]/div/div[3]/div/div[5]/div/div/div/ul/li[1]').text.split(' ')[1]
        standard_list = []
        for x in range(int(max_num)//100+1):
            elements = driver.find_elements(By.XPATH, '//*[@id="app"]/div/div[3]/div/div[5]/div/div/div/div/div/div/table/tbody/tr')
            # print(len(elements))
            i = x*100 + 0
            for element in elements:
                # 标准编号，标准标题，实施日期，作废日期，标准状态，下载链接
                standard = []
                element_child = element.find_elements(By.CLASS_NAME, 'ant-table-row-cell-break-word')
                standard.append(element_child[1].text)
                standard.append(element_child[2].text)
                try:
                    standard.append(element_child[6].text)
                    standard.append('')
                    standard.append(element_child[4].text)
                    standard.append('')
                except:
                    standard.append('')
                    standard.append('')
                    standard.append('')
                    standard.append('')
                standard_list.append(standard)
                i += 1
                # print(f'获取广东省地方标准第{i}/{max_num}条')
            driver.find_element(By.XPATH, '//*[@id="app"]/div/div[3]/div/div[5]/div/div/div/ul/li[5]').click()
            time.sleep(1)
        print(standard_list)
        return standard_list

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
        max_page = driver.find_element(By.CSS_SELECTOR, '#layui-laypage-1 > a.layui-laypage-last').text
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

    def Guangxi():
        pass

    def Hainan():
        pass

    def Chongqing():
        pass

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

class format_data():
    def F_Hebei(input_str):
        # 去除字符串中的空格
        input_str = input_str.replace(" ", "")
        # 使用正则表达式匹配不同格式的字符串
        match = re.search(r'(DB13JT|DB13J|DBJT02)(\d+)-(\d{4})', input_str)

        if match:
            code, number, year = match.groups()
            formatted_str = f'{code}-{number}-{year}'
            return formatted_str
        else:
            # 如果输入字符串不匹配预期格式，返回原始字符串
            return input_str

    def F_Shanghai(input_str):
        # 去除字符串中的空格
        input_str = input_str.replace(" ", "")
        input_str = input_str.replace('\\', '/')
        input_str = input_str.replace('DGTJ', 'DG/TJ')
        # 使用正则表达式匹配不同格式的字符串
        match = re.search(r'(DG/TJ08|DGJ08|DBJT08)(\d+)-(\d{4})', input_str)
        if match:
            code, number, year = match.groups()
            formatted_str = f'{code}-{number}-{year}'
            return formatted_str
        else:
            # 如果输入字符串不匹配预期格式，返回原始字符串
            return input_str
    def F_Beijing(input_str):
        # 去除字符串中的空格
        input_str = input_str.replace(" ", "")
        input_str = input_str.replace("DB11/", "DB11")
        # 使用正则表达式匹配不同格式的字符串
        if "." in input_str:
            match = re.search(r'(DB11T\s?\d+\.\d+)-(\d{4})', input_str)
            if match:
                code_version, year = match.groups()
                # # 将版本号中的小数点前面插入一个短横线“-”
                parts = code_version.split('.')
                formatted_version = '.'.join(parts)
                formatted_version = formatted_version.replace("DB11T", "")
                formatted_str = f'DB11/T-{formatted_version}-{year}'
                return formatted_str
            else:
                # 如果输入字符串不匹配预期格式，返回原始字符串
                return input_str
        else:
            match = re.search(r'(DB11T|DB11|)(\d+)-(\d{4})', input_str)
            if match:
                code, number, year = match.groups()
                formatted_str = f'{code}-{number}-{year}'
                formatted_str = formatted_str.replace("DB11T","DB11/T")
                return formatted_str
            else:
                # 如果输入字符串不匹配预期格式，返回原始字符串
                return input_str
    def F_Sichuan(input_str):
        # 去除字符串中的空格
        input_str = input_str.replace('DB51/T', 'DB51T-')
        input_str = input_str.replace('DBJ51/T', 'DBJ51T-')
        input_str = input_str.replace('DBJ51/', 'DBJ51-')
        input_str = input_str.replace('DB51/', 'DB51-')
        return input_str

if __name__ == "__main__":
    print(DB_data_get.Tianjin())

