from pathlib import Path
from boofuzz import *

# vulnserver
ip = "127.0.0.1"
port = 9999

# vulnserver Connection
connection = SocketConnection(ip, port, proto="tcp")
target = Target(connection=connection)
session = Session(target=target)

# Fuzzing Setup
s_initialize("vulnserver-trun")    

s_string("LTER", fuzzable=False)
s_delim(" ", fuzzable=False)
s_string("something")       # Fuzzing Point

session.connect(s_get("vulnserver-trun"))

session.fuzz()
