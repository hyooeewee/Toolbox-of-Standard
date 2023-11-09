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
import urllib
import urllib.request
import webbrowser

import requests
from PyQt5 import QtWidgets, uic
from PyQt5.QtCore import Qt, QUrl, QThread, pyqtSignal, QDate
from PyQt5.QtGui import QCursor, QIcon, QColor
from PyQt5.QtWidgets import (
    QApplication, QFileDialog, QMainWindow, QMessageBox, QTableWidgetItem, QGraphicsDropShadowEffect, QDialog,
    QTableWidget)
from UI.res_rc import *
from PyQt5.QtWebEngineWidgets import QWebEngineView
from scripts.download import *
from scripts.logic import *
from scripts.logic import *
from scripts import News_Search
from web import app
import multiprocessing

INI_PATH = r".\resources\config.ini"
ICON_PATH = r".\resources\Logo.ico"
DATABASE_PATH = r'.\database\users.db'
UID = ''
USER = ''
PASSWORD = ''
AUTO_LOGIN = 0
REMEMBER_PASSWORD = 0
PROVINCE_CODE = []
online_db_config = {
    'host': '123.60.58.210',  # 远程MySQL数据库的主机地址（IP地址或域名）
    'user': 'root',  # 远程MySQL数据库的用户名
    'password': 'CLFZZRe5Mn27w72y',  # 远程MySQL数据库的密码
    'database': 'standard_db',  # 要连接的数据库名称
    'port': 5896  # MySQL默认端口号
}

