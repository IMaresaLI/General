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
from PIL import Image
from convert import Ui_MainWindow as ic
import sys
import os 



class imgConvert(QtWidgets.QMainWindow):
    def __init__(self):
        super(imgConvert,self).__init__()
        self.ui = ic()
        self.ui.setupUi(self)
        self.show()

        self.ui.toolButton.clicked.connect(self.geturl)
        self.ui.pushButton.clicked.connect(self.imgcon)
        self.ui.pushButton_2.clicked.connect(self.yenile)

    def yenile(self):
        QtWidgets.qApp.closeAllWindows()
        self.show()


    
    def geturl(self):
        try:
            a = QtWidgets.QFileDialog.getOpenFileName()
            self.ui.lineEdit.setText(a[0])
        except Exception as err:
            self.ui.textBrowser.setText(str(err))



    def imgcon(self):
        try:
            file = self.ui.lineEdit.text()
            x = self.ui.comboBox.currentText()
            if x == 'PNG':
                a = Image.open(file)
                text , ok = QtWidgets.QInputDialog.getText(self,"Resim Çevirici","Yeni resim için isim giriniz.",QtWidgets.QLineEdit.Normal)
                if text and ok :
                    a.save(f"{text}.png")
                    jpath = os.path.realpath(f"{text}.png")
                    self.ui.textBrowser.setText(f"PNG Çevirme Başarılı \nDosya Konumunuz : {jpath}")
            elif x == 'JPG':
                a = Image.open(file)
                text , ok = QtWidgets.QInputDialog.getText(self,"Resim Çevirici","Yeni resim için isim giriniz.",QtWidgets.QLineEdit.Normal)
                if text and ok :
                    z = a.convert("RGB")
                    z.save(f"{text}.jpg")
                    jpath = os.path.realpath(f"{text}.jpg")
                    self.ui.textBrowser.setText(f"Jpg Çevirme Başarılı \nDosya Konumunuz : {jpath}")
            elif x == 'GIF':
                a = Image.open(file)
                text , ok = QtWidgets.QInputDialog.getText(self,"Resim Çevirici","Yeni resim için isim giriniz.",QtWidgets.QLineEdit.Normal)
                if text and ok :
                    z = a.convert("RGB")
                    z.save(f"{text}.gif")
                    jpath = os.path.realpath(f"{text}.gif")
                    self.ui.textBrowser.setText(f"Gif Çevirme Başarılı \nDosya Konumunuz : {jpath}")
            elif x == 'ICO':
                a = Image.open(file)
                text , ok = QtWidgets.QInputDialog.getText(self,"Resim Çevirici","Yeni resim için isim giriniz.",QtWidgets.QLineEdit.Normal)
                if text and ok :
                    icon_sizes = [(16,16),(32,32),(48,48),(64,64)]
                    a.save(f"{text}.ico", sizes=icon_sizes)
                    jpath = os.path.realpath(f"{text}.ico")
                    self.ui.textBrowser.setText(f"Ico Çevirme Başarılı \nDosya Konumunuz : {jpath}")
        except Exception as err :
            self.ui.textBrowser.setText(str(err))           





if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    main = imgConvert()
    app.setStyle('Fusion')
    app.exit(app.exec_())
