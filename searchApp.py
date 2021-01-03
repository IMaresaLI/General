################################################
################################################
################################################
#########*******###*******####**********########
########**#####**#**#####**###**######**########
########**#####**#**#####**###**######**########
########**#####**#**#####**###**********########
########**#####**#**#####**###**################
########**#####**#**#####**###**################
########**######***######**###**################
########**###############**###**################
########**###############**###**################
################################################
########Copyright © Maresal Programming#########
################################################

from PyQt5 import QtWidgets
from PyQt5 import QtCore
from PyQt5 import QtGui
from tarama import Ui_MainWindow
import os 
import sys
import psutil
import datetime

class searchFiles(QtWidgets.QMainWindow):
    def __init__(self):
        super(searchFiles,self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setStyleSheet(open("style.css","r").read())
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.show()
        self.loadingProgram()
        
        self.ui.pushButton_3.clicked.connect(self.minimize)
        self.ui.pushButton_2.clicked.connect(self.exit)
        self.ui.pushButton.clicked.connect(self.search)
        self.ui.listWidget.currentItemChanged.connect(self.fileDescription)



    def loadingProgram(self):
        list = []
        for i in psutil.disk_partitions():
            list.append(i.device)
        self.ui.comboBox.addItems(list)
        list2 = [".exe",".bin",".bat",".vvv",".zip",".rar",".py",".dart",".css"]
        self.ui.comboBox_2.addItems(list2)

    def search(self):
        try :
            self.ui.lineEdit.clear()
            self.ui.listWidget.clear()       
            sysPath = self.ui.comboBox.currentText()
            fileExtent = self.ui.comboBox_2.currentText()
            dir_path = os.path.dirname(os.path.realpath(sysPath))
            
            for root,dirs,files in os.walk(dir_path): 
                for file in files:
                    if file.endswith(fileExtent): 
                        self.ui.listWidget.addItem(root+'/'+str(file))
                        self.ui.lineEdit.setText(str(len(file)))
        except Exception:
            pass

    def fileDescription(self):
        try: 
            url = self.ui.listWidget.currentItem()
            information = os.stat(url.text())
            createDate = datetime.datetime.fromtimestamp(information.st_ctime)
            lastAccess = datetime.datetime.fromtimestamp(information.st_atime)
            lastReplace = datetime.datetime.fromtimestamp(information.st_mtime)
            fileSize = (information.st_size/1024) / 1024

            self.ui.textBrowser.setText(
                f"Dosya path : {url.text()}\n"
                f"Oluşturulma Tarihi : {createDate}\n"
                f"Son Erişim Tarihi : {lastAccess}\n"
                f"Son Değişim Tarihi : {lastReplace}\n"
                f"Dosya Boyutu : {round(fileSize,2)} MB")
        except Exception :
            pass

    def minimize(self):
        main.showMinimized()

    def exit(self):
        app.exit()


# Ekran Sürükleme Ayarları

    def mousePressEvent(self, event):
        if event.buttons() == QtCore.Qt.LeftButton:
            self.dragPos = event.globalPos()
            event.accept()

    def mouseMoveEvent(self, event):
        if event.buttons() == QtCore.Qt.LeftButton:
            self.move(self.pos() + event.globalPos() - self.dragPos)
            self.dragPos = event.globalPos()
            event.accept()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    main = searchFiles()
    app.setStyle("Fusion")
    app.exit(app.exec_())