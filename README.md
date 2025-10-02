Some notes to myself from the readings:

The default character encoding of the web is “ISO-8859-1”.

s = "Hello, world!"          # String
b = s.encode("ISO-8859-1")   # Sequence of bytes

To convert from a byte sequence you received from a socket in ISO-8859-1 format to a string:

s = b.decode("ISO-8859-1")

Ends-of-line are delimited by a Carriage Return/Linefeed combination. In Python or C, you write a CRLF like this:

"\r\n"

If you were requesting a specific file, it would be on that first line, for example:

GET /path/to/file.html HTTP/1.1

A simple HTTP response from a server looks like:

HTTP/1.1 200 OK
Content-Type: text/plain
Content-Length: 6
Connection: close

Hello!

Notice that the Content-Length is set to the size of the payload: 6 bytes for Hello!.

Another common Content-Type is text/html when the payload has HTML data in it.

