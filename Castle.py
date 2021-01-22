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
modelpath = os.path.join(localpath, "models/resnet50_coco_best_v2.1.0.h5")

detector = imageai.Detection.ObjectDetection()
detector.setModelTypeAsRetinaNet()
detector.setModelPath(modelpath)
detector.loadModel()
custom_objects = detector.CustomObjects(person=True)
		
		
for line in tail ("-f", "/var/log/vsftpd.log", _iter=True):
	if("OK UPLOAD" in line):
		start = line.find("/files")
		end = line.find(",", start)
		filename = "/home/castle/ftp" + line[start:end-1]

		print(filename)
		try:
			output = str(subprocess.check_output("sudo alpr " + filename, shell=True)).replace("\\t", " ").replace("\\n", ";")
			if("No license plates found" in output):
				output = ""
			
			
			detection = self.detector.detectCustomObjectsFromImage(custom_objects=custom_objects, input_image=filename, minimum_percentage_probability=30)
			for eachItem in detection:
				output = output + "\n" + eachItem["name"] + " (" + eachItem["box_points"] + ")"
			
			if(len(output) > 1 ):
				context = ssl._create_unverified_context()
				post_data = urllib.parse.urlencode({"owner":"intesla_test", "activity":output}).encode('utf-8')
				x = urllib.request.urlopen(url="http://www.pendola.net/api/castleapi.php", data=post_data, context=context, timeout=15)
				html = x.read().decode("utf-8")
				print(html)
				
			
		except:
			print("ouch... that wasn't an image")
			pass
