Simple Chat Application

This is a simple chat application that allows multiple clients to connect to a server and exchange messages in real-time. Each client can set a nickname, which will be displayed alongside their messages in the chat.

Features

Multiple clients: Multiple clients can connect to the server simultaneously.
Nicknames: Clients can set their own nicknames upon connecting to the server.
Real-time messaging: Messages are broadcasted to all connected clients in real-time.
Server management: The server handles all client connections and message broadcasting.
Getting Started

Prerequisites
Python 3.x
Installation
Clone the repository:
bash
Copy code
git clone https://github.com/yourusername/chat-application.git
cd chat-application
Run the server:
bash
Copy code
python chat_server.py
Run the client:
bash
Copy code
python chat_client.py
You can run multiple instances of the client to simulate multiple users.
Usage

Starting the Server:
Start the server by running chat_server.py. The server will start listening for incoming client connections.
Connecting a Client:
Run chat_client.py to connect to the server. You will be prompted to enter a nickname. After entering the nickname, you can start sending messages.
Exiting the Chat:
Type exit in the client to disconnect from the server.
Code Structure

chat_server.py: Handles incoming client connections, manages nicknames, and broadcasts messages to all connected clients.
chat_client.py: Connects to the server, allows the user to set a nickname, send messages, and receive messages from the server.
Example

Start the server:
Copy code
Сервер запущен и ожидает подключения клиентов...
Connect a client:
Copy code
Введите свой никнейм: Alice
Alice присоединился к чату!
Start chatting:
makefile
Copy code
Alice: Привет всем!
Known Issues

Currently, the server does not handle reconnection attempts for clients that disconnect unexpectedly.
The application is designed for LAN environments and may require additional configuration for use over the internet.
Future Improvements

Add support for private messaging between clients.
Implement a GUI for both the client and server.
Improve error handling and reconnection logic.
License

This project is licensed under the MIT License - see the LICENSE file for details.
