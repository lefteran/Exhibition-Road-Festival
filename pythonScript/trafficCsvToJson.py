import os.path

def getAvgFlows(filename):
    timsNodeFlowsDict = {
        '01/093': [],
        '12/017': [],
        '12/114': [],
        '12/004': [],
        '12/013': [],
        '12/010': [],
    }
    fp = open(filename,"r")
    for line in fp:
        elements = line.split(",")
        node = elements[1].strip()
        if node in timsNodeFlowsDict:
            flow = int(elements[4].strip())
            timsNodeFlowsDict[node].append(flow)
    fp.close()

    avgFlowList = []
    for _, flowList in timsNodeFlowsDict.items():
        if flowList:
            avgFlow = sum(flowList) / len(flowList)
            avgFlowList.append(avgFlow)
        else:
            avgFlowList.append(0)
    return avgFlowList


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
# filename1 = timsPath + '\\detdata25042019-164522.csv'
# filename2 =  timsPath + '\\detdata27052019-000017.csv'
