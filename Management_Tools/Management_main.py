import datetime
import os
import random
import re
import sqlite3
import sys
import urllib
from time import sleep
from bs4 import BeautifulSoup
from requests.exceptions import RequestException
import requests
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import (QApplication, QFileDialog, QMainWindow, QMessageBox, QTableWidgetItem)
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.by import By
import pymysql

INI_PATH = r"config.ini"
DATABASE_PATH = r'.\management.db'


class MyMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # 使用loadUi加载UI文件
        self.ui = uic.loadUi(r'.\UI\management.ui', self)
        self.ui.OLDB_CONNECT.clicked.connect(self.OLDB_PW_button_click)
        self.ui.S_Spider.clicked.connect(self.S_Spider_button_click)
        self.ui.OL_PUSH.clicked.connect(self.data_transmit)
        self.ui.OL_CHECK.clicked.connect(self.OL_CHECK_function)
                # 在这里可以添加自定义功能
    def OLDB_PW_button_click(self):
        IP = self.ui.OLDB_IP.text()
        PORT = self.ui.OLDB_PORT.text()
        ACCOUNT = self.ui.OLDB_ACCOUNT.text()
        PW = self.ui.OLDB_PW.text()
        message = button_function.OLDB_CONNECT(IP,PORT,ACCOUNT,PW)
        self.ui.OLDB_MB.append(message)

    def S_Spider_button_click(self):
        if self.ui.S_GUOBIAO.isChecked():
            self.ui.S_MB.append("正在爬取国标数据，数据源为http://www.ccsn.org.cn/Zbbz/ShowFullText.aspx")
            temp_list = self.Standards_Spider.S_GB()
            self.data_update(temp_list)
            self.ui.S_MB.append("已经完成国标数据爬取")
        if self.ui.S_BEIJING.isChecked():
            self.ui.S_MB.append("正在爬取北京地方标准数据，数据源为http://bjjs.zjw.beijing.gov.cn/")
            temp_list = self.Standards_Spider.S_Beijing()
            self.data_update(temp_list)
            self.ui.S_MB.append("已经完成北京地方标准数据爬取")
        if self.ui.S_TIANJIN.isChecked():
            self.ui.S_MB.append("正在爬取天津地方标准数据，数据源为https://zfcxjs.tj.gov.cn/")
            temp_list = self.Standards_Spider.S_Tianjin()
            self.data_update(temp_list)
            self.ui.S_MB.append("已经完成天津地方标准数据爬取")
        if self.ui.S_HEBEI.isChecked():
            self.ui.S_MB.append("正在爬取河北地方标准数据，数据源为http://zfcxjst.hebei.gov.cn/")
            temp_list = self.Standards_Spider.S_Hebei()
            self.data_update(temp_list)
            self.ui.S_MB.append("已经完成河北地方标准数据爬取")
        if self.ui.S_SHANXI.isChecked():
            pass
        if self.ui.S_NEIMENG.isChecked():
            pass
        if self.ui.S_JILIN.isChecked():
            pass
        if self.ui.S_HEILONGJIANG.isChecked():
            pass
        if self.ui.S_SHANGHAI.isChecked():
            self.ui.S_MB.append("正在爬取上海地方标准数据，数据源为https://zjw.sh.gov.cn/")
            temp_list = self.Standards_Spider.S_Shanghai()
            self.data_update(temp_list)
            self.ui.S_MB.append("已经完成上海地方标准数据爬取")
        if self.ui.S_JIANGSU.isChecked():
            pass
        if self.ui.S_ZHEJIANG.isChecked():
            pass
        if self.ui.S_ANHUI.isChecked():
            pass
        if self.ui.S_FUJIAN.isChecked():
            pass
        if self.ui.S_JIANGXI.isChecked():
            pass
        if self.ui.S_SHANDONG.isChecked():
            pass
        if self.ui.S_HENAN.isChecked():
            pass
        if self.ui.S_HUBEI.isChecked():
            pass
        if self.ui.S_HUNAN.isChecked():
            pass
        if self.ui.S_GUANGDONG.isChecked():
            pass
        if self.ui.S_GUANGXI.isChecked():
            pass
        if self.ui.S_BEIJING.isChecked():
            pass
        if self.ui.S_HAINAN.isChecked():
            pass
        if self.ui.S_CHONGQING.isChecked():
            pass
        if self.ui.S_SICHUAN.isChecked():
            self.ui.S_MB.append("正在爬取四川地方标准数据，数据源为http://jst.sc.gov.cn/scjst/bzgf/zhuanlan.shtml")
            temp_list = self.Standards_Spider.S_Shanghai()
            self.data_update(temp_list)
            self.ui.S_MB.append("已经完成四川地方标准数据爬取")
        if self.ui.S_GUIZHOU.isChecked():
            pass
        if self.ui.S_YUNNAN.isChecked():
            pass
        if self.ui.S_XIZANG.isChecked():
            pass
        if self.ui.S_SHANNXI.isChecked():
            pass
        if self.ui.S_GANSU.isChecked():
            pass
        if self.ui.S_QINGHAI.isChecked():
            pass
        if self.ui.S_NINGXIA.isChecked():
            pass
        if self.ui.S_XINJIANG.isChecked():
            pass

    def data_update(result_list):
        if result_list:
            conn = sqlite3.connect(DATABASE_PATH)
            cur = conn.cursor()
            for i in result_list:
                try:
                    cur.execute(
                        f"insert into standards values('{i[0]}','{i[2]}','{i[3]}','{i[4]}','{i[5]}',"
                        f"'{i[6]}','{i[7]}','{i[1]}','{i[8]}')")
                except:
                    cur.execute(
                        f"update standards set StandardNames='{i[2]}',StartDate='{i[3]}', EndDate='{i[4]}',"
                        f"Status='{i[5]}',DownloadLinks='{i[6]}',TYPE='{i[1]}',HEADERS='{i[7]}',UPDATE_TIME='{i[8]}'"
                        f" where StandardNumbers='{i[0]}'")
            conn.commit()
            conn.close()
    class Standards_Spider():  # 各省市的爬虫，返回的都是一个list
        def S_GB():
            def GuoBiao_get_PDF(GB_URL, Guid, IP_List):
                try:
                    headers = HEADERS_ToolS.Random_headers()
                    proxies = HEADERS_ToolS.Random_IP(IP_List)
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

            Proxies_IP_List = HEADERS_ToolS.IP_Pool()
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
            print("国家标准总计条数：" + total_piece)
            print("正在爬取第1页，共计" + total_page + "页")
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
                    S_Date = str(
                        str(S_Date).split("/")[0] + "年" + str(S_Date).split("/")[1] + "月" + str(S_Date).split("/")[
                            2] + "日")
                dizhi = 'http://www.ccsn.org.cn/Zbbz/Show.aspx' + matches[i][0]
                dizhi = GuoBiao_get_PDF(dizhi, matches[i][0], Proxies_IP_List)
                # {代码，标准名，开始时间，截止时间，当前状态，下载链接，区域，headers，更新时间}
                total_list.append([ID, Name, S_Date, "", "", dizhi, "国标", "", str(datetime.datetime.now())])
                print(
                    "数据为：" + ID + "," + Name + "," + S_Date + "," + "" + "," + "现行" + "," + dizhi + "," + "国标" + "," + str(
                        datetime.datetime.now()))

            for i in range(int(int(total_page) - 1)):
                Proxies_IP_List = HEADERS_ToolS.IP_Pool()
                print("当前正在爬取第" + str(i + 2) + "页，共计" + str(total_page) + "页")
                button = driver.find_element(By.XPATH, "//a[@id='ID_ucZbbzList_ucPager1_btnNext']")
                button.click()
                html = driver.page_source
                matches = re.findall(standards_pattern, html, re.S)
                for i in range(len(matches)):
                    ID = matches[i][2]
                    Name = matches[i][1]
                    S_Date = matches[i][4]
                    if len(S_Date) > 6:  # 清洗日期数据，格式化显示，if避免空白内容
                        S_Date = str(
                            str(S_Date).split("/")[0] + "年" + str(S_Date).split("/")[1] + "月" + str(S_Date).split("/")[
                                2] + "日")
                    dizhi = 'http://www.ccsn.org.cn/Zbbz/Show.aspx' + matches[i][0]
                    dizhi = GuoBiao_get_PDF(dizhi, matches[i][0], Proxies_IP_List)
                    # {代码，标准名，开始时间，截止时间，当前状态，下载链接，区域，headers，更新时间}
                    total_list.append([ID, Name, S_Date, "", "现行", dizhi, "国标", "", str(datetime.datetime.now())])
                    print(
                        "数据为：" + ID + "," + Name + "," + S_Date + "," + "" + "," + "" + "," + dizhi + "," + "国标" + "," + str(
                            datetime.datetime.now()))
            driver.quit()
            return total_list

        def S_Beijing():
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
            for i in range(int(total_page / 10)):
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
                total_list.append(
                    [bianhao, biaoti, StartDate, '', '现行', DownloadLink, "北京", "", str(datetime.datetime.now())])
            return total_list

        def S_Tianjin():
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
                html = response.text.encode('raw_unicode_escape').decode().replace(" ", "").replace("\n", "").replace(
                    "	", "")
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
                    if len(s_data) > 8:  # 清洗日期数据，格式化显示，if避免空白内容
                        s_data = str(datetime.datetime.strptime(s_data, "%Y年%m月%d日").strftime("%Y年%m月%d日"))
                    total_list.append(
                        [bianhao, biaoti, s_data, e_data, status, dizhi, "天津", "", str(datetime.datetime.now())])
                return total_list

        def S_Hebei():
            print("正在爬取河北省地方标准")
            total_list = []
            chrome_options = Options()  # 实例化option对象
            chrome_options.add_argument("--headless")  # 把Chrome浏览器设置为静默模式
            chrome_options.add_argument('--disable-gpu')  # 禁止加载图片
            chrome_options.add_argument('log-level=3')
            driver = webdriver.Chrome(options=chrome_options)
            browser = webdriver.Chrome(options=chrome_options)
            base_url = 'http://zfcxjst.hebei.gov.cn/hbzjt/ztzl/jj/gcjsgf/'
            standard_list = []
            for item in ['fwjz/', 'szgc/', 'czjs/', 'sxjs/', 'zjbz/']:
                item_url = base_url + item
                driver.get(item_url)
                try:
                    max_page = re.findall('index_(.*?).html', driver.find_element(By.CSS_SELECTOR,
                                                                                  '#page_nav_list > a.pb_end_page').get_attribute(
                        'href'))[0]
                except:
                    max_page = 1
                for i in range(1, int(max_page) + 1):
                    url = item_url + f"index_{i}.html"
                    driver.get(url)
                    elements = driver.find_elements(By.CSS_SELECTOR, '#number > li')
                    for element in elements:
                        # 标准编号，标准标题，实施日期，作废日期，标准状态，下载链接
                        standard = []
                        standard.append(
                            element.find_element(By.CSS_SELECTOR, '#number > li > div.bianhao.pso > span').text)
                        standard.append(element.find_element(By.CSS_SELECTOR, '#number > li > div.mingcheng > a').text)
                        try:
                            standard.append(
                                element.find_element(By.CSS_SELECTOR, '#number > li > div.riqi.pso > span').text)
                            standard.append('')
                            standard.append('现行')
                            href = element.find_element(By.CSS_SELECTOR,
                                                        '#number > li > div.yulan.pso > span > a').get_attribute('href')

                            browser.get(href)
                            standard.append(browser.find_element(By.CSS_SELECTOR,
                                                                 '#yanse > div.p_nei > div > span > div > iframe').get_attribute(
                                'src'))
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
                    standard_list[i][2] = str(
                        datetime.datetime.strptime(standard_list[i][2], "%Y-%m-%d").strftime("%Y年%m月%d日"))
                standard_list[i][0] = format_data.F_Hebei(standard_list[i][0])
                total_list.append([standard_list[i][0], standard_list[i][1], standard_list[i][2], standard_list[i][3],
                                   standard_list[i][4], standard_list[i][5], "河北", "", str(datetime.datetime.now())])
            return total_list

        def S_Shanghai():
            total_list = []
            headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 Edg/115.0.1901.203"
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
                    data[5] = 'https://zjw.sh.gov.cn/' + data[5]
                return data

            for item in ['xxbz', 'xxbzsj', 'fzbz', 'fzbzsj']:
                url = f'https://zjw.sh.gov.cn/{item}/index.html'
                response = requests.get(url, headers=headers).text
                total_page = re.findall(' totalPage: ([0-9]*?),', response)[0]
                for i in range(1, int(total_page) + 1):
                    if i != 1:
                        url = f'https://zjw.sh.gov.cn/{item}/index_{i}.html'
                    response = requests.get(url, headers=headers).text
                    data_list = re.findall(
                        '<td width="15%">(.*?)</td>.*?<td width="32%">(.*?)</td>.*?<td width="10%">(.*?)</td>.*?<td width="8%"><a href="(.*?)" title="">',
                        response, re.S)
                    standard_list += list(map(change_data, data_list))
            for i in range(len(standard_list)):
                if len(standard_list[i][2]) > 6:  # 清洗日期数据，格式化显示，if避免空白内容
                    standard_list[i][2] = str(
                        datetime.datetime.strptime(standard_list[i][2].replace(" ", ""), "%Y-%m-%d").strftime(
                            "%Y年%m月%d日"))
                standard_list[i][0] = format_data.F_Shanghai(standard_list[i][0])
                total_list.append([standard_list[i][0], standard_list[i][1], standard_list[i][2], standard_list[i][3],
                                   standard_list[i][4], standard_list[i][5], "上海", "", str(datetime.datetime.now())])
            return total_list

        def S_Sichuan():
            total_list = []
            SiChuan_URL = "http://jst.sc.gov.cn/scjst/bzgf/zhuanlan.shtml"
            data_list = []
            result_list = []
            total_html = ""
            try:
                url = "http://jst.sc.gov.cn/scjst/bzgf/2023/3/13/ded7b643735240758041911d7f30f084.shtml"
                response = requests.get(url)
                if response.status_code == 200:
                    soup = BeautifulSoup(response.content, "html.parser")  # 定位表格元素
                    table = soup.find("table")  # 遍历表格行并提取数据
                    for row in table.find_all("tr"):
                        row_data = [cell.get_text(strip=True) for cell in row.find_all(["th", "td"])]
                        data_list.append(row_data)
                    data_list.pop(0)
                    for i in range(len(data_list)):  # 因为表格的原因，如果有缺少一列的情况，从此循环遍历补齐
                        if len(data_list[i]) == 6:
                            data_list[i] = [""] + data_list[i]
                    for i in range(len(data_list)):  # 状态空白的补充”现行“
                        if len(data_list[i][6]) == 0:
                            data_list[i][6] = '现行'
                    for i in range(len(data_list)):
                        result_list.append([data_list[i][2], data_list[i][3], data_list[i][5], '', data_list[i][6], ''])
                    # 以上为获取总目录及规范编号，以下为获取所有的下载链接
                url = "http://jst.sc.gov.cn/scjst/bzgf/zhuanlan.shtml"
                response = requests.get(url)
                if response.status_code == 200:
                    total_html = total_html + response.text
                for i in range(8):
                    url = "http://jst.sc.gov.cn/scjst/bzgf/zhuanlan" + "_" + str(i + 2) + ".shtml"
                    response = requests.get(url)
                    if response.status_code == 200:
                        total_html = total_html + response.text
                pattern = r'title="【四川省.*?】(.*?)" href="(.*?)" target='
                SiChuan_URL = re.findall(pattern, total_html, re.S)
                for i in range(len(result_list)):
                    for j in range(len(SiChuan_URL)):
                        if str(result_list[i][1]) in str(SiChuan_URL[j][0]):
                            result_list[i][5] = str('http://jst.sc.gov.cn' + "/" + SiChuan_URL[j][1])[
                                                :-6] + "/files/" + urllib.parse.quote(result_list[i][1],
                                                                                      safe='') + ".pdf"
                            break
                for i in range(len(result_list)):
                    result_list[i][0] = format_data.F_Sichuan(result_list[i][0])
                    if len(result_list[i][2]) > 4:  # 清洗日期数据，格式化显示，if避免空白内容
                        result_list[i][2] = str(
                            datetime.datetime.strptime(result_list[i][2], "%Y.%m.%d").strftime("%Y年%m月%d日"))
                    total_list.append(
                        [result_list[i][0], result_list[i][1], result_list[i][2], result_list[i][3], result_list[i][4],
                         result_list[i][5], "四川", "", str(datetime.datetime.now())])
                return total_list
            except RequestException:
                return total_list

    def data_transmit(self):
        # 连接本地SQLite数据库
        sqlite_connection = sqlite3.connect(DATABASE_PATH)
        sqlite_cursor = sqlite_connection.cursor()
        # 连接云端mysql数据库
        online_db_config = {
            'host': self.ui.OLDB_IP.text() ,  # 远程MySQL数据库的主机地址（IP地址或域名）
            'user': self.ui.OLDB_ACCOUNT.text(),        # 远程MySQL数据库的用户名
            'password': self.ui.OLDB_PW.text(),    # 远程MySQL数据库的密码
            'database': 'standard_db',  # 要连接的数据库名称
            'port': self.ui.OLDB_PORT.text()                    # MySQL默认端口号
        }
        mysql_connection = pymysql.connect(**online_db_config)
        mysql_cursor = mysql_connection.cursor()
        # 选中所有数据
        sqlite_cursor.execute('SELECT * FROM standards')
        data_to_insert = sqlite_cursor.fetchall()
        i = 1
        for row in data_to_insert:
            mysql_cursor.execute(
                'INSERT INTO STANDARD (SN, TYPE, NAME, START_DATE, END_DATE , STATUS, LINK, RE_HEADERS, UPDATE_TIME) '
                'VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)', row)
            i = i + 1
            print("共计" + str(len(data_to_insert)) + "条数据，当前已插入完成" + str(i) + "条！")
        mysql_connection.commit()
        mysql_connection.close()
        sqlite_connection.close()

    def OL_CHECK_function(self):
        def regexp(expr, result):
            reg = re.compile(expr)
            return reg.search(result) is not None
        conn = sqlite3.connect(DATABASE_PATH)
        cur = conn.cursor()
        pattarn = "Status REGEXP '^'"
        if pattarn:
            conn.create_function("REGEXP", 2, regexp)
            cur.execute(f"SELECT * FROM standards WHERE {pattarn}")
            print(pattarn)
        else:
            cur.execute("SELECT * FROM standards")
        data = cur.fetchall()
        conn.commit()
        conn.close()
        y = len(data)
        self.ui.tableWidget.setRowCount(y)
        for iy, i in enumerate(data):
            for ix, v in enumerate(i):
                item = QTableWidgetItem(v)
                self.ui.tableWidget.setItem(iy, ix, item)
        self.ui.tableWidget.resizeColumnsToContents()
        self.ui.tableWidget.resizeRowsToContents()
        self.ui.tableWidget.setColumnWidth(0, 160)
        self.ui.tableWidget.setColumnWidth(1, 190)
        self.ui.tableWidget.setColumnWidth(2, 100)
        self.ui.tableWidget.setColumnWidth(3, 100)
        self.ui.tableWidget.setColumnWidth(4, 60)
        self.ui.tableWidget.setColumnWidth(5, 60)
        for row in range(self.ui.tableWidget.rowCount()):
            self.ui.tableWidget.setRowHeight(row, 25)

