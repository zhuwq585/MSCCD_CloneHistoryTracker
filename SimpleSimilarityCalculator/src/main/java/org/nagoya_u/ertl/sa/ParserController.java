package org.nagoya_u.ertl.sa;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.List;
import java.util.regex.Pattern;

import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.tree.*;
import org.nagoya_u.ertl.sa.parser.*;

public class ParserController { 
    static private String REGEX_OPR = "[^0-9a-zA-Z]+";

    public ParseTree pTree;
    public List<Token> lexicalUnits;
    ParserController(){  } 
     
    public boolean run(String filePath){
        try{
            if (Files.lines(Paths.get(filePath)).count() > 10000){ 
                System.out.println("too big file. ");
                return false;
            }
            CharStream input = CharStreams.fromFileName(filePath);
            CPP14Lexer lexer = new CPP14Lexer(input);

            CommonTokenStream tokens = new CommonTokenStream(lexer);

            tokens.getNumberOfOnChannelTokens();

            CPP14Parser parser = new CPP14Parser(tokens);

            ParseTree tree = parser.translationUnit();
            pTree = tree;
            lexicalUnits = tokens.getTokens();
        }catch (Exception e){ 
            System.out.println("File not found.");
            return false;
        }
        return true;
    }
    
    public ParseTree getPTree(){
        return pTree;
    }
    
    public List<Token> getLexicalUnits(){
        return lexicalUnits;
    }
    public void reset(){
        pTree  = null;
        lexicalUnits = null;
    }

    TokenBag generateTokenBagByLinePosition(String filePath, int startLine, int endLine, KeywordsSet kSet){
        if (this.run(filePath)){
            TokenBag res = new TokenBag(-1, -1, startLine, endLine);
            int tokenType ;
            for (Token commonToken : this.lexicalUnits){
                if (commonToken.getLine() < startLine || commonToken.getLine() > endLine)
                    continue;


                String tokenText = commonToken.getText();
                tokenType = this.getTokenType(tokenText, kSet );
                if (tokenType == 1){
                    res.addToken(tokenText);
                    res.addTokenToSequence(tokenText);
                }
                else if(tokenType == 3){
                    res.addTokenToSequence(tokenText);
                    Pattern p = Pattern.compile("\\W+");
                    String[] splitedToken = p.split(tokenText);
                    for(int i = 0; i < splitedToken.length; i++){
                        res.addToken(splitedToken[i]);
                    }
                }
            }
            return res;
        }
        return null;
    }


    private int getTokenType(String str, KeywordsSet kSet){ // 0other 1keyword 3identify or literial
        if (str == null)
            return 0;
            
        if(Pattern.matches(REGEX_OPR, str)) // operators and other separator charactors
            return 0;
        else if ( kSet.checkKeywords(str) ) // keyword
            return 1;
        else
            return 3;
    }
}