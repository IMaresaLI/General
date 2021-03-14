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
import os,sys,requests,json
from currencyDesign import Ui_MainWindow as ui



class CurrentApplication(QtWidgets.QMainWindow):
    def __init__(self):
        super(CurrentApplication,self).__init__()
        self.ui = ui()
        self.ui.setupUi(self)
        self.start()
        self.ui.tryCbx.currentIndexChanged.connect(self.TRYCbx)
        self.ui.usdCbx.currentIndexChanged.connect(self.USDCbx)
        self.ui.rubCbx.currentIndexChanged.connect(self.RUBCbx)

        self.ui.tbx.textEdited.connect(self.TRYTbx)
        self.ui.tbx3.textEdited.connect(self.USDTbx)
        self.ui.tbx7.textEdited.connect(self.RUBTbx)

    def ApiStart(self,baseCurrency,currency):
        url = "https://api.exchangeratesapi.io/latest?base="+baseCurrency
        result = requests.get(url)
        result = json.loads(result.text)
        return str(result["rates"][baseCurrency]),str(result["rates"][currency])

    def start(self):
        self.TRYCbx()
        self.USDCbx()
        self.RUBCbx()

    def TRYCbx(self):
        TRYtext = self.ui.tryCbx.currentText()
        TRYtext = TRYtext.split("-")
        x = self.ApiStart(TRYtext[0],TRYtext[1])
        self.ui.tbx.setText(x[0])
        self.ui.tbx2.setText(x[1])
    def USDCbx(self):
        USDText = self.ui.usdCbx.currentText()
        USDText = USDText.split("-")
        x = self.ApiStart(USDText[0],USDText[1])
        self.ui.tbx3.setText(x[0])
        self.ui.tbx4.setText(x[1])
    def RUBCbx(self):
        RUBText = self.ui.rubCbx.currentText()
        RUBText = RUBText.split("-")
        x = self.ApiStart(RUBText[0],RUBText[1])
        self.ui.tbx7.setText(x[0])
        self.ui.tbx8.setText(x[1])

    def changeTbx(self,cbx,tbx,tbx2):
        x = cbx.currentText()
        x = x.split("-")
        rate = self.ApiStart(x[0],x[1])
        currency = tbx.text()
        cal = self.calc(rate[1],currency)
        tbx2.setText(str(cal))

    def TRYTbx(self):
        try:
            self.changeTbx(self.ui.tryCbx,self.ui.tbx,self.ui.tbx2)
        except:
            pass
    def USDTbx(self):
        try:
            self.changeTbx(self.ui.usdCbx,self.ui.tbx3,self.ui.tbx4)
        except:
            pass
    def RUBTbx(self):
        try :
            self.changeTbx(self.ui.rubCbx,self.ui.tbx7,self.ui.tbx8)
        except:
            pass

    
    def calc(self,currency,cur):
        x = float(currency) * float(cur)
        return x
        




if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    main = CurrentApplication()
    main.show()
    app.setStyle("Fusion")
    app.exit(app.exec_())
