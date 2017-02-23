# -*- coding: utf-8 -*-
"""
在PyQt中，所以class都是从QObject派生而来，QWidget对象就可以有一个parent。
这种parent-child关系主要用于两个方面：

没有parent的QWidget类被认为是最上层的窗体（通常是Mainself），
由于Mainself的一些操作生成的新窗体对象，parent都应该指向Mainself。
由于parent-child关系的存在，它保证了child窗体在主窗体被回收之时也被回收。
parent作为构造函数的最后一个参数被传入，但通常情况下不必显示去指定parent对象。
因为当调用局管理器时，部局管理器会自动处理这种parent-child关系。
但是在一些特殊的情况下，我们必须显示的指定parent-child关系。
如当生成的子类不是QWidget对象但继承了QObject对象，用作dock widgets的QWidget对象。
我们可以看到，对象之间有了依赖和生命周期，把IOC容器运用到GUI编程中是自然而然的事情了
"""
import os
from PySide import QtCore, QtGui
from PySide.QtCore import Qt
from view.layout import Ui_Form
from model.IEEE754 import float_to_binary,binary_to_float
from model.magic_convert import convert2fixed_directly
class MainWindow(QtGui.QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.dir=os.path.dirname(os.path.realpath(__file__))
        self.icon = QtGui.QIcon(self.dir+"\\view\\icon.png")
        self.setWindowIcon(self.icon)
        self.ui.lineEdit_mem_like.setAlignment(Qt.AlignCenter)
        self.ui.lineEdit_return_float.setAlignment(Qt.AlignCenter)
        self.ui.lineEdit_float_input.setAlignment(Qt.AlignCenter)
        self.ui.lineEdit_fd_input.setAlignment(Qt.AlignCenter)
        self.ui.lineEdit_fn_input.setAlignment(Qt.AlignCenter)
        self.ui.lineEdit_fn_input.setText('16')
        self.ui.lineEdit_dn_input.setAlignment(Qt.AlignCenter)
        self.ui.lineEdit_dn_input.setText('16')
        self.ui.lineEdit_fd_mem_like.setAlignment(Qt.AlignCenter)

        self.ui.lineEdit_return_fd.setAlignment(Qt.AlignCenter)

        self.ui.lineEdit_fd_mem_like.setReadOnly(True)
        self.ui.lineEdit_mem_like.setReadOnly(True)
        self.ui.lineEdit_return_float.setReadOnly(True)
        self.loadStyleSheet("layout")
        self.connect(self.ui.pushButton_exit, QtCore.SIGNAL("clicked()"), QtGui.qApp, QtCore.SLOT("quit()"))
        self.connect(self.ui.pushButton_min, QtCore.SIGNAL("clicked()"), self, QtCore.SLOT("showMinimized()"))
        self.ui.lineEdit_float_input.textChanged.connect(self.btn_transfor_clink)
        self.ui.lineEdit_fd_input.textChanged.connect(self.btn_fd_transfor_clink)
    def btn_fd_transfor_clink(self):
        fd_num_string = self.ui.lineEdit_fd_input.text()
        fd_dn_num_string =self.ui.lineEdit_dn_input.text()
        fd_fn_num_string =self.ui.lineEdit_fn_input.text()
        try:
            string_binary=convert2fixed_directly(int(fd_dn_num_string),int(fd_fn_num_string),fd_num_string,'d2b')
            self.ui.lineEdit_fd_mem_like.setText(string_binary)
        except:
            self.ui.lineEdit_fd_mem_like.setText("Invalid Number")

    def btn_transfor_clink(self):
        float_num_string = self.ui.lineEdit_float_input.text()
        try:
            if float_num_string != '':
                if(len(float_num_string)>=7):
                    self.ui.label_warn.setText(u'单精度浮点数只有七位有效数字')
                float_num = float(float_num_string)
                biary_num_string = float_to_binary(float_num)  #
                self.ui.lineEdit_mem_like.setText(biary_num_string)
                transfored_float_num_string=binary_to_float(biary_num_string)
                self.ui.lineEdit_return_float.setText(transfored_float_num_string)
            else:
                self.ui.lineEdit_mem_like.setText('')
                self.ui.lineEdit_return_float.setText('')
        except:
            self.ui.lineEdit_mem_like.setText("Invalid Number")
            self.ui.lineEdit_return_float.setText("Invalid Number")
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
        # QtGui.qApp.setStyleSheet(styleSheet)
        self.setStyleSheet(styleSheet)

    def getFloatNumString(self):
        return self.ui.lineEdit_2.text()

    def setBinaryString(self,String2Disp):
        self.ui.lineEdit.setText(String2Disp)

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
    self = Mainself()
    self.show()
    sys.exit(app.exec_())
