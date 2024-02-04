import os, sys, ujson 
from jinja2 import Environment, FileSystemLoader

CLONETRACKER_PATH = "/Users/syu/workspace/MSCCD_CloneHistoryTracker/"

def getFileContent(file, startLine, endLine):
    if os.path.exists(file):
        fileLines = open(file,"r").readlines()
        
        if startLine < 0:
            if len(fileLines) == 1:
                return fileLines[0]
            else:
                return "Target function not found in this commit."
        else:
            return fileLines[startLine-1:endLine]

def generateJSONForDVG( commitList, similarityList):

    res = {
        "points" : [],  # older to newer
        "links" : []
    }
    for commitIndex in range(len(commitList)):
        res['points'].append({
            "segment" : commitList[commitIndex][1],
            "commitId" : commitList[commitIndex][0],
            "indexInList" : commitIndex
        })
    
    for simiItem in similarityList:
        linkItem = []
        for pointIndex in range(len(res['points'])):
            if res['points'][pointIndex]['commitId'] == simiItem['segment1']['commitId'] or res['points'][pointIndex]['commitId'] == simiItem['segment2']['commitId']:
                linkItem.append(pointIndex)
        linkItem.append(simiItem['similarity'][0])
        res['links'].append(linkItem)

            
            
    # open(outputFile,"w").write(ujson.dumps(res))
    return res

if __name__ == "__main__":
    taskId      = sys.argv[1]
    detectionId = sys.argv[2]
    cloneIndex  = sys.argv[3]
    
    # taskId      = "11011"
    # detectionId = "10"
    # cloneIndex  = "31"
    
    trackerResultSource = CLONETRACKER_PATH + "reports/" + taskId + "-" + detectionId + "/" + cloneIndex + "/result.json"
    outputFile = CLONETRACKER_PATH + "reports/" + taskId + "-" + detectionId + "/" + cloneIndex + "/report.html"
    trackerResult = ujson.loads(open(trackerResultSource,"r").read())
    
    if "functionName" in trackerResult["targetPair"]['segment1']:
    
        result = {
            "segment1" : {
                "projectName" : trackerResult["targetPair"]['segment1']['projectName'],
                "filePath"    : trackerResult["targetPair"]['segment1']['filePath'],
                "functionName": trackerResult["targetPair"]['segment1']['functionName'],
                "defaultBranch" : trackerResult["targetPair"]['segment1']['defaultBranchName'],
                "commitNum_fileModification" : trackerResult["targetPair"]['segment1']['commitNum_fileModification'],
                "commitNum_functionIdendified" : trackerResult["targetPair"]['segment1']['commitNum_functionIdendified'],
                "commitNum_functionModification" : trackerResult["targetPair"]['segment1']['commitNum_functionModification']
            },
            "segment2" : {
                "projectName" : trackerResult["targetPair"]['segment2']['projectName'],
                "filePath"    : trackerResult["targetPair"]['segment2']['filePath'],
                "functionName": trackerResult["targetPair"]['segment2']['functionName'],
                "defaultBranch" : trackerResult["targetPair"]['segment2']['defaultBranchName'],
                "commitNum_fileModification" : trackerResult["targetPair"]['segment2']['commitNum_fileModification'],
                "commitNum_functionIdendified" : trackerResult["targetPair"]['segment2']['commitNum_functionIdendified'],
                "commitNum_functionModification" : trackerResult["targetPair"]['segment2']['commitNum_functionModification']
            },    
            "simiItems" : [],
            "language": trackerResult["targetPair"]['language']

            
        }
    else:
        result = {
            "segment1" : {
                "projectName" : trackerResult["targetPair"]['segment1']['projectName'],
                "filePath"    : trackerResult["targetPair"]['segment1']['filePath'],
                "defaultBranch" : trackerResult["targetPair"]['segment1']['defaultBranchName'],
                "commitNum_fileModification" : trackerResult["targetPair"]['segment1']['commitNum_fileModification'],
                "commitNum_functionIdendified" : "",
                "commitNum_functionModification" :""
            },
            "segment2" : {
                "projectName" : trackerResult["targetPair"]['segment2']['projectName'],
                "filePath"    : trackerResult["targetPair"]['segment2']['filePath'],
                "defaultBranch" : trackerResult["targetPair"]['segment2']['defaultBranchName'],
                "commitNum_fileModification" : trackerResult["targetPair"]['segment2']['commitNum_fileModification'],
                "commitNum_functionIdendified" : "",
                "commitNum_functionModification" :  ""
            },    
            "simiItems" : [],
            "language": trackerResult["targetPair"]['language']
            
        }
    
    for simiItem_input_index in range(len(trackerResult["similarityList"])):
        
        simiItem_input = trackerResult["similarityList"][simiItem_input_index]
        
        simiItem_output = {
            "segment1" : simiItem_input['segment1'],
            "segment2" : simiItem_input['segment2'],
            "diffContent": "",
            "reasonSegment" : simiItem_input['reasonSegment'],
            "newerSegment" : simiItem_input['newerSegment'],
            "oSimi": simiItem_input['similarity'][0],
            "lSimi": simiItem_input['similarity'][1],
            "index" : simiItem_input_index
        }
        
        simiItem_output['segment1']['code'] = "".join(getFileContent(simiItem_input['segment1']['commitContent']['pathInCommit'], simiItem_input['segment1']['commitContent']['startLine'], simiItem_input['segment1']['commitContent']['endLine']))
        simiItem_output['segment2']['code'] = "".join(getFileContent(simiItem_input['segment2']['commitContent']['pathInCommit'], simiItem_input['segment2']['commitContent']['startLine'], simiItem_input['segment2']['commitContent']['endLine']))
        
        if simiItem_input_index > 0:   # show diff content
        
            if "diffContent" in simiItem_input[simiItem_input['reasonSegment']]['commitContent']:
                simiItem_output['diffContent'] = simiItem_input[simiItem_input['reasonSegment']]['commitContent']['diffContent']
        
        result['simiItems'].append(simiItem_output)
        
    result['DVGData'] = generateJSONForDVG(trackerResult['commitList'], trackerResult['similarityList'])
    
        
    env = Environment(loader=FileSystemLoader('./'))
    template = env.get_template('templete/templete.html')
    with open(outputFile,'w') as HTMLFile:
        htmlContent = template.render(report=result)
        HTMLFile.write(htmlContent)
        HTMLFile.close()
    
    print("Report generated: " + outputFile)