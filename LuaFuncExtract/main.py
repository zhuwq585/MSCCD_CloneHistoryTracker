import sys
from antlr4 import *
from LuaLexer import LuaLexer
from LuaParser import LuaParser
from LuaListener import LuaListener

# 自定义监听器，用于提取函数信息
class FunctionInfoListener(LuaListener):
    def __init__(self):
        self.functionList = []
        
    def enterStat(self, ctx):
        firstChildText = None
        try: 
            firstChildText = ctx.getChild(0).getText()
        except TypeError:
            pass
        if firstChildText == "function":
            # target
            functionName = ctx.getChild(1).getText()
            startLine = ctx.start.line
            endLine = ctx.stop.line
            params = []
            if ctx.funcbody().parlist():
                try:
                    params = [param.getText() for param in ctx.funcbody().parlist().namelist().NAME()]
                except:
                    params = []
                # params = [param.getText() for param in ctx.funcbody().parlist().namelist().NAME()]
            paramsList = ", ".join(params)
            # print(f'Function Name: {functionName}, Parameters: {paramsList}, Start Line: {startLine}, End Line: {endLine}')
            print('{' + f'"name": "{functionName}", "params": "{paramsList}", "startLine": "{startLine}", "endLine": "{endLine}"' + '}')
            self.functionList.append('{' + f'"name": "{functionName}", "params": "{paramsList}", "startLine": "{startLine}", "endLine": "{endLine}"' + '}')
        else:
            pass
            
    # def enterFunctiondef(self, ctx):
    #     functionName = "Anonymous"
    #     # if ctx.parentCtx.funcname():
    #     #     functionName = ctx.parentCtx.funcname().getText()
    #     startLine = ctx.start.line
    #     endLine = ctx.stop.line
    #     params = []
    #     if ctx.funcbody().parlist():
    #         params = [param.getText() for param in ctx.funcbody().parlist().namelist().NAME()]
    #     paramsList = ", ".join(params)
    #     # print(f'Function Name: {functionName}, Parameters: {paramsList}, Start Line: {startLine}, End Line: {endLine}')
    #     print('{' + f'"name": "{functionName}", "params": "{paramsList}", "startLine": "{startLine}", "endLine": "{endLine}"' + '}')

def main(path):
    with open(path, 'r', encoding='utf-8', errors='ignore') as file:
        input_stream = InputStream(file.read())  
    lexer = LuaLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = LuaParser(stream)
    tree = parser.chunk()

    # 使用自定义监听器遍历解析树
    listener = FunctionInfoListener()
    walker = ParseTreeWalker()
    walker.walk(listener, tree)
    return listener.functionList

# if __name__ == '__main__':
#     main(sys.argv)
