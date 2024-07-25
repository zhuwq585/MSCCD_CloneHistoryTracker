import ujson
from datetime import datetime


# [{
#     "date" : "Thu Oct 14 15:55:16 2021 +0800",
#     "similarity" : 0.9,
#     "reasonSegment" : 0 # 0: segment1, 1: segment2
#     "message": ""
# }]

def convertDateToTimestamp(date):
    date_format = "%a %b %d %H:%M:%S %Y %z"
    return datetime.strptime(date, date_format).timestamp()
    # "date" : "Thu Oct 14 15:55:16 2021 +0800",
    # convert to timestamp
    
    
    
    

def generateGraphData(resultJsonFilePath):
    res = {
        'segment1': "",
        'segment2': "",
        'dataList': []
    }
    
    with open(resultJsonFilePath, 'r') as f:
        resultObj = ujson.loads(f.read())
        res['segment1ProjName'] = resultObj['targetPair']['segment1']['projectName']
        res['segment2ProjName'] = resultObj['targetPair']['segment2']['projectName']
        
        currentCommentId  = ""
        
        for similarityListItemIndex in range(len(resultObj['similarityList'])):
            similarityListItem = resultObj['similarityList'][similarityListItemIndex]
            reasonSegment = None
            
            if similarityListItemIndex == 0:
                reasonSegment = "segment1" if similarityListItem['newerSegment'] == "segment2" else "segment2"
                res['dataList'].append({
                    'date': similarityListItem[reasonSegment]['commitContent']['date'],
                    'dataStamp': convertDateToTimestamp(similarityListItem[reasonSegment]['commitContent']['date']),
                    'similarity': similarityListItem['similarity'][0],
                    'reasonSegment': 1 if similarityListItem['newerSegment'] == "segment1" else 0,
                    'message': "",
                    'commitId': similarityListItem[reasonSegment]['commitId']
                })  
                reasonSegment = "segment2" if similarityListItem['newerSegment'] == "segment2" else "segment1"
                res['dataList'].append({
                    'date': similarityListItem[reasonSegment]['commitContent']['date'],
                    'dataStamp': convertDateToTimestamp(similarityListItem[reasonSegment]['commitContent']['date']),
                    'similarity': similarityListItem['similarity'][0],
                    'reasonSegment': 0 if similarityListItem['newerSegment'] == "segment1" else 1,
                    'message': "",
                    'commitId': similarityListItem[reasonSegment]['commitId']
                })             

                currentCommentId = similarityListItem[similarityListItem["newerSegment"]]['commitId']
            else:
                reasonSegment = "segment2" if similarityListItem['newerSegment'] == "segment2" else "segment1"
                res['dataList'].append({
                    'date': similarityListItem[reasonSegment]['commitContent']['date'],
                    'dataStamp': convertDateToTimestamp(similarityListItem[reasonSegment]['commitContent']['date']),
                    'similarity': similarityListItem['similarity'][0],
                    'reasonSegment': 0 if similarityListItem['newerSegment'] == "segment1" else 1,
                    'message': "",
                    'commitId': similarityListItem[reasonSegment]['commitId']
                })
                
                olderSegment = "segment1" if similarityListItem['newerSegment'] == "segment2" else "segment2"
                if similarityListItem[olderSegment]['commitId'] != currentCommentId:
                    currentCommentId = similarityListItem[olderSegment]['commitId']
                
            # if similarityListItemIndex <= len(resultObj['similarityList']) - 2:
            #     # if (similarityListItem['newerSegment'] == "segment1" and resultObj['similarityList'][similarityListItemIndex + 1]['newerSegment'] == "segment1") or (similarityListItem['newerSegment'] == "segment2" and resultObj['similarityList'][similarityListItemIndex + 1]['newerSegment'] == "segment2"):
            #     #     reasonSegment = "segment2"
            #     # else:
            #     #     reasonSegment = "segment1"
            #     if similarityListItem['newerSegment'] == resultObj['similarityList'][similarityListItemIndex + 1]['newerSegment']:
            #         reasonSegment = "segment2" if similarityListItem['newerSegment'] == "segment1" else "segment1"
            #     else:
            #         reasonSegment = "segment1" if similarityListItem['newerSegment'] == "segment1" else "segment2"
                
            # else: 
            #     reasonSegment = "segment1" if similarityListItem['newerSegment'] == "segment1" else "segment2"
            
            
            
            # res['dataList'].append({
            #     'date': similarityListItem[reasonSegment]['commitContent']['date'],
            #     'dataStamp': convertDateToTimestamp(similarityListItem[reasonSegment]['commitContent']['date']),
            #     'similarity': similarityListItem['similarity'][0],
            #     'reasonSegment': 0 if reasonSegment == "segment1" else 1,
            #     'message': "",
            #     'commitId': similarityListItem[reasonSegment]['commitId']
            # })
            
    
    # sort the dataList in res by the timestamp field
    # res['dataList'].sort(key=lambda x: x['date'])
    
      
        
    return res
        
    

if __name__ == "__main__":
    taskId = "20010"
    detectionId = "1"
    granularity = "file"
    cloneIndex = "1474"
    
    # /Users/syu/workspace/MSCCD_CloneHistoryTracker/reports/20021-2_file/324/result.json
    resultJsonFile = "/Users/syu/workspace/MSCCD_CloneHistoryTracker/reports/" + taskId + "-" + detectionId + "_" + granularity + "/"+ cloneIndex + "/result.json"
    
    print(generateGraphData(resultJsonFile))
    
    