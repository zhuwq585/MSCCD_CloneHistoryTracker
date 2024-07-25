# This version uses both Jaccard and Lcs similarity to classify the pattern

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


def patternClassify(cloneIndex, cloneOrigin, similarityType):
    # read the result file
    fld = sys.path[0] + "/reports/" + taskId + "-" + detectionId + "_" + cloneOrigin
    if not os.path.exists(fld):
        fld = sys.path[0] + "/reports/" + taskId + "-" + detectionId
    trackerResultSource = fld + "/" + str(cloneIndex) + "/result.json"
    try:
        tarckerResult = ujson.loads(open(trackerResultSource,"r").read())
    except Exception:
        return -1
    
    
    similarityTypeIndex = None
    if similarityType == "Jaccard":
        similarityTypeIndex = 0
    elif similarityType == "Lcs":
        similarityTypeIndex = 1
    
    res = 0
    ##### Bit difinition (new)
    # bit 1 - 2: modification situation: 00: no modification, 11:modification in both side, 01 or 10: modification in single side
    # bit 3 - 4: similarity change situation (From Start Commit): 00: no result, 11: similarity not changed sighificantly, 01: similarity increased, 10: similarity decreased
    # bit 5 - 6: similarity change situation (From Oldest Commit): 00: no result, 11: similarity not changed sighificantly, 01: similarity increased, 10: similarity decreased
    # bit 7: if oldest similarity != start similarity  =>  1
    
         

    
    if len(tarckerResult['similarityList']) < 1:
        return -1
    
    similarity_oldest = tarckerResult['similarityList'][0]['similarity'][similarityTypeIndex]
    similarity_start  = tarckerResult['similarityList'][0 + tarckerResult['negative_search_num']]['similarity'][similarityTypeIndex]
    similarity_newest = tarckerResult['similarityList'][-1]['similarity'][similarityTypeIndex]
    similarity_max = 0
    similarity_min = 1
    
    # get max and min similarity
    cursor  = 0
    while cursor < len(tarckerResult['similarityList']):
        if tarckerResult['similarityList'][cursor]['similarity'][similarityTypeIndex] > similarity_max:
            similarity_max = tarckerResult['similarityList'][cursor]['similarity'][similarityTypeIndex]
        if tarckerResult['similarityList'][cursor]['similarity'][similarityTypeIndex] < similarity_min:
            similarity_min = tarckerResult['similarityList'][cursor]['similarity'][similarityTypeIndex]
        cursor += 1

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
            res = res | 2
        else:
            res = res | 1

    # bit3 - bit4
    if similarity_newest - similarity_start >= similarity_changed_threshold:
        res = res | 4
    elif similarity_start - similarity_newest >= similarity_changed_threshold:
        res = res | 8
    else:
        res = res | 12
        
    # bit5 - bit6
    if similarity_newest - similarity_oldest >= similarity_changed_threshold:
        res = res | 16
    elif similarity_oldest - similarity_newest >= similarity_changed_threshold:
        res = res | 32
    else:
        res = res | 48
    
    
    # bit7
    if similarity_oldest != similarity_start:
        res = res | 64
        
    return res
    

