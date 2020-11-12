
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

from dbwork import *
from PyQt5 import QtWidgets
from PyQt5 import QtCore
from dbkayit import Ui_MainWindow as a
from reg_log import Ui_MainWindow as b
from anasayfa import Ui_MainWindow as c
import os
import sys
import time


class dbkyt(QtWidgets.QMainWindow):
    def __init__(self):
        super(dbkyt, self).__init__()
        self.dbk = a()
        self.dbk.setupUi(self)
        self.dbk.pushButton.clicked.connect(self.kayit)
        self.show()


    def kayit(self):
        try:
            hn = self.dbk.lineEdit.text()
            dbuser = self.dbk.lineEdit_2.text()
            dbpw = self.dbk.lineEdit_3.text()
            db = self.dbk.lineEdit_4.text()
            if hn == "" and dbuser == "" and dbpw == "" and db == "":
                self.dbk.textBrowser.setText(
                    'Lütfen Tüm Bilgileri Doldurunuz.')
            else:
                with open('dbwork.py', 'w+', encoding='UTF-8') as file:
                    file.write("import mysql.connector\n\n" +
                               f"connection = mysql.connector.connect(\n     host='{hn}',\n     user='{dbuser}',\n     password='{dbpw}',\n     database='{db}')"+"\ncursor = connection.cursor()")
                    self.dbk.textBrowser.setText(
                        'Database Bilgileri Dosyası Oluşturuldu.\ndbwork.py dosyasının içindeki bilgiler databaseye ile bağlantı kurmak içindir.')
                self.yenlog = logSc()
                self.yenlog.show()
                self.close()
        except Exception as err:
            print(str(err))


class logSc(QtWidgets.QMainWindow):
    def __init__(self):
        super(logSc, self).__init__()
        self.lg = b()
        self.lg.setupUi(self)

        self.lg.pushButton_3.clicked.connect(self.kytbtn)
        self.lg.pushButton_2.clicked.connect(self.grsbtn)
        self.lg.pushButton.clicked.connect(self.login)
        self.lg.pushButton_4.clicked.connect(self.reg)

    def kytbtn(self):
        x = self.lg.groupBox_2.isHidden()
        if x == True:
            self.lg.groupBox_2.setHidden(False)
            self.lg.pushButton_3.setEnabled(False)
            self.lg.groupBox.setHidden(True)
            self.lg.pushButton_2.setEnabled(True)
        else:
            self.lg.groupBox_2.setHidden(True)
            self.lg.pushButton_3.setEnabled(True)
            self.lg.groupBox.setHidden(True)

    def grsbtn(self):
        x = self.lg.groupBox.isHidden()
        if x == True:
            self.lg.groupBox.setHidden(False)
            self.lg.pushButton_2.setEnabled(False)
            self.lg.groupBox_2.setHidden(True)
            self.lg.pushButton_3.setEnabled(True)
        else:
            self.lg.groupBox.setHidden(True)
            self.lg.pushButton_2.setEnabled(True)
            self.lg.groupBox_2.setHidden(True)

    def login(self):
        try:
            usern = self.lg.lineEdit.text()
            paswd = self.lg.lineEdit_2.text()
            cb = self.lg.comboBox_2.currentText()
            sql = "SELECT * from users Where username=%s"
            value = (usern,)
            cursor.execute(sql, value)
            result = cursor.fetchone()

            if usern == '' and paswd == '':
                self.lg.textBrowser.setText('Tüm Bilgileri Doldurmadınız.')
            elif cb == 'Admin':
                if result[1] == usern and result[2] == paswd and result[3] == 'Admin':
                    self.lg.textBrowser.setText('Giriş Başarılı')
                    self.log = admK()
                    self.log.show()
                    self.close()

                elif result[1] == usern and result[2] == paswd and result[3] == 'User':
                    self.lg.textBrowser.setText(
                        'Giriş hesap yönetici hesabı değildir.')

                else:
                    self.lg.textBrowser.setText(
                        'Lütfen Bilgilerinizi Kontrol Edip tekrar giriş yapmayı deneyiniz.')
            elif cb == 'User':
                if result[1] == usern and result[2] == paswd and result[3] == 'Admin' or result[3] == 'User':
                    self.lg.textBrowser.setText('Giriş Başarılı')

                elif result[1] == usern and result[2] == paswd and result[3] == 'User':
                    self.lg.textBrowser.setText(
                        'Giriş hesap yönetici hesabı değildir.')

                else:
                    self.lg.textBrowser.setText(
                        'Lütfen Bilgilerinizi Kontrol Edip tekrar giriş yapmayı deneyiniz.')
        except Exception as err:
            print(str(err))

    def reg(self):
        try:
            usern = self.lg.lineEdit_3.text()
            paswd = self.lg.lineEdit_4.text()
            role = 'User'

            if usern == '' and paswd == '':
                self.lg.textBrowser_2.setText('Lütfen Tüm Bilgileri giriniz.')
            else:
                sql = 'INSERT INTO users(username,password,role) VALUES (%s,%s,%s)'
                values = (usern, paswd, role)
                cursor.execute(sql, values)
                connection.commit()

                self.lg.textBrowser_2.setText('Kayıt işlemi tamamlandı.')
        except Exception as err:
            print(str(err))


