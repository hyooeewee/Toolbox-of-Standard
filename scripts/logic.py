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

INI_PATH = r".\resources\config.ini"
JSON_PATH = r".\resources\info.json"
ICON_PATH = r".\resources\Logo.ico"
DATABASE_PATH = r'.\database\users.db'

class DB_Action():
    """ 
    操作本地数据库
    :param act_type:操作类型,增删改查,默认为查
     """
    def __init__(self, act_type=3, sql_query=None: list) -> None:
        self.type = act_type
        self.sql_query = sql_query
    
    def act(self)
        conn = sqlite3.connect(DATABASE_PATH)
        cur = conn.cursor()
        if 
        try:
            cur.execute(self.sql_query)
        except:
            conn.commit()
        finally:
            conn.close()
            
class MyMessageBox(QMessageBox):
    '''定时关闭的提示框
    :param ICON:窗口的图标；
    :param title:显示的窗口标题；
    :param icon:显示的图标；
    :param text:显示的文本；
    :param delay:延时关闭的时间，毫秒。
    '''
    def __init__(self, ICON='', title="提示",text="操作成功", delay=3000):
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
    '''批量下载相关的函数类'''
    status_signal = pyqtSignal(int)
    def run(self):
        self.read_data()
        self.cpar_data()
        self.dump_data()
        self.status_signal.emit(i)

    def read_data(self, fileName):
        """ 读取数据 """
        # 默认读取第一个sheet，之后为了避免出现问题要做用户选择界面
        self.df = pd.read_excel(fileName, sheet_name="Sheet1")
        self.data = dict(zip(df.iloc[:, 1], df.iloc[:, 2]))
    
    def cpar_data(self):
        """ 比对数据 """
        pass

    def dump_data(self) -> int:
        """ 装载数据 """
        pass

class Utils():
    '''其他不便于归类的函数类'''
    pass


if __name__ == "__main__":
    app = QApplication([])  # 创建应用对象
    MyMessageBox()
