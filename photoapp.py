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
import sys
from photo import Ui_MainWindow as a
from PIL import Image, ImageFilter
from random import *
import string
import os


class pth(QtWidgets.QMainWindow):
    def __init__(self):
        super(pth, self).__init__()
        self.ui = a()
        self.ui.setupUi(self)
        self.show()

        self.ui.actionOpen.triggered.connect(self.openimage)

        self.ui.pushButton.clicked.connect(self.imageSHARPEN)
        self.ui.pushButton_2.clicked.connect(self.blurmenu)
        self.ui.pushButton_11.clicked.connect(self.blur)
        self.ui.pushButton_12.clicked.connect(self.BoxBlur)
        self.ui.pushButton_13.clicked.connect(self.GaussianBlu)
        self.ui.pushButton_3.clicked.connect(self.contour)
        self.ui.pushButton_4.clicked.connect(self.edge)
        self.ui.pushButton_16.clicked.connect(self.edgeEnhange)
        self.ui.pushButton_14.clicked.connect(self.edgeEnhange_more)
        self.ui.pushButton_15.clicked.connect(self.finedges)
        self.ui.pushButton_5.clicked.connect(self.filters)
        self.ui.pushButton_21.clicked.connect(self.minfilter)
        self.ui.pushButton_17.clicked.connect(self.maxfilter)
        self.ui.pushButton_18.clicked.connect(self.medianfilter)
        self.ui.pushButton_19.clicked.connect(self.Modefilter)
        self.ui.pushButton_20.clicked.connect(self.Rankfilter)
        self.ui.pushButton_6.clicked.connect(self.smoothmenu)
        self.ui.pushButton_22.clicked.connect(self.smooth)
        self.ui.pushButton_23.clicked.connect(self.smoothmore)
        self.ui.pushButton_7.clicked.connect(self.others)
        self.ui.pushButton_28.clicked.connect(self.detail)
        self.ui.pushButton_24.clicked.connect(self.emboss)
        self.ui.pushButton_25.clicked.connect(self.unsharpmask)
        self.ui.pushButton_8.clicked.connect(self.back)
        self.ui.pushButton_9.clicked.connect(self.go)
        self.ui.pushButton_10.clicked.connect(self.reset)
        self.ui.actionSave.triggered.connect(self.save)
        self.ui.actionSave_As.triggered.connect(self.saveAs)
        self.ui.actionExit.triggered.connect(self.exit)

    def btnClosed(self):
        if self.ui.groupBox.isHidden() == True:
            self.ui.groupBox_2.setHidden(True)
            self.ui.pushButton_4.setStyleSheet("#pushButton_4{border-image: url(:/icons/icons/btn1.png);}\n"
                                            "#pushButton_4:hover{border-image: url(:/icons/icons/btn.png);}")
            self.ui.groupBox_3.setHidden(True)
            self.ui.pushButton_5.setStyleSheet("#pushButton_5{border-image: url(:/icons/icons/btn1.png);}\n"
                                            "#pushButton_5:hover{border-image: url(:/icons/icons/btn.png);}")
            self.ui.groupBox_4.setHidden(True)
            self.ui.pushButton_6.setStyleSheet("#pushButton_6{border-image: url(:/icons/icons/btn1.png);}\n"
                                            "#pushButton_6:hover{border-image: url(:/icons/icons/btn.png);}")
            self.ui.groupBox_5.setHidden(True)
            self.ui.pushButton_7.setStyleSheet("#pushButton_7{border-image: url(:/icons/icons/btn1.png);}\n"
                                            "#pushButton_7:hover{border-image: url(:/icons/icons/btn.png);}")
        elif self.ui.groupBox_2.isHidden() == True :
            self.ui.groupBox.setHidden(True)
            self.ui.pushButton_2.setStyleSheet("#pushButton_2{border-image: url(:/icons/icons/btn1.png);}\n"
                                            "#pushButton_2:hover{border-image: url(:/icons/icons/btn.png);}")
            self.ui.groupBox_3.setHidden(True)
            self.ui.pushButton_5.setStyleSheet("#pushButton_5{border-image: url(:/icons/icons/btn1.png);}\n"
                                            "#pushButton_5:hover{border-image: url(:/icons/icons/btn.png);}")
            self.ui.groupBox_4.setHidden(True)
            self.ui.pushButton_6.setStyleSheet("#pushButton_6{border-image: url(:/icons/icons/btn1.png);}\n"
                                            "#pushButton_6:hover{border-image: url(:/icons/icons/btn.png);}")
            self.ui.groupBox_5.setHidden(True)
            self.ui.pushButton_7.setStyleSheet("#pushButton_7{border-image: url(:/icons/icons/btn1.png);}\n"
                                            "#pushButton_7:hover{border-image: url(:/icons/icons/btn.png);}")
        elif self.ui.groupBox_3.isHidden() == True :
            self.ui.groupBox.setHidden(True)
            self.ui.pushButton_2.setStyleSheet("#pushButton_2{border-image: url(:/icons/icons/btn1.png);}\n"
                                            "#pushButton_2:hover{border-image: url(:/icons/icons/btn.png);}")
            self.ui.groupBox_2.setHidden(True)
            self.ui.pushButton_4.setStyleSheet("#pushButton_4{border-image: url(:/icons/icons/btn1.png);}\n"
                                            "#pushButton_4:hover{border-image: url(:/icons/icons/btn.png);}")
            self.ui.groupBox_4.setHidden(True)
            self.ui.pushButton_6.setStyleSheet("#pushButton_6{border-image: url(:/icons/icons/btn1.png);}\n"
                                            "#pushButton_6:hover{border-image: url(:/icons/icons/btn.png);}")
            self.ui.groupBox_5.setHidden(True)
            self.ui.pushButton_7.setStyleSheet("#pushButton_7{border-image: url(:/icons/icons/btn1.png);}\n"
                                            "#pushButton_7:hover{border-image: url(:/icons/icons/btn.png);}")
        elif self.ui.groupBox_4.isHidden() == True :
            self.ui.groupBox.setHidden(True)
            self.ui.pushButton_2.setStyleSheet("#pushButton_2{border-image: url(:/icons/icons/btn1.png);}\n"
                                            "#pushButton_2:hover{border-image: url(:/icons/icons/btn.png);}")
            self.ui.groupBox_2.setHidden(True)
            self.ui.pushButton_4.setStyleSheet("#pushButton_4{border-image: url(:/icons/icons/btn1.png);}\n"
                                            "#pushButton_4:hover{border-image: url(:/icons/icons/btn.png);}")
            self.ui.groupBox_3.setHidden(True)
            self.ui.pushButton_5.setStyleSheet("#pushButton_5{border-image: url(:/icons/icons/btn1.png);}\n"
                                            "#pushButton_5:hover{border-image: url(:/icons/icons/btn.png);}")
            self.ui.groupBox_5.setHidden(True)
            self.ui.pushButton_7.setStyleSheet("#pushButton_7{border-image: url(:/icons/icons/btn1.png);}\n"
                                            "#pushButton_7:hover{border-image: url(:/icons/icons/btn.png);}")
        elif self.ui.groupBox_5.isHidden() == True :
            self.ui.groupBox.setHidden(True)
            self.ui.pushButton_2.setStyleSheet("#pushButton_2{border-image: url(:/icons/icons/btn1.png);}\n"
                                            "#pushButton_2:hover{border-image: url(:/icons/icons/btn.png);}")
            self.ui.groupBox_2.setHidden(True)
            self.ui.pushButton_4.setStyleSheet("#pushButton_4{border-image: url(:/icons/icons/btn1.png);}\n"
                                            "#pushButton_4:hover{border-image: url(:/icons/icons/btn.png);}")
            self.ui.groupBox_3.setHidden(True)
            self.ui.pushButton_5.setStyleSheet("#pushButton_5{border-image: url(:/icons/icons/btn1.png);}\n"
                                            "#pushButton_5:hover{border-image: url(:/icons/icons/btn.png);}")
            self.ui.groupBox_4.setHidden(True)
            self.ui.pushButton_6.setStyleSheet("#pushButton_6{border-image: url(:/icons/icons/btn1.png);}\n"
                                            "#pushButton_6:hover{border-image: url(:/icons/icons/btn.png);}")

    def openimage(self):
        global img
        try:
            delprg()
            img = QtWidgets.QFileDialog.getOpenFileName()

            zz = Image.open(img[0])
            zz.save('prg/original.png')
            self.ui.label.setStyleSheet(
                "#label{image: url(prg/original.png);}")
            print(img[0])
            with open('prg/prg.txt', 'a+', encoding='UTF-8') as file:
                file.write('original.png'+'\n')
            x = img[0].split('/')
            self.ui.tabWidget.setTabText(0, x[-1])
            self.ui.frame.setHidden(False)
        except Exception as err:
            with open('log.txt', 'a+', encoding='UTF-8') as file:
                file.write(str(err)+'\n')

    def save(self):
        try:
            c = self.ui.label.styleSheet()
            n = c.split('(')
            n2 = n[1].split(')')

            xx = Image.open(n2[0])
            xx.save(img[0])

        except Exception as err:
            with open('log.txt', 'a+', encoding='UTF-8') as file:
                file.write(str(err)+'\n')

    def saveAs(self):
        try:
            c = self.ui.label.styleSheet()
            n = c.split('(')
            n2 = n[1].split(')')
            zz = Image.open(n2[0])
            a = QtWidgets.QFileDialog.getSaveFileName(
                self, 'Selected Folder', None, '*.jpg;; *.png ;;*.gif')
            zz.save(a[0])
            QtWidgets.QMessageBox.information(
                self, 'Kaydedildi', f'Resminiz belirlediğiniz {a[0]} konumuna eklendi.')
        except Exception as err:
            with open('log.txt', 'a+', encoding='UTF-8') as file:
                file.write(str(err)+'\n')

    def imageSHARPEN(self):
        try:
            c = self.ui.label.styleSheet()
            z = c.split('(')
            v = z[1].split(')')

            img = Image.open(v[0])
            imgN = img.filter(ImageFilter.SHARPEN)
            character = string.ascii_letters
            paswd = ''.join(choice(character) for x in range(randint(4, 10)))
            imgN.save(f'prg/{paswd}.png')
            self.ui.label.setStyleSheet("#label{\n"
                                        "image: url(prg/"+paswd+".png);}")
            with open('prg/prg.txt', 'a+', encoding='UTF-8') as file:
                file.write(paswd+'.png\n')

            self.ui.pushButton_10.setEnabled(True)
            self.ui.pushButton_10.setStyleSheet("#pushButton_10{border-image: url(:/icons/icons/reset.png);}\n"
                                                "#pushButton_10:hover{border-image: url(:/icons/icons/reset1.png);}")
            self.ui.pushButton_8.setEnabled(True)
            self.ui.pushButton_8.setStyleSheet("#pushButton_8{border-image: url(:/icons/icons/leftok.png);}\n"
                                               "#pushButton_8:hover{border-image: url(:/icons/icons/leftok1.png);}")
        except Exception as err:
            with open('log.txt', 'a+', encoding='UTF-8') as file:
                file.write(str(err)+'\n')

    def blurmenu(self):
        try:
            
            a = self.ui.groupBox.isHidden()

            if a == False:
                
                self.ui.groupBox.setHidden(True)
                self.ui.pushButton_2.setStyleSheet("#pushButton_2{border-image: url(:/icons/icons/btn1.png);}\n"
                                                   "#pushButton_2:hover{border-image: url(:/icons/icons/btn.png);}")
            else:
                self.btnClosed()
                self.ui.groupBox.setHidden(False)
                self.ui.pushButton_2.setStyleSheet(
                    "#pushButton_2{border-image: url(:/icons/icons/btn.png);}")
        except Exception as err:
            with open('log.txt', 'a+', encoding='UTF-8') as file:
                file.write(str(err)+'\n')

    def blur(self):
        try:
            c = self.ui.label.styleSheet()
            z = c.split('(')
            v = z[1].split(')')
            img = Image.open(v[0])
            imgN = img.filter(ImageFilter.BLUR)
            character = string.ascii_letters
            paswd = ''.join(choice(character) for x in range(randint(4, 10)))
            imgN.save(f'prg/{paswd}.png')
            self.ui.label.setStyleSheet("#label{\n"
                                        "image: url(prg/"+paswd+".png);}")
            with open('prg/prg.txt', 'a+', encoding='UTF-8') as file:
                file.write(paswd+'.png\n')

            self.ui.pushButton_10.setEnabled(True)
            self.ui.pushButton_10.setStyleSheet("#pushButton_10{border-image: url(:/icons/icons/reset.png);}\n"
                                                "#pushButton_10:hover{border-image: url(:/icons/icons/reset1.png);}")
            self.ui.pushButton_8.setEnabled(True)
            self.ui.pushButton_8.setStyleSheet("#pushButton_8{border-image: url(:/icons/icons/leftok.png);}\n"
                                               "#pushButton_8:hover{border-image: url(:/icons/icons/leftok1.png);}")
        except Exception as err:
            with open('log.txt', 'a+', encoding='UTF-8') as file:
                file.write(str(err)+'\n')

    def BoxBlur(self):
        try:
            c = self.ui.label.styleSheet()
            z = c.split('(')
            v = z[1].split(')')
            img = Image.open(v[0])
            text, ok = QtWidgets.QInputDialog.getInt(
                self, "Get Radius", "Radius", QtWidgets.QLineEdit.Normal)
            if text and ok:
                print(text)
                imgN = img.filter(ImageFilter.BoxBlur(text))
                character = string.ascii_letters
                paswd = ''.join(choice(character)
                                for x in range(randint(4, 10)))
                imgN.save(f'prg/{paswd}.png')
                self.ui.label.setStyleSheet("#label{\n"
                                            "image: url(prg/"+paswd+".png);}")
                with open('prg/prg.txt', 'a+', encoding='UTF-8') as file:
                    file.write(paswd+'.png\n')
            self.ui.pushButton_10.setEnabled(True)
            self.ui.pushButton_10.setStyleSheet("#pushButton_10{border-image: url(:/icons/icons/reset.png);}\n"
                                                "#pushButton_10:hover{border-image: url(:/icons/icons/reset1.png);}")
            self.ui.pushButton_8.setEnabled(True)
            self.ui.pushButton_8.setStyleSheet("#pushButton_8{border-image: url(:/icons/icons/leftok.png);}\n"
                                               "#pushButton_8:hover{border-image: url(:/icons/icons/leftok1.png);}")
        except Exception as err:
            with open('log.txt', 'a+', encoding='UTF-8') as file:
                file.write(str(err)+'\n')

    def GaussianBlu(self):
        try:
            c = self.ui.label.styleSheet()
            z = c.split('(')
            v = z[1].split(')')
            img = Image.open(v[0])
            imgN = img.filter(ImageFilter.GaussianBlur)
            character = string.ascii_letters
            paswd = ''.join(choice(character) for x in range(randint(4, 10)))
            imgN.save(f'prg/{paswd}.png')
            self.ui.label.setStyleSheet("#label{\n"
                                        "image: url(prg/"+paswd+".png);}")
            with open('prg/prg.txt', 'a+', encoding='UTF-8') as file:
                file.write(paswd+'.png\n')

            self.ui.pushButton_10.setEnabled(True)
            self.ui.pushButton_10.setStyleSheet("#pushButton_10{border-image: url(:/icons/icons/reset.png);}\n"
                                                "#pushButton_10:hover{border-image: url(:/icons/icons/reset1.png);}")
            self.ui.pushButton_8.setEnabled(True)
            self.ui.pushButton_8.setStyleSheet("#pushButton_8{border-image: url(:/icons/icons/leftok.png);}\n"
                                               "#pushButton_8:hover{border-image: url(:/icons/icons/leftok1.png);}")
        except Exception as err:
            with open('log.txt', 'a+', encoding='UTF-8') as file:
                file.write(str(err)+'\n')

    def contour(self):
        try:
            c = self.ui.label.styleSheet()
            z = c.split('(')
            v = z[1].split(')')
            img = Image.open(v[0])
            imgN = img.filter(ImageFilter.CONTOUR)
            character = string.ascii_letters
            paswd = ''.join(choice(character) for x in range(randint(4, 10)))
            imgN.save(f'prg/{paswd}.png')
            self.ui.label.setStyleSheet("#label{\n"
                                        "image: url(prg/"+paswd+".png);}")
            with open('prg/prg.txt', 'a+', encoding='UTF-8') as file:
                file.write(paswd+'.png\n')
            self.ui.pushButton_10.setEnabled(True)
            self.ui.pushButton_10.setStyleSheet("#pushButton_10{border-image: url(:/icons/icons/reset.png);}\n"
                                                "#pushButton_10:hover{border-image: url(:/icons/icons/reset1.png);}")
            self.ui.pushButton_8.setEnabled(True)
            self.ui.pushButton_8.setStyleSheet("#pushButton_8{border-image: url(:/icons/icons/leftok.png);}\n"
                                               "#pushButton_8:hover{border-image: url(:/icons/icons/leftok1.png);}")
        except Exception as err:
            with open('log.txt', 'a+', encoding='UTF-8') as file:
                file.write(str(err)+'\n')

    def edge(self):
        try:
            
            a = self.ui.groupBox_2.isHidden()

            if a == False:
                self.ui.groupBox_2.setHidden(True)
                self.ui.pushButton_4.setStyleSheet("#pushButton_4{border-image: url(:/icons/icons/btn1.png);}\n"
                                                   "#pushButton_4:hover{border-image: url(:/icons/icons/btn.png);}")
            else:
                self.btnClosed()
                self.ui.groupBox_2.setHidden(False)
                self.ui.pushButton_4.setStyleSheet(
                    "#pushButton_2{border-image: url(:/icons/icons/btn.png);}")
        except Exception as err:
            with open('log.txt', 'a+', encoding='UTF-8') as file:
                file.write(str(err)+'\n')

    def edgeEnhange(self):
        try:
            c = self.ui.label.styleSheet()
            z = c.split('(')
            v = z[1].split(')')
            img = Image.open(v[0])
            imgN = img.filter(ImageFilter.EDGE_ENHANCE)
            character = string.ascii_letters
            paswd = ''.join(choice(character) for x in range(randint(4, 10)))
            imgN.save(f'prg/{paswd}.png')
            self.ui.label.setStyleSheet("#label{\n"
                                        "image: url(prg/"+paswd+".png);}")
            with open('prg/prg.txt', 'a+', encoding='UTF-8') as file:
                file.write(paswd+'.png\n')
            self.ui.pushButton_10.setEnabled(True)
            self.ui.pushButton_10.setStyleSheet("#pushButton_10{border-image: url(:/icons/icons/reset.png);}\n"
                                                "#pushButton_10:hover{border-image: url(:/icons/icons/reset1.png);}")
            self.ui.pushButton_8.setEnabled(True)
            self.ui.pushButton_8.setStyleSheet("#pushButton_8{border-image: url(:/icons/icons/leftok.png);}\n"
                                               "#pushButton_8:hover{border-image: url(:/icons/icons/leftok1.png);}")
        except Exception as err:
            with open('log.txt', 'a+', encoding='UTF-8') as file:
                file.write(str(err)+'\n')

    def edgeEnhange_more(self):
        try:
            c = self.ui.label.styleSheet()
            z = c.split('(')
            v = z[1].split(')')
            img = Image.open(v[0])
            imgN = img.filter(ImageFilter.EDGE_ENHANCE_MORE)
            character = string.ascii_letters
            paswd = ''.join(choice(character) for x in range(randint(4, 10)))
            imgN.save(f'prg/{paswd}.png')
            self.ui.label.setStyleSheet("#label{\n"
                                        "image: url(prg/"+paswd+".png);}")
            with open('prg/prg.txt', 'a+', encoding='UTF-8') as file:
                file.write(paswd+'.png\n')

            self.ui.pushButton_10.setEnabled(True)
            self.ui.pushButton_10.setStyleSheet("#pushButton_10{border-image: url(:/icons/icons/reset.png);}\n"
                                                "#pushButton_10:hover{border-image: url(:/icons/icons/reset1.png);}")
            self.ui.pushButton_8.setEnabled(True)
            self.ui.pushButton_8.setStyleSheet("#pushButton_8{border-image: url(:/icons/icons/leftok.png);}\n"
                                               "#pushButton_8:hover{border-image: url(:/icons/icons/leftok1.png);}")
        except Exception as err:
            with open('log.txt', 'a+', encoding='UTF-8') as file:
                file.write(str(err)+'\n')

    def finedges(self):
        try:
            c = self.ui.label.styleSheet()
            z = c.split('(')
            v = z[1].split(')')
            img = Image.open(v[0])
            imgN = img.filter(ImageFilter.FIND_EDGES)
            character = string.ascii_letters
            paswd = ''.join(choice(character) for x in range(randint(4, 10)))
            imgN.save(f'prg/{paswd}.png')
            self.ui.label.setStyleSheet("#label{\n"
                                        "image: url(prg/"+paswd+".png);}")
            with open('prg/prg.txt', 'a+', encoding='UTF-8') as file:
                file.write(paswd+'.png\n')

            self.ui.pushButton_10.setEnabled(True)
            self.ui.pushButton_10.setStyleSheet("#pushButton_10{border-image: url(:/icons/icons/reset.png);}\n"
                                                "#pushButton_10:hover{border-image: url(:/icons/icons/reset1.png);}")
            self.ui.pushButton_8.setEnabled(True)
            self.ui.pushButton_8.setStyleSheet("#pushButton_8{border-image: url(:/icons/icons/leftok.png);}\n"
                                               "#pushButton_8:hover{border-image: url(:/icons/icons/leftok1.png);}")
        except Exception as err:
            with open('log.txt', 'a+', encoding='UTF-8') as file:
                file.write(str(err)+'\n')

    def filters(self):
        try:
            
            a = self.ui.groupBox_3.isHidden()

            if a == False:
                self.ui.groupBox_3.setHidden(True)
                self.ui.pushButton_5.setStyleSheet("#pushButton_5{border-image: url(:/icons/icons/btn1.png);}\n"
                                                   "#pushButton_5:hover{border-image: url(:/icons/icons/btn.png);}")
            else:
                self.btnClosed()
                self.ui.groupBox_3.setHidden(False)
                self.ui.pushButton_5.setStyleSheet(
                    "#pushButton_5{border-image: url(:/icons/icons/btn.png);}")
        except Exception as err:
            with open('log.txt', 'a+', encoding='UTF-8') as file:
                file.write(str(err)+'\n')

    def minfilter(self):
        try:
            c = self.ui.label.styleSheet()
            z = c.split('(')
            v = z[1].split(')')
            img = Image.open(v[0])
            text, ok = QtWidgets.QInputDialog.getInt(
                self, "Get Radius", "Radius(1-3-5-7)", QtWidgets.QLineEdit.Normal)
            if text and ok:
                imgN = img.filter(ImageFilter.MinFilter(text))
                character = string.ascii_letters
                paswd = ''.join(choice(character)
                                for x in range(randint(4, 10)))
                imgN.save(f'prg/{paswd}.png')
                self.ui.label.setStyleSheet("#label{\n"
                                            "image: url(prg/"+paswd+".png);}")
                with open('prg/prg.txt', 'a+', encoding='UTF-8') as file:
                    file.write(paswd+'.png\n')

            self.ui.pushButton_10.setEnabled(True)
            self.ui.pushButton_10.setStyleSheet("#pushButton_10{border-image: url(:/icons/icons/reset.png);}\n"
                                                "#pushButton_10:hover{border-image: url(:/icons/icons/reset1.png);}")
            self.ui.pushButton_8.setEnabled(True)
            self.ui.pushButton_8.setStyleSheet("#pushButton_8{border-image: url(:/icons/icons/leftok.png);}\n"
                                               "#pushButton_8:hover{border-image: url(:/icons/icons/leftok1.png);}")
        except Exception as err:
            with open('log.txt', 'a+', encoding='UTF-8') as file:
                file.write(str(err)+'\n')

    def maxfilter(self):
        try:
            c = self.ui.label.styleSheet()
            z = c.split('(')
            v = z[1].split(')')
            img = Image.open(v[0])
            imgN = img.filter(ImageFilter.MaxFilter)
            character = string.ascii_letters
            paswd = ''.join(choice(character) for x in range(randint(4, 10)))
            imgN.save(f'prg/{paswd}.png')
            self.ui.label.setStyleSheet("#label{\n"
                                        "image: url(prg/"+paswd+".png);}")
            with open('prg/prg.txt', 'a+', encoding='UTF-8') as file:
                file.write(paswd+'.png\n')

            self.ui.pushButton_10.setEnabled(True)
            self.ui.pushButton_10.setStyleSheet("#pushButton_10{border-image: url(:/icons/icons/reset.png);}\n"
                                                "#pushButton_10:hover{border-image: url(:/icons/icons/reset1.png);}")
            self.ui.pushButton_8.setEnabled(True)
            self.ui.pushButton_8.setStyleSheet("#pushButton_8{border-image: url(:/icons/icons/leftok.png);}\n"
                                               "#pushButton_8:hover{border-image: url(:/icons/icons/leftok1.png);}")
        except Exception as err:
            with open('log.txt', 'a+', encoding='UTF-8') as file:
                file.write(str(err)+'\n')

    def medianfilter(self):
        try:
            c = self.ui.label.styleSheet()
            z = c.split('(')
            v = z[1].split(')')
            img = Image.open(v[0])
            imgN = img.filter(ImageFilter.MedianFilter)
            character = string.ascii_letters
            paswd = ''.join(choice(character) for x in range(randint(4, 10)))
            imgN.save(f'prg/{paswd}.png')
            self.ui.label.setStyleSheet("#label{\n"
                                        "image: url(prg/"+paswd+".png);}")
            with open('prg/prg.txt', 'a+', encoding='UTF-8') as file:
                file.write(paswd+'.png\n')
            self.ui.pushButton_10.setEnabled(True)
            self.ui.pushButton_10.setStyleSheet("#pushButton_10{border-image: url(:/icons/icons/reset.png);}\n"
                                                "#pushButton_10:hover{border-image: url(:/icons/icons/reset1.png);}")
            self.ui.pushButton_8.setEnabled(True)
            self.ui.pushButton_8.setStyleSheet("#pushButton_8{border-image: url(:/icons/icons/leftok.png);}\n"
                                               "#pushButton_8:hover{border-image: url(:/icons/icons/leftok1.png);}")
        except Exception as err:
            with open('log.txt', 'a+', encoding='UTF-8') as file:
                file.write(str(err)+'\n')

    def Modefilter(self):
        try:
            c = self.ui.label.styleSheet()
            z = c.split('(')
            v = z[1].split(')')
            img = Image.open(v[0])
            imgN = img.filter(ImageFilter.ModeFilter)
            character = string.ascii_letters
            paswd = ''.join(choice(character) for x in range(randint(4, 10)))
            imgN.save(f'prg/{paswd}.png')
            self.ui.label.setStyleSheet("#label{\n"
                                        "image: url(prg/"+paswd+".png);}")
            with open('prg/prg.txt', 'a+', encoding='UTF-8') as file:
                file.write(paswd+'.png\n')

            self.ui.pushButton_10.setEnabled(True)
            self.ui.pushButton_10.setStyleSheet("#pushButton_10{border-image: url(:/icons/icons/reset.png);}\n"
                                                "#pushButton_10:hover{border-image: url(:/icons/icons/reset1.png);}")
            self.ui.pushButton_8.setEnabled(True)
            self.ui.pushButton_8.setStyleSheet("#pushButton_8{border-image: url(:/icons/icons/leftok.png);}\n"
                                               "#pushButton_8:hover{border-image: url(:/icons/icons/leftok1.png);}")
        except Exception as err:
            with open('log.txt', 'a+', encoding='UTF-8') as file:
                file.write(str(err)+'\n')

    def Rankfilter(self):
        try:
            c = self.ui.label.styleSheet()
            z = c.split('(')
            v = z[1].split(')')
            img = Image.open(v[0])
            text, ok = QtWidgets.QInputDialog.getInt(
                self, "Get Radius", "Radius(1-3-5-7..)", QtWidgets.QLineEdit.Normal)
            if text and ok:
                imgN = img.filter(ImageFilter.RankFilter(text, 2))
                character = string.ascii_letters
                paswd = ''.join(choice(character)
                                for x in range(randint(4, 10)))
                imgN.save(f'prg/{paswd}.png')
                self.ui.label.setStyleSheet("#label{\n"
                                            "image: url(prg/"+paswd+".png);}")
                with open('prg/prg.txt', 'a+', encoding='UTF-8') as file:
                    file.write(paswd+'.png\n')

            self.ui.pushButton_10.setEnabled(True)
            self.ui.pushButton_10.setStyleSheet("#pushButton_10{border-image: url(:/icons/icons/reset.png);}\n"
                                                "#pushButton_10:hover{border-image: url(:/icons/icons/reset1.png);}")
            self.ui.pushButton_8.setEnabled(True)
            self.ui.pushButton_8.setStyleSheet("#pushButton_8{border-image: url(:/icons/icons/leftok.png);}\n"
                                               "#pushButton_8:hover{border-image: url(:/icons/icons/leftok1.png);}")
        except Exception as err:
            with open('log.txt', 'a+', encoding='UTF-8') as file:
                file.write(str(err)+'\n')

    def smoothmenu(self):
        try:
            
            a = self.ui.groupBox_4.isHidden()

            if a == False:
                self.ui.groupBox_4.setHidden(True)
                self.ui.pushButton_6.setStyleSheet("#pushButton_6{border-image: url(:/icons/icons/btn1.png);}\n"
                                                   "#pushButton_6:hover{border-image: url(:/icons/icons/btn.png);}")
            else:
                self.btnClosed()
                self.ui.groupBox_4.setHidden(False)
                self.ui.pushButton_6.setStyleSheet(
                    "#pushButton_6{border-image: url(:/icons/icons/btn.png);}")
        except Exception as err:
            with open('log.txt', 'a+', encoding='UTF-8') as file:
                file.write(str(err)+'\n')

    def smooth(self):
        try:
            c = self.ui.label.styleSheet()
            z = c.split('(')
            v = z[1].split(')')
            img = Image.open(v[0])
            imgN = img.filter(ImageFilter.SMOOTH)
            character = string.ascii_letters
            paswd = ''.join(choice(character) for x in range(randint(4, 10)))
            imgN.save(f'prg/{paswd}.png')
            self.ui.label.setStyleSheet("#label{\n"
                                        "image: url(prg/"+paswd+".png);}")
            with open('prg/prg.txt', 'a+', encoding='UTF-8') as file:
                file.write(paswd+'.png\n')

            self.ui.pushButton_10.setEnabled(True)
            self.ui.pushButton_10.setStyleSheet("#pushButton_10{border-image: url(:/icons/icons/reset.png);}\n"
                                                "#pushButton_10:hover{border-image: url(:/icons/icons/reset1.png);}")
            self.ui.pushButton_8.setEnabled(True)
            self.ui.pushButton_8.setStyleSheet("#pushButton_8{border-image: url(:/icons/icons/leftok.png);}\n"
                                               "#pushButton_8:hover{border-image: url(:/icons/icons/leftok1.png);}")
        except Exception as err:
            with open('log.txt', 'a+', encoding='UTF-8') as file:
                file.write(str(err)+'\n')

    def smoothmore(self):
        try:
            c = self.ui.label.styleSheet()
            z = c.split('(')
            v = z[1].split(')')
            img = Image.open(v[0])
            imgN = img.filter(ImageFilter.SMOOTH_MORE)
            character = string.ascii_letters
            paswd = ''.join(choice(character) for x in range(randint(4, 10)))
            imgN.save(f'prg/{paswd}.png')
            self.ui.label.setStyleSheet("#label{\n"
                                        "image: url(prg/"+paswd+".png);}")
            with open('prg/prg.txt', 'a+', encoding='UTF-8') as file:
                file.write(paswd+'.png\n')

            self.ui.pushButton_10.setEnabled(True)
            self.ui.pushButton_10.setStyleSheet("#pushButton_10{border-image: url(:/icons/icons/reset.png);}\n"
                                                "#pushButton_10:hover{border-image: url(:/icons/icons/reset1.png);}")
            self.ui.pushButton_8.setEnabled(True)
            self.ui.pushButton_8.setStyleSheet("#pushButton_8{border-image: url(:/icons/icons/leftok.png);}\n"
                                               "#pushButton_8:hover{border-image: url(:/icons/icons/leftok1.png);}")
        except Exception as err:
            with open('log.txt', 'a+', encoding='UTF-8') as file:
                file.write(str(err)+'\n')

    def others(self):
        try:
            
            a = self.ui.groupBox_5.isHidden()

            if a == False:
                self.ui.groupBox_5.setHidden(True)
                self.ui.pushButton_7.setStyleSheet("#pushButton_7{border-image: url(:/icons/icons/btn1.png);}\n"
                                                   "#pushButton_7:hover{border-image: url(:/icons/icons/btn.png);}")
            else:
                self.btnClosed()
                self.ui.groupBox_5.setHidden(False)
                self.ui.pushButton_7.setStyleSheet(
                    "#pushButton_7{border-image: url(:/icons/icons/btn.png);}")
        except Exception as err:
            with open('log.txt', 'a+', encoding='UTF-8') as file:
                file.write(str(err)+'\n')

    def detail(self):
        try:
            c = self.ui.label.styleSheet()
            z = c.split('(')
            v = z[1].split(')')
            img = Image.open(v[0])
            imgN = img.filter(ImageFilter.DETAIL)
            character = string.ascii_letters
            paswd = ''.join(choice(character) for x in range(randint(4, 10)))
            imgN.save(f'prg/{paswd}.png')
            self.ui.label.setStyleSheet("#label{\n"
                                        "image: url(prg/"+paswd+".png);}")
            with open('prg/prg.txt', 'a+', encoding='UTF-8') as file:
                file.write(paswd+'.png\n')

            self.ui.pushButton_10.setEnabled(True)
            self.ui.pushButton_10.setStyleSheet("#pushButton_10{border-image: url(:/icons/icons/reset.png);}\n"
                                                "#pushButton_10:hover{border-image: url(:/icons/icons/reset1.png);}")
            self.ui.pushButton_8.setEnabled(True)
            self.ui.pushButton_8.setStyleSheet("#pushButton_8{border-image: url(:/icons/icons/leftok.png);}\n"
                                               "#pushButton_8:hover{border-image: url(:/icons/icons/leftok1.png);}")
        except Exception as err:
            with open('log.txt', 'a+', encoding='UTF-8') as file:
                file.write(str(err)+'\n')

    def emboss(self):
        try:
            c = self.ui.label.styleSheet()
            z = c.split('(')
            v = z[1].split(')')
            img = Image.open(v[0])
            imgN = img.filter(ImageFilter.EMBOSS)
            character = string.ascii_letters
            paswd = ''.join(choice(character) for x in range(randint(4, 10)))
            imgN.save(f'prg/{paswd}.png')
            self.ui.label.setStyleSheet("#label{\n"
                                        "image: url(prg/"+paswd+".png);}")
            with open('prg/prg.txt', 'a+', encoding='UTF-8') as file:
                file.write(paswd+'.png\n')

            self.ui.pushButton_10.setEnabled(True)
            self.ui.pushButton_10.setStyleSheet("#pushButton_10{border-image: url(:/icons/icons/reset.png);}\n"
                                                "#pushButton_10:hover{border-image: url(:/icons/icons/reset1.png);}")
            self.ui.pushButton_8.setEnabled(True)
            self.ui.pushButton_8.setStyleSheet("#pushButton_8{border-image: url(:/icons/icons/leftok.png);}\n"
                                               "#pushButton_8:hover{border-image: url(:/icons/icons/leftok1.png);}")
        except Exception as err:
            with open('log.txt', 'a+', encoding='UTF-8') as file:
                file.write(str(err)+'\n')

    def unsharpmask(self):
        try:
            c = self.ui.label.styleSheet()
            z = c.split('(')
            v = z[1].split(')')
            img = Image.open(v[0])
            imgN = img.filter(ImageFilter.UnsharpMask)
            character = string.ascii_letters
            paswd = ''.join(choice(character) for x in range(randint(4, 10)))
            imgN.save(f'prg/{paswd}.png')
            self.ui.label.setStyleSheet("#label{\n"
                                        "image: url(prg/"+paswd+".png);}")
            with open('prg/prg.txt', 'a+', encoding='UTF-8') as file:
                file.write(paswd+'.png\n')

            self.ui.pushButton_10.setEnabled(True)
            self.ui.pushButton_10.setStyleSheet("#pushButton_10{border-image: url(:/icons/icons/reset.png);}\n"
                                                "#pushButton_10:hover{border-image: url(:/icons/icons/reset1.png);}")
            self.ui.pushButton_8.setEnabled(True)
            self.ui.pushButton_8.setStyleSheet("#pushButton_8{border-image: url(:/icons/icons/leftok.png);}\n"
                                               "#pushButton_8:hover{border-image: url(:/icons/icons/leftok1.png);}")
        except Exception as err:
            with open('log.txt', 'a+', encoding='UTF-8') as file:
                file.write(str(err)+'\n')

    def back(self):
        try:
            self.ui.pushButton_9.setEnabled(True)
            self.ui.pushButton_9.setStyleSheet("#pushButton_9{border-image: url(:/icons/icons/rightok.png);}\n"
                                               "#pushButton_9:hover{border-image: url(:/icons/icons/rightok1.png);}")

            with open('./prg/prg.txt', 'r+', encoding='UTF-8') as file:
                a = file.read()

            b = a.split('\n')
            c = self.ui.label.styleSheet()
            if c == "#label{\nimage: url(prg/original.png);}" or c == "#label{image: url(prg/original.png);}":
                    self.ui.pushButton_8.setEnabled(False)
                    self.ui.pushButton_8.setStyleSheet(
                    "#pushButton_8{border-image: url(:/icons/icons/closeleft.png);}")

            if c == "#label{\nimage: url(prg/"+b[-2]+");}" or c == "#label{image: url(prg/"+b[-2]+");}":
                x = self.ui.label.setStyleSheet(
                    "#label{image: url(prg/"+b[-3]+");}")
            elif c == "#label{\nimage: url(prg/"+b[-3]+");}" or c == "#label{image: url(prg/"+b[-3]+");}":
                x = self.ui.label.setStyleSheet(
                    "#label{image: url(prg/"+b[-4]+");}")
            elif c == "#label{\nimage: url(prg/"+b[-4]+");}" or c == "#label{image: url(prg/"+b[-4]+");}":
                x = self.ui.label.setStyleSheet(
                    "#label{image: url(prg/"+b[-5]+");}")
            elif c == "#label{\nimage: url(prg/"+b[-5]+");}" or c == "#label{image: url(prg/"+b[-5]+");}":
                x = self.ui.label.setStyleSheet(
                    "#label{image: url(prg/"+b[-6]+");}")
            elif c == "#label{\nimage: url(prg/"+b[-6]+");}" or c == "#label{image: url(prg/"+b[-6]+");}":
                x = self.ui.label.setStyleSheet(
                    "#label{image: url(prg/"+b[-7]+");}")
            elif c == "#label{\nimage: url(prg/"+b[-7]+");}" or c == "#label{image: url(prg/"+b[-7]+");}":
                x = self.ui.label.setStyleSheet(
                    "#label{image: url(prg/"+b[-8]+");}")
            elif c == "#label{\nimage: url(prg/"+b[-8]+");}" or c == "#label{image: url(prg/"+b[-8]+");}":
                x = self.ui.label.setStyleSheet(
                    "#label{image: url(prg/"+b[-9]+");}")
            elif c == "#label{\nimage: url(prg/"+b[-9]+");}" or c == "#label{image: url(prg/"+b[-9]+");}":
                x = self.ui.label.setStyleSheet(
                    "#label{image: url(prg/"+b[-10]+");}")
            elif c == "#label{\nimage: url(prg/"+b[-10]+");}" or c == "#label{image: url(prg/"+b[-10]+");}":
                x = self.ui.label.setStyleSheet(
                    "#label{image: url(prg/"+b[-11]+");}")
            else:
                QtWidgets.QMessageBox.information(
                    self, 'Hata', f'Maximum geri alma İşlemi veya sondasınız.')




        except Exception as err:
            with open('log.txt', 'a+', encoding='UTF-8') as file:
                file.write(str(err)+'\n')

    def go(self):
        try:
            self.ui.pushButton_8.setEnabled(True)
            self.ui.pushButton_8.setStyleSheet("#pushButton_8{border-image: url(:/icons/icons/leftok.png);}\n"
                                               "#pushButton_8:hover{border-image: url(:/icons/icons/leftok1.png);}")
            with open('./prg/prg.txt', 'r+', encoding='UTF-8') as file:
                a = file.read()

            b = a.split('\n')

            c = self.ui.label.styleSheet()

            if c == "#label{\nimage: url(prg/"+b[-3]+");}" or c == "#label{image: url(prg/"+b[-3]+");}":
                x = self.ui.label.setStyleSheet(
                    "#label{image: url(prg/"+b[-2]+");}")
            elif c == "#label{\nimage: url(prg/"+b[-4]+");}" or c == "#label{image: url(prg/"+b[-4]+");}":
                x = self.ui.label.setStyleSheet(
                    "#label{image: url(prg/"+b[-3]+");}")
            elif c == "#label{\nimage: url(prg/"+b[-5]+");}" or c == "#label{image: url(prg/"+b[-5]+");}":
                x = self.ui.label.setStyleSheet(
                    "#label{image: url(prg/"+b[-4]+");}")
            elif c == "#label{\nimage: url(prg/"+b[-6]+");}" or c == "#label{image: url(prg/"+b[-6]+");}":
                x = self.ui.label.setStyleSheet(
                    "#label{image: url(prg/"+b[-5]+");}")
            elif c == "#label{\nimage: url(prg/"+b[-7]+");}" or c == "#label{image: url(prg/"+b[-7]+");}":
                x = self.ui.label.setStyleSheet(
                    "#label{image: url(prg/"+b[-6]+");}")
            elif c == "#label{\nimage: url(prg/"+b[-8]+");}" or c == "#label{image: url(prg/"+b[-8]+");}":
                x = self.ui.label.setStyleSheet(
                    "#label{image: url(prg/"+b[-7]+");}")
            elif c == "#label{\nimage: url(prg/"+b[-9]+");}" or c == "#label{image: url(prg/"+b[-9]+");}":
                x = self.ui.label.setStyleSheet(
                    "#label{image: url(prg/"+b[-8]+");}")
            elif c == "#label{\nimage: url(prg/"+b[-10]+");}" or c == "#label{image: url(prg/"+b[-10]+");}":
                x = self.ui.label.setStyleSheet(
                    "#label{image: url(prg/"+b[-9]+");}")
            elif c == "#label{\nimage: url(prg/"+b[-11]+");}" or c == "#label{image: url(prg/"+b[-11]+");}":
                x = self.ui.label.setStyleSheet(
                    "#label{image: url(prg/"+b[-10]+");}")
            else:
                self.ui.pushButton_9.setEnabled(False)
                self.ui.pushButton_9.setStyleSheet(
                    "#pushButton_9{border-image: url(:/icons/icons/closeright.png);}")
                QtWidgets.QMessageBox.information(
                    self, 'Hata', f'Maximum ileri alma İşlemi veya sondasınız.')

        except Exception as err:
            with open('log.txt', 'a+', encoding='UTF-8') as file:
                file.write(str(err)+'\n')

    def reset(self):
        try:
            qclear = QtWidgets.QMessageBox.question(
                self, 'Sıfırlama', f'Devam Ederseniz tekrardan resminiz yüklenecek ve geçmiş silinecektir.', QtWidgets.QMessageBox.Ok | QtWidgets.QMessageBox.Cancel)
            if qclear == QtWidgets.QMessageBox.Ok:
                delprg()
                zz = Image.open(img[0])
                zz.save('prg/original.png')
                self.ui.label.setStyleSheet(
                    "#label{image: url(prg/original.png);}")
                print(img[0])
                with open('prg/prg.txt', 'a+', encoding='UTF-8') as file:
                    file.write('original.png'+'\n')
                self.ui.label.setStyleSheet(
                    "#label{image: url(prg/original.png);}")
                self.ui.pushButton_10.setEnabled(False)
                self.ui.pushButton_10.setStyleSheet(
                    "#pushButton_10{border-image: url(:/icons/icons/restartclose.png);}")
                self.ui.pushButton_9.setEnabled(False)
                self.ui.pushButton_9.setStyleSheet(
                    "#pushButton_9{border-image: url(:/icons/icons/closeright.png);}")
                self.ui.pushButton_8.setEnabled(False)
                self.ui.pushButton_8.setStyleSheet(
                    "#pushButton_8{border-image: url(:/icons/icons/closeleft.png);}")
        except Exception as err:
            with open('log.txt', 'a+', encoding='UTF-8') as file:
                file.write(str(err)+'\n')

    def exit(self):
        qclear = QtWidgets.QMessageBox.question(
            self, 'Uygulama Kapatma', f'Uygulamayı Kapatıyorsunuz işlemleriniz kayıt edilmemiş olabilir.Kapatmak istediğinize eminmisiniz?', QtWidgets.QMessageBox.Ok | QtWidgets.QMessageBox.Cancel)
        if qclear == QtWidgets.QMessageBox.Ok:
            app.exit()




def delprg():
    try:
        a = os.listdir('prg')

        for i in a:
            os.remove(f'prg/{i}')

        a = os.listdir('prg')
    except Exception as err:
        with open('log.txt', 'a+', encoding='UTF-8') as file:
            file.write(err)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    main = pth()
    app.setStyle('Fusion')
    app.exec_()
    if main.close() == True:
        delprg()
