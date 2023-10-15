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



def getFunctionName_Ptn_JavaScript(path, startLine, endLine):
    # node JSFunctionExtraction.js path
    cmd = "node JSFunctionExtraction.js " + path
    jsFuncItemsSources = os.popen(cmd).readlines()
    
    for line in jsFuncItemsSources:
        jsFuncItem = ujson.loads(line)
        startLine_jsctag = jsFuncItem['startLine']
        endLine_jsctag = jsFuncItem['endLine']
        
        ptn = ""
        for param in jsFuncItem['params']:
            ptn += param['type'] + "@@"
        if len(ptn) == 0:
            ptn = "--"
        
        if startLine_jsctag == startLine and endLine_jsctag == endLine:
            res = (jsFuncItem['name'], ptn)
    
    return res[0], res[1]

# get function position in the file by function name and pattern

def getFunctionPosition_JavaScript(path, functionName, patternString):
    cmd = "node JSFunctionExtraction.js " + path
    if not os.path.exists(path):
        # wait 1 second and try again
        time.sleep(1)
    
    if os.path.exists(path):
        jsFuncItemsSource = os.popen(cmd).readlines()
        for line in jsFuncItemsSource:
            jsFuncItem = ujson.loads(line)
            
            jsctagPtn = ""
            for param in jsFuncItem['params']:
                jsctagPtn += param['type'] + "@@"
            if len(jsctagPtn) == 0:
                jsctagPtn = "--"
            
            if jsFuncItem['name'] == functionName and jsctagPtn == patternString:
                return jsFuncItem['startLine'], jsFuncItem['endLine']
        
        # print("Cannot find function: " + functionName + " in file: " + path)
        # if input("Do you want to continue to input line number manually? (y/n)") != "n":
        #     startLine = input("Please input start line: ")
        #     endLine = input("Please input end line: ")
        #     return int(startLine), int(endLine)
        return -1,-1


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
        
        # print("Cannot find function: " + functionName + " in file: " + path)
        # if input("Do you want to continue to input line number manually? (y/n)") != "n":
        #     startLine = input("Please input start line: ")
        #     endLine = input("Please input end line: ")
        #     return int(startLine), int(endLine)
        return -1,-1    
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
        
        # print("Cannot find function: " + functionName + " in file: " + path)
        # if input("Do you want to continue to input line number manually? (y/n)") != "n":
        #     startLine = input("Please input start line: ")
        #     endLine = input("Please input end line: ")
        #     return int(startLine), int(endLine)
        return -1,-1
    
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
