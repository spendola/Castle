import subprocess
import sys
import urllib
import urllib.request
import json
import ssl
import os
import imageai.Detection
from sh import tail

# initialization of imageai
localpath = os.path.dirname(os.path.realpath(__file__))
modelpath = os.path.join(self.localpath, "models/resnet50_coco_best_v2.0.1.h5")

detector = imageai.Detection.ObjectDetection()
detector.setModelTypeAsRetinaNet()
detector.setModelPath(self.modelpath)
detector.loadModel(detection_speed="fast")
custom_objects = detector.CustomObjects(person=True, sports_ball=True)
		
		
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