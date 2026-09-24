import socket
import pickle

HOST = "127.0.0.1"
PORT = 5000

# Create TCP socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to server
client.connect((HOST, PORT))

# Input matrix order
n = int(input("Enter the order of matrix: "))

# Input matrix
matrix = []

print("Enter matrix elements:")

for i in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)

# Display original matrix
print("\nOriginal Matrix:")

for row in matrix:
    print(*row)

# Send matrix to server
data = pickle.dumps(matrix)
client.send(data)

# Receive transpose
data = client.recv(4096)
transpose = pickle.loads(data)

# Display transpose
print("\nTranspose Matrix:")

for row in transpose:
    print(*row)

client.close()