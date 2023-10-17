#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :logic.py
# @Time      :2023/10/17 16:47:30
# @Author    :hyooeewee

import pandas as pd

class Window_action():
    '''窗口操作函数类'''
    pass

class Setting(ConfigParser):
    '''设置相关的函数类'''
    def optionxform(self, optionstr):
        '''重写类，取消大小写不敏感'''
        return optionstr

    def load_setting():
        global UID, USER, PASSWORD, AUTO_LOGIN, REMEMBER_PASSWORD, PROVINCE_CODE
        cf = MyConfigParser()
        cf.read(INI_PATH, encoding='utf-8')
        LOGIN_SETTINGS = cf.items('LOGIN_SETTINGS')
        UID = LOGIN_SETTINGS[0][1]
        USER = LOGIN_SETTINGS[1][1]
        PASSWORD = LOGIN_SETTINGS[2][1]
        AUTO_LOGIN = int(LOGIN_SETTINGS[3][1])
        REMEMBER_PASSWORD = int(LOGIN_SETTINGS[4][1])
        PROVINCE_CODE = cf.items('PROVINCE_CODE')

    def dump_setting():
        global UID, USER, PASSWORD, AUTO_LOGIN, REMEMBER_PASSWORD
        cf = MyConfigParser(comment_prefixes='；', allow_no_value=True)
        cf.read(INI_PATH, encoding='utf-8')
        cf['LOGIN_SETTINGS']['UID'] = str(UID)
        cf['LOGIN_SETTINGS']['USER'] = str(USER)
        cf['LOGIN_SETTINGS']['PASSWORD'] = str(PASSWORD)
        cf['LOGIN_SETTINGS']['AUTO_LOGIN'] = str(AUTO_LOGIN)
        cf['LOGIN_SETTINGS']['REMEMBER_PASSWORD'] = str(REMEMBER_PASSWORD)
        with open(INI_PATH, 'w', encoding='utf-8') as f:
            cf.write(f)

class Multi_Update():
    '''批量下载相关的函数类'''
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

class Utils():
    '''其他不便于归类的函数类'''
    pass

if __name__ == "__main__":
    pass