import socket

HOST = "127.0.0.1"
PORT = 5000

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect((HOST, PORT))

# Get filename from user
filename = input("Enter filename: ")

# Send filename to server
client.send(filename.encode())

# Receive response
response = client.recv(4096).decode()

print("\nServer Response")
print("----------------")
print(response)

client.close()