if __name__ == "__main__":
    # parameter: taskId, detectionId
    taskId                       = sys.argv[1]
    detectionId                  = sys.argv[2]
    similarity_changed_threshold = float(sys.argv[3])
    cloneOrigin                  = sys.argv[4] # file or func
    
    # test
    # taskId = "20021"
    # detectionId = "2"
    # similarity_changed_threshold = 0.10
    # cloneOrigin = "file"
    
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
    
    indexes_consistantChange_fromStart                        = {"Jac":[],"Lcs":[]}
    indexes_inconsistantChange_similarityIncreased_fromStart  = {"Jac":[],"Lcs":[]}
    indexes_inconsistantChange_similarityDecreased_fromStart  = {"Jac":[],"Lcs":[]}
    indexes_inconsistantChange_similarityNotChanged_fromStart = {"Jac":[],"Lcs":[]}
    
    indexes_consistantChange_fromOldest                        = {"Jac":[],"Lcs":[]}
    indexes_inconsistantChange_similarityIncreased_fromOldest  = {"Jac":[],"Lcs":[]}
    indexes_inconsistantChange_similarityDecreased_fromOldest  = {"Jac":[],"Lcs":[]}
    indexes_inconsistantChange_similarityNotChanged_fromOldest = {"Jac":[],"Lcs":[]}
    
    indexes_max_oldest = {"Jac":[],"Lcs":[]}
    
    indexes_simiJac_simiLcs = []
    
    cloneIndexes = getCloneIndexList(taskId, detectionId, cloneOrigin)
    
    print("all num" + str(len(cloneIndexes)))
    
    for cloneIndex in cloneIndexes:

        cloneIndex = int(cloneIndex)

        resJac = patternClassify(cloneIndex, cloneOrigin, "Jaccard") 
        resLcs = patternClassify(cloneIndex, cloneOrigin, "Lcs")    
        
        ifDif = False
        if resJac != resLcs:   
            indexes_simiJac_simiLcs.append(cloneIndex)
            ifDif = True
        
        if resJac == -1 or resLcs == -1:
            print("Error: similarity_newest < 0.6 in cloneIndex or no similarity item " + str(cloneIndex))
            continue
        
        if resJac & 0 == 0 or resLcs & 0 == 0:
            indexes_noModification.append(cloneIndex)
        
        
        # get inconsistance pairs
        if resJac & 3 == 3:
            if resJac & 12 == 12:
                indexes_consistantChange_fromStart["Jac"].append(cloneIndex)
            if resJac & 48 == 48:
                indexes_consistantChange_fromOldest["Jac"].append(cloneIndex)
        
        if resLcs & 3 == 3:
            if resLcs & 12 == 12:
                indexes_consistantChange_fromStart["Lcs"].append(cloneIndex)
            if resLcs & 48 == 48:
                indexes_consistantChange_fromOldest["Lcs"].append(cloneIndex)
        
        
            
        if resJac & 2 == 2 or resJac & 1 == 1:
            if resJac & 4 == 4:
                indexes_inconsistantChange_similarityIncreased_fromStart["Jac"].append(cloneIndex)
            elif resJac & 8 == 8:
                indexes_inconsistantChange_similarityDecreased_fromStart["Jac"].append(cloneIndex)
            elif resJac & 12 == 12:
                indexes_inconsistantChange_similarityNotChanged_fromStart["Jac"].append(cloneIndex)
                
            if resJac & 16 == 16:
                indexes_inconsistantChange_similarityIncreased_fromOldest["Jac"].append(cloneIndex)
            elif resJac & 32 == 32:
                indexes_inconsistantChange_similarityDecreased_fromOldest["Jac"].append(cloneIndex)
            elif resJac & 48 == 48:
                indexes_inconsistantChange_similarityNotChanged_fromOldest["Jac"].append(cloneIndex)
                
        
        if resLcs & 2 == 2 or resLcs & 1 == 1:
            if resLcs & 4 == 4:
                indexes_inconsistantChange_similarityIncreased_fromStart["Lcs"].append(cloneIndex)
            elif resLcs & 8 == 8:
                indexes_inconsistantChange_similarityDecreased_fromStart["Lcs"].append(cloneIndex)
            elif resLcs & 12 == 12:
                indexes_inconsistantChange_similarityNotChanged_fromStart["Lcs"].append(cloneIndex)
        
            if resLcs & 16 == 16:
                indexes_inconsistantChange_similarityIncreased_fromOldest["Lcs"].append(cloneIndex)
            elif resLcs & 32 == 32:
                indexes_inconsistantChange_similarityDecreased_fromOldest["Lcs"].append(cloneIndex)
            elif resLcs & 48 == 48:
                indexes_inconsistantChange_similarityNotChanged_fromOldest["Lcs"].append(cloneIndex)
        
        if resJac & 64 == 64:
            indexes_max_oldest["Jac"].append(cloneIndex)
        if resLcs & 64 == 64:
            indexes_max_oldest["Lcs"].append(cloneIndex)
    
   
   
    pass     

    report = []
    report.append("No modification: " + str(len(indexes_noModification)))
    report.append("Consistant change: " + str(len(indexes_consistantChange_fromStart["Jac"]) + len(indexes_consistantChange_fromStart["Lcs"])))
    report.append("Inconsistant change (similarity increased): " + str(len(indexes_inconsistantChange_similarityIncreased_fromStart["Jac"]) + len(indexes_inconsistantChange_similarityIncreased_fromStart["Lcs"])))
    report.append("Inconsistant change (similarity decreased): " + str(len(indexes_inconsistantChange_similarityDecreased_fromStart["Jac"]) + len(indexes_inconsistantChange_similarityDecreased_fromStart["Lcs"])))
    report.append("Inconsistant change (similarity not changed): " + str(len(indexes_inconsistantChange_similarityNotChanged_fromStart["Jac"]) + len(indexes_inconsistantChange_similarityNotChanged_fromStart["Lcs"])))
    report.append("Consistant change (from oldest): " + str(len(indexes_consistantChange_fromOldest["Jac"]) + len(indexes_consistantChange_fromOldest["Lcs"])))
    report.append("Inconsistant change (similarity increased) (from oldest): " + str(len(indexes_inconsistantChange_similarityIncreased_fromOldest["Jac"]) + len(indexes_inconsistantChange_similarityIncreased_fromOldest["Lcs"])))
    report.append("Inconsistant change (similarity decreased) (from oldest): " + str(len(indexes_inconsistantChange_similarityDecreased_fromOldest["Jac"]) + len(indexes_inconsistantChange_similarityDecreased_fromOldest["Lcs"])))
    report.append("Inconsistant change (similarity not changed) (from oldest): " + str(len(indexes_inconsistantChange_similarityNotChanged_fromOldest["Jac"]) + len(indexes_inconsistantChange_similarityNotChanged_fromOldest["Lcs"])))
    report.append("")
    
                  
                  
