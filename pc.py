# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pc.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(690, 415)
        MainWindow.setMinimumSize(QtCore.QSize(690, 415))
        MainWindow.setMaximumSize(QtCore.QSize(690, 415))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/icons/marelogo.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.cpuBar = QtWidgets.QProgressBar(self.centralwidget)
        self.cpuBar.setGeometry(QtCore.QRect(470, 20, 201, 41))
        self.cpuBar.setProperty("value", 24)
        self.cpuBar.setOrientation(QtCore.Qt.Vertical)
        self.cpuBar.setTextDirection(QtWidgets.QProgressBar.TopToBottom)
        self.cpuBar.setObjectName("cpuBar")
        self.ramBar = QtWidgets.QProgressBar(self.centralwidget)
        self.ramBar.setGeometry(QtCore.QRect(470, 100, 201, 41))
        self.ramBar.setProperty("value", 24)
        self.ramBar.setOrientation(QtCore.Qt.Vertical)
        self.ramBar.setObjectName("ramBar")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(20, 10, 421, 101))
        self.groupBox.setObjectName("groupBox")
        self.diskYonetimi = QtWidgets.QTextBrowser(self.groupBox)
        self.diskYonetimi.setGeometry(QtCore.QRect(10, 30, 201, 71))
        self.diskYonetimi.setStyleSheet("#diskYonetimi{background-color: transparent;}")
        self.diskYonetimi.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.diskYonetimi.setFrameShadow(QtWidgets.QFrame.Plain)
        self.diskYonetimi.setLineWidth(0)
        self.diskYonetimi.setObjectName("diskYonetimi")
        self.diskYonetimi_2 = QtWidgets.QTextBrowser(self.groupBox)
        self.diskYonetimi_2.setGeometry(QtCore.QRect(210, 30, 201, 71))
        self.diskYonetimi_2.setStyleSheet("#diskYonetimi_2{background-color: transparent;}")
        self.diskYonetimi_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.diskYonetimi_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.diskYonetimi_2.setLineWidth(0)
        self.diskYonetimi_2.setObjectName("diskYonetimi_2")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(20, 110, 421, 281))
        self.groupBox_2.setObjectName("groupBox_2")
        self.cpuYonetimi = QtWidgets.QTextBrowser(self.groupBox_2)
        self.cpuYonetimi.setGeometry(QtCore.QRect(10, 20, 391, 261))
        self.cpuYonetimi.setStyleSheet("#cpuYonetimi{background-color: transparent;}")
        self.cpuYonetimi.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.cpuYonetimi.setFrameShadow(QtWidgets.QFrame.Plain)
        self.cpuYonetimi.setLineWidth(0)
        self.cpuYonetimi.setObjectName("cpuYonetimi")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(470, 70, 201, 21))
        self.label_3.setText("")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(470, 150, 201, 21))
        self.label_4.setText("")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.ramBar_2 = QtWidgets.QProgressBar(self.centralwidget)
        self.ramBar_2.setGeometry(QtCore.QRect(470, 180, 201, 41))
        self.ramBar_2.setProperty("value", 24)
        self.ramBar_2.setOrientation(QtCore.Qt.Vertical)
        self.ramBar_2.setObjectName("ramBar_2")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(470, 230, 201, 21))
        self.label_5.setText("")
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(470, 270, 91, 91))
        self.label.setStyleSheet("image: url(:/icons/icons/mplog.png);")
        self.label.setText("")
        self.label.setWordWrap(False)
        self.label.setOpenExternalLinks(True)
        self.label.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(580, 270, 91, 91))
        self.label_2.setStyleSheet("image: url(:/icons/icons/Python.png);")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 690, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Sistem Kontrol | Maresal PRM"))
        self.groupBox.setTitle(_translate("MainWindow", "Disk Bilgileri"))
        self.diskYonetimi.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'MS Shell Dlg 2\';\"><br /></p></body></html>"))
        self.diskYonetimi_2.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'MS Shell Dlg 2\';\"><br /></p></body></html>"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Genel Bilgiler"))
        self.cpuYonetimi.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'MS Shell Dlg 2\';\"><br /></p></body></html>"))
        self.label.setToolTip(_translate("MainWindow", "<html><head/><body><p>https://www.instagram.com/maresalp/</p></body></html>"))
        self.label_2.setToolTip(_translate("MainWindow", "<html><head/><body><p>https://www.python.org/</p></body></html>"))
import icons_rc
