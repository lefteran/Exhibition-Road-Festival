# http://jamcams.tfl.gov.uk/00001.09744.mp4
# https://www.tfljamcams.net/
# https://www.trafficdelays.co.uk/a1-a504-finchley-lane-london-cctv-traffic-camera/
# https://londonist.com/london/transport/an-interactive-live-traffic-map-of-london
import urllib.request
import os
import datetime

def download_file(website, camera, extension, mainFolder):
	now = datetime.datetime.now()
	timestamp = now.strftime("%Y-%m-%d_%H.%M")
	url = website + camera + extension
	print('Downloading  %s.mp4' %camera)
	# name = mainFolder + camera
	filePath = mainFolder + "/" + camera + "/" + timestamp + extension
	print("filepath is ", filePath)
	urllib.request.urlretrieve(url, filePath)



website = "http://jamcams.tfl.gov.uk/00001."
camerasList = ["06641", "06640", "06595", "06508", "06597", "06607", "06608", "06598"]
extension = ".mp4"

mainFolder = "./TfLVideos"
if not os.path.exists(mainFolder):
	os.makedirs(mainFolder)
for camera in camerasList:
	cameraFolder = mainFolder + "/" + camera
	if not os.path.exists(cameraFolder):
		os.makedirs(cameraFolder)


for camera in camerasList:
	download_file(website, camera, extension, mainFolder)