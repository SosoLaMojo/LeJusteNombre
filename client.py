import socket

HOST = "localhost"
PORT = 5827

main_connexion = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    main_connexion.connect((HOST, PORT))
    print("Client is connected")

    dataServer = main_connexion.recv(1024)
    dataServer = dataServer.decode("utf8")
    print(dataServer)

    dataClient = "Hello! Je suis le " + dataServer
    dataClient = dataClient.encode("utf8")
    main_connexion.sendall(dataClient)

    while True:
        dataServer = main_connexion.recv(1024)#Recoit un message d'attente que l'autre joueur joue
        dataServer = dataServer.decode("utf8")
        print(dataServer) #Affiche le message d'attente d'un autre joueur
        dataServer = main_connexion.recv(1024) #Recoit la réponse de l'autre joueur
        dataServer = dataServer.decode("utf8")
        print(dataServer) # Affiche la réponse de l'autre joueur
        dataServer = main_connexion.recv(1024) #Recoit la question
        dataServer = dataServer.decode("utf8")
        dataClient = input(dataServer)
        dataClient = dataClient.encode("utf8")
        main_connexion.sendall(dataClient)

        dataServer = main_connexion.recv(1024)  # Recoit sa propre réponse
        dataServer = dataServer.decode("utf8")
        print(dataServer)  # Affiche sa propre réponse

except:
    print("Connection to server failed")
