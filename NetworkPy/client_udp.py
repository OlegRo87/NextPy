import socket

SERVER_IP = "127.0.0.1"
PORT = 8821
MAX_MSG_SIZE = 1024
my_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
data = ""
while data != "EXIT":
    msg = input("Please send a message :\n")
    my_socket.sendto(msg.encode(), (SERVER_IP, PORT))
    (response, remote_address) = my_socket.recvfrom(MAX_MSG_SIZE)
    data = response.decode()
    print("The server sent " + data)

my_socket.close()