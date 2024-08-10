import socket
import threading

# Конфигурация сервера
HOST = '0.0.0.0'
PORT = 12345
clients = []


def broadcast(message, client_socket):
    for client in clients:
        if client == client_socket:
            try:
                client.send(message)
            except:
                client.close()
                clients.remove(client)


def handle_client(client_socket):
    nickname = client_socket.recv(1024).decode('utf-8')  # Получаем никнейм от клиента
    clients.append(client_socket)
    broadcast(f'{nickname} присоединился к чату!'.encode('utf-8'), client_socket)

    while True:
        try:
            message = client_socket.recv(1024)
            if not message:
                break
            broadcast(message, client_socket)
        except:
            client_socket.close()
            clients.remove(client_socket)
            broadcast(f'{nickname} покинул чат.'.encode('utf-8'), client_socket)
            break


def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((HOST, PORT))
    server_socket.listen(5)

    print("Сервер запущен и ожидает подключения клиентов...")

    while True:
        client_socket, client_address = server_socket.accept()
        print(f'{client_address} подключен.')
        threading.Thread(target=handle_client, args=(client_socket,)).start()


if __name__ == "__main__":
    main()
