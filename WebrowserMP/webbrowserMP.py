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

from PyQt5 import QtCore
from PyQt5 import QtWidgets
from PyQt5 import QtGui
from PyQt5 import QtWebEngineWidgets
import os
import sys


class WeBMP(QtWidgets.QMainWindow):
    def __init__(self,*args,**kwargs):
        super(WeBMP,self).__init__(*args,**kwargs)
        self.setWindowTitle('Maresal Programming Browser')
        self.setMinimumSize(500,500)
        self.setWindowIcon(QtGui.QIcon('marelogo.ico'))
        self.showMaximized()
        self.show()


        self.tab = QtWidgets.QTabWidget()
        self.setCentralWidget(self.tab)
        self.tab.setDocumentMode(True)
        
        self.tab.tabBarDoubleClicked.connect(self.doubleclickNewTAB)
        self.tab.currentChanged.connect(self.currentTab)
        self.tab.tabCloseRequested.connect(self.closeTab)
        self.tab.setTabsClosable(True)

        self.navbar = QtWidgets.QToolBar()
        self.navbar.setMovable(False)


        self.addToolBar(self.navbar)
        self.geriBTN = QtWidgets.QAction('<<',self)
        self.geriBTN.triggered.connect(lambda: self.tab.currentWidget().back())
        self.navbar.addAction(self.geriBTN)

        self.ileriBTN = QtWidgets.QAction('>>',self)
        self.ileriBTN.triggered.connect(lambda:self.tab.currentWidget().forward())
        self.navbar.addAction(self.ileriBTN)

        self.yenileBTN = QtWidgets.QAction('Yenile',self)
        self.yenileBTN.setStatusTip("Yenile") 
        self.yenileBTN.triggered.connect(lambda: self.tab.currentWidget().reload())
        self.navbar.addAction(self.yenileBTN)

        self.anabtn = QtWidgets.QAction('Anasayfa', self) 
        self.anabtn.setStatusTip("Anasayfayı Aç") 
        self.anabtn.triggered.connect(self.anasayfa)
        self.navbar.addAction(self.anabtn)

        self.navbar.addSeparator()

        self.urlbar = QtWidgets.QLineEdit()
        self.urlbar.returnPressed.connect(self.Urlink)
        self.navbar.addWidget(self.urlbar)

        self.yenitab(QtCore.QUrl('https://www.google.com.tr'),'Anasayfa')


    def yenitab(self,url = None, QL = 'Boş Sayfa'):
        
        if url is None:
            url = QtCore.QUrl('http://www.google.com')

        browser = QtWebEngineWidgets.QWebEngineView()
        browser.setUrl(url)

        x = self.tab.addTab(browser,QL)
        self.tab.setCurrentIndex(x)
        
        browser.urlChanged.connect(lambda url,browser = browser:
                                self.UrlUpdate(url,browser))
        browser.loadFinished.connect(lambda _,x=x,browser=browser:
                                self.tab.setTabText(x,browser.page().title()))

    def doubleclickNewTAB(self, x):
        if x == -1:
            self.yenitab() 


    def closeTab(self,x):
        if self.tab.count() < 2:
            return

        self.tab.removeTab(x)

    def currentTab(self,x):
        url = self.tab.currentWidget().url()

        self.UrlUpdate(url, self.tab.currentWidget())
        
        self.updateMaintitle(self.tab.currentWidget())

    def updateMaintitle(self, browser):

        if browser != self.tab.currentWidget():
            return
        

        title = self.tab.currentWidget().page().title()

        self.setWindowTitle('% s - Maresal Programming Browser' % title)


    def Urlink(self):
        a = QtCore.QUrl(self.urlbar.text())

        if a.scheme() == '':
            a.setScheme('http')

        self.tab.currentWidget().QtWebEngineWidgets.QWebEngineView.setUrl(a)

    def UrlUpdate(self,a,wbr = None):
        if wbr != self.tab.currentWidget():
            return

        self.urlbar.setText(a.toString())
        self.urlbar.setCursorPosition(0)


    def anasayfa(self):
        self.tab.currentWidget().setUrl(QtCore.QUrl("http://www.google.com"))

    




app = QtWidgets.QApplication(sys.argv)
main = WeBMP()
app.setStyle('Fusion')
app.setApplicationName("Maresal Programming")
sys.exit(app.exec_())


    