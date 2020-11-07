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

from hardpsw import Ui_MainWindow as a
from PyQt5 import QtWidgets
from PyQt5 import QtCore
import sys
import os
import string
from random import *
import time
from pyqrcode import QRCode
from PIL import Image
import pyqrcode


class hdrpsw(QtWidgets.QMainWindow):
    def __init__(self):
        super(hdrpsw,self).__init__()
        self.ui = a()
        self.ui.setupUi(self)
        self.setting()
        self.show()
        self.ui.radioButton.setChecked(True)

        self.ui.radioButton.toggled.connect(self.selected)
        self.ui.radioButton_2.toggled.connect(self.selected)
        self.ui.radioButton_3.toggled.connect(self.selected)

        self.ui.checkBox.stateChanged.connect(self.show_state)

        self.ui.pushButton.clicked.connect(self.olusturucu1)
        self.ui.pushButton_2.clicked.connect(self.copy)

        self.ui.actionTr.triggered.connect(self.tr)
        self.ui.action_ngilizce_2.triggered.connect(self.ing)
        self.ui.pushButton_3.clicked.connect(self.qr)
    
    def setting(self):
        with open('settinghpw.py','r',encoding='UTF-8') as file :
            b = file.read()

        if b == '' :
            with open('settinghpw.py','w+',encoding='UTF-8') as file :
                file.write('TR Seçildi.')
                self.setWindowTitle('Şifre Oluşturucu | MARESAL PRM')
                self.ui.groupBox.setTitle('Şifre Türünü Seçiniz.')
                self.ui.radioButton.setText('Sadece Harf')
                self.ui.radioButton_2.setText("Sadece Rakam")
                self.ui.radioButton_3.setText("Her İkiside Olsun.")
                self.ui.checkBox.setText('Özel Karakterler Eklensi mi ?')
                self.ui.groupBox_2.setTitle('Karakter Boyutu Seçiniz.')
                self.ui.label.setText('Şifreniz :')
                self.ui.pushButton.setText('Oluştur')
                self.ui.pushButton_2.setText('Kopyala')
                self.ui.menuDil.setTitle('Dil')
                self.ui.actionTr.setText('Türkçe')
                self.ui.action_ngilizce_2.setText('İngilizce')
                self.ui.actionTr.setChecked(True)
                self.ui.action_ngilizce_2.setChecked(False)
        elif b == 'TR Seçildi.' :
            self.setWindowTitle('Şifre Oluşturucu | MARESAL PRM')
            self.ui.groupBox.setTitle('Şifre Türünü Seçiniz.')
            self.ui.radioButton.setText('Sadece Harf')
            self.ui.radioButton_2.setText("Sadece Rakam")
            self.ui.radioButton_3.setText("Her İkiside Olsun.")
            self.ui.checkBox.setText('Özel Karakterler Eklensi mi ?')
            self.ui.groupBox_2.setTitle('Karakter Boyutu Seçiniz.')
            self.ui.label.setText('Şifreniz :')
            self.ui.pushButton.setText('Oluştur')
            self.ui.pushButton_2.setText('Kopyala')
            self.ui.menuDil.setTitle('Dil')
            self.ui.actionTr.setText('Türkçe')
            self.ui.action_ngilizce_2.setText('İngilizce')
            self.ui.actionTr.setChecked(True)
            self.ui.action_ngilizce_2.setChecked(False)
        elif b == 'EN Selected.' :
            self.setWindowTitle('Password Generator | MARESAL PRM')
            self.ui.groupBox.setTitle('Select Password Type')
            self.ui.radioButton.setText('Letter Only')
            self.ui.radioButton_2.setText("Digit Only")
            self.ui.radioButton_3.setText("Have Both")
            self.ui.checkBox.setText('Adding Special Characters?')
            self.ui.groupBox_2.setTitle('Select Character Size.')
            self.ui.label.setText('Your password :')
            self.ui.pushButton.setText('Create')
            self.ui.pushButton_2.setText('Copy')
            self.ui.menuDil.setTitle('Language')
            self.ui.actionTr.setText('Turkish')
            self.ui.action_ngilizce_2.setText('English')
            self.ui.actionTr.setChecked(False)
            self.ui.action_ngilizce_2.setChecked(True)

    def selected(self):
        self.sender()

    def show_state(self):
        self.sender()

    def olusturucu1(self):
        items = self.ui.groupBox.findChildren(QtWidgets.QRadioButton)
        n = self.ui.comboBox.currentText()
        y = int(n)
        
        if self.ui.checkBox.isChecked() == False:
            for i in items:
                if i.isChecked():
                    if i.text() == 'Sadece Harf' or i.text() == 'Letter Only' :
                        character = string.ascii_letters+string.ascii_lowercase+string.ascii_uppercase
                        paswd =''.join(choice(character) for x in range(randint(y-3,y)))
                        self.ui.lineEdit.setText(paswd)
                    elif i.text() == 'Sadece Rakam' or i.text() == 'Digit Only':
                        character = string.digits
                        paswd = ''.join(choice(character) for x in range(randint(y-3,y)))
                        self.ui.lineEdit.setText(paswd)
                    elif i.text() == 'Her İkiside Olsun.' or i.text() == 'Have Both' :
                        character = string.ascii_letters+string.digits
                        paswd =''.join(choice(character) for x in range(randint(y-3,y)))
                        self.ui.lineEdit.setText(paswd)
        else :
            for i in items:
                if i.isChecked():
                    if i.text() == 'Sadece Harf' or i.text() == 'Letter Only':
                        character = string.ascii_letters+string.ascii_lowercase+string.ascii_uppercase+string.punctuation
                        paswd =''.join(choice(character) for x in range(randint(y-3,y)))
                        self.ui.lineEdit.setText(paswd)
                    elif i.text() == 'Sadece Rakam' or i.text() == 'Digit Only':
                        character = string.digits+string.punctuation
                        paswd = ''.join(choice(character) for x in range(randint(y-3,y)))
                        self.ui.lineEdit.setText(paswd)
                    elif i.text() == 'Her İkiside Olsun' or i.text() == 'Have Both':
                        character = string.ascii_letters+string.digits+string.punctuation
                        paswd =''.join(choice(character) for x in range(randint(y-3,y)))
                        self.ui.lineEdit.setText(paswd)
    
    def copy(self):
        cp = QtWidgets.QApplication.clipboard()
        cp.clear()
        cp.setText(self.ui.lineEdit.text())
    
    def qr(self):
        paswd = self.ui.lineEdit.text()
        character = string.ascii_letters
        urlName =''.join(choice(character) for x in range(randint(1,10)))
        url = pyqrcode.create(paswd)
        url.png(f'{urlName}.png',scale=6)
        jpath = os.path.realpath(f'{urlName}.png')
        x = Image.open(jpath)
        x.show()




    def tr(self):
        self.setWindowTitle('Şifre Oluşturucu | MARESAL PRM')
        self.ui.groupBox.setTitle('Şifre Türünü Seçiniz.')
        self.ui.radioButton.setText('Sadece Harf')
        self.ui.radioButton_2.setText("Sadece Rakam")
        self.ui.radioButton_3.setText("Her İkiside Olsun.")
        self.ui.checkBox.setText('Özel Karakterler Eklensi mi ?')
        self.ui.groupBox_2.setTitle('Karakter Boyutu Seçiniz.')
        self.ui.label.setText('Şifreniz :')
        self.ui.pushButton.setText('Oluştur')
        self.ui.pushButton_2.setText('Kopyala')
        self.ui.menuDil.setTitle('Dil')
        self.ui.actionTr.setText('Türkçe')
        self.ui.action_ngilizce_2.setText('İngilizce')
        self.ui.actionTr.setChecked(True)
        self.ui.action_ngilizce_2.setChecked(False)
        with open('settinghpw.py','w+', encoding='UTF-8') as file :
            file.write('TR Seçildi.')
        self.close()
        time.sleep(2.5)
        self.show()

    def ing(self):
        self.setWindowTitle('Password Generator | MARESAL PRM')
        self.ui.groupBox.setTitle('Select Password Type')
        self.ui.radioButton.setText('Letter Only')
        self.ui.radioButton_2.setText("Digit Only")
        self.ui.radioButton_3.setText("Have Both")
        self.ui.checkBox.setText('Adding Special Characters?')
        self.ui.groupBox_2.setTitle('Select Character Size.')
        self.ui.label.setText('Your password :')
        self.ui.pushButton.setText('Create')
        self.ui.pushButton_2.setText('Copy')
        self.ui.menuDil.setTitle('Language')
        self.ui.actionTr.setText('Turkish')
        self.ui.action_ngilizce_2.setText('English')
        self.ui.actionTr.setChecked(False)
        self.ui.action_ngilizce_2.setChecked(True)
        with open('settinghpw.py','w+', encoding='UTF-8') as file :
            file.write('EN Selected.')
        self.close()
        time.sleep(2.5)
        self.show()




                    




if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle('Fusion')
    main = hdrpsw()
    sys.exit(app.exec_())
    