import os
import json
from openalpr import Alpr

def main():
	print("Castle Server")

	alpr = Alpr("us", "/etc/openalpr/openalpr.conf", "/usr/share/openalpr/runtime_data")
	if not alpr.is_loaded():
		print("Error loading OpenALPR")
		sys.exit(1)
	results = alpr.recognize_file("/path/to/image.jpg")
	print(json.dumps(results, indent=4))
	alpr.unload()
	
if __name__ == "__main__": 
	main()
