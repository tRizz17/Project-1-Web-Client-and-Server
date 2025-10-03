import socket
import argparse

def WebServer(port):
    s = socket.socket()
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind(('', port))
    while True:
        s.listen()
        print("Listening for incoming connections... ")
        new_conn = s.accept()
        new_socket = new_conn[0]
        data = new_socket.recv(1024).decode("ISO-8859-1")
        print(data)
        response = 'HTTP/1.1 200 OK\r\nContent-Type: text/plain\r\nContent-Length: 6\r\nConnection: close\r\n\r\nHello!\r\n\r\n'
        new_socket.sendall(response.encode("ISO-8859-1"))
        new_socket.close()

parser = argparse.ArgumentParser(description="Specify a port number if you wish")
parser.add_argument("port", nargs="?", type=int, default=28333, help="Enter a valid port number")
args = parser.parse_args()

if __name__ == "__main__":
    WebServer(args.port)
