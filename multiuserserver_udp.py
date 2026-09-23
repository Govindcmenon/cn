import socket
import threading

HOST = "127.0.0.1"
PORT = 5002

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind((HOST, PORT))

clients = {}

print("Chat server started...")
print("Waiting for clients...")

def receive_messages():
    while True:
        message, address = server.recvfrom(1024)
        message = message.decode()

        # First message is username
        if address not in clients:
            clients[address] = message
            print(message, "joined the chat.")
        else:
            name = clients[address]
            print(name + ":", message)

            # Send message to all other clients
            for client in clients:
                if client != address:
                    server.sendto(
                        (name + ": " + message).encode(),
                        client
                    )

thread = threading.Thread(target=receive_messages)
thread.start()
