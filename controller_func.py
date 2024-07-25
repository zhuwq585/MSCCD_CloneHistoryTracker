## input: taskId, detectionId, cloneIndex of target clone pair in a MSCCD detection task.
## output: clone history of the target clone pair in the MSCCD detection task.

import sys,os,ujson, random
from MSCCDTaskData import *
from FuncIdentification import *
from GitUsage import *


# sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

MSCCD_PATH = "/Users/syu/workspace/MSCCD/"

def similarityCalculation(filePath1, startLine1, endLine1, filePath2, startLine2, endLine2, keywordsListPath, grammarName ):
    if startLine1 == -1 or startLine2 == -1 or endLine1 == -1 or endLine2 == -1:
        return (0,0)
    
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
            "similarity" : similarityCalculation(targetPair[olderCommitItem[1]]['diffHis'][olderCommitItem[0]]['pathInCommit'], targetPair[olderCommitItem[1]]['diffHis'][olderCommitItem[0]]['startLine'], targetPair[olderCommitItem[1]]['diffHis'][olderCommitItem[0]]['endLine'], targetPair[newerCommitItem[1]]['diffHis'][newerCommitItem[0]]['pathInCommit'], targetPair[newerCommitItem[1]]['diffHis'][newerCommitItem[0]]['startLine'], targetPair[newerCommitItem[1]]['diffHis'][newerCommitItem[0]]['endLine'], keywordsList, targetPair['language'])
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
            "similarity" : similarityCalculation(targetPair[olderCommitItem[1]]['diffHis'][olderCommitItem[0]]['pathInCommit'], targetPair[olderCommitItem[1]]['diffHis'][olderCommitItem[0]]['startLine'], targetPair[olderCommitItem[1]]['diffHis'][olderCommitItem[0]]['endLine'], targetPair[newerCommitItem[1]]['diffHis'][newerCommitItem[0]]['pathInCommit'], targetPair[newerCommitItem[1]]['diffHis'][newerCommitItem[0]]['startLine'], targetPair[newerCommitItem[1]]['diffHis'][newerCommitItem[0]]['endLine'], keywordsList, targetPair['language'])
        }
    return res




def generateFileCopyTaskObj(segmentName, targetPair, workFolder):
    res = []
    for commitObj in getCommitIdListFromHistoryByDateOrder(targetPair[segmentName]['diffHis'], "segment1"):
        copyTaskObj_file = {}
        copyTaskObj_file['projPath'] = targetPair[segmentName]['projPath']
        copyTaskObj_file['filePath'] = targetPair[segmentName]['filePath']
        copyTaskObj_file['projName'] = targetPair[segmentName]['projectName']
        copyTaskObj_file['functionName'] = targetPair[segmentName]['functionName']
        copyTaskObj_file['commitId'] = commitObj[0]
        copyTaskObj_file['workFolder'] = workFolder
        copyTaskObj_file['defaultBranchName'] = targetPair[segmentName]['defaultBranchName']
        
        extName = getExtensionNameFromFilePath(copyTaskObj_file['filePath'])
        targetFolder = workFolder + "/" + copyTaskObj_file['projName'] + "_" + copyTaskObj_file['functionName']

        pathInCommit = targetFolder + "/" + copyTaskObj_file['commitId'] + extName
        copyTaskObj_file['pathInCommit'] = pathInCommit
        
        res.append(copyTaskObj_file)
    
    return res

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
                targetFolder = copyTaskObj_file['workFolder'] + "/" + projName + "_" + copyTaskObj_file['functionName']
                if not os.path.exists(targetFolder):
                    os.mkdir(targetFolder)
                # convert targetFolder to absolute path
                targetFolder = os.path.abspath(targetFolder)
                
                cmd = "cp " + filePath_abs + " " + targetFolder + "/" + commitId + extName
                res = os.popen(cmd).read()
        switchToHeadCommit(projPath, tasksDict[projName][commitId][0]['defaultBranchName'])

