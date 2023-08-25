from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import re
import time
import requests
# request
# url_list = {
#     'http://zfcxjst.hebei.gov.cn/hbzjt/ztzl/jj/gcjsgf/fwjz/',
#     'http://zfcxjst.hebei.gov.cn/hbzjt/ztzl/jj/gcjsgf/szgc/',
#     'http://zfcxjst.hebei.gov.cn/hbzjt/ztzl/jj/gcjsgf/czjs/',
#     'http://zfcxjst.hebei.gov.cn/hbzjt/ztzl/jj/gcjsgf/sxjs/',
#     'http://zfcxjst.hebei.gov.cn/hbzjt/ztzl/jj/gcjsgf/zjbz/'
# }
# base_url = 'http://zfcxjst.hebei.gov.cn/hbzjt/ztzl/jj/gcjsgf/'
# url = 'http://zfcxjst.hebei.gov.cn/zycms/www/hbzjt/ztzl/jj/gcjsgf/fwjz/index_11.html'
# response = requests.get(url).text
# print(response)

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

print(standard_list)

time.sleep(1000)




data = DB_data_get.Beijing()
data = DB_data_get.Tianjin()
data = DB_data_get.Hebei()
data = DB_data_get.Sanxi()
data = DB_data_get.Neimenggu()
data = DB_data_get.Liaoning()
data = DB_data_get.Jilin()
data = DB_data_get.Heilongjiang()
data = DB_data_get.Shanghai()
data = DB_data_get.Jiangsu()
data = DB_data_get.ZheJiang()
data = DB_data_get.Anhui()
data = DB_data_get.Fujian()
data = DB_data_get.Jiangxi()
data = DB_data_get.Shandong()
data = DB_data_get.Henan()
data = DB_data_get.Hubei()
data = DB_data_get.Hunan()
data = DB_data_get.Guangdong()
data = DB_data_get.Guangxi()
data = DB_data_get.Hainan()
data = DB_data_get.Chongqing()
data = DB_data_get.Sichuan()
data = DB_data_get.Guizhou()
data = DB_data_get.Yunnan()
data = DB_data_get.Xizang()
data = DB_data_get.Shanxi()
data = DB_data_get.Gansu()
data = DB_data_get.Qinghai()
data = DB_data_get.Ningxia()
data = DB_data_get.Xinjiang()
data = DB_data_get.Taiwan()
data = DB_data_get.Hongkong()
data = DB_data_get.Macau()