#!/usr/bin/python
import subprocess
import sys

line = sys.argv[1]
start = line.find("/files")
end = line.find(",", start)
filename = "/home/castle/ftp" + line[start:end-1]

print(filename)
output = str(subprocess.check_output("sudo alpr " + filename, shell=True)).replace("\\t", " ").replace("\\n", ";")
print(output)

