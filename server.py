import socket
import random

HOST = "localhost"
PORT = 5827

main_connexion = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    main_connexion.bind((HOST, PORT))
except socket.error as e:
    str(e)

main_connexion.listen(2)
print("The server is started")

nbrRandom = 0

def chooseNbrRandom():
    global nbrRandom
    nbrRandom = random.randint(0, 50)
    print("Le nbr random choisit par le serveur est:")
    print(nbrRandom)
    #"Le serveur choisit un nbr random"

chooseNbrRandom()


address: object
conn1, address1 = main_connexion.accept()
conn1.sendall(str.encode("joueur1"))

print("The server is now listening on the port {}".format(PORT))
dataClient1 = conn1.recv(1024)
# "recoit les data du client"
dataClient1 = dataClient1.decode("utf8")
# "décode les data du client"
print(dataClient1)
conn1.sendall(str.encode("En attente de la connexion d'un autre joueur"))
print("En attente de la connexion d'un autre joueur")

conn2, address2 = main_connexion.accept()
conn2.sendall(str.encode("joueur2"))
print("The server is now listening on the port {}".format(PORT))

dataClient2 = conn2.recv(1024)
# "recoit les data du client"
dataClient2 = dataClient2.decode("utf8")
# "décode les data du client"
print(dataClient2)

conn1.sendall(str.encode("Deuxième joueur connecté!"))

while True:
    dataServer = "Attend que l'autre joueur joue "
    dataServer = dataServer.encode("utf8")
    conn2.sendall(dataServer)

    dataServer = "Joueur1 entre un nombre entre 0 et 50: "
    dataServer = dataServer.encode("utf8")
    conn1.sendall(dataServer)
    dataClient1 = conn1.recv(1024) #Recoit la réponse
    # "recoit les data du client"
    dataClient1 = dataClient1.decode("utf8")
    # "décode les data du client"
    print(dataClient1)

    if int(dataClient1) == nbrRandom:
        dataServer = "Le joueur1 à gagné, le nombre était " + str(nbrRandom)
        dataServer = dataServer.encode("utf8")
        conn1.sendall(dataServer)
        conn2.sendall(dataServer)
        break
    elif int(dataClient1) < nbrRandom:
        dataServer = "Le nombre choisit par le joueur1 est: " + dataClient1 + ", le nombre à trouver est plus grand!"
    elif int(dataClient1) > nbrRandom:
        dataServer = "Le nombre choisit par le joueur1 est: " + dataClient1 + ", le nombre à trouver est plus petit!"
    else:
        dataServer = "Réponse incorrect!"

    print(nbrRandom)
    print(int(dataClient1))
    dataServer = dataServer.encode("utf8")
    conn1.sendall(dataServer)
    conn2.sendall(dataServer)


    dataServer = "Attend que l'autre joueur joue"
    dataServer = dataServer.encode("utf8")
    conn1.sendall(dataServer)

    dataServer = "Joueur2 entre un nombre entre 0 et 50: "
    dataServer = dataServer.encode("utf8")
    conn2.sendall(dataServer)
    dataClient2 = conn2.recv(1024)
    # "recoit les data du client"
    dataClient2 = dataClient2.decode("utf8")
    # "décode les data du client"
    print(dataClient2)

    if int(dataClient2) == nbrRandom:
        dataServer = "Le joueur2 à gagné, le nombre était " + str(nbrRandom)
        dataServer = dataServer.encode("utf8")
        conn1.sendall(dataServer)
        conn2.sendall(dataServer)
        break
    elif int(dataClient2) < nbrRandom:
        dataServer = "Le nombre choisit par le joueur1 est: " + dataClient2 + ", le nombre à trouver est plus grand!"
    elif int(dataClient2) > nbrRandom:
        dataServer = "Le nombre choisit par le joueur1 est: " + dataClient2 + ", le nombre à trouver est plus petit!"
    else:
        dataServer = "Réponse incorrect!"

    print(int(dataClient2))
    dataServer = dataServer.encode("utf8")
    conn1.sendall(dataServer)
    conn2.sendall(dataServer)

conn1.close()
conn2.close()
main_connexion.close()