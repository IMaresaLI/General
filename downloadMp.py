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
from youtubeDownload import Ui_MainWindow as w
from pytube import YouTube
import os 
import sys
import random


class dwMp(QtWidgets.QMainWindow):
    def __init__(self):
        super(dwMp,self).__init__()
        self.dw = w()
        self.dw.setupUi(self)
        self.show()
        self.dw.pushButton.clicked.connect(self.indir)

    def indir(self):
        try :
            cb = self.dw.comboBox.currentText()
            if cb == '.mp4':
                self.mp4i()
            if cb == '.mp3':
                self.mp3i()
        except Exception:
            pass

    def mp4i(self):
        url = self.dw.lineEdit.text()
        dw = YouTube(f"{url}").streams.first().download()
        xx = dw.title()
        self.dw.textBrowser.setText(f'Dosya Başarılı bir şekilde indirildi.\nDosya Konumu : {xx}')


    def mp3i(self):
        try :
            url = self.dw.lineEdit.text()
            dw = YouTube(f"{url}").streams.first().download()
            mp4 = dw.title()
            new = random.randint(0,99)
            title_mp4 = os.path.splitext(mp4)
            n = title_mp4[0].split('\\')
            x = n[4]+".mp4"
            os.rename(mp4,x+'-'+str(new)+'.mp3')
            pth = os.path.realpath(x+'-'+str(new)+'.mp3')
            self.dw.textBrowser.setText(f'Dosya Başarılı bir şekilde indirildi.\nDosya Konumu : {pth}')
        except Exception as err :
            pass
            




if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    main = dwMp()
    app.setStyle('Fusion')
    app.exit(app.exec_())

