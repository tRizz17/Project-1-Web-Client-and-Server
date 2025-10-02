import socket
import argparse


def HTTP_Request(url, port):
    s = socket.socket()
    server = (url, port)
    s.connect(server)
    request = f"GET / HTTP/1.1\r\nHost:{url}\r\nConnection: close\r\n\r\n"
    request = request.encode("ISO-8859-1")
    s.sendall(request)
    while True:
        data = s.recv(4096)
        if len(data) == 0:
            break
        response = data.decode("ISO-8859-1")
        print(response)
    s.close()

parser = argparse.ArgumentParser(description="Specify URL and port number if you wish")
parser.add_argument("url", nargs="?", default="www.example.com", help="Enter a valid URL")
parser.add_argument("port", nargs="?", type = int, default=80, help="Enter a valid port number")
args = parser.parse_args()

if __name__ == "__main__":
    HTTP_Request(args.url, args.port)


# This needs to run with 'python3 webclient.py example.com'
# ALSO: you need to be able specify a port number to connect to on the command line. This defaults to port 80 if not specified. So you could connect to a webserver on a different port like so:

# $ python webclient.py example.com 8088
