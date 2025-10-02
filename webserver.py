import socket
import argparse

def WebServer(port):
    s = socket.socket()
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind(('', port))
    s.listen()
    print("Listening for incoming connections... ")
    while True:
        new_conn = s.accept()
        new_socket = new_conn[0]
        print("meow")
        while True:
            data = new_socket.recv(4096)
            data.decode("ISO-8859-1")
            if data == "\r\n\r\n":
                break
        response = "HTTP/1.1 200 OK\r\nContent-Type: text/plain\r\nContent-Length: 6\r\nConnection: close\r\n\r\nHello!\r\n\r\n"
        response.encode("ISO-8859-1")
        new_socket.sendall(response)

parser = argparse.ArgumentParser(description="Specify a port number if you wish")
parser.add_argument("port", nargs="?", type=int, default=28333, help="Enter a valid port number")
args = parser.parse_args()

if __name__ == "__main__":
    WebServer(args.port)
