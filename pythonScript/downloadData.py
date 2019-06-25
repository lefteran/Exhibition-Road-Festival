# http://jamcams.tfl.gov.uk/00001.09744.mp4
# https://www.tfljamcams.net/
# https://www.trafficdelays.co.uk/a1-a504-finchley-lane-london-cctv-traffic-camera/
# https://londonist.com/london/transport/an-interactive-live-traffic-map-of-london
# https://gridreferencefinder.com/?gr=TQ2679479680|01/000093|0,TQ2613579653|01/000105|0,TQ2639879629|01/000106|0,TQ2661479642|01/000254|0,TQ2710079694|01/000325|0,TQ2760379757|01/000573|0,TQ2761679682|01/000574|0,TQ2679479716|01/000580|0,TQ2739579304|12/000004|0,TQ2607378882|12/000006|0,TQ2585078860|12/000008|0,TQ2536578833|12/000009|0,TQ2623978909|12/000010|0,TQ2559778864|12/000012|0,TQ2650778947|12/000013|0,TQ2554078580|12/000014|0,TQ2548478630|12/000015|0,TQ2575478283|12/000016|0,TQ2688079004|12/000017|0,TQ2652478030|12/000018|0,TQ2676378289|12/000020|0,TQ2721078763|12/000021|0,TQ2700778557|12/000023|0,TQ2627078830|12/000024|0,TQ2631278725|12/000025|0,TQ2565879669|12/000037|0,TQ2576179699|12/000038|0,TQ2714778031|12/000050|0,TQ2724378091|12/000051|0,TQ2644678495|12/000061|0,TQ2656378590|12/000062|0,TQ2558678186|12/000063|0,TQ2653378780|12/000064|0,TQ2681078825|12/000067|0,TQ2717079100|12/000068|0,TQ2688978943|12/000069|0,TQ2757079170|12/000070|0,TQ2535078360|12/000072|0,TQ2540578316|12/000073|0,TQ2603378413|12/000077|0,TQ2623978432|12/000078|0,TQ2641977923|12/000080|0,TQ2726279189|12/000089|0,TQ2727879187|12/000090|0,TQ2685378783|12/000091|0,TQ2678178988|12/000094|0,TQ2593079698|12/000104|0,TQ2593079710|12/000105|0,TQ2600679684|12/000106|0,TQ2600179696|12/000107|0,TQ2746779366|12/000110|0,TQ2747879364|12/000111|0,TQ2760979506|12/000112|0,TQ2766579592|12/000114|0,TQ2542179501|12/000120|0,TQ2550179544|12/000121|0,TQ2756279447|12/000129|0,TQ2755979458|12/000130|0,TQ2567478423|12/000133|0,TQ2536478037|12/000134|0,TQ2559979820|12/000137|0,TQ2535379472|12/000146|0,TQ2574877979|12/000156|0,TQ2586378084|12/000160|0,TQ2739578656|12/000200|0,TQ2734978163|12/000201|0,TQ2560379617|12/000204|0,TQ2559379621|12/000205|0,TQ2670178809|12/000215|0,TQ2545678274|12/000224|0&v=r

import urllib.request
import os
import datetime
import requests
from time import time
import trafficCsvToJson

def downloadJamCams(website, camera, extension, videosFolder):
	now = datetime.datetime.now()
	timestamp = now.strftime("%Y-%m-%d_%H.%M")
	url = website + camera + extension
	print('Downloading  %s.mp4' %camera)
	filePath = videosFolder + "/" + camera + "/" + timestamp + extension
	print("filepath is ", filePath)
	urllib.request.urlretrieve(url, filePath)

def exists(path):
    r = requests.head(path)
    return r.status_code == requests.codes.ok

def downloadTims():
	now = datetime.datetime.now()
	dateNow = now.strftime("%d%m%Y-%H%M%S")
	timeInterval = 1200						# in seconds
	for pastSeconds in range(timeInterval):
		pastSeconds *= (-1)
		past = now + datetime.timedelta(seconds=pastSeconds)
		datePast = past.strftime("%d%m%Y-%H%M%S")
		fileName = "detdata" + past.strftime("%d%m%Y-%H%M%S") + ".csv"
		website = "http://roads.data.tfl.gov.uk/TIMS/"
		url = website + fileName
		filePath = "./pythonScript/TIMS" + "/" + fileName
		if exists(url):
			# print("####### file %s exists ########" %fileName)
			urllib.request.urlretrieve(url, filePath)
			return filePath




if __name__ == "__main__":
	website = "http://jamcams.tfl.gov.uk/00001."
	camerasList = ["06641", "06640", "06595", "06508", "06597", "06607", "06608", "06598"]
	extension = ".mp4"

	videosFolder = "./pythonScript/TfLVideos"
	if not os.path.exists(videosFolder):
		os.makedirs(videosFolder)
	for camera in camerasList:
		cameraFolder = videosFolder + "/" + camera
		if not os.path.exists(cameraFolder):
			os.makedirs(cameraFolder)
	timsFolder = "./pythonScript/TIMS"
	if not os.path.exists(timsFolder):
		os.makedirs(timsFolder)

	# JamCams
	# for camera in camerasList:
	# 	downloadJamCams(website, camera, extension, videosFolder)

	# TIMS
	start_time = time()
	filename1 = 'pythonScript/TIMS/detdata25042019-164522.csv'
	filename2 = downloadTims()
	jsonFilename = 'trafficData.json'

	week1Flows = trafficCsvToJson.getAvgFlows(filename1)
	week2Flows = trafficCsvToJson.getAvgFlows(filename2)
	trafficCsvToJson.exportToJson(jsonFilename, week1Flows, week2Flows)

	print("--- %s seconds ---" % (time() - start_time))

