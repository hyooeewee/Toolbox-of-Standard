#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :standards_spider.py
# @Time      :2023/02/20 13:40:11
# @Author    :Hughie Wei

import codecs
import json
import re

import chardet
import pandas as pd
import requests
from bs4 import BeautifulSoup

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
    keyword = '信息技术'
    keyword_str = str(keyword.encode('GB2312')).split("'")[1].replace(r'\x', '%').replace(' ', '+')
    # 1.获取标准id
    # 1.1.读取文件数据
    # filename = input('请指定文件路径：')
    filename = r'D:\Users\Hughi\OneDrive - hrbeu.edu.cn\Work2023\04.行政管理\01.标准更新\规范、规程、标准和图集资料\《2022年度现行规范、规程、标准和图集清单》.xls'
    df = pd.ExcelFile(filename)
    # sheet_name = input('请确认表格名称{}：'.format(df.sheet_names))
    sheet_name = '施工标准'
    sheet = df.parse(sheet_name)
    # cell_loc = input('请输入单元格位置，如C6：')
    # i = int(re.findall('[0-9]', cell_loc)[0])-1
    # ord('A')=65
    # j = ord(re.findall('[A-Za-z]', cell_loc)[0].upper())-65
    # i,j = 5,2
    # print(sheet.iat[i,j])
    # 1.2 读取单元格数据
    # count = 0
    # id_list = {}
    # while count <= 3:
    #     if read_cell_data(sheet, i, j) != None:
    #         value,i,j = read_cell_data(sheet, i, j)
    #         id_list[value] = [i,j]
    #     else:
    #         count += 1
    #     i += 1
    # print(id_list)
    id_list = {'GB50202-2018': [6, 2], 'GB50203-2011': [7, 2]}
    for value, loc in id_list.items():
        # print(value,loc)
        data = csres_get(value)
        # print(data)
        wash_data(data)
        # with open('./standards/standerds.html', 'w+', encoding='utf-8') as fp:
        #     fp.write(data)
        break

