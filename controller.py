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
    
def generateSimilarityCalItem(olderCommitItem, newerCommitItem, reasonSegment):
    # olderCommitItem, newerCommitItem
    # res = {
    #     "newCommit" : newerCommitItem[0],
    #     "newCommitContent" : targetPair[newerCommitItem[1]]['diffHis'][newerCommitItem[0]],
    #     "newProj" : targetPair[newerCommitItem[1]]['projectName'],
    #     "oldCommit" : olderCommitItem[0],
    #     "oldCommitContent" : targetPair[olderCommitItem[1]]['diffHis'][olderCommitItem[0]],
    #     "similarity" : similarityCalculation(targetPair[olderCommitItem[1]]['diffHis'][olderCommitItem[0]]['pathInCommit'], targetPair[olderCommitItem[1]]['diffHis'][olderCommitItem[0]]['startLine'], targetPair[olderCommitItem[1]]['diffHis'][olderCommitItem[0]]['endLine'], targetPair[newerCommitItem[1]]['diffHis'][newerCommitItem[0]]['pathInCommit'], targetPair[newerCommitItem[1]]['diffHis'][newerCommitItem[0]]['startLine'], targetPair[newerCommitItem[1]]['diffHis'][newerCommitItem[0]]['endLine'], keywordsList, targetPair['language'])
    # }  
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


