#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :download.py
# @Time      :2023/10/17 16:50:24
# @Author    :hyooeewee

import os

class DB_update():
    '''本地数据库更新的类'''
    pass

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