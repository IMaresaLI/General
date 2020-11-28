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
from cryptoMP import Ui_MainWindow
import os
import sys
import requests


class MpCrypto(QtWidgets.QMainWindow):
    def __init__(self):
        super(MpCrypto,self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.show()
        self.cryptoget()


        zamanlayıcı = QtCore.QTimer(self.ui.frame)
        zamanlayıcı.timeout.connect(self.cryptoget)
        zamanlayıcı.start(5000)



    def cryptoget(self):
        a = requests.get(
            "https://api.coingecko.com/api/v3/coins/markets?vs_currency=TRY&order=market_cap_desc&per_page=100&page=1&sparkline=false")
        response_json = a.json()
        for i in response_json:
            if i["id"] == "bitcoin":
                self.ui.label.setText("Güncel Fiyat : "+str(i["current_price"])+" TRY")
                self.ui.label_2.setText("En Yüksek(24h) : "+str(i["high_24h"])+ " TRY") 
                print(f'BTC : {i["current_price"]}')
            if i["id"] == "dogecoin":
                self.ui.label_5.setText("Güncel Fiyat : "+str(i["current_price"])+" TRY")
                self.ui.label_6.setText("En Yüksek(24h) : "+str(i["high_24h"])+ " TRY") 
                print(f'DOGE : {i["current_price"]}')
            if i["id"] == "ethereum":
                self.ui.label_3.setText("Güncel Fiyat : "+str(i["current_price"])+" TRY")
                self.ui.label_4.setText("En Yüksek(24h) : "+str(i["high_24h"])+ " TRY") 
                print(f'ETH : {i["current_price"]}')
            if i["id"] == "ripple":
                self.ui.label_7.setText("Güncel Fiyat : "+str(i["current_price"])+" TRY")
                self.ui.label_8.setText("En Yüksek(24h) : "+str(i["high_24h"])+ " TRY") 
                print(f'XRP : {i["current_price"]}')




if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    main = MpCrypto()
    app.setStyle("Fusion")
    app.exit(app.exec_())