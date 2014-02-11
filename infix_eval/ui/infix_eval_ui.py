from infix_eval.ui import main_ui
from PyQt5 import QtWidgets, QtGui, QtCore
from infix_eval.evaluator import Evaluator
import math
from collections import namedtuple

class InfixEvalUi(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self, parent)
        self.main_window_ui = main_ui.Ui_MainWindow()
        self.main_window_ui.setupUi(self)
        self.main_window_ui.evaluateButton.clicked.connect(self.eval_and_print)
        self.scene = QtWidgets.QGraphicsScene()
        self.view = self.main_window_ui.treeView
        self.main_window_ui.treeView.setScene(self.scene)
        self.scene.setSceneRect(0, 0, self.view.width(), self.view.height())
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
       font = QtGui.QFont("Droid Sans Mono")
       font.setPointSize(20)

       result_text = QtWidgets.QGraphicsTextItem("%.3f" % result.result)
       result_text.setFont(font)
       result_text.setPos(-self.view.width() / 2 + 50,
                          -self.view.height() / 2 + 20)
       self.scene.addItem(result_text)
       
       self.print_tree(result.tree, 25, -100, font, 100)

    def print_tree(self, tree, x, y, font, offset):
        if tree is None:
            return
        result_text = QtWidgets.QGraphicsTextItem(str(tree.data))
        font.setPointSize(10)
        result_text.setFont(font)
        result_text.setPos(x+5, y+5)
        self.scene.addItem(TreeNode(x, y))
        self.scene.addItem(result_text)
        if tree.left is not None:
            c1_x = x + TreeNode.radius
            c1_y = y + TreeNode.radius
            c2_x = c1_x - offset
            c2_y = c1_y + 60

            dv = center_to_circle(c1_x, c1_y, c2_x, c2_y)

            self.scene.addLine(c1_x + dv.x, c1_y + dv.y, c2_x - dv.x, c2_y - dv.y)

        if tree.right is not None:
            c1_x = x + TreeNode.radius
            c1_y = y + TreeNode.radius
            c2_x = c1_x + offset
            c2_y = c1_y + 60

            dv = center_to_circle(c1_x, c1_y, c2_x, c2_y)

            self.scene.addLine(c1_x + dv.x, c1_y + dv.y, c2_x - dv.x, c2_y - dv.y)


        self.print_tree(tree.left, x - offset, y + 60, font, offset * 0.70)
        self.print_tree(tree.right, x + offset, y + 60, font, offset * 0.70)
       

       
class TreeNode(QtWidgets.QGraphicsEllipseItem):
    diameter = 35
    radius = diameter/2
    def __init__(self, x, y):
        super(QtWidgets.QGraphicsEllipseItem, self).__init__(QtCore.QRectF(x, y, TreeNode.diameter, TreeNode.diameter))

def center_to_circle(x1, y1, x2, y2):
    vec = (x2 - x1, y2 - y1)
    length = math.sqrt((x2-x1)**2 + (y2-y1)**2) 
    vec_n = ((x2-x1)/length, (y2-y1)/length)

    Vector = namedtuple('Vector', ['x', 'y'])
    return Vector(x=TreeNode.radius*vec_n[0], y=TreeNode.radius*vec_n[1])
