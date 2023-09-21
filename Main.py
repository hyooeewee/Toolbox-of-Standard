#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :main.py
# @Time      :2023/09/28 10:40:35
# @Author    :hyooeewee,Mason_Lee
import ctypes
import re
import sqlite3
import sys
import time
import os
import datetime
from configparser import ConfigParser
from PyQt5 import QtWidgets, uic
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QCursor, QIcon
from PyQt5.QtWidgets import (QApplication, QFileDialog, QMainWindow, QMessageBox,QTableWidgetItem)
from standards_spider import *
from UI.res_rc import *

INI_PATH = r"config.ini"
DATABASE_PATH = r'.\Database\users.db'
UID = ''
USER = ''
PASSWORD = ''
AUTO_LOGIN = 0
REMEMBER_PASSWORD = 0
PROVINCE_CODE = []
class MyConfigParser(ConfigParser):
    '''重写类，取消大小写不敏感'''
    def optionxform(self, optionstr):
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

class LoginWindow(QMainWindow): #登录界面的相关函数
    global AUTO_LOGIN, REMEMBER_PASSWORD
    def __init__(self):
        super().__init__()
        self.ui = uic.loadUi(r'.\UI\Login.ui', self)  # 直接将UI文件导入作为显示界面
        self.setWindowFlag(Qt.FramelessWindowHint)  # 去掉外边框
        self.setAttribute(Qt.WA_TranslucentBackground)  # 设置背景透明和图标
        self.label.setStyleSheet('background-color: white;')  # 设置标签
        self.setWindowIcon(QIcon(r'Logo.ico'))  # 设置标题栏logo为Logo.ico
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("myappid")  # myappid是一个占位符，后边可以改成需要的AppUserModelID替换，这个ID是win系统中应用程序的唯一识别码，用于在任务栏中的分组
        self.ui.pushButton_Login.clicked.connect(lambda: self.ui.stackedWidget_2.setCurrentIndex(0))  # 登录页切换
        self.ui.pushButton_Register.clicked.connect(lambda: self.ui.stackedWidget_2.setCurrentIndex(1))  # 注册页切换
        self.ui.pushButton_LSure.clicked.connect(self.local_login)  # 点击登录按钮，连接至login函数
        self.ui.checkBox_RememberPassword.setChecked(REMEMBER_PASSWORD)  # 记住密码相关检测
        if self.ui.checkBox_RememberPassword.isChecked():
            self.ui.lineEdit_LPassword.setText(PASSWORD)
            self.ui.checkBox_AutoLogin.setChecked(AUTO_LOGIN)
        self.ui.checkBox_AutoLogin.stateChanged.connect(self.auto_login)
        self.ui.checkBox_RememberPassword.stateChanged.connect(self.remember_number)
        self.ui.pushButton_Forgetpassword.clicked.connect(lambda: QMessageBox.warning(self, "提示", "功能研发中..."))
        if USER:
            self.ui.lineEdit_LAccount.setText(USER)
        self.ui.pushButton_RSure.clicked.connect(self.register)
        self.show()
        if self.ui.checkBox_AutoLogin.isChecked():
            self.local_login()

    def mousePressEvent(self, event):  # 拖动窗口时，述标变成小手，这个函数为检测点击的位置
        if event.button() == Qt.LeftButton:
            self.m_flag = True
            self.m_Position = event.globalPos() - self.pos()  # 获取鼠标相对窗口的位置
            event.accept()
            self.setCursor(QCursor(Qt.OpenHandCursor))  # 更改鼠标图标

    def mouseMoveEvent(self, QMouseEvent):  # 拖动窗口时，述标变成小手，这个函数为拖动的函数
        if Qt.LeftButton and self.m_flag:
            self.move(QMouseEvent.globalPos() - self.m_Position)  # 更改窗口位置
            QMouseEvent.accept()

    def mouseReleaseEvent(self, QMouseEvent):  # 拖动窗口时，述标变成小手，这个函数为释放的函数
        self.m_flag = False
        self.setCursor(QCursor(Qt.ArrowCursor))

    def auto_login(self):  # 自动登录相关函数
        global AUTO_LOGIN, REMEMBER_PASSWORD
        if self.ui.checkBox_AutoLogin.isChecked():
            REMEMBER_PASSWORD = 1
            AUTO_LOGIN = 1
            self.ui.checkBox_RememberPassword.setChecked(REMEMBER_PASSWORD)
        else:
            AUTO_LOGIN = 0

    def remember_number(self):  # 记住账号密码检测函数
        global AUTO_LOGIN, REMEMBER_PASSWORD
        if self.ui.checkBox_RememberPassword.isChecked():
            REMEMBER_PASSWORD = 1
        else:
            AUTO_LOGIN = 0
            REMEMBER_PASSWORD = 0
            self.ui.checkBox_AutoLogin.setChecked(AUTO_LOGIN)

    def local_login(self):
        global UID, USER, PASSWORD
        account = self.ui.lineEdit_LAccount.text()
        password = self.ui.lineEdit_LPassword.text()
        if account and password:
            conn = sqlite3.connect(DATABASE_PATH)
            cur = conn.cursor()
            cur.execute(f'select uids, passwords from users where accounts="{account}"')
            rows = cur.fetchall()
            conn.commit()
            conn.close()
            # print(rows)
            if rows:
                for row in rows:
                    if row[1] == password:
                        UID = row[0]
                        USER = account
                        PASSWORD = password
                        dump_setting()
                        self.ui.stackedWidget.setCurrentIndex(0)
                        self.ui.label_Tips.setText('登录成功！')
                        self.close()
                        MainWindow()
            else:
                self.ui.stackedWidget.setCurrentIndex(1)
                self.ui.label_Wrong.setText('账号或者密码错误！')
        else:
            self.ui.stackedWidget.setCurrentIndex(1)
            self.ui.label_Wrong.setText('账号或密码不能为空！')

    def forget_password(self):
        self.ui.stackedWidget.setCurrentIndex(1)
        self.ui.label_Wrong.setText('功能研发中！')

    def register(self):
        account = self.ui.lineEdit_RAccount.text()
        password1 = self.ui.lineEdit_RPassword1.text()
        password2 = self.ui.lineEdit_RPassword2.text()
        if account and password1 and password2:
            if password1 == password2:
                conn = sqlite3.connect(DATABASE_PATH)
                cur = conn.cursor()
                cur.execute(f'select uids, passwords from users where accounts="{account}"')
                rows = cur.fetchall()
                if rows:
                    self.ui.stackedWidget.setCurrentIndex(1)
                    self.ui.label_Wrong.setText('账户已存在！')
                    self.ui.lineEdit_RAccount.setText()
                    self.ui.lineEdit_RPassword1.setText()
                    self.ui.lineEdit_RPassword2.setText()
                else:
                    cur.execute(
                        'insert into users values({:.0f}, \'{}\', \'{}\')'.format(time.time(), account, password1))
                    conn.commit()
                conn.close()
                self.ui.stackedWidget.setCurrentIndex(0)
                self.ui.label_Tips.setText('注册成功！')
                time.sleep(1)
                self.ui.stackedWidget_2.setCurrentIndex(0)
            else:
                self.ui.stackedWidget.setCurrentIndex(1)
                self.ui.label_Wrong.setText('两次输入密码不一致！')
        else:
            self.ui.stackedWidget.setCurrentIndex(1)
            self.ui.label_Wrong.setText('请填写完整！')


