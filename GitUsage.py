import os,sys, datetime
import time
# git log -L:main:controller.py --no-patch

def mergeTwoCommitIdListByDateOrder(commitIdList1, commitIdList2):
    res = []
    while len(commitIdList1) > 0 and len(commitIdList2) > 0:
        if compareDateByStr(commitIdList1[0][2], commitIdList2[0][2]):
            res.append(commitIdList2[0])
            commitIdList2.pop(0)
        else:
            res.append(commitIdList1[0])
            commitIdList1.pop(0)
            
    if len(commitIdList1) > 0:
        res.extend(commitIdList1)
        
    if len(commitIdList2) > 0:
        res.extend(commitIdList2)
    return res


def getDefaultBranchName(projPath):
    cmd = "cd " + projPath + "; git remote show origin"
    res = os.popen(cmd).readlines()
    for line in res:
        if "HEAD branch" in line:
            return line.split(":")[1].strip()
    
    return "master"
    

def ifFileDifferenceInLineRange(diffHistoryObj1, diffHistoryObj2):
    # file1, startLine1, endLine1, file2, startLine2, endLine2
    file1      = diffHistoryObj1['pathInCommit']
    startLine1 = diffHistoryObj1['startLine']
    endLine1   = diffHistoryObj1['endLine']
    file2      = diffHistoryObj2['pathInCommit']
    startLine2 = diffHistoryObj2['startLine']
    endLine2   = diffHistoryObj2['endLine']
    
    if startLine1 < 0 and startLine2 < 0:
        return None
    elif (startLine1 < 0 and startLine2 >= 0) or (startLine1 >= 0 and startLine2 < 0):
        return "Target segment initialization"
    
    # diffInRange.sh oldCommitFile startLine1 endLine1 newCommitFile startLine2 endLine2
    cmd = "./diffInRange.sh " + file1 + " " + str(startLine1) + " " + str(endLine1) + " " + file2 + " " + str(startLine2) + " " + str(endLine2)
    res = os.popen(cmd).read()
    if len(res) > 0:
        return res
    else:
        return None
    
def commitIdListFilterByFileDifferenceInLineRange(commitIdList, diffHistoryDict):
    
    res = [] # a queue, left side is the oldest commit id
    
    len_before = len(res)
    
        
    # res.append(commitIdList[-1])
    
    cursor = len(commitIdList) - 1
    while cursor >= 1:
        commitId = commitIdList[cursor][0]
        commitId_pre = commitIdList[cursor - 1][0]
        
        fileDiffRes = ifFileDifferenceInLineRange(diffHistoryDict[commitId], diffHistoryDict[commitId_pre])
        if fileDiffRes != None:    
            res.insert(0, commitIdList[cursor])
            diffHistoryDict[commitId]['diffContent'] = fileDiffRes
            
        cursor -= 1
    
    if len(res) == 0:
        res.insert(0, commitIdList[-1])
        
    if len_before > len(res) and len(res) <= 1:
        print("Most file modification included commit was filtered out, please check if there are function renaming or file renaming in the commit history")
        # sys.exit()
    
    return res



   

def getCommitIdListFromHistoryByDateOrder(diffHistoryDict, segmentId): 
    commitIdList = []
    for commitId in diffHistoryDict:
        if "startLine" in diffHistoryDict[commitId]: 
            if diffHistoryDict[commitId]['startLine'] != -1:
                commitIdList.append( (commitId, segmentId, diffHistoryDict[commitId]['date']) )
        else:
            commitIdList.append( (commitId, segmentId, diffHistoryDict[commitId]['date']) )
    commitIdList.reverse()
    
    return commitIdList 
    # return commitIdListFilterByFileDifferenceInLineRange(commitIdList, diffHistoryDict) # commitIdList[0] is the oldest commit id

def getCommitIdListFromHistoryByDateOrder_fileExistense(diffHistoryDict, segmentId):
    commitIdList = []
    for commitId in diffHistoryDict:
        if 'pathInCommit' in diffHistoryDict[commitId]:
            commitIdList.append( (commitId, segmentId, diffHistoryDict[commitId]['date']) )
    commitIdList.reverse()
    
    return commitIdList


# an example that code provided by capilot is buggy
# def transDiffHistoryToDict(diffHistory):
#     diffHistoryDict = {}
#     for line in diffHistory:
#         if "commit" in line:
#             commit = line.split(" ")[1].strip()
#             diffHistoryDict[commit] = {"Content":[]}
#         elif "Author:" in line:
#             author = line.split("Author:")[1].strip()
#             diffHistoryDict[commit]['author'] = author
#         elif "Date:" in line:
#             date = line.split("Date:")[1].strip()
#             diffHistoryDict[commit]['date'] = date
#         elif "    " in line:
#             diffHistoryDict[commit]['Content'].append(line.strip())
#     return diffHistoryDict

