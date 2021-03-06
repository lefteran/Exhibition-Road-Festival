import os.path
from time import time
import datetime

def initFlowsDict():
    flowsDict = {
        '01/093': [],
        '12/017': [],
        '12/114': [],
        '12/004': [],
        '12/013': [],
        '12/010': [],
    }
    return flowsDict


def getFlows(filename, flowsDict):
    fp = open(filename,"r")
    next(fp)
    for line in fp:
        elements = line.split(",")
        node = elements[1].strip()
        if node in flowsDict:
            flow = int(elements[4].strip())
            flowsDict[node].append(flow)
    fp.close()


def calculateAvgFlowList(flowsDict):
    avgFlowList = []
    for _, flowList in flowsDict.items():
        if flowList:
            avgFlow = sum(flowList) / len(flowList)
            avgFlowList.append(avgFlow)
        else:
            avgFlowList.append(0)
    return avgFlowList



def exportFixedWeekToJson(filename, avgFlowList):
    fp = open(filename,"w")
    fp.write("data = \'[")
    for i in range(len(avgFlowList)):
        if i!=0:
            fp.write("\t")
        fp.write("{\"week1\" : \"%.2f\"}" %avgFlowList[i])
        if i!= len(avgFlowList)-1:
            fp.write(",\\\n")
        else:
            fp.write("\\\n")
    fp.write("\t]';")
    fp.close()

def exportToJson(filename, week1Flows, week2Flows):
    fp = open(filename,"w")
    fp.write("data = \'[")
    for i in range(len(week1Flows)):
        if i!=0:
            fp.write("\t")
        fp.write("{\"week1\" : \"%.2f\", \"week2\" : \"%.2f\"}" %(week1Flows[i], week2Flows[i]))
        if i!= len(week1Flows)-1:
            fp.write(",\\\n")
        else:
            fp.write("\\\n")
    fp.write("\t]';")
    fp.close()

# timsPath = os.path.abspath(os.path.join(os.pardir, "exhibitionFestival/TIMS"))
# timsPath = os.path.abspath(os.path.join(os.getcwd(), "pythonScript/TIMS"))


def getFixedWeekFlowsDict():
    print("Preparing traffic json data for last weekend ...")
    flowsDict = initFlowsDict()
    count = 0
    # saturdayPath = os.path.join(os.getcwd(), "pythonScript\Saturday_traffic")
    saturdayPath = "d:\\Github\\Exhibition-Road-Festival\\pythonScript\\Saturday_traffic"
    saturdayList = os.listdir(saturdayPath)
    for filename in saturdayList:
        count += 1
        filePath = saturdayPath + "\\" + filename
        # print("%d. Saturday file %s" %(count, filePath))
        getFlows(filePath, flowsDict)

    count = 0
    sundayPath = os.path.join(os.getcwd(), "pythonScript\Sunday_traffic")
    sundayPath = "d:\\Github\\Exhibition-Road-Festival\\pythonScript\\Sunday_traffic"
    sundayList = os.listdir(sundayPath)
    for filename in sundayList:
        count += 1
        filePath = sundayPath + "\\" + filename
        # print("%d. Sunday file %s" %(count, filePath))
        getFlows(filePath, flowsDict)
    return flowsDict


def getTodaysFlowsDict():
    print("Preparing today's traffic json data ...")
    flowsDict = initFlowsDict()
    count = 0
    now = datetime.datetime.now()
    day = now.strftime("%d")
    if day == '28':
        todaysDir = "\\traffic2806"
    elif day == '29':
        todaysDir = "\\traffic2906"
    else:
        todaysDir = "\\traffic3006"
    # todaysPath = os.path.join(os.getcwd(), todaysDir)
    todaysPath = "d:\\Github\\Exhibition-Road-Festival\\pythonScript" + todaysDir
    todaysList = os.listdir(todaysPath)
    for filename in todaysList:
        count += 1
        filePath = todaysPath + "\\" + filename
        # print("%d. Today's file %s" %(count, filePath))
        getFlows(filePath, flowsDict)
    return flowsDict

def getTrafficJsonFile():
    # start_time = time()
    print("Preparing traffic json file...")
    fixedWeekFlowsDict = getFixedWeekFlowsDict()
    fixedWeekAvgFlowList = calculateAvgFlowList(fixedWeekFlowsDict)
    todayFlowsDict = getTodaysFlowsDict()
    todayFlowList = calculateAvgFlowList(todayFlowsDict)
    exportToJson("trafficData.json", fixedWeekAvgFlowList,todayFlowList)
    # print("--- %s seconds ---" % (time() - start_time))


# getTrafficJsonFile()