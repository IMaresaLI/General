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

Header_Length = 10
host = '127.0.0.1'
port = 1881

server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
server_socket.bind((host,port))
server_socket.listen()
print('Server Aktif')

sockets_list = [server_socket]

clients = {}


def mesajilet(client_socket):
    try:
        message_header = client_socket.recv(Header_Length)

        if not len(message_header):
            return False 

        message_length = int(message_header.decode('UTF-8').strip())
        return {'header': message_header,'data':client_socket.recv(message_length)}
 
    except:
        return False

while True :
    read_sockets, _, exception_sockets = select.select(sockets_list, [],sockets_list)
    for notified_socket in read_sockets:
        if notified_socket == server_socket:
            client_socket,client_address=server_socket.accept()

            user = mesajilet(client_socket)
            if user is False:
                continue
            
            sockets_list.append(client_socket)
            clients[client_socket] = user

            print('Bağlantı Kabul Edildi {}:{}, Kullanıcı : {}'.format(*client_address, user['data'].decode('utf-8')))

        else :
            message = mesajilet(notified_socket)
            if message is False :
                print('Serverdan {} kullanıcısı ayrıldı.'.format(clients[notified_socket]['data'].decode('utf-8')))
                sockets_list.remove(notified_socket)
                del clients[notified_socket]
                continue

            user = clients[notified_socket]
            print(f'{user["data"].decode("utf-8")} Adlı Kullanıcı : {message["data"].decode("utf-8")} Mesajı Yazdı.')

            for client_socket in clients:
                if client_socket != notified_socket:
                    client_socket.send(user['header']+ user['data'] + message['header'] + message['data'])

    for notified_socket in exception_sockets:
        sockets_list.remove(notified_socket)
        del clients[notified_socket]

