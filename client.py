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
    host = 'IP_DEL_SERVIDOR'  # Reemplaza con la IP real de la máquina donde está el servidor
    port = 5555

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        client.connect((host, port))
    except Exception as e:
        print("No se pudo conectar al servidor:", e)
        return

    # Inicia un hilo para recibir mensajes del servidor
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
