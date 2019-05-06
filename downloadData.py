# http://jamcams.tfl.gov.uk/00001.09744.mp4
# https://www.tfljamcams.net/
# https://www.trafficdelays.co.uk/a1-a504-finchley-lane-london-cctv-traffic-camera/
# https://londonist.com/london/transport/an-interactive-live-traffic-map-of-london
import urllib.request
import os
import datetime
import requests
import time

def downloadJamCams(website, camera, extension, videosFolder):
	now = datetime.datetime.now()
	timestamp = now.strftime("%Y-%m-%d_%H.%M")
	url = website + camera + extension
	print('Downloading  %s.mp4' %camera)
	# name = videosFolder + camera
	filePath = videosFolder + "/" + camera + "/" + timestamp + extension
	print("filepath is ", filePath)
	urllib.request.urlretrieve(url, filePath)



def exists(path):
    r = requests.head(path)
    return r.status_code == requests.codes.ok

def downloadTims():
	now = datetime.datetime.now()
	dateNow = now.strftime("%d%m%Y-%H%M%S")
	# print("dateNow is ", dateNow)
	timeInterval = 1200						# in seconds
	for pastSeconds in range(timeInterval):
		# print("second: %s" %pastSeconds)
		pastSeconds *= (-1)
		past = now + datetime.timedelta(seconds=pastSeconds)
		# print("past is ", past)
		datePast = past.strftime("%d%m%Y-%H%M%S")
		# print("datePast is ", datePast)
		fileName = "detdata" + past.strftime("%d%m%Y-%H%M%S") + ".csv"
		website = "http://roads.data.tfl.gov.uk/TIMS/"
		url = website + fileName
		filePath = "./TIMS" + "/" + fileName
		if exists(url):
			print("####### file %s exists ########" %fileName)
			urllib.request.urlretrieve(url, filePath)
		# print("fileName is %s" %fileName)
	# print("day is %s, month is %s, year is %s" %(day, month, year))
	# CHECK IN AN INTERVAL OF 20 MINUTES (1200 SECONDS)
	# BEFORE DOWNLOADING CHECK IF THE FILE ALREADY EXISTS
	# RUN THE ABOVE EVERY 5 MINUTES (WAIT FUNCTION)  





website = "http://jamcams.tfl.gov.uk/00001."
camerasList = ["06641", "06640", "06595", "06508", "06597", "06607", "06608", "06598"]
extension = ".mp4"

videosFolder = "./TfLVideos"
if not os.path.exists(videosFolder):
	os.makedirs(videosFolder)
for camera in camerasList:
	cameraFolder = videosFolder + "/" + camera
	if not os.path.exists(cameraFolder):
		os.makedirs(cameraFolder)
timsFolder = "./TIMS"
if not os.path.exists(timsFolder):
	os.makedirs(timsFolder)

# JamCams
# for camera in camerasList:
# 	downloadJamCams(website, camera, extension, videosFolder)

# TIMS
start_time = time.time()
downloadTims()
print("--- %s seconds ---" % (time.time() - start_time))






# Traffic counters


