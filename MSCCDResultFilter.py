import MSCCDTaskData
import FuncIdentification
import ujson, sys, os



def funcExtractor(language):
    res = [] # a list of token bags presenting functions
    

    language     = language
    notationLine_max = 2
    
    
    for projectId in range(len(tokenBagList)):
        for fileId in range(len(tokenBagList[projectId])):
            
            # if not ifPathValid(fileList[projectId][fileId]):
            #     continue
            
            sourceFile = fileList[projectId][fileId]
    
            # extract all functions with their start line and end line
            
            allFuncs = FuncIdentification.getAllFunctionItems(sourceFile, language)
            
            # compare extracted functions with token bags to get the token bags presenting functions using start line and end line
            
            for tokenBag in tokenBagList[projectId][fileId]:
                notationLine = 0
                while notationLine <= notationLine_max:
                    if tokenBag['startLine'] - notationLine in allFuncs:
                        if tokenBag['endLine'] in allFuncs[tokenBag['startLine'] - notationLine]:
                            res.append((tokenBag, allFuncs[tokenBag['startLine'] - notationLine][tokenBag['endLine']]["name"]))
                            break
                    notationLine += 1
                
    return res

def file_level_bag_Extractor():
    res = [] 
    for projectId in range(len(tokenBagList)):
        for fileId in range(len(tokenBagList[projectId])):
            for tokenBag in tokenBagList[projectId][fileId]:
                if tokenBag['granularity'] == 0:
                    res.append(tokenBag)
                    
    return res



# convert a list of token bags into a dict of token bags, which is indexed by the project id, file id and bag id saved in each token bag object.
def tokenBagList2Dict(tokenBagList):
    res = {}
    for tokenBag in tokenBagList:
        projectId = tokenBag['projectId']
        fileId    = tokenBag['fileId']
        bagId     = tokenBag['bagId']
        if projectId not in res:
            res[projectId] = {}
        if fileId not in res[projectId]:
            res[projectId][fileId] = {}
        if bagId not in res[projectId][fileId]:
            res[projectId][fileId][bagId] = tokenBag
    return res


def functionNameFilter(tokenBagList): 
    res = []
    
    filteredFunctionNameList = ["equals", "hashCode", "Reset", "ProtoReflect"]
    
    for tokenBagItem in tokenBagList:
        if tokenBagItem[1] not in filteredFunctionNameList:
            res.append(tokenBagItem[0])
    
    return res


def tokenNumFilter(tokenBagList, minToken):
    res = []
    
    for tokenBag in tokenBagList:
        if tokenBag['tokenNum'] >= minToken:
            res.append(tokenBag)
    
    return res


# if inputed path includes a setted folder name, return false
def ifPathValid(path):
    filteredPathNameList = ["vendor"]
    for name in path.split("/"):
        if name in filteredPathNameList:
            return False
    return True


def ifBagInDict(bagArr, bagDict):
    if bagArr[0] in bagDict:
        if bagArr[1] in bagDict[bagArr[0]]:
            if bagArr[2] in bagDict[bagArr[0]][bagArr[1]]:
                return True
    return False

if __name__ == "__main__":
    # taskId = sys.argv[1]
    # detectionId = sys.argv[2]
    # newDetectionId = sys.argv[3]
    # graunlarity = sys.argv[4]
    # language = sys.argv[5]
    
    taskId = "11010"
    detectionId = "3"
    newDetectionId = "11"
    granularity = "file"
    language = "Java"
    
    tokenBagList = MSCCDTaskData.tokenBagListGeneration(taskId)
    fileList     = MSCCDTaskData.fileListGeneration(taskId)
    
    if granularity == "file":
        filteredTokenBags = tokenBagList2Dict(tokenNumFilter(file_level_bag_Extractor(), 50))
    elif granularity == "function":
        filteredTokenBags = tokenBagList2Dict(functionNameFilter(funcExtractor(language)))
    else:
        print("granularity error")
        sys.exit()
    
    
    
    cloneList = MSCCDTaskData.cloneListGeneration(taskId, detectionId)
    newCloneList = []
    for clonePair in cloneList:
        if not (not ifPathValid(fileList[clonePair[0][0]][clonePair[0][1]]) and not ifPathValid(fileList[clonePair[1][0]][clonePair[1][1]])):
            if ifBagInDict(clonePair[0], filteredTokenBags) and ifBagInDict(clonePair[1], filteredTokenBags):
                    newCloneList.append(clonePair)
    
    newDetection = MSCCDTaskData.MSCCD_PATH + "/tasks/task" + taskId + "/detection" + newDetectionId
    if not os.path.exists(newDetection):
        os.mkdir(newDetection)
    newResultFile = newDetection + "/pairs.file"
    with open(newResultFile,"w") as f:
        for newClone in newCloneList:
            f.write(ujson.dumps(newClone) + "\n")