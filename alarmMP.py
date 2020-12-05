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
from alarm import Ui_MainWindow as x
from PyQt5.uic import *
import os
import sys
import time as t
from pygame import mixer


class alarMP(QtWidgets.QMainWindow):
    def __init__(self):
        super(alarMP,self).__init__()
        self.ap = x()
        self.ap.setupUi(self)
        self.show()
        self.ap.timeEdit.setTime(QtCore.QTime.currentTime())
        self.ap.lcdNumber.setSegmentStyle(QtWidgets.QLCDNumber().Filled)
        zamanlayıcı = QtCore.QTimer(self.ap.lcdNumber)
        zamanlayıcı.timeout.connect(self.zamanigoster)
        zamanlayıcı.start(1000)
        self.ap.pushButton.clicked.connect(self.setAlarm)
        self.ap.pushButton_2.clicked.connect(self.stopalarm)
        global zamanlayıcı1
        zamanlayıcı1 = QtCore.QTimer(self.ap.menubar)
        zamanlayıcı1.timeout.connect(self.alarmstart)

    def zamanigoster(self):
        zaman = QtCore.QTime.currentTime()
        metin = zaman.toString("hh:mm")
        if (zaman.second()%2) == 0:
            metin =metin[:2]+" "+metin[3:]
        self.ap.lcdNumber.display(metin)

    def setAlarm(self):
        time = QtCore.QTime.currentTime()
        realtime =f"{time.hour()}:{time.minute()}"
        timeBox = self.ap.timeEdit.dateTime()
        BoxTime = f"{timeBox.time().hour()}:{timeBox.time().minute()}"
        AlarmName = self.ap.lineEdit.text()
        self.ap.label_3.setText(AlarmName)
        self.ap.label_4.setText(BoxTime)
        self.ap.label_5.setText(realtime)
        zamanlayıcı1.start(1000)

        
    def alarmstart(self):
        try:
            time = QtCore.QTime.currentTime()
            realtime =f"{time.hour()}:{time.minute()}"
            AlarmTime = self.ap.label_4.text()
            if realtime == AlarmTime:
                url = "music/AlarmSes.mp3"
                mixer.init()
                mixer.music.load(url)
                mixer.music.play() 
            else :
                mixer.music.stop()
                print(f"Saat {realtime}")
        except Exception:
            pass
            
    def stopalarm(self):
        try :
            mixer.music.stop()
            zamanlayıcı1.stop()
            self.ap.label_3.clear()
            self.ap.label_4.clear()
            self.ap.label_5.clear()
        except Exception :
            pass








if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    main = alarMP()
    app.setStyle('Fusion')
    app.exit(app.exec_())