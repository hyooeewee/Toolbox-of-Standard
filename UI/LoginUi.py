# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Login.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_LoginWindow(object):
    def setupUi(self, LoginWindow):
        LoginWindow.setObjectName("LoginWindow")
        LoginWindow.resize(850, 540)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(LoginWindow.sizePolicy().hasHeightForWidth())
        LoginWindow.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(14)
        LoginWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(LoginWindow)
        self.centralwidget.setMinimumSize(QtCore.QSize(720, 500))
        self.centralwidget.setMaximumSize(QtCore.QSize(720, 500))
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_5.setContentsMargins(10, 10, 10, 10)
        self.horizontalLayout_5.setSpacing(10)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setMinimumSize(QtCore.QSize(360, 480))
        self.frame.setMaximumSize(QtCore.QSize(380, 500))
        self.frame.setStyleSheet("#frame{\n"
"background-color: qlineargradient(spread:pad, x1:0.517045, y1:1, x2:0.5, y2:0, stop:0 rgba(255, 0, 0, 255), stop:0.522727 rgba(255, 0, 127, 255), stop:1 rgba(0, 170, 255, 255));\n"
"border-radius:20px;\n"
"}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_7.setContentsMargins(12, 0, 0, 0)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        spacerItem = QtWidgets.QSpacerItem(20, 160, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_7.addItem(spacerItem)
        self.label = QtWidgets.QLabel(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 25pt \"Aa而墨行书\";")
        self.label.setObjectName("label")
        self.verticalLayout_7.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Aa而墨行书")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 18pt \"Aa而墨行书\";")
        self.label_2.setObjectName("label_2")
        self.verticalLayout_7.addWidget(self.label_2)
        spacerItem1 = QtWidgets.QSpacerItem(20, 160, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_7.addItem(spacerItem1)
        self.horizontalLayout_5.addWidget(self.frame)
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setMinimumSize(QtCore.QSize(350, 460))
        self.frame_2.setMaximumSize(QtCore.QSize(350, 460))
        self.frame_2.setStyleSheet("#frame_2{\n"
"    background-color: rgb(255, 255, 255);\n"
"    border-top-right-radius:20px;\n"
"    border-bottom-right-radius:20px;\n"
"    padding-left:20px;\n"
"}")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.frame1 = QtWidgets.QFrame(self.frame_2)
        self.frame1.setObjectName("frame1")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame1)
        self.horizontalLayout_2.setContentsMargins(-1, 10, 10, -1)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.pushButton = QtWidgets.QPushButton(self.frame1)
        self.pushButton.setStyleSheet("QPushButton{\n"
"    border:none;\n"
"    padding: 5px;\n"
"}\n"
"QPushButton:hover{\n"
"    padding-bottom: 0px;\n"
"    padding-right: 0px;\n"
"}")
        self.pushButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/icons/3917759.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QtCore.QSize(20, 20))
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_2.addWidget(self.pushButton)
        self.verticalLayout_8.addWidget(self.frame1)
        self.frame_3 = QtWidgets.QFrame(self.frame_2)
        self.frame_3.setMinimumSize(QtCore.QSize(221, 231))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_4 = QtWidgets.QFrame(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(6)
        sizePolicy.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_4)
        self.verticalLayout_3.setContentsMargins(9, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.frame_6 = QtWidgets.QFrame(self.frame_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(5)
        sizePolicy.setHeightForWidth(self.frame_6.sizePolicy().hasHeightForWidth())
        self.frame_6.setSizePolicy(sizePolicy)
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_6)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.stackedWidget_2 = QtWidgets.QStackedWidget(self.frame_6)
        self.stackedWidget_2.setMinimumSize(QtCore.QSize(0, 250))
        self.stackedWidget_2.setMaximumSize(QtCore.QSize(16777215, 250))
        self.stackedWidget_2.setStyleSheet("QLineEdit{\n"
"    \n"
"    background-color: rgba(255, 255, 255, 0);\n"
"    border:none;\n"
"    border-bottom:1px solid black\n"
"}\n"
"QPushButton{\n"
"    background-color: rgb(0, 0, 0);\n"
"    color: rgb(255, 255, 255);\n"
"    border-radius:7px;\n"
"}\n"
"QPushButton:pressed{\n"
"    padding-top:5px;\n"
"    padding-left:5px;\n"
"}")
        self.stackedWidget_2.setObjectName("stackedWidget_2")
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setStyleSheet("")
        self.page_3.setObjectName("page_3")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.page_3)
        self.verticalLayout_5.setContentsMargins(15, 0, 15, 0)
        self.verticalLayout_5.setSpacing(10)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.lineEdit_LAccount = QtWidgets.QLineEdit(self.page_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_LAccount.sizePolicy().hasHeightForWidth())
        self.lineEdit_LAccount.setSizePolicy(sizePolicy)
        self.lineEdit_LAccount.setMinimumSize(QtCore.QSize(0, 40))
        self.lineEdit_LAccount.setMaximumSize(QtCore.QSize(16777215, 40))
        self.lineEdit_LAccount.setObjectName("lineEdit_LAccount")
        self.verticalLayout_5.addWidget(self.lineEdit_LAccount)
        self.lineEdit_LPassword = QtWidgets.QLineEdit(self.page_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_LPassword.sizePolicy().hasHeightForWidth())
        self.lineEdit_LPassword.setSizePolicy(sizePolicy)
        self.lineEdit_LPassword.setMinimumSize(QtCore.QSize(0, 40))
        self.lineEdit_LPassword.setMaximumSize(QtCore.QSize(16777215, 40))
        self.lineEdit_LPassword.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_LPassword.setObjectName("lineEdit_LPassword")
        self.verticalLayout_5.addWidget(self.lineEdit_LPassword)
        self.frame_8 = QtWidgets.QFrame(self.page_3)
        self.frame_8.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_8.sizePolicy().hasHeightForWidth())
        self.frame_8.setSizePolicy(sizePolicy)
        self.frame_8.setMaximumSize(QtCore.QSize(16777215, 40))
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.frame_8)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setSpacing(40)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.checkBox_AutoLogin = QtWidgets.QCheckBox(self.frame_8)
        self.checkBox_AutoLogin.setObjectName("checkBox_AutoLogin")
        self.horizontalLayout_6.addWidget(self.checkBox_AutoLogin)
        self.checkBox_RememberPassword = QtWidgets.QCheckBox(self.frame_8)
        self.checkBox_RememberPassword.setObjectName("checkBox_RememberPassword")
        self.horizontalLayout_6.addWidget(self.checkBox_RememberPassword)
        self.pushButton_Forgetpassword = QtWidgets.QPushButton(self.frame_8)
        self.pushButton_Forgetpassword.setStyleSheet("QPushButton{\n"
"    background-color: rgba(255, 255, 255, 0);\n"
"    color: rgb(0, 0, 0);\n"
"}")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/icons/3916693.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_Forgetpassword.setIcon(icon1)
        self.pushButton_Forgetpassword.setObjectName("pushButton_Forgetpassword")
        self.horizontalLayout_6.addWidget(self.pushButton_Forgetpassword)
        self.verticalLayout_5.addWidget(self.frame_8)
        self.pushButton_LSure = QtWidgets.QPushButton(self.page_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_LSure.sizePolicy().hasHeightForWidth())
        self.pushButton_LSure.setSizePolicy(sizePolicy)
        self.pushButton_LSure.setMinimumSize(QtCore.QSize(0, 40))
        self.pushButton_LSure.setMaximumSize(QtCore.QSize(16777215, 40))
        self.pushButton_LSure.setObjectName("pushButton_LSure")
        self.verticalLayout_5.addWidget(self.pushButton_LSure)
        self.stackedWidget_2.addWidget(self.page_3)
        self.page_4 = QtWidgets.QWidget()
        self.page_4.setObjectName("page_4")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.page_4)
        self.verticalLayout_6.setContentsMargins(15, 0, 15, 0)
        self.verticalLayout_6.setSpacing(10)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.lineEdit_RAccount = QtWidgets.QLineEdit(self.page_4)
        self.lineEdit_RAccount.setMinimumSize(QtCore.QSize(0, 40))
        self.lineEdit_RAccount.setObjectName("lineEdit_RAccount")
        self.verticalLayout_6.addWidget(self.lineEdit_RAccount)
        self.lineEdit_RPassword1 = QtWidgets.QLineEdit(self.page_4)
        self.lineEdit_RPassword1.setMinimumSize(QtCore.QSize(0, 40))
        self.lineEdit_RPassword1.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_RPassword1.setObjectName("lineEdit_RPassword1")
        self.verticalLayout_6.addWidget(self.lineEdit_RPassword1)
        self.lineEdit_RPassword2 = QtWidgets.QLineEdit(self.page_4)
        self.lineEdit_RPassword2.setMinimumSize(QtCore.QSize(0, 40))
        self.lineEdit_RPassword2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_RPassword2.setObjectName("lineEdit_RPassword2")
        self.verticalLayout_6.addWidget(self.lineEdit_RPassword2)
        self.pushButton_RSure = QtWidgets.QPushButton(self.page_4)
        self.pushButton_RSure.setMinimumSize(QtCore.QSize(0, 40))
        self.pushButton_RSure.setObjectName("pushButton_RSure")
        self.verticalLayout_6.addWidget(self.pushButton_RSure)
        self.stackedWidget_2.addWidget(self.page_4)
        self.verticalLayout_4.addWidget(self.stackedWidget_2)
        self.verticalLayout_3.addWidget(self.frame_6)
        self.frame_7 = QtWidgets.QFrame(self.frame_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.frame_7.sizePolicy().hasHeightForWidth())
        self.frame_7.setSizePolicy(sizePolicy)
        self.frame_7.setStyleSheet("QPushButton{\n"
"    border:none;\n"
"    padding:5px\n"
"}\n"
"QPushButton:hover{\n"
"    padding-top:7px;\n"
"    padding-left:7px;\n"
"}")
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_7)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_Login = QtWidgets.QPushButton(self.frame_7)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/icons/3917749.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_Login.setIcon(icon2)
        self.pushButton_Login.setObjectName("pushButton_Login")
        self.horizontalLayout.addWidget(self.pushButton_Login)
        self.pushButton_Register = QtWidgets.QPushButton(self.frame_7)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icons/icons/3917698.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_Register.setIcon(icon3)
        self.pushButton_Register.setObjectName("pushButton_Register")
        self.horizontalLayout.addWidget(self.pushButton_Register)
        self.verticalLayout_3.addWidget(self.frame_7)
        self.verticalLayout.addWidget(self.frame_4)
        self.frame_5 = QtWidgets.QFrame(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.frame_5.sizePolicy().hasHeightForWidth())
        self.frame_5.setSizePolicy(sizePolicy)
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_5)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.stackedWidget = QtWidgets.QStackedWidget(self.frame_5)
        self.stackedWidget.setStyleSheet("font: 12pt \"幼圆\";")
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.page)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_Tips = QtWidgets.QLabel(self.page)
        self.label_Tips.setStyleSheet("")
        self.label_Tips.setText("")
        self.label_Tips.setObjectName("label_Tips")
        self.horizontalLayout_7.addWidget(self.label_Tips, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.page_2)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_Wrong = QtWidgets.QLabel(self.page_2)
        self.label_Wrong.setStyleSheet("color: rgb(255, 0, 0);")
        self.label_Wrong.setText("")
        self.label_Wrong.setObjectName("label_Wrong")
        self.horizontalLayout_3.addWidget(self.label_Wrong, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.stackedWidget.addWidget(self.page_2)
        self.horizontalLayout_4.addWidget(self.stackedWidget)
        self.verticalLayout.addWidget(self.frame_5)
        self.verticalLayout_8.addWidget(self.frame_3)
        self.horizontalLayout_5.addWidget(self.frame_2)
        self.frame_2.raise_()
        self.frame.raise_()
        LoginWindow.setCentralWidget(self.centralwidget)
        self.actionhuanying = QtWidgets.QAction(LoginWindow)
        self.actionhuanying.setObjectName("actionhuanying")
        self.actionguanyu = QtWidgets.QAction(LoginWindow)
        self.actionguanyu.setObjectName("actionguanyu")

        self.retranslateUi(LoginWindow)
        self.stackedWidget_2.setCurrentIndex(0)
        self.stackedWidget.setCurrentIndex(1)
        self.pushButton.clicked.connect(LoginWindow.close) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(LoginWindow)

    def retranslateUi(self, LoginWindow):
        _translate = QtCore.QCoreApplication.translate
        LoginWindow.setWindowTitle(_translate("LoginWindow", "MainWindow"))
        self.label.setText(_translate("LoginWindow", "Welcome"))
        self.label_2.setText(_translate("LoginWindow", "欢迎使用标准工具箱\n"
"你的支持是我不断前进的动力"))
        self.lineEdit_LAccount.setPlaceholderText(_translate("LoginWindow", "账号："))
        self.lineEdit_LPassword.setPlaceholderText(_translate("LoginWindow", "密码："))
        self.checkBox_AutoLogin.setText(_translate("LoginWindow", "自动登录"))
        self.checkBox_RememberPassword.setText(_translate("LoginWindow", "记住密码"))
        self.pushButton_Forgetpassword.setText(_translate("LoginWindow", "找回密码"))
        self.pushButton_LSure.setText(_translate("LoginWindow", "登录"))
        self.lineEdit_RAccount.setPlaceholderText(_translate("LoginWindow", "账号："))
        self.lineEdit_RPassword1.setPlaceholderText(_translate("LoginWindow", "密码："))
        self.lineEdit_RPassword2.setPlaceholderText(_translate("LoginWindow", "确认密码："))
        self.pushButton_RSure.setText(_translate("LoginWindow", "注册"))
        self.pushButton_Login.setText(_translate("LoginWindow", " 登录"))
        self.pushButton_Register.setText(_translate("LoginWindow", " 注册"))
        self.actionhuanying.setText(_translate("LoginWindow", "huanying "))
        self.actionguanyu.setText(_translate("LoginWindow", "guanyu"))
import res_rc