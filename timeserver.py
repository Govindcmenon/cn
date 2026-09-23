import socket
import datetime

HOST = "127.0.0.1"
PORT = 5000

# Create UDP socket
server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind socket
server.bind((HOST, PORT))

print("Time Server Started...")
print("Waiting for time requests...")

while True:

    # Receive request from client
    data, address = server.recvfrom(1024)

    print("Request received from:", address)

    # Get server system time
    current_time = datetime.datetime.now()

    # Convert time to string
    time_string = current_time.strftime("%Y-%m-%d %H:%M:%S")

    # Send time to client
    server.sendto(time_string.encode(), address)

    print("Time sent:", time_string)
