import sys,os,ujson, random, time
from MSCCDTaskData import *
from FuncIdentification import *
from GitUsage import *
MSCCD_PATH = "/Users/syu/workspace/MSCCD/"

def similarityCalculation(filePath1, startLine1, endLine1, filePath2, startLine2, endLine2, keywordsListPath, grammarName ):
    if startLine1 == -1 or startLine2 == -1:
        return (0,0)
    
    endLine1 = len(open(filePath1,"r",errors="ignore").readlines()) - 1
    endLine2 = len(open(filePath2,"r",errors="ignore").readlines()) - 1
    
    cmd = "java -jar Calculators/" + grammarName + ".jar " + filePath1 + " " + str(startLine1) + " " + str(endLine1) + " " + filePath2 + " " + str(startLine2) + " " + str(endLine2) + " " + keywordsListPath
    print(cmd)
    res = os.popen(cmd).readlines()[0].split(",")
    if len(res) == 2:
        return (float(res[0]), float(res[1]))
    else:
        print(res)
        return None, None
    
def generateSimilarityCalItem(olderCommitItem, newerCommitItem, reasonSegment, targetPair, keywordsList):
    print("Calculating similarity between " + olderCommitItem[0] + " and " + newerCommitItem[0])
    if olderCommitItem[1] == "segment1": 
        res = {
            "segment1" : {
                "commitId" : olderCommitItem[0],
                "commitContent" : targetPair[olderCommitItem[1]]['diffHis'][olderCommitItem[0]],
                "proj" : targetPair[olderCommitItem[1]]['projectName'],
            },
            "segment2" : {
                "commitId" : newerCommitItem[0],
                "commitContent" : targetPair[newerCommitItem[1]]['diffHis'][newerCommitItem[0]],
                "proj" : targetPair[newerCommitItem[1]]['projectName']
            },
            "newerSegment" : newerCommitItem[1],
            "reasonSegment" :  reasonSegment,
            "similarity" : similarityCalculation(targetPair[olderCommitItem[1]]['diffHis'][olderCommitItem[0]]['pathInCommit'], 0, -1, targetPair[newerCommitItem[1]]['diffHis'][newerCommitItem[0]]['pathInCommit'], 0, -1, keywordsList, targetPair['language'])
        }
    elif olderCommitItem[1] == "segment2":
        res = {
            "segment2" : {
                "commitId" : olderCommitItem[0],
                "commitContent" : targetPair[olderCommitItem[1]]['diffHis'][olderCommitItem[0]],
                "proj" : targetPair[olderCommitItem[1]]['projectName'],
            },
            "segment1" : {
                "commitId" : newerCommitItem[0],
                "commitContent" : targetPair[newerCommitItem[1]]['diffHis'][newerCommitItem[0]],
                "proj" : targetPair[newerCommitItem[1]]['projectName']
            },
            "newerSegment" : newerCommitItem[1],
            "reasonSegment" :  reasonSegment,
            "similarity" : similarityCalculation(targetPair[olderCommitItem[1]]['diffHis'][olderCommitItem[0]]['pathInCommit'], 0, -1, targetPair[newerCommitItem[1]]['diffHis'][newerCommitItem[0]]['pathInCommit'], 0, -1, keywordsList, targetPair['language'])
        }
    return res


