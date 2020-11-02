## Maresal Programming ##

import sys
from PyQt5 import QtWidgets

w = QtWidgets.QMainWindow
d = QtWidgets.QApplication

class MainForm(w):
    def __init__(self):
        super(MainForm,self).__init__()

        self.setWindowTitle("Calculator")
        self.setGeometry(200,200,500,500)
        self.initUI()

    def initUI(self):
        self.lbl_sayi1 = QtWidgets.QLabel(self)
        self.lbl_sayi1.setText("Sayı 1 :")
        self.lbl_sayi1.move(50,30)

        self.txt_sayi1 = QtWidgets.QLineEdit(self)
        self.txt_sayi1.move(150,30)
        self.txt_sayi1.resize(200,32)

        self.lbl_sayi2 = QtWidgets.QLabel(self)
        self.lbl_sayi2.setText("Sayı 2 :")
        self.lbl_sayi2.move(50,80)

        self.txt_sayi2 = QtWidgets.QLineEdit(self)
        self.txt_sayi2.move(150,80)
        self.txt_sayi2.resize(200,32)

        self.btn_topla = QtWidgets.QPushButton(self)
        self.btn_topla.setText("Toplama")
        self.btn_topla.move(150,130)
        self.btn_topla.clicked.connect(self.hesapla)

        self.btn_topla = QtWidgets.QPushButton(self)
        self.btn_topla.setText("Çıkarma")
        self.btn_topla.move(150,170)
        self.btn_topla.clicked.connect(self.hesapla)

        self.btn_topla = QtWidgets.QPushButton(self)
        self.btn_topla.setText("Çarpma")
        self.btn_topla.move(150,210)
        self.btn_topla.clicked.connect(self.hesapla)

        self.btn_topla = QtWidgets.QPushButton(self)
        self.btn_topla.setText("Bölme")
        self.btn_topla.move(150,250)
        self.btn_topla.clicked.connect(self.hesapla)

        self.lbl_sonuc = QtWidgets.QLabel(self)
        self.lbl_sonuc.setText("Sonuç :")
        self.lbl_sonuc.move(150,290)

    def hesapla(self):
        sender = self.sender().text()
        result = 0
        if sender == "Toplama" :
            result = int(self.txt_sayi1.text()) + int(self.txt_sayi2.text())
        elif sender == "Çıkarma":
            result = int(self.txt_sayi1.text()) - int(self.txt_sayi2.text())
        elif sender == "Çarpma":
            result = int(self.txt_sayi1.text()) * int(self.txt_sayi2.text())
        elif sender == "Bölme":
            result = float(self.txt_sayi1.text()) / float(self.txt_sayi2.text())

        self.lbl_sonuc.setStyleSheet('font: 75 10pt "MS Shell Dlg 2";')
        self.lbl_sonuc.setText("Sonuç : "+ str(result))


def app():
    app = d(sys.argv)
    win = MainForm()
    win.show()
    app.setStyle('Fusion')
    sys.exit(app.exec_())

app()