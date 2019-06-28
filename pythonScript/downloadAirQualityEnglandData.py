
import urllib.request
import os
import datetime
import requests
from time import time
import webbrowser

def exists(path):
    r = requests.head(path)
    return r.status_code == requests.codes.ok


def firstStep():
	startDate = "2019-06-28"
	endDate = "2019-06-28"
	website = "https://www.airqualityengland.co.uk/site/data.php?site_id=KC2&parameter_id%5B%5D=NO2&f_query_id=1314247&data=%3C%3Fphp+print+htmlentities%28%24data%29%3B+%3F%3E&f_date_started="
	url = website + startDate + "&f_date_ended=" + endDate + "&la_id=291&action=download&submit=Download+Data"
	# webbrowser.open(url)
	now = datetime.datetime.now()
	dateNow = now.strftime("%d%m%Y-%H%M%S")
	return dateNow

def secondStep(dateNow):
	now = datetime.datetime.now()
	startDate = "2019-06-28"
	timeInterval = 120						# in seconds
	for pastSeconds in range(timeInterval):
		pastSeconds *= (-1)
		past = now + datetime.timedelta(seconds=pastSeconds)
		pastTime = past.strftime("%H%M%S")
		# print("pastTime is ", pastTime)
	
	day = now.strftime("%d")
	# timeOfDataCreation = "103446"
	timestamp = "1906" + day + pastTime
	website = "https://www.airqualityengland.co.uk/assets/downloads/"
	url = website + startDate + "-" + timestamp + ".csv"



	# now = datetime.datetime.now()
	# dateNow = now.strftime("%d%m%Y-%H%M%S")
	# timeInterval = 1200						# in seconds
	# for pastSeconds in range(timeInterval):
	# 	pastSeconds *= (-1)
	# 	past = now + datetime.timedelta(seconds=pastSeconds)
	# 	datePast = past.strftime("%d%m%Y-%H%M%S")
	# 	fileName = "detdata" + past.strftime("%d%m%Y-%H%M%S") + ".csv"
	# 	website = "http://roads.data.tfl.gov.uk/TIMS/"
	# 	url = website + fileName
	# 	filePath = "./pythonScript/TIMS" + "/" + fileName
	# 	if exists(url):
	# 		# print("####### file %s exists ########" %fileName)
	# 		urllib.request.urlretrieve(url, filePath)
	# 		return filePath



dateNow = firstStep()
secondStep(dateNow)
