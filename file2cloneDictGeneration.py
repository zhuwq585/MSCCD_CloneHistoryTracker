from MSCCDTaskData import * 
from FuncIdentification import getAllFunctionItems

import os,sys,ujson


def calculateFileCoverage(cloneSengmentList, fileLength):
    cloneSengmentList.sort()
    coverage = 0
    lastEndLine = 0
    for cloneSengment in cloneSengmentList:
        startLine = cloneSengment[0]
        endLine   = cloneSengment[1]
        if startLine > lastEndLine:
            coverage += endLine - startLine + 1
        else:
            coverage += endLine - lastEndLine
        lastEndLine = max(lastEndLine, endLine)
    coverage = float(coverage) / fileLength
    if coverage > 1:
        coverage = 1
    return coverage

# def getLOCUsingCLOC(filePath):
#     cmd = "cloc " + filePath + " --json --timeout 0"
#     res = os.popen(cmd).read()
#     try:
#         res = ujson.loads(res)
#         res = res['SUM']['code']
#     except ujson.JSONDecodeError:
#         res = 0
    
#     return int(res)

    
def main(taskId, detectionId):
    # taskId          = "20005"
    # detectionId = "1"

    # language        = sys.argv[3]
    # detectionId_fun = sys.argv[4]
    
    
    tokenBagList  = tokenBagListGeneration(taskId)
    
    fileList = fileListGeneration(taskId)
    ### Generate single id for each file from their double id (pId, fId)
    projId2SingleId = {}
    singleId2DoubleId = []
    for projectId in range(len(fileList)):
        for fileId in range(len(fileList[projectId])):
                singleId = len(singleId2DoubleId)
                singleId2DoubleId.append((projectId, fileId))
                filePath = fileList[projectId][fileId]
                fileList[projectId][fileId] = {
                    "singleId" : singleId,
                    "filePath" : filePath,
                    # "length"   : getLOCUsingCLOC(filePath)
                    "length"   : len(open(filePath, "r", errors="ignore").readlines())
                }
                # singleId2TurpleId[singleId]['singleId'] = singleId
                
                if not projectId in projId2SingleId:
                    projId2SingleId[projectId] = []
                projId2SingleId[projectId].append(singleId)
                
      
    cloneDict_file = {}  
    
    cloneList = cloneListGeneration(taskId, detectionId) 
    for cloneIndex in range(len(cloneList)):
        if cloneList[cloneIndex][0][0] == cloneList[cloneIndex][1][0]: ## filter out inner-project clones
            continue
        
        cloneItem1 = cloneList[cloneIndex][0]
        cloneItem2 = cloneList[cloneIndex][1]
        
        
        singleId1 = fileList[cloneItem1[0]][cloneItem1[1]]['singleId']
        singleId2 = fileList[cloneItem2[0]][cloneItem2[1]]['singleId']
        
        ## make sure singleId1 < singleId2 
        if singleId2 < singleId1:
            singleId1, singleId2 = singleId2, singleId1
            cloneItem1, cloneItem2 = cloneItem2, cloneItem1
        
        if not singleId1 in cloneDict_file:
            cloneDict_file[singleId1] = {}
            
        if not singleId2 in cloneDict_file[singleId1]:
            cloneDict_file[singleId1][singleId2] = {
                "clonedSegment1" : [],
                "clonedSegment2" : [],
                "clonedSegmentNum" : 0,
                "relatedCloneIndex" : []
            }
        
        
        tokenBag1 = tokenBagList[cloneItem1[0]][cloneItem1[1]][cloneItem1[2]]
        tokenBag2 = tokenBagList[cloneItem2[0]][cloneItem2[1]][cloneItem2[2]]
        
        cloneDict_file[singleId1][singleId2]['clonedSegment1'].append((tokenBag1['startLine'], tokenBag1['endLine']))
        cloneDict_file[singleId1][singleId2]['clonedSegment2'].append((tokenBag2['startLine'], tokenBag2['endLine']))
        cloneDict_file[singleId1][singleId2]['clonedSegmentNum'] += 1
        cloneDict_file[singleId1][singleId2]['relatedCloneIndex'].append(cloneIndex)
        
    
    # calculate max coverage for each clone pair
    for singleId1 in cloneDict_file:
        for singleId2 in cloneDict_file[singleId1]:
            cloneDict_file[singleId1][singleId2]['coverage1'] = calculateFileCoverage(cloneDict_file[singleId1][singleId2]['clonedSegment1'], fileList[singleId2DoubleId[singleId1][0]][singleId2DoubleId[singleId1][1]]['length'])
            cloneDict_file[singleId1][singleId2]['coverage2'] = calculateFileCoverage(cloneDict_file[singleId1][singleId2]['clonedSegment2'],fileList[singleId2DoubleId[singleId2][0]][singleId2DoubleId[singleId2][1]]['length'])
        
            cloneDict_file[singleId1][singleId2]['coverage'] = max(cloneDict_file[singleId1][singleId2]['coverage1'], cloneDict_file[singleId1][singleId2]['coverage2'])

    
    
    
    res = []
    for singleId1 in cloneDict_file:
        for singleId2 in cloneDict_file[singleId1]:
            res.append((cloneDict_file[singleId1][singleId2]['coverage'],singleId1,singleId2, cloneDict_file[singleId1][singleId2]))
    res.sort()
    res.reverse()
    
    with open("/Users/syu/workspace/MSCCD_CloneHistoryTracker/reports/" + taskId + "-" + detectionId + "/cloneDict_file" + ".txt", "w") as f:
        f.write("taskId:" + str(taskId) + " detectionId:" + str(detectionId) + "\n")
        for item in res:
            f.write("#########" + "\n")
            filePath1 = fileList[singleId2DoubleId[item[1]][0]][singleId2DoubleId[item[1]][1]]['filePath']
            filePath2 = fileList[singleId2DoubleId[item[2]][0]][singleId2DoubleId[item[2]][1]]['filePath']
            f.write("Related clone index:" + str(item[3]['relatedCloneIndex']) + "\n")
            f.write(filePath1 + "\n")
            f.write(str(item[3]['clonedSegment1']) + "\n")
            f.write(filePath2 + "\n")
            f.write(str(item[3]['clonedSegment2']) + "\n")
            f.write("Coverage:" + str(item[3]['coverage']) + "\n\n")
    
    return fileList,singleId2DoubleId,cloneDict_file
            
    
    
if __name__ == "__main__":
    main( sys.argv[1], sys.argv[2])
