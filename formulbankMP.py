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
from PyQt5 import QtGui
from formulsayfa import Ui_MainWindow as a
import os 
import sys



class formulbnk(QtWidgets.QMainWindow):
    def __init__(self):
        super(formulbnk,self).__init__()
        self.fb = a()
        self.fb.setupUi(self)
        self.show()
        self.setWindowIcon(QtGui.QIcon('marelogo.ico'))
        self.fb.comboBox.currentTextChanged.connect(self.mateF)
        self.fb.comboBox_2.currentTextChanged.connect(self.ElecF)
        self.fb.pushButton.clicked.connect(self.mateHe)
        self.fb.pushButton_2.clicked.connect(self.ElecHe)

    def mateF(self):
        scb = self.fb.comboBox.currentText()
        x = scb.split('-')
        if x[1] == 'Kare Alanı':
            self.fb.lineEdit.setHidden(False)
            self.fb.label.setText('Kenar Verisi :')
            self.fb.lineEdit_2.setHidden(True)
            self.fb.lineEdit_3.setHidden(True)
            self.fb.label_2.setHidden(True)
            self.fb.label_3.setHidden(True)
            self.fb.lineEdit.clear()
            self.fb.lineEdit_2.clear()
            self.fb.lineEdit_3.clear()
            self.fb.textBrowser.clear()
        elif x[1] == 'Dikdörtgen Alanı' :
            self.fb.lineEdit.setHidden(False)
            self.fb.lineEdit_2.setHidden(False)
            self.fb.lineEdit_3.setHidden(True)
            self.fb.label_3.setHidden(False)
            self.fb.label_2.setHidden(True)
            self.fb.label.setText('Kısa Kenar Verisi :')
            self.fb.label_3.setText('Uzun Kenar Verisi :')
            self.fb.lineEdit.clear()
            self.fb.lineEdit_2.clear()
            self.fb.lineEdit_3.clear()
            self.fb.textBrowser.clear()
        elif x[1] == 'Yamuk Alanı' :
            self.fb.lineEdit.setHidden(False)
            self.fb.lineEdit_2.setHidden(False)
            self.fb.lineEdit_3.setHidden(False)
            self.fb.label_3.setHidden(False)
            self.fb.label_2.setHidden(False)
            self.fb.label.setText('Alt taban uzunluğu :')
            self.fb.label_3.setText('Üst taban uzunluğu :')
            self.fb.label_2.setText('Yükseklik :')
            self.fb.lineEdit.clear()
            self.fb.lineEdit_2.clear()
            self.fb.lineEdit_3.clear()
            self.fb.textBrowser.clear()
        elif x[1] == 'Paralel Kenarın Alanı' :
            self.fb.lineEdit.setHidden(False)
            self.fb.lineEdit_2.setHidden(False)
            self.fb.label_3.setHidden(False)
            self.fb.lineEdit_3.setHidden(True)
            self.fb.label_2.setHidden(True)
            self.fb.label.setText('Taban Kenarı :')
            self.fb.label_3.setText('Tabana inen Yükseklik :')
            self.fb.lineEdit.clear()
            self.fb.lineEdit_2.clear()
            self.fb.lineEdit_3.clear()
            self.fb.textBrowser.clear()
        elif x[1] == 'Silindir Hacmi' :
            self.fb.lineEdit.setHidden(False)
            self.fb.lineEdit_2.setHidden(False)
            self.fb.label_3.setHidden(False)
            self.fb.lineEdit_3.setHidden(True)
            self.fb.label_2.setHidden(True)
            self.fb.label.setText('Taban Yarıçapı :')
            self.fb.label_3.setText('Yükseklik :')
            self.fb.lineEdit.clear()
            self.fb.lineEdit_2.clear()
            self.fb.lineEdit_3.clear()
            self.fb.textBrowser.clear()
        elif x[1] == 'Küpün Hacmi' :
            self.fb.lineEdit.setHidden(False)
            self.fb.lineEdit_2.setHidden(True)
            self.fb.label_3.setHidden(True)
            self.fb.lineEdit_3.setHidden(True)
            self.fb.label_2.setHidden(True)
            self.fb.label.setText('Bir Kenar Uzunluğu :')
            self.fb.lineEdit.clear()
            self.fb.lineEdit_2.clear()
            self.fb.lineEdit_3.clear()
            self.fb.textBrowser.clear()
        elif x[1] == 'Dikdörtgen Prizmasının Hacmi' :
            self.fb.lineEdit.setHidden(False)
            self.fb.lineEdit_2.setHidden(False)
            self.fb.label_3.setHidden(False)
            self.fb.lineEdit_3.setHidden(False)
            self.fb.label_2.setHidden(False)
            self.fb.label.setText('En Bilgisi :')
            self.fb.label_3.setText('Boy Bilgisi :')
            self.fb.label_2.setText('Yükseklik Bilgisi :')
            self.fb.lineEdit.clear()
            self.fb.lineEdit_2.clear()
            self.fb.lineEdit_3.clear()
            self.fb.textBrowser.clear()
        elif x[1] == 'Kare Prizmanın Hacmi' :
            self.fb.lineEdit.setHidden(False)
            self.fb.lineEdit_2.setHidden(False)
            self.fb.label_3.setHidden(False)
            self.fb.lineEdit_3.setHidden(True)
            self.fb.label_2.setHidden(True)
            self.fb.label.setText('Kare Prizma Tabanı :')
            self.fb.label_3.setText('Yükseklik :')
            self.fb.lineEdit.clear()
            self.fb.lineEdit_2.clear()
            self.fb.lineEdit_3.clear()
            self.fb.textBrowser.clear()
        elif x[1] == 'Dik Prizmaların Hacmi' :
            self.fb.lineEdit.setHidden(False)
            self.fb.lineEdit_2.setHidden(False)
            self.fb.label_3.setHidden(False)
            self.fb.lineEdit_3.setHidden(True)
            self.fb.label_2.setHidden(True)
            self.fb.label.setText('Taban bilgisi :')
            self.fb.label_3.setText('Yükseklik bilgisi :')
            self.fb.lineEdit.clear()
            self.fb.lineEdit_2.clear()
            self.fb.lineEdit_3.clear()
            self.fb.textBrowser.clear()
        elif x[1] == 'Çemberin ve Dairenin Çevresi' :
            self.fb.lineEdit.setHidden(False)
            self.fb.lineEdit_2.setHidden(True)
            self.fb.label_3.setHidden(True)
            self.fb.lineEdit_3.setHidden(True)
            self.fb.label_2.setHidden(True)
            self.fb.label.setText('Yarıçap Bilgisi :')
            self.fb.lineEdit.clear()
            self.fb.lineEdit_2.clear()
            self.fb.lineEdit_3.clear()
            self.fb.textBrowser.clear()

    def ElecF(self):
        scb = self.fb.comboBox_2.currentText()
        x = scb.split('-')
        if x[1] == 'Akım Şiddeti':
            self.fb.lineEdit_5.setHidden(False)
            self.fb.lineEdit_4.setHidden(False)
            self.fb.lineEdit_6.setHidden(True)
            self.fb.label_6.setHidden(False)
            self.fb.label_5.setHidden(True)
            self.fb.label_6.setText('Gerilim :')
            self.fb.label_4.setText('Direnç :')
            self.fb.lineEdit_5.clear()
            self.fb.lineEdit_4.clear()
            self.fb.lineEdit_6.clear()
            self.fb.textBrowser_2.clear()
        elif x[1] == 'Direnç Hesabı' :
            self.fb.lineEdit_5.setHidden(False)
            self.fb.lineEdit_4.setHidden(False)
            self.fb.lineEdit_6.setHidden(True)
            self.fb.label_6.setHidden(False)
            self.fb.label_5.setHidden(True)
            self.fb.label_6.setText('Gerilim :')
            self.fb.label_4.setText('Akım Şiddeti :')
            self.fb.lineEdit_5.clear()
            self.fb.lineEdit_4.clear()
            self.fb.lineEdit_6.clear()
            self.fb.textBrowser_2.clear()
        elif x[1] == 'Gerilim Hesabı' :
            self.fb.lineEdit_5.setHidden(False)
            self.fb.lineEdit_4.setHidden(False)
            self.fb.lineEdit_6.setHidden(True)
            self.fb.label_6.setHidden(False)
            self.fb.label_5.setHidden(True)
            self.fb.label_6.setText('Akım Şiddeti :')
            self.fb.label_4.setText('Direnç :')
            self.fb.lineEdit_5.clear()
            self.fb.lineEdit_4.clear()
            self.fb.lineEdit_6.clear()
            self.fb.textBrowser_2.clear()
        elif x[1] == 'Kondansatorde Depolanan Enerji Hesabı' :
            self.fb.lineEdit_5.setHidden(False)
            self.fb.lineEdit_4.setHidden(False)
            self.fb.lineEdit_6.setHidden(True)
            self.fb.label_6.setHidden(False)
            self.fb.label_5.setHidden(True)
            self.fb.label_6.setText('Yük Değeri :')
            self.fb.label_4.setText('Potansiyel Fark Değeri :')
            self.fb.lineEdit_5.clear()
            self.fb.lineEdit_4.clear()
            self.fb.lineEdit_6.clear()
            self.fb.textBrowser_2.clear()
        elif x[1] == 'Sığa Hesabı' :
            self.fb.lineEdit_5.setHidden(False)
            self.fb.lineEdit_4.setHidden(False)
            self.fb.lineEdit_6.setHidden(True)
            self.fb.label_6.setHidden(False)
            self.fb.label_5.setHidden(True)
            self.fb.label_6.setText('Yük Değeri :')
            self.fb.label_4.setText('Potansiyel Fark Değeri :')
            self.fb.lineEdit_5.clear()
            self.fb.lineEdit_4.clear()
            self.fb.lineEdit_6.clear()
            self.fb.textBrowser_2.clear()

    def mateHe(self):
        try :
            scb = self.fb.comboBox.currentText()
            x = scb.split('-')
            pi = 3.14
            print(x)
            if x[1] == 'Kare Alanı':
                sayi = self.fb.lineEdit.text()
                formul = "a.a"
                hesap = int(sayi)*int(sayi)
                self.fb.textBrowser.setText(f'Kare Alanı Formülü : {formul}\nSonuç : {sayi}x{sayi} = {hesap} ')
            elif x[1] == 'Dikdörtgen Alanı' :
                kisa = self.fb.lineEdit.text()
                uzun = self.fb.lineEdit_2.text()
                formul =  "a.b"
                hesap = int(kisa)*int(uzun)
                self.fb.textBrowser.setText(f'Dikdörtgen Alanı Formülü : {formul}\nSonuç : {kisa}x{uzun} = {hesap} ')
            elif x[1] == 'Yamuk Alanı' :
                atab = self.fb.lineEdit.text()
                utab = self.fb.lineEdit_2.text()
                yks = self.fb.lineEdit_3.text()
                formul = '(a+b)*h/2'
                hesap = (int(atab)+int(utab))*int(yks)/2
                self.fb.textBrowser.setText(f'Yamuk Alanı Formülü : {formul}\nSonuç : ({atab}+{utab})x{yks}/2 = {hesap} ')
            elif x[1] == 'Paralel Kenarın Alanı' :
                tk = self.fb.lineEdit.text()
                tiy = self.fb.lineEdit_2.text()
                formul = 'a*h'
                hesap = int(tk)*int(tiy)
                self.fb.textBrowser.setText(f'Paralel Kenarın Alanı Formülü : {formul}\nSonuç : {tk}x{tiy} = {hesap} ')
            elif x[1] == 'Silindir Hacmi' :
                r = self.fb.lineEdit.text()
                h = self.fb.lineEdit_2.text()
                formul = '\nV = π.r².h | π = 3,14'
                hesap = pi*(int(r)**2)*int(h)
                self.fb.textBrowser.setText(f'Silindir Hacim Formülü : {formul}\nSonuç : {pi}x({r}²)x{h} = {hesap} ')
            elif x[1] == 'Küpün Hacmi' :
                a = self.fb.lineEdit.text()
                formul = 'h = a³'
                hesap = int(a)**3
                self.fb.textBrowser.setText(f'Küpün Hacim Formülü : {formul}\nSonuç : {a}³ = {hesap} ')
            elif x[1] == 'Dikdörtgen Prizmasının Hacmi' :
                e = self.fb.lineEdit.text()
                b = self.fb.lineEdit_2.text()
                h = self.fb.lineEdit_3.text()
                formul = "H = a.b.c"
                hesap = int(e)*int(b)*int(h)
                self.fb.textBrowser.setText(f'Dikdörtgen Prizmasının Hacim Formülü : {formul}\nSonuç : {e}x{b}x{h} = {hesap} ')
            elif x[1] == 'Kare Prizmanın Hacmi' :
                kpt = self.fb.lineEdit.text()
                h = self.fb.lineEdit_2.text()
                formul = "a².h"
                hesap = int(kpt)**2*int(h)
                self.fb.textBrowser.setText(f'Kare Prizmanın Hacim Formülü : {formul}\nSonuç : {kpt}²x{h} = {hesap} ')
            elif x[1] == 'Dik Prizmaların Hacmi' :
                t = self.fb.lineEdit.text()
                h = self.fb.lineEdit_2.text()
                formul = "V = a.h"
                hesap = int(t)*int(h)
                self.fb.textBrowser.setText(f'Kare Prizmanın Hacim Formülü : {formul}\nSonuç : V={t}x{h} = {hesap} ')
            elif x[1] == 'Çemberin ve Dairenin Çevresi' :
                t = self.fb.lineEdit.text()
                formul = "2.π.r"
                hesap = 2*pi*int(t)
                self.fb.textBrowser.setText(f'Çemberin veya Dairenin Çevre Formülü : {formul}\nSonuç : 2x{pi}x{t} = {hesap} ')
        except Exception:
            pass

    def ElecHe(self):
        try:
            scb = self.fb.comboBox_2.currentText()
            x = scb.split('-')
            print(x)
            if x[1] == 'Akım Şiddeti':
                V = self.fb.lineEdit_5.text()
                R = self.fb.lineEdit_4.text()
                formul = "I = V/R"
                hesap = int(V)/int(R)
                self.fb.textBrowser_2.setText(f'Akım Şiddeti Formülü : {formul}\nSonuç : {V}/{R} = {hesap} ')
            elif x[1] == 'Direnç Hesabı' :
                V = self.fb.lineEdit_5.text()
                R = self.fb.lineEdit_4.text()
                formul = "R = V/I"
                hesap = int(V)/int(R)
                self.fb.textBrowser_2.setText(f'Direnç Formülü : {formul}\nSonuç : {V}/{R} = {hesap} ')
            elif x[1] == 'Gerilim Hesabı' :
                V = self.fb.lineEdit_5.text()
                R = self.fb.lineEdit_4.text()
                formul = "V = I.R"
                hesap = int(V)*int(R)
                self.fb.textBrowser_2.setText(f'Gerilim Formülü : {formul}\nSonuç : {V}.{R} = {hesap} ')
            elif x[1] == 'Kondansatorde Depolanan Enerji Hesabı' :
                Q = self.fb.lineEdit_5.text()
                V = self.fb.lineEdit_4.text()
                formul = "Uc = 1/2.Q.V"
                hesap = 1/2*int(Q)*int(V)
                self.fb.textBrowser_2.setText(f'Kondansatörde Depolanan Enerji Formülü : {formul}\nSonuç : 1/2.{Q}.{V} = {hesap} ')
            elif x[1] == 'Sığa Hesabı' :
                Q = self.fb.lineEdit_5.text()
                V = self.fb.lineEdit_4.text()
                formul = "C = Q/V"
                hesap = int(Q)/int(V)
                self.fb.textBrowser_2.setText(f'Sığa Hesabı Formülü : {formul}\nSonuç : {Q}/{V} = {hesap} ')
        except Exception:
            pass

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    main = formulbnk()
    app.exit(app.exec_())