#     report = []
#     report.append("No modification: " + str(len(indexes_noModification)))
#     report.append("Consistant change: " + str(len(indexes_consistantChange_fromStart)))
#     report.append("Inconsistant change (similarity increased): " + str(len(indexes_inconsistantChange_similarityIncreased_fromStart)))
#     report.append("Inconsistant change (similarity decreased): " + str(len(indexes_inconsistantChange_similarityDecreased_fromStart)))
#     report.append("Inconsistant change (similarity not changed): " + str(len(indexes_inconsistantChange_similarityNotChanged_fromStart)))
#     report.append("Consistant change (from oldest): " + str(len(indexes_consistantChange_fromOldest)))
#     report.append("Inconsistant change (similarity increased) (from oldest): " + str(len(indexes_inconsistantChange_similarityIncreased_fromOldest)))
#     report.append("Inconsistant change (similarity decreased) (from oldest): " + str(len(indexes_inconsistantChange_similarityDecreased_fromOldest)))
#     report.append("Inconsistant change (similarity not changed) (from oldest): " + str(len(indexes_inconsistantChange_similarityNotChanged_fromOldest)))
#     report.append("")
    
#     report.append("--------------------")
#     report.append("------No modification List-----")
#     report.append(indexes_noModification)
#     report.append("--------------------")
#     report.append("------Consistant change List-----")
#     report.append(indexes_consistantChange_fromStart)
#     report.append("--------------------")
#     report.append("------Inconsistant change (similarity increased) List-----")
#     report.append(indexes_inconsistantChange_similarityIncreased_fromStart)
#     report.append("--------------------")
#     report.append("------Inconsistant change (similarity decreased) List-----")
#     report.append(indexes_inconsistantChange_similarityDecreased_fromStart)
#     report.append("--------------------")
#     report.append("------Inconsistant change (similarity not changed) List-----")
#     report.append(indexes_inconsistantChange_similarityNotChanged_fromStart)
#     report.append("--------------------")
#     report.append("------Consistant change (from oldest) List-----")
#     report.append(indexes_consistantChange_fromOldest)
#     report.append("--------------------")
#     report.append("------Inconsistant change (similarity increased) (from oldest) List-----")
#     report.append(indexes_inconsistantChange_similarityIncreased_fromOldest)
#     report.append("--------------------")
#     report.append("------Inconsistant change (similarity decreased) (from oldest) List-----")
#     report.append(indexes_inconsistantChange_similarityDecreased_fromOldest)
#     report.append("--------------------")
#     report.append("------Inconsistant change (similarity not changed) (from oldest) List-----")
#     report.append(indexes_inconsistantChange_similarityNotChanged_fromOldest)
    
#     resJsonObj = {
#         "1" : indexes_noModification,
#         "2" : indexes_consistantChange_fromStart,
#         "3" : indexes_inconsistantChange_similarityIncreased_fromStart,
#         "4" : indexes_inconsistantChange_similarityDecreased_fromStart,
#         "5" : indexes_inconsistantChange_similarityNotChanged_fromStart,
#         "6" : indexes_consistantChange_fromOldest,
#         "7" : indexes_inconsistantChange_similarityIncreased_fromOldest,
#         "8" : indexes_inconsistantChange_similarityDecreased_fromOldest,
#         "9" : indexes_inconsistantChange_similarityNotChanged_fromOldest,
#         "memo": "Ptn1: No modification; Ptn2: Consistant change; Ptn3: Inconsistant change (similarity increased); Ptn4: Inconsistant change (similarity decreased); Ptn5: Inconsistant change (similarity not changed); Ptn6: Consistant change (from oldest); Ptn7: Inconsistant change (similarity increased) (from oldest); Ptn8: Inconsistant change (similarity decreased) (from oldest); Ptn9: Inconsistant change (similarity not changed) (from oldest)",
#         "threshold": similarity_changed_threshold,
#         "taskId": taskId,
#         "detectionId": detectionId
#     }
    