def cloneTracker(targetPair):
    # set startLine and endLine for each segment
    for commitIdObj in getCommitIdListFromHistoryByDateOrder(targetPair['segment1']['diffHis'], "segment1"):
        extName = getExtensionNameFromFilePath(targetPair['segment1']['filePath'])
        fileName = targetPair['segment1']['filePath'].split("/")[-1]
        targetFolder = targetPair['workFolder'] + '/' + targetPair['segment1']['projectName'] + '_' + fileName
        pathInCommit = targetFolder + '/' + commitIdObj[0] + extName
        
        if os.path.exists(pathInCommit):
            targetPair['segment1']['diffHis'][commitIdObj[0]]['pathInCommit'] = pathInCommit
            targetPair['segment1']['diffHis'][commitIdObj[0]]['startLine'] = 1
            targetPair['segment1']['diffHis'][commitIdObj[0]]['endLine'] = len(open(pathInCommit,"r",errors="ignore").readlines())
            
    
    for commitIdObj in getCommitIdListFromHistoryByDateOrder(targetPair['segment2']['diffHis'], "segment2"):
        extName = getExtensionNameFromFilePath(targetPair['segment2']['filePath'])
        fileName = targetPair['segment2']['filePath'].split("/")[-1]
        targetFolder = targetPair['workFolder'] + '/' + targetPair['segment2']['projectName'] + '_' + fileName
        pathInCommit = targetFolder + '/' + commitIdObj[0] + extName
        
        if os.path.exists(pathInCommit):
            targetPair['segment2']['diffHis'][commitIdObj[0]]['pathInCommit'] = pathInCommit
            targetPair['segment2']['diffHis'][commitIdObj[0]]['startLine'] = 1
            targetPair['segment2']['diffHis'][commitIdObj[0]]['endLine'] = len(open(pathInCommit,"r",errors="ignore").readlines())
        
        # targetPair['segment2']['diffHis'][commitIdObj[0]]['startLine'] = 0
        # targetPair['segment2']['diffHis'][commitIdObj[0]]['endLine'] = len(open(targetPair['segment2']['filePath'],"r",errors="ignore").readlines())
        
    similarityList = []
    commitList1 = commitIdListFilterByFileDifferenceInLineRange(getCommitIdListFromHistoryByDateOrder(targetPair['segment1']['diffHis'], "segment1"), targetPair['segment1']['diffHis'])
    commitList2 = commitIdListFilterByFileDifferenceInLineRange(getCommitIdListFromHistoryByDateOrder(targetPair['segment2']['diffHis'], "segment2"), targetPair['segment2']['diffHis'])
    commitList = mergeTwoCommitIdListByDateOrder(commitList1, commitList2)
    negative_search_num = 0
    
    # try:
    if len(commitList) == 2:
        print("No modification found in both files.")
        similarityList.append(generateSimilarityCalItem(commitList[0], commitList[1], commitList[1][1], targetPair,keywordsListPath) )
    else:
        cursor = len(commitList) - 1
        
        while cursor >= 0: 
            
            targetCursor = cursor - 1
            
            while targetCursor >= 0 and commitList[targetCursor][1] == commitList[cursor][1]:
                targetCursor -= 1
    
            
            if targetCursor >= 0: # got target by positive search (new -> old)
                
                similarityList.insert(0, generateSimilarityCalItem(commitList[targetCursor], commitList[cursor], commitList[cursor][1], targetPair,keywordsListPath))

            else: # no older commit at the other side, negative search (old -> new) to find the cloest one
                targetCursor = cursor + 1
                while commitList[targetCursor][1] == commitList[cursor][1]:
                    targetCursor = targetCursor + 1
                    if targetCursor >= len(commitList):
                        break
                
                if cursor + 1 == targetCursor: # this pair is already calculated but reasonSegment does not have diffContent (because it is the first commit) # update it by this one
                    similarityList.pop(0)
                    similarityList.insert(0, generateSimilarityCalItem(commitList[cursor], commitList[targetCursor], commitList[cursor][1], targetPair,keywordsListPath))
                    # negative_search_num += 1
                else:
                    similarityList.insert(0, generateSimilarityCalItem(commitList[cursor], commitList[targetCursor], commitList[cursor][1], targetPair,keywordsListPath))
                    negative_search_num += 1
            
            cursor = cursor - 1
    
    # except Exception as e:
    #     print(e)
    #     print("Error in cloneTracker")
    #     return

    ## generate report
    result = {
        "taskId": taskId,
        "detectionId": detectionId,
        "cloneIndex" : targetPair["relatedIndex"][0],
        "relatedIndexes": targetPair["relatedIndex"],
        "targetPair" : targetPair,
        "similarityList" : similarityList,
        "commitList" : commitList,
        "negative_search_num" : negative_search_num
    }
    
    open(targetPair['workFolder'] + "/result.json", "w").write(ujson.dumps(result, indent=2))
    for item in similarityList:
        print(str(item['similarity'][0]))
        
    cmd = "python3 reportGeneration.py " + taskId + " " + detectionId + " " + str(result['cloneIndex']) + " file"
    os.system(cmd)

