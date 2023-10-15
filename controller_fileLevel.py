## input: taskId, detectionId, cloneIndex of target clone pair in a MSCCD detection task.
## output: clone history of the target clone pair in the MSCCD detection task.

import sys,os,ujson
from MSCCDTaskData import *
from FuncIdentification import *
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
    
def generateSimilarityCalItem(olderCommitItem, newerCommitItem):
    res = {
        "newCommit" : newerCommitItem[0],
        "newCommitContent" : targetPair[newerCommitItem[1]]['diffHis'][newerCommitItem[0]],
        "newProj" : targetPair[newerCommitItem[1]]['projectName'],
        "oldCommit" : olderCommitItem[0],
        "oldCommitContent" : targetPair[olderCommitItem[1]]['diffHis'][olderCommitItem[0]],
        "similarity" : similarityCalculation(targetPair[olderCommitItem[1]]['diffHis'][olderCommitItem[0]]['pathInCommit'], targetPair[olderCommitItem[1]]['diffHis'][olderCommitItem[0]]['startLine'], targetPair[olderCommitItem[1]]['diffHis'][olderCommitItem[0]]['endLine'], targetPair[newerCommitItem[1]]['diffHis'][newerCommitItem[0]]['pathInCommit'], targetPair[newerCommitItem[1]]['diffHis'][newerCommitItem[0]]['startLine'], targetPair[newerCommitItem[1]]['diffHis'][newerCommitItem[0]]['endLine'], keywordsList, targetPair['language'])
    }   
    return res


