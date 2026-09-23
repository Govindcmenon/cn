import socket

HOST = "127.0.0.1"
PORT = 5000

# Create UDP socket
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Send time request
message = "TIME"
client.sendto(message.encode(), (HOST, PORT))

print("Time request sent to server...")

# Receive time from server
data, address = client.recvfrom(1024)

# Display received time
print("Server time:", data.decode())

client.close()
