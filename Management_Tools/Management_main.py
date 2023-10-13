import sys
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import (QApplication, QFileDialog, QMainWindow, QMessageBox, QTableWidgetItem)
import GB_Standards_Spider

class MyMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # 使用loadUi加载UI文件
        self.ui = uic.loadUi(r'.\management.ui', self)

        # 在这里可以添加自定义功能

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyMainWindow()
    window.show()
    sys.exit(app.exec_())

