#!flask/bin/python
from flask import Flask
from flask import request
from flask import jsonify
import PIL.Image
import numpy as np
import pymysql
import zlib
import json
import io
import gzip
import PlateRecognition as PlateRecognition


# Service Definition
app = Flask(__name__)
@app.route('/', methods = ['POST'])

def main():
	
	try:
		data = request.get_data()
		data = bytearray(data)
		data = np.asarray(data, dtype=np.uint8)
		data = data.reshape(800, 600)
		return "good_image"
	except:
		return "bad_image_shape"
		
	

if __name__ == "__main__":
	print("Initializing Castle")
	Preload()
	app.run(host="0.0.0.0", port=9000)