####
# author: zhuwq585
# This API is to identify functions in source code. Try to get function name and pattern by function position or get function position by function name and pattern.
# Supported languages and approaches:
#  - Java: CTag
#  - JavaScript: JSCTag
#  - C/C++: Clang
#
# Important ConfigItems:
#  - FunctionItemNameSet: a set of function item name. If the item name is in the set, it will be identified as a function item.
#  - NOTATION_LINE: the number of notation line. If the function item is in the notation line range, it will be identified as a function item.
#  - MACRO_LIST: a list of macro. If the macro is in the source code, it will be removed before function identification. DO NOT NEED TO INPUT sharp character.
#  - LLVM_PATH: the path of LLVM. If you want to use Clang to identify functions, you need to set the path of LLVM.

# Usage:
#  - getAllFunctionItems(path, language)
#    - return a dict of all functions in the file
#  - getFunctionName_Ptn(path, startLine, endLine, language)
#    - return function name and pattern by function position
#  - getFunctionPosition(path, functionName, patternString, language, functionIdendified)
#    - return function position by function name and pattern

# Example:
#  - getAllFunctionItems
#    - getAllFunctionItems("test.cpp", "C++")
#  - getFunctionName_Ptn
#    - getFunctionName_Ptn("test.cpp", 1, 5, "C++")
#  - getFunctionPosition
#    - getFunctionPosition("test.cpp", "test", "int@@int", "C++", 1)

####
# ctags --fields=+n --fields=+e --output-format=json ctagsTest/TokenBag.java

#### Config Items
FunctionItemNameSet = {'method','function',"func"}
LLVM_PATH = "/opt/homebrew/opt/llvm/lib"
NOTATION_LINE = 3
MIN_FUNCTIONLINES = 3
MACRO_LIST = ["define", "ifdef", "ifndef", "endif", "undef", "if", "else", "elif", "include"]
IF_MANUAL_CHECK = False

####

import os,ujson, sys
os.environ['LD_LIBRARY_PATH'] = LLVM_PATH
sys.path.append("/Users/syu/workspace/MSCCD_CloneHistoryTracker/ErLangFuncExtract")
sys.path.append("/Users/syu/workspace/MSCCD_CloneHistoryTracker/LuaFuncExtract")
import clang.cindex
import re
import ast
from PyFuncVisitor import FuncVisitor
from redbaron import RedBaron
import chardet
# from LuaFuncExtract.main import main as luaMain
# from ErLangFuncExtract.main import main as erlangMain


clang.cindex.Config.set_library_path(LLVM_PATH)




def getAllFunctionItems(path, language):
    if language in {"Java", "Go", "CSharp", "C#"}:
        return getAllFunctionItems_CTag(path, language)
    elif language in {"JavaScript","TypeScript"}:
        return getAllFunctionItems_EcmaScript(path, language)
    elif language in { "C++", "C"}:
        return getAllFunctionItems_Cpp(path)
    elif language == "Python":
        return getAllFunctionItems_Py(path)
    elif language == "C#" or language == "CSharp":
        return getAllFunctionItems_CS(path)
    elif language == "ErLang" or language == "Erlang":
        return getAllFunctionItems_ER(path)
    elif language == "Lua":
        return getAllFunctionItems_Lua(path)


def getAllFunctionItems_Lua(path):
    if os.path.exists(path):
        res = {}
        # cmd = "python3 /Users/syu/workspace/MSCCD_CloneHistoryTracker/LuaFuncExtract/main.py " + path
        # luaFuncItemsSources = os.popen(cmd).readlines()
        luaFuncItemsSources = luaMain(path)
        for line in luaFuncItemsSources:
            try:
                luaFuncItem = ujson.loads(line)
            except Exception:
                print(path)
                print(line)
                print("->####Error")
                continue
            
            ptn = ""
            if 'param' in luaFuncItem:
                for param in luaFuncItem['params']:
                    ptn += param['type'] + "@@"
            if len(ptn) == 0:
                ptn = "--"
            
            res[luaFuncItem['startLine']] = {
                luaFuncItem['endLine'] : {
                "name" : luaFuncItem['name'],
                "startLine" : luaFuncItem['startLine'],
                "endLine" : luaFuncItem['endLine'],
                "pattern" : ptn
                }
            }
        return res
    else:
        print("Error(getAllFunctionItems): file not found: " + path)
        return None

