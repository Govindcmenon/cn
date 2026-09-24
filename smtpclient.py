import socket

HOST = "127.0.0.1"
PORT = 2525

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to SMTP server
client.connect((HOST, PORT))

# Receive server greeting
print("Server:", client.recv(1024).decode().strip())

# HELO
client.send(b"HELO localhost\r\n")
print("Server:", client.recv(1024).decode().strip())

# MAIL FROM
sender = input("Enter sender email: ")

client.send(("MAIL FROM:<" + sender + ">\r\n").encode())
print("Server:", client.recv(1024).decode().strip())

# RCPT TO
receiver = input("Enter receiver email: ")

client.send(("RCPT TO:<" + receiver + ">\r\n").encode())
print("Server:", client.recv(1024).decode().strip())

# DATA
client.send(b"DATA\r\n")
print("Server:", client.recv(1024).decode().strip())

# Get message
message = input("Enter message: ")

# Send message and end with .
client.send((message + "\r\n.\r\n").encode())

print("Server:", client.recv(1024).decode().strip())

# QUIT
client.send(b"QUIT\r\n")
print("Server:", client.recv(1024).decode().strip())

client.close()