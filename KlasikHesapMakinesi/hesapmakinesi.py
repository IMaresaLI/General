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
import sys
from hesapmakinesi2 import Ui_MainWindow 


class hesapMKN(QtWidgets.QMainWindow):
    def __init__(self):
        super(hesapMKN,self).__init__()
        self.hp = Ui_MainWindow()
        self.hp.setupUi(self)
        self.show()

        self.hp.sifir.pressed.connect(self.btnzero)
        self.hp.bir.pressed.connect(self.btnone)
        self.hp.iki.pressed.connect(self.btntwo)
        self.hp.uc.pressed.connect(self.btnthree)
        self.hp.dort.pressed.connect(self.btnfour)
        self.hp.bes.pressed.connect(self.btnfive)
        self.hp.alti.pressed.connect(self.btnsix)
        self.hp.yedi.pressed.connect(self.btnseven)
        self.hp.sekiz.pressed.connect(self.btneight)
        self.hp.dokuz.pressed.connect(self.btnnine)
        self.hp.silme.pressed.connect(self.clearLine)
        self.hp.modalma.pressed.connect(self.getMod)
        self.hp.bolme.pressed.connect(self.section)
        self.hp.carpma.pressed.connect(self.multiplication)
        self.hp.arti.pressed.connect(self.addition)
        self.hp.eksi.pressed.connect(self.subtraction)
        self.hp.esittir.pressed.connect(self.equals)
        self.hp.pushButton.pressed.connect(self.parentheses1)
        self.hp.pushButton_2.pressed.connect(self.parentheses2)

    def btnzero(self):
        bar = self.hp.lineEdit.text()
        bar += '0'
        self.hp.lineEdit.setText(bar)
    def btnone(self):
        bar = self.hp.lineEdit.text()
        bar += '1'
        self.hp.lineEdit.setText(bar)
    def btntwo(self):
        bar = self.hp.lineEdit.text()
        bar += '2'
        self.hp.lineEdit.setText(bar)
    def btnthree(self):
        bar = self.hp.lineEdit.text()
        bar += '3'
        self.hp.lineEdit.setText(bar)
    def btnfour(self):
        bar = self.hp.lineEdit.text()
        bar += '4'
        self.hp.lineEdit.setText(bar)
    def btnfive(self):
        bar = self.hp.lineEdit.text()
        bar += '5'
        self.hp.lineEdit.setText(bar)
    def btnsix(self):
        bar = self.hp.lineEdit.text()
        bar += '6'
        self.hp.lineEdit.setText(bar)
    def btnseven(self):
        bar = self.hp.lineEdit.text()
        bar += '7'
        self.hp.lineEdit.setText(bar)
    def btneight(self):
        bar = self.hp.lineEdit.text()
        bar += '8'
        self.hp.lineEdit.setText(bar)
    def btnnine(self):
        bar = self.hp.lineEdit.text()
        bar += '9'
        self.hp.lineEdit.setText(bar)
    def getMod(self):
        bar = self.hp.lineEdit.text()
        bar += '%'
        self.hp.lineEdit.setText(bar)
    def section(self):
        bar = self.hp.lineEdit.text()
        bar += '/'
        self.hp.lineEdit.setText(bar)
    def multiplication(self):
        bar = self.hp.lineEdit.text()
        bar += '*'
        self.hp.lineEdit.setText(bar)

    def addition(self):
        bar = self.hp.lineEdit.text()
        bar += '+'
        self.hp.lineEdit.setText(bar)

    def subtraction(self):
        bar = self.hp.lineEdit.text()
        bar += '-'
        self.hp.lineEdit.setText(bar)

    def parentheses1(self):
        bar = self.hp.lineEdit.text()
        bar += '('
        self.hp.lineEdit.setText(bar)

    def parentheses2(self):
        bar = self.hp.lineEdit.text()
        bar += ')'
        self.hp.lineEdit.setText(bar)

    def clearLine(self):
        self.hp.lineEdit.clear()

    def equals(self):
        bar = self.hp.lineEdit.text()
        try:
            result = eval(bar)
            self.hp.lineEdit.setText(str(result))
        except Exception as err :
            self.hp.lineEdit.setText(str(err))

    



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    main = hesapMKN()
    app.setStyle('Fusion')
    app.exit(app.exec_())