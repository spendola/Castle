import urllib
import urllib.request
import json
import ssl
import sys
import requests
from pprint import pprint


def SendActivity(client, level, message):
	try:
		context = ssl._create_unverified_context()
		post_data = urllib.parse.urlencode({"key":"1338", "client":client, "level":level, "message":message}).encode('utf-8')
		x = urllib.request.urlopen(url="http://www.intesla.cl/api/castleapi.php", data=post_data, context=context, timeout=15)
		html = x.read().decode("utf-8")
		print(html)
	except:
		print("exception when sending to url")
	
regions = ['gb', 'it'] 
alprtoken = "5a2c38416725033a0bdddf59c956095d3151ff0b"

with open(sys.argv[1], 'rb') as fp:
	response = requests.post('https://api.platerecognizer.com/v1/plate-reader/', data=dict(regions=regions), files=dict(upload=fp), headers={'Authorization': "TOKEN " + alprtoken})

#pprint(response.json())
#print(" ")

results = response.json()["results"]
for result in results:
	plate = None
	vehicle = "indeterminado"
	if("plate" in result):
		plate = result["plate"].upper()
	if("vehicle" in result and "type" in result["vehicle"]):
		vehicle = result["vehicle"]["type"]
	
	if(plate is not None):
		print(vehicle + " con patente " + plate)
		SendActivity("intesla_test", "warning", vehicle + " con patente " + plate)



