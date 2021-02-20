import subprocess
import sys
import urllib
import urllib.request
import json
import ssl
import os
import cv2
import imageai.Detection
import ftplib
from sh import tail

def SendActivity(client, level, message):
	context = ssl._create_unverified_context()
	post_data = urllib.parse.urlencode({"key":"1338", "client":client, "level":level, "message":message}).encode('utf-8')
	x = urllib.request.urlopen(url="http://www.intesla.cl/api/castleapi.php", data=post_data, context=context, timeout=15)
	html = x.read().decode("utf-8")
	print(html)
	

# initialization of imageai
localpath = os.path.dirname(os.path.realpath(__file__))
modelpath = os.path.join(localpath, "models/resnet50_coco_best_v2.1.0.h5")

detector = imageai.Detection.ObjectDetection()
detector.setModelTypeAsRetinaNet()
detector.setModelPath(modelpath)
detector.loadModel(detection_speed="fast")
custom_objects = detector.CustomObjects(person=True)
		
counter = 0	
print("entering listen mode")
SendActivity("intesla_test", "info", "initializing service")	
for line in tail ("-f", "/var/log/vsftpd.log", _iter=True):
	if("OK UPLOAD" in line):
		start = line.find("/files")
		end = line.find(",", start)
		filename = "/home/castle/ftp" + line[start:end-1]

		print("[" + filename + "]")
		if(".jpg" in filename):
			counter = counter + 1
			outfile = "/home/castle/ftp/" + str(counter) + ".jpg"
			output = str(subprocess.check_output("sudo alpr " + filename, shell=True)).replace("\\t", " ").replace("\\n", ";")
			if("No license plates found" in output):
				output = ""
						
			detection = detector.detectCustomObjectsFromImage(custom_objects=custom_objects, input_image=filename, output_image_path=outfile,  minimum_percentage_probability=30)
			for eachItem in detection:
				output = output + eachItem["name"] + " (" + ",".join([str(x) for x in eachItem["box_points"]]) + "); "
			 
			if(len(output) > 1 ):
				output = output + "[ftplink:" + str(counter) + ".jpg]"
				print("Sending: " + output)
				SendActivity("intesla_test", "warning", output)

				
				#session = ftplib.FTP("ftp.pendola.net", "castle@pendola.net", "8anstll!")
				#file = open(outfile, "rb")
				#session.storbinary("STOR " + str(counter) + ".jpg", file)
				#file.close()
				#session.quit()

