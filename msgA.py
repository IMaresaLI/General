from PyQt5 import QtWidgets
from PyQt5 import QtCore
from msgsfr import Ui_MainWindow as bb
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import sys
import time
import json
import threading


class msgAn(QtWidgets.QMainWindow):
    def __init__(self):
        super(msgAn,self).__init__()
        self.ms = bb()
        self.ms.setupUi(self)
        self.show()

        self.ms.pushButton_2.clicked.connect(self.sifreleme)
        self.ms.pushButton_3.clicked.connect(self.sifrelemecozme)
        self.ms.pushButton_4.clicked.connect(self.E_postaGNR)
        self.ms.pushButton.clicked.connect(self.sifrele)
        self.ms.pushButton_6.clicked.connect(self.sifreCZM)
        self.ms.pushButton_9.clicked.connect(self.msgGND)
        self.ms.checkBox.stateChanged.connect(self.show_state)
        self.ms.pushButton_8.clicked.connect(self.TmsgSend)

    def show_state(self):
        self.sender()
        if self.ms.checkBox.isChecked() == True :
            self.ms.comboBox_3.setHidden(False)
        else :
            self.ms.comboBox_3.setHidden(True)

    def sifreleme(self):
        if self.ms.groupBox.isHidden() == True:
            self.ms.groupBox.setHidden(False)
            self.ms.groupBox_2.setHidden(True)
            self.ms.groupBox_4.setHidden(True)
            self.ms.groupBox_3.setHidden(True)
            self.resize(610, 494)
        else:
            self.ms.groupBox.setHidden(True)
            self.ms.groupBox_2.setHidden(True)
            self.ms.groupBox_4.setHidden(True)
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
            self.ms.groupBox_4.setHidden(True)
            self.resize(610, 494)
            self.ms.groupBox_3.setHidden(True)
        else:
            self.ms.groupBox_2.setHidden(True)
            self.ms.groupBox.setHidden(True)
            self.ms.groupBox_4.setHidden(True)
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

    def E_postaGNR(self):
        if self.ms.groupBox_4.isHidden() == True:
            self.ms.groupBox_4.setHidden(False)
            self.ms.groupBox.setHidden(True)
            self.ms.groupBox_2.setHidden(True)
            self.ms.groupBox_4.resize(481,471)
            self.resize(610, 524)
        else:
            self.ms.groupBox_4.setHidden(True)
            self.ms.groupBox.setHidden(True)
            self.ms.groupBox_2.setHidden(True)
            self.resize(610, 494)

    def msgGND(self):
        cobC =self.ms.comboBox_5.currentText()
        if cobC == 'Tekil Gönderim':
            self.ms.comboBox_4.setHidden(False)
            self.ms.pushButton_10.setHidden(False)
            self.ms.groupBox_4.resize(781,471)
            self.resize(917, 540)
            self.ms.groupBox_3.setHidden(False)
            self.ms.label_8.setText('Alıcı E-mail :')
            self.ms.label_8.setGeometry(160, 90, 61, 31)
            self.ms.lineEdit.setReadOnly(False)
            self.ms.pushButton_10.setHidden(True)
        elif cobC == 'Çoğul Gönderim':
            self.ms.groupBox_4.resize(781,471)
            self.resize(917, 540)
            self.ms.groupBox_3.setHidden(False)
            self.ms.comboBox_4.setHidden(True)
            self.ms.pushButton_10.setHidden(False)
            self.ms.label_8.setText('Alıcı E-mail Dosyası :')
            self.ms.label_8.setGeometry(130,90,101,31)
            self.ms.lineEdit.setReadOnly(True)

    def TmsgSend(self):
        try:
            Kaynak = 'qazwsxedcrfvtgbyhnujmıköolçpşğiü1234567890'
            Hedef = 'ЂЃЅЇгджйклпфхцчшъыьэюёђѓєљњћќџҐҖ¦¨©ª«¬®¯±¶'
            Hedef2 = 'μκτλνιφςθϜͲωηξζσἦορψχσυδȣγϘβαΞπεΩΣϡͰΛбЭ우њ♆'
            Hedef3 = '#+%^<>&/@€₺-?*◑◆卐㊣Ψ∑ζ◎ʊ回¿℃☿♀♆♪۞☄✮✹☻㊝☇☉￠ㄨ￥☪'

            x = self.ms.comboBox_5.currentText()
            if x == 'Tekil Gönderim':
                email = self.ms.lineEdit_4.text()
                self.ms.lineEdit_4.setEnabled(False)            
                paswd = self.ms.lineEdit_3.text()
                self.ms.lineEdit_3.setEnabled(False)            
                Aemail = self.ms.lineEdit.text()
                self.ms.lineEdit.setEnabled(False)
                emailS = self.ms.comboBox_4.currentText()
                self.ms.comboBox_4.setEnabled(False)
                konu = self.ms.lineEdit_2.text()
                self.ms.lineEdit_2.setEnabled(False)  
                mesaj = self.ms.textEdit_4.toPlainText()
                self.ms.textEdit_4.setEnabled(False)  
                if self.ms.comboBox_3.isHidden() == False:
                    cb = self.ms.comboBox_3.currentText()
                    if cb == 'Basit':
                        cevirme = str.maketrans(Kaynak,Hedef)
                        metin = konu
                        x = metin.translate(cevirme)
                        y = cb.translate(cevirme)
                        sifreliKN = (y+':'+x)   

                        cevirme = str.maketrans(Kaynak,Hedef)
                        metin = mesaj
                        a = metin.translate(cevirme)
                        c = cb.translate(cevirme)
                        sifreliMSG = (c+':'+a)

                        mail = smtplib.SMTP('smtp-mail.outlook.com',587)
                        mail.ehlo()
                        mail.starttls()
                        mail.login(f"{email}",f"{paswd}")

                        mesaj = MIMEMultipart()
                        mesaj['From'] = f"{email}"
                        mesaj['To'] = f'{Aemail}{emailS}'

                        mesaj['subject'] = f'{sifreliKN}'

                        body = f'''

                            {sifreliMSG}

                        '''
                        body_text = MIMEText(body,'plain')
                        mesaj.attach(body_text)

                        mail.sendmail(mesaj['From'],mesaj['To'],mesaj.as_string())
                        self.ms.textBrowser_4.setText(f'Mail Başarılı bir şekilde {Aemail}{emailS} kişisine ulaştırıldı.')
                        QtWidgets.QMessageBox.information(self,'Gönderme Onayı','Kişiye Başarılı bir şekilde gönderildi.')
                        self.ms.lineEdit_4.clear()
                        self.ms.lineEdit_4.setEnabled(True)            
                        self.ms.lineEdit_3.clear()
                        self.ms.lineEdit_3.setEnabled(True)            
                        self.ms.lineEdit.clear()
                        self.ms.lineEdit.setEnabled(True)
                        self.ms.comboBox_4.setEnabled(True)
                        self.ms.lineEdit_2.clear()
                        self.ms.lineEdit_2.setEnabled(True)  
                        self.ms.textEdit_4.clear()
                        self.ms.textEdit_4.setEnabled(True)
                    elif cb == 'Orta':
                        try:
                            cevirme = str.maketrans(Kaynak,Hedef)
                            cevirme2 = str.maketrans(Hedef,Hedef2)
                            metin = konu
                            x = metin.translate(cevirme)
                            oa = x.translate(cevirme2)
                            y = cb.translate(cevirme)
                            sifreliKN = (y+':'+oa)

                            cevirme = str.maketrans(Kaynak,Hedef)
                            cevirme2 = str.maketrans(Hedef,Hedef2)
                            metin = mesaj
                            a = metin.translate(cevirme)
                            ox = a.translate(cevirme2)
                            c = cb.translate(cevirme)
                            sifreliMSG = (c+':'+ox)

                            mail = smtplib.SMTP('smtp-mail.outlook.com',587)
                            mail.ehlo()
                            mail.starttls()
                            mail.login(f"{email}",f"{paswd}")

                            mesaj = MIMEMultipart()
                            mesaj['From'] = f"{email}"
                            mesaj['To'] = f'{Aemail}{emailS}'

                            mesaj['subject'] = f'{sifreliKN}'

                            body = f'''

                                {sifreliMSG}

                            '''
                            body_text = MIMEText(body,'plain')
                            mesaj.attach(body_text)

                            mail.sendmail(mesaj['From'],mesaj['To'],mesaj.as_string())
                            self.ms.textBrowser_4.setText(f'Mail Başarılı bir şekilde {Aemail}{emailS} kişisine ulaştırıldı.')
                            QtWidgets.QMessageBox.information(self,'Gönderme Onayı','Kişiye Başarılı bir şekilde gönderildi.')
                            self.ms.lineEdit_4.clear()
                            self.ms.lineEdit_4.setEnabled(True)            
                            self.ms.lineEdit_3.clear()
                            self.ms.lineEdit_3.setEnabled(True)            
                            self.ms.lineEdit.clear()
                            self.ms.lineEdit.setEnabled(True)
                            self.ms.comboBox_4.setEnabled(True)
                            self.ms.lineEdit_2.clear()
                            self.ms.lineEdit_2.setEnabled(True)  
                            self.ms.textEdit_4.clear()
                            self.ms.textEdit_4.setEnabled(True)
                        except Exception as err:
                            print(str(err))
                            self.ms.textBrowser_4.setText('Şifre Yanlış')
                            self.ms.lineEdit_4.setEnabled(True)            
                            self.ms.lineEdit_3.setEnabled(True)            
                            self.ms.lineEdit.setEnabled(True)
                            self.ms.comboBox_4.setEnabled(True)
                            self.ms.lineEdit_2.setEnabled(True)  
                            self.ms.textEdit_4.setEnabled(True)
                    elif cb == 'Zor':
                        cevirme = str.maketrans(Kaynak,Hedef)
                        cevirme2 = str.maketrans(Hedef,Hedef2)
                        cevirme3 = str.maketrans(Hedef2,Hedef3)
                        metin = konu
                        x = metin.translate(cevirme)
                        oa = x.translate(cevirme2)
                        yoa = oa.translate(cevirme3)

                        y = cb.translate(cevirme)
                        sifreliKN = (y+':'+yoa)

                        cevirme = str.maketrans(Kaynak,Hedef)
                        cevirme2 = str.maketrans(Hedef,Hedef2)
                        cevirme3 = str.maketrans(Hedef2,Hedef3)
                        metin = mesaj
                        a = metin.translate(cevirme)
                        ox = a.translate(cevirme2)
                        xox = ox.translate(cevirme3)

                        c = cb.translate(cevirme)
                        sifreliMSG = (c+':'+xox)
                        
                        mail = smtplib.SMTP('smtp-mail.outlook.com',587)
                        mail.ehlo()
                        mail.starttls()
                        mail.login(f"{email}",f"{paswd}")

                        mesaj = MIMEMultipart()
                        mesaj['From'] = f"{email}"
                        mesaj['To'] = f'{Aemail}{emailS}'

                        mesaj['subject'] = f'{sifreliKN}'

                        body = f'''

                            {sifreliMSG}

                        '''
                        body_text = MIMEText(body,'plain')
                        mesaj.attach(body_text)

                        mail.sendmail(mesaj['From'],mesaj['To'],mesaj.as_string())
                        self.ms.textBrowser_4.setText(f'Mail Başarılı bir şekilde {Aemail}{emailS} kişisine ulaştırıldı.')
                        QtWidgets.QMessageBox.information(self,'Gönderme Onayı','Kişiye Başarılı bir şekilde gönderildi.')
                        self.ms.lineEdit_4.clear()
                        self.ms.lineEdit_4.setEnabled(True)            
                        self.ms.lineEdit_3.clear()
                        self.ms.lineEdit_3.setEnabled(True)            
                        self.ms.lineEdit.clear()
                        self.ms.lineEdit.setEnabled(True)
                        self.ms.comboBox_4.setEnabled(True)
                        self.ms.lineEdit_2.clear()
                        self.ms.lineEdit_2.setEnabled(True)  
                        self.ms.textEdit_4.clear()
                        self.ms.textEdit_4.setEnabled(True)
                else :
                    mail = smtplib.SMTP('smtp-mail.outlook.com',587)
                    mail.ehlo()
                    mail.starttls()
                    mail.login(f"{email}",f"{paswd}")

                    mesaj = MIMEMultipart()
                    mesaj['From'] = f"{email}"
                    mesaj['To'] = f'{Aemail}{emailS}'

                    mesaj['subject'] = f'{konu}'

                    body = f'''

                        {mesaj}

                    '''
                    body_text = MIMEText(body,'plain')
                    mesaj.attach(body_text)

                    mail.sendmail(mesaj['From'],mesaj['To'],mesaj.as_string())
                    self.ms.textBrowser_4.setText(f'Mail Başarılı bir şekilde {Aemail}{emailS} kişisine ulaştırıldı.')
                    QtWidgets.QMessageBox.information(self,'Gönderme Onayı','Kişiye Başarılı bir şekilde gönderildi.')
                    self.ms.lineEdit_4.clear()
                    self.ms.lineEdit_4.setEnabled(True)            
                    self.ms.lineEdit_3.clear()
                    self.ms.lineEdit_3.setEnabled(True)            
                    self.ms.lineEdit.clear()
                    self.ms.lineEdit.setEnabled(True)
                    self.ms.comboBox_4.setEnabled(True)
                    self.ms.lineEdit_2.clear()
                    self.ms.lineEdit_2.setEnabled(True)  
                    self.ms.textEdit_4.clear()
                    self.ms.textEdit_4.setEnabled(True)
    
            elif x == 'Çoğul Gönderim':
                email = self.ms.lineEdit_4.text()
                self.ms.lineEdit_4.setEnabled(False)            
                paswd = self.ms.lineEdit_3.text()
                self.ms.lineEdit_3.setEnabled(False)            
                konu = self.ms.lineEdit_2.text()
                self.ms.lineEdit_2.setEnabled(False)  
                mesajs = self.ms.textEdit_4.toPlainText()
                self.ms.textEdit_4.setEnabled(False)
                s = self.ms.lineEdit.text()
                with open(f'{s}','a+',encoding='UTF-8') as file :  
                    x=file.readlines()
                if self.ms.comboBox_3.isHidden() == False:
                    cb = self.ms.comboBox_3.currentText()
                    if cb == 'Basit':
                        cevirme = str.maketrans(Kaynak,Hedef)
                        metin = konu
                        x = metin.translate(cevirme)
                        y = cb.translate(cevirme)
                        sifreliKN = (y+':'+x)   

                        cevirme = str.maketrans(Kaynak,Hedef)
                        metin = mesaj
                        a = metin.translate(cevirme)
                        c = cb.translate(cevirme)
                        sifreliMSG = (c+':'+a)

                        for i in x :
                            mail = smtplib.SMTP('smtp-mail.outlook.com',587)
                            mail.ehlo()
                            mail.starttls()
                            mail.login(f"{email}",f"{paswd}")

                            mesaj = MIMEMultipart()
                            mesaj['From'] = f"{email}"
                            mesaj['To'] = f'{i}'

                            mesaj['subject'] = f'{sifreliKN}'

                            body = f'''

                                {sifreliMSG}

                            '''
                            body_text = MIMEText(body,'plain')
                            mesaj.attach(body_text)

                            mail.sendmail(mesaj['From'],mesaj['To'],mesaj.as_string())
                            with open('sendmsg.json','w',encoding='UTF-8') as file :
                                file.write(f'Mail Başarılı bir şekilde {i} kişisine ulaştırıldı.\n')
                            with open('sendmsg.json','r',encoding='UTF-8') as file :
                                x = file.read()
                            bar = self.ms.textBrowser_4.toPlainText()
                            bar+=x
                            self.ms.textBrowser_4.setText(bar)
                        QtWidgets.QMessageBox.information(self,'Gönderme Onayı','Kişiye Başarılı bir şekilde gönderildi.')
                        self.ms.lineEdit_4.clear()
                        self.ms.lineEdit_4.setEnabled(True)            
                        self.ms.lineEdit_3.clear()
                        self.ms.lineEdit_3.setEnabled(True)            
                        self.ms.lineEdit.clear()
                        self.ms.lineEdit.setEnabled(True)
                        self.ms.comboBox_4.setEnabled(True)
                        self.ms.lineEdit_2.clear()
                        self.ms.lineEdit_2.setEnabled(True)  
                        self.ms.textEdit_4.clear()
                        self.ms.textEdit_4.setEnabled(True)
                    elif cb == 'Orta':
                        cevirme = str.maketrans(Kaynak,Hedef)
                        cevirme2 = str.maketrans(Hedef,Hedef2)
                        metin = konu
                        x = metin.translate(cevirme)
                        oa = a.translate(cevirme2)
                        y = cb.translate(cevirme)
                        sifreliKN = (y+':'+oa)

                        cevirme = str.maketrans(Kaynak,Hedef)
                        cevirme2 = str.maketrans(Hedef,Hedef2)
                        metin = mesaj
                        a = metin.translate(cevirme)
                        ox = a.translate(cevirme2)
                        c = cb.translate(cevirme)
                        sifreliMSG = (c+':'+ox)

                        for i in x :
                            mail = smtplib.SMTP('smtp-mail.outlook.com',587)
                            mail.ehlo()
                            mail.starttls()
                            mail.login(f"{email}",f"{paswd}")

                            mesaj = MIMEMultipart()
                            mesaj['From'] = f"{email}"
                            mesaj['To'] = f'{i}'

                            mesaj['subject'] = f'{sifreliKN}'

                            body = f'''

                                {sifreliMSG}

                            '''
                            body_text = MIMEText(body,'plain')
                            mesaj.attach(body_text)

                            mail.sendmail(mesaj['From'],mesaj['To'],mesaj.as_string())
                            with open('sendmsg.json','w',encoding='UTF-8') as file :
                                file.write(f'Mail Başarılı bir şekilde {i} kişisine ulaştırıldı.\n')
                            with open('sendmsg.json','r',encoding='UTF-8') as file :
                                x = file.read()
                            bar = self.ms.textBrowser_4.toPlainText()
                            bar+=x
                            self.ms.textBrowser_4.setText(bar)  
                        QtWidgets.QMessageBox.information(self,'Gönderme Onayı','Kişiye Başarılı bir şekilde gönderildi.')
                        self.ms.lineEdit_4.clear()
                        self.ms.lineEdit_4.setEnabled(True)            
                        self.ms.lineEdit_3.clear()
                        self.ms.lineEdit_3.setEnabled(True)            
                        self.ms.lineEdit.clear()
                        self.ms.lineEdit.setEnabled(True)
                        self.ms.comboBox_4.setEnabled(True)
                        self.ms.lineEdit_2.clear()
                        self.ms.lineEdit_2.setEnabled(True)  
                        self.ms.textEdit_4.clear()
                        self.ms.textEdit_4.setEnabled(True)
                    elif cb == 'Zor':
                        cevirme = str.maketrans(Kaynak,Hedef)
                        cevirme2 = str.maketrans(Hedef,Hedef2)
                        cevirme3 = str.maketrans(Hedef2,Hedef3)
                        metin = konu
                        x = metin.translate(cevirme)
                        oa = x.translate(cevirme2)
                        yoa = oa.tranlate(cevirme3)

                        y = cb.translate(cevirme)
                        sifreliKN = (y+':'+yoa)

                        cevirme = str.maketrans(Kaynak,Hedef)
                        cevirme2 = str.maketrans(Hedef,Hedef2)
                        cevirme3 = str.maketrans(Hedef2,Hedef3)
                        metin = mesaj
                        a = metin.translate(cevirme)
                        ox = a.translate(cevirme2)
                        xox = ox.translate(cevirme3)
                        c = cb.translate(cevirme)
                        sifreliMSG = (c+':'+xox)
                        
                        for i in x :
                            mail = smtplib.SMTP('smtp-mail.outlook.com',587)
                            mail.ehlo()
                            mail.starttls()
                            mail.login(f"{email}",f"{paswd}")

                            mesaj = MIMEMultipart()
                            mesaj['From'] = f"{email}"
                            mesaj['To'] = f'{i}'

                            mesaj['subject'] = f'{sifreliKN}'

                            body = f'''

                                {sifreliMSG}

                            '''
                            body_text = MIMEText(body,'plain')
                            mesaj.attach(body_text)

                            mail.sendmail(mesaj['From'],mesaj['To'],mesaj.as_string())
                            with open('sendmsg.json','w',encoding='UTF-8') as file :
                                file.write(f'Mail Başarılı bir şekilde {i} kişisine ulaştırıldı.\n')
                            with open('sendmsg.json','r',encoding='UTF-8') as file :
                                x = file.read()
                            bar = self.ms.textBrowser_4.toPlainText()
                            bar+=x
                            self.ms.textBrowser_4.setText(bar) 
                        QtWidgets.QMessageBox.information(self,'Gönderme Onayı','Kişiye Başarılı bir şekilde gönderildi.')
                        self.ms.lineEdit_4.clear()
                        self.ms.lineEdit_4.setEnabled(True)            
                        self.ms.lineEdit_3.clear()
                        self.ms.lineEdit_3.setEnabled(True)            
                        self.ms.lineEdit.clear()
                        self.ms.lineEdit.setEnabled(True)
                        self.ms.comboBox_4.setEnabled(True)
                        self.ms.lineEdit_2.clear()
                        self.ms.lineEdit_2.setEnabled(True)  
                        self.ms.textEdit_4.clear()
                        self.ms.textEdit_4.setEnabled(True)
                else :
                    for i in x :
                        mail = smtplib.SMTP('smtp-mail.outlook.com',587)
                        mail.ehlo()
                        mail.starttls()
                        mail.login(f"{email}",f"{paswd}")

                        mesaj = MIMEMultipart()
                        mesaj['From'] = f"{email}"
                        mesaj['To'] = f'{i}'

                        mesaj['subject'] = f'{konu}'

                        body = f'''

                            {mesajs}

                        '''
                        body_text = MIMEText(body,'plain')
                        mesaj.attach(body_text)

                        mail.sendmail(mesaj['From'],mesaj['To'],mesaj.as_string())
                        with open('sendmsg.json','w+',encoding='UTF-8') as file :
                            file.write(f'Mail Başarılı bir şekilde {i} kişisine ulaştırıldı.\n')
                        with open('sendmsg.json','r+',encoding='UTF-8') as file :
                            x = file.read()
                        bar = self.ms.textBrowser_4.toPlainText()
                        bar+=x
                        self.ms.textBrowser_4.setText(bar)
                    QtWidgets.QMessageBox.information(self,'Gönderme Onayı','Kişiye Başarılı bir şekilde gönderildi.')
                    self.ms.lineEdit_4.clear()
                    self.ms.lineEdit_4.setEnabled(True)            
                    self.ms.lineEdit_3.clear()
                    self.ms.lineEdit_3.setEnabled(True)            
                    self.ms.lineEdit.clear()
                    self.ms.lineEdit.setEnabled(True)
                    self.ms.comboBox_4.setEnabled(True)
                    self.ms.lineEdit_2.clear()
                    self.ms.lineEdit_2.setEnabled(True)  
                    self.ms.textEdit_4.clear()
                    self.ms.textEdit_4.setEnabled(True)
        
        except Exception as err:
            print(str(err))

    def openemail(self):
        a = QtWidgets.QFileDialog.getOpenFileName()
        self.ui.lineEdit.setText(a[0])


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    main = msgAn()
    app.setStyle('Fusion')
    app.exit(app.exec_())