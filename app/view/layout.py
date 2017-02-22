# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'layout.ui'
#
# Created: Wed Feb 22 13:44:14 2017
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(910, 641)
        font = QtGui.QFont()
        font.setPointSize(9)
        Form.setFont(font)
        self.tabWidget = QtGui.QTabWidget(Form)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 911, 641))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtGui.QWidget()
        self.tab.setObjectName("tab")
        self.groupBox = QtGui.QGroupBox(self.tab)
        self.groupBox.setGeometry(QtCore.QRect(20, 10, 881, 591))
        self.groupBox.setObjectName("groupBox")
        self.lineEdit = QtGui.QLineEdit(self.groupBox)
        self.lineEdit.setGeometry(QtCore.QRect(250, 60, 361, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtGui.QLineEdit(self.groupBox)
        self.lineEdit_2.setGeometry(QtCore.QRect(40, 60, 201, 31))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(40, 40, 72, 15))
        self.label.setObjectName("label")
        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(250, 40, 361, 16))
        self.label_2.setObjectName("label_2")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.pushButton_5 = QtGui.QPushButton(self.tab_2)
        self.pushButton_5.setGeometry(QtCore.QRect(10, 580, 93, 28))
        self.pushButton_5.setObjectName("pushButton_5")
        self.tabWidget.addTab(self.tab_2, "")
        self.pushButton_exit = QtGui.QPushButton(Form)
        self.pushButton_exit.setGeometry(QtCore.QRect(872, 0, 31, 28))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.pushButton_exit.setFont(font)
        self.pushButton_exit.setObjectName("pushButton_exit")
        self.pushButton_min = QtGui.QPushButton(Form)
        self.pushButton_min.setGeometry(QtCore.QRect(840, 0, 31, 28))
        self.pushButton_min.setObjectName("pushButton_min")

        self.retranslateUi(Form)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "test", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("Form", "IEEE754 浮点数存储方式", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEdit.setText(QtGui.QApplication.translate("Form", "0123456789ABCDEF0123456789ABCDEF", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEdit_2.setText(QtGui.QApplication.translate("Form", "123", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Form", "浮点数↓", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Form", "符合IEEE754标准时，浮点数在内存中的存储格式↓", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QtGui.QApplication.translate("Form", "Tab 1", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_5.setText(QtGui.QApplication.translate("Form", "打开文件", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QtGui.QApplication.translate("Form", "Tab 2", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_exit.setText(QtGui.QApplication.translate("Form", "×", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_min.setText(QtGui.QApplication.translate("Form", "_", None, QtGui.QApplication.UnicodeUTF8))