if __name__ == "__main__":
    
    # step1: get info from task.obj in MSCCD task folder
    
    # taskId      = sys.argv[1]
    # detectionId = sys.argv[2]
    # cloneIndex  = sys.argv[3]
    # keywordsList = sys.argv[4]
    # language = sys.argv[5]
    
    ### for test
    taskId      = "11008"
    detectionId = "1"
    cloneIndex  = 138
    keywordsList = "/Users/syu/workspace/MSCCD/grammarDefinations/JavaScript/JavaScript.reserved"
    language = "JavaScript" #{"Java", "Go", "C","JavaScript","C++"}
    # "/Users/syu/workspace/MSCCD/grammarDefinations/Java9/Java9.reserved"
    
    workFolder = './reports/' + taskId + "-" + detectionId + "-" + str(cloneIndex) + "/"
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
            "startLine" : 0,
            "endLine" : None,
            "projectName" : projList[cloneList[cloneIndex][0][0]].split("/")[-1],
            "defaultBranchName" : getDefaultBranchName(projList[cloneList[cloneIndex][0][0]])
        },
        "segment2":{
            "projPath" : projList[cloneList[cloneIndex][1][0]],
            "filePath" : fileList[cloneList[cloneIndex][1][0]][cloneList[cloneIndex][1][1]],
            "startLine" : 0,
            "endLine" : None,
            'projectName' : projList[cloneList[cloneIndex][1][0]].split("/")[-1],
            "defaultBranchName" : getDefaultBranchName(projList[cloneList[cloneIndex][1][0]])
        },
        "language" : taskObj['configObj']['tokenizer']
    }
    
    targetPair['segment1']['endLine'] = len(open(targetPair['segment1']['filePath'], "r").readlines()) - 1
    targetPair['segment2']['endLine'] = len(open(targetPair['segment2']['filePath'], "r").readlines()) - 1
    
    
    
    switchToHeadCommit(targetPair['segment1']['projPath'], targetPair['segment1']['defaultBranchName'])
    switchToHeadCommit(targetPair['segment2']['projPath'], targetPair['segment2']['defaultBranchName'])
    
    # step2: get function name using ctags
    # targetPair['segment1']['functionName'], targetPair['segment1']['pattern'] = getFunctionName_Ptn(targetPair['segment1']['filePath'], targetPair['segment1']['startLine'], targetPair['segment1']['endLine'], language)
    # targetPair['segment2']['functionName'], targetPair['segment2']['pattern'] = getFunctionName_Ptn(targetPair['segment2']['filePath'], targetPair['segment2']['startLine'], targetPair['segment2']['endLine'], language)
    
    
    # step3: get diff history using git
    targetPair['segment1']['diffHis'] = getDiffHistory(targetPair['segment1']['projPath'], targetPair['segment1']['filePath'])
    targetPair['segment2']['diffHis'] = getDiffHistory(targetPair['segment2']['projPath'], targetPair['segment2']['filePath'])

    
    # step4: copy target file in each target commit
    # step5: get position of target function in each target file using ctags




    for commitIdObj in getCommitIdListFromHistoryByDateOrder(targetPair['segment1']['diffHis'], "segment1"):
        pathInCommit = copyTargetFileToFolder(targetPair['segment1']['projPath'], targetPair['segment1']['filePath'], targetPair['segment1']['projectName'], targetPair['segment1']['functionName'], commitIdObj[0], workFolder)
        
        startLine = 0
        endLine = len(open(pathInCommit, "r").readlines()) - 1
            
        targetPair['segment1']['diffHis'][commitIdObj[0]]['startLine'] = startLine
        targetPair['segment1']['diffHis'][commitIdObj[0]]['endLine'] = endLine
        targetPair['segment1']['diffHis'][commitIdObj[0]]['pathInCommit'] = pathInCommit
    
    
    
    for commitIdObj in getCommitIdListFromHistoryByDateOrder(targetPair['segment2']['diffHis'],"segment2"):
        pathInCommit = copyTargetFileToFolder(targetPair['segment2']['projPath'], targetPair['segment2']['filePath'], targetPair['segment2']['projectName'], targetPair['segment2']['functionName'], commitIdObj[0], workFolder)

        startLine = 0
        endLine = len(open(pathInCommit, "r").readlines()) - 1
            
        targetPair['segment2']['diffHis'][commitIdObj[0]]['startLine'] = startLine
        targetPair['segment2']['diffHis'][commitIdObj[0]]['endLine'] = endLine
        targetPair['segment2']['diffHis'][commitIdObj[0]]['pathInCommit'] = pathInCommit
   

    
    # step6: similarity calculation 
    
    similarityList = []
    commitList1 = getCommitIdListFromHistoryByDateOrder(targetPair['segment1']['diffHis'],"segment1")
    commitList2 = getCommitIdListFromHistoryByDateOrder(targetPair['segment2']['diffHis'],"segment2")
    
    if len(commitList1) <= 1 and len(commitList2) <= 1:
        print("No modification in both segments")
        similarityList.append(generateSimilarityCalItem(commitList1[0], commitList2[0]))
        
    else:
        commitList  = mergeTwoCommitIdListByDateOrder(commitList1, commitList2)
        
        cursor = 0
        while cursor < len(commitList): 
            
            targetCursor = cursor + 1
            
            while targetCursor < len(commitList) and commitList[targetCursor][1] == commitList[cursor][1]:
                targetCursor += 1
       
            
            if targetCursor < len(commitList): # positive search
                similarityList.append(generateSimilarityCalItem(commitList[cursor], commitList[targetCursor]))

            else: # turn to negative search
                targetCursor = cursor - 1
                while commitList[targetCursor][1] == commitList[cursor][1]:
                    targetCursor = targetCursor - 1
                    if targetCursor < 0:
                        break
                
                if cursor - 1 == targetCursor: # this pair is already calculated
                    pass
                else:
                    similarityList.append(generateSimilarityCalItem(commitList[targetCursor], commitList[cursor]))
            
            cursor = cursor + 1
                    
            
    
    # step7: output report
    result = {
        "taskId": taskId,
        "detectionId": detectionId,
        "cloneIndex": cloneIndex,
        "targetPair" : targetPair,
        "similarityList" : similarityList
    }
    
    open(workFolder + "result.json", "w").write(ujson.dumps(result, indent=2))
    for item in similarityList:
        print(str(item['similarity'][0]))
        
    
    switchToHeadCommit(targetPair['segment1']['projPath'], targetPair['segment1']['defaultBranchName'])
    switchToHeadCommit(targetPair['segment2']['projPath'], targetPair['segment2']['defaultBranchName'])
    