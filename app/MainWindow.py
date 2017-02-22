# -*- coding: utf-8 -*-
"""
在PyQt中，所以class都是从QObject派生而来，QWidget对象就可以有一个parent。
这种parent-child关系主要用于两个方面：

没有parent的QWidget类被认为是最上层的窗体（通常是MainWindow），
由于MainWindow的一些操作生成的新窗体对象，parent都应该指向MainWindow。
由于parent-child关系的存在，它保证了child窗体在主窗体被回收之时也被回收。
parent作为构造函数的最后一个参数被传入，但通常情况下不必显示去指定parent对象。
因为当调用局管理器时，部局管理器会自动处理这种parent-child关系。
但是在一些特殊的情况下，我们必须显示的指定parent-child关系。
如当生成的子类不是QWidget对象但继承了QObject对象，用作dock widgets的QWidget对象。
我们可以看到，对象之间有了依赖和生命周期，把IOC容器运用到GUI编程中是自然而然的事情了
"""
import os
from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import Qt
from view.layout import Ui_Form

class MainWindow(QtGui.QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.dir=os.path.dirname(os.path.realpath(__file__))
        self.icon = QtGui.QIcon(self.dir+"\\view\\icon.png")
        self.setWindowIcon(self.icon)
        self.connect(self.ui.pushButton_exit, QtCore.SIGNAL("clicked()"), QtGui.qApp, QtCore.SLOT("quit()"))
        self.connect(self.ui.pushButton_min, QtCore.SIGNAL("clicked()"), self, QtCore.SLOT("showMinimized()"))
        self.ui.lineEdit.setReadOnly(True)
        self.loadStyleSheet("layout")

    def loadStyleSheet(self, sheetName):
        file = QtCore.QFile(self.dir+'\\view\\%s.qss' % sheetName.lower())
        file.open(QtCore.QFile.ReadOnly)
        styleSheet = file.readAll()
        try:
            # Python v2.
            styleSheet = unicode(styleSheet, encoding='utf8')
        except NameError:
            # Python v3.
            styleSheet = str(styleSheet, encoding='utf8')
        #QtGui.qApp.setStyleSheet(styleSheet)
        self.setStyleSheet(styleSheet)

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
    import sys
    app = QtGui.QApplication(sys.argv)
    myapp = MainWindow()
    myapp.show()
    sys.exit(app.exec_())
