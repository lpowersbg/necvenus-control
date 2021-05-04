import socket

def Main():
    host = '192.168.0.1'
    port = 7142

    mon = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    mon.connect((host, port))
    message = b'\x01\x30\x2A\x30\x41\x30\x43\x02\x43\x32\x30\x33\x44\x36\x30\x30\x30\x34\x03\x15\x0D'
    mon.send(message)
    exit()
    # data = mon.receive(1024)
    # print(data.hex)
    # mon.close()
    # exit()

    # message = b'\x01\x30\x2A\x30\x41\x30\x43\x02\x43\x32\x30\x33\x44\x36\x30\x30\x30\x31\x03\x18\x0D'

if __name__ == '__main__':
    Main()
