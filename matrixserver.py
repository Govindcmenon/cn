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

n = len(matrix)

# Check diagonal matrix
diagonal = True

for i in range(n):
    for j in range(n):
        if i != j and matrix[i][j] != 0:
            diagonal = False

# Check upper triangular matrix
upper = True

for i in range(n):
    for j in range(i):
        if matrix[i][j] != 0:
            upper = False

# Check lower triangular matrix
lower = True

for i in range(n):
    for j in range(i + 1, n):
        if matrix[i][j] != 0:
            lower = False

# Identify matrix type
if diagonal:
    result = "Diagonal Matrix"
elif upper:
    result = "Upper Triangular Matrix"
elif lower:
    result = "Lower Triangular Matrix"
else:
    result = "None"

print("Matrix type:", result)

# Send result to client
client.send(result.encode())

client.close()
server.close()
