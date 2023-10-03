package org.nagoya_u.ertl.sa;

/**
 * Input:
 *  minSize
 *  Keyword list file
 *  Output folder path
 *
 */
public class App 
{



    public static void main (String[] args){
        String filePath1 = args[0];
        int startLine1 = Integer.valueOf(args[1]);
        int endLine1 = Integer.valueOf(args[2]);
        String filePath2 = args[3];
        int startLine2 = Integer.valueOf(args[4]);
        int endLine2 = Integer.valueOf(args[5]);
        String keywordsListPath = args[6];
        // String outputFilePath = args[8];

        //ava -jar Calculators/CPP14.jar /Users/syu/workspace/MSCCD_CloneHistoryTracker/11012-1-6187/device-os_crc32/c87611a26d990b10ae396eb2b2ff23b26dda7901.cpp 193 202 /Users/syu/workspace/MSCCD_CloneHistoryTracker/11012-1-6187/domoticz_Crc8_strMQ/e4930cc38788e780d04467c2b3d60b4d81cc3049.cpp 120 128 /Users/syu/workspace/MSCCD/grammarDefinations/cpp/CPP14.reserved
        // String filePath1 = "/Users/syu/workspace/MSCCD_CloneHistoryTracker/11012-1-6187/device-os_crc32/c87611a26d990b10ae396eb2b2ff23b26dda7901.cpp";
        // int startLine1 = 193;
        // int endLine1 = 202;
        // String filePath2 = "/Users/syu/workspace/MSCCD_CloneHistoryTracker/11012-1-6187/domoticz_Crc8_strMQ/e4930cc38788e780d04467c2b3d60b4d81cc3049.cpp";
        // int startLine2 = 120;
        // int endLine2 = 128;
        // String keywordsListPath = "/Users/syu/workspace/MSCCD/grammarDefinations/cpp/CPP14.reserved";

        KeywordsSet k = new KeywordsSet(keywordsListPath);
        ParserController pController = new ParserController();

        TokenBag bag1 = pController.generateTokenBagByLinePosition(filePath1, startLine1, endLine1, k);
        TokenBag bag2 = pController.generateTokenBagByLinePosition(filePath2, startLine2, endLine2, k);

        Double overlapSimilarity = bag1.OverlapSimilarity(bag2);
        Double LCSimilarity = bag1.LCSSimilarity(bag2);

        System.out.println(String.valueOf(overlapSimilarity) + "," + String.valueOf(LCSimilarity));

    
    }


}
