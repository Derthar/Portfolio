# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '1_form.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QToolTip, QMessageBox, QDesktopWidget


class Ui_Dialog(QWidget):

    def __init__(self):
        super().__init__()
        self.setupUi()

    def setupUi(self):
        self.setObjectName("Dialog")
        self.resize(637, 441)
        self.radioButton = QtWidgets.QRadioButton()
        self.radioButton.setGeometry(QtCore.QRect(20, 30, 82, 17))
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton()
        self.radioButton_2.setEnabled(True)
        self.radioButton_2.setGeometry(QtCore.QRect(110, 30, 82, 17))
        self.radioButton_2.setObjectName("radioButton_2")
        self.checkBox = QtWidgets.QCheckBox()
        self.checkBox.setGeometry(QtCore.QRect(20, 60, 70, 17))
        self.checkBox.setObjectName("checkBox")
        self.Start_button = QtWidgets.QPushButton()
        self.Start_button.setGeometry(QtCore.QRect(10, 410, 75, 23))
        self.Start_button.setObjectName("Start_button")
        self.Exit_button = QtWidgets.QPushButton()
        self.Exit_button.setGeometry(QtCore.QRect(90, 410, 75, 23))
        self.Exit_button.setObjectName("Exit_button")
        self.label = QtWidgets.QLabel()
        self.label.setGeometry(QtCore.QRect(20, 210, 571, 161))
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit()
        self.lineEdit.setGeometry(QtCore.QRect(10, 380, 531, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.Enter_button = QtWidgets.QPushButton()
        self.Enter_button.setGeometry(QtCore.QRect(550, 380, 75, 23))
        self.Enter_button.setObjectName("Enter_button")

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Dialog", "Dialog"))
        self.radioButton.setText(_translate("Dialog", "RadioButton"))
        self.radioButton_2.setText(_translate("Dialog", "RadioButton"))
        self.checkBox.setText(_translate("Dialog", "CheckBox"))
        self.Start_button.setText(_translate("Dialog", "Запустить"))
        self.Exit_button.setText(_translate("Dialog", "Выход"))
        self.label.setText(_translate("Dialog", "Terminal"))
        self.Enter_button.setText(_translate("Dialog", "Ввести"))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    program = Ui_Dialog()
    sys.exit(app.exec_())