# def getFunctionPositions(targetPair)


def cloneTracker(targetPair):
    # get function position in each copied files
    for commitIdObj in getCommitIdListFromHistoryByDateOrder(targetPair['segment1']['diffHis'], 'segment1'):
        extName = getExtensionNameFromFilePath(targetPair['segment1']['filePath'])
        targetFolder = targetPair['workFolder'] + '/' + targetPair['segment1']['projectName'] + '_' + targetPair['segment1']['functionName']
        pathInCommit = targetFolder + '/' + commitIdObj[0] + extName
        
        # try:
        startLine,endLine = getFunctionPosition(pathInCommit, targetPair['segment1']['functionName'], targetPair['segment1']['pattern'], language, targetPair['segment1']['commitNum_functionIdendified'])
        # except TypeError:
        #     startLine = -1
        #     endLine = -1
        
        if startLine >= 0 and endLine >= 0:
            targetPair['segment1']['commitNum_functionIdendified'] += 1
            
        targetPair['segment1']['diffHis'][commitIdObj[0]]['startLine'] = startLine
        targetPair['segment1']['diffHis'][commitIdObj[0]]['endLine'] = endLine
        targetPair['segment1']['diffHis'][commitIdObj[0]]['pathInCommit'] = pathInCommit
    
    
    for commitIdObj in getCommitIdListFromHistoryByDateOrder(targetPair['segment2']['diffHis'], 'segment2'):
        extName = getExtensionNameFromFilePath(targetPair['segment2']['filePath'])
        targetFolder = targetPair['workFolder'] + '/' + targetPair['segment2']['projectName'] + '_' + targetPair['segment2']['functionName']
        pathInCommit = targetFolder + '/' + commitIdObj[0] + extName
        
        try:
            startLine,endLine = getFunctionPosition(pathInCommit, targetPair['segment2']['functionName'], targetPair['segment2']['pattern'], language, targetPair['segment2']['commitNum_functionIdendified'])
        except TypeError:
            startLine = -1
            endLine = -1
        
        if startLine >= 0 and endLine >= 0:
            targetPair['segment2']['commitNum_functionIdendified'] += 1
            
        targetPair['segment2']['diffHis'][commitIdObj[0]]['startLine'] = startLine
        targetPair['segment2']['diffHis'][commitIdObj[0]]['endLine'] = endLine
        targetPair['segment2']['diffHis'][commitIdObj[0]]['pathInCommit'] = pathInCommit
    

    similarityList = []
    commitList1 = commitIdListFilterByFileDifferenceInLineRange(getCommitIdListFromHistoryByDateOrder(targetPair['segment1']['diffHis'],"segment1"), targetPair['segment1']['diffHis']) 
    commitList2 = commitIdListFilterByFileDifferenceInLineRange(getCommitIdListFromHistoryByDateOrder(targetPair['segment2']['diffHis'],"segment2"), targetPair['segment2']['diffHis']) 
    
    
    targetPair['segment1']['commitNum_functionModification'] = len(commitList1)
    targetPair['segment2']['commitNum_functionModification'] = len(commitList2)
    
    
    commitList  = mergeTwoCommitIdListByDateOrder(commitList1, commitList2)
    negative_search_num = 0


    try:
        if len(commitList) == 2:
            print("No modification found in both functions.")
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
                        
    except Exception:
        print("#######")
        print("#######")
        print("Returned by error")
        print(targetPair)
        print("#######")
        print("#######")
        return   
    
    # step7: output report
    result = {
        "taskId": taskId,
        "detectionId": detectionId,
        "cloneIndex": targetPair['cloneIndex'],
        "targetPair" : targetPair,
        "similarityList" : similarityList,
        "commitList" : commitList,
        "negative_search_num" : negative_search_num
    }
    
    open(targetPair['workFolder'] + "/result.json", "w").write(ujson.dumps(result, indent=2))
    for item in similarityList:
        print(str(item['similarity'][0]))
        
    cmd = "python3 reportGeneration.py " + taskId + " " + detectionId + " " + str(result['cloneIndex']) + " func"
    os.system(cmd)
   
