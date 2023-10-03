# ctags --fields=+n --fields=+e --output-format=json ctagsTest/TokenBag.java

import sys,os,ujson

def getFunctionName(path, startLine, endLine):
    cmd = "ctags --fields=+n --fields=+e --output-format=json " + path
    
    res = os.popen(cmd).readlines()
    for ctagItemLine in res:
        ctagItem = ujson.loads(ctagItemLine)
        if (ctagItem['line'] == startLine or ctagItem['line'] - 1 == startLine) and ctagItem['end'] == endLine and (ctagItem['kind'] == 'method' or ctagItem['kind'] == 'function'):
            return ctagItem['name']
        
    return None
    
# get function position in the file by function name
def getFunctionPosition(path, functionName):
    cmd = "ctags --fields=+n --fields=+e --output-format=json " + path
    res = os.popen(cmd).readlines()
    for ctagItemLine in res:
        ctagItem = ujson.loads(ctagItemLine)
        if ctagItem['name'] == functionName and (ctagItem['kind'] == 'method' or ctagItem['kind'] == 'function'):
            return ctagItem['line'], ctagItem['end']
        
    return None