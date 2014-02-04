#!/usr/bin/python3
import sys
from PyQt5 import QtWidgets
from ui.main import Ui_MainWindow

def main():
    app = QtWidgets.QApplication(sys.argv)
    main_window = QtWidgets.QMainWindow() 
    main_window_ui = Ui_MainWindow()
    main_window_ui.setupUi(main_window)
    main_window.show()

    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
