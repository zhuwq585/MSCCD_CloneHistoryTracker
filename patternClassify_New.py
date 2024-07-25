# This version uses only Jaccard similarity

import sys, os, ujson


# a function that find all folder in the current folder that named by taskId-detectionId and return a list of cloneIndex
# def getCloneIndexList(taskId, detectionId):
#     res = []
#     for cloneIndex in os.listdir(sys.path[0] + "/reports/"):
#         if cloneIndex.startswith(taskId + "-" + detectionId + "-"):
#             res.append(cloneIndex.split("-")[-1])
#     return res

# a function that find the folder in the current folder that named by taskId-detectionId, and return a list of subfolder name in that folder
def getCloneIndexList(taskId, detectionId, cloneOrigin):
    res = []
    
    fld  = sys.path[0] + "/reports/" + taskId + "-" + detectionId + "_" + cloneOrigin
    if not os.path.exists(fld):
        fld = sys.path[0] + "/reports/" + taskId + "-" + detectionId
    
    for subFolder in os.listdir(fld):
        if os.path.isdir(fld + "/" + subFolder):
            res.append(subFolder)
    return res


def patternClassify(cloneIndex, cloneOrigin):
    # read the result file
    fld = sys.path[0] + "/reports/" + taskId + "-" + detectionId + "_" + cloneOrigin
    if not os.path.exists(fld):
        fld = sys.path[0] + "/reports/" + taskId + "-" + detectionId
    trackerResultSource = fld + "/" + str(cloneIndex) + "/result.json"
    try:
        tarckerResult = ujson.loads(open(trackerResultSource,"r").read())
    except Exception:
        return -1
    
    
    similarityTypeIndex = 0
       
    res = 0
    
    ##### Bit difinition (new)
    # bit 1 - 2: modification situation: 00: no modification, 11:modification in both side, 01 or 10: modification in single side
    # bit 3 - 4: similarity change situation (From Start Commit): 00: no result, 11: similarity not changed sighificantly, 01: similarity increased, 10: similarity decreased
    
    if len(tarckerResult['similarityList']) < 1:
        return -1
    

    similarity_newest = tarckerResult['similarityList'][-1]['similarity'][similarityTypeIndex]    
    similarity_start = 0
    startIndex = 0
    for index in range(0, tarckerResult['negative_search_num'] + 1):
        if tarckerResult['similarityList'][index]['similarity'][similarityTypeIndex] > similarity_start:
            similarity_start = tarckerResult['similarityList'][index]['similarity'][similarityTypeIndex]
            startIndex = index
    
    similarity_max = 0
    for item in tarckerResult['similarityList']:
        if item['similarity'][similarityTypeIndex] > similarity_max:
            similarity_max = item['similarity'][similarityTypeIndex]
            
    if similarity_max < 0.7:
        return -2
    
    similarityValueSet = set()
    count = 0
    for index in range(startIndex, len(tarckerResult['similarityList'])):
        v = tarckerResult['similarityList'][index]['similarity'][similarityTypeIndex]
        # 保留两位小数
        v = round(v,2)
        similarityValueSet.add(v)
        count += 1
        
    # if len(similarityValueSet) == 1 and count > 1:
    #     return -3
    

    # get reasonSegmentSet 
    seg1CommitSet = set()
    seg2CommitSet = set()
    for item in tarckerResult['similarityList']:
        seg1CommitSet.add(item['segment1']['commitId'])
        seg2CommitSet.add(item['segment2']['commitId'])

    # bit1 - bit2
    if len(tarckerResult['similarityList']) == 1:
        res = res | 0
    else:
        if len(seg1CommitSet) > 1 and len(seg2CommitSet) > 1:
            res = res | 3
        else:
            res = res | 1

    # bit3 - bit4
    if similarity_newest - similarity_start >= similarity_changed_threshold:
        res = res | 4
    elif similarity_start - similarity_newest >= similarity_changed_threshold:
        res = res | 8
    else:
        res = res | 12

        
    return res
    

