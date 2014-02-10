#!/usr/bin/python3
import sys
from PyQt5 import QtWidgets
from infix_eval.ui.infix_eval_ui import InfixEvalUi

def main():
    app = QtWidgets.QApplication(sys.argv)
    window = InfixEvalUi()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