class admK(QtWidgets.QMainWindow):
    def __init__(self):
        super(admK, self).__init__()
        self.adm = c()
        self.adm.setupUi(self)

        self.adm.pushButton_17.clicked.connect(self.kullK)
        self.adm.pushButton_18.clicked.connect(self.veriG)
        self.adm.pushButton.clicked.connect(self.knE)
        self.adm.pushButton_2.clicked.connect(self.knG)
        self.adm.pushButton_3.clicked.connect(self.KnS)
        self.adm.pushButton_4.clicked.connect(self.kE)
        self.adm.pushButton_19.clicked.connect(self.kbg)
        self.adm.pushButton_5.clicked.connect(self.kg)
        self.adm.pushButton_6.clicked.connect(self.ks)
        self.adm.pushButton_7.clicked.connect(self.veris)
        self.adm.pushButton_12.clicked.connect(self.listveri)
        self.adm.pushButton_8.clicked.connect(self.verEk)
        self.adm.pushButton_20.clicked.connect(self.veriEkl)
        self.adm.pushButton_9.clicked.connect(self.veriGNC)
        self.adm.pushButton_10.clicked.connect(self.verial)
        self.adm.pushButton_15.clicked.connect(self.verignc)
        self.adm.pushButton_13.clicked.connect(self.veris2)
        self.adm.pushButton_16.clicked.connect(self.versil)

    def kullK(self):
        KK = self.adm.groupBox.isHidden()
        if KK == True:
            self.adm.groupBox.setHidden(False)
            self.adm.groupBox_2.setHidden(False)
            self.adm.groupBox_3.setHidden(True)
            self.adm.groupBox_4.setHidden(True)
            self.adm.groupBox_5.setHidden(True)
            self.adm.pushButton.setEnabled(False)
            self.adm.pushButton_17.setEnabled(False)
            self.adm.pushButton_18.setEnabled(True)
            self.adm.pushButton_2.setEnabled(True)
            self.adm.pushButton_3.setEnabled(True)

        else:
            self.adm.groupBox.setHidden(True)
            self.adm.groupBox_5.setHidden(True)
            self.adm.pushButton.setEnabled(True)
            self.adm.pushButton_17.setEnabled(True)
            self.adm.pushButton_18.setEnabled(True)

    def knE(self):
        ilg = self.adm.groupBox_2.isHidden()
        if ilg == True:
            self.adm.groupBox_2.setHidden(False)
            self.adm.groupBox_3.setHidden(True)
            self.adm.groupBox_4.setHidden(True)
            self.adm.pushButton.setEnabled(False)
            self.adm.pushButton_2.setEnabled(True)
            self.adm.pushButton_3.setEnabled(True)
        else:
            self.adm.groupBox_2.setHidden(True)
            self.adm.groupBox_3.setHidden(True)
            self.adm.groupBox_4.setHidden(True)
            self.adm.pushButton.setEnabled(True)
            self.adm.pushButton_2.setEnabled(True)
            self.adm.pushButton_3.setEnabled(True)

    def kE(self):
        try:
            userN = self.adm.lineEdit.text()
            pssW = self.adm.lineEdit_2.text()
            coM = self.adm.comboBox.currentText()
            if userN == '' or pssW == '' or coM == '':
                self.adm.textBrowser.setText('Tüm Bilgileri Giriniz.')
            else:
                sql = 'INSERT INTO users(username,password,role) VALUES (%s,%s,%s)'
                values = (userN, pssW, coM)
                cursor.execute(sql, values)
                connection.commit()
                self.adm.textBrowser.setText('Veri Tabanına Ekleme Yapıldı.')
                userN = self.adm.lineEdit.clear()
                pssW = self.adm.lineEdit_2.clear()
        except Exception as err:
            print(str(err))

    def knG(self):
        try:
            kG = self.adm.groupBox_3.isHidden()
            if kG == True:
                self.adm.comboBox_4.clear()
                self.adm.groupBox_3.setHidden(False)
                self.adm.groupBox_2.setHidden(True)
                self.adm.groupBox_4.setHidden(True)
                self.adm.pushButton.setEnabled(True)
                self.adm.pushButton_2.setEnabled(False)
                self.adm.pushButton_3.setEnabled(True)
                sql = 'SELECT * from users'
                cursor.execute(sql)
                c = cursor.fetchall()
                list = []
                for i in c:
                    list.append(i[1])
                self.adm.comboBox_4.addItems(list)
                self.adm.lineEdit_4.clear()
                self.adm.lineEdit_3.clear()
            else:
                self.adm.comboBox_4.clear()
                self.adm.groupBox_2.setHidden(True)
                self.adm.groupBox_3.setHidden(True)
                self.adm.groupBox_4.setHidden(True)
                self.adm.pushButton.setEnabled(True)
                self.adm.pushButton_2.setEnabled(True)
                self.adm.pushButton_3.setEnabled(True)
        except Exception as err:
            print(str(err))

    def kbg(self):
        try:
            username = self.adm.comboBox_4.currentText()
            sql = 'SELECT * From users Where username = %s'
            value = (username,)
            cursor.execute(sql, value)
            a = cursor.fetchone()
            self.adm.lineEdit_4.setText(a[1])
            self.adm.lineEdit_3.setText(a[2])
            self.adm.comboBox_2.setEditText(a[3])
        except Exception as err:
            print(str(err))

    def kg(self):
        try:
            usercb = self.adm.comboBox_4.currentText()
            username = self.adm.lineEdit_4.text()
            passwd = self.adm.lineEdit_3.text()
            role = self.adm.comboBox_2.currentText()
            if username == '' or passwd == '':
                pass
            else:
                sql1 = 'Update users Set username = %s, password = %s, role = %s where username = %s'
                values1 = (username, passwd, role, usercb)
                cursor.execute(sql1, values1)
                connection.commit()
                self.adm.lineEdit_4.clear()
                self.adm.lineEdit_3.clear()
                self.adm.textBrowser_2.setText(
                    f'{usercb} adlı kullanıcı güncellendi.')
        except Exception as err:
            print(str(err))

    def KnS(self):
        try:
            kG = self.adm.groupBox_4.isHidden()
            if kG == True:
                self.adm.listWidget.clear()
                self.adm.groupBox_4.setHidden(False)
                self.adm.groupBox_2.setHidden(True)
                self.adm.groupBox_3.setHidden(True)
                self.adm.pushButton.setEnabled(True)
                self.adm.pushButton_2.setEnabled(True)
                self.adm.pushButton_3.setEnabled(False)
                currentIndex = self.adm.listWidget.currentRow()
                sql = 'SELECT * from users'
                cursor.execute(sql)
                c = cursor.fetchall()
                list = []
                for i in c:
                    list.append(i[1])
                self.adm.listWidget.insertItems(currentIndex, list)
            else:
                self.adm.groupBox_2.setHidden(True)
                self.adm.groupBox_3.setHidden(True)
                self.adm.groupBox_4.setHidden(True)
                self.adm.pushButton.setEnabled(True)
                self.adm.pushButton_2.setEnabled(True)
                self.adm.pushButton_3.setEnabled(True)
        except Exception as err:
            print(str(err))

    def ks(self):
        try:
            index = self.adm.listWidget.currentRow()
            item = self.adm.listWidget.item(index)
            select = self.adm.listWidget.currentItem().text()
            sql = 'DELETE From users Where username = %s'
            value = (select,)
            cursor.execute(sql, value)
            connection.commit()
            item = self.adm.listWidget.takeItem(index)
            del item
            self.adm.textBrowser_3.setText(
                f"{select} isimli kullanıcı veritabanından silindi.")
        except Exception as err:
            print(str(err))

    def veriG(self):
        KK = self.adm.groupBox_5.isHidden()
        if KK == True:
            self.adm.groupBox_5.setHidden(False)
            self.adm.groupBox_2.setHidden(False)
            self.adm.groupBox_3.setHidden(True)
            self.adm.groupBox_4.setHidden(True)
            self.adm.groupBox.setHidden(True)
            self.adm.pushButton_17.setEnabled(True)
            self.adm.pushButton_18.setEnabled(False)
            self.adm.pushButton_7.setEnabled(False)
        else:
            self.adm.groupBox.setHidden(True)
            self.adm.groupBox_5.setHidden(True)
            self.adm.pushButton.setEnabled(True)
            self.adm.pushButton_17.setEnabled(True)
            self.adm.pushButton_18.setEnabled(True)

    def veris(self):
        self.adm.comboBox_3.clear()
        kG = self.adm.groupBox_8.isHidden()
        if kG == True:
            self.adm.groupBox_8.setHidden(False)
            self.adm.groupBox_12.setHidden(True)
            self.adm.groupBox_11.setHidden(True)
            self.adm.groupBox_10.setHidden(True)
            self.adm.pushButton_9.setEnabled(True)
            self.adm.pushButton_8.setEnabled(True)
            self.adm.pushButton_7.setEnabled(False)
            self.adm.pushButton_13.setEnabled(True)
        else:
            self.adm.groupBox_8.setHidden(True)
            self.adm.groupBox_12.setHidden(True)
            self.adm.groupBox_11.setHidden(True)
            self.adm.groupBox_10.setHidden(True)
            self.adm.pushButton_9.setEnabled(True)
            self.adm.pushButton_8.setEnabled(True)
            self.adm.pushButton_7.setEnabled(True)
            self.adm.pushButton_13.setEnabled(True)

    def listveri(self):
        try:
            self.adm.tableWidget.clear()
            sql = f'SELECT * FROM phones'
            cursor.execute(sql,)
            a = cursor.fetchall()
            self.adm.tableWidget.setRowCount(len(a))
            self.adm.tableWidget.setColumnCount(len(cursor.description))
            self.adm.tableWidget.setHorizontalHeaderLabels(
                [i[0] for i in cursor.description])

            rows = 0
            rowIndex = 0
            zx = self.adm.lineEdit_5.text()
            if zx == '':
                for re in a:
                    if rows != len(a):
                        are = [
                            {
                                'id': f'{re[0]}',
                                'phonenames': f'{re[1]}',
                                'phonebrand': f'{re[2]}',
                                'phonerning': f'{re[3]}'}
                        ]

                        rows += 1

                        for i in are:
                            self.adm.tableWidget.setItem(
                                rowIndex, 0, QtWidgets.QTableWidgetItem(i['id']))
                            self.adm.tableWidget.setItem(
                                rowIndex, 1, QtWidgets.QTableWidgetItem(i['phonenames']))
                            self.adm.tableWidget.setItem(
                                rowIndex, 2, QtWidgets.QTableWidgetItem(i['phonebrand']))
                            self.adm.tableWidget.setItem(
                                rowIndex, 3, QtWidgets.QTableWidgetItem(i['phonerning']))

                            rowIndex += 1

            else:
                cursor.execute(
                    f"SELECT * From phones Where phonenames LIKE '%{zx}%'" or f"SELECT * From phones Where phonebrand LIKE '%{zx}%'")
                ft = cursor.fetchall()
                for re in ft:
                    if rows != len(ft):
                        are = [
                            {
                                'id': f'{re[0]}',
                                'phonenames': f'{re[1]}',
                                'phonebrand': f'{re[2]}',
                                'phonerning': f'{re[3]}'}
                        ]

                        rows += 1

                        for i in are:
                            self.adm.tableWidget.setItem(
                                rowIndex, 0, QtWidgets.QTableWidgetItem(i['id']))
                            self.adm.tableWidget.setItem(
                                rowIndex, 1, QtWidgets.QTableWidgetItem(i['phonenames']))
                            self.adm.tableWidget.setItem(
                                rowIndex, 2, QtWidgets.QTableWidgetItem(i['phonebrand']))
                            self.adm.tableWidget.setItem(
                                rowIndex, 3, QtWidgets.QTableWidgetItem(i['phonerning']))
                            rowIndex += 1
        except Exception as err:
            print(str(err))

    def verEk(self):
        kG = self.adm.groupBox_12.isHidden()
        if kG == True:
            self.adm.groupBox_12.setHidden(False)
            self.adm.groupBox_8.setHidden(True)
            self.adm.groupBox_11.setHidden(True)
            self.adm.groupBox_10.setHidden(True)
            self.adm.pushButton_9.setEnabled(True)
            self.adm.pushButton_8.setEnabled(False)
            self.adm.pushButton_7.setEnabled(True)
            self.adm.pushButton_13.setEnabled(True)
        else:
            self.adm.groupBox_12.setHidden(True)
            self.adm.groupBox_8.setHidden(True)
            self.adm.groupBox_11.setHidden(True)
            self.adm.groupBox_10.setHidden(True)
            self.adm.pushButton_9.setEnabled(True)
            self.adm.pushButton_8.setEnabled(True)
            self.adm.pushButton_7.setEnabled(True)
            self.adm.pushButton_13.setEnabled(True)

    def veriEkl(self):
        try:
            phoneN = self.adm.lineEdit_12.text()
            phoneB = self.adm.lineEdit_13.text()
            phoneE = self.adm.lineEdit_14.text()
            sql = 'INSERT INTO phones (phonenames,phonebrand,phonearnings) VALUES (%s,%s,%s)'
            values = (phoneN, phoneB, phoneE)
            cursor.execute(sql, values)
            connection.commit()
            self.adm.lineEdit_12.clear()
            self.adm.lineEdit_13.clear()
            self.adm.lineEdit_14.clear()
            self.adm.textBrowser_10.setText(f"{phoneN} adlı veri eklendi.")
        except Exception as err:
            print(str(err))

    def veriGNC(self):
        try:
            self.adm.comboBox_3.clear()
            kG = self.adm.groupBox_10.isHidden()
            if kG == True:
                self.adm.groupBox_10.setHidden(False)
                self.adm.groupBox_8.setHidden(True)
                self.adm.groupBox_11.setHidden(True)
                self.adm.groupBox_12.setHidden(True)
                self.adm.pushButton_8.setEnabled(True)
                self.adm.pushButton_9.setEnabled(False)
                self.adm.pushButton_7.setEnabled(True)
                self.adm.pushButton_13.setEnabled(True)
                sql = 'Select * from phones'
                cursor.execute(sql)
                c = cursor.fetchall()
                list = []
                for i in c:
                    list.append(i[1])
                self.adm.comboBox_3.addItems(list)
            else:
                self.adm.groupBox_12.setHidden(True)
                self.adm.groupBox_8.setHidden(True)
                self.adm.groupBox_11.setHidden(True)
                self.adm.groupBox_10.setHidden(True)
                self.adm.pushButton_9.setEnabled(True)
                self.adm.pushButton_8.setEnabled(True)
                self.adm.pushButton_7.setEnabled(True)
                self.adm.pushButton_13.setEnabled(True)
        except Exception as err:
            print(str(err))

    def verial(self):
        try:
            scb = self.adm.comboBox_3.currentText()
            sql = 'Select * From phones Where phonenames = %s'
            value = (scb,)
            cursor.execute(sql, value)
            cc = cursor.fetchone()

            self.adm.lineEdit_9.setText(cc[1])
            self.adm.lineEdit_10.setText(cc[2])
            self.adm.lineEdit_11.setText(cc[3])
        except Exception as err:
            print(str(err))

    def verignc(self):
        try:
            scb = self.adm.comboBox_3.currentText()
            phoneN = self.adm.lineEdit_9.text()
            phoneB = self.adm.lineEdit_10.text()
            phoneE = self.adm.lineEdit_11.text()
            sql = 'UPDATE phones set phonenames=%s,phonebrand=%s,phonearnings=%s Where phonenames=%s'
            values = (phoneN, phoneB, phoneE, scb)
            cursor.execute(sql, values)
            connection.commit()
            self.adm.textBrowser_8.setText(f'{phoneN} isimli veri güncelleri')
            self.adm.lineEdit_9.clear()
            self.adm.lineEdit_10.clear()
            self.adm.lineEdit_11.clear()
        except Exception as err:
            print(str(err))

    def veris2(self):
        try:
            self.adm.comboBox_3.clear()
            kG = self.adm.groupBox_11.isHidden()
            if kG == True:
                currentIndex = self.adm.listWidget_2.currentRow()
                self.adm.groupBox_11.setHidden(False)
                self.adm.groupBox_8.setHidden(True)
                self.adm.groupBox_10.setHidden(True)
                self.adm.groupBox_12.setHidden(True)
                self.adm.pushButton_8.setEnabled(True)
                self.adm.pushButton_9.setEnabled(True)
                self.adm.pushButton_7.setEnabled(True)
                self.adm.pushButton_13.setEnabled(False)
                sql = 'Select * from phones'
                cursor.execute(sql)
                c = cursor.fetchall()
                list = []
                for i in c:
                    list.append(i[1])
                self.adm.listWidget_2.insertItems(currentIndex, list)
            else:
                self.adm.groupBox_12.setHidden(True)
                self.adm.groupBox_8.setHidden(True)
                self.adm.groupBox_11.setHidden(True)
                self.adm.groupBox_10.setHidden(True)
                self.adm.pushButton_9.setEnabled(True)
                self.adm.pushButton_8.setEnabled(True)
                self.adm.pushButton_7.setEnabled(True)
                self.adm.pushButton_13.setEnabled(True)
        except Exception as err:
            print(str(err))

    def versil(self):
        try:
            index = self.adm.listWidget_2.currentRow()
            item = self.adm.listWidget_2.item(index)
            select = self.adm.listWidget_2.currentItem().text()
            sql = 'DELETE From phones Where phonenames = %s'
            value = (select,)
            cursor.execute(sql, value)
            connection.commit()
            item = self.adm.listWidget_2.takeItem(index)
            del item
            self.adm.textBrowser_9.setText(
                f"{select} isimli veri veritabanından silindi.")
        except Exception as err:
            print(str(err))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    main = dbkyt()
    app.setStyle('Fusion')
    app.exit(app.exec_())
	cunsor.close()
