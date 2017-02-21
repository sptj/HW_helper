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
        self.connect(self.pushButton_exit, QtCore.SIGNAL("clicked()"), QtGui.qApp, QtCore.SLOT("quit()"))
        self.connect(self.pushButton_min, QtCore.SIGNAL("clicked()"), self, QtCore.SLOT("showMinimized()"))
        self.lineEdit.setReadOnly(True)
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

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    window = MainWidget()
    set_qss_decorator('layout.qss')
    window.show()
    sys.exit(app.exec_())