def copyFiles(fileCopyTasksList):
    tasksDict = {} # projName -> commitId -> taskDict
    
    for copyTaskObj_file in fileCopyTasksList:
        if not copyTaskObj_file['projName'] in tasksDict:
            tasksDict[copyTaskObj_file['projName']] = {}
        
        if not copyTaskObj_file['commitId'] in tasksDict[copyTaskObj_file['projName']]:
            tasksDict[copyTaskObj_file['projName']][copyTaskObj_file['commitId']] = []
        
        tasksDict[copyTaskObj_file['projName']][copyTaskObj_file['commitId']].append(copyTaskObj_file)
        
    for projName in tasksDict:
        print("Copy files for project:" + projName)
        for commitId in tasksDict[projName]:
            projPath = tasksDict[projName][commitId][0]['projPath']
            cmd = "cd " + projPath + "; git checkout -f " + commitId
            res = os.popen(cmd).read()
            
            for copyTaskObj_file in tasksDict[projName][commitId]:
                filePath_relative = copyTaskObj_file['filePath'].replace(projPath,"")
                if filePath_relative[0] == "/":
                    filePath_relative = filePath_relative[1:]
                filePath_abs = projPath + "/" + filePath_relative
                extName = getExtensionNameFromFilePath(copyTaskObj_file['filePath'])    
                targetFolder = copyTaskObj_file['workFolder'] + "/" + projName + "_" + copyTaskObj_file['fileName']
                if not os.path.exists(targetFolder):
                    os.mkdir(targetFolder)
                # convert targetFolder to absolute path
                targetFolder = os.path.abspath(targetFolder)
                
                cmd = "cp " + filePath_abs + " " + targetFolder + "/" + commitId + extName
                res = os.popen(cmd).read()
        switchToHeadCommit(projPath, tasksDict[projName][commitId][0]['defaultBranchName'])

def generateFileCopyTaskObj(segmentName, targetPair, workFolder):
    res = []
    for commitObj in getCommitIdListFromHistoryByDateOrder(targetPair[segmentName]['diffHis'], "segment1"):
        copyTaskObj_file = {}
        copyTaskObj_file['projPath'] = targetPair[segmentName]['projPath']
        copyTaskObj_file['filePath'] = targetPair[segmentName]['filePath']
        copyTaskObj_file['projName'] = targetPair[segmentName]['projectName']
        copyTaskObj_file['fileName'] = targetPair[segmentName]['filePath'].split("/")[-1]
        copyTaskObj_file['commitId'] = commitObj[0]
        copyTaskObj_file['workFolder'] = workFolder
        copyTaskObj_file['defaultBranchName'] = targetPair[segmentName]['defaultBranchName']
        
        extName = getExtensionNameFromFilePath(copyTaskObj_file['filePath'])
        targetFolder = workFolder + "/" + copyTaskObj_file['projName'] + "_" + copyTaskObj_file['fileName']

        pathInCommit = targetFolder + "/" + copyTaskObj_file['commitId'] + extName
        copyTaskObj_file['pathInCommit'] = pathInCommit
        
        res.append(copyTaskObj_file)
    
    return res

