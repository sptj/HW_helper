# -*- coding: utf-8 -*-
import sys
from PyQt4 import QtGui, QtCore, uic
from PyQt4.QtCore import Qt
qtCreatorFile = "layout.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)


def set_qss_decorator(qss_file_name):
    file_qss = QtCore.QFile(qss_file_name)
    file_qss.open(QtCore.QFile.ReadOnly)
    style_sheet = file_qss.readAll()
    style_sheet = unicode(style_sheet, encoding='utf8')
    QtGui.qApp.setStyleSheet(style_sheet)


class MainWidget(QtGui.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.icon = QtGui.QIcon("icon.png")
        self.setWindowIcon(self.icon)
        self.isTopLevel()


        ##################################################
        # self.trayIcon = QtGui.QSystemTrayIcon(self)  # 创建系统托盘对象
        # self.icon = QtGui.QIcon(self.icon)  # 创建图标
        # self.trayIcon.setIcon(self.icon)  # 设置系统托盘图标
        # self.trayIcon.show()
        # self.trayIcon.activated.connect(self.trayClick)  # 点击托盘
        # self.trayIcon.setToolTip(u"托盘小程序")  # 托盘信息

        #self.Menu()  # 右键菜单

        # # 1.是指信息图标：
        # # 2.是指警告图标：
        # # 3.是指错误图标：
        # # 没有其他可选值了
        # self.tray.activated.connect(a)
        # self.tray.messageClicked.connect(message)
        # ##################################################
        # 注册事件
        self.connect(self.pushButton, QtCore.SIGNAL("clicked()"), QtGui.qApp, QtCore.SLOT("quit()"))
        #self.connect(self.pushButton, QtCore.SIGNAL("clicked()"), self, QtCore.SLOT("close()"))
        self.connect(self.pushButton_4, QtCore.SIGNAL("clicked()"), self, QtCore.SLOT("showMinimized()"))
        # 支持窗口拖动,重写两个方法
        self.pushButton_5.clicked.connect(self.loadFile)


    def loadFile(self):  ########载入file
        file_name = QtGui.QFileDialog.getOpenFileName(self, "open file dialog", "C:\Users\Administrator\Desktop",
                                                "Txt files(*.txt)")
        ##"open file Dialog "文件对话框的标题，第二个是打开的默认路径，第三个是文件类型
    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.m_drag = True
            self.m_DragPosition = event.globalPos() - self.pos()
            event.accept()
    def mouseMoveEvent(self, QMouseEvent):
        if self.m_drag and Qt.LeftButton:
            self.move(QMouseEvent.globalPos() - self.m_DragPosition)
            QMouseEvent.accept()
    def mouseReleaseEvent(self, QMouseEvent):
        self.m_drag = False


    def Menu(self):
        self.minimizeAction = QtGui.QAction(u"最小化", self, triggered=self.hide)
        self.maximizeAction = QtGui.QAction(u"最大化", self, triggered=self.showMaximized)
        self.restoreAction  = QtGui.QAction(u"还原", self, triggered=self.showNormal)
        self.quitAction     = QtGui.QAction(u"退出", self, triggered=QtGui.qApp.quit)
        #self.quitAction     = QtGui.QAction(u"退出", self, triggered=self.close)
        self.trayIconMenu = QtGui.QMenu(self)
        self.trayIconMenu.addAction(self.minimizeAction)
        self.trayIconMenu.addAction(self.maximizeAction)
        self.trayIconMenu.addAction(self.restoreAction)
        self.trayIconMenu.addSeparator()  # 间隔线
        self.trayIconMenu.addAction(self.quitAction)
        self.trayIcon.setContextMenu(self.trayIconMenu)  # 右击托盘


    def closeEvent(self, event):
        if self.trayIcon.isVisible():
            self.hide()
            event.ignore()
    def trayClick(self, reason):
        if reason == QtGui.QSystemTrayIcon.DoubleClick:  # 双击
            self.showNormal()
        elif reason == QtGui.QSystemTrayIcon.MiddleClick:  # 中击
            self.showMessage()
        else:
            pass
    def showMessage(self):
        icon = QtGui.QSystemTrayIcon.Information
        self.trayIcon.showMessage(u"提示信息", u"点我干嘛？", icon)

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    window = MainWidget()
    set_qss_decorator('layout1.qss')
    window.show()
    sys.exit(app.exec_())









