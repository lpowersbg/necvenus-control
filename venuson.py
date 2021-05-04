import socket

host = '10.51.201.100'
port = 1000
on = b'<T0000681001000079>'
off = b'<T0000681000000078>'
status = b'<T0000681100000079>'
son = b'<F000068110100007a>'
soff = b'<F0000681100000079>'
goff = b'<F0000681000000078>'

ven = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

def comms(comm):
    ven.sendto(comm, (host, port))
    return ven.recvfrom(1024)[0]

def Main():
    if comms(status) == soff:
        comms(on)
    exit()

if __name__ == '__main__':
    Main()