def getAllFunctionItems_ER(path):
    if os.path.exists(path):
        res = {}
        # cmd = "python3 /Users/syu/workspace/MSCCD_CloneHistoryTracker/ErLangFuncExtract/main.py " + path
        # erFuncItemsSources = os.popen(cmd).readlines()
        erFuncItemsSources = erlangMain(path)
        for line in erFuncItemsSources:
            try:
                erFuncItem = ujson.loads(line)
            except Exception:
                print(path)
                print(line)
                print("->####Error")
                continue
            
            ptn = ""
            if 'param' in erFuncItem:
                for param in erFuncItem['params']:
                    ptn += param['type'] + "@@"
            if len(ptn) == 0:
                ptn = "--"
            
            res[erFuncItem['startLine']] = {
                erFuncItem['endLine'] : {
                "name" : erFuncItem['name'],
                "startLine" : erFuncItem['startLine'],
                "endLine" : erFuncItem['endLine'],
                "pattern" : ptn
                }
            }
        return res
    else:
        print("Error(getAllFunctionItems): file not found: " + path)
        return None

def getAllFunctionItems_CS(path):
    if os.path.exists(path):
        res = {}
        cmd = "./CSFunctionExtraction.sh " + path
        csFuncItemsSources = os.popen(cmd).readlines()
        for line in csFuncItemsSources:
            try:
                csFuncItem = ujson.loads(line)
            except Exception:
                print(path)
                print(line)
                print("->####Error")
                continue
            
            ptn = ""
            if 'param' in csFuncItem:
                for param in csFuncItem['paramss']:
                    ptn += param['type'] + "@@"
                
            if len(ptn) == 0:
                ptn = "--"

                
            res[csFuncItem['startLine']] = {
                csFuncItem['endLine'] : {
                "name" : csFuncItem['name'],
                "startLine" : csFuncItem['startLine'],
                "endLine" : csFuncItem['endLine'],
                "pattern" : ptn
                }
            }
        
        return res
    else:
        print("Error(getAllFunctionItems): file not found: " + path)
        return None 
    
    
def getAllFunctionItems_Py(path):
    if os.path.exists(path):
        res = {}
        
        try:
        ### By using ast
            tree = ast.parse(open(path,"r").read())
            ast.increment_lineno(tree, n=0)
            visitor = FuncVisitor()
            visitor.visit(tree)
            
            for detectedFuncItem in visitor.detectedFunc:
                res[detectedFuncItem['startLine']] = {
                    detectedFuncItem['endLine'] : detectedFuncItem
                }
            return res
        except Exception:

            print("Failed by using ast")
        ### By using redbaron
            try:
                red = RedBaron(open(path,"r").read())
                for function_node in red.find_all('def'):
                    startLine = function_node.absolute_bounding_box.top_left.line
                    endLine = function_node.absolute_bounding_box.bottom_right.line
                    functionName = function_node.name
                    res[startLine] = {
                        endLine: {
                            "name": functionName,
                            "startLine" : startLine,
                            "endLine" : endLine
                        }
                    }
                print("successed:" + path)
                return res
            except Exception:
                print("failed by using redbaron")
                return None
    else:
        print("Error(getAllFunctionItems): file not found: " + path)
        return None 
    
def getAllFunctionItems_CTag(path, language):
    res = {}
    cmd = "ctags --fields=+ne --output-format=json " + path
    
    
    if os.path.exists(path):
        ctagRes = os.popen(cmd).readlines()
        for tagLine in ctagRes:
            ctagItem = ujson.loads(tagLine)
            if ctagItem['kind'] in FunctionItemNameSet:
                if 'end' in ctagItem:
                    res[ctagItem['line']] = {
                            ctagItem['end'] : {
                                "name" : ctagItem['name'],
                                "startLine" : ctagItem['line'],
                                "endLine" : ctagItem['end'],
                                "pattern" : ctagItem['pattern']
                            }
                        }
                else:
                    print("Error(getAllFunctionItems): ctagItem['end'] not found: " + path)
        return res
    else:
        print("Error(getAllFunctionItems): file not found: " + path)
        return []


