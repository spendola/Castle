import os
from sh import tail


for line in tail ("-f", "/var/log/vsftpd.log", _iter=True):
	print(line)
