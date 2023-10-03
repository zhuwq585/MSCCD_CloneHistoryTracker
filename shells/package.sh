# !/bin/bash

cd SimpleSimilarityCalculator
mvn clean
mvn package -Dmaven.test.skip


# if [ ! -d $1/tokenizers/$2 ];then
#   mkdir $1/tokenizers/$2
#   else
#   echo " "
# fi


cp $1/SimpleSimilarityCalculator/target/SimpleSimilarityCalculator-1.0-SNAPSHOT.jar $1/Calculators/$2.jar   

mvn clean