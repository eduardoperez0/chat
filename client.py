import socket
import threading

def receive_messages(client):
    while True:
        try:
            message = client.recv(1024).decode('utf-8')
            if message:
                print("\n" + message)
            else:
                break
        except:
            break

def main():
    # Aquí pones la IP real del servidor
    host = '192.168.1.20'
    port = 5001

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        client.connect((host, port))
    except Exception as e:
        print("No se pudo conectar al servidor:", e)
        return

    # Hilo para recibir mensajes
    thread = threading.Thread(target=receive_messages, args=(client,))
    thread.daemon = True
    thread.start()

    print("Conectado al servidor. Escribe tus mensajes ('salir' para terminar):")
    while True:
        message = input()
        if message.lower() == 'salir':
            break
        client.send(message.encode('utf-8'))

    client.close()

if __name__ == '__main__':
    main()
