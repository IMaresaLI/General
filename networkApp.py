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

from PyQt5 import QtWidgets,QtGui,QtCore,QtNetwork
import os ,sys,socket,time,threading
from network import Ui_MainWindow
import ping
from queue import Queue
from scapy.all import ARP, Ether, srp


class networkingApp(QtWidgets.QMainWindow):
    def __init__(self):
        super(networkingApp,self).__init__()
        self.nt = Ui_MainWindow()
        self.nt.setupUi(self)
        hst = socket.gethostname()
        hostName = socket.gethostbyname(hst)
        self.nt.statusbar.showMessage(hostName)
        

        self.nt.actionPinging.triggered.connect(self.evt_btn_clicked)
        self.nt.actionNetworkipList.triggered.connect(self.NetworkList)
        self.nt.lineEdit.returnPressed.connect(self.NetworkListStart)
        self.nt.actionOpenPorts.triggered.connect(self.startPorting)
        self.nt.actionmaresalp.triggered.connect(self.maresalP)
 

    def Porting(self,value):
        textting = self.nt.textBrowser.toPlainText()
        textting+=value
        self.nt.textBrowser.setText(textting)

    def startPorting(self):
        self.nt.textBrowser.clear()
        self.worker = WorkerThread()
        self.worker.start()
        self.worker.finished.connect(self.evt_worker_finished)
        self.worker.update_val.connect(self.Porting)
        self.progressBar()

    def NetworkList(self):
        self.nt.lineEdit.setHidden(False)

    def NetworkListStart(self):
        self.nt.lineEdit.setHidden(True)
        self.nt.textBrowser.clear()
        if self.nt.lineEdit.text() == "":
            target_ip = "192.168.1.1/24"
        else :
            target_ip = self.nt.lineEdit.text().strip()+"/24"
        arp = ARP(pdst=target_ip)
        ether = Ether(dst="ff:ff:ff:ff:ff:ff")
        packet = ether/arp

        result = srp(packet, timeout=3, verbose=0)[0]

        clients = []

        for sent, received in result:
            clients.append({'ip': received.psrc, 'mac': received.hwsrc})
        self.nt.textBrowser.setText("İnternet Ağınıza Bağlı Cihazların Ip Adresleri\n")
        for client in clients:
            text = self.nt.textBrowser.toPlainText()
            text += "{:16}\n".format(client['ip'])
            self.nt.textBrowser.setText(text)

    def pingGet(self,val):
        ip = "192.168.1."+str(val)
        if ping.ping_ip(ip):
            text = self.nt.textBrowser.toPlainText()
            text+= f"{ip} Ip'ye ping atıldı ve geri dönüş sağlandı.\n"
            self.nt.textBrowser.setText(text)
        else:
            text = self.nt.textBrowser.toPlainText()
            text+= f"{ip} Ip'ye ping atıldı.Fakat geri dönüş sağlanamadı.\n"
            self.nt.textBrowser.setText(text)

    def evt_btn_clicked(self):
        self.nt.textBrowser.clear()
        self.worker2 = WorkerThread2()
        self.worker2.start()
        self.worker2.finished.connect(self.evt_worker_finished)
        self.worker2.update_val.connect(self.pingGet)

    def evt_worker_finished(self):
        QtWidgets.QMessageBox.information(self,"İşlem Sonucu","Yapılan işlem sona ermiştir.")
        self.nt.progressBar.setValue(0)
        self.nt.progressBar.setHidden(True)

    def progressBar(self):
        self.nt.progressBar.setValue(0)
        self.nt.progressBar.setHidden(False)
        for i in range(101):
            self.nt.progressBar.setValue(i)
            time.sleep(0.1*1)

    def maresalP(self):
        os.startfile("https://www.instagram.com/maresalp/")

class WorkerThread(QtCore.QThread):
    update_val = QtCore.pyqtSignal(str)
    socket.setdefaulttimeout(0.25)
    def run(self):
        for i in range(130,136):
            self.porting(i)
            time.sleep(1)

    def porting(self,port):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        hst = socket.gethostname()
        hostName = socket.gethostbyname(hst)
        try:
            con = s.connect(("192.168.1.29", port))
            text = f"[AÇIK]{hostName} Ip Adresinin {port} Nolu Portu Açık.\n"
            self.update_val.emit(text)
        except:
            text = f"[KAPALI]{hostName} Ip Adresinin {port} Nolu Portu Açık değil.\n"
            self.update_val.emit(text)

class WorkerThread2(QtCore.QThread):
    update_val = QtCore.pyqtSignal(int)

    def run(self):
        for i in range(5):
            time.sleep(1)
            self.update_val.emit(i)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle("Fusion")
    main = networkingApp()
    main.show()
    app.exit(app.exec_())
