# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\Hughi\OneDrive - hrbeu.edu.cn\05.Projects\02.Python\Toolbox of Standard\UI\Login.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_LoginWindow(object):
    def setupUi(self, LoginWindow):
        LoginWindow.setObjectName("LoginWindow")
        LoginWindow.resize(800, 500)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(LoginWindow.sizePolicy().hasHeightForWidth())
        LoginWindow.setSizePolicy(sizePolicy)
        LoginWindow.setMinimumSize(QtCore.QSize(800, 500))
        LoginWindow.setMaximumSize(QtCore.QSize(800, 500))
        font = QtGui.QFont()
        font.setFamily("Noto Sans CJK")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        LoginWindow.setFont(font)
        LoginWindow.setStyleSheet("border: 0px;\n"
"padding: 0px;\n"
"margin: 0px;\n"
"font-size: 10pt;\n"
"color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(LoginWindow)
        self.centralwidget.setStyleSheet("#centralwidget{\n"
"    background-color: rgb(255, 255, 255);\n"
"    border-radius:20px;\n"
"}\n"
"\n"
"QFrame,QLabel,QPushButton{\n"
"    background-color: rgba(255, 0, 0, 0);\n"
"}\n"
"#label_title{\n"
"    font-size: 40pt;\n"
"}\n"
"#frame_3{\n"
"    margin: 30px;\n"
"}")
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.frame_3 = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(5)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy)
        self.frame_3.setStyleSheet("")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_icon = QtWidgets.QLabel(self.frame_3)
        self.label_icon.setStyleSheet("")
        self.label_icon.setText("")
        self.label_icon.setPixmap(QtGui.QPixmap(":/icons/icons/3914110.png"))
        self.label_icon.setObjectName("label_icon")
        self.verticalLayout.addWidget(self.label_icon, 0, QtCore.Qt.AlignHCenter)
        self.label_title = QtWidgets.QLabel(self.frame_3)
        font = QtGui.QFont()
        font.setFamily("Noto Sans CJK Medium")
        font.setPointSize(40)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_title.setFont(font)
        self.label_title.setStyleSheet("")
        self.label_title.setObjectName("label_title")
        self.verticalLayout.addWidget(self.label_title, 0, QtCore.Qt.AlignHCenter)
        self.label_version = QtWidgets.QLabel(self.frame_3)
        self.label_version.setObjectName("label_version")
        self.verticalLayout.addWidget(self.label_version, 0, QtCore.Qt.AlignHCenter)
        self.horizontalLayout_3.addWidget(self.frame_3, 0, QtCore.Qt.AlignHCenter)
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(5)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setStyleSheet("")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.frame = QtWidgets.QFrame(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setObjectName("frame")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_2.setContentsMargins(0, 20, 20, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.pushButton = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
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
        self.verticalLayout_8.addWidget(self.frame, 0, QtCore.Qt.AlignTop)
        self.stackedWidget_2 = QtWidgets.QStackedWidget(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(4)
        sizePolicy.setHeightForWidth(self.stackedWidget_2.sizePolicy().hasHeightForWidth())
        self.stackedWidget_2.setSizePolicy(sizePolicy)
        self.stackedWidget_2.setMinimumSize(QtCore.QSize(250, 250))
        self.stackedWidget_2.setMaximumSize(QtCore.QSize(16777215, 16777215))
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
"# pushButton_Forgetpassword:pressed{\n"
"    padding-top:0px;\n"
"    padding-left:0px;\n"
"}\n"
"QPushButton:pressed{\n"
"    padding-top:5px;\n"
"    padding-left:5px;\n"
"}\n"
"")
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
        self.verticalLayout_8.addWidget(self.stackedWidget_2, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.frame_7 = QtWidgets.QFrame(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(2)
        sizePolicy.setHeightForWidth(self.frame_7.sizePolicy().hasHeightForWidth())
        self.frame_7.setSizePolicy(sizePolicy)
        self.frame_7.setStyleSheet("QPushButton{\n"
"    border:none;\n"
"    padding:5px;\n"
"}\n"
"QPushButton:hover{\n"
"    padding-top:7px;\n"
"    padding-left:7px;\n"
"}")
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_7)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(80)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_Login = QtWidgets.QPushButton(self.frame_7)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/icons/3917749.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_Login.setIcon(icon2)
        self.pushButton_Login.setObjectName("pushButton_Login")
        self.horizontalLayout.addWidget(self.pushButton_Login, 0, QtCore.Qt.AlignTop)
        self.pushButton_Register = QtWidgets.QPushButton(self.frame_7)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icons/icons/3917698.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_Register.setIcon(icon3)
        self.pushButton_Register.setObjectName("pushButton_Register")
        self.horizontalLayout.addWidget(self.pushButton_Register, 0, QtCore.Qt.AlignTop)
        self.verticalLayout_8.addWidget(self.frame_7, 0, QtCore.Qt.AlignHCenter)
        self.horizontalLayout_3.addWidget(self.frame_2)
        LoginWindow.setCentralWidget(self.centralwidget)
        self.actionhuanying = QtWidgets.QAction(LoginWindow)
        self.actionhuanying.setObjectName("actionhuanying")
        self.actionguanyu = QtWidgets.QAction(LoginWindow)
        self.actionguanyu.setObjectName("actionguanyu")

        self.retranslateUi(LoginWindow)
        self.stackedWidget_2.setCurrentIndex(0)
        self.pushButton.clicked.connect(LoginWindow.close) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(LoginWindow)

    def retranslateUi(self, LoginWindow):
        _translate = QtCore.QCoreApplication.translate
        LoginWindow.setWindowTitle(_translate("LoginWindow", "MainWindow"))
        self.label_title.setText(_translate("LoginWindow", "规范通"))
        self.label_version.setText(_translate("LoginWindow", "版本 V0.1 Alpha"))
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
