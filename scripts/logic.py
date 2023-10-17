#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :logic.py
# @Time      :2023/10/17 16:47:30
# @Author    :hyooeewee

import pandas as pd

class Multi_Update():
    def read_data(fileName):
        df = pd.read_excel(fileName, sheet_name="Sheet1")
        data = dict(zip(df.iloc[:, 1], df.iloc[:, 2]))
        return data

    def wash_data(data):
        soup = BeautifulSoup(data, 'lxml')
        print(type(soup))
        # with open('soup.text', 'w+', encoding='utf-8') as fp:
        #     fp.write(str(soup))
        print(soup.find_all('.*?<font color="#000000">(.*?)</font>.*?'))

if __name__ == "__main__":
    pass