from ErlangListener import ErlangListener
from ErlangParser import ErlangParser

class ErlangFunctionListener(ErlangListener):
    def __init__(self) -> None:
        super().__init__()
        self.functionList = []
        
    def enterFunction_(self, ctx:ErlangParser.Function_Context):
        functionName = ctx.functionClause(0).tokAtom().getText()  # 假设函数名在第一个functionClause中定义
        paramsList = ctx.functionClause(0).clauseArgs().getText()  # 获取参数列表
        startLine = ctx.start.line
        endLine = ctx.stop.line
        # print(f'Function Name: {functionName}, Parameters: {paramsList}, Start Line: {startLine}, End Line: {endLine}')
        print('{' + f'"name": "{functionName}", "params": "{paramsList}", "startLine": "{startLine}", "endLine": "{endLine}"' + '}')
        self.functionList.append('{' + f'"name": "{functionName}", "params": "{paramsList}", "startLine": "{startLine}", "endLine": "{endLine}"' + '}')