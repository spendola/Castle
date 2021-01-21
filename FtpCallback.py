#!/usr/bin/python
import subprocess
import sys


print("Python received: " + sys.argv[1])
line = sys.argv[1]
start = line.find("/files")
end = line.find(",", start)
filename = "/home/castle/ftp" + line[start:end-1]
print(filename)

output = subprocess.check_output("alpr " + filename)
print(output)