def getAllFunctionItems_EcmaScript(path, language):
    # print("#####")
    # print(path)
    # print("####")
    res = {}
    if language == "JavaScript":
        cmd = "node JSFunctionExtraction.js " + path
    elif language == "TypeScript":
        cmd = "node TSFunctionExtraction.js " + path
        
    jsFuncItemsSources = os.popen(cmd).readlines()
    for line in jsFuncItemsSources:
        try:
            jsFuncItem = ujson.loads(line)
        except Exception:
            print(path)
            print(line)
            print("####")
            continue
        
        ptn = ""
        if 'param' in jsFuncItem:
            for param in jsFuncItem['params']:
                ptn += param['type'] + "@@"
            
        if len(ptn) == 0:
            ptn = "--"

            
        res[jsFuncItem['startLine']] = {
            jsFuncItem['endLine'] : {
            "name" : jsFuncItem['name'],
            "startLine" : jsFuncItem['startLine'],
            "endLine" : jsFuncItem['endLine'],
            "pattern" : ptn
            }
        }
    
    return res



def getAllFunctionItems_Cpp(path):
    removeMacro_Cpp(path)
    res = {}
    # clang.cindex.Config.set_library_path("/opt/homebrew/opt/llvm/lib")
    index = clang.cindex.Index.create()
    
    
    try:
        translation_unit = index.parse(path, args=['-std=c++11',  '-x', 'c++', '-Xclang', '-fsyntax-only'])
    except Exception as e:
        recoverMacro_Cpp(path)
        print("Error(getAllFunctionItems): " + path)
        print(e)
        return None
    
    
    for cursor in translation_unit.cursor.walk_preorder():
        try:
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
            
                res[cursor.extent.start.line] = {
                    cursor.extent.end.line : {
                    "name" : function_name,
                    "startLine" : cursor.extent.start.line,
                    "endLine" : cursor.extent.end.line,
                    "pattern" : pattern
                    }
                }
        except ValueError:
            continue
    recoverMacro_Cpp(path)
    return res
   


def JavaPatternGeneration(str):
    
    pattern = re.split(r'[,\s]+', str.split("(")[1].split(")")[0])[0::2]
    res = "::".join(pattern)
    if len(res) == 0:
        res = "--"
    return res

def getFunctionName_Ptn(path, startLine, endLine, language):
    if language in {"Java", "Go", "CSharp", "C#"}:
        return getFunctionName_Ptn_CTAG(path, startLine, endLine, language)
    elif language in {"JavaScript","TypeScript"}:
        return getFunctionName_Ptn_EcmaScript(path, startLine, endLine,language)
    elif language in {"C++", "C"}:
        return getFunctionName_Ptn_Cpp(path, startLine, endLine)
    elif language == "Python":
        return getFunctionName_Ptn_Py(path, startLine, endLine)
    elif language == "C#" or language == "CSharp":
        return getFunctionName_Ptn_CS(path,startLine,endLine)
    elif language in {"ErLang", "Erlang","Lua"}:
        return getFunctionName_Ptn_ANTLRParser(path, startLine, endLine, language)

def getFunctionName_Ptn_ANTLRParser(path, startLine, endLine, language):
    if language == "ErLang" or language == "Erlang":
        funcItems = getAllFunctionItems_ER(path)
    elif language == "Lua":
        funcItems = getAllFunctionItems_Lua(path)
    
    for startLineDetected in funcItems:
        for endLineDetected in funcItems[startLineDetected]:
            if (startLineDetected <= startLine+NOTATION_LINE and startLineDetected >= startLine-NOTATION_LINE )and (endLineDetected <= endLine + NOTATION_LINE and endLineDetected >= endLine - NOTATION_LINE):
                return funcItems[startLineDetected][endLineDetected]['name'], funcItems[startLineDetected][endLineDetected]['pattern']
            
def getFunctionName_Ptn_CS(path, startLine, endLine):
    funcItems = getAllFunctionItems_CS(path)
    for startLineDetected in funcItems:
        for endLineDetected in funcItems[startLineDetected]:
            if (startLineDetected <= startLine+NOTATION_LINE and startLineDetected >= startLine-NOTATION_LINE )and (endLineDetected <= endLine + NOTATION_LINE and endLineDetected >= endLine - NOTATION_LINE):
                return funcItems[startLineDetected][endLineDetected]['name'], funcItems[startLineDetected][endLineDetected]['pattern']
    

def getFunctionName_Ptn_Py(path, startLine, endLine):
    funcItems = getAllFunctionItems_Py(path)
    if startLine in funcItems:
        if endLine in funcItems[startLine]:
            return funcItems[startLine][endLine]['name'], "py"
    
    return None

