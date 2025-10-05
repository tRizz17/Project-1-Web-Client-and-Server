import socket
import argparse


def WebClient(url, port):
    s = socket.socket()
    server = (url, port)
    s.connect(server)
    request = f"GET / HTTP/1.1\r\nHost:{url}\r\nConnection: close\r\n\r\n"
    request = request.encode("ISO-8859-1")
    s.sendall(request)
    buffer = ""
    while True:
        data = s.recv(4096)
        if len(data) == 0:
            break
        data = data.decode("ISO-8859-1")
        buffer += data
        print(buffer)
    s.close()

parser = argparse.ArgumentParser(description="Specify URL and port number if you wish")
parser.add_argument("url", nargs="?", default="www.example.com", help="Enter a valid URL")
parser.add_argument("port", nargs="?", type = int, default=80, help="Enter a valid port number")
args = parser.parse_args()

if __name__ == "__main__":
    WebClient(args.url, args.port)