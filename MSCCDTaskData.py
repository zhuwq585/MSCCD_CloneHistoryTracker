import ujson
MSCCD_PATH = "/Users/syu/workspace/MSCCD/"

def fileListGeneration(taskId):
    fileListPath = MSCCD_PATH + "/tasks/task" + str(taskId) + "/fileList.txt"
    res = []
    splitTmp = None
    for dataLine in open(fileListPath,"r").readlines():
        splitTmp = dataLine[:-1].split(",")
        projectId = int(splitTmp[0])
        while len(res) - 1 < projectId:
            res.append([])
        res[projectId].append(splitTmp[1])

    return res


def cloneListGeneration(taskId, detectionId):
    clonePath = MSCCD_PATH + "/tasks/task" + str(taskId) + "/detection" + str(detectionId) + "/pairs.file"
    res = []
    for cloneLine in open(clonePath, "r").readlines():
        cloneClass = ujson.loads(cloneLine[:-1])
        # if cloneFilter(cloneClass[0], fileListArr):
        res.append(cloneClass)
    return res

def tokenBagListGeneration(taskId):
    # not gain all the informations, only line number range
    sourcePath = MSCCD_PATH + "/tasks/task" + str(taskId) + "/tokenBags"
    res = []
    splitTmp = None
    for sourceline in open(sourcePath,"r").readlines():
        splitTmp  = sourceline[:-1].split("@ @")
        projectId = int(splitTmp[0])
        fileId    = int(splitTmp[1])
        bagId     = int(splitTmp[2])
        lineArr   = splitTmp[7].split(": :")
        startLine = int(lineArr[0])
        endLine   = int(lineArr[1])
        
        bag = {
            "projectId" : projectId,
            "fileId"    : fileId,
            "bagId"     : bagId,
            "startLine" : startLine,
            "endLine"   : endLine,
            "tokenNum"  : int(splitTmp[6]),
            "granularity" : int(splitTmp[3])
        }
        
        while len(res) - 1 < projectId:
            res.append([])
        while len(res[projectId]) - 1 < fileId:
            res[projectId].append([])
        res[projectId][fileId].append( bag  )
        if bagId != len(res[projectId][fileId]) - 1:
            print("err")
    
    return res

def getConfigObj(taskId):
    configPath = MSCCD_PATH + "/tasks/task" + str(taskId) + "/config.json"
    return ujson.loads(open(configPath,"r").read())