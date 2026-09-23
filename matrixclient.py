import socket
import random
import pickle

HOST = "127.0.0.1"
PORT = 5000

# Create TCP socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect((HOST, PORT))

n = int(input("Enter the order of matrix: "))

matrix = []

for i in range(n):
    row = []

    for j in range(n):
        row.append(random.randint(1, 50))

    matrix.append(row)

# Display matrix
print("\nGenerated Matrix:")

for row in matrix:
    print(*row)

# Send matrix to server
data = pickle.dumps(matrix)
client.send(data)

# Receive result
result = client.recv(1024).decode()

print("\nMatrix Type:", result)

client.close()
