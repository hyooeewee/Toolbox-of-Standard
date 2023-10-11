import os
import re
import time
import pandas as pd
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from datetime import date
import numpy as np

FILE_PATH = r"D:\Users\weihao\OneDrive - hrbeu.edu.cn\05.Projects\02.Python\input.xlsx"
DIRECTORY = r"D:\Users\weihao\OneDrive - hrbeu.edu.cn\05.Projects\02.Python"
SAVE_PATH = os.path.join(DIRECTORY, 'output.xlsx')
df = pd.read_excel(FILE_PATH)
chrome_options = Options() # 实例化option对象
chrome_options.add_argument("--headless") # 把Chrome浏览器设置为静默模式
chrome_options.add_argument('--disable-gpu') # 禁止加载图片
chrome_options.add_argument('log-level=3') # 禁用日志输出#INFO = 0 WARNING = 1 LOG_ERROR = 2 LOG_FATAL = 3 default is 0
driver = webdriver.Chrome(options=chrome_options) 
for i in range(df.index.stop):
    # print(i)
    # print(i, df.values[i][1])
    url = 'https://dbba.sacinfo.org.cn/stdList?key=' + df.values[i][1]
    driver.get(url)
    time.sleep(1)
    elements = driver.find_elements(By.XPATH, '//*[@id="hbtable"]/tbody/tr')
    # print(i, df.values[i][6])
    # if df.values[i][6] is not np.nan:
    #     date_time = re.findall('.*?([0-9]*?)年([0-9]*?)月([0-9]*?)日.*?', df.values[i][6])
    # if date_time:
    #     d = date(int(date_time[0][0]), int(date_time[0][1]), int(date_time[0][2]))
    #     # print(d)
    #     df.iloc[i, 3] = d
    for j, element in enumerate(elements):
        try:
            # print(element.find_element(By.XPATH, f'//*[@id="hbtable"]/tbody/tr[{j+1}]/td[3]/div/a').text)
            if element.find_element(By.XPATH, f'//*[@id="hbtable"]/tbody/tr[{j+1}]/td[3]/div/a').text == df.values[i][1]:
                standard_number = element.find_element(By.XPATH, f'//*[@id="hbtable"]/tbody/tr[{j+1}]/td[2]').text
                start_date = element.find_element(By.XPATH, f'//*[@id="hbtable"]/tbody/tr[{j+1}]/td[7]').text
                status = element.find_element(By.XPATH, f'//*[@id="hbtable"]/tbody/tr[{j+1}]/td[5]/span').text
                print(standard_number,start_date,status)
                if start_date != df.values[i][3]:
                    # print('更新')
                    df.iloc[i, 4] = f'{df.values[i][4]}{df.values[i][2]}；'.replace('nan', '')
                    df.iloc[i, 2] = standard_number
                    df.iloc[i, 3] = start_date
                    df.iloc[i, 5] = '更新完成'
                else:
                    # print('现行')
                    df.iloc[i, 5] = '现行标准'        
        except:
            # print('错误')
            df.iloc[i, 5] = '查询错误'
    # print(df)
    df.to_excel(SAVE_PATH, index=False)
print('done!')
# df.set_index('序号', inplace=True)
# df.to_excel(SAVE_PATH)