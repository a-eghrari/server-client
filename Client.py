import socket 

# You can change host and port!
host = '127.0.0.1'
port = 1234

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((host,port)) 
    while True: 
        message = input("Enter your command: ") 
        if message == 'exit':
            s.sendall(message.encode('ascii')) 
            break
        elif message == 'just receive':
            data = s.recv(1024)   
        else:
            s.sendall(message.encode('ascii'))
            data = s.recv(1024)
        print('Received from the server :',str(data.decode('ascii'))) 