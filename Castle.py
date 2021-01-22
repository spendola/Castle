import subprocess
import sys
import urllib
import urllib.request
import json
import ssl
import os
from sh import tail


for line in tail ("-f", "/var/log/vsftpd.log", _iter=True):
	if("OK UPLOAD" in line):
		start = line.find("/files")
		end = line.find(",", start)
		filename = "/home/castle/ftp" + line[start:end-1]

		print(filename)
		output = str(subprocess.check_output("sudo alpr " + filename, shell=True)).replace("\\t", " ").replace("\\n", ";")
		print(output)

		if("No license plates found" not in output):
			context = ssl._create_unverified_context()
			post_data = urllib.parse.urlencode({"owner":"intesla_test", "activity":output}).encode('utf-8')
			x = urllib.request.urlopen(url="http://www.pendola.net/api/castleapi.php", data=post_data, context=context, timeout=15)
			html = x.read().decode("utf-8")
			print(html)