# -*- coding: utf-8 -*-
import sys
from PySide import QtGui, QtCore
from app.view.ui2py import ui_document_transfor
from app.MainWindow import MainWindow
if __name__ == "__main__":
    ui_document_transfor()
    app = QtGui.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())