class HEADERS_ToolS():  #在爬虫过程中可能会用到的一些请求头工具
    def IP_Pool():
        HTTP_IP = []
        HTTPS_IP = []
        count = 10  # 一次获取的IP数量
        HTTP_response = requests.get("http://zltiqu.pyhttp.taolop.com/getip?count=" + str(
            count) + "&neek=87070&type=1&yys=0&port=1&sb=*&mr=1&sep=6")
        HTTP_IP_List = HTTP_response.text.split("*")
        HTTP_IP_List = HTTP_IP_List[:-1]
        for i in range(len(HTTP_IP_List)):
            HTTP_IP_List[i] = HTTP_IP_List[i].replace(" ", "").replace("\r", "").replace("\n", "")
            resp = requests.get("https://www.baidu.com", proxies={"http": "http://" + HTTP_IP_List[i]})
            if resp.status_code == 200:
                HTTP_IP.append(HTTP_IP_List[i])
        sleep(2)
        HTTPS_response = requests.get("http://zltiqu.pyhttp.taolop.com/getip?count=" + str(
            count) + "&neek=87070&type=1&yys=0&port=2&sb=*&mr=1&sep=6")
        HTTPS_IP_List = HTTPS_response.text.split("*")
        HTTPS_IP_List = HTTPS_IP_List[:-1]
        for i in range(len(HTTPS_IP_List)):
            HTTPS_IP_List[i] = HTTPS_IP_List[i].replace(" ", "").replace("\r", "").replace("\n", "")
            resp = requests.get("https://www.baidu.com", proxies={"http": "http://" + HTTPS_IP_List[i]})
            if resp.status_code == 200:
                HTTPS_IP.append(HTTPS_IP_List[i])
        total_list = [HTTP_IP, HTTPS_IP]
        print(total_list)
        return total_list

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

