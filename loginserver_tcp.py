import socket

HOST = "127.0.0.1"
PORT = 5000

# Valid username and password
USERNAME = "admin"
PASSWORD = "1234"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(1)

print("Server started...")
print("Waiting for client...")

client, address = server.accept()
print("Client connected:", address)

# Receive username
username = client.recv(1024).decode()

# Receive password
password = client.recv(1024).decode()

# Check credentials
if username == USERNAME and password == PASSWORD:
    client.send("Login Successful".encode())
    print("Login Successful")
else:
    client.send("Invalid username or password".encode())
    print("Login Failed")

client.close()
server.close()
