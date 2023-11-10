#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :download.py
# @Time      :2023/10/17 16:50:24
# @Author    :hyooeewee

import os
from PyQt5.QtCore import QThread, pyqtSignal
import pymysql
import sqlite3

DATABASE_PATH = r'.\database\users.db'
online_db_config = {
    "host": "123.60.58.210",  # 远程MySQL数据库的主机地址（IP地址或域名）
    "user": "root",  # 远程MySQL数据库的用户名
    "password": "CLFZZRe5Mn27w72y",  # 远程MySQL数据库的密码
    "database": "standard_db",  # 要连接的数据库名称
    "port": 5896,  # MySQL默认端口号
}

class DB_update(QThread):
    """ 本地数据库更新线程类 """
    status_signal = pyqtSignal(int)
    def run(self):
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
        if result_list:
            conn = sqlite3.connect(DATABASE_PATH)
            cur = conn.cursor()
            for i in result_list:
                try:
                    cur.execute(
                        f"insert into standards values('{i[0]}','{i[2]}','{i[3]}','{i[4]}','{i[5]}',"
                        f"'{i[6]}','{i[7]}','{i[1]}','{i[8]}')")
                except:
                    try:
                        cur.execute(
                            f"update standards set StandardNames='{i[2]}',StartDate='{i[3]}', EndDate='{i[4]}',"
                            f"Status='{i[5]}',DownloadLinks='{i[6]}',TYPE='{i[1]}',HEADERS='{i[7]}',UPDATE_TIME='{i[8]}'"
                            f" where StandardNumbers='{i[0]}'")
                    except:
                        pass
            conn.commit()
            conn.close()
        self.status_signal.emit(len(result_list))



class File_download():
    '''文件下载的函数类'''
    def get_desktop_path():  # 获取桌面的路径，作为默认存储路径
        home_path = os.path.expanduser("~")
        if os.name == "posix":  # macOS or Linux
            desktop_path = os.path.join(home_path, "Desktop")
        elif os.name == "nt":  # Windows
            desktop_path = os.path.join(home_path, "Desktop")
        else:
            desktop_path = None
        return desktop_path

class News_update():
    '''新闻的函数类'''
    pass

if __name__ == "__main__":
    pass