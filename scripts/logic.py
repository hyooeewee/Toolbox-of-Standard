#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :logic.py
# @Time      :2023/10/17 16:47:30
# @Author    :hyooeewee

import pandas as pd
from configparser import ConfigParser
from PyQt5.QtWidgets import QMessageBox, QApplication
from PyQt5.QtCore import QTimer, QThread, pyqtSignal
from PyQt5.QtGui import QIcon
import time
import re
import sqlite3
import os

INI_PATH = r".\resources\config.ini"
JSON_PATH = r".\resources\info.json"
ICON_PATH = r".\resources\Logo.ico"
DATABASE_PATH = r'.\database\users.db'


class DB_Action():
    """ 
    操作本地数据库
    :param act_type:操作类型,增删改查,默认为查
    :param sql_chain:SQL的语句链,仅str支持fetchall
     """
    def __init__(self, sql_chain: str|list, act_type=3) -> None:
        self.act_type = act_type
        self.sql_chain = sql_chain

    def act(self) -> None:
        conn = sqlite3.connect(DATABASE_PATH)
        cur = conn.cursor()
        if type(self.sql_chain) is str:
            try:
                cur.execute(self.sql_chain)
                if self.act_type == 3:
                    return cur.fetchall()
                else:
                    conn.commit()
            except:
                print('str')
            finally:
                conn.close()
        elif type(self.sql_chain) is list:
            try:
                for lang in self.sql_chain:
                    cur.execute(lang)
                    if self.act_type == 3:
                        return cur.fetchall()
                    else:
                        conn.commit()
            except:
                pass
            finally:
                conn.close()
        else:
            print('参数类型错误')


class MyMessageBox(QMessageBox):
    '''定时关闭的提示框
    :param ICON:窗口的图标；
    :param title:显示的窗口标题；
    :param icon:显示的图标；
    :param text:显示的文本；
    :param delay:延时关闭的时间，毫秒。
    '''

    def __init__(self, ICON='', title="提示", text="操作成功", delay=3000):
        super(MyMessageBox, self).__init__()
        self.setWindowTitle(title)
        if ICON:
            self.setWindowIcon(ICON)
        # self.setIcon(icon)
        self.setText(text)
        self.delay = delay
        self.exec()

    def showEvent(self, event):
        QTimer().singleShot(self.delay, self.close)
        super(MyMessageBox, self).showEvent(event)


class MyConfigParser(ConfigParser):
    def optionxform(self, optionstr):
        '''重写类，取消大小写不敏感'''
        return optionstr


class Setting():
    '''设置初始化等相关的函数类'''
    def load_setting():
        global UID, USER, PASSWORD, AUTO_LOGIN, REMEMBER_PASSWORD, PROVINCE_CODE, ICON
        cf = MyConfigParser()
        cf.read(INI_PATH, encoding='utf-8')
        LOGIN_SETTINGS = cf.items('LOGIN_SETTINGS')
        UID = LOGIN_SETTINGS[0][1]
        USER = LOGIN_SETTINGS[1][1]
        PASSWORD = LOGIN_SETTINGS[2][1]
        AUTO_LOGIN = int(LOGIN_SETTINGS[3][1])
        REMEMBER_PASSWORD = int(LOGIN_SETTINGS[4][1])
        PROVINCE_CODE = cf.items('PROVINCE_CODE')
        print('设置读取完毕！！！')
        return UID, USER, PASSWORD, AUTO_LOGIN, REMEMBER_PASSWORD, PROVINCE_CODE

    def dump_setting(UID, USER, PASSWORD, AUTO_LOGIN, REMEMBER_PASSWORD):
        cf = MyConfigParser(comment_prefixes='；', allow_no_value=True)
        cf.read(INI_PATH, encoding='utf-8')
        cf['LOGIN_SETTINGS']['UID'] = str(UID)
        cf['LOGIN_SETTINGS']['USER'] = str(USER)
        cf['LOGIN_SETTINGS']['PASSWORD'] = str(PASSWORD)
        cf['LOGIN_SETTINGS']['AUTO_LOGIN'] = str(AUTO_LOGIN)
        cf['LOGIN_SETTINGS']['REMEMBER_PASSWORD'] = str(REMEMBER_PASSWORD)
        with open(INI_PATH, 'w', encoding='utf-8') as f:
            cf.write(f)
        print('设置保存完毕！！！')

    def load_json():
        """ 加载json文件 """
        return JSON_PATH

    def save_setting():
        """ 保存设置 """
        return 1


class Multi_Update(QThread):
    '''批量更新线程函数类'''
    max_signal = pyqtSignal(int)
    cur_signal = pyqtSignal(int)
    def __init__(self, fileName: str, directory: str) -> None:
        super(Multi_Update, self).__init__()
        self.fileName = fileName
        self.directory = directory
        print('init')

    def run(self):
        print('读取数据')
        self.read_data()
        if not self.df.empty:
            print('比对数据')
            self.max_signal.emit(len(self.df))
            self.cpar_data()
            print('写入数据')
            self.dump_data()

    def read_data(self):
        """ 读取数据 """
        # 默认读取第一个sheet，之后为了避免出现问题要做用户选择界面
        self.df = pd.read_excel(self.fileName, sheet_name="Sheet1")
        # self.data = dict(zip(self.df.iloc[:, 1], self.df.iloc[:, 3]))
        # print(len(self.data))
        print(len(self.df))
        # print(self.df)


    def cpar_data(self):
        """ 比对数据 """
        # 查询数据
        for i, item in enumerate(self.df.iloc[:, 1]):
            # 数据库查询
            self.cur_signal.emit(i)
            print(i, item, sep='')
            # self.status_signal.emit(i)
            # print(self.df.iloc[:, 3][1])     
            try:
                res = DB_Action(f'SELECT * FROM standards WHERE StandardNames is "{item}"', 3).act()
                print(res)
                if res:
                    sorted(res, key=lambda i: i[2])
                    if self.df.iloc[:, 3][1] and self.df.iloc[:, 3][1] >= res[-1][2]:
                        # 无更新
                        print('无更新')
                        self.df.iloc[i, 5] = '无更新'
                    else:
                        # 有更新
                        print('有更新')
                        self.df.iloc[i, 4] = self.df.iloc[i, 2]
                        self.df.iloc[i, 3] = res[-1][0]
                        self.df.iloc[i, 5] = '有更新'
                else:
                    # 无数据
                    print('无数据')
                    self.df.iloc[i, 5] = '无数据'
                print(self.df)
            except:
                # 出错了
                print('出错了')

    def dump_data(self) -> None:
        """ 装载数据 """
        self.df.to_excel(os.path.join(self.directory, r'output.xlsx'), index=None)


class Utils():
    '''其他不便于归类的函数类'''
    pass


if __name__ == "__main__":
    # app = QApplication([])  # 创建应用对象
    # MyMessageBox()
    mu = Multi_Update(r"test\input.xlsx", r"test")
    mu.read_data()
    mu.cpar_data()
    mu.dump_data()