def getFunctionName_Ptn_Cpp(path, startLine, endLine):
    removeMacro_Cpp(path)
    # clang.cindex.Config.set_library_path("/opt/homebrew/opt/llvm/lib")
    try:
        index = clang.cindex.Index.create()
        translation_unit = index.parse(path)
        for cursor in translation_unit.cursor.walk_preorder():
            if (cursor.extent.start.line <= startLine+NOTATION_LINE and cursor.extent.start.line >= startLine-NOTATION_LINE )and (cursor.extent.end.line <= endLine + NOTATION_LINE and cursor.extent.end.line >= endLine - NOTATION_LINE) and (cursor.kind == clang.cindex.CursorKind.CXX_METHOD or cursor.kind == clang.cindex.CursorKind.FUNCTION_DECL):
                
                file_path_cursor = cursor.extent.start.file.name
                if file_path_cursor != path:
                    continue
                function_name = cursor.spelling
                
                
                pattern = cursor.type.spelling
                recoverMacro_Cpp(path)
                return function_name, pattern
        
        # function not found
        if IF_MANUAL_CHECK:
            print("### Cannot find function in file: " + path)
            print("Start line: " + str(startLine) + " End line: " + str(endLine))
            if input("Function not found in the newest commit, maybe in the macro. Do you want to manully check code base and input line number? (y/n)") != "n":
                function_name = input("Function Name: ")
                pattern = input("Pattern Line: ")
                recoverMacro_Cpp(path)
                return function_name, pattern
        else:
            return None, None
    except Exception:
        recoverMacro_Cpp(path)
        print("Error(getFunctionName_Ptn): " + path)
        return None, None
        


def getFunctionName_Ptn_CTAG(path, startLine, endLine, language):
    cmd = "ctags --fields=+ne --output-format=json " + path
    
    res = os.popen(cmd).readlines()
    for ctagItemLine in res:
        ctagItem = ujson.loads(ctagItemLine)
        try:
            if ((ctagItem['line'] <= startLine) or (ctagItem['line'] >= startLine  - NOTATION_LINE)) and ctagItem['end'] == endLine and ctagItem['kind'] in FunctionItemNameSet:
                
                # if language == "Java":
                #     return ctagItem['name'],JavaPatternGeneration(ctagItem['pattern'])
                
                return ctagItem['name'], ctagItem['pattern']
        except KeyError:
            continue
        
    return None



def getFunctionName_Ptn_EcmaScript(path, startLine, endLine, language):
    # node JSFunctionExtraction.js path
    if language == "JavaScript":
        cmd = "node JSFunctionExtraction.js " + path
    elif language == "TypeScript":
        cmd = "node TSFunctionExtraction.js " + path
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

def getFunctionPosition_EcmaScript(path, functionName, patternString, language):
    if language == "JavaScript":
        cmd = "node JSFunctionExtraction.js " + path
    elif language == "TypeScript":
        cmd = "node TSFunctionExtraction.js " + path
    # if not os.path.exists(path):
    #     # wait 1 second and try again
    #     time.sleep(1)
    
    if os.path.exists(path):
        jsFuncItemsSource = os.popen(cmd).readlines()
        matchedFuns = []
        for line in jsFuncItemsSource:
            jsFuncItem = ujson.loads(line)
            
            jsctagPtn = ""
            for param in jsFuncItem['params']:
                jsctagPtn += param['type'] + "@@"
            if len(jsctagPtn) == 0:
                jsctagPtn = "--"
            
            # if jsFuncItem['name'] == functionName and jsctagPtn == patternString:
            if jsFuncItem['name'] == functionName:
                matchedFuns.append((jsFuncItem['startLine'], jsFuncItem['endLine']))
        
        if len(matchedFuns) == 1:
            return matchedFuns[0][0],matchedFuns[0][1]
        elif len(matchedFuns) > 1:
            print("Multiple target found:" + matchedFuns)
            index = input("please input index of matched target:")
            
            if index < 0:
                return -1,-1
            else:
                return matchedFuns[index][0],matchedFuns[index][1]
        else:
            print("Cannot find function: " + functionName + " in file: " + path)
            if IF_MANUAL_CHECK:
                # if input("Do you want to continue to input line number manually? (y/n)") != "n":
                startLine = input("Please input start line: ")
                endLine = input("Please input end line: ")
                return int(startLine), int(endLine)
            else:
                return -1,-1
    else:
        print("Error(getFunctionPosition): file not found: " + path)
        return -1, -1

