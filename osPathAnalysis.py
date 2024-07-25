from MSCCDTaskData import *
import ujson


###CONFIG
keyset_test = {"test"}
keyset_driver = {"drivers","driver","arch","boards","board","misc","soc","chip"}
keyset_kernel = {"kernel","rtos"}
keyset_component = {"lib","library","libraries","share","modules","component","subsys","connectivity","storage"}


def checkPath(path):
    pathSplit = path.split("/")[6:-1]
    for index in range(len(pathSplit)):
        pathSplit[index] = pathSplit[index].lower()

    for item in pathSplit:
        for keyword in keyset_test:
            if keyword in item:
                return 0
    
    for item in pathSplit:
        for keyword in keyset_driver:
            if keyword in item:
                return 1
            
    
    for item in pathSplit:
        for keyword in keyset_kernel:
            if keyword in item:
                return 2

    for item in pathSplit:
        for keyword in keyset_component:
            if keyword in item:
                return 3
    return 4
    
    

if __name__ == "__main__":
    taskId = "20021"
    detectionId = "11"
    
    cloneList = cloneListGeneration(taskId,detectionId)
    fileList = fileListGeneration(taskId)
    
    resDict = {}
    
    for cloneindex in  range(len(cloneList)):
        cloneItem = cloneList[cloneindex]
        path1 = fileList[cloneItem[0][0]][cloneItem[0][1]]
        path2 = fileList[cloneItem[1][0]][cloneItem[1][1]]
        
        res1 = checkPath(path1)
        res2 = checkPath(path2)
        
        if res1 > res2:
            tmp = res2
            res2 = res1
            res1 = tmp
        
        if not res1 in resDict:
            resDict[res1] = {}
        
        if not res2 in resDict[res1]:
            resDict[res1][res2] = {
                "sum" : 0,
                "indexes" : []
            }
        
        resDict[res1][res2]['sum'] += 1
        resDict[res1][res2]['indexes'].append(cloneindex)
        
    sum = 0
    for index1 in resDict:
        for index2 in resDict[index1]:
           sum += resDict[index1][index2]['sum']
           
    for index1 in resDict:
        for index2 in resDict[index1]:
           print(str(index1) + "-" + str(index2) + ":")
           print("sum: " + str(resDict[index1][index2]['sum']))
           print("divi: " + str(resDict[index1][index2]['sum'] / sum))
    
    open("filePathAnalysisRes.json","w").write(ujson.dumps(resDict,indent=2))