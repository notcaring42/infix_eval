#!/usr/bin/python3
import sys
from PyQt5 import QtWidgets
from infix_eval.ui import main_ui

def main():
    app = QtWidgets.QApplication(sys.argv)
    main_window = QtWidgets.QMainWindow() 
    main_window_ui = main_ui.Ui_MainWindow()
    main_window_ui.setupUi(main_window)
    main_window.show()

    sys.exit(app.exec_())