class LoginWindow(QMainWindow):
    '''登录界面'''

    def __init__(self):
        super().__init__()
        self.m_flag = False
        self.ui = uic.loadUi(r'.\UI\Login.ui', self)  # 直接将UI文件导入作为显示界面
        self.setWindowFlag(Qt.FramelessWindowHint)  # 去掉外边框
        self.setAutoFillBackground(True)  # 一定要加上
        self.setAttribute(Qt.WA_TranslucentBackground)  # 窗口透明
        # self.shadow = QGraphicsDropShadowEffect()  # 创建阴影
        # self.shadow.setBlurRadius(5)  # 阴影模糊半径
        # self.shadow.setColor(QColor("#444444"))  # 设置颜色透明度为100的（0,0,0）黑色
        # self.shadow.setOffset(0, 5)  # 阴影的偏移值
        # self.setGraphicsEffect(self.shadow)  # 添加阴影
        self.setWindowIcon(QIcon(ICON_PATH))  # 设置标题栏logo为Logo.ico
        # myappid是一个占位符，后边可以改成需要的AppUserModelID替换，这个ID是win系统中应用程序的唯一识别码，用于在任务栏中的分组
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(
            "myappid")

        self.ui.pushButton_Login.clicked.connect(
            lambda: self.ui.stackedWidget_2.setCurrentIndex(0))  # 登录页切换
        self.ui.pushButton_Register.clicked.connect(
            lambda: self.ui.stackedWidget_2.setCurrentIndex(1))  # 注册页切换
        self.ui.pushButton_LSure.clicked.connect(
            self.local_login)  # 点击登录按钮，连接至login函数
        self.ui.checkBox_RememberPassword.setChecked(REMEMBER_PASSWORD)
        if self.ui.checkBox_RememberPassword.isChecked():
            self.ui.lineEdit_LPassword.setText(PASSWORD)
            self.ui.checkBox_AutoLogin.setChecked(AUTO_LOGIN)
        self.ui.checkBox_AutoLogin.stateChanged.connect(self.auto_login)
        self.ui.checkBox_RememberPassword.stateChanged.connect(
            self.remember_number)
        self.ui.pushButton_Forgetpassword.clicked.connect(
            lambda: QMessageBox.warning(self, "提示", "功能研发中..."))
        if USER:
            self.ui.lineEdit_LAccount.setText(USER)
        self.ui.pushButton_RSure.clicked.connect(self.register)
        self.show()
        if self.ui.checkBox_AutoLogin.isChecked():
            self.local_login()

    def mousePressEvent(self, event):  # 检测点击的位置
        self.m_Position = event.globalPos() - self.pos()  # 获取鼠标相对窗口的位置
        if event.button() == Qt.LeftButton:
            self.m_flag = True
            event.accept()

    def mouseMoveEvent(self, QMouseEvent):  # 拖动的函数
        if Qt.LeftButton and self.m_flag:
            self.setCursor(QCursor(Qt.OpenHandCursor))  # 更改鼠标图标
            self.move(QMouseEvent.globalPos() - self.m_Position)  # 更改窗口位置
            QMouseEvent.accept()

    def mouseReleaseEvent(self, QMouseEvent):  # 释放的函数
        self.setCursor(QCursor(Qt.ArrowCursor))

    def auto_login(self):  # 自动登录相关函数
        global AUTO_LOGIN, REMEMBER_PASSWORD
        if self.ui.checkBox_AutoLogin.isChecked():
            REMEMBER_PASSWORD = 1
            AUTO_LOGIN = 1
            self.ui.checkBox_RememberPassword.setChecked(REMEMBER_PASSWORD)
        else:
            AUTO_LOGIN = 0
        if not REMEMBER_PASSWORD:
            UID = USER = PASSWORD = ''

    def remember_number(self):  # 记住账号密码检测函数
        global AUTO_LOGIN, REMEMBER_PASSWORD
        if self.ui.checkBox_RememberPassword.isChecked():
            REMEMBER_PASSWORD = 1
        else:
            AUTO_LOGIN = 0
            REMEMBER_PASSWORD = 0
            self.ui.checkBox_AutoLogin.setChecked(AUTO_LOGIN)

    def local_login(self):  # 获取输入的账号和密码，与本地数据库进行比对，这个函数后期要改成在线验证，通过GET获取
        global UID, USER, PASSWORD
        account = self.ui.lineEdit_LAccount.text()
        password = self.ui.lineEdit_LPassword.text()
        if account and password:
            conn = sqlite3.connect(DATABASE_PATH)
            cur = conn.cursor()
            cur.execute(
                f'select uids, passwords from users where accounts="{account}"')
            rows = cur.fetchall()
            conn.close()
            if rows:
                for row in rows:
                    if row[1] == password:
                        UID = row[0]
                        USER = account
                        PASSWORD = password
                        Setting.dump_setting(
                            UID, USER, PASSWORD, AUTO_LOGIN, REMEMBER_PASSWORD)
                        MyMessageBox(QIcon(ICON_PATH), '提示', '登录成功！！！', 2000)
                        self.close()
                        MainWindow()
                    else:
                        MyMessageBox(QIcon(ICON_PATH), '提示', '账号或者密码错误！', 1000)
        else:
            MyMessageBox(QIcon(ICON_PATH), '提示', '账号或密码不能为空！', 1000)

    def forget_password(self):  # 忘记密码
        pass

    def register(self):  # 注册账户，和本地数据库进行比对
        account = self.ui.lineEdit_RAccount.text()
        password1 = self.ui.lineEdit_RPassword1.text()
        password2 = self.ui.lineEdit_RPassword2.text()
        if account and password1 and password2:
            if password1 == password2:
                conn = sqlite3.connect(DATABASE_PATH)
                cur = conn.cursor()
                cur.execute(
                    f'select uids, passwords from users where accounts="{account}"')
                rows = cur.fetchall()
                if rows:
                    MyMessageBox(QIcon(ICON_PATH), '提示', '账户已存在！', 1000)
                    self.ui.lineEdit_RAccount.setText()
                    self.ui.lineEdit_RPassword1.setText()
                    self.ui.lineEdit_RPassword2.setText()
                else:
                    cur.execute(
                        'insert into users values({:.0f}, \'{}\', \'{}\')'.format(time.time(), account, password1))
                    conn.commit()
                conn.close()
                MyMessageBox(QIcon(ICON_PATH), '提示', '注册成功！', 1000)
                self.ui.stackedWidget_2.setCurrentIndex(0)
            else:
                MyMessageBox(QIcon(ICON_PATH), '提示', '两次输入密码不一致！', 1000)
        else:
            MyMessageBox(QIcon(ICON_PATH), '提示', '请填写完整！', 1000)


