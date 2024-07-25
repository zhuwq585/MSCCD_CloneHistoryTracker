import sys, ujson
import file2cloneDictGeneration
import MSCCDTaskData

# taskId = sys.argv[1]
# detectionId = sys.argv[2]
# similarityThreshold = sys.argv[3]
taskId = "20021"
detectionId = "11"
similarityThreshold = "0.05"

cloneList = MSCCDTaskData.cloneListGeneration(taskId, detectionId)
fileList,singleId2DoubleId,cloneDict_file = file2cloneDictGeneration.main(taskId, detectionId)

patternDictFile = "/Users/syu/workspace/MSCCD_CloneHistoryTracker/reports/" + taskId + "-" + detectionId + "/patternClassified_" + str(similarityThreshold) + ".json"
patternDict = ujson.load(open(patternDictFile))

pathAnalysisDict = ujson.loads(open("/Users/syu/workspace/MSCCD_CloneHistoryTracker/filePathAnalysisRes.json").read())

for patternKey in patternDict:
    if isinstance(patternDict[patternKey], list):
        patternDict[patternKey] = set(patternDict[patternKey])

for patternKey1 in pathAnalysisDict:
    for patternKey2 in pathAnalysisDict[patternKey1]:
        if isinstance(pathAnalysisDict[patternKey1][patternKey2]['indexes'], list):
            pathAnalysisDict[patternKey1][patternKey2]['indexes'] = set(pathAnalysisDict[patternKey1][patternKey2]['indexes'])
            
            
           
# res = pathAnalysisDict['3']['3']['indexes'].intersection(patternDict['1'])
# print(str(res))
# res = pathAnalysisDict['3']['3']['indexes'].intersection(patternDict['2'])
# print(str(res))
# res = pathAnalysisDict['3']['3']['indexes'].intersection(patternDict['3'])
# print(str(res))
# res = pathAnalysisDict['3']['3']['indexes'].intersection(patternDict['4'])
# print(str(res))
# res = pathAnalysisDict['3']['3']['indexes'].intersection(patternDict['5'])
# print(str(res))
# res = pathAnalysisDict['3']['3']['indexes'].intersection(patternDict['6'])
# print(str(res))
res = pathAnalysisDict['3']['3']['indexes'].intersection(patternDict['9'])
print(len(res))
print(str(res))
# res = pathAnalysisDict['3']['3']['indexes'].intersection(patternDict['8'])
# print(str(res))
# res = pathAnalysisDict['3']['3']['indexes'].intersection(patternDict['9'])
# print(str(res))