def cloneTrackPrepare(fileList, cloneList, tokenBagList, taskObj, cloneIndex, language):
    projList     = taskObj['configObj']['inputProject']
    workFolder_detection = './reports/' + taskId + "-" + detectionId + "_func"
    if not os.path.exists(workFolder_detection):
        os.mkdir(workFolder_detection) 
    workFolder = workFolder_detection + "/" + str(cloneIndex) + "/"
    if not os.path.exists(workFolder):
        os.mkdir(workFolder)
    
    targetPair = {
        "segment1":{
            "projPath" : projList[cloneList[cloneIndex][0][0]],
            "filePath" : fileList[cloneList[cloneIndex][0][0]][cloneList[cloneIndex][0][1]],
            "startLine" : tokenBagList[cloneList[cloneIndex][0][0]][cloneList[cloneIndex][0][1]][cloneList[cloneIndex][0][2]]["startLine"],
            "endLine" : tokenBagList[cloneList[cloneIndex][0][0]][cloneList[cloneIndex][0][1]][cloneList[cloneIndex][0][2]]["endLine"],
            "projectName" : projList[cloneList[cloneIndex][0][0]].split("/")[-1],
            "defaultBranchName" : getDefaultBranchName(projList[cloneList[cloneIndex][0][0]])
        },
        "segment2":{
            "projPath" : projList[cloneList[cloneIndex][1][0]],
            "filePath" : fileList[cloneList[cloneIndex][1][0]][cloneList[cloneIndex][1][1]],
            "startLine" : tokenBagList[cloneList[cloneIndex][1][0]][cloneList[cloneIndex][1][1]][cloneList[cloneIndex][1][2]]["startLine"],
            "endLine" : tokenBagList[cloneList[cloneIndex][1][0]][cloneList[cloneIndex][1][1]][cloneList[cloneIndex][1][2]]["endLine"],
            'projectName' : projList[cloneList[cloneIndex][1][0]].split("/")[-1],
            "defaultBranchName" : getDefaultBranchName(projList[cloneList[cloneIndex][1][0]])
        },
        "language" : taskObj['configObj']['tokenizer'],
        "workFolder" : workFolder,
        "cloneIndex" : cloneIndex
    }
    
    switchToHeadCommit(targetPair['segment1']['projPath'], targetPair['segment1']['defaultBranchName'])
    switchToHeadCommit(targetPair['segment2']['projPath'], targetPair['segment2']['defaultBranchName'])

    targetPair['segment1']['functionName'], targetPair['segment1']['pattern'] = getFunctionName_Ptn(targetPair['segment1']['filePath'], targetPair['segment1']['startLine'], targetPair['segment1']['endLine'], language)
    targetPair['segment2']['functionName'], targetPair['segment2']['pattern'] = getFunctionName_Ptn(targetPair['segment2']['filePath'], targetPair['segment2']['startLine'], targetPair['segment2']['endLine'], language)
    
    if targetPair['segment1']['functionName'] == None or targetPair['segment1']['pattern'] == None or targetPair['segment2']['functionName'] == None or targetPair['segment2']['pattern'] == None:
        return None,None


    targetPair['segment1']['diffHis'] = getDiffHistory(targetPair['segment1']['projPath'], targetPair['segment1']['filePath'], targetPair['segment1']['defaultBranchName'])
    targetPair['segment1']['commitNum_fileModification'] = len(targetPair['segment1']['diffHis'])
    targetPair['segment1']['commitNum_functionIdendified'] = 0
    targetPair['segment2']['diffHis'] = getDiffHistory(targetPair['segment2']['projPath'], targetPair['segment2']['filePath'], targetPair['segment2']['defaultBranchName'])
    targetPair['segment2']['commitNum_fileModification'] = len(targetPair['segment2']['diffHis'])
    targetPair['segment2']['commitNum_functionIdendified'] = 0
    
    copyFileTaskObjList = []
    copyFileTaskObjList1 = generateFileCopyTaskObj('segment1', targetPair, workFolder)
    for item in copyFileTaskObjList1:
        copyFileTaskObjList.append(item)
        
    copyFileTaskObjList2 = generateFileCopyTaskObj('segment2', targetPair, workFolder)
    for item in copyFileTaskObjList2:
        copyFileTaskObjList.append(item)
    
    return targetPair, copyFileTaskObjList
       
        
