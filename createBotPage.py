from createBot import Ui_Form
from PyQt5 import QtWidgets,QtCore
from botCodes import *

class createBotPage(QtWidgets.QDialog):
    def __init__(self):
        super(createBotPage,self).__init__()
        self.cb = Ui_Form()
        self.cb.setupUi(self)
        self.hiddenElements()
        self.chkChanged()

        self.cb.botCreateBtn.clicked.connect(self.botCreated)
        

    def chkChanged(self):
        self.cb.clearRolChk.stateChanged.connect(self.checkedRol)
        self.cb.cloneRolChk.stateChanged.connect(self.checkedRol)
        self.cb.kickRolChk.stateChanged.connect(self.checkedRol)
        self.cb.banRolChk.stateChanged.connect(self.checkedRol)
        self.cb.unbanRolChk.stateChanged.connect(self.checkedRol)

    def openSelected(self,liste):
        global selecteds
        selecteds = []
        self.hiddenElements()
        for i in liste:
            if i == "Kullanıcı Giriş":
                self.cb.jointbx.setHidden(False)
                self.cb.lineEdit.setHidden(False)
            if i == "Kullanıcı Çıkış":
                self.cb.closeTbx.setHidden(False)
                self.cb.lineEdit_2.setHidden(False)
            if i == "Mesaj Temizleme":
                self.cb.amountTbx.setHidden(False)
                self.cb.clearRolChk.setHidden(False)
                self.cb.clearTbx.setHidden(False)
            if i == "Kanal Klonlama":
                self.cb.cloneTbx.setHidden(False)
                self.cb.cloneRolChk.setHidden(False)
            if i == "Kullanıcı Atma":
                self.cb.kickRolChk.setHidden(False)
                self.cb.kickTbx.setHidden(False)
            if i == "Kullanıcı Banlama":
                self.cb.banRolChk.setHidden(False)
                self.cb.banTbx.setHidden(False)
            if i == "Kullanıcı Banı Açma":
                self.cb.unbanTbx.setHidden(False)
                self.cb.unbanRolChk.setHidden(False)
            selecteds.append(i)
        self.cb.botCreateBtn.setHidden(False)

    def hiddenElements(self):
        self.cb.jointbx.setHidden(True)
        self.cb.lineEdit.setHidden(True)
        self.cb.closeTbx.setHidden(True)
        self.cb.lineEdit_2.setHidden(True)

        self.cb.banRolChk.setHidden(True)
        self.cb.banTbx.setHidden(True)
        self.cb.rol4Tbx.setHidden(True)

        self.cb.amountTbx.setHidden(True)
        self.cb.clearRolChk.setHidden(True)
        self.cb.clearTbx.setHidden(True)
        self.cb.rolTbx.setHidden(True)

        self.cb.cloneTbx.setHidden(True)
        self.cb.cloneRolChk.setHidden(True)
        self.cb.rol2Tbx.setHidden(True)

        self.cb.kickRolChk.setHidden(True)
        self.cb.kickTbx.setHidden(True)
        self.cb.rol3Tbx.setHidden(True)

        self.cb.unbanTbx.setHidden(True)
        self.cb.unbanRolChk.setHidden(True)
        self.cb.rol5Tbx.setHidden(True)

        self.cb.botCreateBtn.setHidden(True)

    def checkedRol(self):
        self.sender()
        if self.cb.clearRolChk.isChecked():
            self.cb.rolTbx.setHidden(False)
        else :
            self.cb.rolTbx.setHidden(True)
        if self.cb.cloneRolChk.isChecked():
            self.cb.rol2Tbx.setHidden(False)
        else :
            self.cb.rol2Tbx.setHidden(True)
        if self.cb.kickRolChk.isChecked():
            self.cb.rol3Tbx.setHidden(False)
        else :
            self.cb.rol3Tbx.setHidden(True)
        if self.cb.banRolChk.isChecked():
            self.cb.rol4Tbx.setHidden(False)
        else :
            self.cb.rol4Tbx.setHidden(True)
        if self.cb.unbanRolChk.isChecked():
            self.cb.rol5Tbx.setHidden(False)
        else :
            self.cb.rol5Tbx.setHidden(True)

    def botCreated(self):
        list = []
        for i in selecteds:
            if i == "Kullanıcı Giriş":
                list.append(joinCode(self.cb.lineEdit.text(),self.cb.jointbx.text()))
            if i == "Kullanıcı Çıkış":
                list.append(remove(self.cb.lineEdit_2.text(),self.cb.closeTbx.text()))
            if i == "Mesaj Temizleme":
                if self.cb.clearRolChk.isChecked():
                    list.append(clear(self.cb.amountTbx.text(),self.cb.rolTbx.text()))
                else :
                    list.append(clear(self.cb.amountTbx.text()))
            if i == "Kanal Klonlama":
                if self.cb.cloneRolChk.isChecked():
                    list.append(clones(self.cb.cloneTbx.text(),self.cb.rol2Tbx.text()))
                else :
                    list.append(clones(self.cb.cloneTbx.text()))
            if i == "Kullanıcı Atma":
                if self.cb.kickRolChk.isChecked():
                    list.append(kick(self.cb.kickTbx.text(),self.cb.rol3Tbx.text()))
                else :
                    list.append(kick(self.cb.kickTbx.text()))
            if i == "Kullanıcı Banlama":
                if self.cb.banRolChk.isChecked():
                    list.append(ban(self.cb.banTbx.text(),self.cb.rol4Tbx.text()))
                else :
                    list.append(ban(self.cb.banTbx.text()))
            if i == "Kullanıcı Banı Açma":
                if self.cb.unbanRolChk.isChecked():
                    list.append(ban(self.cb.unbanTbx.text(),self.cb.rol5Tbx.text()))
                else :
                    list.append(ban(self.cb.unbanTbx.text()))
        Prefix,ok = QtWidgets.QInputDialog.getText(self,"Prefix Belirleme","Prefix :")
        if Prefix and ok:
            Token,ok = QtWidgets.QInputDialog.getText(self,"Token","Bot Token :")
            if Token and ok :
                liste = [botMainCode(Prefix),token(Token)]
                with open("bot.py","w+",encoding="UTF-8") as file:
                    file.write(liste[0])
                    for j in list:
                        file.write(j)
                    file.write(liste[1])
                QtWidgets.QMessageBox.information(self,"Onay","Discord bot dosyanız oluşturulmuştur.") 
                self.clear()
                self.close()              
        
    def clear(self):
        self.cb.jointbx.clear()
        self.cb.lineEdit.clear()
        self.cb.closeTbx.clear()
        self.cb.lineEdit_2.clear()

        self.cb.banTbx.clear()
        self.cb.rol4Tbx.clear()

        self.cb.rolTbx.clear()

        self.cb.cloneTbx.clear()
        self.cb.rol2Tbx.clear()
        self.cb.kickTbx.clear()
        self.cb.rol3Tbx.clear()

        self.cb.unbanTbx.clear()
        self.cb.rol5Tbx.clear()



        
        
        
        
        