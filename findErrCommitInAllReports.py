import os, ujson

def find_result_json_files(folder_path):
    result_files = []
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file == 'result.json':
                full_path = os.path.join(root, file)
                
                if not 'file' in full_path:
                    continue
                
                result_files.append(full_path)
    return result_files

ErrKeyword = ["error", "errors", "bug", "bugs", "issue", "issues"]

def cmtMsgContainsError(commitMessage):
    commitMessageWordSet = set(commitMessage.lower().split())
    for keyword in ErrKeyword:
        if keyword in commitMessageWordSet:
            return True
    return False



if __name__ == "__main__":
    res = find_result_json_files('./reports')
    pairNum = 0
    for resultJSONFile in res:
        resultObj = ujson.loads(open(resultJSONFile, 'r').read())
        
        if len(resultObj['similarityList']) < 1:
            continue
        
        if not( resultObj['similarityList'][0]['similarity'][0] >= 0.8 or resultObj['similarityList'][0]['similarity'][1] >= 0.8 or resultObj['similarityList'][-1]['similarity'][0] >= 0.8 or resultObj['similarityList'][-1]['similarity'][1] >= 0.8):
            continue
        
        for commitId in resultObj['targetPair']['segment1']['diffHis']:
            commitMsg = " ".join(resultObj['targetPair']['segment1']['diffHis'][commitId]['Content'])
            res = []
            if cmtMsgContainsError(commitMsg):
                res.append("segment1: " + commitMsg) 
                
                
                
        for commitId in resultObj['targetPair']['segment2']['diffHis']:
            commitMsg = " ".join(resultObj['targetPair']['segment2']['diffHis'][commitId]['Content'])
            if cmtMsgContainsError(commitMsg):
                res.append("segment2: " + commitMsg)
        
        if len(res) > 0:
            res.insert(0, resultJSONFile[:-11] + "report.html")
        
        if len(res) > 0:
            print(res[0])
            pairNum += 1
    
    print("Total pair number: " + str(pairNum))