def getFunctionPosition_Py(path, functionName):
    detectedFuncs = getAllFunctionItems_Py(path)
    for startLine in detectedFuncs:
        for endLine in detectedFuncs[startLine]:
            if detectedFuncs[startLine][endLine]['name'] == functionName:
                return startLine, endLine
    
    return -1, -1


def getFunctionPosition_CTag(path, functionName, patternString, language, functionIdendified):

    cmd = "ctags --fields=+ne --output-format=json " + path
    # if not os.path.exists(path):
    #     # wait 1 second and try again
    #     time.sleep(1)
    
    if os.path.exists(path):
        res = os.popen(cmd).readlines()
        for ctagItemLine in res:
            
            ctagItem = ujson.loads(ctagItemLine)
            
            # if language == "Java":
            #     cTagPattern = JavaPatternGeneration(ctagItem['pattern'])
            # else:
            cTagPattern = ctagItem['pattern']
                
            if ctagItem['name'] == functionName and ctagItem['kind'] in FunctionItemNameSet and cTagPattern == patternString:
            # if ctagItem['name'] == functionName and ctagItem['kind'] in FunctionItemNameSet:
                return ctagItem['line'], ctagItem['end']
        
        # an example that code provided by capilot is buggy
        # print("Cannot find function: " + functionName + " in file: " + path")
        
        print("### Cannot find function: " + functionName + " in file: " + path)
        if functionIdendified > 0:
            if IF_MANUAL_CHECK:
                if input("Function not found in a non-initial commit, maybe rename or retype. Do you want to manully check code base and input line number? (y/n)") != "n":
                    startLine = input("Please input start line: ")
                    endLine = input("Please input end line: ")
                    return int(startLine), int(endLine)
        return -1,-1    
    else:
        print("Error(getFunctionPosition): file not found: " + path)
        return -1,-1

def getFunctionPosition_Cpp(path, functionName, patternString):        
    if os.path.exists(path):
        # clang.cindex.Config.set_library_path("/opt/homebrew/opt/llvm/lib")

        removeMacro_Cpp(path)
        index = clang.cindex.Index.create()
        
        try:
            translation_unit = index.parse(path, args=['-std=c++11',  '-x', 'c++', '-Xclang', '-fsyntax-only'])
        except Exception as e:
            recoverMacro_Cpp(path)
            print("Error(getFunctionPosition_Cpp) " + path)
            print(e)
            return -1,-1
        
        
        detectedFunction = []
        for cursor in translation_unit.cursor.walk_preorder():
            if cursor.kind == clang.cindex.CursorKind.CXX_METHOD or cursor.kind == clang.cindex.CursorKind.FUNCTION_DECL:
                
                file_path_cursor = cursor.extent.start.file.name
                if file_path_cursor != path:
                    continue
                function_name = cursor.spelling
                
                # new version
                pattern = cursor.type.spelling
                
                if function_name == functionName and pattern == patternString:
                    # recoverMacro_Cpp(path)
                    detectedFunction.append((cursor.extent.start.line, cursor.extent.end.line))
                    # return cursor.extent.start.line, cursor.extent.end.line
        
        recoverMacro_Cpp(path)
        if len(detectedFunction) == 1:
            return detectedFunction[0][0],detectedFunction[0][1]
        elif len(detectedFunction) > 1:
            # return -1, -1
            filteredFunction = []
            for item in detectedFunction:
                if item[1] - item[0] >= MIN_FUNCTIONLINES:
                    filteredFunction.append(item)
            
            if len(filteredFunction) == 1:
                return filteredFunction[0][0],filteredFunction[0][1]
            else:
                if IF_MANUAL_CHECK:
                    print("Multiple function named " + function_name + " detected in lines: \n")
                    for item in detectedFunction:
                        print(str(item[0]) + "-" + str(item[1]))
                    startLine = input("Please input start line: ")
                    endLine = input("Please input end line: ")
                    return int(startLine), int(endLine)
                else:
                    return -1, -1
        else:
            ## function not found
            # return -1,-1
            if IF_MANUAL_CHECK:
                print("Cannot find function: " + functionName + " in file: " + path)
                if input("Do you want to continue to input line number manually? (y/n)") != "n":
                    startLine = input("Please input start line: ")
                    # if startLine < 0:
                    #     return -1, -1 
                    endLine = input("Please input end line: ")
                    return int(startLine), int(endLine)
                return -1,-1
            else:
                return -1,-1
    
    else:
        print("Error(getFunctionPosition): file not found: " + path)
        return -1,-1
 
