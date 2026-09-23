import socket

HOST = "127.0.0.1"
PORT = 5000

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

# Get login details
username = input("Enter username: ")
password = input("Enter password: ")

# Send username and password
client.send(username.encode())
client.send(password.encode())

# Receive result
response = client.recv(1024).decode()

print("Server:", response)

client.close()
