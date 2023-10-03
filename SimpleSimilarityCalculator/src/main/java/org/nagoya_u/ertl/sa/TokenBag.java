package org.nagoya_u.ertl.sa;

import java.util.HashMap;
import java.util.LinkedList;
import java.util.Set;

import org.antlr.runtime.Token;

public class TokenBag{

    public HashMap<String, Integer> tokenMap;
    public LinkedList<String> tokenSequence;
    public int projectId;
    public int fileId;
    public int bagId;
    public int granularity;
    public int startLine;
    public int endLine;
    public int num_keywords;
    public int tokenNum;
    public int symbolNum;

    // TokenBag(int fileId, int bagId, int granularity, int symbolNum, int pId){
    TokenBag(int fileId, int granularity, int symbolNum, int pId){
        tokenMap = new HashMap<String, Integer>();
        tokenSequence = new LinkedList<String>();
        this.fileId       = fileId;
        this.granularity  = granularity;
        // this.bagId        = bagId;
        this.symbolNum    = symbolNum;
        this.projectId    = pId;

        tokenNum     = 0;
        num_keywords = 0;
    }

    public boolean ifBagIdentified(TokenBag inputedBag){
        if (inputedBag.projectId == this.projectId && inputedBag.fileId == this.fileId){
            if (inputedBag.startLine == this.startLine && inputedBag.endLine == this.endLine){
                return true;
            }
        }
        return false;
    }

    public void setBagId(int bagId){
        this.bagId = bagId;
    }

    public void addToken(String str){
        if(str.length() < 1)
            return;
            
        str = this.removeEnter(str);
        try{
            if ( tokenMap.containsKey(str))
                tokenMap.put(str, tokenMap.get(str)+1);
            else
                tokenMap.put(str, 1);    
            
            tokenNum++;
        }catch(OutOfMemoryError e){
            e.printStackTrace();
        }

    }

    public void addTokenToSequence(String str){
        this.tokenSequence.add(str);
    }

    private String removeEnter(String str){
        // if (str.equalsIgnoreCase(str)){
        //     str = str.replaceAll("\n", "");
        // }
        final String pattern = "\\s";
        str = str.replaceAll(pattern, "");
        return str;
    }

    public String[] getAllToken(){
        Set<String> keyset = tokenMap.keySet();
        return keyset.toArray(new String[keyset.size()]);
    }

    public void setPosition(int startLine, int endLint){
        this.startLine = startLine;
        this.endLine   = endLint;
    }

    public void addKeywords(){
        num_keywords++;
    }

    public String getPosition(){
        String res = String.valueOf(startLine) + ": :" + String.valueOf(endLine);
        return res;
    }

    public String getTokens(){
        String res = "";
        Object[] tokens = getAllToken();
        for(int i = 0; i < tokens.length; i++)
            res += tokens[i] + ": :" + tokenMap.get(tokens[i]) + "_ _";
        return res;
    }

    public String toString(){
        String res = "";
        // res += "file id: " + String.valueOf(fileId) + " path:" + filePath + "\n";
        res += "bag id: " + String.valueOf(bagId) + "\n";
        res += "lines: " + getPosition() + '\n';
        res += getTokens() + '\n';
        return res;
    }

    public String outputBag(){
        String res = "";
        String separator = "@ @";
        res += String.valueOf(projectId) + separator;
        res += String.valueOf(fileId) + separator + String.valueOf(bagId) + separator;
        res += String.valueOf(granularity) + separator;
        res += String.valueOf(num_keywords) + separator;
        res += String.valueOf(symbolNum) + separator;
        res += String.valueOf(tokenNum) + separator;
        res += getPosition() + separator;
        res += getTokens() + "\n";
        return res;
    }

    // Each instance of TokenBag contains a bag of tokens, which is a HashMap<String, Integer> tokenMap
    // Now generate a function to calculate the similarity between two TokenBags
    // The similarity is defined as the number of common tokens divided by the larger size of two bags
    // The function takes two TokenBags as input and returns a double value
    public double OverlapSimilarity(TokenBag bag2){
        int commonTokens = 0;
        String[] tokens1 = this.getAllToken();
        String[] tokens2 = bag2.getAllToken();
        for(int i = 0; i < tokens1.length; i++){
            if(bag2.tokenMap.containsKey(tokens1[i])){
                commonTokens += Math.min(this.tokenMap.get(tokens1[i]), bag2.tokenMap.get(tokens1[i]));
            }
        }

        if (this.tokenNum >= bag2.tokenNum){
            return (double)commonTokens / (double)this.tokenNum;
        }else{
            return (double)commonTokens / (double)this.tokenNum;
        }
    }
  
    
    // Each instance of TokenBag contains a sequence of tokens, which is a LinkedList<String> tokenSequence
    // Now generate a function to calculate the LCS similarity between two token sequences from two TokenBags
    // The similarity is defined as the length of the longest common subsequence divided by the larger size of two sequences
    // The function takes two TokenBags as input and returns a double value
    public double LCSSimilarity(TokenBag bag2){
        int[][] dp = new int[this.tokenSequence.size() + 1][bag2.tokenSequence.size() + 1];
        for(int i = 0; i < this.tokenSequence.size(); i++){
            for(int j = 0; j < bag2.tokenSequence.size(); j++){
                if(this.tokenSequence.get(i).equals(bag2.tokenSequence.get(j))){
                    dp[i + 1][j + 1] = dp[i][j] + 1;
                }else{
                    dp[i + 1][j + 1] = Math.max(dp[i][j + 1], dp[i + 1][j]);
                }
            }
        }
        return (double)dp[this.tokenSequence.size()][bag2.tokenSequence.size()] / (double)Math.max(this.tokenSequence.size(), bag2.tokenSequence.size());
    }






    // projectId @@ fileId @@ bagId @@ granularity @@ num_keywords @@ symbolN @@ tokenN @@ startline -- endline @@ tokens...........

    // public static void main(String args[]){
    //     TokenBag test = new TokenBag(0, 0, 0, 0);

    //     String a = "/";
    //     System.out.println(a);
    //     System.out.println(test.removeEnter(a));
    //     System.out.println(test.removeEnter(a));
    // }
}