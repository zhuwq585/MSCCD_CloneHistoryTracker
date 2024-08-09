# MSCCD_CloneHistoryTracker


## How to use

### Step 1: generate a similarity calculator of the target language

+ Config the generator by **./parserConfig.json**
  + parser: the path of the folder where ANTLR grammars of the target language are
  + grammarName
  + startSymbol
+ generate calculator: **python3 calculatorGeneration.py**

### Step 2: start tracking

+ This tool support two granularities:
  + File level: controller_file.py
  + Function level: controller_func.py
    +  We indentify the function as the same function in the past versions by function name and parameter list. So this tool can not track all the modification history when rename or parameter list modification exists. 
+ Configurations in the controller_**.py
  + MSCCD_PATH: path to MSCCD root folder
  + taskId, detectionId
  + cloneIndex: to configure which pair to track
    + x(x >= 0) : the clone index of target clone 
    + -1 : for all the clone
    + x(x < -1) : random sampling x pair from the taskId-detectionId
  + language
+ Dependencies: (Function mode only)
  + Java,Go: CTag
  + JavaScript, TypeScript: nodejs
  + C/C++: Clang
  
### Step 3: check results 

+ HTML report will be generated automatically in **./reports** folder
+ 
+ ![alt text](HTMLReport-1.png)




## Dependency

+ jinja2
+ ujson 
+ matplotlib