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

import socket
import select
import errno
import sys

Header_Length = 10
host = '127.0.0.1'
port = 1881

my_username = input('Kullanıcı Adı:')

client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client_socket.connect((host,port))
client_socket.setblocking(False)

username = my_username.encode('utf-8')
username_header = f"{len(username):<{Header_Length}}".encode('utf-8')
client_socket.send(username_header + username)

while True :
    message = input(f'{my_username} >')
    if message:
        message = message.encode('utf-8')
        message_header = f'{len(message) :< {Header_Length}}'.encode('utf-8')
        client_socket.send(message_header + message)

    try:
        while True :
            username_header = client_socket.recv(Header_Length)
            if not len(username_header):
                print('Bağlantı Kapatıldı')
                sys.exit()
            
            username_lenght = int(username_header.decode('utf-8').strip())
            username = client_socket.recv(username_lenght).decode('utf-8')

            message_header = client_socket.recv(Header_Length)
            message_length = int(message_header.decode('utf-8').strip())
            message = client_socket.recv(message_length).decode('utf-8')

            print(f"{username} >> {message}")

    except IOError as e :
        if e.errno != errno.EAGAIN and e.errno != errno.EWOULDBLOCK:
            print('Error: {}'.format(str(e)))
            sys.exit()
            continue



    except Exception as err :
        print('Error:{}'.format(str(err)))
        sys.exit()