#     # report.append("Ptn1: " + str(len(result_dict[1]))) 
#     # report.append("Ptn2: " + str(len(result_dict[2]) + len(result_dict[6])))
#     # report.append("Ptn3: " + str(len(result_dict[3]) + len(result_dict[7])))
#     # report.append("Ptn4: " + str(len(result_dict[4])))
#     # report.append("Ptn5: " + str(len(result_dict[5])))
#     # report.append("SP1: (Newest similarity is 100%) " + str(len(simi_newest_100)))
#     # report.append("SP2: (Start similarity is 100%) " + str(len(simi_start_100)))
#     # report.append("SP3: (Oldest similarity significantly diffenert from start similarity) " + str(len(simi_old_start)))
#     # report.append("SP4: (Function modification is not evenly distributed (when similarity item num more than 4)) " + str(len(function_modification_averaged)))
#     # report.append("SP5: Max similarity - Min similarity >= " + str(similarity_changed_threshold) + " (when similarity item num more than 4) " + str(len(max_min_High)))
#     # report.append("--------------------")
#     # report.append("------Ptn1 List-----")
#     # report.append(result_dict[1])
#     # report.append("--------------------")
#     # report.append("------Ptn2 List-----")
#     # report.append(result_dict[2] + result_dict[6])
#     # report.append("--------------------")
#     # report.append("------Ptn3 List-----")
#     # report.append(result_dict[3] + result_dict[7])
#     # report.append("--------------------")
#     # report.append("------Ptn4 List-----")
#     # report.append(result_dict[4])
#     # report.append("--------------------")
#     # report.append("------Ptn5 List-----")
#     # report.append(result_dict[5])
#     # report.append("--------------------")
#     # report.append("------SP1 List-----")
#     # report.append(simi_newest_100)
#     # report.append("--------------------")
#     # report.append("------SP2 List-----")
#     # report.append(simi_start_100)
#     # report.append("--------------------")
#     # report.append("------SP3 List-----")
#     # report.append(simi_old_start)
#     # report.append("--------------------")
#     # report.append("------SP4 List-----")
#     # report.append(function_modification_averaged)
#     # report.append("--------------------")
#     # report.append("------SP5 List-----")
#     # report.append(max_min_High)
    
    # with open(sys.path[0] + "/reports/" + taskId + "-" + detectionId + "/patternClassified_" + str(similarity_changed_threshold) + ".txt", "w") as f:
    for line in report:
        print(line)
            # f.write(str(line) + "\n")


    
#     with open(sys.path[0] + "/reports/" + taskId + "-" + detectionId + "/patternClassified_" + str(similarity_changed_threshold) + ".json", "w") as f:    
#         f.write(ujson.dumps(resJsonObj))
#     # print(sys.path[0])
    
    
    
    
    
    



#  # ### Bit difinition of res
#     # bit 1: if modification exists
#     # bit 2: if modification exist in both side
#     # bit 3: if similarity changed siginificantly (larger that the threshold)
#     # bit 4: if similarity increased 
#     # bit 5: oldest similarity == start similarity?
#     # bit 6: max similarity == 100%
#     # bit 7: newest similarity == 100%
#     # bit 8: oldest similarity == 100%
#     # bit 9: start similarity == 100%
#     # bit 10: if similarity changed siginificantly (larger that the threshold) (from oldest)
#     # bit 11: if similarity increased (from oldest)

#     # # # bit 1
#     # # if len(tarckerResult['similarityList']) > 1:
#     # #     res = res | 1
#     # # # bit 2
#     # # if len(seg1CommitSet) > 1 and len(seg2CommitSet) > 1:
#     # #     res = res | 2
    
#     # # bit 3 changed -> 1  no change -> 0
#     # if abs(similarity_newest - similarity_start) >= similarity_changed_threshold:
#     #     res = res | 4
#     # # bit 4 increased -> 1  decreased -> 0 and bit 3 is 1
#     # if similarity_newest - similarity_start >= similarity_changed_threshold:
#     #     res = res | 8
#     # # bit 5
#     # if abs(similarity_oldest - similarity_start) < similarity_changed_threshold :
#     #     res = res | 16
#     # # bit 6
#     # if similarity_max == 1:
#     #     res = res | 32
#     # # bit 7
#     # if similarity_newest == 1:
#     #     res = res | 64
#     # # bit 8
#     # if similarity_oldest == 1:
#     #     res = res | 128
#     # # bit 9
#     # if similarity_start == 1:
#     #     res = res | 256
    
#     # # bit 10
#     # if abs(similarity_newest - similarity_oldest) >= similarity_changed_threshold:
#     #     res = res | 512

#     # # bit 11
#     # if similarity_newest - similarity_oldest >= similarity_changed_threshold:
#     #     res = res | 1024