def getFunctionPosition_ANTLRParser(path, functionName, patternString, language):
    if os.path.exists(path):
        if language == "ErLang" or language == "Erlang":
            allFunctionItemsInSource = getAllFunctionItems_ER(path)
        elif language == "Lua":
            allFunctionItemsInSource = getAllFunctionItems_Lua(path)
        
        matchedItems = []
        for startLineDetected in allFunctionItemsInSource:
            for endLineDetected in allFunctionItemsInSource[startLineDetected]:
                if allFunctionItemsInSource[startLineDetected][endLineDetected]['name'] == functionName and allFunctionItemsInSource[startLineDetected][endLineDetected]['pattern'] == patternString:
                    matchedItems.append(allFunctionItemsInSource[startLineDetected][endLineDetected])
        
        if len(matchedItems) == 1:
            return matchedItems[0]['startLine'],matchedItems[0]['endLine']
        elif len(matchedItems) > 1:
            # return -1, -1
            filteredFunction = []
            for item in matchedItems:
                if item[1] - item[0] >= MIN_FUNCTIONLINES:
                    filteredFunction.append(item)
            
            if len(filteredFunction) == 1:
                return filteredFunction[0][0],filteredFunction[0][1]
            else:
                if IF_MANUAL_CHECK:
                    print("Multiple function named " + functionName + " detected in lines: \n")
                    for item in matchedItems:
                        print(str(item[0]) + "-" + str(item[1]))
                    startLine = input("Please input start line: ")
                    endLine = input("Please input end line: ")
                    return int(startLine), int(endLine)
                else:
                    return -1, -1
        else:
            ## function not found
            # return -1,-1
            if IF_MANUAL_CHECK:
                print("Cannot find function: " + functionName + " in file: " + path)
                if input("Do you want to continue to input line number manually? (y/n)") != "n":
                    startLine = input("Please input start line: ")
                    # if startLine < 0:
                    #     return -1, -1 
                    endLine = input("Please input end line: ")
                    return int(startLine), int(endLine)
                return -1,-1
            else:
                return -1,-1
    else:
        print("Error(getFunctionPosition): file not found: " + path)
        return -1,-1
    
   
def getFunctionPosition_CS(path, functionName, patternString):
    if os.path.exists(path):
        allFunctionItemsInSource = getAllFunctionItems_CS(path)
        
        matchedItems = []
        for startLineDetected in allFunctionItemsInSource:
            for endLineDetected in allFunctionItemsInSource[startLineDetected]:
                if allFunctionItemsInSource[startLineDetected][endLineDetected]['name'] == functionName and allFunctionItemsInSource[startLineDetected][endLineDetected]['pattern'] == patternString:
                    matchedItems.append(allFunctionItemsInSource[startLineDetected][endLineDetected])
        
        
        if len(matchedItems) == 1:
            return matchedItems[0]['startLine'],matchedItems[0]['endLine']
        elif len(matchedItems) > 1:
            # return -1, -1
            filteredFunction = []
            for item in matchedItems:
                if item[1] - item[0] >= MIN_FUNCTIONLINES:
                    filteredFunction.append(item)
            
            if len(filteredFunction) == 1:
                return filteredFunction[0][0],filteredFunction[0][1]
            else:
                if IF_MANUAL_CHECK:
                    print("Multiple function named " + functionName + " detected in lines: \n")
                    for item in matchedItems:
                        print(str(item[0]) + "-" + str(item[1]))
                    startLine = input("Please input start line: ")
                    endLine = input("Please input end line: ")
                    return int(startLine), int(endLine)
                else:
                    return -1, -1
        else:
            ## function not found
            # return -1,-1
            if IF_MANUAL_CHECK:
                print("Cannot find function: " + functionName + " in file: " + path)
                if input("Do you want to continue to input line number manually? (y/n)") != "n":
                    startLine = input("Please input start line: ")
                    # if startLine < 0:
                    #     return -1, -1 
                    endLine = input("Please input end line: ")
                    return int(startLine), int(endLine)
                return -1,-1
            else:
                return -1,-1
        
                

    else:
        print("Error(getFunctionPosition): file not found: " + path)
        return -1,-1
    
