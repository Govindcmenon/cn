import socket
import threading
import os

HOST = "127.0.0.1"
PORT = 5000

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(5)

print("File Server Started...")
print("Server PID:", os.getpid())
print("Waiting for clients...\n")


def handle_client(client, address):
    pid = os.getpid()

    print("Client connected:", address)

    # Receive filename
    filename = client.recv(1024).decode()

    print("Requested file:", filename)

    # Check whether file exists
    if os.path.exists(filename):

        with open(filename, "r") as file:
            content = file.read()

        response = "PID: " + str(pid) + "\n"
        response += "File Contents:\n"
        response += content

    else:

        response = "PID: " + str(pid) + "\n"
        response += "File not found."

    # Send response
    client.send(response.encode())

    client.close()

    print("Client disconnected:", address)


while True:

    client, address = server.accept()

    # Create a new thread for each client
    thread = threading.Thread(
        target=handle_client,
        args=(client, address)
    )

    thread.start()
