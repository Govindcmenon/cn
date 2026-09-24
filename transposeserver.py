import socket
import pickle

HOST = "127.0.0.1"
PORT = 5000

# Create TCP socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind socket
server.bind((HOST, PORT))

# Listen for client
server.listen(1)

print("Server started...")
print("Waiting for client...")

# Accept connection
client, address = server.accept()

print("Client connected:", address)

# Receive matrix
data = client.recv(4096)
matrix = pickle.loads(data)

# Find transpose
transpose = []

for j in range(len(matrix[0])):
    row = []

    for i in range(len(matrix)):
        row.append(matrix[i][j])

    transpose.append(row)

# Send transpose to client
data = pickle.dumps(transpose)
client.send(data)

print("Transpose calculated and sent.")

client.close()
server.close()