class format_data():    #清洗数据用的工具
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

class button_function():   #按钮功能的集成
    def online_db_version(online_db_config):
        print(online_db_config)
        time_list = []
        connection = pymysql.connect(**online_db_config)
        try:
            # 创建一个数据库游标对象
            with connection.cursor() as cursor:
                # 执行 SQL 查询
                sql_query = "SELECT * FROM STANDARD"
                cursor.execute(sql_query)
                # 获取所有行的结果
                rows = cursor.fetchall()
                # 将结果转换为列表
                result_list = list(rows)
        finally:
            # 关闭数据库连接
            connection.close()
        for i in range(len(result_list)):  # 提取全部的时间，转换成datetime对象
            time_list.append(datetime.datetime.strptime(result_list[i][8], "%Y-%m-%d %H:%M:%S.%f"))
        result = max(time_list)
        return str(result).split('.')[0]

    def OLDB_CONNECT(IP,PORT,ACCOUNT,PW):
        return_message = ""
        online_db_config = {
            'host': str(IP),  # 远程MySQL数据库的主机地址（IP地址或域名）
            'user': str(ACCOUNT),  # 远程MySQL数据库的用户名
            'password': str(PW),  # 远程MySQL数据库的密码
            'database': 'standard_db',  # 要连接的数据库名称
            'port': int(PORT)  # MySQL默认端口号
            }
        try:
            conn = sqlite3.connect(DATABASE_PATH)
            cur = conn.cursor()
            return_message += '【成功连接到本地sqlite数据库】' + "\n"
            return_message += '本地sqlite数据库更新时间为' + str(datetime.datetime.fromtimestamp(os.path.getmtime(os.getcwd() + "/management.db"))).split('.')[0] + "\n"
        except pymysql.Error as e:
            return_message += str(f'本地sqlite数据库连接错误')
            return_message += str(f'错误信息为: {e}')
        finally:
            # 最后记得关闭数据库连接
            if 'connection' in locals():
                conn.commit()
                conn.close()
        try:
            connection = pymysql.connect(**online_db_config)
            return_message += '【成功连接到MySQL数据库】' + "\n"
            return_message += str(f'当前数据库IP为: {IP}') + "\n"
            return_message += str(f'当前数据库端口为: {PORT}') + "\n"
            return_message += str(f'当前数据库登陆账号为: {ACCOUNT}') + "\n"
            return_message += str(f'云数据库更新时间为: ') + str(button_function.online_db_version(online_db_config)) + "\n"
        except pymysql.Error as e:
            return_message += str('云端mysql数据库连接错误')
            return_message += str(f'错误信息为: {e}')
        finally:
            # 最后记得关闭数据库连接
            if 'connection' in locals():
                connection.close()
        return return_message


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyMainWindow()
    window.show()
    sys.exit(app.exec_())



