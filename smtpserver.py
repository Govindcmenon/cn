import socket

HOST = "127.0.0.1"
PORT = 2525

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(1)

print("SMTP Server started...")
print("Waiting for client...")

client, address = server.accept()

print("Client connected:", address)

# Send greeting
client.send(b"220 Simple SMTP Server Ready\r\n")

while True:
    data = client.recv(1024).decode()

    if not data:
        break

    print("Client:", data.strip())

    command = data.strip().upper()

    if command.startswith("HELO"):
        client.send(b"250 Hello\r\n")

    elif command.startswith("MAIL FROM"):
        client.send(b"250 Sender OK\r\n")

    elif command.startswith("RCPT TO"):
        client.send(b"250 Recipient OK\r\n")

    elif command == "DATA":
        client.send(b"354 Start mail input; end with <CRLF>.<CRLF>\r\n")

        # Receive email content
        message = client.recv(4096).decode()

        print("\nEmail received:")
        print(message)

        client.send(b"250 Message received\r\n")

    elif command == "QUIT":
        client.send(b"221 Bye\r\n")
        break

    else:
        client.send(b"500 Command not recognized\r\n")

client.close()
server.close()

print("Server stopped.")