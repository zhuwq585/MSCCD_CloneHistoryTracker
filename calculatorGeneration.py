# step 1: init
# del * in folder parser

# step 2: config reading and copy files

# step 3: parser generation

# step 4: ParserController generation

# step 5: pack the tokenizer into jar file
import sys, os, ujson


def parserControllerFileGeneration(grammarName, buildingAbspath, startRule):
    context = open(buildingAbspath + "ParserController.template", "r").read()
    context = context.replace("<<+GrammarName+>>", grammarName)
    context = context.replace("<<+StartRule+>>", startRule)


    filePath = buildingAbspath + '/ParserController.java'
    open(filePath, 'w').write(context)
    
    pass


def addPackageDeclaration(rpath):
    fileList = []
    if os.path.exists(rpath):
        fileWalking = os.walk(rpath)
        for path, dir_list, file_list in fileWalking:
            for file_name in file_list:
                filePathTmp = os.path.abspath(path+"/"+file_name)
                if os.path.splitext(filePathTmp)[1] == ".java":
                    fileList.append(filePathTmp)
    
    for filePath in fileList:
        file = open(filePath, "r")
        content = "package org.nagoya_u.ertl.sa.parser;\n"
        for line in file.readlines():
            content = content + line
        file = open(filePath, 'w')
        file.write(content)


if __name__ == "__main__":

    CONFIG_FILE        = "./parserConfig.json"
    rootAbspath        = os.path.abspath(sys.path[0])
    buildingAbspath    = rootAbspath + '/SimpleSimilarityCalculator/src/main/java/org/nagoya_u/ertl/sa/'
    parserBuildingPath = buildingAbspath + "/parser/"
    MSCCD_PATH         = "/Users/syu/workspace/MSCCD/"
    
    # rootAbspath     = os.path.abspath(sys.path[0])
    # buildingAbspath = rootAbspath + '/runtime'

    print("############################")
    print("#### Tokenizer generation started.")
    print("############################")

    # step1
    print("#### Clear building folder.")
    os.system("bash shells/clearTokenizerBuildingFolder.sh " + parserBuildingPath)
    
    #step2
    print("#### Copy resources to building folder.")
    configObj   = ujson.loads(open(CONFIG_FILE, "r").read())
    parserSourcePath  = MSCCD_PATH + configObj['parser']
    
    os.system("bash shells/cpResources.sh " + parserSourcePath + " " + parserBuildingPath)
    # os.system("bash shells/cpResources.sh " + parserSourcePath + " " + buildingAbspath)

    # step3 
    print("#### Generate a parser by ANTLR.")
    os.system("bash shells/javaParserGeneration.sh " + parserBuildingPath)
    # os.system("bash shells/javaParserGeneration.sh " + buildingAbspath)

    addPackageDeclaration(parserBuildingPath)

    # step4 
    print("#### Tokenizer generation. ")
    parserControllerFileGeneration(configObj['grammarName'] , buildingAbspath, configObj["startSymbol"])

    # step5
    os.system("bash shells/package.sh " + rootAbspath + " " + configObj["grammarName"])

    print("###################")

    if os.path.exists("./Calculators/" +  configObj['grammarName'] + ".jar"):
        # print("#### Tokenizer for " + str(configObj['grammarName']) + " is generated in ./tokenizers/" + str(configObj['grammarName']))
        # print("#### You can use this tokenizer by configuring the field 'tokenizer' of ./config.json to '" + str(configObj['grammarName']) + "'")
        print("#### Over")
    else:
        print("Failed to generate tokenizer.")
        # print("Check error report below.")
        # print("Over")
    print("###################")
    # os.system("bash shells/runtimeCreation.sh " + rootAbspath)
    pass



