# ctags --fields=+n --fields=+e --output-format=json ctagsTest/TokenBag.java

import sys,os,ujson
import time
import clang.cindex
import re

FunctionItemNameSet = {'method','function',"func"}

def JavaPatternGeneration(str):
    
    pattern = re.split(r'[,\s]+', str.split("(")[1].split(")")[0])[0::2]
    res = "::".join(pattern)
    if len(res) == 0:
        res = "--"
    return res

def getFunctionName_Ptn(path, startLine, endLine, language):
    if language in {"Java", "Go", "C"}:
        return getFunctionName_Ptn_CTAG(path, startLine, endLine, language)
    elif language == "JavaScript":
        return getFunctionName_Ptn_JavaScript(path, startLine, endLine)
    elif language == "C++":
        return getFunctionName_Ptn_Cpp(path, startLine, endLine)


def getFunctionName_Ptn_Cpp(path, startLine, endLine):
    clang.cindex.Config.set_library_path("/opt/homebrew/opt/llvm/lib")
    index = clang.cindex.Index.create()
    translation_unit = index.parse(path)
    for cursor in translation_unit.cursor.walk_preorder():
        if cursor.extent.start.line == startLine and cursor.extent.end.line == endLine and (cursor.kind == clang.cindex.CursorKind.CXX_METHOD or cursor.kind == clang.cindex.CursorKind.FUNCTION_DECL):
            
            file_path_cursor = cursor.extent.start.file.name
            if file_path_cursor != path:
                continue
            
            function_params_type = [p.type.spelling for p in cursor.get_arguments()]
            function_name = cursor.displayname
            if cursor.semantic_parent.kind == clang.cindex.CursorKind.CLASS_DECL:
                class_name = cursor.semantic_parent.displayname
            else:
                class_name = "@NONE@"
            
            pattern = class_name + "@@" + "::".join(function_params_type)
            
            return function_name, pattern

def getFunctionName_Ptn_JavaScript(path, startLine, endLine):
    cmd = "jsctags " + path
    res = os.popen(cmd).read()
    for jsctagItem in ujson.loads(res):
            #    jsctagItem =     {
            #     "id": "e7087d3e-6418-11ee-8a1b-57af52f350c4",
            #     "name": "languages2words",
            #     "addr": "/languages2words/",
            #     "kind": "f",
            #     "type": "void function(string)",
            #     "lineno": 283,
            #     "origin": {
            #       "!span": "8439[282:9]-8454[282:24]",
            #       "!type": "fn(src: string)",
            #       "!data": {
            #         "isConstructor": false,
            #         "type": "Function.prototype"
            #       }
            #     },
            #     "tagfile": "/Users/syu/TestRepos/JavaScript/ioBroker.hue/CTagsTest/gulpfile.js"
            #   }
        startLine_jsctag = jsctagItem['lineno']
        endLine_jsctag = jsctagItem['origin']['!span'].split("-")[1].split("[")[1].split(":")[0]
        if startLine_jsctag == startLine and endLine_jsctag == endLine and jsctagItem['kind'] == "f":
            return jsctagItem['name'], jsctagItem['origin']['type']
        


def getFunctionName_Ptn_CTAG(path, startLine, endLine, language):
    cmd = "ctags --fields=+ne --output-format=json " + path
    
    res = os.popen(cmd).readlines()
    for ctagItemLine in res:
        ctagItem = ujson.loads(ctagItemLine)
        if (ctagItem['line'] == startLine or ctagItem['line'] - 1 == startLine) and ctagItem['end'] == endLine and ctagItem['kind'] in FunctionItemNameSet:
            
            # if language == "Java":
            #     return ctagItem['name'],JavaPatternGeneration(ctagItem['pattern'])
            
            return ctagItem['name'], ctagItem['pattern']
        
    return None


# get function position in the file by function name and pattern




