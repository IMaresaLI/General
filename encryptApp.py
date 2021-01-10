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
from encode import Ui_MainWindow
import os 
import sys
import base64
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.fernet import Fernet,InvalidToken
from random import choice,randint
import string


class encryptApps(QtWidgets.QMainWindow):
    def __init__(self):
        super(encryptApps,self).__init__()
        self.enc = Ui_MainWindow()
        self.enc.setupUi(self)
        self.show()

        self.enc.actionmetinSifreleme.triggered.connect(self.textCActive)
        self.enc.actiondMetinCozumleme.triggered.connect(self.textDActive)
        self.enc.actionfileEncrypt.triggered.connect(self.fileCActive)
        self.enc.actionfileDecrypt.triggered.connect(self.fileDActive)

        
        self.enc.MetinKeyOnayBtn.clicked.connect(self.KeyCreate)
        self.enc.DosyaKeyOnayBtn.clicked.connect(self.KeyCreate)
        self.enc.sifreleBtn.clicked.connect(self.textEncrypt)
        self.enc.metinCozBtn.clicked.connect(self.textDecrypt)
        self.enc.SifreleToolBtn.clicked.connect(self.filePath)
        self.enc.SifreleToolBar_2.clicked.connect(self.filePath)
        self.enc.DosyaSifreleBtn.clicked.connect(self.fileEncrypt)
        self.enc.DosyaCozBtn.clicked.connect(self.fileDecrypt)

    
    def textCActive(self):
        if self.enc.MetinKeyOnayBtn.isHidden() == True:
            self.enc.MetinKeyOnayBtn.setHidden(False)
            self.enc.keyCbx.setHidden(False)
            self.enc.metinSifreCozme.setHidden(True)
            self.enc.dosyaCozmeBox.setHidden(True)
            self.enc.dosyaSifreleBox.setHidden(True)
            self.enc.DosyaKeyOnayBtn.setHidden(True)
            self.enc.MetinKeyOnayBtn.setEnabled(True)
            self.enc.DosyaKeyOnayBtn.setEnabled(True)
            self.enc.keyCbx.setEnabled(True)
            self.AllClear()
        else :
            self.enc.MetinKeyOnayBtn.setHidden(True)
            self.enc.keyCbx.setHidden(True)
            self.enc.metinSifreCozme.setHidden(True)
            self.enc.dosyaCozmeBox.setHidden(True)
            self.enc.dosyaSifreleBox.setHidden(True)
            self.enc.DosyaKeyOnayBtn.setHidden(True)
            self.enc.metinSifreleBox.setHidden(True)
            self.enc.MetinKeyOnayBtn.setEnabled(True)
            self.enc.keyCbx.setEnabled(True)
            self.AllClear()

    def KeyCreate(self):
        global otoKey
        global paswd1
        character = string.ascii_letters
        paswd1 = ''.join(choice(character) for x in range(randint(4, 6)))         
        CbxSelected = self.enc.keyCbx.currentText()
        list = ["MD5","SHA224","SHA256","SHA384","SHA512"]
        if CbxSelected == "Otomatik Anahtar Oluşturma":
            otoKey = Fernet.generate_key()
            with open(f"{paswd1}.key","wb") as file :
                file.write(otoKey)
            if self.enc.MetinKeyOnayBtn.isHidden() == False :
                self.enc.metinSifreleBox.setHidden(False)
                self.enc.keyCbx.setEnabled(False)
                self.enc.MetinKeyOnayBtn.setEnabled(False)
            if self.enc.DosyaKeyOnayBtn.isHidden() == False :
                self.enc.dosyaSifreleBox.setHidden(False)
                self.enc.keyCbx.setEnabled(False)
                self.enc.DosyaKeyOnayBtn.setEnabled(False)
            QtWidgets.QMessageBox.information(self,"Key Oluşturma",f"Anahtarınız Otomatik olarak oluşturuldu.<br>Anahtar Dosya Konumunuz :<br> {os.path.realpath(f'{paswd1}.key')}")
        elif CbxSelected == "Manuel Anahtar Oluşturma":
            paswd,Ok = QtWidgets.QInputDialog.getText(self,"Key Oluşturma", "Lütfen Şifre Giriniz : ")
            if paswd and Ok:
                algo,Ok = QtWidgets.QInputDialog.getItem(self,"Key Algoritması", "Key Algoritmaları : ",list)
                if algo and Ok:
                    result = QtWidgets.QMessageBox.information(self,"Key Oluşturma",f"Oluşturulacak key bilgilerini onaylıyor musunuz?<br>Belirlenen Key Şifresi : {paswd} <br>Key Algoritması : {algo}",QtWidgets.QMessageBox.Ok | QtWidgets.QMessageBox.Cancel)
                    if result == QtWidgets.QMessageBox.Ok:
                        with open(f"{paswd1}.key","wb") as file:
                                file.write(self.manuelKey(algo=algo,metin=paswd))
                        QtWidgets.QMessageBox.information(self,"Key Oluşturma",f"Anahtarınız oluşturuldu.<br>Anahtar Dosya Konumunuz :<br> {os.path.realpath(f'{paswd1}.key')}")
                        if self.enc.MetinKeyOnayBtn.isHidden() == False :
                            self.enc.metinSifreleBox.setHidden(False)
                            self.enc.keyCbx.setEnabled(False)
                            self.enc.MetinKeyOnayBtn.setEnabled(False)
                        if self.enc.DosyaKeyOnayBtn.isHidden() == False :
                            self.enc.dosyaSifreleBox.setHidden(False)
                            self.enc.keyCbx.setEnabled(False)
                            self.enc.DosyaKeyOnayBtn.setEnabled(False)
        
    def manuelKey(self,algo,metin):
        if algo == "MD5":
            password = metin.encode()
            salt = b'salt_'
            kdf = PBKDF2HMAC(
                algorithm=hashes.MD5(),
                length=32,
                salt=salt,
                iterations=100000,
                backend=default_backend()
                )
            key = base64.urlsafe_b64encode(kdf.derive(password))
            return key
        elif algo == "SHA224":
            password = metin.encode()
            salt = b'salt_'
            kdf = PBKDF2HMAC(
                algorithm=hashes.SHA224(),
                length=32,
                salt=salt,
                iterations=100000,
                backend=default_backend()
                )
            key = base64.urlsafe_b64encode(kdf.derive(password))
            return key
        elif algo == "SHA256":
            password = metin.encode()
            salt = b'salt_'
            kdf = PBKDF2HMAC(
                algorithm=hashes.MD5(),
                length=32,
                salt=salt,
                iterations=100000,
                backend=default_backend()
                )
            key = base64.urlsafe_b64encode(kdf.derive(password))
            return key
        elif algo == "SHA384":
            password = metin.encode()
            salt = b'salt_'
            kdf = PBKDF2HMAC(
                algorithm=hashes.MD5(),
                length=32,
                salt=salt,
                iterations=100000,
                backend=default_backend()
                )
            key = base64.urlsafe_b64encode(kdf.derive(password))
            return key
        elif algo == "SHA512":
            password = metin.encode()
            salt = b'salt_'
            kdf = PBKDF2HMAC(
                algorithm=hashes.MD5(),
                length=32,
                salt=salt,
                iterations=100000,
                backend=default_backend()
                )
            key = base64.urlsafe_b64encode(kdf.derive(password))
            return key

    def textEncrypt(self):
        CbxSelected = self.enc.keyCbx.currentText()
        text = self.enc.metinSifrelemeTxt.toPlainText()
        if CbxSelected == "Otomatik Anahtar Oluşturma":
            message = text.encode()
            f = Fernet(otoKey)
            encrypted = f.encrypt(message)
            self.enc.sifreliMetin.setText(str(encrypted).split("'")[1]) 
            oKey = str(otoKey).split("'")[1]
            QtWidgets.QMessageBox.information(self,"Metin Şifreleme",f"Metniniz başarıyla şifrelenmiştir.<br>Anahtarınız : {oKey}")
            self.enc.MetinKeyOnayBtn.setEnabled(True)
            self.enc.keyCbx.setEnabled(True)

        elif CbxSelected == "Manuel Anahtar Oluşturma":
            message = text.encode()
            with open(paswd1+".key","rb") as file :
                manuelKey = file.read()
            f = Fernet(manuelKey)
            encrypted = f.encrypt(message)
            print(encrypted)
            mKey = str(manuelKey).split("'")[1]
            self.enc.sifreliMetin.setText(str(encrypted).split("'")[1])
            QtWidgets.QMessageBox.information(self,"Metin Şifreleme",f"Metniniz başarıyla şifrelenmiştir.<br>Anahtarınız : {mKey}")
            self.enc.MetinKeyOnayBtn.setEnabled(True)
            self.enc.keyCbx.setEnabled(True)

    def textDActive(self):
        if self.enc.metinSifreCozme.isHidden() == True:
            self.enc.MetinKeyOnayBtn.setHidden(True)
            self.enc.keyCbx.setHidden(True)
            self.enc.metinSifreleBox.setHidden(True)
            self.enc.metinSifreCozme.setHidden(False)
            self.enc.dosyaCozmeBox.setHidden(True)
            self.enc.dosyaSifreleBox.setHidden(True)
            self.enc.DosyaKeyOnayBtn.setHidden(True)
            self.enc.MetinKeyOnayBtn.setEnabled(True)
            self.enc.DosyaKeyOnayBtn.setEnabled(True)
            self.enc.keyCbx.setEnabled(True)
            self.AllClear()
        else :
            self.enc.DosyaKeyOnayBtn.setHidden(True)
            self.enc.MetinKeyOnayBtn.setHidden(True)
            self.enc.keyCbx.setHidden(True)
            self.enc.metinSifreCozme.setHidden(True)
            self.enc.dosyaCozmeBox.setHidden(True)
            self.enc.dosyaSifreleBox.setHidden(True)
            self.enc.DosyaKeyOnayBtn.setHidden(True)
            self.enc.metinSifreleBox.setHidden(True)
            self.enc.MetinKeyOnayBtn.setEnabled(True)
            self.enc.DosyaKeyOnayBtn.setEnabled(True)
            self.enc.keyCbx.setEnabled(True)
            self.AllClear()

    def textDecrypt(self):
        text = self.enc.metinCozmeTxt.toPlainText()
        try :
            paswd,Ok = QtWidgets.QInputDialog.getText(self,"Anahtar", "Lütfen Anahtarınızı Giriniz : ")
            if paswd and Ok:
                message = text.encode()
                f = Fernet(paswd)
                decrypted = f.decrypt(message) 
                self.enc.cozulmusMetin.setText(str(decrypted).split("'")[1])
        except InvalidToken as e:
            print(e)
            QtWidgets.QMessageBox.warning(self,"Anahtar Hatası",f"Girdiğiniz anahtar yanlış lütfen tekrar deneyiniz.")

    def fileCActive(self):
        if self.enc.DosyaKeyOnayBtn.isHidden() == True:
            self.enc.MetinKeyOnayBtn.setHidden(True)
            self.enc.keyCbx.setHidden(False)
            self.enc.metinSifreCozme.setHidden(True)
            self.enc.dosyaCozmeBox.setHidden(True)
            self.enc.dosyaSifreleBox.setHidden(True)
            self.enc.DosyaKeyOnayBtn.setHidden(False)
            self.enc.MetinKeyOnayBtn.setEnabled(True)
            self.enc.DosyaKeyOnayBtn.setEnabled(True)
            self.enc.keyCbx.setEnabled(True)
            self.AllClear()

        else :
            self.enc.DosyaKeyOnayBtn.setHidden(True)
            self.enc.MetinKeyOnayBtn.setHidden(True)
            self.enc.keyCbx.setHidden(True)
            self.enc.metinSifreCozme.setHidden(True)
            self.enc.dosyaCozmeBox.setHidden(True)
            self.enc.dosyaSifreleBox.setHidden(True)
            self.enc.DosyaKeyOnayBtn.setHidden(True)
            self.enc.metinSifreleBox.setHidden(True)
            self.enc.MetinKeyOnayBtn.setEnabled(True)
            self.enc.DosyaKeyOnayBtn.setEnabled(True)
            self.enc.keyCbx.setEnabled(True)
            self.AllClear()

    def filePath(self):
        try: 
            url = QtWidgets.QFileDialog.getOpenFileName()
            if self.enc.dosyaSifreleBox.isHidden() == False:
                self.enc.txtUrlsifrele.setText(url[0])
            else :
                self.enc.txtUrlsifrele_2.setText(url[0])
        except Exception :
            pass

    def fileEncrypt(self):
        CbxSelected = self.enc.keyCbx.currentText()
        path = self.enc.txtUrlsifrele.text()
        if CbxSelected == "Otomatik Anahtar Oluşturma":
            input_file = path
            fileName = input_file.split("/")[-1].split(".")[0] 
            output_file = f'{fileName}.encrypted'

            with open(input_file,"rb") as f:
                data = f.read()
        
            fernet = Fernet(otoKey)
            encrypted = fernet.encrypt(data)

            with open(output_file,'wb') as f:
                f.write(encrypted)
            oKey = str(otoKey).split("'")[1] 
            self.enc.sifrelenmisHk.setText(f"Dosyanız {oKey} anahtarı ile şifrelenmiştir.\nŞifrelenmiş Dosya Konumunuz : \n{os.path.realpath(output_file)}") 
            QtWidgets.QMessageBox.information(self,"Dosya Şifreleme",f"Dosyanız başarıyla şifrelenmiştir.<br>Anahtarınız : {oKey}")
            self.enc.DosyaKeyOnayBtn.setEnabled(True)
            self.enc.keyCbx.setEnabled(True)

        elif CbxSelected == "Manuel Anahtar Oluşturma":
            input_file = path
            fileName = input_file.split("/")[-1].split(".")[0] 
            output_file = f'{fileName}.encrypted'

            with open(input_file,'rb') as f:
                data = f.read()

            with open(paswd1+".key","rb") as file :
                manuelKey = file.read()

            fernet = Fernet(manuelKey)
            encrypted = fernet.encrypt(data)

            with open(output_file,'wb') as f:
                f.write(encrypted)

            mKey = str(manuelKey).split("'")[1]
            self.enc.sifrelenmisHk.setText(f"Dosyanız {mKey} anahtarı ile şifrelenmiştir.\nŞifrelenmiş Dosya Konumunuz : \n{os.path.realpath(output_file)}") 
            QtWidgets.QMessageBox.information(self,"Dosya Şifreleme",f"Dosyanız başarıyla şifrelenmiştir.<br>Anahtarınız : {mKey}")
            self.enc.DosyaKeyOnayBtn.setEnabled(True)
            self.enc.keyCbx.setEnabled(True)
    
    def fileDActive(self):
        if self.enc.dosyaCozmeBox.isHidden() == True:
            self.enc.MetinKeyOnayBtn.setHidden(True)
            self.enc.keyCbx.setHidden(True)
            self.enc.metinSifreCozme.setHidden(True)
            self.enc.dosyaCozmeBox.setHidden(False)
            self.enc.dosyaSifreleBox.setHidden(True)
            self.enc.DosyaKeyOnayBtn.setHidden(True)
            self.enc.MetinKeyOnayBtn.setEnabled(True)
            self.enc.DosyaKeyOnayBtn.setEnabled(True)
            self.enc.keyCbx.setEnabled(True)
            self.AllClear()
        else :
            self.enc.DosyaKeyOnayBtn.setHidden(True)
            self.enc.MetinKeyOnayBtn.setHidden(True)
            self.enc.keyCbx.setHidden(True)
            self.enc.metinSifreCozme.setHidden(True)
            self.enc.dosyaCozmeBox.setHidden(True)
            self.enc.dosyaSifreleBox.setHidden(True)
            self.enc.DosyaKeyOnayBtn.setHidden(True)
            self.enc.metinSifreleBox.setHidden(True)
            self.enc.MetinKeyOnayBtn.setEnabled(True)
            self.enc.DosyaKeyOnayBtn.setEnabled(True)
            self.enc.keyCbx.setEnabled(True)
            self.AllClear()

    def fileDecrypt(self):
        path = self.enc.txtUrlsifrele_2.text()
        input_file = path
        fileName = input_file.split("/")[-1].split(".")[0] 
        output_file = f'{fileName}.txt'

        with open(input_file,'rb') as f:
            data = f.read()
        try : 
            paswd,Ok = QtWidgets.QInputDialog.getText(self,"Anahtar", "Lütfen Anahtarınızı Giriniz : ")
            if paswd and Ok:

                fernet = Fernet(paswd)
                decrypted = fernet.decrypt(data)
                with open(output_file,'wb') as f:
                    f.write(decrypted)

                self.enc.cozulmusMetin_4.setText(f"Dosyanız {paswd} anahtarı ile açılmıştır.\nAçılmış Dosya Konumunuz : \n{os.path.realpath(output_file)}") 
                QtWidgets.QMessageBox.information(self,"Dosya Açma",f"Dosyanız başarıyla açılmıştır.<br>Anahtarınız : {paswd}")
        except InvalidToken :
            QtWidgets.QMessageBox.warning(self,"Anahtar Hatası",f"Girdiğiniz anahtar yanlış lütfen tekrar deneyiniz.")

    def AllClear(self):
        self.enc.cozulmusMetin_4.clear()
        self.enc.metinCozmeTxt.clear()
        self.enc.metinSifrelemeTxt.clear()
        self.enc.sifreliMetin.clear()
        self.enc.txtUrlsifrele.clear()
        self.enc.txtUrlsifrele_2.clear()
        self.enc.sifrelenmisHk.clear()
        self.enc.cozulmusMetin.clear()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    main = encryptApps()
    app.setStyle("Fusion")
    app.exit(app.exec_())
