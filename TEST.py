import socket
import sys

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = ''
port = 4444

s.bind((host, port))
s.listen(2)
conn, add = s.accept()
print('Connection is established successfully' + '\nip:' + add[0] + '\nport:' + str(add[1]))

def command(conn):
    while True:
        cmd = input()
        if cmd == 'quit' or cmd == 'exit':
            s.close()
            conn.close()
            sys.exit()
        if len(str.encode(cmd)) > 0:
            conn.send(str.encode(cmd))
            client_response = str(conn.recv(1024), 'utf-8')
            print(client_response, end='')


command(conn)
conn.close()

if __name__ == '__main__':
    command(conn)