class MainWindow(QMainWindow):
    """ main window """
    def __init__(self):
        global PROVINCE_CODE
        super().__init__()

        self.m_flag = False
        self.ui = uic.loadUi(r'.\UI\Main.ui', self)  # 直接引用UI文件作为窗口
        self.setWindowFlag(Qt.FramelessWindowHint)  # 去掉外边框
        self.setAutoFillBackground(True)  # 一定要加上
        self.setAttribute(Qt.WA_TranslucentBackground)  # 窗口透明
        # self.shadow = QGraphicsDropShadowEffect()  # 创建阴影
        # self.shadow.setBlurRadius(5)  # 设置阴影大小为5px
        # self.shadow.setColor(QColor("#444444"))  # 设置颜色透明度为100的（0,0,0）黑色
        # self.shadow.setOffset(2, 2)  # 阴影偏移距离为0px
        # self.setGraphicsEffect(self.shadow)  # 添加阴影
        self.setWindowIcon(QIcon(ICON_PATH))  # 设置标题栏logo为Logo.ico
        # myappid是一个占位符，后边可以改成需要的AppUserModelID替换，这个ID是win系统中应用程序的唯一识别码，用于在任务栏中的分组
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(
            "myappid")
        if self.ui.pushButton_Home.isChecked():
            self.ui.stackedWidget.setCurrentIndex(0)
        self.ui.pushButton_Home.clicked.connect(
            lambda: self.ui.stackedWidget.setCurrentIndex(0))
        self.ui.pushButton_Check.clicked.connect(
            lambda: self.ui.stackedWidget.setCurrentIndex(1))
        self.ui.pushButton_CheckList.clicked.connect(
            lambda: self.ui.stackedWidget.setCurrentIndex(2))
        # self.ui.pushButton_Generate.clicked.connect(
        #     lambda: self.ui.stackedWidget.setCurrentIndex(3))
        self.ui.pushButton_News.clicked.connect(
            lambda: self.ui.stackedWidget.setCurrentIndex(4))
        self.ui.pushButton_About.clicked.connect(
            lambda: self.ui.stackedWidget.setCurrentIndex(5))
        # page init
        self.ui.pushButton_back.hide()
        self.ui.pushButton_max.clicked.connect(
            lambda: (self.ui.pushButton_back.show(), self.ui.pushButton_max.hide()))
        self.ui.pushButton_back.clicked.connect(
            lambda: (self.ui.pushButton_back.hide(), self.ui.pushButton_max.show()))
        # page 1
        self.ui.label_LocalDB_V.setText(
            str(datetime.datetime.fromtimestamp(os.path.getmtime(
                os.getcwd() + "/Database/users.db"))).split('.')[0]
        )
        self.ui.label_OnlineDB_V.setText(self.online_db_version())
        self.ui.label_UserName.setText(str(USER))
        self.ui.pushButton_Export.clicked.connect(
        self.show_confirmation_dialog)
        # page 2
        self.K_background()
        self.ui.comboBox_1.currentIndexChanged.connect(self.standard_CB1)
        self.ui.comboBox_2.hide()
        self.ui.comboBox_2.addItems(['不限'] + [x[0] for x in PROVINCE_CODE])
        self.ui.tableWidget.horizontalHeader().setVisible(True)
        self.ui.pushButton_Search.clicked.connect(self.search)
        self.ui.tableWidget.resizeColumnsToContents()
        self.ui.tableWidget.resizeRowsToContents()
        self.ui.tableWidget.resizeColumnsToContents()
        self.ui.tableWidget.setColumnWidth(0, 200)
        self.ui.tableWidget.setColumnWidth(1, 190)
        self.ui.tableWidget.setColumnWidth(2, 100)
        self.ui.tableWidget.setColumnWidth(3, 100)
        self.ui.tableWidget.setColumnWidth(4, 60)
        self.ui.tableWidget.setColumnWidth(5, 60)
        self.ui.pushButton_DownLoad.clicked.connect(self.PDF_DOWNLOAD)
        self.ui.pushButton_K.clicked.connect(self.toggle_new_dialog)
        self.WEB_engine = None  # 用于跟踪新界面的状态
        self.ui.tableWidget.setSelectionBehavior(QTableWidget.SelectRows)  # 设置选择整行
        self.ui.tableWidget.itemSelectionChanged.connect(self.onItemSelected)  #传递表格变化的信号到槽函数
        # page 3
        self.ui.pushButton_CLOpen1.clicked.connect(self.select_file1)
        self.ui.pushButton_CLOpen2.clicked.connect(self.select_file2)
        self.ui.pushButton_Update.clicked.connect(self.update)
        # page 4
        # page 5
        self.ui.pushButton_Search_3.clicked.connect(self.News_Search)
        self.ui.pushButton_NEWS.clicked.connect(self.open_News)
        self.ui.dateEdit_4.setDate(QDate.currentDate())
        self.ui.dateEdit_3.setDate(QDate.currentDate().addDays(-180))
        self.ui.tableWidget_News.setColumnWidth(0, 400)
        self.ui.tableWidget_News.setColumnWidth(1, 100)
        self.ui.tableWidget_News.setColumnWidth(2, 100)
        self.ui.tableWidget_News.setColumnWidth(3, 100)
        self.ui.tableWidget_News.setColumnWidth(4, 200)

        # page 6
        self.ui.pushButton_MSure.clicked.connect(self.change_password)
        self.show()

    def mousePressEvent(self, event):  # 检测点击的位置
        self.m_Position = event.globalPos() - self.pos()  # 获取鼠标相对窗口的位置
        if event.button() == Qt.LeftButton:
            self.m_flag = True
            event.accept()

    def mouseMoveEvent(self, QMouseEvent):  # 拖动的函数
        if Qt.LeftButton and self.m_flag:
            self.setCursor(QCursor(Qt.OpenHandCursor))  # 更改鼠标图标
            self.move(QMouseEvent.globalPos() - self.m_Position)  # 更改窗口位置
            QMouseEvent.accept()

    def mouseReleaseEvent(self, QMouseEvent):  # 释放的函数
        self.setCursor(QCursor(Qt.ArrowCursor))
    
    def mouseDoubleClickEvent(self, event):
        """ override double click founction """
        if event.button() != Qt.LeftButton:
            return
        if self.window().isMaximized():
            self.window().showNormal()
            self.ui.pushButton_back.hide()
            self.ui.pushButton_max.show()
        else:
            self.window().showMaximized()
            self.ui.pushButton_back.show()
            self.ui.pushButton_max.hide()

    def standard_CB1(self):
        level = self.ui.comboBox_1.currentText()
        if level == '地标':
            self.ui.comboBox_2.show()
        else:
            self.ui.comboBox_2.hide()

    def search(self):
        self.tableWidget.clearSelection()
        level = self.ui.comboBox_1.currentText()
        state = self.ui.comboBox_2.currentText()
        status = self.ui.comboBox_3.currentText()
        def regexp(expr, result):
            reg = re.compile(expr)
            return reg.search(result) is not None
        conn = sqlite3.connect(DATABASE_PATH)
        cur = conn.cursor()
        pattarn = p1 = p2 = p3 = ''
        if level == '国标':
            pattarn = 'GB'
        elif level == '地标':
            pattarn = 'DB'
        elif level == '行标':
            pattarn = 'JG'
        elif level == '团标':
            pattarn = ''
        else:
            pattarn = ''
        if pattarn:
            p1 = f"StandardNumbers REGEXP '^{pattarn}'"
            if state != '不限' and pattarn == 'DB':
                p1 += ' AND ' + f"TYPE REGEXP '^{state[:2]}'"
        if status != '不限':
            p2 = f"Status REGEXP '^{status}'"
        else:
            p2 = f"Status REGEXP '^'"
        if self.ui.lineEdit_Search.text():
            p3 = f"(StandardNumbers  LIKE '%" \
                 f"{self.ui.lineEdit_Search.text()}%' OR StandardNames LIKE '%{self.ui.lineEdit_Search.text()}%')"
        if p1:
            pattarn = p1
            if p2:
                pattarn += ' AND ' + p2
                if p3:
                    pattarn += ' AND ' + p3
                    print(pattarn)
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
            print(pattarn)
        else:
            cur.execute("SELECT * FROM standards")
        data = cur.fetchall()
        conn.commit()
        conn.close()
        y = len(data)
        if y < 17:
            y = 17
        self.ui.tableWidget.setRowCount(y)
        for iy, i in enumerate(data):
            for ix, v in enumerate(i):
                item = QTableWidgetItem(v)
                self.ui.tableWidget.setItem(iy, ix, item)
        self.ui.tableWidget.resizeColumnsToContents()
        self.ui.tableWidget.resizeRowsToContents()
        for row in range(self.ui.tableWidget.rowCount()):
            self.ui.tableWidget.setRowHeight(row, 25)
        if y == 1:
            print(f"Selected second column data: {data[0][1]}")
            with open(r'.\WEB\templates\temp.txt','w', encoding='utf-8') as file:
                # 写入新内容
                file.write(f'{data[0][1]}')

    def News_Search(self):
        self.tableWidget_News.clearSelection()
        for row in range(self.ui.tableWidget_News.rowCount()):
            for col in range(self.ui.tableWidget_News.columnCount()):
                self.ui.tableWidget_News.setItem(row, col, None)
        self.tableWidget_News.clearSelection()
        level = self.ui.comboBox_6.currentText()
        start_time = self.ui.dateEdit_3.date().toString(Qt.ISODate)
        end_time = self.ui.dateEdit_4.date().toString(Qt.ISODate)
        keyword = self.ui.lineEdit_Search_3.text()
        News_result = News_Search.get_News(online_db_config,level,keyword,start_time,end_time)
        y = len(News_result)
        if y < 17:
            y = 17
        self.ui.tableWidget_News.setRowCount(y)
        try:
            for row in range(len(News_result)):
                self.ui.tableWidget_News.setItem(row, 0, QTableWidgetItem(News_result[row][1]))
                self.ui.tableWidget_News.setItem(row, 1, QTableWidgetItem(News_result[row][2]))
                self.ui.tableWidget_News.setItem(row, 2, QTableWidgetItem(News_result[row][0]))
                self.ui.tableWidget_News.setItem(row, 3, QTableWidgetItem(News_result[row][3]))
                self.ui.tableWidget_News.setItem(row, 4, QTableWidgetItem(News_result[row][4]))
        except Exception as e:
            print(f"An exception occurred: {e}")

    def open_News(self):
        selected_items = self.tableWidget_News.selectedItems()
        if selected_items:
            row = selected_items[0].row()
            url = self.tableWidget_News.item(row, 3).text()
            webbrowser.open(url)
    def select_file1(self):
        # 调用QFileDialog.getOpenFileName方法，弹出文件选择窗口
        # 参数依次为：父窗口、标题、默认目录、文件类型过滤器、选项
        self.fileName, _ = QFileDialog.getOpenFileName(
            self, '选择文件', os.getcwd(), '所有文件(*);;表格文件(*.xlxs, *.xls)')
        # 如果用户选择了文件，打印文件名
        if self.fileName:
            self.ui.lineEdit_CLOpen1.setText(self.fileName)

    def select_file2(self):
        # 调用QFileDialog.getOpenFileName方法，弹出文件选择窗口
        # 参数依次为：父窗口、标题、默认目录、文件类型过滤器、选项

        self.directory = QtWidgets.QFileDialog.getExistingDirectory(
            self, "选取文件夹", os.getcwd())
        if self.directory:  # 如果用户选择了文件，打印文件名
            self.ui.lineEdit_CLOpen2.setText(self.directory)

    def update(self):
        # QMessageBox.warning(self, "提示", "功能研发中...")
        # self.fileName = r"test\input.xlsx"
        # self.directory = r"test"
        self.t = Multi_Update(self.fileName, self.directory)
        self.t.max_signal.connect(lambda max: self.ui.progressBar.setMaximum(max))
        self.t.cur_signal.connect(self.cur_status)
        self.t.start()
    def cur_status(self, cur_value):
        self.ui.progressBar.setValue(cur_value)
        if cur_value + 1 == self.ui.progressBar.maximum():
            MyMessageBox(QIcon(ICON_PATH), '提示', '更新完成！', 2000)
            self.ui.progressBar.reset()

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
                    MyMessageBox(QIcon(ICON_PATH), '提示', '新密码不能与原密码相同！', 1000)
                else:
                    cur.execute(
                        f'update users set passwords="{password1}" where uids={UID}')
                    MyMessageBox(QIcon(ICON_PATH), '提示', '修改成功！', 1000)
                conn.commit()
                conn.close()
            else:
                MyMessageBox(QIcon(ICON_PATH), '提示', '输入不一致！', 1000)
        else:
            MyMessageBox(QIcon(ICON_PATH), '提示', '请填写完整！', 1000)

    def export(self):  # 从服务器端更新本地数据库
        self.update_DB = DB_update()
        self.update_DB.status_signal.connect(lambda:self.ui.label_LocalDB_V.setText(str(datetime.datetime.fromtimestamp(os.path.getmtime(DATABASE_PATH))).split(".")[0]))
        self.update_DB.start()

    def online_db_version(self):
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
            time_list.append(datetime.datetime.strptime(
                result_list[i][8], "%Y-%m-%d %H:%M:%S.%f"))
        result = max(time_list)
        return str(result).split('.')[0]

    def show_confirmation_dialog(self):
        # 创建一个确认对话框
        confirmation = QMessageBox()
        confirmation.setWindowIcon(QIcon(ICON_PATH))
        confirmation.setWindowTitle("数据库更新确认")
        confirmation.setText("数据库将在后台更新~")
        confirmation.setIcon(QMessageBox.Question)
        confirmation.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        # 显示对话框并获取用户的选择
        user_choice = confirmation.exec_()
        # 根据用户选择执行相应的操作
        if user_choice == QMessageBox.Ok:
            self.export()
        else:
            print("操作已取消")

    def PDF_DOWNLOAD(self):
        selected_row = self.tableWidget.currentRow()
        if selected_row != -1:  # 检查是否有行被选中（-1 表示没有行被选中）
            row_data = []
            column_count = self.tableWidget.columnCount()  # 获取列数
            for column in range(column_count):
                # 获取选中行的每个单元格的 QTableWidgetItem 对象
                item = self.tableWidget.item(selected_row, column)
                if item is not None:
                    row_data.append(item.text())  # 获取单元格中的文本数据
            # 现在，row_data 列表包含了选中行的数据
            print(row_data)
            link = row_data[5]
            if "无" in link:
                print('无链接')
            elif len(link) < 10:
                print('无链接')
            else:
                name = str(row_data[0]) + " " + str(row_data[1])
                name = name.replace("/", "-")
                options = QFileDialog.Options()
                options |= QFileDialog.ReadOnly  # 使对话框只读
                # 获取用户选择的路径
                desktop_dir = os.path.expanduser("~/Desktop")
                selected_path = QFileDialog.getExistingDirectory(
                    self, '选择路径', options=options, directory=desktop_dir)
                if selected_path:
                    print(f'选择的路径为: {selected_path}')
                    file_address = selected_path + "/" + name + ".pdf"
                    print(file_address)
                    print(link)
                    try:
                        urllib.request.urlretrieve(link, file_address)
                    except:
                        print('下载失败')
                        confirmation = QMessageBox()
                        confirmation.setWindowTitle("下载失败")
                        confirmation.setText("下载失败，请检查网络连接")
                        confirmation.setIcon(QMessageBox.Question)
                        confirmation.setStandardButtons(QMessageBox.Ok)
                        # 显示对话框并获取用户的选择
                        user_choice = confirmation.exec_()
                else:
                    print('未选择路径')
        else:
            print("没有选中行")

    def get_desktop_path(self):  # 获取桌面的路径，作为默认存储路径
        home_path = os.path.expanduser("~")
        if os.name == "posix":  # macOS or Linux
            desktop_path = os.path.join(home_path, "Desktop")
        elif os.name == "nt":  # Windows
            desktop_path = os.path.join(home_path, "Desktop")
        else:
            desktop_path = None
        return desktop_path

    def toggle_new_dialog(self):
        try:
            if self.WEB_engine is None:
                selected_items = self.tableWidget.selectedItems()
                if selected_items:
                    # 如果新界面未显示，创建并显示它
                    url = f'http://127.0.0.1:5000/'
                    response = requests.get(url)
                    self.WEB_engine = WEB(self)
                    self.WEB_engine.show()

            else:
                # 如果新界面已显示，关闭它并设置状态为None
                self.WEB_engine.close()
                self.WEB_engine = None
        except Exception as e:
            print(f"An exception occurred: {e}")

    def moveEvent(self, event):
        for WEB_engine in self.findChildren(WEB):
            WEB_engine.move(self.geometry().right() + 10, self.geometry().top())

    def onItemSelected(self):
        selected_items = self.tableWidget.selectedItems()
        if selected_items:
            # 获取第二列的数据
            row = selected_items[0].row()
            second_column_data = self.tableWidget.item(row, 1).text()
            print(f"Selected second column data: {second_column_data}")
            with open(r'.\WEB\templates\temp.txt','w', encoding='utf-8') as file:
                # 写入新内容
                file.write(f'{second_column_data}')


    def K_background(self):
        process = multiprocessing.Process(target=worker_function)
        process.start()

class WEB(QDialog):
    '''知识图谱WEB引擎'''
    def __init__(self, parent):  # 将parent参数设置为默认值为None
        super().__init__(parent)
        if parent:
            self.ui = uic.loadUi(r'.\UI\WEB.ui', self)  # 直接引用UI文件作为窗口
            self.setWindowFlag(Qt.FramelessWindowHint)  # 去掉外边框
            self.setGeometry(parent.geometry().right() + 5, parent.geometry().top(), 630, 480)
            self.webEngineView.setUrl(QUrl("http://127.0.0.1:5000/"))

def worker_function():
    app.app.run(debug=None)
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
    UID, USER, PASSWORD, AUTO_LOGIN, REMEMBER_PASSWORD, PROVINCE_CODE = Setting.load_setting()
    # Setting.load_json()
    app = QApplication(sys.argv)
    win = LoginWindow()
    sys.exit(app.exec_())# 运行应用程序的主事件循环

