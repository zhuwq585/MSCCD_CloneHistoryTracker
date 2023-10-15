import os, sys, ujson 
from jinja2 import Environment, FileSystemLoader

CLONETRACKER_PATH = "/Users/syu/workspace/MSCCD_CloneHistoryTracker/"

def getFileContent(file, startLine, endLine):
    if os.path.exists(file):
        return open(file,"r").readlines()[startLine-1:endLine]

if __name__ == "__main__":
    # taskId      = sys.argv[1]
    # detectionId = sys.argv[2]
    # cloneIndex  = sys.argv[3]
    
    taskId      = "11008"
    detectionId = "1"
    cloneIndex  = "138"
    
    trackerResultSource = CLONETRACKER_PATH + "reports/" + taskId + "-" + detectionId + "-" + cloneIndex + "/result.json"
    outputFile = CLONETRACKER_PATH + "reports/" + taskId + "-" + detectionId + "-" + cloneIndex + "/report.html"
    trackerResult = ujson.loads(open(trackerResultSource,"r").read())
    
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
        "simiItems" : []
        
    }
    
    for simiItem_input_index in range(len(trackerResult["similarityList"])):
        simiItem_input = trackerResult["similarityList"][simiItem_input_index]
        simiItem_output = {
            "segment1" : {},
            "segment2" : {},
            "diffContent": "",
            "diffIndex" : None,
            "oSimi": simiItem_input['similarity'][0],
            "lSimi": simiItem_input['similarity'][1]
        }
        
        newerCommit = {
            "commitId" : simiItem_input['newCommit'],
            "date" : simiItem_input['newCommitContent']['date'],
            "position" : str(simiItem_input['newCommitContent']['startLine']) + "-" + str(simiItem_input['newCommitContent']['endLine']),
            "author" : simiItem_input['newCommitContent']['author'],
            "commitContent" : "".join(simiItem_input['newCommitContent']['Content']),
            "code" : "".join(getFileContent(simiItem_input['newCommitContent']['pathInCommit'], simiItem_input['newCommitContent']['startLine'], simiItem_input['newCommitContent']['endLine']))
        }
        olderCommit = {
            "commitId" : simiItem_input['oldCommit'],
            "date" : simiItem_input['oldCommitContent']['date'],
            "position" : str(simiItem_input['oldCommitContent']['startLine']) + "-" + str(simiItem_input['oldCommitContent']['endLine']),
            "author" : simiItem_input['oldCommitContent']['author'],
            "commitContent" : "".join(simiItem_input['oldCommitContent']['Content']),
            "code" : "".join(getFileContent(simiItem_input['oldCommitContent']['pathInCommit'], simiItem_input['oldCommitContent']['startLine'], simiItem_input['oldCommitContent']['endLine']))
        }
        
        # print(olderCommit['code'])
        
        if simiItem_input_index > 0:
            segmentMatching = None # 1: segment1 is the newer version, 2: segment2 is the newer version
            
            if simiItem_input['newProj'] == result['segment1']['projectName']:## segment1 is the newer version
                simiItem_output['segment1'] = newerCommit
                simiItem_output['segment2'] = olderCommit
                segmentMatching = 1
            else:## segment2 is the newer version
                simiItem_output['segment1'] = olderCommit
                simiItem_output['segment2'] = newerCommit
                segmentMatching = 2
                
            
            if "diffContent" in simiItem_input['newCommitContent'] and "diffContent" in simiItem_input['oldCommitContent']:
                simiItem_output['diffContent'] = simiItem_input['newCommitContent']['diffContent']
                simiItem_output['diffIndex'] = segmentMatching
            else:
                if "diffContent" in simiItem_input['newCommitContent']: 
                    simiItem_output['diffContent'] = simiItem_input['newCommitContent']['diffContent']

                    if segmentMatching == 1:
                        simiItem_output['diffIndex'] = 1
                    else:
                        simiItem_output['diffIndex'] = 2
                elif "diffContent" in simiItem_input['oldCommitContent']:
                    simiItem_output['diffContent'] = simiItem_input['oldCommitContent']['diffContent']
                    
                    if segmentMatching == 1:
                        simiItem_output['diffIndex'] = 2
                    else:
                        simiItem_output['diffIndex'] = 1
        else:
            if simiItem_input['newProj'] == result['segment1']['projectName']:## segment1 is the newer version
                simiItem_output['segment1'] = newerCommit
                simiItem_output['segment2'] = olderCommit
            else:## segment2 is the newer version
                simiItem_output['segment1'] = olderCommit
                simiItem_output['segment2'] = newerCommit
            simiItem_output['diffIndex'] = 0
                

   
        
        result['simiItems'].append(simiItem_output)
        
        
    env = Environment(loader=FileSystemLoader('./'))
    template = env.get_template('templete/templete.html')
    with open(outputFile,'w') as HTMLFile:
        htmlContent = template.render(report=result)
        HTMLFile.write(htmlContent)
        HTMLFile.close()
    
    print("Report generated: " + outputFile)