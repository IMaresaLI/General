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

from PyQt5 import QtWidgets,QtCore,QtGui
import os,sys,paramiko,time
from ssh import Ui_MainWindow


class GApp(QtWidgets.QMainWindow):
    def __init__(self):
        super(GApp,self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setStyleSheet(open("style.css","r").read())
        self.ui.pushButton.clicked.connect(self.startSSH)
        self.ui.lineEdit_2.returnPressed.connect(self.onPressed)

    def startSSH(self):
        global list
        list = []
        Ip = self.ui.lineEdit.text()
        user,ok = QtWidgets.QInputDialog.getText(self,"Server Bağlantı","Server Username")
        if user and ok :
            paswd,ok = QtWidgets.QInputDialog.getText(self,"Server Bağlantı","Server Password",QtWidgets.QLineEdit.Password)
            if paswd and ok :
                list.append(Ip)
                list.append(user)
                list.append(paswd)
                self.evt_btn_clicked()



    def evt_btn_clicked(self):
        self.worker = WorkerThread()
        self.worker.start()
        self.worker.finished.connect(self.evt_worker_finished)

    def evt_worker_finished(self):
        if Error == "CE":
            QtWidgets.QMessageBox.information(self,"Connect",f"Giriş Başarılı.")
            self.ui.stackedWidget.setCurrentIndex(1)
            self.ui.textBrowser.setText(f"""*-* Maresal Programming *-* || IP {list[0]} ONLİNE""")
        else :
            QtWidgets.QMessageBox.warning(self,"Hata","Giriş Hatası")

    def setCommand(self,command):
        stdin, stdout, stderr = ssh.exec_command(command)
        for i in stdout.read().decode('ascii').split('\n') :
            text = self.ui.textBrowser.toPlainText()
            text+=str(i)+"\n"
            self.ui.textBrowser.setText(text)


    def onPressed(self):
        command = self.ui.lineEdit_2.text()
        if command == "clear":
            self.ui.textBrowser.clear()
        elif command == "--yardım":
            self.help()
        else :
            self.setCommand(command)
        self.ui.lineEdit_2.clear()
        self.ui.textBrowser.moveCursor(QtGui.QTextCursor.End)



    def help(self):
            text = self.ui.textBrowser.toPlainText()
            text+="""
                pwd - Hangi Dosyada olduğunuzu bildirir.
                ls - Dizindeki tüm dosyaları getirir
                mkdir -  Dosya - Klasör oluşturma
                rmdir -  Dosya - Klasör Silme
                ping <url> - Bağlantı öğrenme

                Yönetici 
                whoami - Kullanıcı Adı
                hostname - Host ismi
                ifconfig - Ağ bilgileri
                id[kullanıcı_ismi] - Grup Bilgisi
                cat /etc/passwd - Tüm kullanıcı bilgileri
                \n"""
            self.ui.textBrowser.setText(text)



class WorkerThread(QtCore.QThread):
    def run(self):
        try :
            global ssh,Error
            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh.connect(hostname=list[0],username=list[1],password=list[2])
            Error = "CE"
        except Exception as err:
            Error = err




if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle("Fusion")
    main = GApp()
    main.show()
    app.exit(app.exec_())