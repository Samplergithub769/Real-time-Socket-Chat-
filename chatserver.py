import socket
serversocket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
serversocket.bind(("127.0.0.1",6000))
serversocket.listen()
print("server started,waiting for client....")
client,address=serversocket.accept()
print("Client connected:",address)

while True:
    try:
        msg=client.recv(1024).decode()
        if not msg:
            print("Client disconnected")
            break
        if msg.lower()=="exit":
            print("Client left the chat")
            break
        print("Client:",msg)
        reply=input("Server:")
        if reply.lower()=="exit":
            client.send("Server left the chat".encode())
            break
        client.send(reply.encode())
    except Exception as E:
        print("Error:",E)
        break
    
client.close()
serversocket.close()