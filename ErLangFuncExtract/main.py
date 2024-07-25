import sys
sys.setrecursionlimit(10000)
from antlr4 import *
from ErlangLexer import ErlangLexer
from ErlangParser import ErlangParser
from ErlangFunctionListener import ErlangFunctionListener  # 确保导入你的自定义Listener

def main(path):
    with open(path, 'r', encoding='utf-8', errors='ignore') as file:
        input_stream = InputStream(file.read())    
    
    lexer = ErlangLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = ErlangParser(stream)
    tree = parser.forms()  # 根据你的语法规则，这可能需要调整

    listener = ErlangFunctionListener()
    walker = ParseTreeWalker()
    walker.walk(listener, tree)
    return listener.functionList

# if __name__ == '__main__':
#     main(sys.argv)
