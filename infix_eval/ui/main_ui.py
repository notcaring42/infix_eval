# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created: Mon Feb 10 22:21:56 2014
#      by: PyQt5 UI code generator 5.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(366, 454)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout.setObjectName("verticalLayout")
        self.treeView = QtWidgets.QGraphicsView(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.treeView.sizePolicy().hasHeightForWidth())
        self.treeView.setSizePolicy(sizePolicy)
        self.treeView.setObjectName("treeView")
        self.verticalLayout.addWidget(self.treeView)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.expressionLabel = QtWidgets.QLabel(self.centralwidget)
        self.expressionLabel.setObjectName("expressionLabel")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.expressionLabel)
        self.expressionLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.expressionLineEdit.setText("")
        self.expressionLineEdit.setObjectName("expressionLineEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.expressionLineEdit)
        self.evaluateButton = QtWidgets.QPushButton(self.centralwidget)
        self.evaluateButton.setObjectName("evaluateButton")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.SpanningRole, self.evaluateButton)
        self.verticalLayout.addLayout(self.formLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Infix Expression Evaluator"))
        self.expressionLabel.setText(_translate("MainWindow", "Expression:"))
        self.evaluateButton.setText(_translate("MainWindow", "Evaluate"))

