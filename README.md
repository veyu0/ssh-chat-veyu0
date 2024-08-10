**Simple Chat Application**

This is a simple chat application that allows multiple clients to connect to a server and exchange messages in real-time. Each client can set a nickname, which will be displayed alongside their messages in the chat.

**Features**

Multiple clients: Multiple clients can connect to the server simultaneously.
Nicknames: Clients can set their own nicknames upon connecting to the server.
Real-time messaging: Messages are broadcasted to all connected clients in real-time.
Server management: The server handles all client connections and message broadcasting.
Getting Started

Prerequisites
- Python 3.x

Installation
Clone the repository:
```
git clone https://github.com/yourusername/ssh-chat-veyu0.git
cd ssh-chat-veyu0
```
Run the server:
```
python chat_server.py
```
Run the client:
```
python chat_client.py
```
You can run multiple instances of the client to simulate multiple users.

**Usage**

Starting the Server:
- Start the server by running chat_server.py. The server will start listening for incoming client connections.

Connecting a Client:
- Run chat_client.py to connect to the server. You will be prompted to enter a nickname. After entering the nickname, you can start sending messages.

Exiting the Chat:
- Type exit in the client to disconnect from the server.

**Code Structure**

- chat_server.py: Handles incoming client connections, manages nicknames, and broadcasts messages to all connected clients.
- chat_client.py: Connects to the server, allows the user to set a nickname, send messages, and receive messages from the server.
