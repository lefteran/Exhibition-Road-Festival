import downloadTrafficData
import trafficCsvToJson
from time import sleep
from datetime import datetime

for i in range(4):
    downloadTrafficData.downloadCurrentTrafficData()
    trafficCsvToJson.getTrafficJsonFile()
    sleep(800)
now = datetime.now()
print(now)
