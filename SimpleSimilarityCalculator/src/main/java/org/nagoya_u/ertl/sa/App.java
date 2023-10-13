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

        //java -jar Calculators/Java9.jar 11010-1-7391/smarthome_equals/11730b46103ba7899addf6bac7c9bfc1e2d68212.java 118 133 11010-1-7391/freedomotic_equals/952ae0b698cbe625be7f4889d549a6e7152b6b09.java 430 446 ~/workspace/MSCCD/grammarDefinations/Java9/Java9.reserved
        // String filePath1 = "11010-1-7391/smarthome_equals/11730b46103ba7899addf6bac7c9bfc1e2d68212.java";
        // int startLine1 = 118;
        // int endLine1 = 133;
        // String filePath2 = "11010-1-7391/freedomotic_equals/952ae0b698cbe625be7f4889d549a6e7152b6b09.java";
        // int startLine2 = 430;
        // int endLine2 = 446;
        // String keywordsListPath = "/Users/syu/workspace/MSCCD/grammarDefinations/Java9/Java9.reserved";


        KeywordsSet k = new KeywordsSet(keywordsListPath);
        ParserController pController = new ParserController();

        TokenBag bag1 = pController.generateTokenBagByLinePosition(filePath1, startLine1, endLine1, k);
        TokenBag bag2 = pController.generateTokenBagByLinePosition(filePath2, startLine2, endLine2, k);

        Double overlapSimilarity = bag1.OverlapSimilarity(bag2);
        Double LCSimilarity = bag1.LCSSimilarity(bag2);

        System.out.println(String.valueOf(overlapSimilarity) + "," + String.valueOf(LCSimilarity));

    
    }


}
