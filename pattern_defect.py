import os, sys, ujson

def getDefectCloneIndexSet(taskId, detectionId):
    defectCloneIndxList = set()
    source = "./reports/" + taskId + "-" + detectionId + "/commitContentList4.json"
    res = ujson.loads(open(source, "r").read())
    
    defect = 0
    
    print("Commit num: " + str(len(res.keys())))
    
    for commitId in res:
        if res[commitId]['isDefect']:
            defect += 1
            for cloneIndexItem in res[commitId]['cloneIndex']:
                defectCloneIndxList.add(cloneIndexItem[0])

    print("Defect commit num: " + str(defect))
    return defectCloneIndxList

def getCloneIndexSetForPattern(taskId, detectionId, pattern):
    PTN = {
        1: "------Ptn1 List-----",
        2: "------Ptn2 List-----",
        3: "------Ptn3 List-----",
        4: "------Ptn4 List-----",
        5: "------Ptn5 List-----"
    }
    
    source = "./reports/" + taskId + "-" + detectionId + "/patternClassified_0.05.txt"
    sourceLines = open(source, "r").readlines()
    for lineIndex in range(len(sourceLines)):

        if PTN[pattern] in sourceLines[lineIndex]:
            return set(ujson.loads(sourceLines[lineIndex + 1]))


if __name__ == "__main__":
    # taskId = sys.argv[1]
    # detectionId = sys.argv[2]
    
    taskId = "11008"
    detectionId = "10"
    
    defectIndexSet = getDefectCloneIndexSet(taskId, detectionId)
    
    for ptn in [1,2,3,4,5]:
        cloneIndexSet = getCloneIndexSetForPattern(taskId, detectionId, ptn)
        if cloneIndexSet == None:
            cloneIndexSet = set()
        
        res = defectIndexSet.intersection(cloneIndexSet)
        
        print("Pattern " + str(ptn) + " defect clone index list: ")
        print(res)
        print("Pattern " + str(ptn) + " defect clone index list length: ")
        print(len(res))
        print("\n")
        
    
    