# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/alcros33/Sources/QT/Curso_PyQt/2_Designer/Complete/MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(274, 374)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit_1 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_1.setGeometry(QtCore.QRect(60, 30, 151, 51))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_1.setFont(font)
        self.lineEdit_1.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_1.setObjectName("lineEdit_1")
        self.sumButton = QtWidgets.QPushButton(self.centralwidget)
        self.sumButton.setGeometry(QtCore.QRect(90, 190, 99, 38))
        self.sumButton.setObjectName("sumButton")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(60, 100, 151, 51))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(60, 260, 151, 51))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_3.setPlaceholderText("")
        self.lineEdit_3.setObjectName("lineEdit_3")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 274, 30))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.lineEdit_1, self.lineEdit_2)
        MainWindow.setTabOrder(self.lineEdit_2, self.sumButton)
        MainWindow.setTabOrder(self.sumButton, self.lineEdit_3)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Sumador"))
        self.lineEdit_1.setPlaceholderText(_translate("MainWindow", "Num1"))
        self.sumButton.setText(_translate("MainWindow", "Sumar"))
        self.lineEdit_2.setPlaceholderText(_translate("MainWindow", "Num2"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionExit.setShortcut(_translate("MainWindow", "Ctrl+Q"))


