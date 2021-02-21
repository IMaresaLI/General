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
import os,sys,sqlite3
from pwRvDesigner import Ui_MainWindow
from pwManager import Ui_Form
import databaseConnect


class pwApp(QtWidgets.QMainWindow):
    def __init__(self):
        super(pwApp,self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.IdControl()
        self.getPasswords()
        self.ui.AddBtn.clicked.connect(self.Added)
        self.ui.DeleteBtn.clicked.connect(self.Deleted)
        self.ui.listView.doubleClicked.connect(self.Updated)

        zamanlayıcı = QtCore.QTimer(self)
        zamanlayıcı.timeout.connect(self.getPasswords)
        zamanlayıcı.start(1000)

        

    def IdControl(self):
        UserPw = databaseConnect.getPasswdUser(1)
        print(UserPw)
        if UserPw == None:
            text , ok = QtWidgets.QInputDialog.getText(self,"Giriş Onay","Giriş Şifresi Belirleyiniz :")
            if text and ok :
                databaseConnect.Add("Program","Admin",text)
                return self.IdControl()
            else :
                QtWidgets.QMessageBox.warning(self,"Hata","Parola Oluşturulmadı.")
                quit()
        else :
            text,ok = QtWidgets.QInputDialog.getText(self,"Giriş Onay","Admin Parolası")
            if text and ok :
                if UserPw[3] == text :
                    print("Kabul Edildi")
                else :
                    QtWidgets.QMessageBox.warning(self,"Hata","Parola Yanlış")
                    return self.IdControl()
            else :
                quit()

    def getPasswords(self):
        try:
            data = databaseConnect.getDatabase()

            model = QtGui.QStandardItemModel()
            self.ui.listView.setModel(model)

            for i in data:
                dataModel = f"{i[0]}-{i[1]}\nUsername : {i[2]}\nPassword : {i[3]}"
                item = QtGui.QStandardItem(dataModel)
                model.appendRow(item)
        except :
            pass
        
    def Added(self):
        self.pwM = pwMng()
        self.pwM.show()

    def Deleted(self):
        try:
            data = self.ui.listView.currentIndex().data()
            idNo = data.split("-")[0]
            result = QtWidgets.QMessageBox.question(self,"Silme Onay","Silme işlemini onaylıyor musunuz?",QtWidgets.QMessageBox.Ok | QtWidgets.QMessageBox.Cancel)
            if result == 1024:
                print("Çalıştı")
                databaseConnect.Delete(int(idNo))
                self.getPasswords()
        except :
            pass
            
    def Updated(self):
        global list
        list = []
        data = self.ui.listView.currentIndex().data()
        idNo = data.split("-")[0]
        list.append(idNo)
        self.pwM = pwMng()
        self.pwM.show()
        self.pwM.Update()


class pwMng(QtWidgets.QWidget):
    def __init__(self):
        super(pwMng,self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.pushButton.setHidden(False)
        self.ui.pushButton.clicked.connect(self.AddPassword)
        self.ui.pushButton_2.clicked.connect(self.UpdatePassword)

    def AddPassword(self):
        bilgi = self.ui.lineEdit.text()
        userN = self.ui.lineEdit_2.text()
        pw = self.ui.lineEdit_3.text()
        databaseConnect.Add(bilgi,userN,pw)
        self.close()

    def Update(self):
        data = databaseConnect.getPasswdUser(list[0])
        self.ui.lineEdit.setText(data[1])
        self.ui.lineEdit_2.setText(data[2])
        self.ui.lineEdit_3.setText(data[3])
        self.ui.pushButton_2.setHidden(False)
        self.ui.pushButton.setHidden(True)

    def UpdatePassword(self):
        data = databaseConnect.getPasswdUser(list[0])
        bilgi = self.ui.lineEdit.text()
        userName = self.ui.lineEdit_2.text()
        pw = self.ui.lineEdit_3.text()
        databaseConnect.Update(bilgi,userName,pw,data[0])
        self.close()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    main = pwApp()
    main.show()
    app.setStyle("Fusion")
    app.exit(app.exec_())