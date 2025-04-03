import socket
import threading

def broadcast(message, current_client, clients):
    # Envía el mensaje a todos los clientes excepto el que lo envió
    for client in clients:
        if client != current_client:
            try:
                client.send(message)
            except:
                client.close()
                if client in clients:
                    clients.remove(client)

def handle_client(client, clients):
    while True:
        try:
            message = client.recv(1024)
            if message:
                print("Mensaje recibido:", message.decode('utf-8'))
                broadcast(message, client, clients)
            else:
                client.close()
                if client in clients:
                    clients.remove(client)
                break
        except:
            client.close()
            if client in clients:
                clients.remove(client)
            break

def main():
    host = '0.0.0.0'  # Escucha en todas las interfaces de red
    port = 5555
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port))
    server.listen(5)
    print(f"Servidor escuchando en {host}:{port}")

    clients = []
    while True:
        client, addr = server.accept()
        print(f"Conexión aceptada de {addr}")
        clients.append(client)
        thread = threading.Thread(target=handle_client, args=(client, clients))
        thread.start()

if __name__ == '__main__':
    main()
