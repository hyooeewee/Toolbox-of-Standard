#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :main.py
# @Time      :2023/07/28 16:27:35
# @Author    :hyooeewee

"""
 * **************************************************************************
 * ********************                                  ********************
 * ********************              佛祖保佑             ********************
 * ********************                                  ********************
 * **************************************************************************
 *                                                                          *
 *                                   _oo8oo_                                *
 *                                  o8888888o                               *
 *                                  88" . "88                               *
 *                                  (| -_- |)                               *
 *                                  0\  =  /0                               *
 *                                ___/'==='\___                             *
 *                              .' \\|     |// '.                           *
 *                             / \\|||  :  |||// \                          *
 *                            / _||||| -:- |||||_ \                         *
 *                           |   | \\\  -  /// |   |                        *
 *                           | \_|  ''\---/''  |_/ |                        *
 *                           \  .-\__  '-'  __/-.  /                        *
 *                         ___'. .'  /--.--\  '. .'___                      *
 *                      ."" '<  '.___\_<|>_/___.'  >' "".                   *
 *                     | | :  `- \`.:`\ _ /`:.`/ -`  : | |                  *
 *                     \  \ `-.   \_ __\ /__ _/   .-` /  /                  *
 *                 =====`-.____`.___ \_____/ ___.`____.-`=====              *
 *                                   `=---=`                                *
 * **************************************************************************
 * ********************                                  ********************
 * ********************              永不报错             ********************
 * ********************                                  ********************
 * **************************************************************************
 """

# 已知抽象操作，后期优化
# 1.常量应当大写，按需要设置为全局变量
# 2.stackedWidget控件设置得很抽象，部分地方可以使用lable加属性实现
# 3.应当设置用户配置在窗口初始化时引入

import ctypes
import os
import sqlite3
import sys
import time
import webbrowser
from configparser import ConfigParser

from PyQt5 import QtWidgets, uic
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QCursor, QIcon, QMoveEvent
from PyQt5.QtWidgets import (QApplication, QFileDialog, QMainWindow,
                             QMessageBox, QPushButton, QTableWidgetItem)

from standards_spider import *
from UI.res_rc import *
# from UI.LoginUi import Ui_LoginWindow
INI_PATH = r"config.ini"
# INI_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "config.ini")
DATABASE_PATH = r'.\Database\users.db'
LOGIN_SETTINGS = []
UID = ''
USER = ''
PROVINCE_CODE = []

def load_setting():
    global LOGIN_SETTINGS, PROVINCE_CODE
    cf = ConfigParser()
    cf.read(INI_PATH, encoding='utf-8')
    LOGIN_SETTINGS = cf.items('LOGIN_SETTINGS')
    UID = LOGIN_SETTINGS[0][1]
    USER = LOGIN_SETTINGS[1][1]
    PROVINCE_CODE = cf.items('PROVINCE_CODE')

class LoginWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # self.ui = Ui_LoginWindow()
        # self.ui.setupUi(self)
        self.ui = uic.loadUi(r'.\UI\Login.ui', self)

        # 去掉外边框，设置背景透明和图标
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        # 不懂为啥这里是myappid，后面来研究
        self.setWindowIcon(QIcon(r'.\UI\icons\3914110.ico'))
        # 不懂为啥这里是myappid，后面来研究
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("myappid")


        # 添加阴影
        self.shadow = QtWidgets.QGraphicsDropShadowEffect(self)
        self.shadow.setOffset(0, 0)
        self.shadow.setBlurRadius(20)
        self.shadow.setColor(Qt.gray)
        self.ui.frame.setGraphicsEffect(self.shadow)

        # 添加逻辑
        self.ui.pushButton_Login.clicked.connect(lambda: self.ui.stackedWidget_2.setCurrentIndex(0))
        self.ui.pushButton_Register.clicked.connect(lambda: self.ui.stackedWidget_2.setCurrentIndex(1))

        self.ui.pushButton_LSure.clicked.connect(self.login)
        self.ui.checkBox_AutoLogin.isChecked()
        self.ui.checkBox_RememberPassword.isChecked()
        self.ui.checkBox_AutoLogin.stateChanged.connect(lambda: QMessageBox.warning(self, "提示", "功能研发中..."))
        self.ui.checkBox_RememberPassword.stateChanged.connect(lambda: QMessageBox.warning(self, "提示", "功能研发中..."))
        self.ui.pushButton_Forgetpassword.clicked.connect(lambda: QMessageBox.warning(self, "提示", "功能研发中..."))
        if USER:
            self.ui.lineEdit_LAccount.setText(USER)
        
        self.ui.pushButton_RSure.clicked.connect(self.register)

        self.show()

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.m_flag = True
            self.m_Position = event.globalPos()-self.pos()  # 获取鼠标相对窗口的位置
            event.accept()
            self.setCursor(QCursor(Qt.OpenHandCursor))  # 更改鼠标图标

    def mouseMoveEvent(self, QMouseEvent):
        if Qt.LeftButton and self.m_flag:
            self.move(QMouseEvent.globalPos()-self.m_Position)  # 更改窗口位置
            QMouseEvent.accept()

    def mouseReleaseEvent(self, QMouseEvent):
        self.m_flag = False
        self.setCursor(QCursor(Qt.ArrowCursor))

    def login(self):
        global USER, UID
        account = self.ui.lineEdit_LAccount.text()
        password = self.ui.lineEdit_LPassword.text()
        if account and password:
            conn = sqlite3.connect(DATABASE_PATH)
            cur = conn.cursor()
            cur.execute(f'select uids, passwords from users where accounts="{account}"')
            rows = cur.fetchall()
            conn.commit()
            conn.close()
            print(rows)
            if rows:
                for row in rows:
                    if row[1] == password:
                        UID = row[0]
                        self.ui.stackedWidget.setCurrentIndex(0)
                        self.ui.label_Tips.setText('登录成功！')
                        time.sleep(1)
                        break
            else:
                self.ui.stackedWidget.setCurrentIndex(1)
                self.ui.label_Wrong.setText('账号或者密码错误！')
        else:
            self.ui.stackedWidget.setCurrentIndex(1)
            self.ui.label_Wrong.setText('账号或密码不能为空！')
        if UID:
            USER = account
            self.win = MainWindow()
            self.close()

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
                    cur.execute('insert into users values({:.0f}, \'{}\', \'{}\')'.format(time.time(), account, password1))
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
        self.ui = uic.loadUi(r'.\UI\Main.ui', self)
        # self.ui = Ui_MainWindow()
        # self.ui.setupUi(self)
        self.ui.setWindowTitle('标准工具箱')
        self.ui.setWindowIcon(QIcon(r'.\UI\icons\3914110.ico'))
        # 不懂为啥这里是myappid，后面来研究
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("myappid")

        # 添加逻辑
        self.ui.pushButton_Home.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(0))
        self.ui.pushButton_Check.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(1))
        self.ui.pushButton_CheckList.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(2))
        self.ui.pushButton_My.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(3))
        # page 1
        # page 2
        self.ui.comboBox_1.currentIndexChanged.connect(self.standard_CB1)
        self.ui.comboBox_2.hide()
        self.ui.comboBox_2.addItems(['不限'] + [x[0] for x in PROVINCE_CODE])
        # self.ui.comboBox_2.currentIndexChanged.connect(self.standard_CB2)
        self.ui.pushButton_Search.clicked.connect(self.search)
        self.ui.tableWidget.resizeColumnsToContents()
        self.ui.tableWidget.resizeRowsToContents()
        self.ui.pushButton_Export.clicked.connect(self.export)
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

    # def standard_CB2(self):
    #     state = self.ui.comboBox_2.currentText()

    def search(self):
        level = self.ui.comboBox_1.currentText()
        state = self.ui.comboBox_2.currentText()
        status = self.ui.comboBox_3.currentText()
        def regexp(expr, item): 
            reg = re.compile(expr) 
            return reg.search(item) is not None 
        # print(f'level = {level}, state = {state}')
        conn = sqlite3.connect(DATABASE_PATH)
        cur = conn.cursor()
        # if state in ['不限']:
        #     # QMessageBox.warning(self, "提示", "查询中...")
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
        # print(pattarn)
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
        # print(pattarn)
        if pattarn:
            conn.create_function("REGEXP", 2, regexp)
            # print(f"SELECT * FROM standards WHERE {pattarn}")
            cur.execute(f"SELECT * FROM standards WHERE {pattarn}" )
        else:
            cur.execute("SELECT * FROM standards" )
        data = cur.fetchall()
        # print(data)
        conn.commit()
        conn.close()
        y = len(data)
        self.ui.tableWidget.setRowCount(y)
        for iy, i in enumerate(data):
            for ix, v in enumerate(i):
                item = QTableWidgetItem(v)
                self.ui.tableWidget.setItem(iy, ix, item)
        # elif state == '北京市':
        #     state = 11
        #     conn = sqlite3.connect(DATABASE_PATH)
        #     cur = conn.cursor()
        #     conn.create_function("REGEXP", 2, regexp) 
        #     cur.execute(f"SELECT * FROM standards WHERE (StandardNumbers REGEXP '^DB{state}' AND Status='{status}'")
        #     data = cur.fetchall()
        #     print(data)
        #     y = len(data)
        #     self.ui.tableWidget.setRowCount(y)
        #     for iy, i in enumerate(data):
        #         for ix, v in enumerate(i):
        #             item = QTableWidgetItem(v)
        #             self.ui.tableWidget.setItem(iy, ix, item)
        #     conn.close()
        # else:
        #     QMessageBox.warning(self, "提示", "该省级规范正在加速收集中...")
        self.ui.tableWidget.resizeColumnsToContents()
        self.ui.tableWidget.resizeRowsToContents()
         
        
    def export(self):
        # data = DB_data_get.SiChuan()
        # data += DB_data_get.BeiJing()
        data = DB_data_get.TianJin()
        # data = csres_get(self.ui.lineEdit_Search.text())
        if data:
            conn = sqlite3.connect(DATABASE_PATH)
            cur = conn.cursor()
            for i in data:
                try:
                    cur.execute(f"insert into standards values('{i[0]}','{i[1]}','{i[2]}','{i[3]}','{i[4]}','{i[5]}')")
                except:
                    cur.execute(f"update standards set StandardNames='{i[1]}',StartDate='{i[2]}', EndDate='{i[3]}',Status='{i[4]}',DownloadLinks='{i[5]}' where StandardNumbers='{i[0]}'")
            conn.commit()
            conn.close()

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
        directory = QtWidgets.QFileDialog.getExistingDirectory(self,"选取文件夹",os.getcwd())
        # 如果用户选择了文件，打印文件名
        if directory:
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
    # 修改当前工作目录，使得资源文件可以被正确访问
    cd = source_path('')
    os.chdir(cd)

    load_setting()
    load_json()
    app = QApplication(sys.argv)
    win = LoginWindow()
    # win = MainWindow()
    sys.exit(app.exec_())
