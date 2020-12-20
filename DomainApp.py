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
from domainkont import Ui_MainWindow as a
import whois



class domainKont(QtWidgets.QMainWindow):
    def __init__(self):
        super(domainKont,self).__init__()
        self.ui = a()
        self.ui.setupUi(self)
        self.setStyleSheet(open("style.css","r").read())
        self.show()
        self.ui.pushButton.clicked.connect(self.DomainKontrol)

    def DomainKontrol(self):
        try :
            self.ui.textBrowser.clear()
            self.ui.textBrowser_3.clear()
            self.ui.textBrowser_4.clear()
            Domain = whois.whois(self.ui.lineEdit.text()) 
            ServerName = Domain.whois_server
            Security = Domain.registrar
            CreateDate = Domain.creation_date
            ExpDate = Domain.expiration_date
            UpdateDate = Domain.updated_date
            Org = Domain.org
            State = Domain.state
            City = Domain.city
            Country = Domain.country

            NameServers = Domain.name_servers
            status = Domain.status

            if len(CreateDate) >= 2:

                self.ui.textBrowser.setText(
                f"Sunucu Adı : {ServerName}\n"
                f"Güvenlik : {Security}\n"
                f"Oluşturulma Tarihi : {CreateDate[0]}\n"
                f"Son Kullanma Tarihi : {ExpDate[0]}\n"
                f"Güncellenme Tarihi : {UpdateDate[0]}\n"
                f"Ülke : {Country}\n"
                f"Kaynak : {Org}\n"
                f"Şehir : {City}\n"
                f"Eyalet : {State}")
                for i in NameServers :
                    Text = self.ui.textBrowser_3.toPlainText()
                    self.ui.textBrowser_3.setText(Text+i+"\n")
                for i in status :
                    Text = self.ui.textBrowser_4.toPlainText()
                    self.ui.textBrowser_4.setText(Text+i+"\n")
                    
                     

        except Exception as err:
            if str("object of type 'datetime.datetime' has no len()") == str(err):
                self.ui.textBrowser.setText(
                f"Sunucu Adı : {ServerName}\n"
                f"Güvenlik : {Security}\n"
                f"Oluşturulma Tarihi : {CreateDate}\n"
                f"Son Kullanma Tarihi : {ExpDate}\n"
                f"Güncellenme Tarihi : {UpdateDate}\n"
                f"Ülke : {Country}\n"
                f"Kaynak : {Org}\n"
                f"Şehir : {City}\n"
                f"Eyalet : {State}")
                for i in NameServers :
                    Text = self.ui.textBrowser_3.toPlainText()
                    self.ui.textBrowser_3.setText(Text+i+"\n")
                for i in status :
                    Text = self.ui.textBrowser_4.toPlainText()
                    self.ui.textBrowser_4.setText(Text+i+"\n")


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = domainKont()
    app.setStyle("Fusion")
    sys.exit(app.exec_())
