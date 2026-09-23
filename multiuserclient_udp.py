import socket
import threading

HOST = "127.0.0.1"
PORT = 5002

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

name = input("Enter your name: ")

# Send name to server
client.sendto(name.encode(), (HOST, PORT))


def receive_messages():
    while True:
        try:
            message, address = client.recvfrom(1024)
            print(message.decode())
        except:
            break


def send_messages():
    while True:
        message = input()
        client.sendto(message.encode(), (HOST, PORT))


receive_thread = threading.Thread(target=receive_messages)
send_thread = threading.Thread(target=send_messages)

receive_thread.start()
send_thread.start()
