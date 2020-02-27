#!/usr/bin/env python3
  
import socket
import sys

HOST = sys.argv[1]
PORT = 3000

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(b'Hello from the second server')
    data = s.recv(1024)

print('Received', repr(data))