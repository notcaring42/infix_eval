# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'error_dialog.ui'
#
# Created: Tue Feb 11 13:13:32 2014
#      by: PyQt5 UI code generator 5.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(376, 114)
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(280, 80, 85, 27))
        self.pushButton.setObjectName("pushButton")
        self.errorMsg = QtWidgets.QLabel(Dialog)
        self.errorMsg.setGeometry(QtCore.QRect(10, 10, 361, 61))
        self.errorMsg.setTextFormat(QtCore.Qt.PlainText)
        self.errorMsg.setAlignment(QtCore.Qt.AlignCenter)
        self.errorMsg.setObjectName("errorMsg")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Error"))
        self.pushButton.setText(_translate("Dialog", "OK"))
        self.errorMsg.setText(_translate("Dialog", "TextLabel"))

