import socket
# asks for user IP, Port, and username
host = input("Enter server IP address: ")
port = int(input("Enter server port number: "))
username = input("Enter your username: ")

# create  object and connect to the server
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((host, port))

# welcome message from the server
welcome_msg = client_socket.recv(1024).decode()
print(welcome_msg)

while True:
    # ask the user to enter a message
    msg = input("Enter a message to send to the server: ")
    
    # send the message to the server
    client_socket.send(msg.encode())
    
    if msg == "end":
        # if the user enters "end", exit program
        client_socket.close()
        exit()
    
    # receive a message from the server
    reply = client_socket.recv(1024).decode()
    
    # print the message and the sender's username to the client console
    print(reply)