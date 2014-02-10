from infix_eval.ui import main_ui
from PyQt5 import QtWidgets

class InfixEvalUi(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self, parent)
        self.main_window_ui = main_ui.Ui_MainWindow()
        self.main_window_ui.setupUi(self)
        self.main_window_ui.evaluateButton.clicked.connect(eval_and_print)

def eval_and_print():
    print("Button clicked!")
