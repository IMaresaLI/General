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
import os,sys
from dcBotDesign import Ui_MainWindow
from createBotPage import createBotPage

class dcApp(QtWidgets.QMainWindow):
    def __init__(self):
        super(dcApp,self).__init__()
        self.dc = Ui_MainWindow()
        self.dc.setupUi(self)
        self.CheckBoxLoads()

        self.botPage = createBotPage()
        self.dc.createBtn.clicked.connect(self.botCreatePage)


    def CheckBoxLoads(self):
        self.dc.loginChk.stateChanged.connect(self.SelectedCb)
        self.dc.closeChk.stateChanged.connect(self.SelectedCb)
        self.dc.clearChk.stateChanged.connect(self.SelectedCb)
        self.dc.clonChk.stateChanged.connect(self.SelectedCb)
        self.dc.kickChk.stateChanged.connect(self.SelectedCb)
        self.dc.banChk.stateChanged.connect(self.SelectedCb)
        self.dc.unbanChk.stateChanged.connect(self.SelectedCb)

    def SelectedCb(self):
        global list
        list = []
        self.sender()
        items = self.dc.grbxBot.findChildren(QtWidgets.QCheckBox)
        for item in items:
            if item.isChecked():
                list.append(item.text())

    def botCreatePage(self):
        try : 
            if len(list) >= 1:
                self.botPage.show()
                self.botPage.openSelected(list)
        except Exception as err:
            print(err)
        



if __name__== "__main__":
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle("Fusion")
    main = dcApp()
    main.show()
    app.exit(app.exec_())