def cloneTrackPrepare(fileList, cloneList, tokenBagList,taskObj, relatedCloneIndexList, language):
    index = relatedCloneIndexList[0]
    projList =  taskObj['configObj']['inputProject']
    workFolder_detection = './reports/' + taskId + "-" + detectionId + "_file"
    if not os.path.exists(workFolder_detection):
        os.mkdir(workFolder_detection) 
    workFolder = workFolder_detection + "/" + str(index) + "/"
    if not os.path.exists(workFolder):
        os.mkdir(workFolder)
    
    targetPair = {
        "segment1" : {
            "projPath" : projList[cloneList[index][0][0]],
            "filePath" : fileList[cloneList[index][0][0]][cloneList[index][0][1]]['filePath'],
            # "startLine" : 0,
            # "endLine"   : len(open(fileList[cloneList[index][0][0]][cloneList[index][0][1]]['filePath'],"r",errors="ignore").readlines()),
            "projectName" : projList[cloneList[index][0][0]].split("/")[-1],
            "defaultBranchName" : getDefaultBranchName(projList[cloneList[index][0][0]])
        },
        "segment2" : {
            "projPath" : projList[cloneList[index][1][0]],
            "filePath" : fileList[cloneList[index][1][0]][cloneList[index][1][1]]['filePath'],
            # "startLine" : 0,
            # "endLine"   : len(open(fileList[cloneList[index][1][0]][cloneList[index][1][1]]['filePath'],"r",errors="ignore").readlines()),
            "projectName" : projList[cloneList[index][1][0]].split("/")[-1],
            "defaultBranchName" : getDefaultBranchName(projList[cloneList[index][1][0]])
        },
        "language" : taskObj['configObj']['tokenizer'],
        "workFolder" : workFolder,
        "relatedIndex" : relatedCloneIndexList
    }
        
    switchToHeadCommit(targetPair['segment1']['projPath'], targetPair['segment1']['defaultBranchName'])
    time.sleep(0.5)
    switchToHeadCommit(targetPair['segment2']['projPath'], targetPair['segment2']['defaultBranchName'])
    
    
    targetPair['segment1']['diffHis'] = getDiffHistory(targetPair['segment1']['projPath'], targetPair['segment1']['filePath'], targetPair['segment1']['defaultBranchName'])
    targetPair['segment1']['commitNum_fileModification'] = len(targetPair['segment1']['diffHis'])
    time.sleep(0.5)
    targetPair['segment2']['diffHis'] = getDiffHistory(targetPair['segment2']['projPath'], targetPair['segment2']['filePath'], targetPair['segment2']['defaultBranchName'])
    targetPair['segment2']['commitNum_fileModification'] = len(targetPair['segment2']['diffHis'])
    
    copyFileTaskObjList = []
    copyFileTaskObjList1 = generateFileCopyTaskObj('segment1', targetPair, workFolder)
    for item in copyFileTaskObjList1:
        copyFileTaskObjList.append(item)
        
    copyFileTaskObjList2 = generateFileCopyTaskObj('segment2', targetPair, workFolder)
    for item in copyFileTaskObjList2:
        copyFileTaskObjList.append(item)
    
    return targetPair, copyFileTaskObjList

