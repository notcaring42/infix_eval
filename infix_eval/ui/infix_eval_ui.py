from infix_eval.ui import main_ui
from PyQt5 import QtWidgets, QtGui, QtCore
from infix_eval.evaluator import Evaluator

class InfixEvalUi(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self, parent)
        self.main_window_ui = main_ui.Ui_MainWindow()
        self.main_window_ui.setupUi(self)
        self.main_window_ui.evaluateButton.clicked.connect(self.eval_and_print)
        self.scene = QtWidgets.QGraphicsScene()
        self.main_window_ui.treeView.setScene(self.scene)
        self.scene.setSceneRect(0, 0, 348, 348)
        self.evaluator = Evaluator()

    def eval_and_print(self):
        expression = self.main_window_ui.expressionLineEdit.text()

        try:
           result = self.evaluator.evaluate(expression) 
        except ValueError as e:
            print(e)

        print(result.result)
        self.scene.clear()
        self.show_results(result)
    
    def show_results(self, result):
       font = QtGui.QFont("Droid Sans")
       font.setPointSize(20)

       result_text = QtWidgets.QGraphicsTextItem("%.3f" % result.result)
       result_text.setFont(font)
       result_text.setPos(0, 0)
       self.scene.addItem(result_text)
       
       self.print_tree(result.tree, 100, 100, font, 100)

    def print_tree(self, tree, x, y, font, offset):
        if tree is None:
            return
        result_text = QtWidgets.QGraphicsTextItem(str(tree.data))
        font.setPointSize(10)
        result_text.setFont(font)
        result_text.setPos(x+5, y+5)
        self.scene.addItem(TreeNode(x, y, 35))
        self.scene.addItem(result_text)
        self.print_tree(tree.left, x - offset, y + 60, font, offset * 0.70)
        self.print_tree(tree.right, x + offset, y + 60, font, offset * 0.70)
        

       
class TreeNode(QtWidgets.QGraphicsEllipseItem):
    def __init__(self, x, y, size):
        super(QtWidgets.QGraphicsEllipseItem, self).__init__(QtCore.QRectF(x, y, size, size))
