const fs = require('fs');
const ts = require("typescript");
const args = process.argv;





function extractFunctionsFromFile() {
    if(args.length >= 3){
        


        filePath = args[2];
        // filePath = "/Users/syu/workspace/MSCCD_CloneHistoryTracker/TSFunctionExtraction.js";
        var sourceFile;
        try{
            sourceFile = ts.createSourceFile(
                filePath,
                ts.sys.readFile(filePath),
                ts.ScriptTarget.Latest,
                true
            );
        }catch(e){
            console.log("")
        }

        const functions = []


        function visit(node) {
            // 检查是否为函数声明节点
            try{
                if (ts.isFunctionDeclaration(node)) {
                    const functionName = node.name ? node.name.text : "anonymous";
                    const startLine = sourceFile.getLineAndCharacterOfPosition(node.getStart()).line + 1;
                    const endLine = sourceFile.getLineAndCharacterOfPosition(node.getEnd()).line + 1;
                    // console.log(`Function name: ${functionName}, Start line: ${startLine}, End line: ${endLine}`);
                    let paramsTmp = []
                    for(var paraIndex = 0; paraIndex < node.parameters.length; paraIndex++){
                        try{
                            paramsTmp.push({type:node.parameters[paraIndex].type.constructor.name})
                        }catch(e){
                            paramsTmp.push({type:'undefined'})
                        }
                    }
                    
                    if (node.type == undefined){
                        typeTmp = "undefined"
                    }else{
                        typeTmp = node.type.constructor.name
                    }

                    functions.push({
                        name: functionName,
                        startLine: startLine,
                        endLine : endLine,
                        type:typeTmp,
                        params : paramsTmp
                    })
                }
            }catch(e){
                return;
            }
        
            // 遍历子节点
            ts.forEachChild(node, visit);
        }
        
        visit(sourceFile);

        functions.forEach((fn) => {
            // console.log(`Name: ${fn.name}`);
            // console.log(`Start Line: ${fn.startLine}`);
            // console.log(`End Line: ${fn.endLine}`);
            // console.log('-----');
            try{
                console.log(JSON.stringify(fn))
            }catch(e){
                console.log(filePath)
            }
          });
    }
}

// 使用此函数提取特定TypeScript文件中的函数
extractFunctionsFromFile();