if __name__ == "__main__":
    taskId      = "20004"
    detectionId = "2"
    cloneIndex  = -1
    language    = "C"
    
    # taskId      = sys.argv[1]
    # detectionId = sys.argv[2]
    # cloneIndex  = int(sys.argv[3])
    # language = sys.argv[4]
    
    keywordListDict = {
        "Java"       : "/Users/syu/workspace/MSCCD/grammarDefinations/Java/Java.reserved",
        "Go"         : "/Users/syu/workspace/MSCCD/grammarDefinations/Go/Go.reserved",
        "C"          : "/Users/syu/workspace/MSCCD/grammarDefinations/C/C.reserved",
        "JavaScript" : "/Users/syu/workspace/MSCCD/grammarDefinations/JavaScript/JavaScript.reserved",
        "C++"        : "/Users/syu/workspace/MSCCD/grammarDefinations/CPP14/CPP14.reserved",
        "Erlang"     : "/Users/syu/workspace/MSCCD/grammarDefinations/Erlang/Erlang.reserved",
        "Lua"        : "/Users/syu/workspace/MSCCD/grammarDefinations/Lua/Lua.reserved"
    }
    
    if language in keywordListDict:
        keywordsListPath = keywordListDict[language]
    else:
        raise Exception("Language not supported")
    
    taskObjPath = MSCCD_PATH + "tasks/task" + taskId + "/taskData.obj"
    taskObj     = ujson.load(open(taskObjPath, "r"))
    fileList     = fileListGeneration(taskId)
    cloneList    = cloneListGeneration(taskId, detectionId)
    tokenBagList = tokenBagListGeneration(taskId)
    
    
    if cloneIndex < 0:
        
        # get all cross-project clone pairs
        cloneIndexList_crossProj = []
        for cloneItemIndex in range(len(cloneList)):
            cloneItem = cloneList[cloneItemIndex]
            if cloneItem[0][0] != cloneItem[1][0]:
                cloneIndexList_crossProj.append(cloneItemIndex)
        
        cloneListSampled = None
        if cloneIndex < -1:
            print("#### Track random sampled clones.")
            cloneListSampled = random.sample(cloneIndexList_crossProj, -cloneIndex)
        else:
            print("#### Track all cross-project clones.")
            cloneListSampled = cloneIndexList_crossProj
        
    else:
        if cloneList[cloneIndex][0][0] == cloneList[cloneIndex][1][0]:
            print("#### Skip inner-project clones.")
            cloneListSampled = []
        else:
            cloneListSampled = [cloneIndex]
        

    # cloneListSampled = list(range(294,301))
    # cloneListSampled = [77]
    
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
                    # "length"   : len(open(filePath, "r", errors="ignore").readlines())
                }
                # singleId2TurpleId[singleId]['singleId'] = singleId
                
                if not projectId in projId2SingleId:
                    projId2SingleId[projectId] = []
                projId2SingleId[projectId].append(singleId)
    
    cloneDict_file = {}
    for cloneIndex in cloneListSampled:
        cloneItem = cloneList[cloneIndex]
        singleId1 = fileList[cloneItem[0][0]][cloneItem[0][1]]['singleId']
        singleId2 = fileList[cloneItem[1][0]][cloneItem[1][1]]['singleId']
        
        if singleId2 < singleId1:
            singleId1, singleId2 = singleId2, singleId1
            cloneItem = (cloneItem[1], cloneItem[0])

        if not singleId1 in cloneDict_file:
            cloneDict_file[singleId1] = {}
        if not singleId2 in cloneDict_file[singleId1]:
            cloneDict_file[singleId1][singleId2] = {
                "relatedCloneIndex" : [cloneIndex]
            }
        else:
            cloneDict_file[singleId1][singleId2]['relatedCloneIndex'].append(cloneIndex)
    
    
    cloneListToTrack = []
    for singleId1 in cloneDict_file:
        for singleId2 in cloneDict_file[singleId1]:
            cloneListToTrack.append(cloneDict_file[singleId1][singleId2]['relatedCloneIndex'])
    
    
    # Step 1
    # generate copy file task list (commitId, filePath, newPath)
    # generate cloneTracker task list
    
    print("#### Generate cloneTrackTasks objects and filtCopyTask objects.")
    
    calculatedIndexList    = []
    cloneTrackTasksObjList = []
    fileCopyTasksList      = []
    
    for relatedCloneIndexList in cloneListToTrack:
        print(relatedCloneIndexList)
        # index = relatedCloneIndexList[0]
        time.sleep(0.5)
        cloneTrackTaskObj, fileCopyTasks = cloneTrackPrepare(fileList, cloneList, tokenBagList, taskObj, relatedCloneIndexList, language)
        
        if cloneTrackTaskObj == None:
            continue
        
        cloneTrackTasksObjList.append(cloneTrackTaskObj)
        for item in fileCopyTasks:
            fileCopyTasksList.append(item)
            
    copyFiles(fileCopyTasksList)
    
    for cloneTrackTaskObj in cloneTrackTasksObjList:
        cloneTracker(cloneTrackTaskObj)
    
    print(calculatedIndexList)