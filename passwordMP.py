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
from passwdMP import Ui_MainWindow as a 
import os 
import sys
import hashlib
from random import choice,randint
import string


class pwmp(QtWidgets.QMainWindow):
    def __init__(self):
        super(pwmp,self).__init__()
        self.pw = a()
        self.pw.setupUi(self)
        self.show()

        self.pw.comboBox_2.currentTextChanged.connect(self.sayfaD)
        self.pw.comboBox.currentTextChanged.connect(self.onePwsec)
        self.pw.pushButton.clicked.connect(self.onePw)
        self.pw.pushButton_2.clicked.connect(self.onepwkayit)
        self.pw.toolButton.clicked.connect(self.openfile)
        self.pw.comboBox_4.currentTextChanged.connect(self.cogulpwsec)
        self.pw.pushButton_3.clicked.connect(self.cogpw)
        self.pw.action_ifrelenenleri_Getir.triggered.connect(self.kayitget)
        self.pw.action_ifrelenenleri_Temizle.triggered.connect(self.kayitsil)
        self.pw.actionExit.triggered.connect(self.ex)
        self.pw.actionFacebook.triggered.connect(self.facebook)
        self.pw.actionInstagram.triggered.connect(self.instagram)
        self.pw.actionGithub.triggered.connect(self.github)

    def sayfaD(self):
        secim = self.pw.comboBox_2.currentText()
        if secim == 'Tek Şifreleme':
            self.pw.groupBox.setHidden(False)
            self.pw.groupBox_2.setHidden(True)
            self.pw.lineEdit_2.clear()
            self.pw.textBrowser_3.clear()
            self.pw.textBrowser_4.clear()
        elif secim == 'Çoğul Şifreleme':
            self.pw.groupBox.setHidden(True)
            self.pw.groupBox_2.setHidden(False)
            self.pw.lineEdit.clear()
            self.pw.textBrowser.clear()
            self.pw.textBrowser_2.clear()

    def onePwsec(self):
        sifrelemeTuru = self.pw.comboBox.currentText()
        
        if sifrelemeTuru == 'Md5':
            self.pw.comboBox_3.setEnabled(False)
        elif sifrelemeTuru == 'Sha224':
            self.pw.comboBox_3.setEnabled(False)
        elif sifrelemeTuru == 'Sha256':
            self.pw.comboBox_3.setEnabled(False)
        elif sifrelemeTuru == 'Sha384':
            self.pw.comboBox_3.setEnabled(False)            
        elif sifrelemeTuru == 'Sha512':
            self.pw.comboBox_3.setEnabled(False)
        elif sifrelemeTuru == 'Sha3_224':
            self.pw.comboBox_3.setEnabled(False)
        elif sifrelemeTuru == 'Sha3_256':
            self.pw.comboBox_3.setEnabled(False)
        elif sifrelemeTuru == 'Sha3_384':
            self.pw.comboBox_3.setEnabled(False)
        elif sifrelemeTuru == 'Sha3_512':
            self.pw.comboBox_3.setEnabled(False)
        elif sifrelemeTuru == 'Blake2b':
            self.pw.comboBox_3.setEnabled(True)
        elif sifrelemeTuru == 'Blake2s':
            self.pw.comboBox_3.setEnabled(True)
        elif sifrelemeTuru == 'Shake_128':
            self.pw.comboBox_3.setEnabled(True)
        elif sifrelemeTuru == 'Shake_256':
            self.pw.comboBox_3.setEnabled(True)

    def onePw(self):
        try :
            pw = self.pw.lineEdit.text()
            sifrelemeTuru = self.pw.comboBox.currentText()
            byteayar = self.pw.comboBox_3.currentText()
            ayirma = byteayar.split(' ')

            if sifrelemeTuru == 'Md5':
                pwmd = hashlib.md5(pw.encode('UTF-8')).hexdigest()
                self.pw.textBrowser.setText(f'Yazılan : {pw}\nMd5 ile Çevrilmiş Hali : {pwmd}')
            elif sifrelemeTuru == 'Sha224':
                pwmd = hashlib.sha224(pw.encode('UTF-8')).hexdigest()
                self.pw.textBrowser.setText(f'Yazılan  : {pw}\nSha224 ile Çevrilmiş Hali : {pwmd}')
            elif sifrelemeTuru == 'Sha256':
                pwmd = hashlib.sha256(pw.encode('UTF-8')).hexdigest()
                self.pw.textBrowser.setText(f'Yazılan  : {pw}\nSha256 ile Çevrilmiş Hali : {pwmd}')
            elif sifrelemeTuru == 'Sha384':
                pwmd = hashlib.sha384(pw.encode('UTF-8')).hexdigest()
                self.pw.textBrowser.setText(f'Yazılan  : {pw}\nSha384 ile Çevrilmiş Hali : {pwmd}')
            elif sifrelemeTuru == 'Sha512':
                pwmd = hashlib.sha512(pw.encode('UTF-8')).hexdigest()
                self.pw.textBrowser.setText(f'Yazılan  : {pw}\nSha512 ile Çevrilmiş Hali : {pwmd}')
            elif sifrelemeTuru == 'Sha3_224':
                pwmd = hashlib.sha3_224(pw.encode('UTF-8')).hexdigest()
                self.pw.textBrowser.setText(f'Yazılan  : {pw}\nSha3_224 ile Çevrilmiş Hali : {pwmd}')
            elif sifrelemeTuru == 'Sha3_256':
                pwmd = hashlib.sha3_256(pw.encode('UTF-8')).hexdigest()
                self.pw.textBrowser.setText(f'Yazılan  : {pw}\nSha3_256 ile Çevrilmiş Hali : {pwmd}')
            elif sifrelemeTuru == 'Sha3_384':
                pwmd = hashlib.sha3_384(pw.encode('UTF-8')).hexdigest()
                self.pw.textBrowser.setText(f'Yazılan  : {pw}\nSha3_384 ile Çevrilmiş Hali : {pwmd}')
            elif sifrelemeTuru == 'Sha3_512':
                pwmd = hashlib.sha3_512(pw.encode('UTF-8')).hexdigest()
                self.pw.textBrowser.setText(f'Yazılan  : {pw}\nSha3_512 ile Çevrilmiş Hali : {pwmd}')
            elif sifrelemeTuru == 'Blake2b':
                pwmd = hashlib.blake2b(pw.encode('UTF-8'),digest_size=int(ayirma[0])).hexdigest()
                self.pw.textBrowser.setText(f'Yazılan  : {pw}\nBlake2b ile Çevrilmiş Hali : {pwmd}')
            elif sifrelemeTuru == 'Blake2s':
                pwmd = hashlib.blake2s(pw.encode('UTF-8'),digest_size=int(ayirma[0])).hexdigest()
                self.pw.textBrowser.setText(f'Yazılan  : {pw}\nBlake2s ile Çevrilmiş Hali : {pwmd}')
            elif sifrelemeTuru == 'Shake_128':
                pwmd = hashlib.shake_128(pw.encode('UTF-8')).hexdigest(int(ayirma[0]))
                self.pw.textBrowser.setText(f'Yazılan  : {pw}\nShake_128 ile Çevrilmiş Hali : {pwmd}')
            elif sifrelemeTuru == 'Shake_256':
                pwmd = hashlib.shake_256(pw.encode('UTF-8')).hexdigest(int(ayirma[0]))
                self.pw.textBrowser.setText(f'Yazılan  : {pw}\nShake_256 ile Çevrilmiş Hali : {pwmd}')
        except Exception:
            pass

    def onepwkayit(self):
        try:
            textbx = self.pw.textBrowser.toPlainText()
            x = textbx.split(":")
            x2 = x[1].split('\n')
            x3 = x2[1].split(' ')
            dict = {"Metin": f"{x2[0]}",f"{x3[0]}":f"{x[2]}"}
            character = string.ascii_letters
            paswd = ''.join(choice(character) for x in range(randint(4, 6)))
            py = f'\n{paswd} = {dict}'
            with open('pwkayit.txt','a+',encoding='UTF-8') as file :
                file.write(py)
            self.pw.textBrowser_2.setText('Şifreleme dosyaya eklendi.')
        except Exception:
            pass

    def openfile(self):
        try :
            url = QtWidgets.QFileDialog.getOpenFileName()
            self.pw.lineEdit_2.setText(url[0])
        except Exception :
            pass

    def cogulpwsec(self):
        sifrelemeTuru = self.pw.comboBox_4.currentText()
        if sifrelemeTuru == 'Md5':
            self.pw.comboBox_5.setEnabled(False)
        elif sifrelemeTuru == 'Sha224':
            self.pw.comboBox_5.setEnabled(False)
        elif sifrelemeTuru == 'Sha256':
            self.pw.comboBox_5.setEnabled(False)
        elif sifrelemeTuru == 'Sha384':
            self.pw.comboBox_5.setEnabled(False)            
        elif sifrelemeTuru == 'Sha512':
            self.pw.comboBox_5.setEnabled(False)
        elif sifrelemeTuru == 'Sha3_224':
            self.pw.comboBox_5.setEnabled(False)
        elif sifrelemeTuru == 'Sha3_256':
            self.pw.comboBox_5.setEnabled(False)
        elif sifrelemeTuru == 'Sha3_384':
            self.pw.comboBox_5.setEnabled(False)
        elif sifrelemeTuru == 'Sha3_512':
            self.pw.comboBox_5.setEnabled(False)
        elif sifrelemeTuru == 'Blake2b':
            self.pw.comboBox_5.setEnabled(True)
        elif sifrelemeTuru == 'Blake2s':
            self.pw.comboBox_5.setEnabled(True)
        elif sifrelemeTuru == 'Shake_128':
            self.pw.comboBox_5.setEnabled(True)
        elif sifrelemeTuru == 'Shake_256':
            self.pw.comboBox_5.setEnabled(True)
           
    def cogpw(self):
        try :
            pw = self.pw.lineEdit_2.text()
            sifrelemeTuru = self.pw.comboBox_4.currentText()
            byteayar = self.pw.comboBox_5.currentText()
            ayirma = byteayar.split(' ')
            print('çalıştı')
            with open(f'{pw}','r',encoding='UTF-8') as file :
                cc = file.readlines()
            for i in cc :
                n = i.strip('\n')
                print('çalıştı1')
                if sifrelemeTuru == 'Md5':
                    pwmd = hashlib.md5(n.encode('UTF-8')).hexdigest()
                    self.pw.textBrowser_5.setText(f'Yazılan : {n}\nMd5 ile Çevrilmiş Hali : {pwmd}\n')
                    a = self.pw.textBrowser_3.toPlainText()
                    a += f'Yazılan : {n}\nMd5 ile Çevrilmiş Hali : {pwmd}\n'
                    self.pw.textBrowser_3.setText(a)
                    self.kytcog()
                elif sifrelemeTuru == 'Sha224':
                    pwmd = hashlib.sha224(n.encode('UTF-8')).hexdigest()
                    self.pw.textBrowser_5.setText(f'Yazılan : {n}\nSha224 ile Çevrilmiş Hali : {pwmd}\n')
                    a = self.pw.textBrowser_3.toPlainText()
                    a += f'Yazılan  : {n}\nSha224 ile Çevrilmiş Hali : {pwmd}\n'
                    self.pw.textBrowser_3.setText(a)
                    self.kytcog()
                elif sifrelemeTuru == 'Sha256':
                    pwmd = hashlib.sha256(n.encode('UTF-8')).hexdigest()
                    self.pw.textBrowser_5.setText(f'Yazılan : {n}\nSha256 ile Çevrilmiş Hali : {pwmd}\n')
                    a = self.pw.textBrowser_3.toPlainText()
                    a += f'Yazılan  : {n}\nSha256 ile Çevrilmiş Hali : {pwmd}\n'
                    self.pw.textBrowser_3.setText(a)
                    self.kytcog()
                elif sifrelemeTuru == 'Sha384':
                    pwmd = hashlib.sha384(n.encode('UTF-8')).hexdigest()
                    self.pw.textBrowser_5.setText(f'Yazılan : {n}\nSha384 ile Çevrilmiş Hali : {pwmd}\n')
                    a = self.pw.textBrowser_3.toPlainText()
                    a += f'Yazılan  : {n}\nSha384 ile Çevrilmiş Hali : {pwmd}\n'
                    self.pw.textBrowser_3.setText(a)
                    self.kytcog()
                elif sifrelemeTuru == 'Sha512':
                    pwmd = hashlib.sha512(n.encode('UTF-8')).hexdigest()
                    self.pw.textBrowser_5.setText(f'Yazılan : {n}\nSha512 ile Çevrilmiş Hali : {pwmd}\n')
                    a = self.pw.textBrowser_3.toPlainText()
                    a += f'Yazılan  : {n}\nSha512 ile Çevrilmiş Hali : {pwmd}\n'
                    self.pw.textBrowser_3.setText(a)
                    self.kytcog()
                elif sifrelemeTuru == 'Sha3_224':
                    pwmd = hashlib.sha3_224(n.encode('UTF-8')).hexdigest()
                    self.pw.textBrowser_5.setText(f'Yazılan : {n}\nSha3_224 ile Çevrilmiş Hali : {pwmd}\n')
                    a = self.pw.textBrowser_3.toPlainText()
                    a += f'Yazılan  : {n}\nSha3_224 ile Çevrilmiş Hali : {pwmd}\n'
                    self.pw.textBrowser_3.setText(a)
                    self.kytcog()
                elif sifrelemeTuru == 'Sha3_256':
                    pwmd = hashlib.sha3_256(n.encode('UTF-8')).hexdigest()
                    self.pw.textBrowser_5.setText(f'Yazılan : {n}\nSha3_256 ile Çevrilmiş Hali : {pwmd}\n')
                    a = self.pw.textBrowser_3.toPlainText()
                    a += f'Yazılan  : {n}\nSha3_256 ile Çevrilmiş Hali : {pwmd}\n'
                    self.pw.textBrowser_3.setText(a)
                    self.kytcog()
                elif sifrelemeTuru == 'Sha3_512':
                    pwmd = hashlib.sha3_512(n.encode('UTF-8')).hexdigest()
                    self.pw.textBrowser_5.setText(f'Yazılan : {n}\nSha3_512 ile Çevrilmiş Hali : {pwmd}\n')
                    a = self.pw.textBrowser_3.toPlainText()
                    a += f'Yazılan  : {n}\nSha3_512 ile Çevrilmiş Hali : {pwmd}\n'
                    self.pw.textBrowser_3.setText(a)
                    self.kytcog()
                elif sifrelemeTuru == 'Blake2b':
                    pwmd = hashlib.blake2b(n.encode('UTF-8'),digest_size=int(ayirma[0])).hexdigest()
                    self.pw.textBrowser_5.setText(f'Yazılan : {n}\nBlake2b ile Çevrilmiş Hali : {pwmd}\n')
                    a = self.pw.textBrowser_3.toPlainText()
                    a += f'Yazılan  : {n}\nBlake2b ile Çevrilmiş Hali : {pwmd}\n'
                    self.pw.textBrowser_3.setText(a)
                    self.kytcog()
                elif sifrelemeTuru == 'Blake2s':
                    pwmd = hashlib.blake2s(n.encode('UTF-8'),digest_size=int(ayirma[0])).hexdigest()
                    self.pw.textBrowser_5.setText(f'Yazılan : {n}\nBlake2s ile Çevrilmiş Hali : {pwmd}\n')
                    a = self.pw.textBrowser_3.toPlainText()
                    a += f'Yazılan  : {n}\nBlake2s ile Çevrilmiş Hali : {pwmd}\n'
                    self.pw.textBrowser_3.setText(a)
                    self.kytcog()
                elif sifrelemeTuru == 'Shake_128':
                    pwmd = hashlib.shake_128(n.encode('UTF-8')).hexdigest(int(ayirma[0]))
                    self.pw.textBrowser_5.setText(f'Yazılan : {n}\nShake_128 ile Çevrilmiş Hali : {pwmd}\n')
                    a = self.pw.textBrowser_3.toPlainText()
                    a += f'Yazılan  : {n}\nShake_128 ile Çevrilmiş Hali : {pwmd}\n'
                    self.pw.textBrowser_3.setText(a)
                    self.kytcog()
                elif sifrelemeTuru == 'Shake_256':
                    pwmd = hashlib.shake_256(n.encode('UTF-8')).hexdigest(int(ayirma[0]))
                    self.pw.textBrowser_5.setText(f'Yazılan : {n}\nSnake_256 ile Çevrilmiş Hali : {pwmd}\n')
                    a = self.pw.textBrowser_3.toPlainText()
                    a += f'Yazılan  : {pw}\nShake_256 ile Çevrilmiş Hali : {pwmd}'
                    self.pw.textBrowser_3.setText(a)
                    self.kytcog()
                self.pw.textBrowser_4.setText('Çoğul Dönüştürmelerde Tüm Şifrelemeler Otomatik kaydolur.')
        except Exception :
            pass

    def kytcog(self):
        vv = self.pw.textBrowser_5.toPlainText()
        x = vv.split(":")
        print(x)
        x2 = x[1].split('\n')
        print(x2)
        x3 = x2[1].split(' ')
        x4 = x[2].split('\n')
        print(x2)
        print(x3)
        dict = {"Metin": f"{x2[0]}",f"{x3[0]}":f"{x4[0]}"}
        character = string.ascii_letters
        paswd = ''.join(choice(character) for x in range(randint(4, 6)))
        py = f'{paswd} = {dict}\n'
        with open('pwkayit.txt','a+',encoding='UTF-8') as file :
            file.write(f"{py}")

    def kayitget(self):
        os.startfile('pwkayit.txt')

    def kayitsil(self):
        os.remove('pwkayit.txt')
        with open('pwkayit.txt','a+'):
            pass            

    def ex(self):
        app.exit()

    def facebook(self):
        os.startfile("https://www.facebook.com/maresalprogramming")

    def instagram(self):
        os.startfile("https://www.instagram.com/maresalp/")

    def github(self):
        os.startfile("https://github.com/IMaresaLI")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    main = pwmp()
    app.setStyle('Fusion')
    app.exit(app.exec_())
