import os
from openalpr import Alpr

def main():
	print("Castle Server")
	localPath = os.path.dirname(os.path.realpath(__file__))
	
	confpath = os.path.join(localPath, "openalpr/config")
	runtimepath = os.path.join(localPath, "openalpr/runtime_data")
	alpr = Alpr("us", confpath, runtimepath)
	
	if(not alpr.is_loaded()):
		print("Error loading OpenALPR")
		sys.exit(1)

	alpr.unload()
	
if __name__ == "__main__": 
	main()



#  if not alpr.is_loaded():
#      print("Error loading OpenALPR")
#      sys.exit(1)
# 
#  alpr.set_top_n(20)
#  alpr.set_default_region("md")
# 
#  results = alpr.recognize_file("/path/to/image.jpg")
# 
#  i = 0
#  for plate in results['results']:
#      i += 1
#      print("Plate #%d" % i)
#      print("   %12s %12s" % ("Plate", "Confidence"))
#      for candidate in plate['candidates']:
#          prefix = "-"
#          if candidate['matches_template']:
#              prefix = "*"
# 
#          print("  %s %12s%12f" % (prefix, candidate['plate'], candidate['confidence']))
# 
#  # Call when completely done to release memory
#  alpr.unload()