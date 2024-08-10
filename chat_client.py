import socket
import threading

# Конфигурация клиента
HOST = '127.0.0.1'  # Замените на IP-адрес сервера
PORT = 12345


def receive_messages(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            print(message)
        except:
            print("Соединение с сервером потеряно.")
            client_socket.close()
            break


def main():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((HOST, PORT))

    nickname = input("Введите свой никнейм: ")
    client_socket.send(nickname.encode('utf-8'))  # Отправка никнейма на сервер

    threading.Thread(target=receive_messages, args=(client_socket,)).start()

    while True:
        message = input()
        if message.lower() == 'exit':
            client_socket.send(f'{nickname} покинул чат.'.encode('utf-8'))
            client_socket.close()
            break
        client_socket.send(f'{nickname}: {message}'.encode('utf-8'))


if __name__ == "__main__":
    main()