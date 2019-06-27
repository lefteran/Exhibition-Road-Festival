import os.path
import re
import emissionsLineChartCsvToJson

def initSensorEmissionsDict():
    sensorEmissionsDict = {
        'no2': [],
        'pm10': [],
        'pm25': []
    }
    return sensorEmissionsDict


# THIS CALCULATES THE AVERAGE FOR ONLY ONE SENSOR
def calculateSensorAvgEmissionList(emissionsDict):
    avgEmissionList = []
    for _, emissionsList in emissionsDict.items():
        if emissionsList:
            avgEmissions = sum(emissionsList) / len(emissionsList)
            avgEmissionList.append(avgEmissions)
        else:
            avgEmissionList.append(0)
    return avgEmissionList



def getEmissions(filename, emissionsDict):
    fp = open(filename,"r")
    next(fp)
    for line in fp:
        elements = line.split(",")
        no2 = float(elements[2].strip().replace('"', ''))
        pm10 = float(elements[5].strip().replace('"', ''))
        pm25 = float(elements[8].strip().replace('"', ''))
        emissionsDict['no2'].append(no2)
        emissionsDict['pm10'].append(pm10)
        emissionsDict['pm25'].append(pm25)
    fp.close()



def getSensorId(filename):
    return re.search('-(.*)_', filename).group(1)

def getSensorDataToExport(weekendSensorsEmissionsDict, todaysSensorsEmissionsDict):
    sensorDataDict = {}
    for sensorKey, _ in weekendSensorsEmissionsDict.items():
        sensorDataDict[sensorKey] = []
    for sensorKey, _ in sensorDataDict.items():
        sensorDataDict[sensorKey].extend(weekendSensorsEmissionsDict[sensorKey])
        sensorDataDict[sensorKey].extend(todaysSensorsEmissionsDict[sensorKey])
    return sensorDataDict


def exportAvgEmissionsToJson(filename, weekendSensorsEmissionsDict, todaysSensorsEmissionsDict, weekdayListOfDicts):
    fp = open(filename,"w")
    fp.write("data = \'[")
    sensorDataDict = getSensorDataToExport(weekendSensorsEmissionsDict, todaysSensorsEmissionsDict)
    count = 0
    for _, sensorList in sensorDataDict.items():
        if count!=0:
            fp.write("\t")
        fp.write("{\"no2Old\" : \"%.2f\", \"no2New\" : \"%.2f\", \"pm10Old\" : \"%.2f\", \"pm10New\" : \"%.2f\", \"pm25Old\" : \"%.2f\", \"pm25New\" : \"%.2f\"}"\
        %(sensorList[0], sensorList[3], sensorList[1], sensorList[4], sensorList[2], sensorList[5]))
        # if count!= len(sensorDataDict)-1:
        fp.write(",\\\n")
        # else:
        #     fp.write("\\\n")
        count += 1
    day = 0
    for dictOfDay in weekdayListOfDicts:
        day += 1
        if dictOfDay:
            fp.write("\t{\"no2_33\" : \"%.2f\", \"pm10_33\" : \"%.2f\", \"pm25_33\" : \"%.2f\", "\
            %(dictOfDay['2033150'][0], dictOfDay['2033150'][1], dictOfDay['2033150'][2]))
            
            fp.write("\"no2_37\" : \"%.2f\", \"pm10_37\" : \"%.2f\", \"pm25_37\" : \"%.2f\", "\
            %(dictOfDay['2037150'][0], dictOfDay['2037150'][1], dictOfDay['2037150'][2]))
            
            fp.write("\"no2_39\" : \"%.2f\", \"pm10_39\" : \"%.2f\", \"pm25_39\" : \"%.2f\"}"\
            %(dictOfDay['2039150'][0], dictOfDay['2039150'][1], dictOfDay['2039150'][2]))
        else:
            fp.write("\t{\"no2_33\" : \"\", \"pm10_33\" : \"\", \"pm25_33\" : \"\", ")
            fp.write("\"no2_37\" : \"\", \"pm10_37\" : \"\", \"pm25_37\" : \"\", ")
            fp.write("\"no2_39\" : \"\", \"pm10_39\" : \"\", \"pm25_39\" : \"\"}")
        if day != len(weekdayListOfDicts):
            fp.write(",\\\n")
        else:
            fp.write("\\\n")
    fp.write("\t]';")
    fp.close()


def getAllSensorsEmissionsDict(emissionsPath):
    allSensorsEmissionsDict = {}
    emissionsFileList = os.listdir(emissionsPath)
    for filename in emissionsFileList:
        emissionsDict = initSensorEmissionsDict()
        sensorId = getSensorId(filename)
        filePath = emissionsPath + "\\" + filename
        getEmissions(filePath, emissionsDict)
        avgSensorEmissionList = calculateSensorAvgEmissionList(emissionsDict)
        allSensorsEmissionsDict[sensorId] = avgSensorEmissionList
    return allSensorsEmissionsDict



weekendEmissionsPath = os.path.join(os.getcwd(), "pythonScript\\weekend_emissions")
todaysEmissionsPath = os.path.join(os.getcwd(), "pythonScript\\todays_emissions")
weekendSensorsEmissionsDict = getAllSensorsEmissionsDict(weekendEmissionsPath)
todaysSensorsEmissionsDict = getAllSensorsEmissionsDict(todaysEmissionsPath)
weekdayListOfDicts = emissionsLineChartCsvToJson.getAllDaysListOfDicts()

exportAvgEmissionsToJson("emissionData.json", weekendSensorsEmissionsDict, todaysSensorsEmissionsDict, weekdayListOfDicts)
