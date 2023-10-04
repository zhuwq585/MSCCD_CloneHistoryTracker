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
    taskId      = "11006"
    detectionId = "1"
    cloneIndex  = 2097950
    keywordsList = "/Users/syu/workspace/MSCCD/grammarDefinations/Go/Go.reserved"
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
    
    switchToHeadCommit(targetPair['segment1']['projPath'])
    switchToHeadCommit(targetPair['segment2']['projPath'])
    
    # step2: get function name using ctags
    targetPair['segment1']['functionName'] = getFunctionName(targetPair['segment1']['filePath'], targetPair['segment1']['startLine'], targetPair['segment1']['endLine'])
    targetPair['segment2']['functionName'] = getFunctionName(targetPair['segment2']['filePath'], targetPair['segment2']['startLine'], targetPair['segment2']['endLine'])
    
    # step3: get diff history using git
    targetPair['segment1']['diffHis'] = getDiffHistory(targetPair['segment1']['projPath'], targetPair['segment1']['filePath'], targetPair['segment1']['functionName'])
    targetPair['segment2']['diffHis'] = getDiffHistory(targetPair['segment2']['projPath'], targetPair['segment2']['filePath'], targetPair['segment2']['functionName'])
    # diffHis1 = getDiffHistory(targetPair['segment1']['projPath'], targetPair['segment1']['filePath'], targetPair['segment1']['functionName'])
    # diffHis2 = getDiffHistory(targetPair['segment2']['projPath'], targetPair['segment2']['filePath'], targetPair['segment2']['functionName'])
    
    # step4: copy target file in each target commit
    # step5: get position of target function in each target file using ctags




    for commitIdObj in getCommitIdListFromHistoryByDateOrder(targetPair['segment1']['diffHis'], "segment1"):
        pathInCommit = copyTargetFileToFolder(targetPair['segment1']['projPath'], targetPair['segment1']['filePath'], targetPair['segment1']['projectName'], targetPair['segment1']['functionName'], commitIdObj[0], workFolder)
        
        startLine,endLine = getFunctionPosition(pathInCommit, targetPair['segment1']['functionName'])
        targetPair['segment1']['diffHis'][commitIdObj[0]]['startLine'] = startLine
        targetPair['segment1']['diffHis'][commitIdObj[0]]['endLine'] = endLine
        targetPair['segment1']['diffHis'][commitIdObj[0]]['pathInCommit'] = pathInCommit
    
    
    
    for commitIdObj in getCommitIdListFromHistoryByDateOrder(targetPair['segment2']['diffHis'],"segment2"):
        pathInCommit = copyTargetFileToFolder(targetPair['segment2']['projPath'], targetPair['segment2']['filePath'], targetPair['segment2']['projectName'], targetPair['segment2']['functionName'], commitIdObj[0], workFolder)
    
        startLine,endLine = getFunctionPosition(pathInCommit, targetPair['segment2']['functionName'])
        targetPair['segment2']['diffHis'][commitIdObj[0]]['startLine'] = startLine
        targetPair['segment2']['diffHis'][commitIdObj[0]]['endLine'] = endLine
        targetPair['segment2']['diffHis'][commitIdObj[0]]['pathInCommit'] = pathInCommit
   

    
    # step6: similarity calculation 
    
    similarityList = []
    commitList1 = getCommitIdListFromHistoryByDateOrder(targetPair['segment1']['diffHis'],"segment1")
    commitList2 = getCommitIdListFromHistoryByDateOrder(targetPair['segment2']['diffHis'],"segment2")
    commitList  = mergeTwoCommitIdListByDateOrder(commitList1, commitList2)
    
    r = None
    
    while len(commitList) >= 2:
        if commitList[0][1] != commitList[1][1]: # if the two commits are from different segment 
            print("calculate similarity between " + commitList[0][0] + " and " + commitList[1][0])
            # generate similarity between commitList[0] and commitList[1], and set modifiedCommit, modifiedCommitContent and modifiedProj based on commitList[1]
            similarityList.append({
                "modifiedCommit" : commitList[1][0],
                "modifiedCommitContent" : targetPair[commitList[1][1]]['diffHis'][commitList[1][0]],
                "modifiedProj" : targetPair[commitList[1][1]]['projectName'],
                "unmodifiedCommitContent" : targetPair[commitList[0][1]]['diffHis'][commitList[0][0]],
                "similarity" : similarityCalculation(targetPair[commitList[0][1]]['diffHis'][commitList[0][0]]['pathInCommit'], targetPair[commitList[0][1]]['diffHis'][commitList[0][0]]['startLine'], targetPair[commitList[0][1]]['diffHis'][commitList[0][0]]['endLine'], targetPair[commitList[1][1]]['diffHis'][commitList[1][0]]['pathInCommit'], targetPair[commitList[1][1]]['diffHis'][commitList[1][0]]['startLine'], targetPair[commitList[1][1]]['diffHis'][commitList[1][0]]['endLine'], keywordsList, targetPair['language'])
            })
            r = commitList.pop(0)
            
        else:
            if r == None:
                # cursor = 2
                # while cursor < len(commitList):
                #     if commitList[cursor][1] != commitList[0][1]:
                #         r = commitList[cursor]
                #         break
                #     cursor = cursor + 1
                
                # similarityList.append({
                #     "modifiedCommit" : commitList[0][0],
                #     "modifiedCommitContent" : targetPair[commitList[0][1]]['diffHis'][commitList[0][0]],
                #     "modifiedProj" : targetPair[commitList[0][1]]['projectName'],
                #     "unmodifiedCommitContent" : targetPair[r[1]]['diffHis'][r[0]],
                #     "similarity" : similarityCalculation(targetPair[commitList[0][1]]['diffHis'][commitList[0][0]]['pathInCommit'], targetPair[commitList[0][1]]['diffHis'][commitList[0][0]]['startLine'], targetPair[commitList[0][1]]['diffHis'][commitList[0][0]]['endLine'], targetPair[r[1]]['diffHis'][r[0]]['pathInCommit'], targetPair[r[1]]['diffHis'][r[0]]['startLine'], targetPair[r[1]]['diffHis'][r[0]]['endLine'], keywordsList, targetPair['language'])
                # })
                commitList.pop(0)
            # generate similarity between r and commitList[1], and set modifiedCommit, modifiedCommitContent and modifiedProj based on commitList[1]
            else:
                similarityList.append({
                    "modifiedCommit" : commitList[1][0],
                    "modifiedCommitContent" : targetPair[commitList[1][1]]['diffHis'][commitList[1][0]],
                    "modifiedProj" : targetPair[commitList[1][1]]['projectName'],
                    "unmodifiedCommitContent" : targetPair[r[1]]['diffHis'][r[0]],
                    "similarity" : similarityCalculation(targetPair[r[1]]['diffHis'][r[0]]['pathInCommit'], targetPair[r[1]]['diffHis'][r[0]]['startLine'], targetPair[r[1]]['diffHis'][r[0]]['endLine'], targetPair[commitList[1][1]]['diffHis'][commitList[1][0]]['pathInCommit'], targetPair[commitList[1][1]]['diffHis'][commitList[1][0]]['startLine'], targetPair[commitList[1][1]]['diffHis'][commitList[1][0]]['endLine'], keywordsList, targetPair['language'])
                })
                commitList.pop(0)                
            

    
    
    # step7: output report
    open(workFolder + "result.json", "w").write(ujson.dumps(similarityList, indent=2))
    print(similarityList)