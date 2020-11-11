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
from drh import Ui_MainWindow as dr
import sys
import os




class DRH(QtWidgets.QMainWindow):
    def __init__(self):
        super(DRH,self).__init__()
        self.dh = dr()
        self.dh.setupUi(self)
        self.show()
        self.dh.listWidget.clicked.connect(self.renkdegisimi)
        self.dh.listWidget_2.clicked.connect(self.renkdegisimi)
        self.dh.listWidget_3.clicked.connect(self.renkdegisimi)
        self.dh.listWidget_4.clicked.connect(self.renkdegisimi)

        self.dh.pushButton.clicked.connect(self.boxselects)

    def boxselects(self):
        a = self.dh.listWidget.currentRow()
        x = self.dh.listWidget_2.currentRow()
        zz = self.dh.listWidget_3.currentRow()
        b = self.dh.listWidget_4.currentItem()
        z = self.dh.listWidget_3.item(zz)
        p = z.text()
        c = p.split('*')
        
        if zz == 8 or zz == 9:
            s = ((a * 10) + x)*float(c[0])
            self.dh.lineEdit.setText("Sonuç : "+str(s)+' Ω | Tolerans : '+ b.text())
        else :
            s = ((a * 10) + x)*float(c[0])
            self.dh.lineEdit.setText("Sonuç : "+str(s)+' Ω | Tolerans : '+ b.text())

        

        

    def renkdegisimi(self):
        a = self.dh.listWidget.currentRow()
        if a == 0:
            self.dh.label.setStyleSheet("background-color: rgb(0, 0, 0);")
        elif a == 1 :
            self.dh.label.setStyleSheet("background-color: rgb(170, 85, 0);")
        elif a == 2 :
            self.dh.label.setStyleSheet("background-color: rgb(255, 0, 0);")
        elif a == 3 :
            self.dh.label.setStyleSheet("background-color: rgb(255, 69, 0);")        
        elif a == 4 :
            self.dh.label.setStyleSheet("background-color: rgb(255, 255, 0);")
        elif a == 5 :
            self.dh.label.setStyleSheet("background-color: rgb(0, 255, 0);")
        elif a == 6 :
            self.dh.label.setStyleSheet("background-color: rgb(0, 0, 255);")
        elif a == 7 :
            self.dh.label.setStyleSheet("background-color: rgb(128, 0, 128);")
        elif a == 8 :
            self.dh.label.setStyleSheet("background-color: rgb(54, 54, 54);")
        elif a == 9 :
            self.dh.label.setStyleSheet("background-color: rgb(255, 255, 255);")

        b = self.dh.listWidget_2.currentRow()
        if b == 0:
            self.dh.label_3.setStyleSheet("background-color: rgb(0, 0, 0);")
        elif b == 1 :
            self.dh.label_3.setStyleSheet("background-color: rgb(170, 85, 0);")
        elif b == 2 :
            self.dh.label_3.setStyleSheet("background-color: rgb(255, 0, 0);")
        elif b == 3 :
            self.dh.label_3.setStyleSheet("background-color: rgb(255, 69, 0);")        
        elif b == 4 :
            self.dh.label_3.setStyleSheet("background-color: rgb(255, 255, 0);")
        elif b == 5 :
            self.dh.label_3.setStyleSheet("background-color: rgb(0, 255, 0);")
        elif b == 6 :
            self.dh.label_3.setStyleSheet("background-color: rgb(0, 0, 255);")
        elif b == 7 :
            self.dh.label_3.setStyleSheet("background-color: rgb(128, 0, 128);")
        elif b == 8 :
            self.dh.label_3.setStyleSheet("background-color: rgb(54, 54, 54);")
        elif b == 9 :
            self.dh.label_3.setStyleSheet("background-color: rgb(255, 255, 255);")

        c = self.dh.listWidget_3.currentRow()
        if c == 0:
            self.dh.label_4.setStyleSheet("background-color: rgb(0, 0, 0);")
        elif c == 1 :
            self.dh.label_4.setStyleSheet("background-color: rgb(170, 85, 0);")
        elif c == 2 :
            self.dh.label_4.setStyleSheet("background-color: rgb(255, 0, 0);")
        elif c == 3 :
            self.dh.label_4.setStyleSheet("background-color: rgb(255, 69, 0);")        
        elif c == 4 :
            self.dh.label_4.setStyleSheet("background-color: rgb(255, 255, 0);")
        elif c == 5 :
            self.dh.label_4.setStyleSheet("background-color: rgb(0, 255, 0);")
        elif c == 6 :
            self.dh.label_4.setStyleSheet("background-color: rgb(0, 0, 255);")
        elif c == 8 :
            self.dh.label_4.setStyleSheet("background-color: rgb(255, 215, 0);")
        elif c == 9 :
            self.dh.label_4.setStyleSheet("background-color: rgb(130, 130, 130);")
        
        d = self.dh.listWidget_4.currentRow()
        if d == 0:
            self.dh.label_5.setStyleSheet("background-color: rgb(255, 215, 0);")
        elif d == 1 :
            self.dh.label_5.setStyleSheet("background-color: rgb(130, 130, 130);")
        elif d == 2 :
            self.dh.label_5.setStyleSheet("background-color: rgb(170, 85, 0);")
        elif d == 3 :
            self.dh.label_5.setStyleSheet("background-color: rgb(255, 0, 0);")        











if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    main = DRH()
    app.setStyle('Fusion')
    app.exit(app.exec_())