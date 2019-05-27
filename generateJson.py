# timsNodesDict = {
#     'Kensington Rd/Exhibition Rd': '01/093',
#     'Exhibition Rd/Cromwell Rd': '12/017',
#     'Brompton Rd': '12/114',
#     'Brompton Rd/Beaufort Grns': '12/004',
#     'A4 Cromwell Rd/Queens Gate': '12/013',
#     'A4 Cromwell Rd/Gloucester Rd': '12/010',
# }
# invTimsNodesDict = {value: key for key, value in timsNodesDict.items()}


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
        fp.write("{\"week1\" : \"%f\", \"week2\" : \"%f\"}" %(week1Flows[i], week2Flows[i]))
        if i!= len(week1Flows)-1:
            fp.write(",\\\n")
        else:
            fp.write("\\\n")
    fp.write("\t]';")
    fp.close()


if __name__ == "__main__":
    filename1 = './TIMS/detdata25042019-164522.csv'
    filename2 = './TIMS/detdata27052019-000017.csv'
    jsonFilename = 'data.json'

    week1Flows = getAvgFlows(filename1)
    week2Flows = getAvgFlows(filename2)
    exportToJson(jsonFilename, week1Flows, week2Flows)