import socket
import binascii

def Main():
    host = '192.168.2.3'
    port = 8000

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    print 'connected'
    message = '\x00\x01\x02\x01\x00\x12\x03\x6b\xd6\x6f\x01\x01\x00\x00\x02\x58\x69\x47\xae\x58\x69\x47\xae\x00'
    s.send(message)
    print 'sent command'

    data = s.recv(1024)
    s.close()
    print type(data)

    print binascii.hexlify(data)

if __name__ == '__main__':
    Main()