if __name__ == "__main__":
    
    # step1: get info from task.obj in MSCCD task folder
    
    # taskId      = sys.argv[1]
    # detectionId = sys.argv[2]
    # cloneIndex  = sys.argv[3]
    # keywordsList = sys.argv[4]
    # language = sys.argv[5]
    
    ### for test
    taskId      = "11011"
    detectionId = "3"
    cloneIndex  = 10790
    keywordsList = "/Users/syu/workspace/MSCCD/grammarDefinations/Go/Go.reserved"
    language = "Go" #{"Java", "Go", "C","JavaScript","C++"}
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
        "language" : taskObj['configObj']['tokenizer']
    }
    
    switchToHeadCommit(targetPair['segment1']['projPath'], targetPair['segment1']['defaultBranchName'])
    switchToHeadCommit(targetPair['segment2']['projPath'], targetPair['segment2']['defaultBranchName'])
    
    # step2: get function name using ctags
    targetPair['segment1']['functionName'], targetPair['segment1']['pattern'] = getFunctionName_Ptn(targetPair['segment1']['filePath'], targetPair['segment1']['startLine'], targetPair['segment1']['endLine'], language)
    targetPair['segment2']['functionName'], targetPair['segment2']['pattern'] = getFunctionName_Ptn(targetPair['segment2']['filePath'], targetPair['segment2']['startLine'], targetPair['segment2']['endLine'], language)
    
    
    # step3: get diff history using git
    targetPair['segment1']['diffHis'] = getDiffHistory(targetPair['segment1']['projPath'], targetPair['segment1']['filePath'], targetPair['segment1']['defaultBranchName'])
    targetPair['segment1']['commitNum_fileModification'] = len(targetPair['segment1']['diffHis'])
    targetPair['segment1']['commitNum_functionIdendified'] = 0
    targetPair['segment2']['diffHis'] = getDiffHistory(targetPair['segment2']['projPath'], targetPair['segment2']['filePath'], targetPair['segment2']['defaultBranchName'])
    targetPair['segment2']['commitNum_fileModification'] = len(targetPair['segment2']['diffHis'])
    targetPair['segment2']['commitNum_functionIdendified'] = 0
    # diffHis1 = getDiffHistory(targetPair['segment1']['projPath'], targetPair['segment1']['filePath'], targetPair['segment1']['functionName'])
    # diffHis2 = getDiffHistory(targetPair['segment2']['projPath'], targetPair['segment2']['filePath'], targetPair['segment2']['functionName'])
    
    # step4: copy target file in each target commit
    # step5: get position of target function in each target file using ctags




    for commitIdObj in getCommitIdListFromHistoryByDateOrder(targetPair['segment1']['diffHis'], "segment1"):
        pathInCommit = copyTargetFileToFolder(targetPair['segment1']['projPath'], targetPair['segment1']['filePath'], targetPair['segment1']['projectName'], targetPair['segment1']['functionName'], commitIdObj[0], workFolder)
        
        try:
            startLine,endLine = getFunctionPosition(pathInCommit, targetPair['segment1']['functionName'], targetPair['segment1']['pattern'], language)
        except TypeError:
            print("Error: " + pathInCommit + " " + targetPair['segment1']['functionName'] + " " + targetPair['segment1']['pattern'])
            startLine = -1
            endLine = -1
        
        if startLine >= 0 and endLine >= 0:
            targetPair['segment1']['commitNum_functionIdendified'] += 1
        targetPair['segment1']['diffHis'][commitIdObj[0]]['startLine'] = startLine
        targetPair['segment1']['diffHis'][commitIdObj[0]]['endLine'] = endLine
        targetPair['segment1']['diffHis'][commitIdObj[0]]['pathInCommit'] = pathInCommit
    
    
    
    for commitIdObj in getCommitIdListFromHistoryByDateOrder(targetPair['segment2']['diffHis'],"segment2"):
        pathInCommit = copyTargetFileToFolder(targetPair['segment2']['projPath'], targetPair['segment2']['filePath'], targetPair['segment2']['projectName'], targetPair['segment2']['functionName'], commitIdObj[0], workFolder)

        try:
            startLine,endLine = getFunctionPosition(pathInCommit, targetPair['segment2']['functionName'], targetPair['segment2']['pattern'],language)
        except TypeError:
            print("Error: Can not find function position" + pathInCommit + " " + targetPair['segment2']['functionName'] + " " + targetPair['segment2']['pattern'])
            startLine = -1
            endLine = -1
            
        if startLine >= 0 and endLine >= 0:
            targetPair['segment2']['commitNum_functionIdendified'] += 1
        targetPair['segment2']['diffHis'][commitIdObj[0]]['startLine'] = startLine
        targetPair['segment2']['diffHis'][commitIdObj[0]]['endLine'] = endLine
        targetPair['segment2']['diffHis'][commitIdObj[0]]['pathInCommit'] = pathInCommit
   

    
    # step6: similarity calculation 
    
    similarityList = []
    commitList1 = commitIdListFilterByFileDifferenceInLineRange(getCommitIdListFromHistoryByDateOrder(targetPair['segment1']['diffHis'],"segment1"), targetPair['segment1']['diffHis']) 
    commitList2 = commitIdListFilterByFileDifferenceInLineRange(getCommitIdListFromHistoryByDateOrder(targetPair['segment2']['diffHis'],"segment2"), targetPair['segment2']['diffHis']) 
    
    targetPair['segment1']['commitNum_functionModification'] = len(commitList1)
    targetPair['segment2']['commitNum_functionModification'] = len(commitList2)
    
    commitList  = mergeTwoCommitIdListByDateOrder(commitList1, commitList2)

    if len(commitList) == 2:
        print("No modification found in both functions.")
        similarityList.append(generateSimilarityCalItem(commitList[0], commitList[1], commitList[1][1]))
        
        
        
    else:
        
        cursor = len(commitList) - 1
        while cursor >= 0: 
            
            targetCursor = cursor - 1
            
            while targetCursor >= 0 and commitList[targetCursor][1] == commitList[cursor][1]:
                targetCursor -= 1
       
            
            if targetCursor >= 0: # got target by positive search (new -> old)
                
                similarityList.insert(0, generateSimilarityCalItem(commitList[targetCursor], commitList[cursor], commitList[cursor][1]))

            else: # no older commit at the other side, negative search (old -> new) to find the cloest one
                targetCursor = cursor + 1
                while commitList[targetCursor][1] == commitList[cursor][1]:
                    targetCursor = targetCursor + 1
                    if targetCursor >= len(commitList):
                        break
                
                if cursor + 1 == targetCursor: # this pair is already calculated but reasonSegment does not have diffContent (because it is the first commit) # update it by this one
                    similarityList.pop(0)
                    similarityList.insert(0, generateSimilarityCalItem(commitList[cursor], commitList[targetCursor], commitList[cursor][1]))
                else:
                    similarityList.insert(0, generateSimilarityCalItem(commitList[cursor], commitList[targetCursor], commitList[cursor][1]))
            
            cursor = cursor - 1
                    
            
    
    # step7: output report
    result = {
        "taskId": taskId,
        "detectionId": detectionId,
        "cloneIndex": cloneIndex,
        "targetPair" : targetPair,
        "similarityList" : similarityList,
        "commitList" : commitList
    }
    
    open(workFolder + "result.json", "w").write(ujson.dumps(result, indent=2))
    for item in similarityList:
        print(str(item['similarity'][0]))
        
    
    switchToHeadCommit(targetPair['segment1']['projPath'], targetPair['segment1']['defaultBranchName'])
    switchToHeadCommit(targetPair['segment2']['projPath'], targetPair['segment2']['defaultBranchName'])
    