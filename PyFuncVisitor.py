import ast

class FuncVisitor(ast.NodeVisitor):
    def __init__(self):
        self.detectedFunc = []
    
    def visit_FunctionDef(self, node):
        # print(f"Function name: {node.name}, Start line: {node.lineno}, End line: {node.end_lineno}")
        self.detectedFunc.append({
        "name": node.name,
        "startLine" : node.lineno,
        "endLine" : node.end_lineno
        })
        self.generic_visit(node) 