def getFunctionPosition_JavaScript(path, functionName, patternString):
    cmd = "jsctags " + path
    if not os.path.exists(path):
        # wait 1 second and try again
        time.sleep(1)
    
    if os.path.exists(path):
        res = os.popen(cmd).read()
        for jsctagItem in ujson.loads(res):
            if jsctagItem['name'] == functionName and jsctagItem['origin']['type'] == patternString and jsctagItem['kind'] == "f":
                return jsctagItem['lineno'], jsctagItem['origin']['!span'].split("-")[1].split("[")[1].split(":")[0]   
        
        print("Cannot find function: " + functionName + " in file: " + path)
        if input("Do you want to continue to input line number manually? (y/n)") != "n":
            startLine = input("Please input start line: ")
            endLine = input("Please input end line: ")
            return int(startLine), int(endLine)
        return None,None 


def getFunctionPosition_CTag(path, functionName, patternString, language):

    cmd = "ctags --fields=+ne --output-format=json " + path
    if not os.path.exists(path):
        # wait 1 second and try again
        time.sleep(1)
    
    if os.path.exists(path):
        res = os.popen(cmd).readlines()
        for ctagItemLine in res:
            
            ctagItem = ujson.loads(ctagItemLine)
            
            # if language == "Java":
            #     cTagPattern = JavaPatternGeneration(ctagItem['pattern'])
            # else:
            cTagPattern = ctagItem['pattern']
                
            # if ctagItem['name'] == functionName and ctagItem['kind'] in FunctionItemNameSet and cTagPattern == patternString:
            if ctagItem['name'] == functionName and ctagItem['kind'] in FunctionItemNameSet:
                return ctagItem['line'], ctagItem['end']
        
        # an example that code provided by capilot is buggy
        # print("Cannot find function: " + functionName + " in file: " + path")
        
        print("Cannot find function: " + functionName + " in file: " + path)
        if input("Do you want to continue to input line number manually? (y/n)") != "n":
            startLine = input("Please input start line: ")
            endLine = input("Please input end line: ")
            return int(startLine), int(endLine)
        return None,None
    
    else:
        print("Error(getFunctionPosition): file not found: " + path)
        return None

def getFunctionPosition_Cpp(path, functionName, patternString):
    if not os.path.exists(path):
        # wait 1 second and try again
        time.sleep(1)
    
    if os.path.exists(path):
        clang.cindex.Config.set_library_path("/opt/homebrew/opt/llvm/lib")
        index = clang.cindex.Index.create()
        translation_unit = index.parse(path)
        for cursor in translation_unit.cursor.walk_preorder():
            if cursor.kind == clang.cindex.CursorKind.CXX_METHOD or cursor.kind == clang.cindex.CursorKind.FUNCTION_DECL:
                
                file_path_cursor = cursor.extent.start.file.name
                if file_path_cursor != path:
                    continue
                
                function_params_type = [p.type.spelling for p in cursor.get_arguments()]
                function_name = cursor.displayname
                if cursor.semantic_parent.kind == clang.cindex.CursorKind.CLASS_DECL:
                    class_name = cursor.semantic_parent.displayname
                else:
                    class_name = "@NONE@"
                
                pattern = class_name + "@@" + "::".join(function_params_type)
                
                if function_name == functionName and pattern == patternString:
                    return cursor.extent.start.line, cursor.extent.end.line
        
        print("Cannot find function: " + functionName + " in file: " + path)
        if input("Do you want to continue to input line number manually? (y/n)") != "n":
            startLine = input("Please input start line: ")
            endLine = input("Please input end line: ")
            return int(startLine), int(endLine)
        return None,None
    
    else:
        print("Error(getFunctionPosition): file not found: " + path)
        return None
def getFunctionPosition(path, functionName, patternString, language):
    if language in {"Java", "Go", "C"}:
        return getFunctionPosition_CTag(path, functionName, patternString, language)
    elif language == "JavaScript":
        return getFunctionPosition_JavaScript(path, functionName, patternString)
    elif language == "C++":
        return getFunctionPosition_Cpp(path, functionName, patternString)
