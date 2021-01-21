#!/usr/bin/python
import subprocess
import sys


print("Python received: " + sys.argv[1])
line = sys.argv[1]
start = line.find("/files")
end = line.find(",", start)
filename = line[start:end]
print(filename)