if __name__ == "__main__":
    
    # step1: get info from task.obj in MSCCD task folder
    
    # taskId      = sys.argv[1]
    # detectionId = sys.argv[2]
    # cloneIndex  = int(sys.argv[3])
    # language = sys.argv[4]
    
    ### for test
    taskId      = "20008"
    detectionId = "11"
    cloneIndex  = -1
    language = "Go"  #{"Java", "Go", "C","JavaScript","C++"}
    # "/Users/syu/workspace/MSCCD/grammarDefinations/Java9/Java9.reserved"
    
    keywordListDict = {
        "Java" : "/Users/syu/workspace/MSCCD/grammarDefinations/Java/Java.reserved",
        "Go" : "/Users/syu/workspace/MSCCD/grammarDefinations/Go/Go.reserved",
        "C" : "/Users/syu/workspace/MSCCD/grammarDefinations/C/C.reserved",
        "JavaScript" : "/Users/syu/workspace/MSCCD/grammarDefinations/JavaScript/JavaScript.reserved",
        "C++" : "/Users/syu/workspace/MSCCD/grammarDefinations/CPP14/CPP14.reserved"
    }
    
    if language in keywordListDict:
        keywordsListPath = keywordListDict[language]
    else:
        raise Exception("Language not supported.")
    
    
    
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
                cloneIndexList_crossProj.append( cloneItemIndex) 
        
        
        cloneListSampled = None
        if cloneIndex < -1:
            print("#### Track random sampled clones.")
            cloneListSampled = random.sample(cloneIndexList_crossProj, -cloneIndex)
        else:
            print("#### Track all cross-project clones.")
            cloneListSampled = cloneIndexList_crossProj
            
        # cloneListSampled = list(range(0,1279))
            
    else :
        cloneListSampled = [cloneIndex]  
        
        
    calculateIndexLst = []
    cloneTrackTasksObjList = []
    fileCopyTasksList = []
    
    
                
    # Step 1
    # get function name, get commit list
    # generate copy file task list (commentid, filePath, newPath)
    # generate cloneTracker task list
    print("#### Generate cloneTrackTasks objects and filtCopyTask objects.")

    for index in cloneListSampled:
        print(index)
        cloneTrackTaskObj, fileCopyTasks = cloneTrackPrepare(fileList, cloneList, tokenBagList, taskObj, index, language)
        
        if cloneTrackTaskObj == None or fileCopyTasks == None:
            continue
        
        cloneTrackTasksObjList.append(cloneTrackTaskObj)
        for item in fileCopyTasks:
            fileCopyTasksList.append(item)
    
    # Step 2
    # do tasks in lists
    copyFiles(fileCopyTasksList)
    
    for cloneTrackTaskObj in cloneTrackTasksObjList:
        cloneTracker(cloneTrackTaskObj)
    
    print(calculateIndexLst) 
    # else:
    #     cloneTracker(fileList, cloneList, tokenBagList, taskObj, cloneIndex, language, keywordsListPath)
        
        
        
    #     cmd = "python3 reportGeneration.py " + taskId + " " + detectionId + " " + str(cloneIndex)
    #     os.system(cmd)