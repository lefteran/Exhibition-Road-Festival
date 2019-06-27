import os.path
import re

def initSensorEmissionsDict():
    sensorEmissionsDict = {
        'no2': [],
        'pm10': [],
        'pm25': []
    }
    return sensorEmissionsDict


def getAvgEmissionsList(emissionsDict):
    avgEmissionsDict = {}
    avgEmissionsList = []
    for emissionsKey, emissionsList in emissionsDict.items():
        if emissionsList:
            avgEmissions = sum(emissionsList) / len(emissionsList)
            avgEmissionsDict[emissionsKey] = avgEmissions
        else:
            avgEmissionsDict[emissionsKey] = 0
    avgEmissionsList.append(avgEmissionsDict['no2'])
    avgEmissionsList.append(avgEmissionsDict['pm10'])
    avgEmissionsList.append(avgEmissionsDict['pm25'])
    return avgEmissionsList


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


def dictOfTheDay(daysPath):
    dictOfTheDay = {}
    daysFileList = os.listdir(daysPath)
    for filename in daysFileList:
        sensorId = getSensorId(filename)
        filePath = daysPath + "\\" + filename
        emissionsDict = initSensorEmissionsDict()
        getEmissions(filePath, emissionsDict)
        avgEmissionsList = getAvgEmissionsList(emissionsDict)
        dictOfTheDay[sensorId] = avgEmissionsList
    return dictOfTheDay


def getAllDaysListOfDicts():
    listOfDicts = []
    saturday1EmissionsPath = os.path.join(os.getcwd(), "pythonScript\\weekday_emissions\\saturday1")
    sunday1EmissionsPath = os.path.join(os.getcwd(), "pythonScript\\weekday_emissions\\sunday1")
    mondayEmissionsPath = os.path.join(os.getcwd(), "pythonScript\\weekday_emissions\\monday")
    tuesdayEmissionsPath = os.path.join(os.getcwd(), "pythonScript\\weekday_emissions\\tuesday")
    wednesdayEmissionsPath = os.path.join(os.getcwd(), "pythonScript\\weekday_emissions\\wednesday")
    thursdayEmissionsPath = os.path.join(os.getcwd(), "pythonScript\\weekday_emissions\\thursday")
    fridayEmissionsPath = os.path.join(os.getcwd(), "pythonScript\\weekday_emissions\\friday")
    saturday2EmissionsPath = os.path.join(os.getcwd(), "pythonScript\\weekday_emissions\\saturday2")
    sunday2EmissionsPath = os.path.join(os.getcwd(), "pythonScript\\weekday_emissions\\sunday2")

    saturday1EmissionsDict = dictOfTheDay(saturday1EmissionsPath)
    listOfDicts.append(saturday1EmissionsDict)
    sunday1EmissionsDict = dictOfTheDay(sunday1EmissionsPath)
    listOfDicts.append(sunday1EmissionsDict)
    mondayEmissionsDict = dictOfTheDay(mondayEmissionsPath)
    listOfDicts.append(mondayEmissionsDict)
    tuesdayEmissionsDict = dictOfTheDay(tuesdayEmissionsPath)
    listOfDicts.append(tuesdayEmissionsDict)
    wednesdayEmissionsDict = dictOfTheDay(wednesdayEmissionsPath)
    listOfDicts.append(wednesdayEmissionsDict)
    thursdayEmissionsDict = dictOfTheDay(thursdayEmissionsPath)
    listOfDicts.append(thursdayEmissionsDict)
    fridayEmissionsDict = dictOfTheDay(fridayEmissionsPath)
    listOfDicts.append(fridayEmissionsDict)
    saturday2EmissionsDict = dictOfTheDay(saturday2EmissionsPath)
    listOfDicts.append(saturday2EmissionsDict)
    sunday2EmissionsDict = dictOfTheDay(sunday2EmissionsPath)
    listOfDicts.append(sunday2EmissionsDict)
    return listOfDicts