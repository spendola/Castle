import numpy as np
import cv2
import os
import sys
import urllib
import urllib.request
import ssl
import requests
import threading
		
def SendActivity(client, level, message):
	def callback():
		try:
			context = ssl._create_unverified_context()
			post_data = urllib.parse.urlencode({"key":"1338", "client":client, "level":level, "message":message}).encode('utf-8')
			x = urllib.request.urlopen(url="http://www.intesla.cl/api/castleapi.php", data=post_data, context=context, timeout=10)
			html = x.read().decode("utf-8")
			print(html)
		except:
			print("exception when sending to url")
	thread = threading.Thread(target=callback)
	thread.start()
	
		
hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

localpath = os.path.dirname(os.path.realpath(__file__))
image = cv2.imread(os.path.join(localpath, sys.argv[1]))
image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
boxes, weights = hog.detectMultiScale(image, winStride=(8,8) )
boxes = np.array([[x, y, x + w, y + h] for (x, y, w, h) in boxes])

print(len(boxes))
if(len(boxes) > 0):
	for box in boxes:
		message = "Persona detectada en " + str(box[0]) + ", " + str(box[1]) + ", " + str(box[2]) + ", " + str(box[3])
		print(message)
		SendActivity("intesla_test", "warning", message)