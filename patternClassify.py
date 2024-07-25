import sys, os, ujson


# a function that find all folder in the current folder that named by taskId-detectionId and return a list of cloneIndex
# def getCloneIndexList(taskId, detectionId):
#     res = []
#     for cloneIndex in os.listdir(sys.path[0] + "/reports/"):
#         if cloneIndex.startswith(taskId + "-" + detectionId + "-"):
#             res.append(cloneIndex.split("-")[-1])
#     return res

# a function that find the folder in the current folder that named by taskId-detectionId, and return a list of subfolder name in that folder
def getCloneIndexList(taskId, detectionId):
    res = []
    for subFolder in os.listdir(sys.path[0] + "/reports/" + taskId + "-" + detectionId):
        if os.path.isdir(sys.path[0] + "/reports/" + taskId + "-" + detectionId + "/" + subFolder):
            res.append(subFolder)
    return res


def patternClassify(cloneIndex):
    # read the result file
    trackerResultSource = sys.path[0] + "/reports/" + taskId + "-" + detectionId + "/" + cloneIndex + "/result.json"
    try:
        tarckerResult = ujson.loads(open(trackerResultSource,"r").read())
    except Exception:
        return -1
    
    
    res = 0
    
    if len(tarckerResult['similarityList']) == 1:
        res = res | 1
    else:
        if len(tarckerResult['similarityList']) - tarckerResult['negative_search_num'] >= 1: # ptn 2 3 4 5
            

            similarity_oldest = tarckerResult['similarityList'][0]['similarity'][0]
            similarity_start = tarckerResult['similarityList'][0 + tarckerResult['negative_search_num']]['similarity'][0]
            similarity_newest = tarckerResult['similarityList'][-1]['similarity'][0]
            similarity_max = 0
            similarity_min = 1
            
            cursor  = tarckerResult['negative_search_num']
            while cursor < len(tarckerResult['similarityList']):
                if tarckerResult['similarityList'][cursor]['similarity'][0] > similarity_max:
                    similarity_max = tarckerResult['similarityList'][cursor]['similarity'][0]
                if tarckerResult['similarityList'][cursor]['similarity'][0] < similarity_min:
                    similarity_min = tarckerResult['similarityList'][cursor]['similarity'][0]
                cursor += 1
            
            
            
            
            if similarity_max < 0.6:
                return -1
            
            if similarity_max - similarity_min >= similarity_changed_threshold:
                res = res | 128 
            
            function_modification_sum = tarckerResult['targetPair']['segment1']['commitNum_functionModification'] + tarckerResult['targetPair']['segment2']['commitNum_functionModification']
            if len(tarckerResult['similarityList']) >= 4 and ( tarckerResult['targetPair']['segment1']['commitNum_functionModification'] / function_modification_sum <= 0.75 or tarckerResult['targetPair']['segment2']['commitNum_functionModification'] / function_modification_sum <= 0.75):
                res = res | 64
            
            if similarity_oldest - similarity_start >= similarity_changed_threshold:
                res = res | 32
                
            if similarity_start == 1 and similarity_newest != 1:
                res = res | 16
                
            if similarity_newest == 1 and similarity_start != 1:
                res = res | 8
            
            # reasonSegmentSet = set()
            # for similarityItem in tarckerResult['similarityList']:
            #     reasonSegmentSet.add(similarityItem['reasonSegment'])
            ## It used to use the length of reasonSegmentSet to judge pattern
            ## Now change the approch to calculate segment num
            
            seg1CommitSet = set()
            seg2CommitSet = set()
            for item in tarckerResult['similarityList']:
                seg1CommitSet.add(item['segment1']['commitId'])
                seg2CommitSet.add(item['segment2']['commitId'])
            
            
            if len(seg1CommitSet) == 1 or len(seg2CommitSet) == 1: # 2,4 similarity changed single size
                if similarity_newest - similarity_start >= similarity_changed_threshold:  # similarity increased
                    res = res | 2
                elif similarity_newest - similarity_start <= -similarity_changed_threshold: # similarity decreased
                    res = res | 4
                else:   # similarity not changed
                    res = res | 6
            else: # 4 5 similarity changed both size
                if similarity_newest - similarity_start >= similarity_changed_threshold:    # similarity increased
                    res = res | 3
                elif similarity_newest - similarity_start <= -similarity_changed_threshold: # similarity decreased
                    res = res | 5
                else:   # similarity not changed
                    res = res | 7
            
        # elif len(tarckerResult['similarityList']) - tarckerResult['negative_search_num'] < 1: # PTN 1 
        #     res = res | 1

    
    return res
    

