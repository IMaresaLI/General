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
from veritabanı import Ui_MainWindow as b 
import sys
from dbconnect import *

class veriTBN(QtWidgets.QMainWindow):
    def __init__(self):
        super(veriTBN,self).__init__()
        self.vr = b()
        self.vr.setupUi(self)
        self.show()


        self.vr.pushButton.clicked.connect(self.tablecreateGRB)
        self.vr.pushButton_4.clicked.connect(self.tableDel)
        self.vr.pushButton_2.clicked.connect(self.datainsert)
        self.vr.pushButton_5.clicked.connect(self.datadel)
        self.vr.pushButton_6.clicked.connect(self.tableCreate)
        self.vr.pushButton_13.clicked.connect(self.gettablo)
        self.vr.pushButton_12.clicked.connect(self.tabledele)
        self.vr.pushButton_9.clicked.connect(self.gettablodata)
        self.vr.pushButton_11.clicked.connect(self.datainsert1)
        self.vr.pushButton_7.clicked.connect(self.gettablo3)
        self.vr.pushButton_3.clicked.connect(self.getdate)
        self.vr.pushButton_8.clicked.connect(self.deletedata)

        self.vr.checkBox.stateChanged.connect(self.selected)
        self.vr.checkBox_2.stateChanged.connect(self.selected)
        self.vr.checkBox_3.stateChanged.connect(self.selected)

        self.vr.checkBox_6.stateChanged.connect(self.selected2)
        self.vr.checkBox_7.stateChanged.connect(self.selected2)
        self.vr.checkBox_8.stateChanged.connect(self.selected2)





    def tablecreateGRB(self):
        tcg = self.vr.groupBox_2.isHidden()
        if tcg == True :
            self.vr.groupBox_2.setHidden(False)
        else :
            self.vr.groupBox_2.setHidden(True)

    def tableDel(self):
        tcg = self.vr.groupBox_6.isHidden()
        if tcg == True :
            self.vr.groupBox_6.setHidden(False)        
        else :
            self.vr.groupBox_6.setHidden(True)

    def datainsert(self):
        tcg = self.vr.groupBox_5.isHidden()
        if tcg == True :
            self.vr.groupBox_5.setHidden(False)        
        else :
            self.vr.groupBox_5.setHidden(True)
   
    def datadel(self):
        tcg = self.vr.groupBox_4.isHidden()
        if tcg == True :
            self.vr.groupBox_4.setHidden(False)        
        else :
            self.vr.groupBox_4.setHidden(True)

    def selected(self):
        cd = self.sender()
        print(cd.text())

    def selected2(self):
        self.sender()

    def tableCreate(self):
        tbn = self.vr.lineEdit.text()
        tbi = self.vr.lineEdit_2.text()
        tbi1 = self.vr.lineEdit_3.text()
        combo1 = self.vr.comboBox_3.currentText()
        combo2 = self.vr.comboBox_4.currentText()
        items = self.vr.groupBox_3.findChildren(QtWidgets.QCheckBox)
        items2 = self.vr.groupBox_7.findChildren(QtWidgets.QCheckBox)
        result = ''
        for i in items :
            if i.isChecked():
                result += i.text()+'\n'
        result2 = ''
        for i in items2 :
            if i.isChecked():
                result2 += i.text()+'\n'


        
        cursor.execute(f'CREATE TABLE {tbn} ({tbi} {combo1} {result} , {tbi1} {combo2} {result2})')

    def gettablo(self):
        
        cursor.execute('SELECT name from sqlite_master where type= "table"')
        c = cursor.fetchall()
        for i in c :
            self.vr.comboBox_5.addItems(i)

    def tabledele(self):
        x = self.vr.comboBox_5.currentText()
        cursor.execute(f'DROP table if exists {x}')

    def gettablodata(self):
        cursor.execute('SELECT name from sqlite_master where type= "table"')
        c = cursor.fetchall()
        for i in c :
            self.vr.comboBox_2.addItems(i)

    def datainsert1(self):
        c = self.vr.comboBox_2.currentText()
        z = self.vr.lineEdit_4.text()
        cursor.execute(f"INSERT INTO {c} VALUES(1,'{z}')")
        connection.commit()

    def gettablo3(self):
        cursor.execute('SELECT name from sqlite_master where type= "table"')
        rows = cursor.fetchall()
        for row in rows:
            self.vr.comboBox.addItems(row)

    def getdate(self):
        vv = self.vr.comboBox.currentText()
        cursor.execute(f'SELECT deneme3 FROM {vv} ')
        xx = cursor.fetchall()
        for i in xx:
            self.vr.comboBox_6.addItems(i)

    def deletedata(self):
        vv = self.vr.comboBox.currentText()
        us =self.vr.comboBox_6.currentText()
        cursor.execute(f'''DELETE FROM {vv} where deneme2=1''')
        connection.commit()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    main = veriTBN()
    app.exit(app.exec_())