def getFunctionPosition(path, functionName, patternString, language, functionIdendified):
    # if language in {"Java", "Go", "C"}:
    if language in {"Java", "Go", "CSharp", "C#"}:
        return getFunctionPosition_CTag(path, functionName, patternString, language, functionIdendified)
    
    elif language in {"JavaScript","TypeScript"}:
        return getFunctionPosition_EcmaScript(path, functionName, patternString,language)
    
    elif language in  {"C++","C"}:
        return getFunctionPosition_Cpp(path, functionName, patternString)
    
    elif language == "Python":
        return getFunctionPosition_Py(path, functionName)
    elif language == "C#" or language == "CSharp":
        return getFunctionPosition_CS(path, functionName, patternString)
    elif language in {"ErLang", "Erlang","Lua"}:
        return getFunctionPosition_ANTLRParser(path, functionName, patternString, language)




def removeMacro_Cpp(path):
    if os.path.exists(path):
        # try:
        #     sourceCodeContent = open(path, "r").read() 
        # except Exception as e:
        #     print("Error(removeMacro_Cpp): " + path)
        #     print(e)
        #     return None
        try:
            sourceCodeContent = open(path, "r").read()
        except UnicodeDecodeError:
            try:
                with open(path, 'rb') as f:
                    raw_data = f.read()
                    encoding = chardet.detect(raw_data)['encoding']

                with open(path, 'r', encoding=encoding) as f:
                    sourceCodeContent = f.read()
            except Exception as e:
                print("Error(removeMacro_Cpp): " + path)
                print(e)
                sourceCodeContent = open(path, "r", errors='ignore').read()
        
        for macro in MACRO_LIST:
            regex = generate_regex_macroRomove(macro)
            sourceCodeContent = re.sub(regex, "//#" + macro, sourceCodeContent)
            
            # sourceCodeContent = sourceCodeContent.replace(macro, "//" + macro)
        open(path, "w").write(sourceCodeContent)
    else:
        print("Error(removeMacro_Cpp): file not found: " + path)
        pass

def recoverMacro_Cpp(path):
        
    if os.path.exists(path):
        # try:
        #     sourceCodeContent = open(path, "r").read() 
        # except Exception as e:
        #     print("Error(recoverMacro_Cpp): " + path)
        #     print(e)
        #     return None
        
        try:
            sourceCodeContent = open(path, "r").read()
        except UnicodeDecodeError:
            try:
                with open(path, 'rb') as f:
                    raw_data = f.read()
                    encoding = chardet.detect(raw_data)['encoding']

                with open(path, 'r', encoding=encoding) as f:
                    sourceCodeContent = f.read()
            except Exception as e:
                print("Error(removeMacro_Cpp): " + path)
                print(e)
                sourceCodeContent = open(path, "r", errors='ignore').read()
        
        
        for macro in MACRO_LIST:
            regex = generate_regex_macroRecovers(macro)
            sourceCodeContent = re.sub(regex, "#" + macro, sourceCodeContent)
            # sourceCodeContent = sourceCodeContent.replace("//" + macro, macro)
        open(path, "w").write(sourceCodeContent)
    else:
        print("Error(recoverMacro_Cpp): file not found: " + path)
        pass
    

def generate_regex_macroRomove(keyword):
    escaped_word = re.escape(keyword)
    return r"#\s*{}".format(escaped_word)

def generate_regex_macroRecovers(keyword):
    escaped_word = re.escape(keyword)
    return r"//#\s*{}".format(escaped_word)


# def detect_encoding(file_path):
#     with open(file_path, 'rb') as file:
#         # 读取一些字节用于检测
#         raw_data = file.read(5000)
#         result = chardet.detect(raw_data)
#         return result["encoding"]


if __name__ == "__main__":
    # functons = getAllFunctionItems("/Users/syu/workspace/MSCCD/scripts/MSCCDTaskData.py", "Python")
    # functions = getFunctionPosition_EcmaScript("/Users/syu/workspace/MSCCD_CloneHistoryTracker/reports/20005-11/2/iotagent-ul_singleMeasure/b3e6334e68ba23d38a9ebf1e7f21a7627045e025.js", "singleMeasure","--","JavaScript")
    
    functions = getAllFunctionItems("/Users/syu/IoT_Projs/Erlang/dgiot/test/emqx_acl_cache_SUITE.erl","Erlang")
    print(functions)
    pass