if __name__ == "__main__":
    # parameter: taskId, detectionId
    taskId = sys.argv[1]
    detectionId = sys.argv[2]
    similarity_changed_threshold = float(sys.argv[3])
    
    # test
    # taskId = "20009"
    # detectionId = "11"
    # similarity_changed_threshold = 0.05
    
        
    # result arrays
    result_dict = {
        1:[],
        2:[],
        3:[],
        4:[],
        5:[],
        6:[],
        7:[]
    }

    simi_newest_100 = []
    simi_start_100 = []
    simi_old_start = []
    function_modification_averaged = []
    max_min_High = []
    
    
    
    cloneIndexes = getCloneIndexList(taskId, detectionId)
    
    for cloneIndex in cloneIndexes:
        res = patternClassify(cloneIndex)
        
        if res == -1:
            print("Error: similarity_newest < 0.7 in cloneIndex " + cloneIndex)
            continue
        
        ptn = res & 7
        if ptn in result_dict:
            result_dict[ptn].append(cloneIndex)
            
            if res & 8:
                simi_newest_100.append(cloneIndex)
            if res & 16:
                simi_start_100.append(cloneIndex)
            if res & 32:
                simi_old_start.append(cloneIndex)
            if res & 64:
                function_modification_averaged.append(cloneIndex)    
            if res & 128:
                max_min_High.append(cloneIndex)
            
        else:
            print("Error: ptn not in result_dict in cloneIndex " + cloneIndex)
            continue
        
    report = []
    report.append("Ptn1: " + str(len(result_dict[1]))) 
    report.append("Ptn2: " + str(len(result_dict[2]) + len(result_dict[6])))
    report.append("Ptn3: " + str(len(result_dict[3]) + len(result_dict[7])))
    report.append("Ptn4: " + str(len(result_dict[4])))
    report.append("Ptn5: " + str(len(result_dict[5])))
    report.append("SP1: (Newest similarity is 100%) " + str(len(simi_newest_100)))
    report.append("SP2: (Start similarity is 100%) " + str(len(simi_start_100)))
    report.append("SP3: (Oldest similarity significantly diffenert from start similarity) " + str(len(simi_old_start)))
    report.append("SP4: (Function modification is not evenly distributed (when similarity item num more than 4)) " + str(len(function_modification_averaged)))
    report.append("SP5: Max similarity - Min similarity >= " + str(similarity_changed_threshold) + " (when similarity item num more than 4) " + str(len(max_min_High)))
    report.append("--------------------")
    report.append("------Ptn1 List-----")
    report.append(result_dict[1])
    report.append("--------------------")
    report.append("------Ptn2 List-----")
    report.append(result_dict[2] + result_dict[6])
    report.append("--------------------")
    report.append("------Ptn3 List-----")
    report.append(result_dict[3] + result_dict[7])
    report.append("--------------------")
    report.append("------Ptn4 List-----")
    report.append(result_dict[4])
    report.append("--------------------")
    report.append("------Ptn5 List-----")
    report.append(result_dict[5])
    report.append("--------------------")
    report.append("------SP1 List-----")
    report.append(simi_newest_100)
    report.append("--------------------")
    report.append("------SP2 List-----")
    report.append(simi_start_100)
    report.append("--------------------")
    report.append("------SP3 List-----")
    report.append(simi_old_start)
    report.append("--------------------")
    report.append("------SP4 List-----")
    report.append(function_modification_averaged)
    report.append("--------------------")
    report.append("------SP5 List-----")
    report.append(max_min_High)
    
    with open(sys.path[0] + "/reports/" + taskId + "-" + detectionId + "/patternClassified_" + str(similarity_changed_threshold) + ".txt", "w") as f:
        for line in report:
            print(line)
            f.write(str(line) + "\n")


    
    
    
    
    # print(sys.path[0])