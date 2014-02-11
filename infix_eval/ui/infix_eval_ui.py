import math
from collections import namedtuple

from PyQt5 import QtWidgets, QtGui, QtCore

from infix_eval.ui import main_ui, error_dialog_ui
from infix_eval.evaluator import Evaluator


class InfixEvalUi(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
    
        # Initialize the main window
        self.main_window_ui = main_ui.Ui_MainWindow()
        self.main_window_ui.setupUi(self)

        # Register event handler for evaluate button
        self.main_window_ui.evaluateButton.clicked.connect(self.eval_and_print)

        # Initialize the error dialog
        self.error_dialog = ErrorDialog()

        # Initialize the graphics view
        self.scene = QtWidgets.QGraphicsScene()
        self.view = self.main_window_ui.treeView
        self.view.setRenderHints(QtGui.QPainter.Antialiasing)
        self.main_window_ui.treeView.setScene(self.scene)
        self.scene.setSceneRect(0, 0, self.view.width(), self.view.height())

        # Create the evaluator
        self.evaluator = Evaluator()

    # Evaluate the expression and output the results
    def eval_and_print(self):
        expression = self.main_window_ui.expressionLineEdit.text()

        # Return an error if the expression is empty
        if expression == '':
            self.error_dialog.error_msg_label.setText(
                "ERROR: Please enter an infix expression")
            self.error_dialog.show()
            return

        # Catch some possible errors
        try:
            result = self.evaluator.evaluate(expression)
        except ValueError as e:
            self.error_dialog.error_msg_label.setText("ERROR: %s" % e)
            self.error_dialog.show()
            return
        except IndexError:
            self.error_dialog.error_msg_label.setText(
                    "ERROR: Expression was invalid.")
            self.error_dialog.show()
            return

        # Clear the scene and show the results
        self.scene.clear()
        self.show_results(result)

    def show_results(self, result):
        font = QtGui.QFont("Droid Sans Mono")
        font.setPointSize(20)

        # Show the numerical result
        result_text = QtWidgets.QGraphicsTextItem("%.3f" % result.result)
        result_text.setFont(font)
        result_text.setPos(-self.view.width() / 2 + 50,
                           -self.view.height() / 2 + 20)
        self.scene.addItem(result_text)

        # Show the tree
        self.print_tree(result.tree, 25, -100, font, 100)

    def print_tree(self, tree, x, y, font, offset):
        if tree is None:
            return

        # Draw the tree node and the node data
        result_text = QtWidgets.QGraphicsTextItem(str(tree.data))
        font.setPointSize(10)
        result_text.setFont(font)
        result_text.setPos(x+5, y+5)
        self.scene.addItem(TreeNode(x, y))
        self.scene.addItem(result_text)

        # Draw connection lines to child nodes
        if tree.left is not None:
            self._connect_to_children(x, y, offset)
        if tree.right is not None:
            self._connect_to_children(x, y, -offset)

        # Recursively draw the left and right subtrees
        self.print_tree(tree.left, x - offset, y + 60, font, offset * 0.60)
        self.print_tree(tree.right, x + offset, y + 60, font, offset * 0.60)

    # Draws connection lines to child nodes
    def _connect_to_children(self, x, y, offset):
        c1_x = x + TreeNode.radius
        c1_y = y + TreeNode.radius
        c2_x = c1_x - offset
        c2_y = c1_y + 60

        dv = center_to_circle(c1_x, c1_y, c2_x, c2_y)

        self.scene.addLine(c1_x + dv.x, c1_y + dv.y,
                           c2_x - dv.x, c2_y - dv.y)


# Error dialog if the expression cannot be parsed
class ErrorDialog(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        # Initialize the ui
        self.dialog_ui = error_dialog_ui.Ui_Dialog()
        self.dialog_ui.setupUi(self)

        # When we press ok on the dialog, close it
        self.dialog_ui.pushButton.clicked.connect(self.hide)
        
        # Create a reference to the error label
        self.error_msg_label = self.dialog_ui.errorMsg

        # Set the label font to something more menacing
        self._set_font()

    def _set_font(self):
        font = self.error_msg_label.font()
        font.setPointSize(12)
        self.error_msg_label.setFont(font)

# Graphical representation of a BinaryNode
class TreeNode(QtWidgets.QGraphicsEllipseItem):
    diameter = 35
    radius = diameter/2

    def __init__(self, x, y):
        super().__init__(QtCore.QRectF(x, y, TreeNode.diameter,
                                       TreeNode.diameter))


# Returns a vector that represents the positional offset
# from the center of a node to the edge of it (on the outer circle)
def center_to_circle(x1, y1, x2, y2):
    vec = (x2 - x1, y2 - y1)
    length = math.sqrt((x2-x1)**2 + (y2-y1)**2)
    vec_n = ((x2-x1)/length, (y2-y1)/length)

    Vector = namedtuple('Vector', ['x', 'y'])
    return Vector(x=TreeNode.radius*vec_n[0], y=TreeNode.radius*vec_n[1])
