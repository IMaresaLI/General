import sqlite3


def Add(bilgi, username, password):
    connection = sqlite3.connect("pwd.db")
    cursor = connection.cursor()
    cursor.execute(f"INSERT INTO PasswordRecorved(bilgi,username,password) VALUES (?,?,?)",
                       (bilgi, username, password))
    connection.commit()
    connection.close()
    
def getDatabase():
    connection = sqlite3.connect("pwd.db")
    cursor = connection.cursor()
    cursor.execute(f"Select * from PasswordRecorved")
    data = cursor.fetchall()
    connection.close()
    return data

def getPasswdUser(id):
    connection = sqlite3.connect("pwd.db")
    cursor = connection.cursor()
    cursor.execute(f"Select * from PasswordRecorved where id=?",(id,))
    data = cursor.fetchone()
    connection.close()
    return data

def Update(bilgi,username,password,id):
    connection = sqlite3.connect("pwd.db")
    cursor = connection.cursor()
    cursor.execute(f"UPDATE PasswordRecorved set Bilgi=?,username=?,password=?  where id=?",(bilgi,username,password,id))
    connection.commit()
    connection.close()

def Delete(id):
    connection = sqlite3.connect("pwd.db")
    cursor = connection.cursor()
    cursor.execute(f"Delete From PasswordRecorved where id=?",(id,))
    connection.commit()
    connection.close()



    
    