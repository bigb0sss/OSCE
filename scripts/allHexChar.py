import sys

print "[+] Printing all hex characters...\n"

for i in range(0, 256):
    sys.stdout.write("\\x" + '{:02x}'.format(i))
