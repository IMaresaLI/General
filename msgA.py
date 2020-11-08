from PyQt5 import QtWidgets
from PyQt5 import QtCore
from msgsfr import Ui_MainWindow as bb
import sys
import time


class msgAn(QtWidgets.QMainWindow):
    def __init__(self):
        super(msgAn,self).__init__()
        self.ms = bb()
        self.ms.setupUi(self)
        self.show()

        self.ms.pushButton_2.clicked.connect(self.sifreleme)
        self.ms.pushButton_3.clicked.connect(self.sifrelemecozme)
        self.ms.pushButton.clicked.connect(self.sifrele)
        self.ms.pushButton_6.clicked.connect(self.sifreCZM)

    def sifreleme(self):
        if self.ms.groupBox.isHidden() == True:
            self.ms.groupBox.setHidden(False)
            self.ms.groupBox_2.setHidden(True)
            self.resize(610, 494)
        else:
            self.ms.groupBox.setHidden(True)
            self.ms.groupBox_2.setHidden(True)
            self.resize(610, 494)

    def sifrele(self):
        Kaynak = 'qazwsxedcrfvtgbyhnujmıköolçpşğiü1234567890'
        Hedef = 'ЂЃЅЇгджйклпфхцчшъыьэюёђѓєљњћќџҐҖ¦¨©ª«¬®¯±¶'
        Hedef2 = 'μκτλνιφςθϜͲωηξζσἦορψχσυδȣγϘβαΞπεΩΣϡͰΛбЭ우њ♆'
        Hedef3 = '#+%^<>&/@€₺-?*◑◆卐㊣Ψ∑ζ◎ʊ回¿℃☿♀♆♪۞☄✮✹☻㊝☇☉￠ㄨ￥☪'

        cb = self.ms.comboBox.currentText()
        if cb == 'Basit':
            cevirme = str.maketrans(Kaynak,Hedef)
            metin = self.ms.textEdit.toPlainText()
            a = metin.translate(cevirme)
            print(a)
            c = cb.translate(cevirme)
            self.ms.textBrowser.setText(c+':' + a)
        elif cb == 'Orta':
            cevirme = str.maketrans(Kaynak,Hedef)
            cevirme2 = str.maketrans(Hedef,Hedef2)
            metin = self.ms.textEdit.toPlainText()
            a = metin.translate(cevirme)
            print(a)
            oa = a.translate(cevirme2)
            print(oa)
            c = cb.translate(cevirme)
            self.ms.textBrowser.setText(c+':' + oa)
        elif cb == 'Zor':
            cevirme = str.maketrans(Kaynak,Hedef)
            cevirme2 = str.maketrans(Hedef,Hedef2)
            cevirme3 = str.maketrans(Hedef2,Hedef3)
            metin = self.ms.textEdit.toPlainText()
            a = metin.translate(cevirme)
            print(a)
            oa = a.translate(cevirme2)
            print(oa)
            zoa = oa.translate(cevirme3)
            print(zoa)
            c = cb.translate(cevirme)
            self.ms.textBrowser.setText(c+':'+zoa)

    def sifrelemecozme(self):
        if self.ms.groupBox_2.isHidden() == True:
            self.ms.groupBox_2.setHidden(False)
            self.ms.groupBox.setHidden(True)
            self.resize(610, 494)
        else:
            self.ms.groupBox_2.setHidden(True)
            self.ms.groupBox.setHidden(True)
            self.resize(610, 494)
    
    def sifreCZM(self):
        Kaynak = 'qazwsxedcrfvtgbyhnujmıköolçpşğiü1234567890'
        Hedef = 'ЂЃЅЇгджйклпфхцчшъыьэюёђѓєљњћќџҐҖ¦¨©ª«¬®¯±¶'
        Hedef2 = 'μκτλνιφςθϜͲωηξζσἦορψχσυδȣγϘβαΞπεΩΣϡͰΛбЭ우њ♆'
        Hedef3 = '#+%^<>&/@€₺-?*◑◆卐㊣Ψ∑ζ◎ʊ回¿℃☿♀♆♪۞☄✮✹☻㊝☇☉￠ㄨ￥☪'

        a = self.ms.textEdit_2.toPlainText()
        print(a)
        c = a.split(':')
        print(c)
        cevirme = str.maketrans(Hedef,Kaynak)
        b = c[0].translate(cevirme)
        print(b)


        if b == 'Basit':
            cevirme = str.maketrans(Hedef,Kaynak)
            metin = c[1]
            a = metin.translate(cevirme)
            self.ms.textBrowser_2.setText(a)
        elif b == 'Orta':
            cevirme2 = str.maketrans(Hedef2,Hedef)
            cevirme = str.maketrans(Hedef,Kaynak)
            metin = c[1]
            mt1 = metin.translate(cevirme2)
            mt2 = mt1.translate(cevirme)
            self.ms.textBrowser_2.setText(mt2)
        elif b == 'Zor':
            cevirme3 = str.maketrans(Hedef3,Hedef2) 
            cevirme2 = str.maketrans(Hedef2,Hedef)
            cevirme = str.maketrans(Hedef,Kaynak)
            metin = c[1]
            mt1 = metin.translate(cevirme3)
            mt2 = mt1.translate(cevirme2)
            mt3 = mt2.translate(cevirme)
            self.ms.textBrowser_2.setText(mt3)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    main = msgAn()
    app.setStyle('Fusion')
    app.exit(app.exec_())