class MainWindow(QMainWindow):
    def __init__(self):
        global PROVINCE_CODE
        super().__init__()
        self.ui = uic.loadUi(r'.\UI\Main.ui', self)  # 直接引用UI文件作为窗口
        self.ui.setWindowTitle('规范通V1.0')  # 命名标题
        self.ui.setWindowIcon(QIcon(r'.\UI\icons\3914110.ico'))  # 设置logo
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("myappid")
        self.ui.pushButton_Home.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(0))
        self.ui.pushButton_Check.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(1))
        self.ui.pushButton_CheckList.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(2))
        self.ui.pushButton_Generate.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(3))
        self.ui.pushButton_News.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(4))
        self.ui.pushButton_My.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(5))
        # page 1
        self.ui.label_LocalDB_V.setText(str(datetime.datetime.fromtimestamp(os.path.getmtime(os.getcwd()+ "/Database/users.db"))))
        self.ui.label_UserName.setText(str(USER))
        self.ui.pushButton_Export.clicked.connect(self.show_confirmation_dialog)
        # page 2
        self.ui.comboBox_1.currentIndexChanged.connect(self.standard_CB1)
        self.ui.comboBox_2.hide()
        self.ui.comboBox_2.addItems(['不限'] + [x[0] for x in PROVINCE_CODE])
        self.tableWidget.setColumnWidth(0, 120)
        self.tableWidget.setColumnWidth(1, 190)
        self.tableWidget.setColumnWidth(2, 80)
        self.tableWidget.setColumnWidth(3, 80)
        self.tableWidget.setColumnWidth(4, 80)
        self.tableWidget.setColumnWidth(5, 80)
        self.ui.pushButton_Search.clicked.connect(self.search)
        self.ui.tableWidget.resizeColumnsToContents()
        self.ui.tableWidget.resizeRowsToContents()
        self.ui.tableWidget.resizeColumnsToContents()
        # page 3
        self.ui.pushButton_CLOpen1.clicked.connect(self.select_file1)
        self.ui.pushButton_CLOpen2.clicked.connect(self.select_file2)
        self.ui.pushButton_Update.clicked.connect(self.update)
        # page 4
        self.ui.pushButton_MSure.clicked.connect(self.change_password)
        self.show()

    def standard_CB1(self):
        level = self.ui.comboBox_1.currentText()
        if level == '地标':
            self.ui.comboBox_2.show()
        else:
            self.ui.comboBox_2.hide()

    def search(self):
        level = self.ui.comboBox_1.currentText()
        state = self.ui.comboBox_2.currentText()
        status = self.ui.comboBox_3.currentText()
        def regexp(expr, item):
            reg = re.compile(expr)
            return reg.search(item) is not None
        conn = sqlite3.connect(DATABASE_PATH)
        cur = conn.cursor()
        pattarn = p1 = p2 = p3 = ''
        if level == '国标':
            pattarn = 'GB'
        elif level == '地标':
            pattarn = 'DB'
            if state != '不限':
                pattarn += [x[1] for x in PROVINCE_CODE if x[0] == state][0]
        elif level == '行标':
            pattarn = ''
        elif level == '团标':
            pattarn = ''
        else:
            pattarn = ''
        if pattarn:
            p1 = f"StandardNumbers REGEXP '^{pattarn}'"
        if status != '不限':
            p2 = f"Status='{status}'"
        if self.ui.lineEdit_Search.text():
            p3 = f"(StandardNumbers  LIKE '%{self.ui.lineEdit_Search.text()}%' OR StandardNames LIKE '%{self.ui.lineEdit_Search.text()}%')"
        if p1:
            pattarn = p1
            if p2:
                pattarn += ' AND ' + p2
                if p3:
                    pattarn += ' AND ' + p3
        elif p2:
            pattarn = p2
            if p3:
                pattarn += ' AND ' + p3
        elif p3:
            pattarn = p3
        else:
            pattarn = ''
        if pattarn:
            conn.create_function("REGEXP", 2, regexp)
            cur.execute(f"SELECT * FROM standards WHERE {pattarn}")
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
        self.tableWidget.setColumnWidth(0, 120)
        self.tableWidget.setColumnWidth(1, 190)
        self.tableWidget.setColumnWidth(2, 80)
        self.tableWidget.setColumnWidth(3, 80)
        self.tableWidget.setColumnWidth(4, 80)
        self.tableWidget.setColumnWidth(5, 80)
    def select_file1(self):
        # 调用QFileDialog.getOpenFileName方法，弹出文件选择窗口
        # 参数依次为：父窗口、标题、默认目录、文件类型过滤器、选项
        fileName, _ = QFileDialog.getOpenFileName(self, '选择文件', os.getcwd(), '所有文件(*);;表格文件(*.xlxs, *.xls)')
        # 如果用户选择了文件，打印文件名
        if fileName:
            self.ui.lineEdit_CLOpen1.setText(fileName)

    def select_file2(self):
        # 调用QFileDialog.getOpenFileName方法，弹出文件选择窗口
        # 参数依次为：父窗口、标题、默认目录、文件类型过滤器、选项
        directory = QtWidgets.QFileDialog.getExistingDirectory(self, "选取文件夹", os.getcwd())
        if directory:           # 如果用户选择了文件，打印文件名
            self.ui.lineEdit_CLOpen2.setText(directory)

    def update(self):
        QMessageBox.warning(self, "提示", "功能研发中...")

    def change_password(self):
        global UID
        password1 = self.ui.lineEdit_MPassword1.text()
        password2 = self.ui.lineEdit_MPassword2.text()
        if password1 and password2:
            if password1 == password2:
                conn = sqlite3.connect(DATABASE_PATH)
                cur = conn.cursor()
                cur.execute(f'select passwords from users where uids="{UID}"')
                rows = cur.fetchall()
                if rows[0] == password1:
                    self.ui.stackedWidget_2.setCurrentIndex(1)
                    self.ui.label_MWrong.setText('新密码不能与原密码相同！')
                else:
                    cur.execute(f'update users set passwords="{password1}" where uids={UID}')
                    self.ui.stackedWidget_2.setCurrentIndex(0)
                    self.ui.label_MTips.setText('修改成功！')
                conn.commit()
                conn.close()
            else:
                self.ui.stackedWidget_2.setCurrentIndex(1)
                self.ui.label_MWrong.setText('输入不一致！')
        else:
            self.ui.stackedWidget_2.setCurrentIndex(1)
            self.ui.label_MWrong.setText('输入不完整！')

    def export(self):   #数据库操作的部分单独拿出来，data从get_data里边获取，方便日后修改至远程端
        # data = DB_data_get.Beijing()
        # data = DB_data_get.Tianjin()
        # data = DB_data_get.Hebei()
        # data = DB_data_get.Shanghai()
        data = DB_data_get.Sichuan()


        # data = DB_data_get.Sanxi()
        # data = DB_data_get.Neimenggu()
        # data = DB_data_get.Liaoning()
        # data = DB_data_get.Jilin()
        # data = DB_data_get.Heilongjiang()
        # data = DB_data_get.Jiangsu()
        # data = DB_data_get.ZheJiang()
        # data = DB_data_get.Anhui()
        # data = DB_data_get.Fujian()
        # data = DB_data_get.Jiangxi()
        # data = DB_data_get.Shandong()
        # data = DB_data_get.Henan()
        # data = DB_data_get.Hubei()
        # data = DB_data_get.Hunan()
        # data = DB_data_get.Guangdong()
        # data = DB_data_get.Guangxi()
        # data = DB_data_get.Hainan()
        # data = DB_data_get.Chongqing()
        # data = DB_data_get.Guizhou()
        # data = DB_data_get.Yunnan()
        # data = DB_data_get.Xizang()
        # data = DB_data_get.Shanxi()
        # data = DB_data_get.Gansu()
        # data = DB_data_get.Qinghai()
        # data = DB_data_get.Ningxia()
        # data = DB_data_get.Xinjiang()
        # data = DB_data_get.Taiwan()
        # data = DB_data_get.Hongkong()
        # data = DB_data_get.Macau()
        if data:
            conn = sqlite3.connect(DATABASE_PATH)
            cur = conn.cursor()
            for i in data:
                try:
                    cur.execute(f"insert into standards values('{i[0]}','{i[1]}','{i[2]}','{i[3]}','{i[4]}','{i[5]}','{i[6]}','{i[7]}','{i[8]}')")
                except:
                    cur.execute(f"update standards set StandardNames='{i[1]}',StartDate='{i[2]}', EndDate='{i[3]}',Status='{i[4]}',DownloadLinks='{i[5]}',TYPE='{i[6]}',HEADERS='{i[7]}',UPDATE_TIME='{i[8]}' where StandardNumbers='{i[0]}'")
            conn.commit()
            conn.close()
            self.ui.label_LocalDB_V.setText(str(datetime.datetime.fromtimestamp(
                os.path.getmtime(os.getcwd() + "/Database/users.db"))))  # 数据库写入完成后，更新本地数据库时间

    def show_confirmation_dialog(self):
        # 创建一个确认对话框
        confirmation = QMessageBox()
        confirmation.setWindowTitle("数据库更新确认")
        confirmation.setText("更新数据库时间可能较长，过程中本程序无法使用，是否需要更新")
        confirmation.setIcon(QMessageBox.Question)
        confirmation.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        # 显示对话框并获取用户的选择
        user_choice = confirmation.exec_()
        # 根据用户选择执行相应的操作
        if user_choice == QMessageBox.Ok:
            self.export()
        else:
            print("操作已取消")

def save_setting():
    print('save setting')
    pass

def load_json():
    pass

# 资源文件目录访问
def source_path(relative_path):
    # 是否Bundle Resource
    if getattr(sys, 'frozen', False):
        base_path = sys._MEIPASS
    else:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)



if __name__ == "__main__":
    # 修改当前工作目录，使得资源文件可以被正确访问，打包需要
    cd = source_path('')
    os.chdir(cd)

    load_setting()
    load_json()
    app = QApplication(sys.argv)
    win = LoginWindow()
    # win = MainWindow()
    sys.exit(app.exec_())
