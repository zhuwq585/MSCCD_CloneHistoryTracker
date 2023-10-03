## input: taskId, detectionId, cloneIndex of target clone pair in a MSCCD detection task.
## output: clone history of the target clone pair in the MSCCD detection task.

import sys,os,ujson
from MSCCDTaskData import *
from CTagsUsage import *
from GitUsage import *

# sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

MSCCD_PATH = "/Users/syu/workspace/MSCCD/"


def similarityCalculation(filePath1, startLine1, endLine1, filePath2, startLine2, endLine2, keywordsListPath, grammarName ):
    cmd = "java -jar Calculators/" + grammarName + ".jar " + filePath1 + " " + str(startLine1) + " " + str(endLine1) + " " + filePath2 + " " + str(startLine2) + " " + str(endLine2) + " " + keywordsListPath
    res = os.popen(cmd).readlines()[0].split(",")
    if len(res) == 2:
        return (float(res[0]), float(res[1]))
    else:
        return None, None
    
    


if __name__ == "__main__":
    
    # step1: get info from task.obj in MSCCD task folder
    
    # taskId      = sys.argv[1]
    # detectionId = sys.argv[2]
    # cloneIndex  = sys.argv[3]
    # keywordsList = sys.argv[4]
    
    ### for test
    taskId      = "11012"
    detectionId = "1"
    cloneIndex  = 6187
    keywordsList = "/Users/syu/workspace/MSCCD/grammarDefinations/cpp/CPP14.reserved"
    # "/Users/syu/workspace/MSCCD/grammarDefinations/Java9/Java9.reserved"
    
    workFolder = './' + taskId + "-" + detectionId + "-" + str(cloneIndex) + "/"
    if not os.path.exists(workFolder):
        os.mkdir(workFolder)    
    
    taskObjPath = MSCCD_PATH + "tasks/task" + taskId + "/taskData.obj"
    taskObj     = ujson.load(open(taskObjPath, "r"))
    
    fileList     = fileListGeneration(taskId)
    cloneList    = cloneListGeneration(taskId, detectionId, fileList)
    tokenBagList = tokenBagListGeneration(taskId)
    projList     = taskObj['configObj']['inputProject']
    
    targetPair = {
        "segment1":{
            "projPath" : projList[cloneList[cloneIndex][0][0]],
            "filePath" : fileList[cloneList[cloneIndex][0][0]][cloneList[cloneIndex][0][1]],
            "startLine" : tokenBagList[cloneList[cloneIndex][0][0]][cloneList[cloneIndex][0][1]][cloneList[cloneIndex][0][2]]["startLine"],
            "endLine" : tokenBagList[cloneList[cloneIndex][0][0]][cloneList[cloneIndex][0][1]][cloneList[cloneIndex][0][2]]["endLine"],
            "projectName" : projList[cloneList[cloneIndex][0][0]].split("/")[-1]
        },
        "segment2":{
            "projPath" : projList[cloneList[cloneIndex][1][0]],
            "filePath" : fileList[cloneList[cloneIndex][1][0]][cloneList[cloneIndex][1][1]],
            "startLine" : tokenBagList[cloneList[cloneIndex][1][0]][cloneList[cloneIndex][1][1]][cloneList[cloneIndex][1][2]]["startLine"],
            "endLine" : tokenBagList[cloneList[cloneIndex][1][0]][cloneList[cloneIndex][1][1]][cloneList[cloneIndex][1][2]]["endLine"],
            'projectName' : projList[cloneList[cloneIndex][1][0]].split("/")[-1]
        },
        "language" : taskObj['configObj']['tokenizer']
    }
    
    # step2: get function name using ctags
    targetPair['segment1']['functionName'] = getFunctionName(targetPair['segment1']['filePath'], targetPair['segment1']['startLine'], targetPair['segment1']['endLine'])
    targetPair['segment2']['functionName'] = getFunctionName(targetPair['segment2']['filePath'], targetPair['segment2']['startLine'], targetPair['segment2']['endLine'])
    
    # step3: get diff history using git
    diffHis1 = getDiffHistory(targetPair['segment1']['projPath'], targetPair['segment1']['filePath'], targetPair['segment1']['functionName'])
    diffHis2 = getDiffHistory(targetPair['segment2']['projPath'], targetPair['segment2']['filePath'], targetPair['segment2']['functionName'])
    
    # step4: copy target file in each target commit
    # step5: get position of target function in each target file using ctags

    for commitId in getCommitIdListFromHistoryByDateOrder(diffHis1):
        pathInCommit = copyTargetFileToFolder(targetPair['segment1']['projPath'], targetPair['segment1']['filePath'], targetPair['segment1']['projectName'], targetPair['segment1']['functionName'], commitId, workFolder)
        
        startLine,endLine = getFunctionPosition(workFolder + "/" + targetPair['segment1']['projectName'] + "_" + targetPair['segment1']['functionName'] + "/" + list(diffHis1.keys())[0]+getExtensionNameFromFilePath(targetPair['segment1']['filePath']), targetPair['segment1']['functionName'])
        diffHis1[commitId]['startLine'] = startLine
        diffHis1[commitId]['endLine'] = endLine
        diffHis1[commitId]['pathInCommit'] = pathInCommit
    
    
    
    for commitId in getCommitIdListFromHistoryByDateOrder(diffHis2):
        pathInCommit = copyTargetFileToFolder(targetPair['segment2']['projPath'], targetPair['segment2']['filePath'], targetPair['segment2']['projectName'], targetPair['segment2']['functionName'], commitId, workFolder)
    
        startLine,endLine = getFunctionPosition(workFolder + "/" + targetPair['segment2']['projectName'] + "_" + targetPair['segment2']['functionName'] + "/" + list(diffHis2.keys())[0]+getExtensionNameFromFilePath(targetPair['segment2']['filePath']), targetPair['segment2']['functionName'])
        diffHis2[commitId]['startLine'] = startLine
        diffHis2[commitId]['endLine'] = endLine
        diffHis2[commitId]['pathInCommit'] = pathInCommit
   
    # switchToHeadCommit(targetPair['segment1']['projPath'])
    # switchToHeadCommit(targetPair['segment2']['projPath'])
    
    # step6: similarity calculation 
    
    similarityList = []
    commitList1 = getCommitIdListFromHistoryByDateOrder(diffHis1)
    commitList2 = getCommitIdListFromHistoryByDateOrder(diffHis2)
    
    
    initCommit = None    
    if compareDateInDiffHistoryDict(diffHis1, commitList1[0], diffHis2, commitList2[0]):
        initCommit = commitList1[0]
    else:
        initCommit = commitList2[0]

    if (len(commitList1) == 1 and len(commitList2) == 1):
        filePath1 = diffHis1[commitList1[0]]['pathInCommit']
        filePath2 = diffHis2[commitList2[0]]['pathInCommit']
        if compareDateInDiffHistoryDict(diffHis1, commitList1[0], diffHis2, commitList2[0]): # commit for segment1 is newer
            similarityList.append({
                "modifiedCommit" : commitList1[0],
                "modifiedCommitContent" : diffHis1[commitList1[0]],
                "modifiedProj" : targetPair['segment1']['projectName'],
                "similarity" : similarityCalculation(filePath1, diffHis1[commitList1[0]]['startLine'], diffHis1[commitList1[0]]['endLine'], filePath2, diffHis2[commitList2[0]]['startLine'], diffHis2[commitList2[0]]['endLine'], keywordsList, targetPair['language'])
            })
        else: # commit for segment2 is newer
            similarityList.append({
                "modifiedCommit" : commitList2[0],
                "modifiedCommitContent" : diffHis2[commitList2[0]],
                "modifiedProj" : targetPair['segment2']['projectName'],
                "similarity" : similarityCalculation(filePath1, diffHis1[commitList1[0]]['startLine'], diffHis1[commitList1[0]]['endLine'], filePath2, diffHis2[commitList2[0]]['startLine'], diffHis2[commitList2[0]]['endLine'], keywordsList, targetPair['language'])
            })
    else:
        olderCommit = None
        while (len(commitList1) != 0 and len(commitList2) != 0):
            filePath1 = diffHis1[commitList1[0]]['pathInCommit']
            filePath2 = diffHis2[commitList2[0]]['pathInCommit']
            
            if compareDateInDiffHistoryDict(diffHis1, commitList1[0], diffHis2, commitList2[0]): # commit for segment1 is newer
                similarityList.append({
                    "modifiedCommit" : commitList1[0],
                    "modifiedCommitContent" : diffHis1[commitList1[0]],
                    "modifiedProj" : targetPair['segment1']['projectName'],
                    "similarity" : similarityCalculation(filePath1, diffHis1[commitList1[0]]['startLine'], diffHis1[commitList1[0]]['endLine'], filePath2, diffHis2[commitList2[0]]['startLine'], diffHis2[commitList2[0]]['endLine'], keywordsList, targetPair['language'])
                })
                olderCommit = commitList1.pop()
            else: # commit for segment2 is newer
                similarityList.append({
                    "modifiedCommit" : commitList2[0],
                    "modifiedCommitContent" : diffHis2[commitList2[0]],
                    "modifiedProj" : targetPair['segment2']['projectName'],
                    "similarity" : similarityCalculation(filePath1, diffHis1[commitList1[0]]['startLine'], diffHis1[commitList1[0]]['endLine'], filePath2, diffHis2[commitList2[0]]['startLine'], diffHis2[commitList2[0]]['endLine'], keywordsList, targetPair['language'])
                })
                olderCommit = commitList2.pop()
            
        while len(commitList1) != 0:
            similarityList.append({
                "modifiedCommit" : commitList1[0],
                "modifiedCommitContent" : diffHis1[commitList1[0]],
                "modifiedProj" : targetPair['segment1']['projectName'],
                "similarity" : similarityCalculation(filePath1, diffHis1[commitList1[0]]['startLine'], diffHis1[commitList1[0]]['endLine'], filePath2, diffHis2[olderCommit]['startLine'], diffHis2[olderCommit]['endLine'], keywordsList, targetPair['language'])
            })
            olderCommit = commitList1.pop(1)
        
        while len(commitList2) != 0:
            similarityList.append({
                "modifiedCommit" : commitList2[0],
                "modifiedCommitContent" : diffHis2[commitList2[0]],
                "modifiedProj" : targetPair['segment2']['projectName'],
                "similarity" : similarityCalculation(filePath2, diffHis1[olderCommit]['startLine'], diffHis1[olderCommit]['endLine'], filePath2, diffHis2[commitList2[0]]['startLine'], diffHis2[commitList2[0]]['endLine'], keywordsList, targetPair['language'])
            })
            olderCommit = commitList2.pop(1)

    switchToHeadCommit(targetPair['segment1']['projPath'])
    switchToHeadCommit(targetPair['segment2']['projPath'])
    
    
    # step7: output report
    open(workFolder + "result.json", "w").write(ujson.dumps(similarityList, indent=2))
    print(similarityList)