if __name__ == "__main__":
    # parameter: taskId, detectionId
    # taskId                       = sys.argv[1]
    # detectionId                  = sys.argv[2]
    # similarity_changed_threshold = float(sys.argv[3])
    # cloneOrigin                  = sys.argv[4] # file or func
    
    # test
    taskId = "20003"
    detectionId = "2"
    similarity_changed_threshold = 0.1
    cloneOrigin = "file"
    
    if not cloneOrigin in {"file","func"}:
        print("Invalid cloneOrigin")
        sys.exit(1)
    
    
        
    # result arrays
    
    # result_dict = { }
    # simi_newest_100 = []
    # simi_start_100 = []
    # simi_old_start = []
    # function_modification_averaged = []
    # max_min_High = []
    
    indexes_noModification = []
    
    indexes_consistantChange                        = []
    indexes_inconsistantChange_similarityIncreased  = []
    indexes_inconsistantChange_similarityDecreased  = []
    indexes_inconsistantChange_similarityNotChanged = []
    indexes_max_oldest = []
    
    indexes_err_NoSimilarity = []
    indexes_err_LowSimilarity = []
    indexes_err_SimilarityNotChanged = []
    
    cloneIndexes = getCloneIndexList(taskId, detectionId, cloneOrigin)
    print("all num" + str(len(cloneIndexes)))
    
    for cloneIndex in cloneIndexes:

        cloneIndex = int(cloneIndex)

        res = patternClassify(cloneIndex, cloneOrigin) 
        
        
            
        ##### Bit difinition (new)
        # bit 1 - 2: modification situation: 00: no modification, 11:modification in both side, 01 or 10: modification in single side
        # bit 3 - 4: similarity change situation (From Start Commit): 00: no result, 11: similarity not changed sighificantly, 01: similarity increased, 10: similarity decreased
        
        if res == -1:
            indexes_err_NoSimilarity.append(cloneIndex)
        elif res == -2:
            indexes_err_LowSimilarity.append(cloneIndex)
        elif res == -3:
            indexes_err_SimilarityNotChanged.append(cloneIndex)
        else:
        
            if res in {0,4,8,12}:
                indexes_noModification.append(cloneIndex)
            
            # get inconsistance pairs
            elif res == 15:
                    indexes_consistantChange.append(cloneIndex)
            
            # get inconsistance pairs
            elif res in {11, 9}:
                indexes_inconsistantChange_similarityDecreased.append(cloneIndex)
            elif res in {7, 5}:
                indexes_inconsistantChange_similarityIncreased.append(cloneIndex)
            elif res == 13:
                indexes_inconsistantChange_similarityNotChanged.append(cloneIndex)
            

        

            


   
   
    pass     


    report = []
    report.append("No modification: " + str(len(indexes_noModification)))
    report.append("Consistant change: " + str(len(indexes_consistantChange)))
    report.append("Inconsistant change (similarity increased): " + str(len(indexes_inconsistantChange_similarityIncreased)))
    report.append("Inconsistant change (similarity decreased): " + str(len(indexes_inconsistantChange_similarityDecreased)))
    report.append("Inconsistant change (similarity not changed): " + str(len(indexes_inconsistantChange_similarityNotChanged)))
    report.append("Error: No Similarity: " + str(len(indexes_err_NoSimilarity)))
    report.append("Error: Low Similarity: " + str(len(indexes_err_LowSimilarity)))
    report.append("Error: Similarity Not Changed: " + str(len(indexes_err_SimilarityNotChanged)))
    report.append("")
    report.append("No modification List")
    report.append(indexes_noModification)
    report.append("")
    report.append("Consistant change List")
    report.append(indexes_consistantChange)
    report.append("")
    report.append("Inconsistant change (similarity increased) List")
    report.append(indexes_inconsistantChange_similarityIncreased)
    report.append("")
    report.append("Inconsistant change (similarity decreased) List")
    report.append(indexes_inconsistantChange_similarityDecreased)
    report.append("")
    report.append("Inconsistant change (similarity not changed) List")
    report.append(indexes_inconsistantChange_similarityNotChanged)
    report.append("Error: No Similarity List")
    report.append(indexes_err_NoSimilarity)
    report.append("Error: Low Similarity List")
    report.append(indexes_err_LowSimilarity)
    report.append("Error: Similarity Not Changed List")
    report.append(indexes_err_SimilarityNotChanged)
    
    
    
    # with open(sys.path[0] + "/reports/" + taskId + "-" + detectionId + "/patternClassified_" + str(similarity_changed_threshold) + ".txt", "w") as f:
    for line in report:
        print(line)
            # f.write(str(line) + "\n")
