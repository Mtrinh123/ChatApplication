import socket

# get user input for IP address, port number, and username
host = input("Enter IP address (localhost)")
port = int(input("Enter port number (defualt port): "))
username = input("Enter your username: ")

# create a socket object and bind it to the given host and port
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((host, port))

server_socket.listen()

print(f"Server started on {host}:{port}")

# create a list to hold client sockets
client_sockets = []

while True:
    client_socket, address = server_socket.accept()
    print(f"Connected to {address}")
    
    client_sockets.append(client_socket)
    
    # send a welcome message to the client
    welcome_msg = f"Welcome to the chat, {username}!"
    client_socket.send(welcome_msg.encode())
    
    while True:
        # receive a message from the client
        msg = client_socket.recv(1024).decode()
        if not msg:
            # if the message is empty, remove the client socket from the list
            client_sockets.remove(client_socket)
            break
        
        # print the message and the sender's username 
        print(f"{username}: {msg}")
        
        # send the message to all other clients
        for socket in client_sockets:
            if socket != client_socket:
                socket.send(f"{username}: {msg}".encode())
        
        # enter a message to send back to the client
        reply = input("Enter a message to send back to the client: ")
        
        # send the message back to the client
        client_socket.send(reply.encode())
        
        if reply == "end":
            # if the user enters "end", exit the program
            server_socket.close()
            exit()