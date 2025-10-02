import socket


def HTTP_Request(method="GET", url="example.com", port=80):
    s = socket.socket()
    server = (url, port)
    s.connect(server)
    request = f"{method} / HTTP/1.1\r\nHost:www.{url}\r\nConnection: close\r\n\r\n"
    request = request.encode("ISO-8859-1")
    s.sendall(request)
    data = s.recv(1024)
    response = data.decode("ISO-8859-1")
    print(response)
    s.close()


if __name__ == "__main__":
    HTTP_Request()



# This needs to run with 'python3 webclient.py example.com'
# ALSO: you need to be able specify a port number to connect to on the command line. This defaults to port 80 if not specified. So you could connect to a webserver on a different port like so:

# $ python webclient.py example.com 8088
