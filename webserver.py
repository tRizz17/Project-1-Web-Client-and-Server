
import socket


def WebServer(port):
    s = socket.socket()
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind('', port)
    s.listen()
    new_conn = s.accept()
    new_socket = new_conn[0]
    while True:
        data = new_socket.recv()
        data.decode("ISO-8859-1")
        if data == "\r\n\r\n":
            break
        response = "HTTP/1.1 200 OK\r\nContent-Type: text/plain\r\nContent-Length: 6\r\nConnection: close\r\n\r\nHello!\r\n\r\n"
        response.encode("ISO-8859-1")

        
# port=28333