def transDiffHistoryToDict(diffHistory):
    diffHistoryDict = {}
    for line in diffHistory:
    
        headStr = line[:7]
        
        if "commit" in headStr:
            commit = line.split(" ")[1].strip()
            diffHistoryDict[commit] = {"Content":[]}
        elif "Author:" in headStr:
            author = line.split("Author:")[1].strip()
            diffHistoryDict[commit]['author'] = author
        elif "Date:" in headStr:
            date = line.split("Date:")[1].strip()
            diffHistoryDict[commit]['date'] = date
        elif "    " in headStr:
            diffHistoryDict[commit]['Content'].append(line.strip())
            
    return diffHistoryDict

def compareDateByStr(dateStr1, dateStr2):
    date1 = datetime.datetime.strptime(dateStr1, "%a %b %d %H:%M:%S %Y %z")
    date2 = datetime.datetime.strptime(dateStr2, "%a %b %d %H:%M:%S %Y %z")
    
    if date1 >= date2:
        return True
    else:
        return False

# compare date by given two commit id in the diffHistoryDict and return the newer one
def compareDateInDiffHistoryDict(diffHistoryDict1, commitId1, diffHistoryDict2, commitId2):
    date1Str = diffHistoryDict1[commitId1]['date']
    date1 = datetime.datetime.strptime(date1Str, "%a %b %d %H:%M:%S %Y %z")
    date2Str = diffHistoryDict2[commitId2]['date']
    date2 = datetime.datetime.strptime(date2Str, "%a %b %d %H:%M:%S %Y %z")
    
    if date1 >= date2: # date1 is the newer one
        return True    
    else: # date1 is the older one
        return False
        

def getDiffHistory(projPath, filePath, defaultBranchName):
    # cmd = "cd " + projPath + "; git log --pretty=format:\"%H\" -S \"" + functionName + "\" -- " + filePath
    filePath_relative = filePath.replace(projPath, "")
    if filePath_relative[0] == "/":
        filePath_relative = filePath_relative[1:]
    
    # cmd = "cd " + projPath + "; git log -L:" + functionName + ":" + filePath_relative + " --no-patch"
    # cmd = "cd " + projPath + "; git log " + filePath_relative
    cmd = "cd " + projPath + "; git log " + defaultBranchName + " -- " + filePath_relative
    res = os.popen(cmd).readlines()
    return transDiffHistoryToDict(res)



def copyTargetFileToFolder(projPath, filePath, projName, functionName, commitId, targetFolder):
    filePath_relative = filePath.replace(projPath, "")
    if filePath_relative[0] == "/":
        filePath_relative = filePath_relative[1:]
    extName = getExtensionNameFromFilePath(filePath)    
        
    targetFolder = targetFolder + "/" + projName + "_" + functionName
    if not os.path.exists(targetFolder):
        os.mkdir(targetFolder)
    # convert targetFolder to absolute path
    targetFolder = os.path.abspath(targetFolder)
    
    cmd = "cd " + projPath + "; git checkout -f " + commitId + "; cp " + filePath_relative + " " + targetFolder + "/" + commitId + extName
    #execute the command cmd and wait for the result
    os.popen(cmd).readlines()
        
    return targetFolder + "/" + commitId + extName


def copyTargetFileToFilder_fileLevel(projPath, filePath, projName, commitId, targetFolder):
    

    
    filePath_relative = filePath.replace(projPath, "")
    if filePath_relative[0] == "/":
        filePath_relative = filePath_relative[1:]
    extName = getExtensionNameFromFilePath(filePath)  
    
    fileName = filePath_relative.split("/")[-1]  
        
    targetFolder = targetFolder + "/" + projName + "_" + fileName
    if not os.path.exists(targetFolder):
        os.mkdir(targetFolder)
    
    # convert targetFolder to absolute path
    targetFolder = os.path.abspath(targetFolder)
    
    cmd = "cd " + projPath + "; git checkout -f " + commitId + "; cp " + filePath_relative + " " + targetFolder + "/" + commitId + extName
    #execute the command cmd and wait for the result
    os.popen(cmd).readlines()
    
    if os.path.exists(targetFolder + "/" + commitId + extName):        
        return targetFolder + "/" + commitId + extName
    else:
        print("File not exists: " + targetFolder + "/" + commitId + extName)
        return None


def switchToHeadCommit(projPath, defaultBranchName):    
    # switch the target repository to head commit 
    cmd = "cd " + projPath + "; git checkout -f " + defaultBranchName
    os.popen(cmd).readlines()
    # print(res)
    
    

def getExtensionNameFromFilePath(filePath):
    return os.path.splitext(filePath)[1]



