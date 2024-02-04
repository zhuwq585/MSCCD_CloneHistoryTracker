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
MACRO_LIST = ["define", "ifdef", "ifndef", "endif", "undef", "if", "else", "elif", "include"]

####

import os,ujson
os.environ['LD_LIBRARY_PATH'] = LLVM_PATH
import clang.cindex
import re
import chardet
clang.cindex.Config.set_library_path(LLVM_PATH)




def getAllFunctionItems(path, language):
    if language in {"Java", "Go"}:
        return getAllFunctionItems_CTag(path, language)
    elif language == "JavaScript":
        return getAllFunctionItems_JavaScript(path)
    elif language in { "C++", "C"}:
        return getAllFunctionItems_Cpp(path)
    
    
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
        return None


def getAllFunctionItems_JavaScript(path):
    res = {}
    cmd = "node JSFunctionExtraction.js " + path
    jsFuncItemsSources = os.popen(cmd).readlines()
    
    for line in jsFuncItemsSources:
        jsFuncItem = ujson.loads(line)
        
        ptn = ""
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
    if language in {"Java", "Go"}:
        return getFunctionName_Ptn_CTAG(path, startLine, endLine, language)
    elif language == "JavaScript":
        return getFunctionName_Ptn_JavaScript(path, startLine, endLine)
    elif language in {"C++", "C"}:
        return getFunctionName_Ptn_Cpp(path, startLine, endLine)


def getFunctionName_Ptn_Cpp(path, startLine, endLine):
    removeMacro_Cpp(path)
    # clang.cindex.Config.set_library_path("/opt/homebrew/opt/llvm/lib")
    try:
        index = clang.cindex.Index.create()
        translation_unit = index.parse(path)
        for cursor in translation_unit.cursor.walk_preorder():
            if cursor.extent.start.line == startLine and cursor.extent.end.line == endLine and (cursor.kind == clang.cindex.CursorKind.CXX_METHOD or cursor.kind == clang.cindex.CursorKind.FUNCTION_DECL):
                
                file_path_cursor = cursor.extent.start.file.name
                if file_path_cursor != path:
                    continue
                function_name = cursor.spelling
                
                # previous version
                # function_params_type = [p.type.spelling for p in cursor.get_arguments()]
                
                # if cursor.semantic_parent.kind == clang.cindex.CursorKind.CLASS_DECL:
                #     class_name = cursor.semantic_parent.displayname
                # else:
                #     class_name = "@NONE@"
                
                # pattern = class_name + "@@" + "::".join(function_params_type)
                
                # new version
                
                pattern = cursor.type.spelling
                recoverMacro_Cpp(path)
                return function_name, pattern
        
        # function not found
        print("### Cannot find function in file: " + path)
        print("Start line: " + str(startLine) + " End line: " + str(endLine))
        if input("Function not found in the newest commit, maybe in the macro. Do you want to manully check code base and input line number? (y/n)") != "n":
            function_name = input("Function Name: ")
            pattern = input("Pattern Line: ")
            recoverMacro_Cpp(path)
            return function_name, pattern
    except Exception:
        recoverMacro_Cpp(path)
        print("Error(getFunctionName_Ptn): " + path)
        return None, None
        


def getFunctionName_Ptn_CTAG(path, startLine, endLine, language):
    cmd = "ctags --fields=+ne --output-format=json " + path
    
    res = os.popen(cmd).readlines()
    for ctagItemLine in res:
        ctagItem = ujson.loads(ctagItemLine)
        if ((ctagItem['line'] <= startLine) and (ctagItem['line'] >= startLine  - NOTATION_LINE)) and ctagItem['end'] == endLine and ctagItem['kind'] in FunctionItemNameSet:
            
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
    # if not os.path.exists(path):
    #     # wait 1 second and try again
    #     time.sleep(1)
    
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
        
        print("Cannot find function: " + functionName + " in file: " + path)
        if input("Do you want to continue to input line number manually? (y/n)") != "n":
            startLine = input("Please input start line: ")
            endLine = input("Please input end line: ")
            return int(startLine), int(endLine)
        return -1,-1
    else:
        print("Error(getFunctionPosition): file not found: " + path)
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
            if input("Function not found in a non-initial commit, maybe rename or retype. Do you want to manully check code base and input line number? (y/n)") != "n":
                startLine = input("Please input start line: ")
                endLine = input("Please input end line: ")
                return int(startLine), int(endLine)
        return -1,-1    
    else:
        print("Error(getFunctionPosition): file not found: " + path)
        return None

def getFunctionPosition_Cpp(path, functionName, patternString):
    # if not os.path.exists(path):
    #     # wait 1 second and try again
    #     time.sleep(1)
        
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
            return None
        
        
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
                    detectedFunction.append(cursor.extent.start.line, cursor.extent.end.line)
                    # return cursor.extent.start.line, cursor.extent.end.line
        
        recoverMacro_Cpp(path)
        if len(detectedFunction) == 1:
            return detectedFunction[0][0],detectedFunction[0][1]
        elif len(detectedFunction) > 1:
            # return -1, -1
            print("Multiple function named " + function_name + " detected in lines: \n")
            for item in detectedFunction:
                print(str(item[0]) + "-" + str(item[1]))
            startLine = input("Please input start line: ")
            endLine = input("Please input end line: ")
            return int(startLine), int(endLine)
        else:
            ## function not found
            # return -1,-1
            print("Cannot find function: " + functionName + " in file: " + path)
            if input("Do you want to continue to input line number manually? (y/n)") != "n":
                startLine = input("Please input start line: ")
                # if startLine < 0:
                #     return -1, -1 
                endLine = input("Please input end line: ")
                return int(startLine), int(endLine)
            return -1,-1
    
    else:
        print("Error(getFunctionPosition): file not found: " + path)
        return None
    
    
    
def getFunctionPosition(path, functionName, patternString, language, functionIdendified):
    # if language in {"Java", "Go", "C"}:
    if language in {"Java", "Go"}:
        return getFunctionPosition_CTag(path, functionName, patternString, language, functionIdendified)
    
    elif language == "JavaScript":
        return getFunctionPosition_JavaScript(path, functionName, patternString)
    
    elif language in  {"C++","C"}:
        return getFunctionPosition_Cpp(path, functionName, patternString)




def removeMacro_Cpp(path):
    if os.path.exists(path):
        try:
            sourceCodeContent = open(path, "r").read() 
        except Exception as e:
            print("Error(removeMacro_Cpp): " + path)
            print(e)
            return None
        
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
        try:
            sourceCodeContent = open(path, "r").read() 
        except Exception as e:
            print("Error(recoverMacro_Cpp): " + path)
            print(e)
            return None
        
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
    functons = getAllFunctionItems("/Users/syu/workspace/MSCCD_CloneHistoryTracker/reports/20021-11/685/AliOS-Things_md5_update/871b538decdbfc9c8ad9ba600b728ebfe8b1118f.c", "C++")
    print(functons)
    pass