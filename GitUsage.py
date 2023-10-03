import os,sys, datetime
# git log -L:main:controller.py --no-patch

def getCommitIdListFromHistoryByDateOrder(diffHistoryDict):
    commitIdList = []
    for commitId in diffHistoryDict:
        commitIdList.append(commitId)
    commitIdList.reverse()
    return commitIdList

def transDiffHistoryToDict(diffHistory):
    diffHistoryDict = {}
    for line in diffHistory:
        if "commit" in line:
            commit = line.split(" ")[1].strip()
            diffHistoryDict[commit] = {"Content":[]}
        elif "Author:" in line:
            author = line.split("Author:")[1].strip()
            diffHistoryDict[commit]['author'] = author
        elif "Date:" in line:
            date = line.split("Date:")[1].strip()
            diffHistoryDict[commit]['date'] = date
        elif "    " in line:
            diffHistoryDict[commit]['Content'].append(line.strip())
    return diffHistoryDict

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
        

def getDiffHistory(projPath, filePath, functionName):
    # cmd = "cd " + projPath + "; git log --pretty=format:\"%H\" -S \"" + functionName + "\" -- " + filePath
    filePath_relative = filePath.replace(projPath, "")
    if filePath_relative[0] == "/":
        filePath_relative = filePath_relative[1:]
    
    cmd = "cd " + projPath + "; git log -L:" + functionName + ":" + filePath_relative + " --no-patch"
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
    
    cmd = "cd " + projPath + "; git checkout " + commitId + "; cp " + filePath_relative + " " + targetFolder + "/" + commitId + extName
    os.popen(cmd)
    
    return targetFolder + "/" + commitId + extName

def switchToHeadCommit(projPath):    
    # switch the target repository to head commit 
    cmd = "cd " + projPath + "; git checkout master"
    res = os.popen(cmd).readlines()
    # print(res)
    
    

def getExtensionNameFromFilePath(filePath):
    return os.path.splitext(filePath)[1]



