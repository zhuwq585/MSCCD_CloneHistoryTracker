# ctags --fields=+n --fields=+e --output-format=json ctagsTest/TokenBag.java

import sys,os,ujson
import time

FunctionItemNameSet = {'method','function',"func"}

def getFunctionName(path, startLine, endLine):
    cmd = "ctags --fields=+n --fields=+e --output-format=json " + path
    
    res = os.popen(cmd).readlines()
    for ctagItemLine in res:
        ctagItem = ujson.loads(ctagItemLine)
        if (ctagItem['line'] == startLine or ctagItem['line'] - 1 == startLine) and ctagItem['end'] == endLine and ctagItem['kind'] in FunctionItemNameSet:
            return ctagItem['name']
        
    return None
    
# get function position in the file by function name
def getFunctionPosition(path, functionName):
    cmd = "ctags --fields=+n --fields=+e --output-format=json " + path
    if not os.path.exists(path):
        # wait 1 second and try again
        time.sleep(1)
    
    if os.path.exists(path):
        res = os.popen(cmd).readlines()
        for ctagItemLine in res:
            ctagItem = ujson.loads(ctagItemLine)
            if ctagItem['name'] == functionName and ctagItem['kind'] in FunctionItemNameSet:
                return ctagItem['line'], ctagItem['end']
        return None,None
    else:
        print("Error(getFunctionPosition): file not found: " + path)
        return None