# This script intends to save videos from traffic cameras for a time lag t
# 23/01/2019 by Clemence Le Cornec (Imperial College London)

import time
import datetime
import requests
import os

# Directory where to save the data
pathSave = "./TfLVideos/"

# Recording time
recordingTime = 15 * 60 # in seconds
intervalBetweenRecords = 5 * 60 # in seconds
elapsedTime = 0

# URL of the mp4 records
urlCameras = "https://s3-eu-west-1.amazonaws.com/jamcams.tfl.gov.uk/00001."

# Camera list (03611 is London Road / Thomas Doyle St and 03612 is St Georges Road/Hayles St
camerasList = ["03611.mp4", "03612.mp4"]

# Function to download from web
def download_file(url, pathSave):
	# local_filename = url.split('/')[-1].split(".")[1] + "_" + str(datetime.datetime.now()) + "." + url.split('/')[-1].split(".")[2]
	local_filename = "test.mp4"
	r = requests.get(url, stream=True)
	with open(pathSave + local_filename, 'wb') as f:
		for chunk in r.iter_content(chunk_size=512): 
			if chunk: 
				f.write(chunk)
	return local_filename
	
# If the folder to save the results doesn't exist, create it
if not os.path.exists(pathSave):
	os.makedirs(pathSave)

# Start timer	
start = datetime.datetime.now()

print("Recording started", datetime.datetime.now())

# While loop to record the videos
while elapsedTime < recordingTime:

	current = datetime.datetime.now()

	for j in range(0,len(camerasList)):
		
		download_file(url = urlCameras + camerasList[j], pathSave = pathSave)
		
	elapsedTime = (current - start).total_seconds()
	
	print("Elapsed time: ", elapsedTime)
	
	# Sleep between two records
	time.sleep(intervalBetweenRecords)

print("Recording ended", datetime.datetime.now())
	

