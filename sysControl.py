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
from pc import Ui_MainWindow
import sys
import os
import psutil
import platform
import GPUtil
import cpuinfo


class sysControls(QtWidgets.QMainWindow):
    def __init__(self):
        super(sysControls, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.show()

        zamanlayıcı = QtCore.QTimer(self.ui.cpuBar)
        zamanlayıcı.timeout.connect(self.sysStatus)
        zamanlayıcı.start(1000)
        self.sysConfig()

    def sysStatus(self):
        cpuStatus = psutil.cpu_percent()
        self.ui.cpuBar.setValue(int(cpuStatus))
        self.ui.label_3.setText(f"CPU : {str(cpuStatus)} %")
        ramStatus = psutil.virtual_memory().percent
        self.ui.ramBar.setValue(int(ramStatus))
        self.ui.label_4.setText(f"Ram : {str(ramStatus)} %")
        gpuStatus = GPUtil.getGPUs()
        for i in gpuStatus:
            self.ui.ramBar_2.setValue(int(i.load*100))
            self.ui.label_5.setText(f"GPU : {str(int(i.load*100))} %")

    def sysConfig(self):
        cDiskAlani = psutil.disk_usage(psutil.disk_partitions()[0][1])
        eDiskAlani = psutil.disk_usage(psutil.disk_partitions()[2][1])
        
        self.ui.diskYonetimi.setText(
            f"Sistem Path (C:/)\nToplam Alan : {round(((cDiskAlani.total/1024)/1024)/1024,2)} GB\nKullanılan Alan : {round(((cDiskAlani.used/1024)/1024)/1024,2)} GB || {cDiskAlani.percent}%\nBoş Alan : {round(((cDiskAlani.free/1024)/1024)/1024,2)} GB")
        self.ui.diskYonetimi_2.setText(
            f"Yedek Path (E:/)\nToplam Alan : {round(((eDiskAlani.total/1024)/1024)/1024,2)} GB\nKullanılan Alan : {round(((eDiskAlani.used/1024)/1024)/1024,2)} GB || {eDiskAlani.percent}%\nBoş Alan : {round(((eDiskAlani.free/1024)/1024)/1024,2)} GB")
        gpuStatus = GPUtil.getGPUs()
        for i in gpuStatus:
            self.ui.cpuYonetimi.setText(f"CPU Aygıt İsmi : {cpuinfo.get_cpu_info()['brand_raw']}\n\nBit Sürümü : {cpuinfo.get_cpu_info()['bits']}-Bit\n\nİşlemci Çekirdeği Sayısı = {cpuinfo.get_cpu_info()['count']}\n\nMinimum GHz : {psutil.cpu_freq()[1]} GHz\n\nMaximum GHz : {psutil.cpu_freq()[2]} GHz\n\nŞuan Kullanılan GHz : {psutil.cpu_freq()[0]} GHz\n\nRam : {round(((psutil.virtual_memory().total/1024)/1024)/1024,0)} GB\n\nGPU Aygıt İsmi : {i.name}\n\nGPU Bellek Boyutu : {i.memoryTotal/1024} GB\n\nGPU Sıcaklığı : {i.temperature} °C / Program Açıldığındaki Sıcaklıktır.")
            



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    main = sysControls()
    app.setStyle("Fusion")
    app.exit(app.exec_())

    