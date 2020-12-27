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
#####################567########################

from PyQt5 import QtWidgets
from PyQt5 import QtCore
from PyQt5 import QtGui
from translate import Ui_MainWindow
from textblob import TextBlob
import os 
import sys



class transApp(QtWidgets.QMainWindow):
    def __init__(self):
        super(transApp,self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setStyleSheet(open("style.css","r").read())
        self.setWindowIcon(QtGui.QIcon('icons/marelogo.ico'))

        self.ui.textEdit.textChanged.connect(self.translater)
        self.ui.comboBox.currentIndexChanged.connect(self.translater)
        self.ui.comboBox_2.currentIndexChanged.connect(self.translater)
        self.ui.pushButton.clicked.connect(self.info)
    

    def translater(self):
        try:
            transDict = {"İngilizce":"en","Türkçe":"tr","Almanca":"de","Fransızca":"fr","İspanyolca":"es"}
            anaMetinDil = self.ui.comboBox.currentText()
            cevrilecekDil = self.ui.comboBox_2.currentText()
            anaMetin = self.ui.textEdit.toPlainText()
            metin = TextBlob(anaMetin)
            cevirme = metin.translate(from_lang=transDict[f"{anaMetinDil}"],to=transDict[f"{cevrilecekDil}"])
            self.ui.textEdit_2.setText(str(cevirme))
        except Exception as err:
            print(str(err))

    def info(self):
        QtWidgets.QMessageBox.about(
            self, "Program Hakkında", f'<html><head/><body><p align=\'center\'>Program Pythonun TextBlob kütüphanesi ile yapılmıştır.</p>\n<p align=\'center\'>Python Versiyonu : 3.8.6 V</p>\n<p align=\'center\'>Copyright © Maresal Programming</p></body></html>')




if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    main = transApp()
    main.show()
    app.setStyle("Fusion")
    app.exit(app.exec_())