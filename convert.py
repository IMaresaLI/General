# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'convert.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(493, 395)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/icons/marelogo.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(65, 100, 291, 32))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(175, 140, 141, 31))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(400, 0, 75, 32))
        self.pushButton_2.setObjectName("pushButton_2")
        self.toolButton = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton.setGeometry(QtCore.QRect(330, 100, 25, 32))
        self.toolButton.setObjectName("toolButton")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(355, 100, 69, 32))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(90, 180, 311, 121))
        self.textBrowser.setObjectName("textBrowser")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 10, 411, 341))
        self.label.setStyleSheet("image: url(:/newPrefix/icons/aa.png);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label.raise_()
        self.lineEdit.raise_()
        self.pushButton.raise_()
        self.pushButton_2.raise_()
        self.toolButton.raise_()
        self.comboBox.raise_()
        self.textBrowser.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 493, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Resim Çevirici | Maresal PRM"))
        self.pushButton.setText(_translate("MainWindow", "Çevir"))
        self.pushButton_2.setText(_translate("MainWindow", "Yenile"))
        self.toolButton.setText(_translate("MainWindow", "..."))
        self.comboBox.setItemText(0, _translate("MainWindow", "PNG"))
        self.comboBox.setItemText(1, _translate("MainWindow", "JPG"))
        self.comboBox.setItemText(2, _translate("MainWindow", "GIF"))
        self.comboBox.setItemText(3, _translate("MainWindow", "ICO"))
import icons