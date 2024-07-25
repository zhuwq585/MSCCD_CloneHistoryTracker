// Generated from /Users/syu/workspace/MSCCD_CloneHistoryTracker/ErLangFuncExtract/Erlang.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast", "CheckReturnValue"})
public class ErlangParser extends Parser {
	static { RuntimeMetaData.checkVersion("4.13.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		T__0=1, T__1=2, T__2=3, T__3=4, T__4=5, T__5=6, T__6=7, T__7=8, T__8=9, 
		T__9=10, T__10=11, T__11=12, T__12=13, T__13=14, T__14=15, T__15=16, T__16=17, 
		T__17=18, T__18=19, T__19=20, T__20=21, T__21=22, T__22=23, T__23=24, 
		T__24=25, T__25=26, T__26=27, T__27=28, T__28=29, T__29=30, T__30=31, 
		T__31=32, T__32=33, T__33=34, T__34=35, T__35=36, T__36=37, T__37=38, 
		T__38=39, T__39=40, T__40=41, T__41=42, T__42=43, T__43=44, T__44=45, 
		T__45=46, T__46=47, T__47=48, T__48=49, T__49=50, T__50=51, T__51=52, 
		T__52=53, T__53=54, T__54=55, T__55=56, T__56=57, T__57=58, T__58=59, 
		T__59=60, T__60=61, T__61=62, T__62=63, T__63=64, TokAtom=65, TokVar=66, 
		TokFloat=67, TokInteger=68, TokChar=69, TokString=70, AttrName=71, Comment=72, 
		WS=73;
	public static final int
		RULE_forms = 0, RULE_form = 1, RULE_tokAtom = 2, RULE_tokVar = 3, RULE_tokFloat = 4, 
		RULE_tokInteger = 5, RULE_tokChar = 6, RULE_tokString = 7, RULE_attribute = 8, 
		RULE_typeSpec = 9, RULE_specFun = 10, RULE_typedAttrVal = 11, RULE_typedRecordFields = 12, 
		RULE_typedExprs = 13, RULE_typedExpr = 14, RULE_typeSigs = 15, RULE_typeSig = 16, 
		RULE_typeGuards = 17, RULE_typeGuard = 18, RULE_topTypes = 19, RULE_topType = 20, 
		RULE_topType100 = 21, RULE_type200 = 22, RULE_type300 = 23, RULE_type400 = 24, 
		RULE_type500 = 25, RULE_re_type = 26, RULE_funType100 = 27, RULE_funType = 28, 
		RULE_mapPairTypes = 29, RULE_mapPairType = 30, RULE_fieldTypes = 31, RULE_fieldType = 32, 
		RULE_binaryType = 33, RULE_binBaseType = 34, RULE_binUnitType = 35, RULE_attrVal = 36, 
		RULE_function_ = 37, RULE_functionClause = 38, RULE_clauseArgs = 39, RULE_clauseGuard = 40, 
		RULE_clauseBody = 41, RULE_expr = 42, RULE_expr100 = 43, RULE_expr150 = 44, 
		RULE_expr160 = 45, RULE_expr200 = 46, RULE_expr300 = 47, RULE_expr400 = 48, 
		RULE_expr500 = 49, RULE_expr600 = 50, RULE_expr650 = 51, RULE_expr700 = 52, 
		RULE_expr800 = 53, RULE_exprMax = 54, RULE_patExpr = 55, RULE_patExpr200 = 56, 
		RULE_patExpr300 = 57, RULE_patExpr400 = 58, RULE_patExpr500 = 59, RULE_patExpr600 = 60, 
		RULE_patExpr650 = 61, RULE_patExpr700 = 62, RULE_patExpr800 = 63, RULE_patExprMax = 64, 
		RULE_mapPatExpr = 65, RULE_recordPatExpr = 66, RULE_re_list = 67, RULE_tail = 68, 
		RULE_binary = 69, RULE_binElements = 70, RULE_binElement = 71, RULE_bitExpr = 72, 
		RULE_optBitSizeExpr = 73, RULE_optBitTypeList = 74, RULE_bitTypeList = 75, 
		RULE_bitType = 76, RULE_bitSizeExpr = 77, RULE_listComprehension = 78, 
		RULE_binaryComprehension = 79, RULE_lcExprs = 80, RULE_lcExpr = 81, RULE_re_tuple = 82, 
		RULE_mapExpr = 83, RULE_mapTuple = 84, RULE_mapField = 85, RULE_mapFieldAssoc = 86, 
		RULE_mapFieldExact = 87, RULE_mapKey = 88, RULE_recordExpr = 89, RULE_recordTuple = 90, 
		RULE_recordFields = 91, RULE_recordField = 92, RULE_functionCall = 93, 
		RULE_ifExpr = 94, RULE_ifClauses = 95, RULE_ifClause = 96, RULE_caseExpr = 97, 
		RULE_crClauses = 98, RULE_crClause = 99, RULE_receiveExpr = 100, RULE_funExpr = 101, 
		RULE_atomOrVar = 102, RULE_integerOrVar = 103, RULE_funClauses = 104, 
		RULE_funClause = 105, RULE_tryExpr = 106, RULE_tryCatch = 107, RULE_tryClauses = 108, 
		RULE_tryClause = 109, RULE_tryOptStackTrace = 110, RULE_argumentList = 111, 
		RULE_patArgumentList = 112, RULE_exprs = 113, RULE_patExprs = 114, RULE_guard = 115, 
		RULE_atomic = 116, RULE_prefixOp = 117, RULE_multOp = 118, RULE_addOp = 119, 
		RULE_listOp = 120, RULE_compOp = 121;
	private static String[] makeRuleNames() {
		return new String[] {
			"forms", "form", "tokAtom", "tokVar", "tokFloat", "tokInteger", "tokChar", 
			"tokString", "attribute", "typeSpec", "specFun", "typedAttrVal", "typedRecordFields", 
			"typedExprs", "typedExpr", "typeSigs", "typeSig", "typeGuards", "typeGuard", 
			"topTypes", "topType", "topType100", "type200", "type300", "type400", 
			"type500", "re_type", "funType100", "funType", "mapPairTypes", "mapPairType", 
			"fieldTypes", "fieldType", "binaryType", "binBaseType", "binUnitType", 
			"attrVal", "function_", "functionClause", "clauseArgs", "clauseGuard", 
			"clauseBody", "expr", "expr100", "expr150", "expr160", "expr200", "expr300", 
			"expr400", "expr500", "expr600", "expr650", "expr700", "expr800", "exprMax", 
			"patExpr", "patExpr200", "patExpr300", "patExpr400", "patExpr500", "patExpr600", 
			"patExpr650", "patExpr700", "patExpr800", "patExprMax", "mapPatExpr", 
			"recordPatExpr", "re_list", "tail", "binary", "binElements", "binElement", 
			"bitExpr", "optBitSizeExpr", "optBitTypeList", "bitTypeList", "bitType", 
			"bitSizeExpr", "listComprehension", "binaryComprehension", "lcExprs", 
			"lcExpr", "re_tuple", "mapExpr", "mapTuple", "mapField", "mapFieldAssoc", 
			"mapFieldExact", "mapKey", "recordExpr", "recordTuple", "recordFields", 
			"recordField", "functionCall", "ifExpr", "ifClauses", "ifClause", "caseExpr", 
			"crClauses", "crClause", "receiveExpr", "funExpr", "atomOrVar", "integerOrVar", 
			"funClauses", "funClause", "tryExpr", "tryCatch", "tryClauses", "tryClause", 
			"tryOptStackTrace", "argumentList", "patArgumentList", "exprs", "patExprs", 
			"guard", "atomic", "prefixOp", "multOp", "addOp", "listOp", "compOp"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'.'", "'-'", "'('", "')'", "':'", "','", "'::'", "'{'", "'}'", 
			"';'", "'when'", "'|'", "'..'", "'['", "']'", "'...'", "'#'", "'fun'", 
			"'->'", "'=>'", "':='", "'<<'", "'>>'", "'*'", "'catch'", "'='", "'!'", 
			"'orelse'", "'andalso'", "'begin'", "'end'", "'/'", "'||'", "'<-'", "'<='", 
			"'if'", "'case'", "'of'", "'receive'", "'after'", "'try'", "'+'", "'bnot'", 
			"'not'", "'div'", "'rem'", "'band'", "'and'", "'bor'", "'bxor'", "'bsl'", 
			"'bsr'", "'or'", "'xor'", "'++'", "'--'", "'=='", "'/='", "'=<'", "'<'", 
			"'>='", "'>'", "'=:='", "'=/='"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, null, null, null, null, null, null, null, null, null, null, null, 
			null, null, null, null, null, null, null, null, null, null, null, null, 
			null, null, null, null, null, null, null, null, null, null, null, null, 
			null, null, null, null, null, null, null, null, null, null, null, null, 
			null, null, null, null, null, null, null, null, null, null, null, null, 
			null, null, null, null, null, "TokAtom", "TokVar", "TokFloat", "TokInteger", 
			"TokChar", "TokString", "AttrName", "Comment", "WS"
		};
	}
	private static final String[] _SYMBOLIC_NAMES = makeSymbolicNames();
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}

	@Override
	public String getGrammarFileName() { return "Erlang.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public ErlangParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@SuppressWarnings("CheckReturnValue")
	public static class FormsContext extends ParserRuleContext {
		public TerminalNode EOF() { return getToken(ErlangParser.EOF, 0); }
		public List<FormContext> form() {
			return getRuleContexts(FormContext.class);
		}
		public FormContext form(int i) {
			return getRuleContext(FormContext.class,i);
		}
		public FormsContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_forms; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof ErlangListener ) ((ErlangListener)listener).enterForms(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof ErlangListener ) ((ErlangListener)listener).exitForms(this);
		}
	}

	public final FormsContext forms() throws RecognitionException {
		FormsContext _localctx = new FormsContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_forms);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(245); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				{
				setState(244);
				form();
				}
				}
				setState(247); 
				_errHandler.sync(this);
				_la = _input.LA(1);
			} while ( _la==T__1 || _la==TokAtom || _la==AttrName );
			setState(249);
			match(EOF);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class FormContext extends ParserRuleContext {
		public AttributeContext attribute() {
			return getRuleContext(AttributeContext.class,0);
		}
		public Function_Context function_() {
			return getRuleContext(Function_Context.class,0);
		}
		public FormContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_form; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof ErlangListener ) ((ErlangListener)listener).enterForm(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof ErlangListener ) ((ErlangListener)listener).exitForm(this);
		}
	}

	public final FormContext form() throws RecognitionException {
		FormContext _localctx = new FormContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_form);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(253);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case T__1:
			case AttrName:
				{
				setState(251);
				attribute();
				}
				break;
			case TokAtom:
				{
				setState(252);
				function_();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
			setState(255);
			match(T__0);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class TokAtomContext extends ParserRuleContext {
		public TerminalNode TokAtom() { return getToken(ErlangParser.TokAtom, 0); }
		public TokAtomContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_tokAtom; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof ErlangListener ) ((ErlangListener)listener).enterTokAtom(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof ErlangListener ) ((ErlangListener)listener).exitTokAtom(this);
		}
	}

	public final TokAtomContext tokAtom() throws RecognitionException {
		TokAtomContext _localctx = new TokAtomContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_tokAtom);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(257);
			match(TokAtom);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class TokVarContext extends ParserRuleContext {
		public TerminalNode TokVar() { return getToken(ErlangParser.TokVar, 0); }
		public TokVarContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_tokVar; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof ErlangListener ) ((ErlangListener)listener).enterTokVar(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof ErlangListener ) ((ErlangListener)listener).exitTokVar(this);
		}
	}

	public final TokVarContext tokVar() throws RecognitionException {
		TokVarContext _localctx = new TokVarContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_tokVar);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(259);
			match(TokVar);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class TokFloatContext extends ParserRuleContext {
		public TerminalNode TokFloat() { return getToken(ErlangParser.TokFloat, 0); }
		public TokFloatContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_tokFloat; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof ErlangListener ) ((ErlangListener)listener).enterTokFloat(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof ErlangListener ) ((ErlangListener)listener).exitTokFloat(this);
		}
	}

	public final TokFloatContext tokFloat() throws RecognitionException {
		TokFloatContext _localctx = new TokFloatContext(_ctx, getState());
		enterRule(_localctx, 8, RULE_tokFloat);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(261);
			match(TokFloat);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class TokIntegerContext extends ParserRuleContext {
		public TerminalNode TokInteger() { return getToken(ErlangParser.TokInteger, 0); }
		public TokIntegerContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_tokInteger; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof ErlangListener ) ((ErlangListener)listener).enterTokInteger(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof ErlangListener ) ((ErlangListener)listener).exitTokInteger(this);
		}
	}

	public final TokIntegerContext tokInteger() throws RecognitionException {
		TokIntegerContext _localctx = new TokIntegerContext(_ctx, getState());
		enterRule(_localctx, 10, RULE_tokInteger);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(263);
			match(TokInteger);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class TokCharContext extends ParserRuleContext {
		public TerminalNode TokChar() { return getToken(ErlangParser.TokChar, 0); }
		public TokCharContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_tokChar; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof ErlangListener ) ((ErlangListener)listener).enterTokChar(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof ErlangListener ) ((ErlangListener)listener).exitTokChar(this);
		}
	}

	public final TokCharContext tokChar() throws RecognitionException {
		TokCharContext _localctx = new TokCharContext(_ctx, getState());
		enterRule(_localctx, 12, RULE_tokChar);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(265);
			match(TokChar);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class TokStringContext extends ParserRuleContext {
		public TerminalNode TokString() { return getToken(ErlangParser.TokString, 0); }
		public TokStringContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_tokString; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof ErlangListener ) ((ErlangListener)listener).enterTokString(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof ErlangListener ) ((ErlangListener)listener).exitTokString(this);
		}
	}

	public final TokStringContext tokString() throws RecognitionException {
		TokStringContext _localctx = new TokStringContext(_ctx, getState());
		enterRule(_localctx, 14, RULE_tokString);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(267);
			match(TokString);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class AttributeContext extends ParserRuleContext {
		public TokAtomContext tokAtom() {
			return getRuleContext(TokAtomContext.class,0);
		}
		public AttrValContext attrVal() {
			return getRuleContext(AttrValContext.class,0);
		}
		public TypedAttrValContext typedAttrVal() {
			return getRuleContext(TypedAttrValContext.class,0);
		}
		public TerminalNode AttrName() { return getToken(ErlangParser.AttrName, 0); }
		public TypeSpecContext typeSpec() {
			return getRuleContext(TypeSpecContext.class,0);
		}
		public AttributeContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_attribute; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof ErlangListener ) ((ErlangListener)listener).enterAttribute(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof ErlangListener ) ((ErlangListener)listener).exitAttribute(this);
		}
	}

	public final AttributeContext attribute() throws RecognitionException {
		AttributeContext _localctx = new AttributeContext(_ctx, getState());
		enterRule(_localctx, 16, RULE_attribute);
		try {
			setState(285);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,2,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(269);
				match(T__1);
				setState(270);
				tokAtom();
				setState(271);
				attrVal();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(273);
				match(T__1);
				setState(274);
				tokAtom();
				setState(275);
				typedAttrVal();
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(277);
				match(T__1);
				setState(278);
				tokAtom();
				setState(279);
				match(T__2);
				setState(280);
				typedAttrVal();
				setState(281);
				match(T__3);
				}
				break;
			case 4:
				enterOuterAlt(_localctx, 4);
				{
				setState(283);
				match(AttrName);
				setState(284);
				typeSpec();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class TypeSpecContext extends ParserRuleContext {
		public SpecFunContext specFun() {
			return getRuleContext(SpecFunContext.class,0);
		}
		public TypeSigsContext typeSigs() {
			return getRuleContext(TypeSigsContext.class,0);
		}
		public TypeSpecContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_typeSpec; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof ErlangListener ) ((ErlangListener)listener).enterTypeSpec(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof ErlangListener ) ((ErlangListener)listener).exitTypeSpec(this);
		}
	}

	public final TypeSpecContext typeSpec() throws RecognitionException {
		TypeSpecContext _localctx = new TypeSpecContext(_ctx, getState());
		enterRule(_localctx, 18, RULE_typeSpec);
		try {
			setState(295);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case TokAtom:
				enterOuterAlt(_localctx, 1);
				{
				setState(287);
				specFun();
				setState(288);
				typeSigs();
				}
				break;
			case T__2:
				enterOuterAlt(_localctx, 2);
				{
				setState(290);
				match(T__2);
				setState(291);
				specFun();
				setState(292);
				typeSigs();
				setState(293);
				match(T__3);
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class SpecFunContext extends ParserRuleContext {
		public List<TokAtomContext> tokAtom() {
			return getRuleContexts(TokAtomContext.class);
		}
		public TokAtomContext tokAtom(int i) {
			return getRuleContext(TokAtomContext.class,i);
		}
		public SpecFunContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_specFun; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof ErlangListener ) ((ErlangListener)listener).enterSpecFun(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof ErlangListener ) ((ErlangListener)listener).exitSpecFun(this);
		}
	}

	public final SpecFunContext specFun() throws RecognitionException {
		SpecFunContext _localctx = new SpecFunContext(_ctx, getState());
		enterRule(_localctx, 20, RULE_specFun);
		try {
			setState(302);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,4,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(297);
				tokAtom();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(298);
				tokAtom();
				setState(299);
				match(T__4);
				setState(300);
				tokAtom();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class TypedAttrValContext extends ParserRuleContext {
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public TypedRecordFieldsContext typedRecordFields() {
			return getRuleContext(TypedRecordFieldsContext.class,0);
		}
		public TopTypeContext topType() {
			return getRuleContext(TopTypeContext.class,0);
		}
		public TypedAttrValContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_typedAttrVal; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof ErlangListener ) ((ErlangListener)listener).enterTypedAttrVal(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof ErlangListener ) ((ErlangListener)listener).exitTypedAttrVal(this);
		}
	}

	public final TypedAttrValContext typedAttrVal() throws RecognitionException {
		TypedAttrValContext _localctx = new TypedAttrValContext(_ctx, getState());
		enterRule(_localctx, 22, RULE_typedAttrVal);
		try {
			setState(312);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,5,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(304);
				expr();
				setState(305);
				match(T__5);
				setState(306);
				typedRecordFields();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(308);
				expr();
				setState(309);
				match(T__6);
				setState(310);
				topType();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class TypedRecordFieldsContext extends ParserRuleContext {
		public TypedExprsContext typedExprs() {
			return getRuleContext(TypedExprsContext.class,0);
		}
		public TypedRecordFieldsContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_typedRecordFields; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof ErlangListener ) ((ErlangListener)listener).enterTypedRecordFields(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof ErlangListener ) ((ErlangListener)listener).exitTypedRecordFields(this);
		}
	}

	public final TypedRecordFieldsContext typedRecordFields() throws RecognitionException {
		TypedRecordFieldsContext _localctx = new TypedRecordFieldsContext(_ctx, getState());
		enterRule(_localctx, 24, RULE_typedRecordFields);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(314);
			match(T__7);
			setState(315);
			typedExprs();
			setState(316);
			match(T__8);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class TypedExprsContext extends ParserRuleContext {
		public TypedExprContext typedExpr() {
			return getRuleContext(TypedExprContext.class,0);
		}
		public TypedExprsContext typedExprs() {
			return getRuleContext(TypedExprsContext.class,0);
		}
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public ExprsContext exprs() {
			return getRuleContext(ExprsContext.class,0);
		}
		public TypedExprsContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_typedExprs; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof ErlangListener ) ((ErlangListener)listener).enterTypedExprs(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof ErlangListener ) ((ErlangListener)listener).exitTypedExprs(this);
		}
	}

	public final TypedExprsContext typedExprs() throws RecognitionException {
		TypedExprsContext _localctx = new TypedExprsContext(_ctx, getState());
		enterRule(_localctx, 26, RULE_typedExprs);
		try {
			setState(331);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,6,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(318);
				typedExpr();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(319);
				typedExpr();
				setState(320);
				match(T__5);
				setState(321);
				typedExprs();
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(323);
				expr();
				setState(324);
				match(T__5);
				setState(325);
				typedExprs();
				}
				break;
			case 4:
				enterOuterAlt(_localctx, 4);
				{
				setState(327);
				typedExpr();
				setState(328);
				match(T__5);
				setState(329);
				exprs();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class TypedExprContext extends ParserRuleContext {
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public TopTypeContext topType() {
			return getRuleContext(TopTypeContext.class,0);
		}
		public TypedExprContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_typedExpr; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof ErlangListener ) ((ErlangListener)listener).enterTypedExpr(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof ErlangListener ) ((ErlangListener)listener).exitTypedExpr(this);
		}
	}

	public final TypedExprContext typedExpr() throws RecognitionException {
		TypedExprContext _localctx = new TypedExprContext(_ctx, getState());
		enterRule(_localctx, 28, RULE_typedExpr);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(333);
			expr();
			setState(334);
			match(T__6);
			setState(335);
			topType();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class TypeSigsContext extends ParserRuleContext {
		public List<TypeSigContext> typeSig() {
			return getRuleContexts(TypeSigContext.class);
		}
		public TypeSigContext typeSig(int i) {
			return getRuleContext(TypeSigContext.class,i);
		}
		public TypeSigsContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_typeSigs; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof ErlangListener ) ((ErlangListener)listener).enterTypeSigs(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof ErlangListener ) ((ErlangListener)listener).exitTypeSigs(this);
		}
	}

	public final TypeSigsContext typeSigs() throws RecognitionException {
		TypeSigsContext _localctx = new TypeSigsContext(_ctx, getState());
		enterRule(_localctx, 30, RULE_typeSigs);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(337);
			typeSig();
			setState(342);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==T__9) {
				{
				{
				setState(338);
				match(T__9);
				setState(339);
				typeSig();
				}
				}
				setState(344);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class TypeSigContext extends ParserRuleContext {
		public FunTypeContext funType() {
			return getRuleContext(FunTypeContext.class,0);
		}
		public TypeGuardsContext typeGuards() {
			return getRuleContext(TypeGuardsContext.class,0);
		}
		public TypeSigContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_typeSig; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof ErlangListener ) ((ErlangListener)listener).enterTypeSig(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof ErlangListener ) ((ErlangListener)listener).exitTypeSig(this);
		}
	}

	public final TypeSigContext typeSig() throws RecognitionException {
		TypeSigContext _localctx = new TypeSigContext(_ctx, getState());
		enterRule(_localctx, 32, RULE_typeSig);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(345);
			funType();
			setState(348);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==T__10) {
				{
				setState(346);
				match(T__10);
				setState(347);
				typeGuards();
				}
			}

			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class TypeGuardsContext extends ParserRuleContext {
		public List<TypeGuardContext> typeGuard() {
			return getRuleContexts(TypeGuardContext.class);
		}
		public TypeGuardContext typeGuard(int i) {
			return getRuleContext(TypeGuardContext.class,i);
		}
		public TypeGuardsContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_typeGuards; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof ErlangListener ) ((ErlangListener)listener).enterTypeGuards(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof ErlangListener ) ((ErlangListener)listener).exitTypeGuards(this);
		}
	}

	public final TypeGuardsContext typeGuards() throws RecognitionException {
		TypeGuardsContext _localctx = new TypeGuardsContext(_ctx, getState());
		enterRule(_localctx, 34, RULE_typeGuards);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(350);
			typeGuard();
			setState(355);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==T__5) {
				{
				{
				setState(351);
				match(T__5);
				setState(352);
				typeGuard();
				}
				}
				setState(357);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class TypeGuardContext extends ParserRuleContext {
		public TokAtomContext tokAtom() {
			return getRuleContext(TokAtomContext.class,0);
		}
		public TopTypesContext topTypes() {
			return getRuleContext(TopTypesContext.class,0);
		}
		public TokVarContext tokVar() {
			return getRuleContext(TokVarContext.class,0);
		}
		public TopTypeContext topType() {
			return getRuleContext(TopTypeContext.class,0);
		}
		public TypeGuardContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_typeGuard; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof ErlangListener ) ((ErlangListener)listener).enterTypeGuard(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof ErlangListener ) ((ErlangListener)listener).exitTypeGuard(this);
		}
	}

	public final TypeGuardContext typeGuard() throws RecognitionException {
		TypeGuardContext _localctx = new TypeGuardContext(_ctx, getState());
		enterRule(_localctx, 36, RULE_typeGuard);
		try {
			setState(367);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case TokAtom:
				enterOuterAlt(_localctx, 1);
				{
				setState(358);
				tokAtom();
				setState(359);
				match(T__2);
				setState(360);
				topTypes();
				setState(361);
				match(T__3);
				}
				break;
			case TokVar:
				enterOuterAlt(_localctx, 2);
				{
				setState(363);
				tokVar();
				setState(364);
				match(T__6);
				setState(365);
				topType();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class TopTypesContext extends ParserRuleContext {
		public List<TopTypeContext> topType() {
			return getRuleContexts(TopTypeContext.class);
		}
		public TopTypeContext topType(int i) {
			return getRuleContext(TopTypeContext.class,i);
		}
		public TopTypesContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_topTypes; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof ErlangListener ) ((ErlangListener)listener).enterTopTypes(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof ErlangListener ) ((ErlangListener)listener).exitTopTypes(this);
		}
	}

	public final TopTypesContext topTypes() throws RecognitionException {
		TopTypesContext _localctx = new TopTypesContext(_ctx, getState());
		enterRule(_localctx, 38, RULE_topTypes);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(369);
			topType();
			setState(374);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==T__5) {
				{
				{
				setState(370);
				match(T__5);
				setState(371);
				topType();
				}
				}
				setState(376);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class TopTypeContext extends ParserRuleContext {
		public TopType100Context topType100() {
			return getRuleContext(TopType100Context.class,0);
		}
		public TokVarContext tokVar() {
			return getRuleContext(TokVarContext.class,0);
		}
		public TopTypeContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_topType; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof ErlangListener ) ((ErlangListener)listener).enterTopType(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof ErlangListener ) ((ErlangListener)listener).exitTopType(this);
		}
	}

	public final TopTypeContext topType() throws RecognitionException {
		TopTypeContext _localctx = new TopTypeContext(_ctx, getState());
		enterRule(_localctx, 40, RULE_topType);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(380);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,12,_ctx) ) {
			case 1:
				{
				setState(377);
				tokVar();
				setState(378);
				match(T__6);
				}
				break;
			}
			setState(382);
			topType100();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class TopType100Context extends ParserRuleContext {
		public Type200Context type200() {
			return getRuleContext(Type200Context.class,0);
		}
		public TopType100Context topType100() {
			return getRuleContext(TopType100Context.class,0);
		}
		public TopType100Context(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_topType100; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof ErlangListener ) ((ErlangListener)listener).enterTopType100(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof ErlangListener ) ((ErlangListener)listener).exitTopType100(this);
		}
	}

	public final TopType100Context topType100() throws RecognitionException {
		TopType100Context _localctx = new TopType100Context(_ctx, getState());
		enterRule(_localctx, 42, RULE_topType100);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(384);
			type200();
			setState(387);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==T__11) {
				{
				setState(385);
				match(T__11);
				setState(386);
				topType100();
				}
			}

			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Type200Context extends ParserRuleContext {
		public List<Type300Context> type300() {
			return getRuleContexts(Type300Context.class);
		}
		public Type300Context type300(int i) {
			return getRuleContext(Type300Context.class,i);
		}
		public Type200Context(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_type200; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof ErlangListener ) ((ErlangListener)listener).enterType200(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof ErlangListener ) ((ErlangListener)listener).exitType200(this);
		}
	}

	public final Type200Context type200() throws RecognitionException {
		Type200Context _localctx = new Type200Context(_ctx, getState());
		enterRule(_localctx, 44, RULE_type200);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(389);
			type300(0);
			setState(392);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==T__12) {
				{
				setState(390);
				match(T__12);
				setState(391);
				type300(0);
				}
			}

			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Type300Context extends ParserRuleContext {
		public Type400Context type400() {
			return getRuleContext(Type400Context.class,0);
		}
		public Type300Context type300() {
			return getRuleContext(Type300Context.class,0);
		}
		public AddOpContext addOp() {
			return getRuleContext(AddOpContext.class,0);
		}
		public Type300Context(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_type300; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof ErlangListener ) ((ErlangListener)listener).enterType300(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof ErlangListener ) ((ErlangListener)listener).exitType300(this);
		}
	}

	public final Type300Context type300() throws RecognitionException {
		return type300(0);
	}

	private Type300Context type300(int _p) throws RecognitionException {
		ParserRuleContext _parentctx = _ctx;
		int _parentState = getState();
		Type300Context _localctx = new Type300Context(_ctx, _parentState);
		Type300Context _prevctx = _localctx;
		int _startState = 46;
		enterRecursionRule(_localctx, 46, RULE_type300, _p);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			{
			setState(395);
			type400(0);
			}
			_ctx.stop = _input.LT(-1);
			setState(403);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,15,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					{
					_localctx = new Type300Context(_parentctx, _parentState);
					pushNewRecursionContext(_localctx, _startState, RULE_type300);
					setState(397);
					if (!(precpred(_ctx, 2))) throw new FailedPredicateException(this, "precpred(_ctx, 2)");
					setState(398);
					addOp();
					setState(399);
					type400(0);
					}
					} 
				}
				setState(405);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,15,_ctx);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			unrollRecursionContexts(_parentctx);
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Type400Context extends ParserRuleContext {
		public Type500Context type500() {
			return getRuleContext(Type500Context.class,0);
		}
		public Type400Context type400() {
			return getRuleContext(Type400Context.class,0);
		}
		public MultOpContext multOp() {
			return getRuleContext(MultOpContext.class,0);
		}
		public Type400Context(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_type400; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof ErlangListener ) ((ErlangListener)listener).enterType400(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof ErlangListener ) ((ErlangListener)listener).exitType400(this);
		}
	}

	public final Type400Context type400() throws RecognitionException {
		return type400(0);
	}

	private Type400Context type400(int _p) throws RecognitionException {
		ParserRuleContext _parentctx = _ctx;
		int _parentState = getState();
		Type400Context _localctx = new Type400Context(_ctx, _parentState);
		Type400Context _prevctx = _localctx;
		int _startState = 48;
		enterRecursionRule(_localctx, 48, RULE_type400, _p);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			{
			setState(407);
			type500();
			}
			_ctx.stop = _input.LT(-1);
			setState(415);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,16,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					{
					_localctx = new Type400Context(_parentctx, _parentState);
					pushNewRecursionContext(_localctx, _startState, RULE_type400);
					setState(409);
					if (!(precpred(_ctx, 2))) throw new FailedPredicateException(this, "precpred(_ctx, 2)");
					setState(410);
					multOp();
					setState(411);
					type500();
					}
					} 
				}
				setState(417);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,16,_ctx);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			unrollRecursionContexts(_parentctx);
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Type500Context extends ParserRuleContext {
		public Re_typeContext re_type() {
			return getRuleContext(Re_typeContext.class,0);
		}
		public PrefixOpContext prefixOp() {
			return getRuleContext(PrefixOpContext.class,0);
		}
		public Type500Context(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_type500; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof ErlangListener ) ((ErlangListener)listener).enterType500(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof ErlangListener ) ((ErlangListener)listener).exitType500(this);
		}
	}

	public final Type500Context type500() throws RecognitionException {
		Type500Context _localctx = new Type500Context(_ctx, getState());
		enterRule(_localctx, 50, RULE_type500);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(419);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & 30786325577732L) != 0)) {
				{
				setState(418);
				prefixOp();
				}
			}

			setState(421);
			re_type();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Re_typeContext extends ParserRuleContext {
		public TopTypeContext topType() {
			return getRuleContext(TopTypeContext.class,0);
		}
		public TokVarContext tokVar() {
			return getRuleContext(TokVarContext.class,0);
		}
		public List<TokAtomContext> tokAtom() {
			return getRuleContexts(TokAtomContext.class);
		}
		public TokAtomContext tokAtom(int i) {
			return getRuleContext(TokAtomContext.class,i);
		}
		public TopTypesContext topTypes() {
			return getRuleContext(TopTypesContext.class,0);
		}
		public MapPairTypesContext mapPairTypes() {
			return getRuleContext(MapPairTypesContext.class,0);
		}
		public FieldTypesContext fieldTypes() {
			return getRuleContext(FieldTypesContext.class,0);
		}
		public BinaryTypeContext binaryType() {
			return getRuleContext(BinaryTypeContext.class,0);
		}
		public TokIntegerContext tokInteger() {
			return getRuleContext(TokIntegerContext.class,0);
		}
		public TokCharContext tokChar() {
			return getRuleContext(TokCharContext.class,0);
		}
		public FunType100Context funType100() {
			return getRuleContext(FunType100Context.class,0);
		}
		public Re_typeContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_re_type; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof ErlangListener ) ((ErlangListener)listener).enterRe_type(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof ErlangListener ) ((ErlangListener)listener).exitRe_type(this);
		}
	}

	public final Re_typeContext re_type() throws RecognitionException {
		Re_typeContext _localctx = new Re_typeContext(_ctx, getState());
		enterRule(_localctx, 52, RULE_re_type);
		try {
			setState(499);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,18,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(423);
				match(T__2);
				setState(424);
				topType();
				setState(425);
				match(T__3);
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(427);
				tokVar();
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(428);
				tokAtom();
				}
				break;
			case 4:
				enterOuterAlt(_localctx, 4);
				{
				setState(429);
				tokAtom();
				setState(430);
				match(T__2);
				setState(431);
				match(T__3);
				}
				break;
			case 5:
				enterOuterAlt(_localctx, 5);
				{
				setState(433);
				tokAtom();
				setState(434);
				match(T__2);
				setState(435);
				topTypes();
				setState(436);
				match(T__3);
				}
				break;
			case 6:
				enterOuterAlt(_localctx, 6);
				{
				setState(438);
				tokAtom();
				setState(439);
				match(T__4);
				setState(440);
				tokAtom();
				setState(441);
				match(T__2);
				setState(442);
				match(T__3);
				}
				break;
			case 7:
				enterOuterAlt(_localctx, 7);
				{
				setState(444);
				tokAtom();
				setState(445);
				match(T__4);
				setState(446);
				tokAtom();
				setState(447);
				match(T__2);
				setState(448);
				topTypes();
				setState(449);
				match(T__3);
				}
				break;
			case 8:
				enterOuterAlt(_localctx, 8);
				{
				setState(451);
				match(T__13);
				setState(452);
				match(T__14);
				}
				break;
			case 9:
				enterOuterAlt(_localctx, 9);
				{
				setState(453);
				match(T__13);
				setState(454);
				topType();
				setState(455);
				match(T__14);
				}
				break;
			case 10:
				enterOuterAlt(_localctx, 10);
				{
				setState(457);
				match(T__13);
				setState(458);
				topType();
				setState(459);
				match(T__5);
				setState(460);
				match(T__15);
				setState(461);
				match(T__14);
				}
				break;
			case 11:
				enterOuterAlt(_localctx, 11);
				{
				setState(463);
				match(T__16);
				setState(464);
				match(T__7);
				setState(465);
				match(T__8);
				}
				break;
			case 12:
				enterOuterAlt(_localctx, 12);
				{
				setState(466);
				match(T__16);
				setState(467);
				match(T__7);
				setState(468);
				mapPairTypes();
				setState(469);
				match(T__8);
				}
				break;
			case 13:
				enterOuterAlt(_localctx, 13);
				{
				setState(471);
				match(T__7);
				setState(472);
				match(T__8);
				}
				break;
			case 14:
				enterOuterAlt(_localctx, 14);
				{
				setState(473);
				match(T__7);
				setState(474);
				topTypes();
				setState(475);
				match(T__8);
				}
				break;
			case 15:
				enterOuterAlt(_localctx, 15);
				{
				setState(477);
				match(T__16);
				setState(478);
				tokAtom();
				setState(479);
				match(T__7);
				setState(480);
				match(T__8);
				}
				break;
			case 16:
				enterOuterAlt(_localctx, 16);
				{
				setState(482);
				match(T__16);
				setState(483);
				tokAtom();
				setState(484);
				match(T__7);
				setState(485);
				fieldTypes();
				setState(486);
				match(T__8);
				}
				break;
			case 17:
				enterOuterAlt(_localctx, 17);
				{
				setState(488);
				binaryType();
				}
				break;
			case 18:
				enterOuterAlt(_localctx, 18);
				{
				setState(489);
				tokInteger();
				}
				break;
			case 19:
				enterOuterAlt(_localctx, 19);
				{
				setState(490);
				tokChar();
				}
				break;
			case 20:
				enterOuterAlt(_localctx, 20);
				{
				setState(491);
				match(T__17);
				setState(492);
				match(T__2);
				setState(493);
				match(T__3);
				}
				break;
			case 21:
				enterOuterAlt(_localctx, 21);
				{
				setState(494);
				match(T__17);
				setState(495);
				match(T__2);
				setState(496);
				funType100();
				setState(497);
				match(T__3);
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class FunType100Context extends ParserRuleContext {
		public TopTypeContext topType() {
			return getRuleContext(TopTypeContext.class,0);
		}
		public FunTypeContext funType() {
			return getRuleContext(FunTypeContext.class,0);
		}
		public FunType100Context(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_funType100; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof ErlangListener ) ((ErlangListener)listener).enterFunType100(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof ErlangListener ) ((ErlangListener)listener).exitFunType100(this);
		}
	}

	public final FunType100Context funType100() throws RecognitionException {
		FunType100Context _localctx = new FunType100Context(_ctx, getState());
		enterRule(_localctx, 54, RULE_funType100);
		try {
			setState(507);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,19,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(501);
				match(T__2);
				setState(502);
				match(T__15);
				setState(503);
				match(T__3);
				setState(504);
				match(T__18);
				setState(505);
				topType();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(506);
				funType();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class FunTypeContext extends ParserRuleContext {
		public TopTypeContext topType() {
			return getRuleContext(TopTypeContext.class,0);
		}
		public TopTypesContext topTypes() {
			return getRuleContext(TopTypesContext.class,0);
		}
		public FunTypeContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_funType; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof ErlangListener ) ((ErlangListener)listener).enterFunType(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof ErlangListener ) ((ErlangListener)listener).exitFunType(this);
		}
	}

	public final FunTypeContext funType() throws RecognitionException {
		FunTypeContext _localctx = new FunTypeContext(_ctx, getState());
		enterRule(_localctx, 56, RULE_funType);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(509);
			match(T__2);
			setState(511);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & 30786330181900L) != 0) || ((((_la - 65)) & ~0x3f) == 0 && ((1L << (_la - 65)) & 27L) != 0)) {
				{
				setState(510);
				topTypes();
				}
			}

			setState(513);
			match(T__3);
			setState(514);
			match(T__18);
			setState(515);
			topType();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class MapPairTypesContext extends ParserRuleContext {
		public List<MapPairTypeContext> mapPairType() {
			return getRuleContexts(MapPairTypeContext.class);
		}
		public MapPairTypeContext mapPairType(int i) {
			return getRuleContext(MapPairTypeContext.class,i);
		}
		public MapPairTypesContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_mapPairTypes; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof ErlangListener ) ((ErlangListener)listener).enterMapPairTypes(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof ErlangListener ) ((ErlangListener)listener).exitMapPairTypes(this);
		}
	}

	public final MapPairTypesContext mapPairTypes() throws RecognitionException {
		MapPairTypesContext _localctx = new MapPairTypesContext(_ctx, getState());
		enterRule(_localctx, 58, RULE_mapPairTypes);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(517);
			mapPairType();
			setState(522);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==T__5) {
				{
				{
				setState(518);
				match(T__5);
				setState(519);
				mapPairType();
				}
				}
				setState(524);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class MapPairTypeContext extends ParserRuleContext {
		public List<TopTypeContext> topType() {
			return getRuleContexts(TopTypeContext.class);
		}
		public TopTypeContext topType(int i) {
			return getRuleContext(TopTypeContext.class,i);
		}
		public MapPairTypeContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_mapPairType; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof ErlangListener ) ((ErlangListener)listener).enterMapPairType(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof ErlangListener ) ((ErlangListener)listener).exitMapPairType(this);
		}
	}

	public final MapPairTypeContext mapPairType() throws RecognitionException {
		MapPairTypeContext _localctx = new MapPairTypeContext(_ctx, getState());
		enterRule(_localctx, 60, RULE_mapPairType);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(525);
			topType();
			setState(526);
			_la = _input.LA(1);
			if ( !(_la==T__19 || _la==T__20) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			setState(527);
			topType();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class FieldTypesContext extends ParserRuleContext {
		public List<FieldTypeContext> fieldType() {
			return getRuleContexts(FieldTypeContext.class);
		}
		public FieldTypeContext fieldType(int i) {
			return getRuleContext(FieldTypeContext.class,i);
		}
		public FieldTypesContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_fieldTypes; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof ErlangListener ) ((ErlangListener)listener).enterFieldTypes(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof ErlangListener ) ((ErlangListener)listener).exitFieldTypes(this);
		}
	}

	public final FieldTypesContext fieldTypes() throws RecognitionException {
		FieldTypesContext _localctx = new FieldTypesContext(_ctx, getState());
		enterRule(_localctx, 62, RULE_fieldTypes);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(529);
			fieldType();
			setState(534);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==T__5) {
				{
				{
				setState(530);
				match(T__5);
				setState(531);
				fieldType();
				}
				}
				setState(536);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class FieldTypeContext extends ParserRuleContext {
		public TokAtomContext tokAtom() {
			return getRuleContext(TokAtomContext.class,0);
		}
		public TopTypeContext topType() {
			return getRuleContext(TopTypeContext.class,0);
		}
		public FieldTypeContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_fieldType; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof ErlangListener ) ((ErlangListener)listener).enterFieldType(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof ErlangListener ) ((ErlangListener)listener).exitFieldType(this);
		}
	}

	public final FieldTypeContext fieldType() throws RecognitionException {
		FieldTypeContext _localctx = new FieldTypeContext(_ctx, getState());
		enterRule(_localctx, 64, RULE_fieldType);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(537);
			tokAtom();
			setState(538);
			match(T__6);
			setState(539);
			topType();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class BinaryTypeContext extends ParserRuleContext {
		public BinBaseTypeContext binBaseType() {
			return getRuleContext(BinBaseTypeContext.class,0);
		}
		public BinUnitTypeContext binUnitType() {
			return getRuleContext(BinUnitTypeContext.class,0);
		}
		public BinaryTypeContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_binaryType; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof ErlangListener ) ((ErlangListener)listener).enterBinaryType(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof ErlangListener ) ((ErlangListener)listener).exitBinaryType(this);
		}
	}

	public final BinaryTypeContext binaryType() throws RecognitionException {
		BinaryTypeContext _localctx = new BinaryTypeContext(_ctx, getState());
		enterRule(_localctx, 66, RULE_binaryType);
		try {
			setState(557);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,23,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(541);
				match(T__21);
				setState(542);
				match(T__22);
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(543);
				match(T__21);
				setState(544);
				binBaseType();
				setState(545);
				match(T__22);
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(547);
				match(T__21);
				setState(548);
				binUnitType();
				setState(549);
				match(T__22);
				}
				break;
			case 4:
				enterOuterAlt(_localctx, 4);
				{
				setState(551);
				match(T__21);
				setState(552);
				binBaseType();
				setState(553);
				match(T__5);
				setState(554);
				binUnitType();
				setState(555);
				match(T__22);
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class BinBaseTypeContext extends ParserRuleContext {
		public TokVarContext tokVar() {
			return getRuleContext(TokVarContext.class,0);
		}
		public Re_typeContext re_type() {
			return getRuleContext(Re_typeContext.class,0);
		}
		public BinBaseTypeContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_binBaseType; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof ErlangListener ) ((ErlangListener)listener).enterBinBaseType(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof ErlangListener ) ((ErlangListener)listener).exitBinBaseType(this);
		}
	}

	public final BinBaseTypeContext binBaseType() throws RecognitionException {
		BinBaseTypeContext _localctx = new BinBaseTypeContext(_ctx, getState());
		enterRule(_localctx, 68, RULE_binBaseType);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(559);
			tokVar();
			setState(560);
			match(T__4);
			setState(561);
			re_type();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class BinUnitTypeContext extends ParserRuleContext {
		public List<TokVarContext> tokVar() {
			return getRuleContexts(TokVarContext.class);
		}
		public TokVarContext tokVar(int i) {
			return getRuleContext(TokVarContext.class,i);
		}
		public Re_typeContext re_type() {
			return getRuleContext(Re_typeContext.class,0);
		}
		public BinUnitTypeContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_binUnitType; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof ErlangListener ) ((ErlangListener)listener).enterBinUnitType(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof ErlangListener ) ((ErlangListener)listener).exitBinUnitType(this);
		}
	}

	public final BinUnitTypeContext binUnitType() throws RecognitionException {
		BinUnitTypeContext _localctx = new BinUnitTypeContext(_ctx, getState());
		enterRule(_localctx, 70, RULE_binUnitType);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(563);
			tokVar();
			setState(564);
			match(T__4);
			setState(565);
			tokVar();
			setState(566);
			match(T__23);
			setState(567);
			re_type();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class AttrValContext extends ParserRuleContext {
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public ExprsContext exprs() {
			return getRuleContext(ExprsContext.class,0);
		}
		public AttrValContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_attrVal; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof ErlangListener ) ((ErlangListener)listener).enterAttrVal(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof ErlangListener ) ((ErlangListener)listener).exitAttrVal(this);
		}
	}

	public final AttrValContext attrVal() throws RecognitionException {
		AttrValContext _localctx = new AttrValContext(_ctx, getState());
		enterRule(_localctx, 72, RULE_attrVal);
		try {
			setState(584);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,24,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(569);
				expr();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(570);
				match(T__2);
				setState(571);
				expr();
				setState(572);
				match(T__3);
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(574);
				expr();
				setState(575);
				match(T__5);
				setState(576);
				exprs();
				}
				break;
			case 4:
				enterOuterAlt(_localctx, 4);
				{
				setState(578);
				match(T__2);
				setState(579);
				expr();
				setState(580);
				match(T__5);
				setState(581);
				exprs();
				setState(582);
				match(T__3);
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Function_Context extends ParserRuleContext {
		public List<FunctionClauseContext> functionClause() {
			return getRuleContexts(FunctionClauseContext.class);
		}
		public FunctionClauseContext functionClause(int i) {
			return getRuleContext(FunctionClauseContext.class,i);
		}
		public Function_Context(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_function_; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof ErlangListener ) ((ErlangListener)listener).enterFunction_(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof ErlangListener ) ((ErlangListener)listener).exitFunction_(this);
		}
	}

	public final Function_Context function_() throws RecognitionException {
		Function_Context _localctx = new Function_Context(_ctx, getState());
		enterRule(_localctx, 74, RULE_function_);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(586);
			functionClause();
			setState(591);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==T__9) {
				{
				{
				setState(587);
				match(T__9);
				setState(588);
				functionClause();
				}
				}
				setState(593);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class FunctionClauseContext extends ParserRuleContext {
		public TokAtomContext tokAtom() {
			return getRuleContext(TokAtomContext.class,0);
		}
		public ClauseArgsContext clauseArgs() {
			return getRuleContext(ClauseArgsContext.class,0);
		}
		public ClauseGuardContext clauseGuard() {
			return getRuleContext(ClauseGuardContext.class,0);
		}
		public ClauseBodyContext clauseBody() {
			return getRuleContext(ClauseBodyContext.class,0);
		}
		public FunctionClauseContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_functionClause; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof ErlangListener ) ((ErlangListener)listener).enterFunctionClause(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof ErlangListener ) ((ErlangListener)listener).exitFunctionClause(this);
		}
	}

	public final FunctionClauseContext functionClause() throws RecognitionException {
		FunctionClauseContext _localctx = new FunctionClauseContext(_ctx, getState());
		enterRule(_localctx, 76, RULE_functionClause);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(594);
			tokAtom();
			setState(595);
			clauseArgs();
			setState(596);
			clauseGuard();
			setState(597);
			clauseBody();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ClauseArgsContext extends ParserRuleContext {
		public PatArgumentListContext patArgumentList() {
			return getRuleContext(PatArgumentListContext.class,0);
		}
		public ClauseArgsContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_clauseArgs; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof ErlangListener ) ((ErlangListener)listener).enterClauseArgs(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof ErlangListener ) ((ErlangListener)listener).exitClauseArgs(this);
		}
	}

	public final ClauseArgsContext clauseArgs() throws RecognitionException {
		ClauseArgsContext _localctx = new ClauseArgsContext(_ctx, getState());
		enterRule(_localctx, 78, RULE_clauseArgs);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(599);
			patArgumentList();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ClauseGuardContext extends ParserRuleContext {
		public GuardContext guard() {
			return getRuleContext(GuardContext.class,0);
		}
		public ClauseGuardContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_clauseGuard; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof ErlangListener ) ((ErlangListener)listener).enterClauseGuard(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof ErlangListener ) ((ErlangListener)listener).exitClauseGuard(this);
		}
	}

	public final ClauseGuardContext clauseGuard() throws RecognitionException {
		ClauseGuardContext _localctx = new ClauseGuardContext(_ctx, getState());
		enterRule(_localctx, 80, RULE_clauseGuard);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(603);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==T__10) {
				{
				setState(601);
				match(T__10);
				setState(602);
				guard();
				}
			}

			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ClauseBodyContext extends ParserRuleContext {
		public ExprsContext exprs() {
			return getRuleContext(ExprsContext.class,0);
		}
		public ClauseBodyContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_clauseBody; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof ErlangListener ) ((ErlangListener)listener).enterClauseBody(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof ErlangListener ) ((ErlangListener)listener).exitClauseBody(this);
		}
	}

	public final ClauseBodyContext clauseBody() throws RecognitionException {
		ClauseBodyContext _localctx = new ClauseBodyContext(_ctx, getState());
		enterRule(_localctx, 82, RULE_clauseBody);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(605);
			match(T__18);
			setState(606);
			exprs();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ExprContext extends ParserRuleContext {
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public Expr100Context expr100() {
			return getRuleContext(Expr100Context.class,0);
		}
		public ExprContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expr; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof ErlangListener ) ((ErlangListener)listener).enterExpr(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof ErlangListener ) ((ErlangListener)listener).exitExpr(this);
		}
	}

	public final ExprContext expr() throws RecognitionException {
		ExprContext _localctx = new ExprContext(_ctx, getState());
		enterRule(_localctx, 84, RULE_expr);
		try {
			setState(611);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case T__24:
				enterOuterAlt(_localctx, 1);
				{
				setState(608);
				match(T__24);
				setState(609);
				expr();
				}
				break;
			case T__1:
			case T__2:
			case T__7:
			case T__13:
			case T__16:
			case T__17:
			case T__21:
			case T__29:
			case T__35:
			case T__36:
			case T__38:
			case T__40:
			case T__41:
			case T__42:
			case T__43:
			case TokAtom:
			case TokVar:
			case TokFloat:
			case TokInteger:
			case TokChar:
			case TokString:
				enterOuterAlt(_localctx, 2);
				{
				setState(610);
				expr100();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Expr100Context extends ParserRuleContext {
		public List<Expr150Context> expr150() {
			return getRuleContexts(Expr150Context.class);
		}
		public Expr150Context expr150(int i) {
			return getRuleContext(Expr150Context.class,i);
		}
		public Expr100Context(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expr100; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof ErlangListener ) ((ErlangListener)listener).enterExpr100(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof ErlangListener ) ((ErlangListener)listener).exitExpr100(this);
		}
	}

	public final Expr100Context expr100() throws RecognitionException {
		Expr100Context _localctx = new Expr100Context(_ctx, getState());
		enterRule(_localctx, 86, RULE_expr100);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(613);
			expr150();
			setState(618);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==T__25 || _la==T__26) {
				{
				{
				setState(614);
				_la = _input.LA(1);
				if ( !(_la==T__25 || _la==T__26) ) {
				_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				setState(615);
				expr150();
				}
				}
				setState(620);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Expr150Context extends ParserRuleContext {
		public List<Expr160Context> expr160() {
			return getRuleContexts(Expr160Context.class);
		}
		public Expr160Context expr160(int i) {
			return getRuleContext(Expr160Context.class,i);
		}
		public Expr150Context(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expr150; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof ErlangListener ) ((ErlangListener)listener).enterExpr150(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof ErlangListener ) ((ErlangListener)listener).exitExpr150(this);
		}
	}

	public final Expr150Context expr150() throws RecognitionException {
		Expr150Context _localctx = new Expr150Context(_ctx, getState());
		enterRule(_localctx, 88, RULE_expr150);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(621);
			expr160();
			setState(626);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==T__27) {
				{
				{
				setState(622);
				match(T__27);
				setState(623);
				expr160();
				}
				}
				setState(628);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Expr160Context extends ParserRuleContext {
		public List<Expr200Context> expr200() {
			return getRuleContexts(Expr200Context.class);
		}
		public Expr200Context expr200(int i) {
			return getRuleContext(Expr200Context.class,i);
		}
		public Expr160Context(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expr160; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof ErlangListener ) ((ErlangListener)listener).enterExpr160(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof ErlangListener ) ((ErlangListener)listener).exitExpr160(this);
		}
	}

	public final Expr160Context expr160() throws RecognitionException {
		Expr160Context _localctx = new Expr160Context(_ctx, getState());
		enterRule(_localctx, 90, RULE_expr160);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(629);
			expr200();
			setState(634);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==T__28) {
				{
				{
				setState(630);
				match(T__28);
				setState(631);
				expr200();
				}
				}
				setState(636);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Expr200Context extends ParserRuleContext {
		public List<Expr300Context> expr300() {
			return getRuleContexts(Expr300Context.class);
		}
		public Expr300Context expr300(int i) {
			return getRuleContext(Expr300Context.class,i);
		}
		public CompOpContext compOp() {
			return getRuleContext(CompOpContext.class,0);
		}
		public Expr200Context(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expr200; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof ErlangListener ) ((ErlangListener)listener).enterExpr200(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof ErlangListener ) ((ErlangListener)listener).exitExpr200(this);
		}
	}

	public final Expr200Context expr200() throws RecognitionException {
		Expr200Context _localctx = new Expr200Context(_ctx, getState());
		enterRule(_localctx, 92, RULE_expr200);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(637);
			expr300();
			setState(641);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (((((_la - 57)) & ~0x3f) == 0 && ((1L << (_la - 57)) & 255L) != 0)) {
				{
				setState(638);
				compOp();
				setState(639);
				expr300();
				}
			}

			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Expr300Context extends ParserRuleContext {
		public List<Expr400Context> expr400() {
			return getRuleContexts(Expr400Context.class);
		}
		public Expr400Context expr400(int i) {
			return getRuleContext(Expr400Context.class,i);
		}
		public List<ListOpContext> listOp() {
			return getRuleContexts(ListOpContext.class);
		}
		public ListOpContext listOp(int i) {
			return getRuleContext(ListOpContext.class,i);
		}
		public Expr300Context(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expr300; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof ErlangListener ) ((ErlangListener)listener).enterExpr300(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof ErlangListener ) ((ErlangListener)listener).exitExpr300(this);
		}
	}

	public final Expr300Context expr300() throws RecognitionException {
		Expr300Context _localctx = new Expr300Context(_ctx, getState());
		enterRule(_localctx, 94, RULE_expr300);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(643);
			expr400();
			setState(649);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==T__54 || _la==T__55) {
				{
				{
				setState(644);
				listOp();
				setState(645);
				expr400();
				}
				}
				setState(651);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Expr400Context extends ParserRuleContext {
		public List<Expr500Context> expr500() {
			return getRuleContexts(Expr500Context.class);
		}
		public Expr500Context expr500(int i) {
			return getRuleContext(Expr500Context.class,i);
		}
		public List<AddOpContext> addOp() {
			return getRuleContexts(AddOpContext.class);
		}
		public AddOpContext addOp(int i) {
			return getRuleContext(AddOpContext.class,i);
		}
		public Expr400Context(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expr400; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof ErlangListener ) ((ErlangListener)listener).enterExpr400(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof ErlangListener ) ((ErlangListener)listener).exitExpr400(this);
		}
	}

	public final Expr400Context expr400() throws RecognitionException {
		Expr400Context _localctx = new Expr400Context(_ctx, getState());
		enterRule(_localctx, 96, RULE_expr400);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(652);
			expr500();
			setState(658);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & 35470245112053764L) != 0)) {
				{
				{
				setState(653);
				addOp();
				setState(654);
				expr500();
				}
				}
				setState(660);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Expr500Context extends ParserRuleContext {
		public List<Expr600Context> expr600() {
			return getRuleContexts(Expr600Context.class);
		}
		public Expr600Context expr600(int i) {
			return getRuleContext(Expr600Context.class,i);
		}
		public List<MultOpContext> multOp() {
			return getRuleContexts(MultOpContext.class);
		}
		public MultOpContext multOp(int i) {
			return getRuleContext(MultOpContext.class,i);
		}
		public Expr500Context(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expr500; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof ErlangListener ) ((ErlangListener)listener).enterExpr500(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof ErlangListener ) ((ErlangListener)listener).exitExpr500(this);
		}
	}

	public final Expr500Context expr500() throws RecognitionException {
		Expr500Context _localctx = new Expr500Context(_ctx, getState());
		enterRule(_localctx, 98, RULE_expr500);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(661);
			expr600();
			setState(667);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & 527769893076992L) != 0)) {
				{
				{
				setState(662);
				multOp();
				setState(663);
				expr600();
				}
				}
				setState(669);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Expr600Context extends ParserRuleContext {
		public PrefixOpContext prefixOp() {
			return getRuleContext(PrefixOpContext.class,0);
		}
		public Expr600Context expr600() {
			return getRuleContext(Expr600Context.class,0);
		}
		public Expr650Context expr650() {
			return getRuleContext(Expr650Context.class,0);
		}
		public Expr600Context(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expr600; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof ErlangListener ) ((ErlangListener)listener).enterExpr600(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof ErlangListener ) ((ErlangListener)listener).exitExpr600(this);
		}
	}

	public final Expr600Context expr600() throws RecognitionException {
		Expr600Context _localctx = new Expr600Context(_ctx, getState());
		enterRule(_localctx, 100, RULE_expr600);
		try {
			setState(674);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case T__1:
			case T__41:
			case T__42:
			case T__43:
				enterOuterAlt(_localctx, 1);
				{
				setState(670);
				prefixOp();
				setState(671);
				expr600();
				}
				break;
			case T__2:
			case T__7:
			case T__13:
			case T__16:
			case T__17:
			case T__21:
			case T__29:
			case T__35:
			case T__36:
			case T__38:
			case T__40:
			case TokAtom:
			case TokVar:
			case TokFloat:
			case TokInteger:
			case TokChar:
			case TokString:
				enterOuterAlt(_localctx, 2);
				{
				setState(673);
				expr650();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Expr650Context extends ParserRuleContext {
		public MapExprContext mapExpr() {
			return getRuleContext(MapExprContext.class,0);
		}
		public Expr700Context expr700() {
			return getRuleContext(Expr700Context.class,0);
		}
		public Expr650Context(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expr650; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof ErlangListener ) ((ErlangListener)listener).enterExpr650(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof ErlangListener ) ((ErlangListener)listener).exitExpr650(this);
		}
	}

	public final Expr650Context expr650() throws RecognitionException {
		Expr650Context _localctx = new Expr650Context(_ctx, getState());
		enterRule(_localctx, 102, RULE_expr650);
		try {
			setState(678);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,36,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(676);
				mapExpr(0);
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(677);
				expr700();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Expr700Context extends ParserRuleContext {
		public FunctionCallContext functionCall() {
			return getRuleContext(FunctionCallContext.class,0);
		}
		public RecordExprContext recordExpr() {
			return getRuleContext(RecordExprContext.class,0);
		}
		public Expr800Context expr800() {
			return getRuleContext(Expr800Context.class,0);
		}
		public Expr700Context(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expr700; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof ErlangListener ) ((ErlangListener)listener).enterExpr700(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof ErlangListener ) ((ErlangListener)listener).exitExpr700(this);
		}
	}

	public final Expr700Context expr700() throws RecognitionException {
		Expr700Context _localctx = new Expr700Context(_ctx, getState());
		enterRule(_localctx, 104, RULE_expr700);
		try {
			setState(683);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,37,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(680);
				functionCall();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(681);
				recordExpr(0);
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(682);
				expr800();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Expr800Context extends ParserRuleContext {
		public List<ExprMaxContext> exprMax() {
			return getRuleContexts(ExprMaxContext.class);
		}
		public ExprMaxContext exprMax(int i) {
			return getRuleContext(ExprMaxContext.class,i);
		}
		public Expr800Context(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expr800; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof ErlangListener ) ((ErlangListener)listener).enterExpr800(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof ErlangListener ) ((ErlangListener)listener).exitExpr800(this);
		}
	}

	public final Expr800Context expr800() throws RecognitionException {
		Expr800Context _localctx = new Expr800Context(_ctx, getState());
		enterRule(_localctx, 106, RULE_expr800);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(685);
			exprMax();
			setState(688);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==T__4) {
				{
				setState(686);
				match(T__4);
				setState(687);
				exprMax();
				}
			}

			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ExprMaxContext extends ParserRuleContext {
		public TokVarContext tokVar() {
			return getRuleContext(TokVarContext.class,0);
		}
		public AtomicContext atomic() {
			return getRuleContext(AtomicContext.class,0);
		}
		public Re_listContext re_list() {
			return getRuleContext(Re_listContext.class,0);
		}
		public BinaryContext binary() {
			return getRuleContext(BinaryContext.class,0);
		}
		public ListComprehensionContext listComprehension() {
			return getRuleContext(ListComprehensionContext.class,0);
		}
		public BinaryComprehensionContext binaryComprehension() {
			return getRuleContext(BinaryComprehensionContext.class,0);
		}
		public Re_tupleContext re_tuple() {
			return getRuleContext(Re_tupleContext.class,0);
		}
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public ExprsContext exprs() {
			return getRuleContext(ExprsContext.class,0);
		}
		public IfExprContext ifExpr() {
			return getRuleContext(IfExprContext.class,0);
		}
		public CaseExprContext caseExpr() {
			return getRuleContext(CaseExprContext.class,0);
		}
		public ReceiveExprContext receiveExpr() {
			return getRuleContext(ReceiveExprContext.class,0);
		}
		public FunExprContext funExpr() {
			return getRuleContext(FunExprContext.class,0);
		}
		public TryExprContext tryExpr() {
			return getRuleContext(TryExprContext.class,0);
		}
		public ExprMaxContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_exprMax; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof ErlangListener ) ((ErlangListener)listener).enterExprMax(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof ErlangListener ) ((ErlangListener)listener).exitExprMax(this);
		}
	}

	public final ExprMaxContext exprMax() throws RecognitionException {
		ExprMaxContext _localctx = new ExprMaxContext(_ctx, getState());
		enterRule(_localctx, 108, RULE_exprMax);
		try {
			setState(710);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,39,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(690);
				tokVar();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(691);
				atomic();
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(692);
				re_list();
				}
				break;
			case 4:
				enterOuterAlt(_localctx, 4);
				{
				setState(693);
				binary();
				}
				break;
			case 5:
				enterOuterAlt(_localctx, 5);
				{
				setState(694);
				listComprehension();
				}
				break;
			case 6:
				enterOuterAlt(_localctx, 6);
				{
				setState(695);
				binaryComprehension();
				}
				break;
			case 7:
				enterOuterAlt(_localctx, 7);
				{
				setState(696);
				re_tuple();
				}
				break;
			case 8:
				enterOuterAlt(_localctx, 8);
				{
				setState(697);
				match(T__2);
				setState(698);
				expr();
				setState(699);
				match(T__3);
				}
				break;
			case 9:
				enterOuterAlt(_localctx, 9);
				{
				setState(701);
				match(T__29);
				setState(702);
				exprs();
				setState(703);
				match(T__30);
				}
				break;
			case 10:
				enterOuterAlt(_localctx, 10);
				{
				setState(705);
				ifExpr();
				}
				break;
			case 11:
				enterOuterAlt(_localctx, 11);
				{
				setState(706);
				caseExpr();
				}
				break;
			case 12:
				enterOuterAlt(_localctx, 12);
				{
				setState(707);
				receiveExpr();
				}
				break;
			case 13:
				enterOuterAlt(_localctx, 13);
				{
				setState(708);
				funExpr();
				}
				break;
			case 14:
				enterOuterAlt(_localctx, 14);
				{
				setState(709);
				tryExpr();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class PatExprContext extends ParserRuleContext {
		public PatExpr200Context patExpr200() {
			return getRuleContext(PatExpr200Context.class,0);
		}
		public PatExprContext patExpr() {
			return getRuleContext(PatExprContext.class,0);
		}
		public PatExprContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_patExpr; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof ErlangListener ) ((ErlangListener)listener).enterPatExpr(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof ErlangListener ) ((ErlangListener)listener).exitPatExpr(this);
		}
	}

	public final PatExprContext patExpr() throws RecognitionException {
		PatExprContext _localctx = new PatExprContext(_ctx, getState());
		enterRule(_localctx, 110, RULE_patExpr);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(712);
			patExpr200();
			setState(715);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==T__25) {
				{
				setState(713);
				match(T__25);
				setState(714);
				patExpr();
				}
			}

			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class PatExpr200Context extends ParserRuleContext {
		public List<PatExpr300Context> patExpr300() {
			return getRuleContexts(PatExpr300Context.class);
		}
		public PatExpr300Context patExpr300(int i) {
			return getRuleContext(PatExpr300Context.class,i);
		}
		public CompOpContext compOp() {
			return getRuleContext(CompOpContext.class,0);
		}
		public PatExpr200Context(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_patExpr200; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof ErlangListener ) ((ErlangListener)listener).enterPatExpr200(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof ErlangListener ) ((ErlangListener)listener).exitPatExpr200(this);
		}
	}

	public final PatExpr200Context patExpr200() throws RecognitionException {
		PatExpr200Context _localctx = new PatExpr200Context(_ctx, getState());
		enterRule(_localctx, 112, RULE_patExpr200);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(717);
			patExpr300();
			setState(721);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (((((_la - 57)) & ~0x3f) == 0 && ((1L << (_la - 57)) & 255L) != 0)) {
				{
				setState(718);
				compOp();
				setState(719);
				patExpr300();
				}
			}

			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class PatExpr300Context extends ParserRuleContext {
		public PatExpr400Context patExpr400() {
			return getRuleContext(PatExpr400Context.class,0);
		}
		public ListOpContext listOp() {
			return getRuleContext(ListOpContext.class,0);
		}
		public PatExpr300Context patExpr300() {
			return getRuleContext(PatExpr300Context.class,0);
		}
		public PatExpr300Context(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_patExpr300; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof ErlangListener ) ((ErlangListener)listener).enterPatExpr300(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof ErlangListener ) ((ErlangListener)listener).exitPatExpr300(this);
		}
	}

	public final PatExpr300Context patExpr300() throws RecognitionException {
		PatExpr300Context _localctx = new PatExpr300Context(_ctx, getState());
		enterRule(_localctx, 114, RULE_patExpr300);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(723);
			patExpr400(0);
			setState(727);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==T__54 || _la==T__55) {
				{
				setState(724);
				listOp();
				setState(725);
				patExpr300();
				}
			}

			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class PatExpr400Context extends ParserRuleContext {
		public PatExpr500Context patExpr500() {
			return getRuleContext(PatExpr500Context.class,0);
		}
		public PatExpr400Context patExpr400() {
			return getRuleContext(PatExpr400Context.class,0);
		}
		public AddOpContext addOp() {
			return getRuleContext(AddOpContext.class,0);
		}
		public PatExpr400Context(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_patExpr400; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof ErlangListener ) ((ErlangListener)listener).enterPatExpr400(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof ErlangListener ) ((ErlangListener)listener).exitPatExpr400(this);
		}
	}

	public final PatExpr400Context patExpr400() throws RecognitionException {
		return patExpr400(0);
	}

	private PatExpr400Context patExpr400(int _p) throws RecognitionException {
		ParserRuleContext _parentctx = _ctx;
		int _parentState = getState();
		PatExpr400Context _localctx = new PatExpr400Context(_ctx, _parentState);
		PatExpr400Context _prevctx = _localctx;
		int _startState = 116;
		enterRecursionRule(_localctx, 116, RULE_patExpr400, _p);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			{
			setState(730);
			patExpr500(0);
			}
			_ctx.stop = _input.LT(-1);
			setState(738);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,43,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					{
					_localctx = new PatExpr400Context(_parentctx, _parentState);
					pushNewRecursionContext(_localctx, _startState, RULE_patExpr400);
					setState(732);
					if (!(precpred(_ctx, 2))) throw new FailedPredicateException(this, "precpred(_ctx, 2)");
					setState(733);
					addOp();
					setState(734);
					patExpr500(0);
					}
					} 
				}
				setState(740);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,43,_ctx);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			unrollRecursionContexts(_parentctx);
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class PatExpr500Context extends ParserRuleContext {
		public PatExpr600Context patExpr600() {
			return getRuleContext(PatExpr600Context.class,0);
		}
		public PatExpr500Context patExpr500() {
			return getRuleContext(PatExpr500Context.class,0);
		}
		public MultOpContext multOp() {
			return getRuleContext(MultOpContext.class,0);
		}
		public PatExpr500Context(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_patExpr500; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof ErlangListener ) ((ErlangListener)listener).enterPatExpr500(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof ErlangListener ) ((ErlangListener)listener).exitPatExpr500(this);
		}
	}

	public final PatExpr500Context patExpr500() throws RecognitionException {
		return patExpr500(0);
	}

	private PatExpr500Context patExpr500(int _p) throws RecognitionException {
		ParserRuleContext _parentctx = _ctx;
		int _parentState = getState();
		PatExpr500Context _localctx = new PatExpr500Context(_ctx, _parentState);
		PatExpr500Context _prevctx = _localctx;
		int _startState = 118;
		enterRecursionRule(_localctx, 118, RULE_patExpr500, _p);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			{
			setState(742);
			patExpr600();
			}
			_ctx.stop = _input.LT(-1);
			setState(750);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,44,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					{
					_localctx = new PatExpr500Context(_parentctx, _parentState);
					pushNewRecursionContext(_localctx, _startState, RULE_patExpr500);
					setState(744);
					if (!(precpred(_ctx, 2))) throw new FailedPredicateException(this, "precpred(_ctx, 2)");
					setState(745);
					multOp();
					setState(746);
					patExpr600();
					}
					} 
				}
				setState(752);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,44,_ctx);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			unrollRecursionContexts(_parentctx);
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class PatExpr600Context extends ParserRuleContext {
		public PrefixOpContext prefixOp() {
			return getRuleContext(PrefixOpContext.class,0);
		}
		public PatExpr600Context patExpr600() {
			return getRuleContext(PatExpr600Context.class,0);
		}
		public PatExpr650Context patExpr650() {
			return getRuleContext(PatExpr650Context.class,0);
		}
		public PatExpr600Context(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_patExpr600; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof ErlangListener ) ((ErlangListener)listener).enterPatExpr600(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof ErlangListener ) ((ErlangListener)listener).exitPatExpr600(this);
		}
	}

	public final PatExpr600Context patExpr600() throws RecognitionException {
		PatExpr600Context _localctx = new PatExpr600Context(_ctx, getState());
		enterRule(_localctx, 120, RULE_patExpr600);
		try {
			setState(757);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case T__1:
			case T__41:
			case T__42:
			case T__43:
				enterOuterAlt(_localctx, 1);
				{
				setState(753);
				prefixOp();
				setState(754);
				patExpr600();
				}
				break;
			case T__2:
			case T__7:
			case T__13:
			case T__16:
			case T__21:
			case TokAtom:
			case TokVar:
			case TokFloat:
			case TokInteger:
			case TokChar:
			case TokString:
				enterOuterAlt(_localctx, 2);
				{
				setState(756);
				patExpr650();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class PatExpr650Context extends ParserRuleContext {
		public MapPatExprContext mapPatExpr() {
			return getRuleContext(MapPatExprContext.class,0);
		}
		public PatExpr700Context patExpr700() {
			return getRuleContext(PatExpr700Context.class,0);
		}
		public PatExpr650Context(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_patExpr650; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof ErlangListener ) ((ErlangListener)listener).enterPatExpr650(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof ErlangListener ) ((ErlangListener)listener).exitPatExpr650(this);
		}
	}

	public final PatExpr650Context patExpr650() throws RecognitionException {
		PatExpr650Context _localctx = new PatExpr650Context(_ctx, getState());
		enterRule(_localctx, 122, RULE_patExpr650);
		try {
			setState(761);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,46,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(759);
				mapPatExpr(0);
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(760);
				patExpr700();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class PatExpr700Context extends ParserRuleContext {
		public RecordPatExprContext recordPatExpr() {
			return getRuleContext(RecordPatExprContext.class,0);
		}
		public PatExpr800Context patExpr800() {
			return getRuleContext(PatExpr800Context.class,0);
		}
		public PatExpr700Context(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_patExpr700; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof ErlangListener ) ((ErlangListener)listener).enterPatExpr700(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof ErlangListener ) ((ErlangListener)listener).exitPatExpr700(this);
		}
	}

	public final PatExpr700Context patExpr700() throws RecognitionException {
		PatExpr700Context _localctx = new PatExpr700Context(_ctx, getState());
		enterRule(_localctx, 124, RULE_patExpr700);
		try {
			setState(765);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case T__16:
				enterOuterAlt(_localctx, 1);
				{
				setState(763);
				recordPatExpr();
				}
				break;
			case T__2:
			case T__7:
			case T__13:
			case T__21:
			case TokAtom:
			case TokVar:
			case TokFloat:
			case TokInteger:
			case TokChar:
			case TokString:
				enterOuterAlt(_localctx, 2);
				{
				setState(764);
				patExpr800();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class PatExpr800Context extends ParserRuleContext {
		public PatExprMaxContext patExprMax() {
			return getRuleContext(PatExprMaxContext.class,0);
		}
		public PatExpr800Context(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_patExpr800; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof ErlangListener ) ((ErlangListener)listener).enterPatExpr800(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof ErlangListener ) ((ErlangListener)listener).exitPatExpr800(this);
		}
	}

	public final PatExpr800Context patExpr800() throws RecognitionException {
		PatExpr800Context _localctx = new PatExpr800Context(_ctx, getState());
		enterRule(_localctx, 126, RULE_patExpr800);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(767);
			patExprMax();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class PatExprMaxContext extends ParserRuleContext {
		public TokVarContext tokVar() {
			return getRuleContext(TokVarContext.class,0);
		}
		public AtomicContext atomic() {
			return getRuleContext(AtomicContext.class,0);
		}
		public Re_listContext re_list() {
			return getRuleContext(Re_listContext.class,0);
		}
		public BinaryContext binary() {
			return getRuleContext(BinaryContext.class,0);
		}
		public Re_tupleContext re_tuple() {
			return getRuleContext(Re_tupleContext.class,0);
		}
		public PatExprContext patExpr() {
			return getRuleContext(PatExprContext.class,0);
		}
		public PatExprMaxContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_patExprMax; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof ErlangListener ) ((ErlangListener)listener).enterPatExprMax(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof ErlangListener ) ((ErlangListener)listener).exitPatExprMax(this);
		}
	}

	public final PatExprMaxContext patExprMax() throws RecognitionException {
		PatExprMaxContext _localctx = new PatExprMaxContext(_ctx, getState());
		enterRule(_localctx, 128, RULE_patExprMax);
		try {
			setState(778);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case TokVar:
				enterOuterAlt(_localctx, 1);
				{
				setState(769);
				tokVar();
				}
				break;
			case TokAtom:
			case TokFloat:
			case TokInteger:
			case TokChar:
			case TokString:
				enterOuterAlt(_localctx, 2);
				{
				setState(770);
				atomic();
				}
				break;
			case T__13:
				enterOuterAlt(_localctx, 3);
				{
				setState(771);
				re_list();
				}
				break;
			case T__21:
				enterOuterAlt(_localctx, 4);
				{
				setState(772);
				binary();
				}
				break;
			case T__7:
				enterOuterAlt(_localctx, 5);
				{
				setState(773);
				re_tuple();
				}
				break;
			case T__2:
				enterOuterAlt(_localctx, 6);
				{
				setState(774);
				match(T__2);
				setState(775);
				patExpr();
				setState(776);
				match(T__3);
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class MapPatExprContext extends ParserRuleContext {
		public MapTupleContext mapTuple() {
			return getRuleContext(MapTupleContext.class,0);
		}
		public PatExprMaxContext patExprMax() {
			return getRuleContext(PatExprMaxContext.class,0);
		}
		public MapPatExprContext mapPatExpr() {
			return getRuleContext(MapPatExprContext.class,0);
		}
		public MapPatExprContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_mapPatExpr; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof ErlangListener ) ((ErlangListener)listener).enterMapPatExpr(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof ErlangListener ) ((ErlangListener)listener).exitMapPatExpr(this);
		}
	}

	public final MapPatExprContext mapPatExpr() throws RecognitionException {
		return mapPatExpr(0);
	}

	private MapPatExprContext mapPatExpr(int _p) throws RecognitionException {
		ParserRuleContext _parentctx = _ctx;
		int _parentState = getState();
		MapPatExprContext _localctx = new MapPatExprContext(_ctx, _parentState);
		MapPatExprContext _prevctx = _localctx;
		int _startState = 130;
		enterRecursionRule(_localctx, 130, RULE_mapPatExpr, _p);
		int _la;
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			{
			setState(782);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & 4210952L) != 0) || ((((_la - 65)) & ~0x3f) == 0 && ((1L << (_la - 65)) & 63L) != 0)) {
				{
				setState(781);
				patExprMax();
				}
			}

			setState(784);
			match(T__16);
			setState(785);
			mapTuple();
			}
			_ctx.stop = _input.LT(-1);
			setState(792);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,50,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					{
					_localctx = new MapPatExprContext(_parentctx, _parentState);
					pushNewRecursionContext(_localctx, _startState, RULE_mapPatExpr);
					setState(787);
					if (!(precpred(_ctx, 1))) throw new FailedPredicateException(this, "precpred(_ctx, 1)");
					setState(788);
					match(T__16);
					setState(789);
					mapTuple();
					}
					} 
				}
				setState(794);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,50,_ctx);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			unrollRecursionContexts(_parentctx);
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class RecordPatExprContext extends ParserRuleContext {
		public List<TokAtomContext> tokAtom() {
			return getRuleContexts(TokAtomContext.class);
		}
		public TokAtomContext tokAtom(int i) {
			return getRuleContext(TokAtomContext.class,i);
		}
		public RecordTupleContext recordTuple() {
			return getRuleContext(RecordTupleContext.class,0);
		}
		public RecordPatExprContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_recordPatExpr; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof ErlangListener ) ((ErlangListener)listener).enterRecordPatExpr(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof ErlangListener ) ((ErlangListener)listener).exitRecordPatExpr(this);
		}
	}

	public final RecordPatExprContext recordPatExpr() throws RecognitionException {
		RecordPatExprContext _localctx = new RecordPatExprContext(_ctx, getState());
		enterRule(_localctx, 132, RULE_recordPatExpr);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(795);
			match(T__16);
			setState(796);
			tokAtom();
			setState(800);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case T__0:
				{
				setState(797);
				match(T__0);
				setState(798);
				tokAtom();
				}
				break;
			case T__7:
				{
				setState(799);
				recordTuple();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Re_listContext extends ParserRuleContext {
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public TailContext tail() {
			return getRuleContext(TailContext.class,0);
		}
		public Re_listContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_re_list; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof ErlangListener ) ((ErlangListener)listener).enterRe_list(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof ErlangListener ) ((ErlangListener)listener).exitRe_list(this);
		}
	}

	public final Re_listContext re_list() throws RecognitionException {
		Re_listContext _localctx = new Re_listContext(_ctx, getState());
		enterRule(_localctx, 134, RULE_re_list);
		try {
			setState(808);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,52,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(802);
				match(T__13);
				setState(803);
				match(T__14);
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(804);
				match(T__13);
				setState(805);
				expr();
				setState(806);
				tail();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class TailContext extends ParserRuleContext {
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public TailContext tail() {
			return getRuleContext(TailContext.class,0);
		}
		public TailContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_tail; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof ErlangListener ) ((ErlangListener)listener).enterTail(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof ErlangListener ) ((ErlangListener)listener).exitTail(this);
		}
	}

	public final TailContext tail() throws RecognitionException {
		TailContext _localctx = new TailContext(_ctx, getState());
		enterRule(_localctx, 136, RULE_tail);
		try {
			setState(819);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case T__14:
				enterOuterAlt(_localctx, 1);
				{
				setState(810);
				match(T__14);
				}
				break;
			case T__11:
				enterOuterAlt(_localctx, 2);
				{
				setState(811);
				match(T__11);
				setState(812);
				expr();
				setState(813);
				match(T__14);
				}
				break;
			case T__5:
				enterOuterAlt(_localctx, 3);
				{
				setState(815);
				match(T__5);
				setState(816);
				expr();
				setState(817);
				tail();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class BinaryContext extends ParserRuleContext {
		public BinElementsContext binElements() {
			return getRuleContext(BinElementsContext.class,0);
		}
		public BinaryContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_binary; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof ErlangListener ) ((ErlangListener)listener).enterBinary(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof ErlangListener ) ((ErlangListener)listener).exitBinary(this);
		}
	}

	public final BinaryContext binary() throws RecognitionException {
		BinaryContext _localctx = new BinaryContext(_ctx, getState());
		enterRule(_localctx, 138, RULE_binary);
		try {
			setState(827);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,54,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(821);
				match(T__21);
				setState(822);
				match(T__22);
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(823);
				match(T__21);
				setState(824);
				binElements();
				setState(825);
				match(T__22);
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class BinElementsContext extends ParserRuleContext {
		public List<BinElementContext> binElement() {
			return getRuleContexts(BinElementContext.class);
		}
		public BinElementContext binElement(int i) {
			return getRuleContext(BinElementContext.class,i);
		}
		public BinElementsContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_binElements; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof ErlangListener ) ((ErlangListener)listener).enterBinElements(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof ErlangListener ) ((ErlangListener)listener).exitBinElements(this);
		}
	}

	public final BinElementsContext binElements() throws RecognitionException {
		BinElementsContext _localctx = new BinElementsContext(_ctx, getState());
		enterRule(_localctx, 140, RULE_binElements);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(829);
			binElement();
			setState(834);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==T__5) {
				{
				{
				setState(830);
				match(T__5);
				setState(831);
				binElement();
				}
				}
				setState(836);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class BinElementContext extends ParserRuleContext {
		public BitExprContext bitExpr() {
			return getRuleContext(BitExprContext.class,0);
		}
		public OptBitSizeExprContext optBitSizeExpr() {
			return getRuleContext(OptBitSizeExprContext.class,0);
		}
		public OptBitTypeListContext optBitTypeList() {
			return getRuleContext(OptBitTypeListContext.class,0);
		}
		public BinElementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_binElement; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof ErlangListener ) ((ErlangListener)listener).enterBinElement(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof ErlangListener ) ((ErlangListener)listener).exitBinElement(this);
		}
	}

	public final BinElementContext binElement() throws RecognitionException {
		BinElementContext _localctx = new BinElementContext(_ctx, getState());
		enterRule(_localctx, 142, RULE_binElement);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(837);
			bitExpr();
			setState(838);
			optBitSizeExpr();
			setState(839);
			optBitTypeList();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class BitExprContext extends ParserRuleContext {
		public ExprMaxContext exprMax() {
			return getRuleContext(ExprMaxContext.class,0);
		}
		public PrefixOpContext prefixOp() {
			return getRuleContext(PrefixOpContext.class,0);
		}
		public BitExprContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_bitExpr; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof ErlangListener ) ((ErlangListener)listener).enterBitExpr(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof ErlangListener ) ((ErlangListener)listener).exitBitExpr(this);
		}
	}

	public final BitExprContext bitExpr() throws RecognitionException {
		BitExprContext _localctx = new BitExprContext(_ctx, getState());
		enterRule(_localctx, 144, RULE_bitExpr);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(842);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & 30786325577732L) != 0)) {
				{
				setState(841);
				prefixOp();
				}
			}

			setState(844);
			exprMax();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class OptBitSizeExprContext extends ParserRuleContext {
		public BitSizeExprContext bitSizeExpr() {
			return getRuleContext(BitSizeExprContext.class,0);
		}
		public OptBitSizeExprContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_optBitSizeExpr; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof ErlangListener ) ((ErlangListener)listener).enterOptBitSizeExpr(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof ErlangListener ) ((ErlangListener)listener).exitOptBitSizeExpr(this);
		}
	}

	public final OptBitSizeExprContext optBitSizeExpr() throws RecognitionException {
		OptBitSizeExprContext _localctx = new OptBitSizeExprContext(_ctx, getState());
		enterRule(_localctx, 146, RULE_optBitSizeExpr);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(848);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==T__4) {
				{
				setState(846);
				match(T__4);
				setState(847);
				bitSizeExpr();
				}
			}

			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class OptBitTypeListContext extends ParserRuleContext {
		public BitTypeListContext bitTypeList() {
			return getRuleContext(BitTypeListContext.class,0);
		}
		public OptBitTypeListContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_optBitTypeList; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof ErlangListener ) ((ErlangListener)listener).enterOptBitTypeList(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof ErlangListener ) ((ErlangListener)listener).exitOptBitTypeList(this);
		}
	}

	public final OptBitTypeListContext optBitTypeList() throws RecognitionException {
		OptBitTypeListContext _localctx = new OptBitTypeListContext(_ctx, getState());
		enterRule(_localctx, 148, RULE_optBitTypeList);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(852);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==T__31) {
				{
				setState(850);
				match(T__31);
				setState(851);
				bitTypeList();
				}
			}

			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class BitTypeListContext extends ParserRuleContext {
		public List<BitTypeContext> bitType() {
			return getRuleContexts(BitTypeContext.class);
		}
		public BitTypeContext bitType(int i) {
			return getRuleContext(BitTypeContext.class,i);
		}
		public BitTypeListContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_bitTypeList; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof ErlangListener ) ((ErlangListener)listener).enterBitTypeList(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof ErlangListener ) ((ErlangListener)listener).exitBitTypeList(this);
		}
	}

	public final BitTypeListContext bitTypeList() throws RecognitionException {
		BitTypeListContext _localctx = new BitTypeListContext(_ctx, getState());
		enterRule(_localctx, 150, RULE_bitTypeList);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(854);
			bitType();
			setState(859);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==T__1) {
				{
				{
				setState(855);
				match(T__1);
				setState(856);
				bitType();
				}
				}
				setState(861);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class BitTypeContext extends ParserRuleContext {
		public TokAtomContext tokAtom() {
			return getRuleContext(TokAtomContext.class,0);
		}
		public TokIntegerContext tokInteger() {
			return getRuleContext(TokIntegerContext.class,0);
		}
		public BitTypeContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_bitType; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof ErlangListener ) ((ErlangListener)listener).enterBitType(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof ErlangListener ) ((ErlangListener)listener).exitBitType(this);
		}
	}

	public final BitTypeContext bitType() throws RecognitionException {
		BitTypeContext _localctx = new BitTypeContext(_ctx, getState());
		enterRule(_localctx, 152, RULE_bitType);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(862);
			tokAtom();
			setState(865);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==T__4) {
				{
				setState(863);
				match(T__4);
				setState(864);
				tokInteger();
				}
			}

			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class BitSizeExprContext extends ParserRuleContext {
		public ExprMaxContext exprMax() {
			return getRuleContext(ExprMaxContext.class,0);
		}
		public BitSizeExprContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_bitSizeExpr; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof ErlangListener ) ((ErlangListener)listener).enterBitSizeExpr(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof ErlangListener ) ((ErlangListener)listener).exitBitSizeExpr(this);
		}
	}

	public final BitSizeExprContext bitSizeExpr() throws RecognitionException {
		BitSizeExprContext _localctx = new BitSizeExprContext(_ctx, getState());
		enterRule(_localctx, 154, RULE_bitSizeExpr);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(867);
			exprMax();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ListComprehensionContext extends ParserRuleContext {
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public LcExprsContext lcExprs() {
			return getRuleContext(LcExprsContext.class,0);
		}
		public ListComprehensionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_listComprehension; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof ErlangListener ) ((ErlangListener)listener).enterListComprehension(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof ErlangListener ) ((ErlangListener)listener).exitListComprehension(this);
		}
	}

	public final ListComprehensionContext listComprehension() throws RecognitionException {
		ListComprehensionContext _localctx = new ListComprehensionContext(_ctx, getState());
		enterRule(_localctx, 156, RULE_listComprehension);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(869);
			match(T__13);
			setState(870);
			expr();
			setState(871);
			match(T__32);
			setState(872);
			lcExprs();
			setState(873);
			match(T__14);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class BinaryComprehensionContext extends ParserRuleContext {
		public ExprMaxContext exprMax() {
			return getRuleContext(ExprMaxContext.class,0);
		}
		public LcExprsContext lcExprs() {
			return getRuleContext(LcExprsContext.class,0);
		}
		public BinaryComprehensionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_binaryComprehension; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof ErlangListener ) ((ErlangListener)listener).enterBinaryComprehension(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof ErlangListener ) ((ErlangListener)listener).exitBinaryComprehension(this);
		}
	}

	public final BinaryComprehensionContext binaryComprehension() throws RecognitionException {
		BinaryComprehensionContext _localctx = new BinaryComprehensionContext(_ctx, getState());
		enterRule(_localctx, 158, RULE_binaryComprehension);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(875);
			match(T__21);
			setState(876);
			exprMax();
			setState(877);
			match(T__32);
			setState(878);
			lcExprs();
			setState(879);
			match(T__22);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class LcExprsContext extends ParserRuleContext {
		public List<LcExprContext> lcExpr() {
			return getRuleContexts(LcExprContext.class);
		}
		public LcExprContext lcExpr(int i) {
			return getRuleContext(LcExprContext.class,i);
		}
		public LcExprsContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_lcExprs; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof ErlangListener ) ((ErlangListener)listener).enterLcExprs(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof ErlangListener ) ((ErlangListener)listener).exitLcExprs(this);
		}
	}

	public final LcExprsContext lcExprs() throws RecognitionException {
		LcExprsContext _localctx = new LcExprsContext(_ctx, getState());
		enterRule(_localctx, 160, RULE_lcExprs);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(881);
			lcExpr();
			setState(886);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==T__5) {
				{
				{
				setState(882);
				match(T__5);
				setState(883);
				lcExpr();
				}
				}
				setState(888);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class LcExprContext extends ParserRuleContext {
		public List<ExprContext> expr() {
			return getRuleContexts(ExprContext.class);
		}
		public ExprContext expr(int i) {
			return getRuleContext(ExprContext.class,i);
		}
		public BinaryContext binary() {
			return getRuleContext(BinaryContext.class,0);
		}
		public LcExprContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_lcExpr; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof ErlangListener ) ((ErlangListener)listener).enterLcExpr(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof ErlangListener ) ((ErlangListener)listener).exitLcExpr(this);
		}
	}

	public final LcExprContext lcExpr() throws RecognitionException {
		LcExprContext _localctx = new LcExprContext(_ctx, getState());
		enterRule(_localctx, 162, RULE_lcExpr);
		try {
			setState(898);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,62,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(889);
				expr();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(890);
				expr();
				setState(891);
				match(T__33);
				setState(892);
				expr();
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(894);
				binary();
				setState(895);
				match(T__34);
				setState(896);
				expr();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Re_tupleContext extends ParserRuleContext {
		public ExprsContext exprs() {
			return getRuleContext(ExprsContext.class,0);
		}
		public Re_tupleContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_re_tuple; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof ErlangListener ) ((ErlangListener)listener).enterRe_tuple(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof ErlangListener ) ((ErlangListener)listener).exitRe_tuple(this);
		}
	}

	public final Re_tupleContext re_tuple() throws RecognitionException {
		Re_tupleContext _localctx = new Re_tupleContext(_ctx, getState());
		enterRule(_localctx, 164, RULE_re_tuple);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(900);
			match(T__7);
			setState(902);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & 33742374977804L) != 0) || ((((_la - 65)) & ~0x3f) == 0 && ((1L << (_la - 65)) & 63L) != 0)) {
				{
				setState(901);
				exprs();
				}
			}

			setState(904);
			match(T__8);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class MapExprContext extends ParserRuleContext {
		public MapTupleContext mapTuple() {
			return getRuleContext(MapTupleContext.class,0);
		}
		public ExprMaxContext exprMax() {
			return getRuleContext(ExprMaxContext.class,0);
		}
		public MapExprContext mapExpr() {
			return getRuleContext(MapExprContext.class,0);
		}
		public MapExprContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_mapExpr; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof ErlangListener ) ((ErlangListener)listener).enterMapExpr(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof ErlangListener ) ((ErlangListener)listener).exitMapExpr(this);
		}
	}

	public final MapExprContext mapExpr() throws RecognitionException {
		return mapExpr(0);
	}

	private MapExprContext mapExpr(int _p) throws RecognitionException {
		ParserRuleContext _parentctx = _ctx;
		int _parentState = getState();
		MapExprContext _localctx = new MapExprContext(_ctx, _parentState);
		MapExprContext _prevctx = _localctx;
		int _startState = 166;
		enterRecursionRule(_localctx, 166, RULE_mapExpr, _p);
		int _la;
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			{
			setState(908);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & 2956015714568L) != 0) || ((((_la - 65)) & ~0x3f) == 0 && ((1L << (_la - 65)) & 63L) != 0)) {
				{
				setState(907);
				exprMax();
				}
			}

			setState(910);
			match(T__16);
			setState(911);
			mapTuple();
			}
			_ctx.stop = _input.LT(-1);
			setState(918);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,65,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					{
					_localctx = new MapExprContext(_parentctx, _parentState);
					pushNewRecursionContext(_localctx, _startState, RULE_mapExpr);
					setState(913);
					if (!(precpred(_ctx, 1))) throw new FailedPredicateException(this, "precpred(_ctx, 1)");
					setState(914);
					match(T__16);
					setState(915);
					mapTuple();
					}
					} 
				}
				setState(920);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,65,_ctx);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			unrollRecursionContexts(_parentctx);
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class MapTupleContext extends ParserRuleContext {
		public List<MapFieldContext> mapField() {
			return getRuleContexts(MapFieldContext.class);
		}
		public MapFieldContext mapField(int i) {
			return getRuleContext(MapFieldContext.class,i);
		}
		public MapTupleContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_mapTuple; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof ErlangListener ) ((ErlangListener)listener).enterMapTuple(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof ErlangListener ) ((ErlangListener)listener).exitMapTuple(this);
		}
	}

	public final MapTupleContext mapTuple() throws RecognitionException {
		MapTupleContext _localctx = new MapTupleContext(_ctx, getState());
		enterRule(_localctx, 168, RULE_mapTuple);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(921);
			match(T__7);
			setState(930);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & 33742374977804L) != 0) || ((((_la - 65)) & ~0x3f) == 0 && ((1L << (_la - 65)) & 63L) != 0)) {
				{
				setState(922);
				mapField();
				setState(927);
				_errHandler.sync(this);
				_la = _input.LA(1);
				while (_la==T__5) {
					{
					{
					setState(923);
					match(T__5);
					setState(924);
					mapField();
					}
					}
					setState(929);
					_errHandler.sync(this);
					_la = _input.LA(1);
				}
				}
			}

			setState(932);
			match(T__8);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class MapFieldContext extends ParserRuleContext {
		public MapFieldAssocContext mapFieldAssoc() {
			return getRuleContext(MapFieldAssocContext.class,0);
		}
		public MapFieldExactContext mapFieldExact() {
			return getRuleContext(MapFieldExactContext.class,0);
		}
		public MapFieldContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_mapField; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof ErlangListener ) ((ErlangListener)listener).enterMapField(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof ErlangListener ) ((ErlangListener)listener).exitMapField(this);
		}
	}

	public final MapFieldContext mapField() throws RecognitionException {
		MapFieldContext _localctx = new MapFieldContext(_ctx, getState());
		enterRule(_localctx, 170, RULE_mapField);
		try {
			setState(936);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,68,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(934);
				mapFieldAssoc();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(935);
				mapFieldExact();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class MapFieldAssocContext extends ParserRuleContext {
		public MapKeyContext mapKey() {
			return getRuleContext(MapKeyContext.class,0);
		}
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public MapFieldAssocContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_mapFieldAssoc; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof ErlangListener ) ((ErlangListener)listener).enterMapFieldAssoc(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof ErlangListener ) ((ErlangListener)listener).exitMapFieldAssoc(this);
		}
	}

	public final MapFieldAssocContext mapFieldAssoc() throws RecognitionException {
		MapFieldAssocContext _localctx = new MapFieldAssocContext(_ctx, getState());
		enterRule(_localctx, 172, RULE_mapFieldAssoc);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(938);
			mapKey();
			setState(939);
			match(T__19);
			setState(940);
			expr();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class MapFieldExactContext extends ParserRuleContext {
		public MapKeyContext mapKey() {
			return getRuleContext(MapKeyContext.class,0);
		}
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public MapFieldExactContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_mapFieldExact; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof ErlangListener ) ((ErlangListener)listener).enterMapFieldExact(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof ErlangListener ) ((ErlangListener)listener).exitMapFieldExact(this);
		}
	}

	public final MapFieldExactContext mapFieldExact() throws RecognitionException {
		MapFieldExactContext _localctx = new MapFieldExactContext(_ctx, getState());
		enterRule(_localctx, 174, RULE_mapFieldExact);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(942);
			mapKey();
			setState(943);
			match(T__20);
			setState(944);
			expr();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class MapKeyContext extends ParserRuleContext {
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public MapKeyContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_mapKey; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof ErlangListener ) ((ErlangListener)listener).enterMapKey(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof ErlangListener ) ((ErlangListener)listener).exitMapKey(this);
		}
	}

	public final MapKeyContext mapKey() throws RecognitionException {
		MapKeyContext _localctx = new MapKeyContext(_ctx, getState());
		enterRule(_localctx, 176, RULE_mapKey);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(946);
			expr();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class RecordExprContext extends ParserRuleContext {
		public List<TokAtomContext> tokAtom() {
			return getRuleContexts(TokAtomContext.class);
		}
		public TokAtomContext tokAtom(int i) {
			return getRuleContext(TokAtomContext.class,i);
		}
		public RecordTupleContext recordTuple() {
			return getRuleContext(RecordTupleContext.class,0);
		}
		public ExprMaxContext exprMax() {
			return getRuleContext(ExprMaxContext.class,0);
		}
		public RecordExprContext recordExpr() {
			return getRuleContext(RecordExprContext.class,0);
		}
		public RecordExprContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_recordExpr; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof ErlangListener ) ((ErlangListener)listener).enterRecordExpr(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof ErlangListener ) ((ErlangListener)listener).exitRecordExpr(this);
		}
	}

	public final RecordExprContext recordExpr() throws RecognitionException {
		return recordExpr(0);
	}

	private RecordExprContext recordExpr(int _p) throws RecognitionException {
		ParserRuleContext _parentctx = _ctx;
		int _parentState = getState();
		RecordExprContext _localctx = new RecordExprContext(_ctx, _parentState);
		RecordExprContext _prevctx = _localctx;
		int _startState = 178;
		enterRecursionRule(_localctx, 178, RULE_recordExpr, _p);
		int _la;
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			{
			setState(950);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & 2956015714568L) != 0) || ((((_la - 65)) & ~0x3f) == 0 && ((1L << (_la - 65)) & 63L) != 0)) {
				{
				setState(949);
				exprMax();
				}
			}

			setState(952);
			match(T__16);
			setState(953);
			tokAtom();
			setState(957);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case T__0:
				{
				setState(954);
				match(T__0);
				setState(955);
				tokAtom();
				}
				break;
			case T__7:
				{
				setState(956);
				recordTuple();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
			}
			_ctx.stop = _input.LT(-1);
			setState(969);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,72,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					{
					_localctx = new RecordExprContext(_parentctx, _parentState);
					pushNewRecursionContext(_localctx, _startState, RULE_recordExpr);
					setState(959);
					if (!(precpred(_ctx, 1))) throw new FailedPredicateException(this, "precpred(_ctx, 1)");
					setState(960);
					match(T__16);
					setState(961);
					tokAtom();
					setState(965);
					_errHandler.sync(this);
					switch (_input.LA(1)) {
					case T__0:
						{
						setState(962);
						match(T__0);
						setState(963);
						tokAtom();
						}
						break;
					case T__7:
						{
						setState(964);
						recordTuple();
						}
						break;
					default:
						throw new NoViableAltException(this);
					}
					}
					} 
				}
				setState(971);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,72,_ctx);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			unrollRecursionContexts(_parentctx);
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class RecordTupleContext extends ParserRuleContext {
		public RecordFieldsContext recordFields() {
			return getRuleContext(RecordFieldsContext.class,0);
		}
		public RecordTupleContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_recordTuple; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof ErlangListener ) ((ErlangListener)listener).enterRecordTuple(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof ErlangListener ) ((ErlangListener)listener).exitRecordTuple(this);
		}
	}

	public final RecordTupleContext recordTuple() throws RecognitionException {
		RecordTupleContext _localctx = new RecordTupleContext(_ctx, getState());
		enterRule(_localctx, 180, RULE_recordTuple);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(972);
			match(T__7);
			setState(974);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==TokAtom || _la==TokVar) {
				{
				setState(973);
				recordFields();
				}
			}

			setState(976);
			match(T__8);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class RecordFieldsContext extends ParserRuleContext {
		public List<RecordFieldContext> recordField() {
			return getRuleContexts(RecordFieldContext.class);
		}
		public RecordFieldContext recordField(int i) {
			return getRuleContext(RecordFieldContext.class,i);
		}
		public RecordFieldsContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_recordFields; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof ErlangListener ) ((ErlangListener)listener).enterRecordFields(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof ErlangListener ) ((ErlangListener)listener).exitRecordFields(this);
		}
	}

	public final RecordFieldsContext recordFields() throws RecognitionException {
		RecordFieldsContext _localctx = new RecordFieldsContext(_ctx, getState());
		enterRule(_localctx, 182, RULE_recordFields);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(978);
			recordField();
			setState(983);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==T__5) {
				{
				{
				setState(979);
				match(T__5);
				setState(980);
				recordField();
				}
				}
				setState(985);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class RecordFieldContext extends ParserRuleContext {
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public TokVarContext tokVar() {
			return getRuleContext(TokVarContext.class,0);
		}
		public TokAtomContext tokAtom() {
			return getRuleContext(TokAtomContext.class,0);
		}
		public RecordFieldContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_recordField; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof ErlangListener ) ((ErlangListener)listener).enterRecordField(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof ErlangListener ) ((ErlangListener)listener).exitRecordField(this);
		}
	}

	public final RecordFieldContext recordField() throws RecognitionException {
		RecordFieldContext _localctx = new RecordFieldContext(_ctx, getState());
		enterRule(_localctx, 184, RULE_recordField);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(988);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case TokVar:
				{
				setState(986);
				tokVar();
				}
				break;
			case TokAtom:
				{
				setState(987);
				tokAtom();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
			setState(990);
			match(T__25);
			setState(991);
			expr();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class FunctionCallContext extends ParserRuleContext {
		public Expr800Context expr800() {
			return getRuleContext(Expr800Context.class,0);
		}
		public ArgumentListContext argumentList() {
			return getRuleContext(ArgumentListContext.class,0);
		}
		public FunctionCallContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_functionCall; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof ErlangListener ) ((ErlangListener)listener).enterFunctionCall(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof ErlangListener ) ((ErlangListener)listener).exitFunctionCall(this);
		}
	}

	public final FunctionCallContext functionCall() throws RecognitionException {
		FunctionCallContext _localctx = new FunctionCallContext(_ctx, getState());
		enterRule(_localctx, 186, RULE_functionCall);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(993);
			expr800();
			setState(994);
			argumentList();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class IfExprContext extends ParserRuleContext {
		public IfClausesContext ifClauses() {
			return getRuleContext(IfClausesContext.class,0);
		}
		public IfExprContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_ifExpr; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof ErlangListener ) ((ErlangListener)listener).enterIfExpr(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof ErlangListener ) ((ErlangListener)listener).exitIfExpr(this);
		}
	}

	public final IfExprContext ifExpr() throws RecognitionException {
		IfExprContext _localctx = new IfExprContext(_ctx, getState());
		enterRule(_localctx, 188, RULE_ifExpr);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(996);
			match(T__35);
			setState(997);
			ifClauses();
			setState(998);
			match(T__30);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class IfClausesContext extends ParserRuleContext {
		public List<IfClauseContext> ifClause() {
			return getRuleContexts(IfClauseContext.class);
		}
		public IfClauseContext ifClause(int i) {
			return getRuleContext(IfClauseContext.class,i);
		}
		public IfClausesContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_ifClauses; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof ErlangListener ) ((ErlangListener)listener).enterIfClauses(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof ErlangListener ) ((ErlangListener)listener).exitIfClauses(this);
		}
	}

	public final IfClausesContext ifClauses() throws RecognitionException {
		IfClausesContext _localctx = new IfClausesContext(_ctx, getState());
		enterRule(_localctx, 190, RULE_ifClauses);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(1000);
			ifClause();
			setState(1005);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==T__9) {
				{
				{
				setState(1001);
				match(T__9);
				setState(1002);
				ifClause();
				}
				}
				setState(1007);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class IfClauseContext extends ParserRuleContext {
		public GuardContext guard() {
			return getRuleContext(GuardContext.class,0);
		}
		public ClauseBodyContext clauseBody() {
			return getRuleContext(ClauseBodyContext.class,0);
		}
		public IfClauseContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_ifClause; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof ErlangListener ) ((ErlangListener)listener).enterIfClause(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof ErlangListener ) ((ErlangListener)listener).exitIfClause(this);
		}
	}

	public final IfClauseContext ifClause() throws RecognitionException {
		IfClauseContext _localctx = new IfClauseContext(_ctx, getState());
		enterRule(_localctx, 192, RULE_ifClause);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(1008);
			guard();
			setState(1009);
			clauseBody();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class CaseExprContext extends ParserRuleContext {
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public CrClausesContext crClauses() {
			return getRuleContext(CrClausesContext.class,0);
		}
		public CaseExprContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_caseExpr; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof ErlangListener ) ((ErlangListener)listener).enterCaseExpr(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof ErlangListener ) ((ErlangListener)listener).exitCaseExpr(this);
		}
	}

	public final CaseExprContext caseExpr() throws RecognitionException {
		CaseExprContext _localctx = new CaseExprContext(_ctx, getState());
		enterRule(_localctx, 194, RULE_caseExpr);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(1011);
			match(T__36);
			setState(1012);
			expr();
			setState(1013);
			match(T__37);
			setState(1014);
			crClauses();
			setState(1015);
			match(T__30);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class CrClausesContext extends ParserRuleContext {
		public List<CrClauseContext> crClause() {
			return getRuleContexts(CrClauseContext.class);
		}
		public CrClauseContext crClause(int i) {
			return getRuleContext(CrClauseContext.class,i);
		}
		public CrClausesContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_crClauses; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof ErlangListener ) ((ErlangListener)listener).enterCrClauses(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof ErlangListener ) ((ErlangListener)listener).exitCrClauses(this);
		}
	}

	public final CrClausesContext crClauses() throws RecognitionException {
		CrClausesContext _localctx = new CrClausesContext(_ctx, getState());
		enterRule(_localctx, 196, RULE_crClauses);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(1017);
			crClause();
			setState(1022);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==T__9) {
				{
				{
				setState(1018);
				match(T__9);
				setState(1019);
				crClause();
				}
				}
				setState(1024);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class CrClauseContext extends ParserRuleContext {
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public ClauseGuardContext clauseGuard() {
			return getRuleContext(ClauseGuardContext.class,0);
		}
		public ClauseBodyContext clauseBody() {
			return getRuleContext(ClauseBodyContext.class,0);
		}
		public CrClauseContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_crClause; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof ErlangListener ) ((ErlangListener)listener).enterCrClause(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof ErlangListener ) ((ErlangListener)listener).exitCrClause(this);
		}
	}

	public final CrClauseContext crClause() throws RecognitionException {
		CrClauseContext _localctx = new CrClauseContext(_ctx, getState());
		enterRule(_localctx, 198, RULE_crClause);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(1025);
			expr();
			setState(1026);
			clauseGuard();
			setState(1027);
			clauseBody();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ReceiveExprContext extends ParserRuleContext {
		public CrClausesContext crClauses() {
			return getRuleContext(CrClausesContext.class,0);
		}
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public ClauseBodyContext clauseBody() {
			return getRuleContext(ClauseBodyContext.class,0);
		}
		public ReceiveExprContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_receiveExpr; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof ErlangListener ) ((ErlangListener)listener).enterReceiveExpr(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof ErlangListener ) ((ErlangListener)listener).exitReceiveExpr(this);
		}
	}

	public final ReceiveExprContext receiveExpr() throws RecognitionException {
		ReceiveExprContext _localctx = new ReceiveExprContext(_ctx, getState());
		enterRule(_localctx, 200, RULE_receiveExpr);
		try {
			setState(1046);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,78,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(1029);
				match(T__38);
				setState(1030);
				crClauses();
				setState(1031);
				match(T__30);
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(1033);
				match(T__38);
				setState(1034);
				match(T__39);
				setState(1035);
				expr();
				setState(1036);
				clauseBody();
				setState(1037);
				match(T__30);
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(1039);
				match(T__38);
				setState(1040);
				crClauses();
				setState(1041);
				match(T__39);
				setState(1042);
				expr();
				setState(1043);
				clauseBody();
				setState(1044);
				match(T__30);
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class FunExprContext extends ParserRuleContext {
		public TokAtomContext tokAtom() {
			return getRuleContext(TokAtomContext.class,0);
		}
		public TokIntegerContext tokInteger() {
			return getRuleContext(TokIntegerContext.class,0);
		}
		public List<AtomOrVarContext> atomOrVar() {
			return getRuleContexts(AtomOrVarContext.class);
		}
		public AtomOrVarContext atomOrVar(int i) {
			return getRuleContext(AtomOrVarContext.class,i);
		}
		public IntegerOrVarContext integerOrVar() {
			return getRuleContext(IntegerOrVarContext.class,0);
		}
		public FunClausesContext funClauses() {
			return getRuleContext(FunClausesContext.class,0);
		}
		public FunExprContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_funExpr; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof ErlangListener ) ((ErlangListener)listener).enterFunExpr(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof ErlangListener ) ((ErlangListener)listener).exitFunExpr(this);
		}
	}

	public final FunExprContext funExpr() throws RecognitionException {
		FunExprContext _localctx = new FunExprContext(_ctx, getState());
		enterRule(_localctx, 202, RULE_funExpr);
		try {
			setState(1064);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,79,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(1048);
				match(T__17);
				setState(1049);
				tokAtom();
				setState(1050);
				match(T__31);
				setState(1051);
				tokInteger();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(1053);
				match(T__17);
				setState(1054);
				atomOrVar();
				setState(1055);
				match(T__4);
				setState(1056);
				atomOrVar();
				setState(1057);
				match(T__31);
				setState(1058);
				integerOrVar();
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(1060);
				match(T__17);
				setState(1061);
				funClauses();
				setState(1062);
				match(T__30);
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class AtomOrVarContext extends ParserRuleContext {
		public TokAtomContext tokAtom() {
			return getRuleContext(TokAtomContext.class,0);
		}
		public TokVarContext tokVar() {
			return getRuleContext(TokVarContext.class,0);
		}
		public AtomOrVarContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_atomOrVar; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof ErlangListener ) ((ErlangListener)listener).enterAtomOrVar(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof ErlangListener ) ((ErlangListener)listener).exitAtomOrVar(this);
		}
	}

	public final AtomOrVarContext atomOrVar() throws RecognitionException {
		AtomOrVarContext _localctx = new AtomOrVarContext(_ctx, getState());
		enterRule(_localctx, 204, RULE_atomOrVar);
		try {
			setState(1068);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case TokAtom:
				enterOuterAlt(_localctx, 1);
				{
				setState(1066);
				tokAtom();
				}
				break;
			case TokVar:
				enterOuterAlt(_localctx, 2);
				{
				setState(1067);
				tokVar();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class IntegerOrVarContext extends ParserRuleContext {
		public TokIntegerContext tokInteger() {
			return getRuleContext(TokIntegerContext.class,0);
		}
		public TokVarContext tokVar() {
			return getRuleContext(TokVarContext.class,0);
		}
		public IntegerOrVarContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_integerOrVar; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof ErlangListener ) ((ErlangListener)listener).enterIntegerOrVar(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof ErlangListener ) ((ErlangListener)listener).exitIntegerOrVar(this);
		}
	}

	public final IntegerOrVarContext integerOrVar() throws RecognitionException {
		IntegerOrVarContext _localctx = new IntegerOrVarContext(_ctx, getState());
		enterRule(_localctx, 206, RULE_integerOrVar);
		try {
			setState(1072);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case TokInteger:
				enterOuterAlt(_localctx, 1);
				{
				setState(1070);
				tokInteger();
				}
				break;
			case TokVar:
				enterOuterAlt(_localctx, 2);
				{
				setState(1071);
				tokVar();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class FunClausesContext extends ParserRuleContext {
		public List<FunClauseContext> funClause() {
			return getRuleContexts(FunClauseContext.class);
		}
		public FunClauseContext funClause(int i) {
			return getRuleContext(FunClauseContext.class,i);
		}
		public FunClausesContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_funClauses; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof ErlangListener ) ((ErlangListener)listener).enterFunClauses(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof ErlangListener ) ((ErlangListener)listener).exitFunClauses(this);
		}
	}

	public final FunClausesContext funClauses() throws RecognitionException {
		FunClausesContext _localctx = new FunClausesContext(_ctx, getState());
		enterRule(_localctx, 208, RULE_funClauses);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(1074);
			funClause();
			setState(1079);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==T__9) {
				{
				{
				setState(1075);
				match(T__9);
				setState(1076);
				funClause();
				}
				}
				setState(1081);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class FunClauseContext extends ParserRuleContext {
		public PatArgumentListContext patArgumentList() {
			return getRuleContext(PatArgumentListContext.class,0);
		}
		public ClauseGuardContext clauseGuard() {
			return getRuleContext(ClauseGuardContext.class,0);
		}
		public ClauseBodyContext clauseBody() {
			return getRuleContext(ClauseBodyContext.class,0);
		}
		public TokVarContext tokVar() {
			return getRuleContext(TokVarContext.class,0);
		}
		public FunClauseContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_funClause; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof ErlangListener ) ((ErlangListener)listener).enterFunClause(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof ErlangListener ) ((ErlangListener)listener).exitFunClause(this);
		}
	}

	public final FunClauseContext funClause() throws RecognitionException {
		FunClauseContext _localctx = new FunClauseContext(_ctx, getState());
		enterRule(_localctx, 210, RULE_funClause);
		try {
			setState(1091);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case T__2:
				enterOuterAlt(_localctx, 1);
				{
				setState(1082);
				patArgumentList();
				setState(1083);
				clauseGuard();
				setState(1084);
				clauseBody();
				}
				break;
			case TokVar:
				enterOuterAlt(_localctx, 2);
				{
				setState(1086);
				tokVar();
				setState(1087);
				patArgumentList();
				setState(1088);
				clauseGuard();
				setState(1089);
				clauseBody();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class TryExprContext extends ParserRuleContext {
		public ExprsContext exprs() {
			return getRuleContext(ExprsContext.class,0);
		}
		public TryCatchContext tryCatch() {
			return getRuleContext(TryCatchContext.class,0);
		}
		public CrClausesContext crClauses() {
			return getRuleContext(CrClausesContext.class,0);
		}
		public TryExprContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_tryExpr; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof ErlangListener ) ((ErlangListener)listener).enterTryExpr(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof ErlangListener ) ((ErlangListener)listener).exitTryExpr(this);
		}
	}

	public final TryExprContext tryExpr() throws RecognitionException {
		TryExprContext _localctx = new TryExprContext(_ctx, getState());
		enterRule(_localctx, 212, RULE_tryExpr);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(1093);
			match(T__40);
			setState(1094);
			exprs();
			setState(1097);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==T__37) {
				{
				setState(1095);
				match(T__37);
				setState(1096);
				crClauses();
				}
			}

			setState(1099);
			tryCatch();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class TryCatchContext extends ParserRuleContext {
		public TryClausesContext tryClauses() {
			return getRuleContext(TryClausesContext.class,0);
		}
		public ExprsContext exprs() {
			return getRuleContext(ExprsContext.class,0);
		}
		public TryCatchContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_tryCatch; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof ErlangListener ) ((ErlangListener)listener).enterTryCatch(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof ErlangListener ) ((ErlangListener)listener).exitTryCatch(this);
		}
	}

	public final TryCatchContext tryCatch() throws RecognitionException {
		TryCatchContext _localctx = new TryCatchContext(_ctx, getState());
		enterRule(_localctx, 214, RULE_tryCatch);
		try {
			setState(1115);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,85,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(1101);
				match(T__24);
				setState(1102);
				tryClauses();
				setState(1103);
				match(T__30);
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(1105);
				match(T__24);
				setState(1106);
				tryClauses();
				setState(1107);
				match(T__39);
				setState(1108);
				exprs();
				setState(1109);
				match(T__30);
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(1111);
				match(T__39);
				setState(1112);
				exprs();
				setState(1113);
				match(T__30);
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class TryClausesContext extends ParserRuleContext {
		public List<TryClauseContext> tryClause() {
			return getRuleContexts(TryClauseContext.class);
		}
		public TryClauseContext tryClause(int i) {
			return getRuleContext(TryClauseContext.class,i);
		}
		public TryClausesContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_tryClauses; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof ErlangListener ) ((ErlangListener)listener).enterTryClauses(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof ErlangListener ) ((ErlangListener)listener).exitTryClauses(this);
		}
	}

	public final TryClausesContext tryClauses() throws RecognitionException {
		TryClausesContext _localctx = new TryClausesContext(_ctx, getState());
		enterRule(_localctx, 216, RULE_tryClauses);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(1117);
			tryClause();
			setState(1122);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==T__9) {
				{
				{
				setState(1118);
				match(T__9);
				setState(1119);
				tryClause();
				}
				}
				setState(1124);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class TryClauseContext extends ParserRuleContext {
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public ClauseGuardContext clauseGuard() {
			return getRuleContext(ClauseGuardContext.class,0);
		}
		public ClauseBodyContext clauseBody() {
			return getRuleContext(ClauseBodyContext.class,0);
		}
		public PatExprContext patExpr() {
			return getRuleContext(PatExprContext.class,0);
		}
		public TryOptStackTraceContext tryOptStackTrace() {
			return getRuleContext(TryOptStackTraceContext.class,0);
		}
		public AtomOrVarContext atomOrVar() {
			return getRuleContext(AtomOrVarContext.class,0);
		}
		public TryClauseContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_tryClause; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof ErlangListener ) ((ErlangListener)listener).enterTryClause(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof ErlangListener ) ((ErlangListener)listener).exitTryClause(this);
		}
	}

	public final TryClauseContext tryClause() throws RecognitionException {
		TryClauseContext _localctx = new TryClauseContext(_ctx, getState());
		enterRule(_localctx, 218, RULE_tryClause);
		try {
			setState(1139);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,88,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(1125);
				expr();
				setState(1126);
				clauseGuard();
				setState(1127);
				clauseBody();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(1132);
				_errHandler.sync(this);
				switch ( getInterpreter().adaptivePredict(_input,87,_ctx) ) {
				case 1:
					{
					setState(1129);
					atomOrVar();
					setState(1130);
					match(T__4);
					}
					break;
				}
				setState(1134);
				patExpr();
				setState(1135);
				tryOptStackTrace();
				setState(1136);
				clauseGuard();
				setState(1137);
				clauseBody();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class TryOptStackTraceContext extends ParserRuleContext {
		public TokVarContext tokVar() {
			return getRuleContext(TokVarContext.class,0);
		}
		public TryOptStackTraceContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_tryOptStackTrace; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof ErlangListener ) ((ErlangListener)listener).enterTryOptStackTrace(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof ErlangListener ) ((ErlangListener)listener).exitTryOptStackTrace(this);
		}
	}

	public final TryOptStackTraceContext tryOptStackTrace() throws RecognitionException {
		TryOptStackTraceContext _localctx = new TryOptStackTraceContext(_ctx, getState());
		enterRule(_localctx, 220, RULE_tryOptStackTrace);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(1143);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==T__4) {
				{
				setState(1141);
				match(T__4);
				setState(1142);
				tokVar();
				}
			}

			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ArgumentListContext extends ParserRuleContext {
		public ExprsContext exprs() {
			return getRuleContext(ExprsContext.class,0);
		}
		public ArgumentListContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_argumentList; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof ErlangListener ) ((ErlangListener)listener).enterArgumentList(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof ErlangListener ) ((ErlangListener)listener).exitArgumentList(this);
		}
	}

	public final ArgumentListContext argumentList() throws RecognitionException {
		ArgumentListContext _localctx = new ArgumentListContext(_ctx, getState());
		enterRule(_localctx, 222, RULE_argumentList);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(1145);
			match(T__2);
			setState(1147);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & 33742374977804L) != 0) || ((((_la - 65)) & ~0x3f) == 0 && ((1L << (_la - 65)) & 63L) != 0)) {
				{
				setState(1146);
				exprs();
				}
			}

			setState(1149);
			match(T__3);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class PatArgumentListContext extends ParserRuleContext {
		public PatExprsContext patExprs() {
			return getRuleContext(PatExprsContext.class,0);
		}
		public PatArgumentListContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_patArgumentList; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof ErlangListener ) ((ErlangListener)listener).enterPatArgumentList(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof ErlangListener ) ((ErlangListener)listener).exitPatArgumentList(this);
		}
	}

	public final PatArgumentListContext patArgumentList() throws RecognitionException {
		PatArgumentListContext _localctx = new PatArgumentListContext(_ctx, getState());
		enterRule(_localctx, 224, RULE_patArgumentList);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(1151);
			match(T__2);
			setState(1153);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & 30786329919756L) != 0) || ((((_la - 65)) & ~0x3f) == 0 && ((1L << (_la - 65)) & 63L) != 0)) {
				{
				setState(1152);
				patExprs();
				}
			}

			setState(1155);
			match(T__3);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ExprsContext extends ParserRuleContext {
		public List<ExprContext> expr() {
			return getRuleContexts(ExprContext.class);
		}
		public ExprContext expr(int i) {
			return getRuleContext(ExprContext.class,i);
		}
		public ExprsContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_exprs; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof ErlangListener ) ((ErlangListener)listener).enterExprs(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof ErlangListener ) ((ErlangListener)listener).exitExprs(this);
		}
	}

	public final ExprsContext exprs() throws RecognitionException {
		ExprsContext _localctx = new ExprsContext(_ctx, getState());
		enterRule(_localctx, 226, RULE_exprs);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(1157);
			expr();
			setState(1162);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==T__5) {
				{
				{
				setState(1158);
				match(T__5);
				setState(1159);
				expr();
				}
				}
				setState(1164);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class PatExprsContext extends ParserRuleContext {
		public List<PatExprContext> patExpr() {
			return getRuleContexts(PatExprContext.class);
		}
		public PatExprContext patExpr(int i) {
			return getRuleContext(PatExprContext.class,i);
		}
		public PatExprsContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_patExprs; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof ErlangListener ) ((ErlangListener)listener).enterPatExprs(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof ErlangListener ) ((ErlangListener)listener).exitPatExprs(this);
		}
	}

	public final PatExprsContext patExprs() throws RecognitionException {
		PatExprsContext _localctx = new PatExprsContext(_ctx, getState());
		enterRule(_localctx, 228, RULE_patExprs);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(1165);
			patExpr();
			setState(1170);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==T__5) {
				{
				{
				setState(1166);
				match(T__5);
				setState(1167);
				patExpr();
				}
				}
				setState(1172);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class GuardContext extends ParserRuleContext {
		public List<ExprsContext> exprs() {
			return getRuleContexts(ExprsContext.class);
		}
		public ExprsContext exprs(int i) {
			return getRuleContext(ExprsContext.class,i);
		}
		public GuardContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_guard; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof ErlangListener ) ((ErlangListener)listener).enterGuard(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof ErlangListener ) ((ErlangListener)listener).exitGuard(this);
		}
	}

	public final GuardContext guard() throws RecognitionException {
		GuardContext _localctx = new GuardContext(_ctx, getState());
		enterRule(_localctx, 230, RULE_guard);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(1173);
			exprs();
			setState(1178);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==T__9) {
				{
				{
				setState(1174);
				match(T__9);
				setState(1175);
				exprs();
				}
				}
				setState(1180);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class AtomicContext extends ParserRuleContext {
		public TokCharContext tokChar() {
			return getRuleContext(TokCharContext.class,0);
		}
		public TokIntegerContext tokInteger() {
			return getRuleContext(TokIntegerContext.class,0);
		}
		public TokFloatContext tokFloat() {
			return getRuleContext(TokFloatContext.class,0);
		}
		public TokAtomContext tokAtom() {
			return getRuleContext(TokAtomContext.class,0);
		}
		public List<TokStringContext> tokString() {
			return getRuleContexts(TokStringContext.class);
		}
		public TokStringContext tokString(int i) {
			return getRuleContext(TokStringContext.class,i);
		}
		public AtomicContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_atomic; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof ErlangListener ) ((ErlangListener)listener).enterAtomic(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof ErlangListener ) ((ErlangListener)listener).exitAtomic(this);
		}
	}

	public final AtomicContext atomic() throws RecognitionException {
		AtomicContext _localctx = new AtomicContext(_ctx, getState());
		enterRule(_localctx, 232, RULE_atomic);
		try {
			int _alt;
			setState(1190);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case TokChar:
				enterOuterAlt(_localctx, 1);
				{
				setState(1181);
				tokChar();
				}
				break;
			case TokInteger:
				enterOuterAlt(_localctx, 2);
				{
				setState(1182);
				tokInteger();
				}
				break;
			case TokFloat:
				enterOuterAlt(_localctx, 3);
				{
				setState(1183);
				tokFloat();
				}
				break;
			case TokAtom:
				enterOuterAlt(_localctx, 4);
				{
				setState(1184);
				tokAtom();
				}
				break;
			case TokString:
				enterOuterAlt(_localctx, 5);
				{
				setState(1186); 
				_errHandler.sync(this);
				_alt = 1;
				do {
					switch (_alt) {
					case 1:
						{
						{
						setState(1185);
						tokString();
						}
						}
						break;
					default:
						throw new NoViableAltException(this);
					}
					setState(1188); 
					_errHandler.sync(this);
					_alt = getInterpreter().adaptivePredict(_input,95,_ctx);
				} while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER );
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class PrefixOpContext extends ParserRuleContext {
		public PrefixOpContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_prefixOp; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof ErlangListener ) ((ErlangListener)listener).enterPrefixOp(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof ErlangListener ) ((ErlangListener)listener).exitPrefixOp(this);
		}
	}

	public final PrefixOpContext prefixOp() throws RecognitionException {
		PrefixOpContext _localctx = new PrefixOpContext(_ctx, getState());
		enterRule(_localctx, 234, RULE_prefixOp);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(1192);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & 30786325577732L) != 0)) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class MultOpContext extends ParserRuleContext {
		public MultOpContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_multOp; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof ErlangListener ) ((ErlangListener)listener).enterMultOp(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof ErlangListener ) ((ErlangListener)listener).exitMultOp(this);
		}
	}

	public final MultOpContext multOp() throws RecognitionException {
		MultOpContext _localctx = new MultOpContext(_ctx, getState());
		enterRule(_localctx, 236, RULE_multOp);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(1194);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & 527769893076992L) != 0)) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class AddOpContext extends ParserRuleContext {
		public AddOpContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_addOp; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof ErlangListener ) ((ErlangListener)listener).enterAddOp(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof ErlangListener ) ((ErlangListener)listener).exitAddOp(this);
		}
	}

	public final AddOpContext addOp() throws RecognitionException {
		AddOpContext _localctx = new AddOpContext(_ctx, getState());
		enterRule(_localctx, 238, RULE_addOp);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(1196);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & 35470245112053764L) != 0)) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ListOpContext extends ParserRuleContext {
		public ListOpContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_listOp; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof ErlangListener ) ((ErlangListener)listener).enterListOp(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof ErlangListener ) ((ErlangListener)listener).exitListOp(this);
		}
	}

	public final ListOpContext listOp() throws RecognitionException {
		ListOpContext _localctx = new ListOpContext(_ctx, getState());
		enterRule(_localctx, 240, RULE_listOp);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(1198);
			_la = _input.LA(1);
			if ( !(_la==T__54 || _la==T__55) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class CompOpContext extends ParserRuleContext {
		public CompOpContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_compOp; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof ErlangListener ) ((ErlangListener)listener).enterCompOp(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof ErlangListener ) ((ErlangListener)listener).exitCompOp(this);
		}
	}

	public final CompOpContext compOp() throws RecognitionException {
		CompOpContext _localctx = new CompOpContext(_ctx, getState());
		enterRule(_localctx, 242, RULE_compOp);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(1200);
			_la = _input.LA(1);
			if ( !(((((_la - 57)) & ~0x3f) == 0 && ((1L << (_la - 57)) & 255L) != 0)) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public boolean sempred(RuleContext _localctx, int ruleIndex, int predIndex) {
		switch (ruleIndex) {
		case 23:
			return type300_sempred((Type300Context)_localctx, predIndex);
		case 24:
			return type400_sempred((Type400Context)_localctx, predIndex);
		case 58:
			return patExpr400_sempred((PatExpr400Context)_localctx, predIndex);
		case 59:
			return patExpr500_sempred((PatExpr500Context)_localctx, predIndex);
		case 65:
			return mapPatExpr_sempred((MapPatExprContext)_localctx, predIndex);
		case 83:
			return mapExpr_sempred((MapExprContext)_localctx, predIndex);
		case 89:
			return recordExpr_sempred((RecordExprContext)_localctx, predIndex);
		}
		return true;
	}
	private boolean type300_sempred(Type300Context _localctx, int predIndex) {
		switch (predIndex) {
		case 0:
			return precpred(_ctx, 2);
		}
		return true;
	}
	private boolean type400_sempred(Type400Context _localctx, int predIndex) {
		switch (predIndex) {
		case 1:
			return precpred(_ctx, 2);
		}
		return true;
	}
	private boolean patExpr400_sempred(PatExpr400Context _localctx, int predIndex) {
		switch (predIndex) {
		case 2:
			return precpred(_ctx, 2);
		}
		return true;
	}
	private boolean patExpr500_sempred(PatExpr500Context _localctx, int predIndex) {
		switch (predIndex) {
		case 3:
			return precpred(_ctx, 2);
		}
		return true;
	}
	private boolean mapPatExpr_sempred(MapPatExprContext _localctx, int predIndex) {
		switch (predIndex) {
		case 4:
			return precpred(_ctx, 1);
		}
		return true;
	}
	private boolean mapExpr_sempred(MapExprContext _localctx, int predIndex) {
		switch (predIndex) {
		case 5:
			return precpred(_ctx, 1);
		}
		return true;
	}
	private boolean recordExpr_sempred(RecordExprContext _localctx, int predIndex) {
		switch (predIndex) {
		case 6:
			return precpred(_ctx, 1);
		}
		return true;
	}

	public static final String _serializedATN =
		"\u0004\u0001I\u04b3\u0002\u0000\u0007\u0000\u0002\u0001\u0007\u0001\u0002"+
		"\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002\u0004\u0007\u0004\u0002"+
		"\u0005\u0007\u0005\u0002\u0006\u0007\u0006\u0002\u0007\u0007\u0007\u0002"+
		"\b\u0007\b\u0002\t\u0007\t\u0002\n\u0007\n\u0002\u000b\u0007\u000b\u0002"+
		"\f\u0007\f\u0002\r\u0007\r\u0002\u000e\u0007\u000e\u0002\u000f\u0007\u000f"+
		"\u0002\u0010\u0007\u0010\u0002\u0011\u0007\u0011\u0002\u0012\u0007\u0012"+
		"\u0002\u0013\u0007\u0013\u0002\u0014\u0007\u0014\u0002\u0015\u0007\u0015"+
		"\u0002\u0016\u0007\u0016\u0002\u0017\u0007\u0017\u0002\u0018\u0007\u0018"+
		"\u0002\u0019\u0007\u0019\u0002\u001a\u0007\u001a\u0002\u001b\u0007\u001b"+
		"\u0002\u001c\u0007\u001c\u0002\u001d\u0007\u001d\u0002\u001e\u0007\u001e"+
		"\u0002\u001f\u0007\u001f\u0002 \u0007 \u0002!\u0007!\u0002\"\u0007\"\u0002"+
		"#\u0007#\u0002$\u0007$\u0002%\u0007%\u0002&\u0007&\u0002\'\u0007\'\u0002"+
		"(\u0007(\u0002)\u0007)\u0002*\u0007*\u0002+\u0007+\u0002,\u0007,\u0002"+
		"-\u0007-\u0002.\u0007.\u0002/\u0007/\u00020\u00070\u00021\u00071\u0002"+
		"2\u00072\u00023\u00073\u00024\u00074\u00025\u00075\u00026\u00076\u0002"+
		"7\u00077\u00028\u00078\u00029\u00079\u0002:\u0007:\u0002;\u0007;\u0002"+
		"<\u0007<\u0002=\u0007=\u0002>\u0007>\u0002?\u0007?\u0002@\u0007@\u0002"+
		"A\u0007A\u0002B\u0007B\u0002C\u0007C\u0002D\u0007D\u0002E\u0007E\u0002"+
		"F\u0007F\u0002G\u0007G\u0002H\u0007H\u0002I\u0007I\u0002J\u0007J\u0002"+
		"K\u0007K\u0002L\u0007L\u0002M\u0007M\u0002N\u0007N\u0002O\u0007O\u0002"+
		"P\u0007P\u0002Q\u0007Q\u0002R\u0007R\u0002S\u0007S\u0002T\u0007T\u0002"+
		"U\u0007U\u0002V\u0007V\u0002W\u0007W\u0002X\u0007X\u0002Y\u0007Y\u0002"+
		"Z\u0007Z\u0002[\u0007[\u0002\\\u0007\\\u0002]\u0007]\u0002^\u0007^\u0002"+
		"_\u0007_\u0002`\u0007`\u0002a\u0007a\u0002b\u0007b\u0002c\u0007c\u0002"+
		"d\u0007d\u0002e\u0007e\u0002f\u0007f\u0002g\u0007g\u0002h\u0007h\u0002"+
		"i\u0007i\u0002j\u0007j\u0002k\u0007k\u0002l\u0007l\u0002m\u0007m\u0002"+
		"n\u0007n\u0002o\u0007o\u0002p\u0007p\u0002q\u0007q\u0002r\u0007r\u0002"+
		"s\u0007s\u0002t\u0007t\u0002u\u0007u\u0002v\u0007v\u0002w\u0007w\u0002"+
		"x\u0007x\u0002y\u0007y\u0001\u0000\u0004\u0000\u00f6\b\u0000\u000b\u0000"+
		"\f\u0000\u00f7\u0001\u0000\u0001\u0000\u0001\u0001\u0001\u0001\u0003\u0001"+
		"\u00fe\b\u0001\u0001\u0001\u0001\u0001\u0001\u0002\u0001\u0002\u0001\u0003"+
		"\u0001\u0003\u0001\u0004\u0001\u0004\u0001\u0005\u0001\u0005\u0001\u0006"+
		"\u0001\u0006\u0001\u0007\u0001\u0007\u0001\b\u0001\b\u0001\b\u0001\b\u0001"+
		"\b\u0001\b\u0001\b\u0001\b\u0001\b\u0001\b\u0001\b\u0001\b\u0001\b\u0001"+
		"\b\u0001\b\u0001\b\u0003\b\u011e\b\b\u0001\t\u0001\t\u0001\t\u0001\t\u0001"+
		"\t\u0001\t\u0001\t\u0001\t\u0003\t\u0128\b\t\u0001\n\u0001\n\u0001\n\u0001"+
		"\n\u0001\n\u0003\n\u012f\b\n\u0001\u000b\u0001\u000b\u0001\u000b\u0001"+
		"\u000b\u0001\u000b\u0001\u000b\u0001\u000b\u0001\u000b\u0003\u000b\u0139"+
		"\b\u000b\u0001\f\u0001\f\u0001\f\u0001\f\u0001\r\u0001\r\u0001\r\u0001"+
		"\r\u0001\r\u0001\r\u0001\r\u0001\r\u0001\r\u0001\r\u0001\r\u0001\r\u0001"+
		"\r\u0003\r\u014c\b\r\u0001\u000e\u0001\u000e\u0001\u000e\u0001\u000e\u0001"+
		"\u000f\u0001\u000f\u0001\u000f\u0005\u000f\u0155\b\u000f\n\u000f\f\u000f"+
		"\u0158\t\u000f\u0001\u0010\u0001\u0010\u0001\u0010\u0003\u0010\u015d\b"+
		"\u0010\u0001\u0011\u0001\u0011\u0001\u0011\u0005\u0011\u0162\b\u0011\n"+
		"\u0011\f\u0011\u0165\t\u0011\u0001\u0012\u0001\u0012\u0001\u0012\u0001"+
		"\u0012\u0001\u0012\u0001\u0012\u0001\u0012\u0001\u0012\u0001\u0012\u0003"+
		"\u0012\u0170\b\u0012\u0001\u0013\u0001\u0013\u0001\u0013\u0005\u0013\u0175"+
		"\b\u0013\n\u0013\f\u0013\u0178\t\u0013\u0001\u0014\u0001\u0014\u0001\u0014"+
		"\u0003\u0014\u017d\b\u0014\u0001\u0014\u0001\u0014\u0001\u0015\u0001\u0015"+
		"\u0001\u0015\u0003\u0015\u0184\b\u0015\u0001\u0016\u0001\u0016\u0001\u0016"+
		"\u0003\u0016\u0189\b\u0016\u0001\u0017\u0001\u0017\u0001\u0017\u0001\u0017"+
		"\u0001\u0017\u0001\u0017\u0001\u0017\u0005\u0017\u0192\b\u0017\n\u0017"+
		"\f\u0017\u0195\t\u0017\u0001\u0018\u0001\u0018\u0001\u0018\u0001\u0018"+
		"\u0001\u0018\u0001\u0018\u0001\u0018\u0005\u0018\u019e\b\u0018\n\u0018"+
		"\f\u0018\u01a1\t\u0018\u0001\u0019\u0003\u0019\u01a4\b\u0019\u0001\u0019"+
		"\u0001\u0019\u0001\u001a\u0001\u001a\u0001\u001a\u0001\u001a\u0001\u001a"+
		"\u0001\u001a\u0001\u001a\u0001\u001a\u0001\u001a\u0001\u001a\u0001\u001a"+
		"\u0001\u001a\u0001\u001a\u0001\u001a\u0001\u001a\u0001\u001a\u0001\u001a"+
		"\u0001\u001a\u0001\u001a\u0001\u001a\u0001\u001a\u0001\u001a\u0001\u001a"+
		"\u0001\u001a\u0001\u001a\u0001\u001a\u0001\u001a\u0001\u001a\u0001\u001a"+
		"\u0001\u001a\u0001\u001a\u0001\u001a\u0001\u001a\u0001\u001a\u0001\u001a"+
		"\u0001\u001a\u0001\u001a\u0001\u001a\u0001\u001a\u0001\u001a\u0001\u001a"+
		"\u0001\u001a\u0001\u001a\u0001\u001a\u0001\u001a\u0001\u001a\u0001\u001a"+
		"\u0001\u001a\u0001\u001a\u0001\u001a\u0001\u001a\u0001\u001a\u0001\u001a"+
		"\u0001\u001a\u0001\u001a\u0001\u001a\u0001\u001a\u0001\u001a\u0001\u001a"+
		"\u0001\u001a\u0001\u001a\u0001\u001a\u0001\u001a\u0001\u001a\u0001\u001a"+
		"\u0001\u001a\u0001\u001a\u0001\u001a\u0001\u001a\u0001\u001a\u0001\u001a"+
		"\u0001\u001a\u0001\u001a\u0001\u001a\u0001\u001a\u0001\u001a\u0003\u001a"+
		"\u01f4\b\u001a\u0001\u001b\u0001\u001b\u0001\u001b\u0001\u001b\u0001\u001b"+
		"\u0001\u001b\u0003\u001b\u01fc\b\u001b\u0001\u001c\u0001\u001c\u0003\u001c"+
		"\u0200\b\u001c\u0001\u001c\u0001\u001c\u0001\u001c\u0001\u001c\u0001\u001d"+
		"\u0001\u001d\u0001\u001d\u0005\u001d\u0209\b\u001d\n\u001d\f\u001d\u020c"+
		"\t\u001d\u0001\u001e\u0001\u001e\u0001\u001e\u0001\u001e\u0001\u001f\u0001"+
		"\u001f\u0001\u001f\u0005\u001f\u0215\b\u001f\n\u001f\f\u001f\u0218\t\u001f"+
		"\u0001 \u0001 \u0001 \u0001 \u0001!\u0001!\u0001!\u0001!\u0001!\u0001"+
		"!\u0001!\u0001!\u0001!\u0001!\u0001!\u0001!\u0001!\u0001!\u0001!\u0001"+
		"!\u0003!\u022e\b!\u0001\"\u0001\"\u0001\"\u0001\"\u0001#\u0001#\u0001"+
		"#\u0001#\u0001#\u0001#\u0001$\u0001$\u0001$\u0001$\u0001$\u0001$\u0001"+
		"$\u0001$\u0001$\u0001$\u0001$\u0001$\u0001$\u0001$\u0001$\u0003$\u0249"+
		"\b$\u0001%\u0001%\u0001%\u0005%\u024e\b%\n%\f%\u0251\t%\u0001&\u0001&"+
		"\u0001&\u0001&\u0001&\u0001\'\u0001\'\u0001(\u0001(\u0003(\u025c\b(\u0001"+
		")\u0001)\u0001)\u0001*\u0001*\u0001*\u0003*\u0264\b*\u0001+\u0001+\u0001"+
		"+\u0005+\u0269\b+\n+\f+\u026c\t+\u0001,\u0001,\u0001,\u0005,\u0271\b,"+
		"\n,\f,\u0274\t,\u0001-\u0001-\u0001-\u0005-\u0279\b-\n-\f-\u027c\t-\u0001"+
		".\u0001.\u0001.\u0001.\u0003.\u0282\b.\u0001/\u0001/\u0001/\u0001/\u0005"+
		"/\u0288\b/\n/\f/\u028b\t/\u00010\u00010\u00010\u00010\u00050\u0291\b0"+
		"\n0\f0\u0294\t0\u00011\u00011\u00011\u00011\u00051\u029a\b1\n1\f1\u029d"+
		"\t1\u00012\u00012\u00012\u00012\u00032\u02a3\b2\u00013\u00013\u00033\u02a7"+
		"\b3\u00014\u00014\u00014\u00034\u02ac\b4\u00015\u00015\u00015\u00035\u02b1"+
		"\b5\u00016\u00016\u00016\u00016\u00016\u00016\u00016\u00016\u00016\u0001"+
		"6\u00016\u00016\u00016\u00016\u00016\u00016\u00016\u00016\u00016\u0001"+
		"6\u00036\u02c7\b6\u00017\u00017\u00017\u00037\u02cc\b7\u00018\u00018\u0001"+
		"8\u00018\u00038\u02d2\b8\u00019\u00019\u00019\u00019\u00039\u02d8\b9\u0001"+
		":\u0001:\u0001:\u0001:\u0001:\u0001:\u0001:\u0005:\u02e1\b:\n:\f:\u02e4"+
		"\t:\u0001;\u0001;\u0001;\u0001;\u0001;\u0001;\u0001;\u0005;\u02ed\b;\n"+
		";\f;\u02f0\t;\u0001<\u0001<\u0001<\u0001<\u0003<\u02f6\b<\u0001=\u0001"+
		"=\u0003=\u02fa\b=\u0001>\u0001>\u0003>\u02fe\b>\u0001?\u0001?\u0001@\u0001"+
		"@\u0001@\u0001@\u0001@\u0001@\u0001@\u0001@\u0001@\u0003@\u030b\b@\u0001"+
		"A\u0001A\u0003A\u030f\bA\u0001A\u0001A\u0001A\u0001A\u0001A\u0001A\u0005"+
		"A\u0317\bA\nA\fA\u031a\tA\u0001B\u0001B\u0001B\u0001B\u0001B\u0003B\u0321"+
		"\bB\u0001C\u0001C\u0001C\u0001C\u0001C\u0001C\u0003C\u0329\bC\u0001D\u0001"+
		"D\u0001D\u0001D\u0001D\u0001D\u0001D\u0001D\u0001D\u0003D\u0334\bD\u0001"+
		"E\u0001E\u0001E\u0001E\u0001E\u0001E\u0003E\u033c\bE\u0001F\u0001F\u0001"+
		"F\u0005F\u0341\bF\nF\fF\u0344\tF\u0001G\u0001G\u0001G\u0001G\u0001H\u0003"+
		"H\u034b\bH\u0001H\u0001H\u0001I\u0001I\u0003I\u0351\bI\u0001J\u0001J\u0003"+
		"J\u0355\bJ\u0001K\u0001K\u0001K\u0005K\u035a\bK\nK\fK\u035d\tK\u0001L"+
		"\u0001L\u0001L\u0003L\u0362\bL\u0001M\u0001M\u0001N\u0001N\u0001N\u0001"+
		"N\u0001N\u0001N\u0001O\u0001O\u0001O\u0001O\u0001O\u0001O\u0001P\u0001"+
		"P\u0001P\u0005P\u0375\bP\nP\fP\u0378\tP\u0001Q\u0001Q\u0001Q\u0001Q\u0001"+
		"Q\u0001Q\u0001Q\u0001Q\u0001Q\u0003Q\u0383\bQ\u0001R\u0001R\u0003R\u0387"+
		"\bR\u0001R\u0001R\u0001S\u0001S\u0003S\u038d\bS\u0001S\u0001S\u0001S\u0001"+
		"S\u0001S\u0001S\u0005S\u0395\bS\nS\fS\u0398\tS\u0001T\u0001T\u0001T\u0001"+
		"T\u0005T\u039e\bT\nT\fT\u03a1\tT\u0003T\u03a3\bT\u0001T\u0001T\u0001U"+
		"\u0001U\u0003U\u03a9\bU\u0001V\u0001V\u0001V\u0001V\u0001W\u0001W\u0001"+
		"W\u0001W\u0001X\u0001X\u0001Y\u0001Y\u0003Y\u03b7\bY\u0001Y\u0001Y\u0001"+
		"Y\u0001Y\u0001Y\u0003Y\u03be\bY\u0001Y\u0001Y\u0001Y\u0001Y\u0001Y\u0001"+
		"Y\u0003Y\u03c6\bY\u0005Y\u03c8\bY\nY\fY\u03cb\tY\u0001Z\u0001Z\u0003Z"+
		"\u03cf\bZ\u0001Z\u0001Z\u0001[\u0001[\u0001[\u0005[\u03d6\b[\n[\f[\u03d9"+
		"\t[\u0001\\\u0001\\\u0003\\\u03dd\b\\\u0001\\\u0001\\\u0001\\\u0001]\u0001"+
		"]\u0001]\u0001^\u0001^\u0001^\u0001^\u0001_\u0001_\u0001_\u0005_\u03ec"+
		"\b_\n_\f_\u03ef\t_\u0001`\u0001`\u0001`\u0001a\u0001a\u0001a\u0001a\u0001"+
		"a\u0001a\u0001b\u0001b\u0001b\u0005b\u03fd\bb\nb\fb\u0400\tb\u0001c\u0001"+
		"c\u0001c\u0001c\u0001d\u0001d\u0001d\u0001d\u0001d\u0001d\u0001d\u0001"+
		"d\u0001d\u0001d\u0001d\u0001d\u0001d\u0001d\u0001d\u0001d\u0001d\u0003"+
		"d\u0417\bd\u0001e\u0001e\u0001e\u0001e\u0001e\u0001e\u0001e\u0001e\u0001"+
		"e\u0001e\u0001e\u0001e\u0001e\u0001e\u0001e\u0001e\u0003e\u0429\be\u0001"+
		"f\u0001f\u0003f\u042d\bf\u0001g\u0001g\u0003g\u0431\bg\u0001h\u0001h\u0001"+
		"h\u0005h\u0436\bh\nh\fh\u0439\th\u0001i\u0001i\u0001i\u0001i\u0001i\u0001"+
		"i\u0001i\u0001i\u0001i\u0003i\u0444\bi\u0001j\u0001j\u0001j\u0001j\u0003"+
		"j\u044a\bj\u0001j\u0001j\u0001k\u0001k\u0001k\u0001k\u0001k\u0001k\u0001"+
		"k\u0001k\u0001k\u0001k\u0001k\u0001k\u0001k\u0001k\u0003k\u045c\bk\u0001"+
		"l\u0001l\u0001l\u0005l\u0461\bl\nl\fl\u0464\tl\u0001m\u0001m\u0001m\u0001"+
		"m\u0001m\u0001m\u0001m\u0003m\u046d\bm\u0001m\u0001m\u0001m\u0001m\u0001"+
		"m\u0003m\u0474\bm\u0001n\u0001n\u0003n\u0478\bn\u0001o\u0001o\u0003o\u047c"+
		"\bo\u0001o\u0001o\u0001p\u0001p\u0003p\u0482\bp\u0001p\u0001p\u0001q\u0001"+
		"q\u0001q\u0005q\u0489\bq\nq\fq\u048c\tq\u0001r\u0001r\u0001r\u0005r\u0491"+
		"\br\nr\fr\u0494\tr\u0001s\u0001s\u0001s\u0005s\u0499\bs\ns\fs\u049c\t"+
		"s\u0001t\u0001t\u0001t\u0001t\u0001t\u0004t\u04a3\bt\u000bt\ft\u04a4\u0003"+
		"t\u04a7\bt\u0001u\u0001u\u0001v\u0001v\u0001w\u0001w\u0001x\u0001x\u0001"+
		"y\u0001y\u0001y\u0000\u0007.0tv\u0082\u00a6\u00b2z\u0000\u0002\u0004\u0006"+
		"\b\n\f\u000e\u0010\u0012\u0014\u0016\u0018\u001a\u001c\u001e \"$&(*,."+
		"02468:<>@BDFHJLNPRTVXZ\\^`bdfhjlnprtvxz|~\u0080\u0082\u0084\u0086\u0088"+
		"\u008a\u008c\u008e\u0090\u0092\u0094\u0096\u0098\u009a\u009c\u009e\u00a0"+
		"\u00a2\u00a4\u00a6\u00a8\u00aa\u00ac\u00ae\u00b0\u00b2\u00b4\u00b6\u00b8"+
		"\u00ba\u00bc\u00be\u00c0\u00c2\u00c4\u00c6\u00c8\u00ca\u00cc\u00ce\u00d0"+
		"\u00d2\u00d4\u00d6\u00d8\u00da\u00dc\u00de\u00e0\u00e2\u00e4\u00e6\u00e8"+
		"\u00ea\u00ec\u00ee\u00f0\u00f2\u0000\u0007\u0001\u0000\u0014\u0015\u0001"+
		"\u0000\u001a\u001b\u0002\u0000\u0002\u0002*,\u0003\u0000\u0018\u0018 "+
		" -0\u0003\u0000\u0002\u0002**16\u0001\u000078\u0001\u00009@\u04cd\u0000"+
		"\u00f5\u0001\u0000\u0000\u0000\u0002\u00fd\u0001\u0000\u0000\u0000\u0004"+
		"\u0101\u0001\u0000\u0000\u0000\u0006\u0103\u0001\u0000\u0000\u0000\b\u0105"+
		"\u0001\u0000\u0000\u0000\n\u0107\u0001\u0000\u0000\u0000\f\u0109\u0001"+
		"\u0000\u0000\u0000\u000e\u010b\u0001\u0000\u0000\u0000\u0010\u011d\u0001"+
		"\u0000\u0000\u0000\u0012\u0127\u0001\u0000\u0000\u0000\u0014\u012e\u0001"+
		"\u0000\u0000\u0000\u0016\u0138\u0001\u0000\u0000\u0000\u0018\u013a\u0001"+
		"\u0000\u0000\u0000\u001a\u014b\u0001\u0000\u0000\u0000\u001c\u014d\u0001"+
		"\u0000\u0000\u0000\u001e\u0151\u0001\u0000\u0000\u0000 \u0159\u0001\u0000"+
		"\u0000\u0000\"\u015e\u0001\u0000\u0000\u0000$\u016f\u0001\u0000\u0000"+
		"\u0000&\u0171\u0001\u0000\u0000\u0000(\u017c\u0001\u0000\u0000\u0000*"+
		"\u0180\u0001\u0000\u0000\u0000,\u0185\u0001\u0000\u0000\u0000.\u018a\u0001"+
		"\u0000\u0000\u00000\u0196\u0001\u0000\u0000\u00002\u01a3\u0001\u0000\u0000"+
		"\u00004\u01f3\u0001\u0000\u0000\u00006\u01fb\u0001\u0000\u0000\u00008"+
		"\u01fd\u0001\u0000\u0000\u0000:\u0205\u0001\u0000\u0000\u0000<\u020d\u0001"+
		"\u0000\u0000\u0000>\u0211\u0001\u0000\u0000\u0000@\u0219\u0001\u0000\u0000"+
		"\u0000B\u022d\u0001\u0000\u0000\u0000D\u022f\u0001\u0000\u0000\u0000F"+
		"\u0233\u0001\u0000\u0000\u0000H\u0248\u0001\u0000\u0000\u0000J\u024a\u0001"+
		"\u0000\u0000\u0000L\u0252\u0001\u0000\u0000\u0000N\u0257\u0001\u0000\u0000"+
		"\u0000P\u025b\u0001\u0000\u0000\u0000R\u025d\u0001\u0000\u0000\u0000T"+
		"\u0263\u0001\u0000\u0000\u0000V\u0265\u0001\u0000\u0000\u0000X\u026d\u0001"+
		"\u0000\u0000\u0000Z\u0275\u0001\u0000\u0000\u0000\\\u027d\u0001\u0000"+
		"\u0000\u0000^\u0283\u0001\u0000\u0000\u0000`\u028c\u0001\u0000\u0000\u0000"+
		"b\u0295\u0001\u0000\u0000\u0000d\u02a2\u0001\u0000\u0000\u0000f\u02a6"+
		"\u0001\u0000\u0000\u0000h\u02ab\u0001\u0000\u0000\u0000j\u02ad\u0001\u0000"+
		"\u0000\u0000l\u02c6\u0001\u0000\u0000\u0000n\u02c8\u0001\u0000\u0000\u0000"+
		"p\u02cd\u0001\u0000\u0000\u0000r\u02d3\u0001\u0000\u0000\u0000t\u02d9"+
		"\u0001\u0000\u0000\u0000v\u02e5\u0001\u0000\u0000\u0000x\u02f5\u0001\u0000"+
		"\u0000\u0000z\u02f9\u0001\u0000\u0000\u0000|\u02fd\u0001\u0000\u0000\u0000"+
		"~\u02ff\u0001\u0000\u0000\u0000\u0080\u030a\u0001\u0000\u0000\u0000\u0082"+
		"\u030c\u0001\u0000\u0000\u0000\u0084\u031b\u0001\u0000\u0000\u0000\u0086"+
		"\u0328\u0001\u0000\u0000\u0000\u0088\u0333\u0001\u0000\u0000\u0000\u008a"+
		"\u033b\u0001\u0000\u0000\u0000\u008c\u033d\u0001\u0000\u0000\u0000\u008e"+
		"\u0345\u0001\u0000\u0000\u0000\u0090\u034a\u0001\u0000\u0000\u0000\u0092"+
		"\u0350\u0001\u0000\u0000\u0000\u0094\u0354\u0001\u0000\u0000\u0000\u0096"+
		"\u0356\u0001\u0000\u0000\u0000\u0098\u035e\u0001\u0000\u0000\u0000\u009a"+
		"\u0363\u0001\u0000\u0000\u0000\u009c\u0365\u0001\u0000\u0000\u0000\u009e"+
		"\u036b\u0001\u0000\u0000\u0000\u00a0\u0371\u0001\u0000\u0000\u0000\u00a2"+
		"\u0382\u0001\u0000\u0000\u0000\u00a4\u0384\u0001\u0000\u0000\u0000\u00a6"+
		"\u038a\u0001\u0000\u0000\u0000\u00a8\u0399\u0001\u0000\u0000\u0000\u00aa"+
		"\u03a8\u0001\u0000\u0000\u0000\u00ac\u03aa\u0001\u0000\u0000\u0000\u00ae"+
		"\u03ae\u0001\u0000\u0000\u0000\u00b0\u03b2\u0001\u0000\u0000\u0000\u00b2"+
		"\u03b4\u0001\u0000\u0000\u0000\u00b4\u03cc\u0001\u0000\u0000\u0000\u00b6"+
		"\u03d2\u0001\u0000\u0000\u0000\u00b8\u03dc\u0001\u0000\u0000\u0000\u00ba"+
		"\u03e1\u0001\u0000\u0000\u0000\u00bc\u03e4\u0001\u0000\u0000\u0000\u00be"+
		"\u03e8\u0001\u0000\u0000\u0000\u00c0\u03f0\u0001\u0000\u0000\u0000\u00c2"+
		"\u03f3\u0001\u0000\u0000\u0000\u00c4\u03f9\u0001\u0000\u0000\u0000\u00c6"+
		"\u0401\u0001\u0000\u0000\u0000\u00c8\u0416\u0001\u0000\u0000\u0000\u00ca"+
		"\u0428\u0001\u0000\u0000\u0000\u00cc\u042c\u0001\u0000\u0000\u0000\u00ce"+
		"\u0430\u0001\u0000\u0000\u0000\u00d0\u0432\u0001\u0000\u0000\u0000\u00d2"+
		"\u0443\u0001\u0000\u0000\u0000\u00d4\u0445\u0001\u0000\u0000\u0000\u00d6"+
		"\u045b\u0001\u0000\u0000\u0000\u00d8\u045d\u0001\u0000\u0000\u0000\u00da"+
		"\u0473\u0001\u0000\u0000\u0000\u00dc\u0477\u0001\u0000\u0000\u0000\u00de"+
		"\u0479\u0001\u0000\u0000\u0000\u00e0\u047f\u0001\u0000\u0000\u0000\u00e2"+
		"\u0485\u0001\u0000\u0000\u0000\u00e4\u048d\u0001\u0000\u0000\u0000\u00e6"+
		"\u0495\u0001\u0000\u0000\u0000\u00e8\u04a6\u0001\u0000\u0000\u0000\u00ea"+
		"\u04a8\u0001\u0000\u0000\u0000\u00ec\u04aa\u0001\u0000\u0000\u0000\u00ee"+
		"\u04ac\u0001\u0000\u0000\u0000\u00f0\u04ae\u0001\u0000\u0000\u0000\u00f2"+
		"\u04b0\u0001\u0000\u0000\u0000\u00f4\u00f6\u0003\u0002\u0001\u0000\u00f5"+
		"\u00f4\u0001\u0000\u0000\u0000\u00f6\u00f7\u0001\u0000\u0000\u0000\u00f7"+
		"\u00f5\u0001\u0000\u0000\u0000\u00f7\u00f8\u0001\u0000\u0000\u0000\u00f8"+
		"\u00f9\u0001\u0000\u0000\u0000\u00f9\u00fa\u0005\u0000\u0000\u0001\u00fa"+
		"\u0001\u0001\u0000\u0000\u0000\u00fb\u00fe\u0003\u0010\b\u0000\u00fc\u00fe"+
		"\u0003J%\u0000\u00fd\u00fb\u0001\u0000\u0000\u0000\u00fd\u00fc\u0001\u0000"+
		"\u0000\u0000\u00fe\u00ff\u0001\u0000\u0000\u0000\u00ff\u0100\u0005\u0001"+
		"\u0000\u0000\u0100\u0003\u0001\u0000\u0000\u0000\u0101\u0102\u0005A\u0000"+
		"\u0000\u0102\u0005\u0001\u0000\u0000\u0000\u0103\u0104\u0005B\u0000\u0000"+
		"\u0104\u0007\u0001\u0000\u0000\u0000\u0105\u0106\u0005C\u0000\u0000\u0106"+
		"\t\u0001\u0000\u0000\u0000\u0107\u0108\u0005D\u0000\u0000\u0108\u000b"+
		"\u0001\u0000\u0000\u0000\u0109\u010a\u0005E\u0000\u0000\u010a\r\u0001"+
		"\u0000\u0000\u0000\u010b\u010c\u0005F\u0000\u0000\u010c\u000f\u0001\u0000"+
		"\u0000\u0000\u010d\u010e\u0005\u0002\u0000\u0000\u010e\u010f\u0003\u0004"+
		"\u0002\u0000\u010f\u0110\u0003H$\u0000\u0110\u011e\u0001\u0000\u0000\u0000"+
		"\u0111\u0112\u0005\u0002\u0000\u0000\u0112\u0113\u0003\u0004\u0002\u0000"+
		"\u0113\u0114\u0003\u0016\u000b\u0000\u0114\u011e\u0001\u0000\u0000\u0000"+
		"\u0115\u0116\u0005\u0002\u0000\u0000\u0116\u0117\u0003\u0004\u0002\u0000"+
		"\u0117\u0118\u0005\u0003\u0000\u0000\u0118\u0119\u0003\u0016\u000b\u0000"+
		"\u0119\u011a\u0005\u0004\u0000\u0000\u011a\u011e\u0001\u0000\u0000\u0000"+
		"\u011b\u011c\u0005G\u0000\u0000\u011c\u011e\u0003\u0012\t\u0000\u011d"+
		"\u010d\u0001\u0000\u0000\u0000\u011d\u0111\u0001\u0000\u0000\u0000\u011d"+
		"\u0115\u0001\u0000\u0000\u0000\u011d\u011b\u0001\u0000\u0000\u0000\u011e"+
		"\u0011\u0001\u0000\u0000\u0000\u011f\u0120\u0003\u0014\n\u0000\u0120\u0121"+
		"\u0003\u001e\u000f\u0000\u0121\u0128\u0001\u0000\u0000\u0000\u0122\u0123"+
		"\u0005\u0003\u0000\u0000\u0123\u0124\u0003\u0014\n\u0000\u0124\u0125\u0003"+
		"\u001e\u000f\u0000\u0125\u0126\u0005\u0004\u0000\u0000\u0126\u0128\u0001"+
		"\u0000\u0000\u0000\u0127\u011f\u0001\u0000\u0000\u0000\u0127\u0122\u0001"+
		"\u0000\u0000\u0000\u0128\u0013\u0001\u0000\u0000\u0000\u0129\u012f\u0003"+
		"\u0004\u0002\u0000\u012a\u012b\u0003\u0004\u0002\u0000\u012b\u012c\u0005"+
		"\u0005\u0000\u0000\u012c\u012d\u0003\u0004\u0002\u0000\u012d\u012f\u0001"+
		"\u0000\u0000\u0000\u012e\u0129\u0001\u0000\u0000\u0000\u012e\u012a\u0001"+
		"\u0000\u0000\u0000\u012f\u0015\u0001\u0000\u0000\u0000\u0130\u0131\u0003"+
		"T*\u0000\u0131\u0132\u0005\u0006\u0000\u0000\u0132\u0133\u0003\u0018\f"+
		"\u0000\u0133\u0139\u0001\u0000\u0000\u0000\u0134\u0135\u0003T*\u0000\u0135"+
		"\u0136\u0005\u0007\u0000\u0000\u0136\u0137\u0003(\u0014\u0000\u0137\u0139"+
		"\u0001\u0000\u0000\u0000\u0138\u0130\u0001\u0000\u0000\u0000\u0138\u0134"+
		"\u0001\u0000\u0000\u0000\u0139\u0017\u0001\u0000\u0000\u0000\u013a\u013b"+
		"\u0005\b\u0000\u0000\u013b\u013c\u0003\u001a\r\u0000\u013c\u013d\u0005"+
		"\t\u0000\u0000\u013d\u0019\u0001\u0000\u0000\u0000\u013e\u014c\u0003\u001c"+
		"\u000e\u0000\u013f\u0140\u0003\u001c\u000e\u0000\u0140\u0141\u0005\u0006"+
		"\u0000\u0000\u0141\u0142\u0003\u001a\r\u0000\u0142\u014c\u0001\u0000\u0000"+
		"\u0000\u0143\u0144\u0003T*\u0000\u0144\u0145\u0005\u0006\u0000\u0000\u0145"+
		"\u0146\u0003\u001a\r\u0000\u0146\u014c\u0001\u0000\u0000\u0000\u0147\u0148"+
		"\u0003\u001c\u000e\u0000\u0148\u0149\u0005\u0006\u0000\u0000\u0149\u014a"+
		"\u0003\u00e2q\u0000\u014a\u014c\u0001\u0000\u0000\u0000\u014b\u013e\u0001"+
		"\u0000\u0000\u0000\u014b\u013f\u0001\u0000\u0000\u0000\u014b\u0143\u0001"+
		"\u0000\u0000\u0000\u014b\u0147\u0001\u0000\u0000\u0000\u014c\u001b\u0001"+
		"\u0000\u0000\u0000\u014d\u014e\u0003T*\u0000\u014e\u014f\u0005\u0007\u0000"+
		"\u0000\u014f\u0150\u0003(\u0014\u0000\u0150\u001d\u0001\u0000\u0000\u0000"+
		"\u0151\u0156\u0003 \u0010\u0000\u0152\u0153\u0005\n\u0000\u0000\u0153"+
		"\u0155\u0003 \u0010\u0000\u0154\u0152\u0001\u0000\u0000\u0000\u0155\u0158"+
		"\u0001\u0000\u0000\u0000\u0156\u0154\u0001\u0000\u0000\u0000\u0156\u0157"+
		"\u0001\u0000\u0000\u0000\u0157\u001f\u0001\u0000\u0000\u0000\u0158\u0156"+
		"\u0001\u0000\u0000\u0000\u0159\u015c\u00038\u001c\u0000\u015a\u015b\u0005"+
		"\u000b\u0000\u0000\u015b\u015d\u0003\"\u0011\u0000\u015c\u015a\u0001\u0000"+
		"\u0000\u0000\u015c\u015d\u0001\u0000\u0000\u0000\u015d!\u0001\u0000\u0000"+
		"\u0000\u015e\u0163\u0003$\u0012\u0000\u015f\u0160\u0005\u0006\u0000\u0000"+
		"\u0160\u0162\u0003$\u0012\u0000\u0161\u015f\u0001\u0000\u0000\u0000\u0162"+
		"\u0165\u0001\u0000\u0000\u0000\u0163\u0161\u0001\u0000\u0000\u0000\u0163"+
		"\u0164\u0001\u0000\u0000\u0000\u0164#\u0001\u0000\u0000\u0000\u0165\u0163"+
		"\u0001\u0000\u0000\u0000\u0166\u0167\u0003\u0004\u0002\u0000\u0167\u0168"+
		"\u0005\u0003\u0000\u0000\u0168\u0169\u0003&\u0013\u0000\u0169\u016a\u0005"+
		"\u0004\u0000\u0000\u016a\u0170\u0001\u0000\u0000\u0000\u016b\u016c\u0003"+
		"\u0006\u0003\u0000\u016c\u016d\u0005\u0007\u0000\u0000\u016d\u016e\u0003"+
		"(\u0014\u0000\u016e\u0170\u0001\u0000\u0000\u0000\u016f\u0166\u0001\u0000"+
		"\u0000\u0000\u016f\u016b\u0001\u0000\u0000\u0000\u0170%\u0001\u0000\u0000"+
		"\u0000\u0171\u0176\u0003(\u0014\u0000\u0172\u0173\u0005\u0006\u0000\u0000"+
		"\u0173\u0175\u0003(\u0014\u0000\u0174\u0172\u0001\u0000\u0000\u0000\u0175"+
		"\u0178\u0001\u0000\u0000\u0000\u0176\u0174\u0001\u0000\u0000\u0000\u0176"+
		"\u0177\u0001\u0000\u0000\u0000\u0177\'\u0001\u0000\u0000\u0000\u0178\u0176"+
		"\u0001\u0000\u0000\u0000\u0179\u017a\u0003\u0006\u0003\u0000\u017a\u017b"+
		"\u0005\u0007\u0000\u0000\u017b\u017d\u0001\u0000\u0000\u0000\u017c\u0179"+
		"\u0001\u0000\u0000\u0000\u017c\u017d\u0001\u0000\u0000\u0000\u017d\u017e"+
		"\u0001\u0000\u0000\u0000\u017e\u017f\u0003*\u0015\u0000\u017f)\u0001\u0000"+
		"\u0000\u0000\u0180\u0183\u0003,\u0016\u0000\u0181\u0182\u0005\f\u0000"+
		"\u0000\u0182\u0184\u0003*\u0015\u0000\u0183\u0181\u0001\u0000\u0000\u0000"+
		"\u0183\u0184\u0001\u0000\u0000\u0000\u0184+\u0001\u0000\u0000\u0000\u0185"+
		"\u0188\u0003.\u0017\u0000\u0186\u0187\u0005\r\u0000\u0000\u0187\u0189"+
		"\u0003.\u0017\u0000\u0188\u0186\u0001\u0000\u0000\u0000\u0188\u0189\u0001"+
		"\u0000\u0000\u0000\u0189-\u0001\u0000\u0000\u0000\u018a\u018b\u0006\u0017"+
		"\uffff\uffff\u0000\u018b\u018c\u00030\u0018\u0000\u018c\u0193\u0001\u0000"+
		"\u0000\u0000\u018d\u018e\n\u0002\u0000\u0000\u018e\u018f\u0003\u00eew"+
		"\u0000\u018f\u0190\u00030\u0018\u0000\u0190\u0192\u0001\u0000\u0000\u0000"+
		"\u0191\u018d\u0001\u0000\u0000\u0000\u0192\u0195\u0001\u0000\u0000\u0000"+
		"\u0193\u0191\u0001\u0000\u0000\u0000\u0193\u0194\u0001\u0000\u0000\u0000"+
		"\u0194/\u0001\u0000\u0000\u0000\u0195\u0193\u0001\u0000\u0000\u0000\u0196"+
		"\u0197\u0006\u0018\uffff\uffff\u0000\u0197\u0198\u00032\u0019\u0000\u0198"+
		"\u019f\u0001\u0000\u0000\u0000\u0199\u019a\n\u0002\u0000\u0000\u019a\u019b"+
		"\u0003\u00ecv\u0000\u019b\u019c\u00032\u0019\u0000\u019c\u019e\u0001\u0000"+
		"\u0000\u0000\u019d\u0199\u0001\u0000\u0000\u0000\u019e\u01a1\u0001\u0000"+
		"\u0000\u0000\u019f\u019d\u0001\u0000\u0000\u0000\u019f\u01a0\u0001\u0000"+
		"\u0000\u0000\u01a01\u0001\u0000\u0000\u0000\u01a1\u019f\u0001\u0000\u0000"+
		"\u0000\u01a2\u01a4\u0003\u00eau\u0000\u01a3\u01a2\u0001\u0000\u0000\u0000"+
		"\u01a3\u01a4\u0001\u0000\u0000\u0000\u01a4\u01a5\u0001\u0000\u0000\u0000"+
		"\u01a5\u01a6\u00034\u001a\u0000\u01a63\u0001\u0000\u0000\u0000\u01a7\u01a8"+
		"\u0005\u0003\u0000\u0000\u01a8\u01a9\u0003(\u0014\u0000\u01a9\u01aa\u0005"+
		"\u0004\u0000\u0000\u01aa\u01f4\u0001\u0000\u0000\u0000\u01ab\u01f4\u0003"+
		"\u0006\u0003\u0000\u01ac\u01f4\u0003\u0004\u0002\u0000\u01ad\u01ae\u0003"+
		"\u0004\u0002\u0000\u01ae\u01af\u0005\u0003\u0000\u0000\u01af\u01b0\u0005"+
		"\u0004\u0000\u0000\u01b0\u01f4\u0001\u0000\u0000\u0000\u01b1\u01b2\u0003"+
		"\u0004\u0002\u0000\u01b2\u01b3\u0005\u0003\u0000\u0000\u01b3\u01b4\u0003"+
		"&\u0013\u0000\u01b4\u01b5\u0005\u0004\u0000\u0000\u01b5\u01f4\u0001\u0000"+
		"\u0000\u0000\u01b6\u01b7\u0003\u0004\u0002\u0000\u01b7\u01b8\u0005\u0005"+
		"\u0000\u0000\u01b8\u01b9\u0003\u0004\u0002\u0000\u01b9\u01ba\u0005\u0003"+
		"\u0000\u0000\u01ba\u01bb\u0005\u0004\u0000\u0000\u01bb\u01f4\u0001\u0000"+
		"\u0000\u0000\u01bc\u01bd\u0003\u0004\u0002\u0000\u01bd\u01be\u0005\u0005"+
		"\u0000\u0000\u01be\u01bf\u0003\u0004\u0002\u0000\u01bf\u01c0\u0005\u0003"+
		"\u0000\u0000\u01c0\u01c1\u0003&\u0013\u0000\u01c1\u01c2\u0005\u0004\u0000"+
		"\u0000\u01c2\u01f4\u0001\u0000\u0000\u0000\u01c3\u01c4\u0005\u000e\u0000"+
		"\u0000\u01c4\u01f4\u0005\u000f\u0000\u0000\u01c5\u01c6\u0005\u000e\u0000"+
		"\u0000\u01c6\u01c7\u0003(\u0014\u0000\u01c7\u01c8\u0005\u000f\u0000\u0000"+
		"\u01c8\u01f4\u0001\u0000\u0000\u0000\u01c9\u01ca\u0005\u000e\u0000\u0000"+
		"\u01ca\u01cb\u0003(\u0014\u0000\u01cb\u01cc\u0005\u0006\u0000\u0000\u01cc"+
		"\u01cd\u0005\u0010\u0000\u0000\u01cd\u01ce\u0005\u000f\u0000\u0000\u01ce"+
		"\u01f4\u0001\u0000\u0000\u0000\u01cf\u01d0\u0005\u0011\u0000\u0000\u01d0"+
		"\u01d1\u0005\b\u0000\u0000\u01d1\u01f4\u0005\t\u0000\u0000\u01d2\u01d3"+
		"\u0005\u0011\u0000\u0000\u01d3\u01d4\u0005\b\u0000\u0000\u01d4\u01d5\u0003"+
		":\u001d\u0000\u01d5\u01d6\u0005\t\u0000\u0000\u01d6\u01f4\u0001\u0000"+
		"\u0000\u0000\u01d7\u01d8\u0005\b\u0000\u0000\u01d8\u01f4\u0005\t\u0000"+
		"\u0000\u01d9\u01da\u0005\b\u0000\u0000\u01da\u01db\u0003&\u0013\u0000"+
		"\u01db\u01dc\u0005\t\u0000\u0000\u01dc\u01f4\u0001\u0000\u0000\u0000\u01dd"+
		"\u01de\u0005\u0011\u0000\u0000\u01de\u01df\u0003\u0004\u0002\u0000\u01df"+
		"\u01e0\u0005\b\u0000\u0000\u01e0\u01e1\u0005\t\u0000\u0000\u01e1\u01f4"+
		"\u0001\u0000\u0000\u0000\u01e2\u01e3\u0005\u0011\u0000\u0000\u01e3\u01e4"+
		"\u0003\u0004\u0002\u0000\u01e4\u01e5\u0005\b\u0000\u0000\u01e5\u01e6\u0003"+
		">\u001f\u0000\u01e6\u01e7\u0005\t\u0000\u0000\u01e7\u01f4\u0001\u0000"+
		"\u0000\u0000\u01e8\u01f4\u0003B!\u0000\u01e9\u01f4\u0003\n\u0005\u0000"+
		"\u01ea\u01f4\u0003\f\u0006\u0000\u01eb\u01ec\u0005\u0012\u0000\u0000\u01ec"+
		"\u01ed\u0005\u0003\u0000\u0000\u01ed\u01f4\u0005\u0004\u0000\u0000\u01ee"+
		"\u01ef\u0005\u0012\u0000\u0000\u01ef\u01f0\u0005\u0003\u0000\u0000\u01f0"+
		"\u01f1\u00036\u001b\u0000\u01f1\u01f2\u0005\u0004\u0000\u0000\u01f2\u01f4"+
		"\u0001\u0000\u0000\u0000\u01f3\u01a7\u0001\u0000\u0000\u0000\u01f3\u01ab"+
		"\u0001\u0000\u0000\u0000\u01f3\u01ac\u0001\u0000\u0000\u0000\u01f3\u01ad"+
		"\u0001\u0000\u0000\u0000\u01f3\u01b1\u0001\u0000\u0000\u0000\u01f3\u01b6"+
		"\u0001\u0000\u0000\u0000\u01f3\u01bc\u0001\u0000\u0000\u0000\u01f3\u01c3"+
		"\u0001\u0000\u0000\u0000\u01f3\u01c5\u0001\u0000\u0000\u0000\u01f3\u01c9"+
		"\u0001\u0000\u0000\u0000\u01f3\u01cf\u0001\u0000\u0000\u0000\u01f3\u01d2"+
		"\u0001\u0000\u0000\u0000\u01f3\u01d7\u0001\u0000\u0000\u0000\u01f3\u01d9"+
		"\u0001\u0000\u0000\u0000\u01f3\u01dd\u0001\u0000\u0000\u0000\u01f3\u01e2"+
		"\u0001\u0000\u0000\u0000\u01f3\u01e8\u0001\u0000\u0000\u0000\u01f3\u01e9"+
		"\u0001\u0000\u0000\u0000\u01f3\u01ea\u0001\u0000\u0000\u0000\u01f3\u01eb"+
		"\u0001\u0000\u0000\u0000\u01f3\u01ee\u0001\u0000\u0000\u0000\u01f45\u0001"+
		"\u0000\u0000\u0000\u01f5\u01f6\u0005\u0003\u0000\u0000\u01f6\u01f7\u0005"+
		"\u0010\u0000\u0000\u01f7\u01f8\u0005\u0004\u0000\u0000\u01f8\u01f9\u0005"+
		"\u0013\u0000\u0000\u01f9\u01fc\u0003(\u0014\u0000\u01fa\u01fc\u00038\u001c"+
		"\u0000\u01fb\u01f5\u0001\u0000\u0000\u0000\u01fb\u01fa\u0001\u0000\u0000"+
		"\u0000\u01fc7\u0001\u0000\u0000\u0000\u01fd\u01ff\u0005\u0003\u0000\u0000"+
		"\u01fe\u0200\u0003&\u0013\u0000\u01ff\u01fe\u0001\u0000\u0000\u0000\u01ff"+
		"\u0200\u0001\u0000\u0000\u0000\u0200\u0201\u0001\u0000\u0000\u0000\u0201"+
		"\u0202\u0005\u0004\u0000\u0000\u0202\u0203\u0005\u0013\u0000\u0000\u0203"+
		"\u0204\u0003(\u0014\u0000\u02049\u0001\u0000\u0000\u0000\u0205\u020a\u0003"+
		"<\u001e\u0000\u0206\u0207\u0005\u0006\u0000\u0000\u0207\u0209\u0003<\u001e"+
		"\u0000\u0208\u0206\u0001\u0000\u0000\u0000\u0209\u020c\u0001\u0000\u0000"+
		"\u0000\u020a\u0208\u0001\u0000\u0000\u0000\u020a\u020b\u0001\u0000\u0000"+
		"\u0000\u020b;\u0001\u0000\u0000\u0000\u020c\u020a\u0001\u0000\u0000\u0000"+
		"\u020d\u020e\u0003(\u0014\u0000\u020e\u020f\u0007\u0000\u0000\u0000\u020f"+
		"\u0210\u0003(\u0014\u0000\u0210=\u0001\u0000\u0000\u0000\u0211\u0216\u0003"+
		"@ \u0000\u0212\u0213\u0005\u0006\u0000\u0000\u0213\u0215\u0003@ \u0000"+
		"\u0214\u0212\u0001\u0000\u0000\u0000\u0215\u0218\u0001\u0000\u0000\u0000"+
		"\u0216\u0214\u0001\u0000\u0000\u0000\u0216\u0217\u0001\u0000\u0000\u0000"+
		"\u0217?\u0001\u0000\u0000\u0000\u0218\u0216\u0001\u0000\u0000\u0000\u0219"+
		"\u021a\u0003\u0004\u0002\u0000\u021a\u021b\u0005\u0007\u0000\u0000\u021b"+
		"\u021c\u0003(\u0014\u0000\u021cA\u0001\u0000\u0000\u0000\u021d\u021e\u0005"+
		"\u0016\u0000\u0000\u021e\u022e\u0005\u0017\u0000\u0000\u021f\u0220\u0005"+
		"\u0016\u0000\u0000\u0220\u0221\u0003D\"\u0000\u0221\u0222\u0005\u0017"+
		"\u0000\u0000\u0222\u022e\u0001\u0000\u0000\u0000\u0223\u0224\u0005\u0016"+
		"\u0000\u0000\u0224\u0225\u0003F#\u0000\u0225\u0226\u0005\u0017\u0000\u0000"+
		"\u0226\u022e\u0001\u0000\u0000\u0000\u0227\u0228\u0005\u0016\u0000\u0000"+
		"\u0228\u0229\u0003D\"\u0000\u0229\u022a\u0005\u0006\u0000\u0000\u022a"+
		"\u022b\u0003F#\u0000\u022b\u022c\u0005\u0017\u0000\u0000\u022c\u022e\u0001"+
		"\u0000\u0000\u0000\u022d\u021d\u0001\u0000\u0000\u0000\u022d\u021f\u0001"+
		"\u0000\u0000\u0000\u022d\u0223\u0001\u0000\u0000\u0000\u022d\u0227\u0001"+
		"\u0000\u0000\u0000\u022eC\u0001\u0000\u0000\u0000\u022f\u0230\u0003\u0006"+
		"\u0003\u0000\u0230\u0231\u0005\u0005\u0000\u0000\u0231\u0232\u00034\u001a"+
		"\u0000\u0232E\u0001\u0000\u0000\u0000\u0233\u0234\u0003\u0006\u0003\u0000"+
		"\u0234\u0235\u0005\u0005\u0000\u0000\u0235\u0236\u0003\u0006\u0003\u0000"+
		"\u0236\u0237\u0005\u0018\u0000\u0000\u0237\u0238\u00034\u001a\u0000\u0238"+
		"G\u0001\u0000\u0000\u0000\u0239\u0249\u0003T*\u0000\u023a\u023b\u0005"+
		"\u0003\u0000\u0000\u023b\u023c\u0003T*\u0000\u023c\u023d\u0005\u0004\u0000"+
		"\u0000\u023d\u0249\u0001\u0000\u0000\u0000\u023e\u023f\u0003T*\u0000\u023f"+
		"\u0240\u0005\u0006\u0000\u0000\u0240\u0241\u0003\u00e2q\u0000\u0241\u0249"+
		"\u0001\u0000\u0000\u0000\u0242\u0243\u0005\u0003\u0000\u0000\u0243\u0244"+
		"\u0003T*\u0000\u0244\u0245\u0005\u0006\u0000\u0000\u0245\u0246\u0003\u00e2"+
		"q\u0000\u0246\u0247\u0005\u0004\u0000\u0000\u0247\u0249\u0001\u0000\u0000"+
		"\u0000\u0248\u0239\u0001\u0000\u0000\u0000\u0248\u023a\u0001\u0000\u0000"+
		"\u0000\u0248\u023e\u0001\u0000\u0000\u0000\u0248\u0242\u0001\u0000\u0000"+
		"\u0000\u0249I\u0001\u0000\u0000\u0000\u024a\u024f\u0003L&\u0000\u024b"+
		"\u024c\u0005\n\u0000\u0000\u024c\u024e\u0003L&\u0000\u024d\u024b\u0001"+
		"\u0000\u0000\u0000\u024e\u0251\u0001\u0000\u0000\u0000\u024f\u024d\u0001"+
		"\u0000\u0000\u0000\u024f\u0250\u0001\u0000\u0000\u0000\u0250K\u0001\u0000"+
		"\u0000\u0000\u0251\u024f\u0001\u0000\u0000\u0000\u0252\u0253\u0003\u0004"+
		"\u0002\u0000\u0253\u0254\u0003N\'\u0000\u0254\u0255\u0003P(\u0000\u0255"+
		"\u0256\u0003R)\u0000\u0256M\u0001\u0000\u0000\u0000\u0257\u0258\u0003"+
		"\u00e0p\u0000\u0258O\u0001\u0000\u0000\u0000\u0259\u025a\u0005\u000b\u0000"+
		"\u0000\u025a\u025c\u0003\u00e6s\u0000\u025b\u0259\u0001\u0000\u0000\u0000"+
		"\u025b\u025c\u0001\u0000\u0000\u0000\u025cQ\u0001\u0000\u0000\u0000\u025d"+
		"\u025e\u0005\u0013\u0000\u0000\u025e\u025f\u0003\u00e2q\u0000\u025fS\u0001"+
		"\u0000\u0000\u0000\u0260\u0261\u0005\u0019\u0000\u0000\u0261\u0264\u0003"+
		"T*\u0000\u0262\u0264\u0003V+\u0000\u0263\u0260\u0001\u0000\u0000\u0000"+
		"\u0263\u0262\u0001\u0000\u0000\u0000\u0264U\u0001\u0000\u0000\u0000\u0265"+
		"\u026a\u0003X,\u0000\u0266\u0267\u0007\u0001\u0000\u0000\u0267\u0269\u0003"+
		"X,\u0000\u0268\u0266\u0001\u0000\u0000\u0000\u0269\u026c\u0001\u0000\u0000"+
		"\u0000\u026a\u0268\u0001\u0000\u0000\u0000\u026a\u026b\u0001\u0000\u0000"+
		"\u0000\u026bW\u0001\u0000\u0000\u0000\u026c\u026a\u0001\u0000\u0000\u0000"+
		"\u026d\u0272\u0003Z-\u0000\u026e\u026f\u0005\u001c\u0000\u0000\u026f\u0271"+
		"\u0003Z-\u0000\u0270\u026e\u0001\u0000\u0000\u0000\u0271\u0274\u0001\u0000"+
		"\u0000\u0000\u0272\u0270\u0001\u0000\u0000\u0000\u0272\u0273\u0001\u0000"+
		"\u0000\u0000\u0273Y\u0001\u0000\u0000\u0000\u0274\u0272\u0001\u0000\u0000"+
		"\u0000\u0275\u027a\u0003\\.\u0000\u0276\u0277\u0005\u001d\u0000\u0000"+
		"\u0277\u0279\u0003\\.\u0000\u0278\u0276\u0001\u0000\u0000\u0000\u0279"+
		"\u027c\u0001\u0000\u0000\u0000\u027a\u0278\u0001\u0000\u0000\u0000\u027a"+
		"\u027b\u0001\u0000\u0000\u0000\u027b[\u0001\u0000\u0000\u0000\u027c\u027a"+
		"\u0001\u0000\u0000\u0000\u027d\u0281\u0003^/\u0000\u027e\u027f\u0003\u00f2"+
		"y\u0000\u027f\u0280\u0003^/\u0000\u0280\u0282\u0001\u0000\u0000\u0000"+
		"\u0281\u027e\u0001\u0000\u0000\u0000\u0281\u0282\u0001\u0000\u0000\u0000"+
		"\u0282]\u0001\u0000\u0000\u0000\u0283\u0289\u0003`0\u0000\u0284\u0285"+
		"\u0003\u00f0x\u0000\u0285\u0286\u0003`0\u0000\u0286\u0288\u0001\u0000"+
		"\u0000\u0000\u0287\u0284\u0001\u0000\u0000\u0000\u0288\u028b\u0001\u0000"+
		"\u0000\u0000\u0289\u0287\u0001\u0000\u0000\u0000\u0289\u028a\u0001\u0000"+
		"\u0000\u0000\u028a_\u0001\u0000\u0000\u0000\u028b\u0289\u0001\u0000\u0000"+
		"\u0000\u028c\u0292\u0003b1\u0000\u028d\u028e\u0003\u00eew\u0000\u028e"+
		"\u028f\u0003b1\u0000\u028f\u0291\u0001\u0000\u0000\u0000\u0290\u028d\u0001"+
		"\u0000\u0000\u0000\u0291\u0294\u0001\u0000\u0000\u0000\u0292\u0290\u0001"+
		"\u0000\u0000\u0000\u0292\u0293\u0001\u0000\u0000\u0000\u0293a\u0001\u0000"+
		"\u0000\u0000\u0294\u0292\u0001\u0000\u0000\u0000\u0295\u029b\u0003d2\u0000"+
		"\u0296\u0297\u0003\u00ecv\u0000\u0297\u0298\u0003d2\u0000\u0298\u029a"+
		"\u0001\u0000\u0000\u0000\u0299\u0296\u0001\u0000\u0000\u0000\u029a\u029d"+
		"\u0001\u0000\u0000\u0000\u029b\u0299\u0001\u0000\u0000\u0000\u029b\u029c"+
		"\u0001\u0000\u0000\u0000\u029cc\u0001\u0000\u0000\u0000\u029d\u029b\u0001"+
		"\u0000\u0000\u0000\u029e\u029f\u0003\u00eau\u0000\u029f\u02a0\u0003d2"+
		"\u0000\u02a0\u02a3\u0001\u0000\u0000\u0000\u02a1\u02a3\u0003f3\u0000\u02a2"+
		"\u029e\u0001\u0000\u0000\u0000\u02a2\u02a1\u0001\u0000\u0000\u0000\u02a3"+
		"e\u0001\u0000\u0000\u0000\u02a4\u02a7\u0003\u00a6S\u0000\u02a5\u02a7\u0003"+
		"h4\u0000\u02a6\u02a4\u0001\u0000\u0000\u0000\u02a6\u02a5\u0001\u0000\u0000"+
		"\u0000\u02a7g\u0001\u0000\u0000\u0000\u02a8\u02ac\u0003\u00ba]\u0000\u02a9"+
		"\u02ac\u0003\u00b2Y\u0000\u02aa\u02ac\u0003j5\u0000\u02ab\u02a8\u0001"+
		"\u0000\u0000\u0000\u02ab\u02a9\u0001\u0000\u0000\u0000\u02ab\u02aa\u0001"+
		"\u0000\u0000\u0000\u02aci\u0001\u0000\u0000\u0000\u02ad\u02b0\u0003l6"+
		"\u0000\u02ae\u02af\u0005\u0005\u0000\u0000\u02af\u02b1\u0003l6\u0000\u02b0"+
		"\u02ae\u0001\u0000\u0000\u0000\u02b0\u02b1\u0001\u0000\u0000\u0000\u02b1"+
		"k\u0001\u0000\u0000\u0000\u02b2\u02c7\u0003\u0006\u0003\u0000\u02b3\u02c7"+
		"\u0003\u00e8t\u0000\u02b4\u02c7\u0003\u0086C\u0000\u02b5\u02c7\u0003\u008a"+
		"E\u0000\u02b6\u02c7\u0003\u009cN\u0000\u02b7\u02c7\u0003\u009eO\u0000"+
		"\u02b8\u02c7\u0003\u00a4R\u0000\u02b9\u02ba\u0005\u0003\u0000\u0000\u02ba"+
		"\u02bb\u0003T*\u0000\u02bb\u02bc\u0005\u0004\u0000\u0000\u02bc\u02c7\u0001"+
		"\u0000\u0000\u0000\u02bd\u02be\u0005\u001e\u0000\u0000\u02be\u02bf\u0003"+
		"\u00e2q\u0000\u02bf\u02c0\u0005\u001f\u0000\u0000\u02c0\u02c7\u0001\u0000"+
		"\u0000\u0000\u02c1\u02c7\u0003\u00bc^\u0000\u02c2\u02c7\u0003\u00c2a\u0000"+
		"\u02c3\u02c7\u0003\u00c8d\u0000\u02c4\u02c7\u0003\u00cae\u0000\u02c5\u02c7"+
		"\u0003\u00d4j\u0000\u02c6\u02b2\u0001\u0000\u0000\u0000\u02c6\u02b3\u0001"+
		"\u0000\u0000\u0000\u02c6\u02b4\u0001\u0000\u0000\u0000\u02c6\u02b5\u0001"+
		"\u0000\u0000\u0000\u02c6\u02b6\u0001\u0000\u0000\u0000\u02c6\u02b7\u0001"+
		"\u0000\u0000\u0000\u02c6\u02b8\u0001\u0000\u0000\u0000\u02c6\u02b9\u0001"+
		"\u0000\u0000\u0000\u02c6\u02bd\u0001\u0000\u0000\u0000\u02c6\u02c1\u0001"+
		"\u0000\u0000\u0000\u02c6\u02c2\u0001\u0000\u0000\u0000\u02c6\u02c3\u0001"+
		"\u0000\u0000\u0000\u02c6\u02c4\u0001\u0000\u0000\u0000\u02c6\u02c5\u0001"+
		"\u0000\u0000\u0000\u02c7m\u0001\u0000\u0000\u0000\u02c8\u02cb\u0003p8"+
		"\u0000\u02c9\u02ca\u0005\u001a\u0000\u0000\u02ca\u02cc\u0003n7\u0000\u02cb"+
		"\u02c9\u0001\u0000\u0000\u0000\u02cb\u02cc\u0001\u0000\u0000\u0000\u02cc"+
		"o\u0001\u0000\u0000\u0000\u02cd\u02d1\u0003r9\u0000\u02ce\u02cf\u0003"+
		"\u00f2y\u0000\u02cf\u02d0\u0003r9\u0000\u02d0\u02d2\u0001\u0000\u0000"+
		"\u0000\u02d1\u02ce\u0001\u0000\u0000\u0000\u02d1\u02d2\u0001\u0000\u0000"+
		"\u0000\u02d2q\u0001\u0000\u0000\u0000\u02d3\u02d7\u0003t:\u0000\u02d4"+
		"\u02d5\u0003\u00f0x\u0000\u02d5\u02d6\u0003r9\u0000\u02d6\u02d8\u0001"+
		"\u0000\u0000\u0000\u02d7\u02d4\u0001\u0000\u0000\u0000\u02d7\u02d8\u0001"+
		"\u0000\u0000\u0000\u02d8s\u0001\u0000\u0000\u0000\u02d9\u02da\u0006:\uffff"+
		"\uffff\u0000\u02da\u02db\u0003v;\u0000\u02db\u02e2\u0001\u0000\u0000\u0000"+
		"\u02dc\u02dd\n\u0002\u0000\u0000\u02dd\u02de\u0003\u00eew\u0000\u02de"+
		"\u02df\u0003v;\u0000\u02df\u02e1\u0001\u0000\u0000\u0000\u02e0\u02dc\u0001"+
		"\u0000\u0000\u0000\u02e1\u02e4\u0001\u0000\u0000\u0000\u02e2\u02e0\u0001"+
		"\u0000\u0000\u0000\u02e2\u02e3\u0001\u0000\u0000\u0000\u02e3u\u0001\u0000"+
		"\u0000\u0000\u02e4\u02e2\u0001\u0000\u0000\u0000\u02e5\u02e6\u0006;\uffff"+
		"\uffff\u0000\u02e6\u02e7\u0003x<\u0000\u02e7\u02ee\u0001\u0000\u0000\u0000"+
		"\u02e8\u02e9\n\u0002\u0000\u0000\u02e9\u02ea\u0003\u00ecv\u0000\u02ea"+
		"\u02eb\u0003x<\u0000\u02eb\u02ed\u0001\u0000\u0000\u0000\u02ec\u02e8\u0001"+
		"\u0000\u0000\u0000\u02ed\u02f0\u0001\u0000\u0000\u0000\u02ee\u02ec\u0001"+
		"\u0000\u0000\u0000\u02ee\u02ef\u0001\u0000\u0000\u0000\u02efw\u0001\u0000"+
		"\u0000\u0000\u02f0\u02ee\u0001\u0000\u0000\u0000\u02f1\u02f2\u0003\u00ea"+
		"u\u0000\u02f2\u02f3\u0003x<\u0000\u02f3\u02f6\u0001\u0000\u0000\u0000"+
		"\u02f4\u02f6\u0003z=\u0000\u02f5\u02f1\u0001\u0000\u0000\u0000\u02f5\u02f4"+
		"\u0001\u0000\u0000\u0000\u02f6y\u0001\u0000\u0000\u0000\u02f7\u02fa\u0003"+
		"\u0082A\u0000\u02f8\u02fa\u0003|>\u0000\u02f9\u02f7\u0001\u0000\u0000"+
		"\u0000\u02f9\u02f8\u0001\u0000\u0000\u0000\u02fa{\u0001\u0000\u0000\u0000"+
		"\u02fb\u02fe\u0003\u0084B\u0000\u02fc\u02fe\u0003~?\u0000\u02fd\u02fb"+
		"\u0001\u0000\u0000\u0000\u02fd\u02fc\u0001\u0000\u0000\u0000\u02fe}\u0001"+
		"\u0000\u0000\u0000\u02ff\u0300\u0003\u0080@\u0000\u0300\u007f\u0001\u0000"+
		"\u0000\u0000\u0301\u030b\u0003\u0006\u0003\u0000\u0302\u030b\u0003\u00e8"+
		"t\u0000\u0303\u030b\u0003\u0086C\u0000\u0304\u030b\u0003\u008aE\u0000"+
		"\u0305\u030b\u0003\u00a4R\u0000\u0306\u0307\u0005\u0003\u0000\u0000\u0307"+
		"\u0308\u0003n7\u0000\u0308\u0309\u0005\u0004\u0000\u0000\u0309\u030b\u0001"+
		"\u0000\u0000\u0000\u030a\u0301\u0001\u0000\u0000\u0000\u030a\u0302\u0001"+
		"\u0000\u0000\u0000\u030a\u0303\u0001\u0000\u0000\u0000\u030a\u0304\u0001"+
		"\u0000\u0000\u0000\u030a\u0305\u0001\u0000\u0000\u0000\u030a\u0306\u0001"+
		"\u0000\u0000\u0000\u030b\u0081\u0001\u0000\u0000\u0000\u030c\u030e\u0006"+
		"A\uffff\uffff\u0000\u030d\u030f\u0003\u0080@\u0000\u030e\u030d\u0001\u0000"+
		"\u0000\u0000\u030e\u030f\u0001\u0000\u0000\u0000\u030f\u0310\u0001\u0000"+
		"\u0000\u0000\u0310\u0311\u0005\u0011\u0000\u0000\u0311\u0312\u0003\u00a8"+
		"T\u0000\u0312\u0318\u0001\u0000\u0000\u0000\u0313\u0314\n\u0001\u0000"+
		"\u0000\u0314\u0315\u0005\u0011\u0000\u0000\u0315\u0317\u0003\u00a8T\u0000"+
		"\u0316\u0313\u0001\u0000\u0000\u0000\u0317\u031a\u0001\u0000\u0000\u0000"+
		"\u0318\u0316\u0001\u0000\u0000\u0000\u0318\u0319\u0001\u0000\u0000\u0000"+
		"\u0319\u0083\u0001\u0000\u0000\u0000\u031a\u0318\u0001\u0000\u0000\u0000"+
		"\u031b\u031c\u0005\u0011\u0000\u0000\u031c\u0320\u0003\u0004\u0002\u0000"+
		"\u031d\u031e\u0005\u0001\u0000\u0000\u031e\u0321\u0003\u0004\u0002\u0000"+
		"\u031f\u0321\u0003\u00b4Z\u0000\u0320\u031d\u0001\u0000\u0000\u0000\u0320"+
		"\u031f\u0001\u0000\u0000\u0000\u0321\u0085\u0001\u0000\u0000\u0000\u0322"+
		"\u0323\u0005\u000e\u0000\u0000\u0323\u0329\u0005\u000f\u0000\u0000\u0324"+
		"\u0325\u0005\u000e\u0000\u0000\u0325\u0326\u0003T*\u0000\u0326\u0327\u0003"+
		"\u0088D\u0000\u0327\u0329\u0001\u0000\u0000\u0000\u0328\u0322\u0001\u0000"+
		"\u0000\u0000\u0328\u0324\u0001\u0000\u0000\u0000\u0329\u0087\u0001\u0000"+
		"\u0000\u0000\u032a\u0334\u0005\u000f\u0000\u0000\u032b\u032c\u0005\f\u0000"+
		"\u0000\u032c\u032d\u0003T*\u0000\u032d\u032e\u0005\u000f\u0000\u0000\u032e"+
		"\u0334\u0001\u0000\u0000\u0000\u032f\u0330\u0005\u0006\u0000\u0000\u0330"+
		"\u0331\u0003T*\u0000\u0331\u0332\u0003\u0088D\u0000\u0332\u0334\u0001"+
		"\u0000\u0000\u0000\u0333\u032a\u0001\u0000\u0000\u0000\u0333\u032b\u0001"+
		"\u0000\u0000\u0000\u0333\u032f\u0001\u0000\u0000\u0000\u0334\u0089\u0001"+
		"\u0000\u0000\u0000\u0335\u0336\u0005\u0016\u0000\u0000\u0336\u033c\u0005"+
		"\u0017\u0000\u0000\u0337\u0338\u0005\u0016\u0000\u0000\u0338\u0339\u0003"+
		"\u008cF\u0000\u0339\u033a\u0005\u0017\u0000\u0000\u033a\u033c\u0001\u0000"+
		"\u0000\u0000\u033b\u0335\u0001\u0000\u0000\u0000\u033b\u0337\u0001\u0000"+
		"\u0000\u0000\u033c\u008b\u0001\u0000\u0000\u0000\u033d\u0342\u0003\u008e"+
		"G\u0000\u033e\u033f\u0005\u0006\u0000\u0000\u033f\u0341\u0003\u008eG\u0000"+
		"\u0340\u033e\u0001\u0000\u0000\u0000\u0341\u0344\u0001\u0000\u0000\u0000"+
		"\u0342\u0340\u0001\u0000\u0000\u0000\u0342\u0343\u0001\u0000\u0000\u0000"+
		"\u0343\u008d\u0001\u0000\u0000\u0000\u0344\u0342\u0001\u0000\u0000\u0000"+
		"\u0345\u0346\u0003\u0090H\u0000\u0346\u0347\u0003\u0092I\u0000\u0347\u0348"+
		"\u0003\u0094J\u0000\u0348\u008f\u0001\u0000\u0000\u0000\u0349\u034b\u0003"+
		"\u00eau\u0000\u034a\u0349\u0001\u0000\u0000\u0000\u034a\u034b\u0001\u0000"+
		"\u0000\u0000\u034b\u034c\u0001\u0000\u0000\u0000\u034c\u034d\u0003l6\u0000"+
		"\u034d\u0091\u0001\u0000\u0000\u0000\u034e\u034f\u0005\u0005\u0000\u0000"+
		"\u034f\u0351\u0003\u009aM\u0000\u0350\u034e\u0001\u0000\u0000\u0000\u0350"+
		"\u0351\u0001\u0000\u0000\u0000\u0351\u0093\u0001\u0000\u0000\u0000\u0352"+
		"\u0353\u0005 \u0000\u0000\u0353\u0355\u0003\u0096K\u0000\u0354\u0352\u0001"+
		"\u0000\u0000\u0000\u0354\u0355\u0001\u0000\u0000\u0000\u0355\u0095\u0001"+
		"\u0000\u0000\u0000\u0356\u035b\u0003\u0098L\u0000\u0357\u0358\u0005\u0002"+
		"\u0000\u0000\u0358\u035a\u0003\u0098L\u0000\u0359\u0357\u0001\u0000\u0000"+
		"\u0000\u035a\u035d\u0001\u0000\u0000\u0000\u035b\u0359\u0001\u0000\u0000"+
		"\u0000\u035b\u035c\u0001\u0000\u0000\u0000\u035c\u0097\u0001\u0000\u0000"+
		"\u0000\u035d\u035b\u0001\u0000\u0000\u0000\u035e\u0361\u0003\u0004\u0002"+
		"\u0000\u035f\u0360\u0005\u0005\u0000\u0000\u0360\u0362\u0003\n\u0005\u0000"+
		"\u0361\u035f\u0001\u0000\u0000\u0000\u0361\u0362\u0001\u0000\u0000\u0000"+
		"\u0362\u0099\u0001\u0000\u0000\u0000\u0363\u0364\u0003l6\u0000\u0364\u009b"+
		"\u0001\u0000\u0000\u0000\u0365\u0366\u0005\u000e\u0000\u0000\u0366\u0367"+
		"\u0003T*\u0000\u0367\u0368\u0005!\u0000\u0000\u0368\u0369\u0003\u00a0"+
		"P\u0000\u0369\u036a\u0005\u000f\u0000\u0000\u036a\u009d\u0001\u0000\u0000"+
		"\u0000\u036b\u036c\u0005\u0016\u0000\u0000\u036c\u036d\u0003l6\u0000\u036d"+
		"\u036e\u0005!\u0000\u0000\u036e\u036f\u0003\u00a0P\u0000\u036f\u0370\u0005"+
		"\u0017\u0000\u0000\u0370\u009f\u0001\u0000\u0000\u0000\u0371\u0376\u0003"+
		"\u00a2Q\u0000\u0372\u0373\u0005\u0006\u0000\u0000\u0373\u0375\u0003\u00a2"+
		"Q\u0000\u0374\u0372\u0001\u0000\u0000\u0000\u0375\u0378\u0001\u0000\u0000"+
		"\u0000\u0376\u0374\u0001\u0000\u0000\u0000\u0376\u0377\u0001\u0000\u0000"+
		"\u0000\u0377\u00a1\u0001\u0000\u0000\u0000\u0378\u0376\u0001\u0000\u0000"+
		"\u0000\u0379\u0383\u0003T*\u0000\u037a\u037b\u0003T*\u0000\u037b\u037c"+
		"\u0005\"\u0000\u0000\u037c\u037d\u0003T*\u0000\u037d\u0383\u0001\u0000"+
		"\u0000\u0000\u037e\u037f\u0003\u008aE\u0000\u037f\u0380\u0005#\u0000\u0000"+
		"\u0380\u0381\u0003T*\u0000\u0381\u0383\u0001\u0000\u0000\u0000\u0382\u0379"+
		"\u0001\u0000\u0000\u0000\u0382\u037a\u0001\u0000\u0000\u0000\u0382\u037e"+
		"\u0001\u0000\u0000\u0000\u0383\u00a3\u0001\u0000\u0000\u0000\u0384\u0386"+
		"\u0005\b\u0000\u0000\u0385\u0387\u0003\u00e2q\u0000\u0386\u0385\u0001"+
		"\u0000\u0000\u0000\u0386\u0387\u0001\u0000\u0000\u0000\u0387\u0388\u0001"+
		"\u0000\u0000\u0000\u0388\u0389\u0005\t\u0000\u0000\u0389\u00a5\u0001\u0000"+
		"\u0000\u0000\u038a\u038c\u0006S\uffff\uffff\u0000\u038b\u038d\u0003l6"+
		"\u0000\u038c\u038b\u0001\u0000\u0000\u0000\u038c\u038d\u0001\u0000\u0000"+
		"\u0000\u038d\u038e\u0001\u0000\u0000\u0000\u038e\u038f\u0005\u0011\u0000"+
		"\u0000\u038f\u0390\u0003\u00a8T\u0000\u0390\u0396\u0001\u0000\u0000\u0000"+
		"\u0391\u0392\n\u0001\u0000\u0000\u0392\u0393\u0005\u0011\u0000\u0000\u0393"+
		"\u0395\u0003\u00a8T\u0000\u0394\u0391\u0001\u0000\u0000\u0000\u0395\u0398"+
		"\u0001\u0000\u0000\u0000\u0396\u0394\u0001\u0000\u0000\u0000\u0396\u0397"+
		"\u0001\u0000\u0000\u0000\u0397\u00a7\u0001\u0000\u0000\u0000\u0398\u0396"+
		"\u0001\u0000\u0000\u0000\u0399\u03a2\u0005\b\u0000\u0000\u039a\u039f\u0003"+
		"\u00aaU\u0000\u039b\u039c\u0005\u0006\u0000\u0000\u039c\u039e\u0003\u00aa"+
		"U\u0000\u039d\u039b\u0001\u0000\u0000\u0000\u039e\u03a1\u0001\u0000\u0000"+
		"\u0000\u039f\u039d\u0001\u0000\u0000\u0000\u039f\u03a0\u0001\u0000\u0000"+
		"\u0000\u03a0\u03a3\u0001\u0000\u0000\u0000\u03a1\u039f\u0001\u0000\u0000"+
		"\u0000\u03a2\u039a\u0001\u0000\u0000\u0000\u03a2\u03a3\u0001\u0000\u0000"+
		"\u0000\u03a3\u03a4\u0001\u0000\u0000\u0000\u03a4\u03a5\u0005\t\u0000\u0000"+
		"\u03a5\u00a9\u0001\u0000\u0000\u0000\u03a6\u03a9\u0003\u00acV\u0000\u03a7"+
		"\u03a9\u0003\u00aeW\u0000\u03a8\u03a6\u0001\u0000\u0000\u0000\u03a8\u03a7"+
		"\u0001\u0000\u0000\u0000\u03a9\u00ab\u0001\u0000\u0000\u0000\u03aa\u03ab"+
		"\u0003\u00b0X\u0000\u03ab\u03ac\u0005\u0014\u0000\u0000\u03ac\u03ad\u0003"+
		"T*\u0000\u03ad\u00ad\u0001\u0000\u0000\u0000\u03ae\u03af\u0003\u00b0X"+
		"\u0000\u03af\u03b0\u0005\u0015\u0000\u0000\u03b0\u03b1\u0003T*\u0000\u03b1"+
		"\u00af\u0001\u0000\u0000\u0000\u03b2\u03b3\u0003T*\u0000\u03b3\u00b1\u0001"+
		"\u0000\u0000\u0000\u03b4\u03b6\u0006Y\uffff\uffff\u0000\u03b5\u03b7\u0003"+
		"l6\u0000\u03b6\u03b5\u0001\u0000\u0000\u0000\u03b6\u03b7\u0001\u0000\u0000"+
		"\u0000\u03b7\u03b8\u0001\u0000\u0000\u0000\u03b8\u03b9\u0005\u0011\u0000"+
		"\u0000\u03b9\u03bd\u0003\u0004\u0002\u0000\u03ba\u03bb\u0005\u0001\u0000"+
		"\u0000\u03bb\u03be\u0003\u0004\u0002\u0000\u03bc\u03be\u0003\u00b4Z\u0000"+
		"\u03bd\u03ba\u0001\u0000\u0000\u0000\u03bd\u03bc\u0001\u0000\u0000\u0000"+
		"\u03be\u03c9\u0001\u0000\u0000\u0000\u03bf\u03c0\n\u0001\u0000\u0000\u03c0"+
		"\u03c1\u0005\u0011\u0000\u0000\u03c1\u03c5\u0003\u0004\u0002\u0000\u03c2"+
		"\u03c3\u0005\u0001\u0000\u0000\u03c3\u03c6\u0003\u0004\u0002\u0000\u03c4"+
		"\u03c6\u0003\u00b4Z\u0000\u03c5\u03c2\u0001\u0000\u0000\u0000\u03c5\u03c4"+
		"\u0001\u0000\u0000\u0000\u03c6\u03c8\u0001\u0000\u0000\u0000\u03c7\u03bf"+
		"\u0001\u0000\u0000\u0000\u03c8\u03cb\u0001\u0000\u0000\u0000\u03c9\u03c7"+
		"\u0001\u0000\u0000\u0000\u03c9\u03ca\u0001\u0000\u0000\u0000\u03ca\u00b3"+
		"\u0001\u0000\u0000\u0000\u03cb\u03c9\u0001\u0000\u0000\u0000\u03cc\u03ce"+
		"\u0005\b\u0000\u0000\u03cd\u03cf\u0003\u00b6[\u0000\u03ce\u03cd\u0001"+
		"\u0000\u0000\u0000\u03ce\u03cf\u0001\u0000\u0000\u0000\u03cf\u03d0\u0001"+
		"\u0000\u0000\u0000\u03d0\u03d1\u0005\t\u0000\u0000\u03d1\u00b5\u0001\u0000"+
		"\u0000\u0000\u03d2\u03d7\u0003\u00b8\\\u0000\u03d3\u03d4\u0005\u0006\u0000"+
		"\u0000\u03d4\u03d6\u0003\u00b8\\\u0000\u03d5\u03d3\u0001\u0000\u0000\u0000"+
		"\u03d6\u03d9\u0001\u0000\u0000\u0000\u03d7\u03d5\u0001\u0000\u0000\u0000"+
		"\u03d7\u03d8\u0001\u0000\u0000\u0000\u03d8\u00b7\u0001\u0000\u0000\u0000"+
		"\u03d9\u03d7\u0001\u0000\u0000\u0000\u03da\u03dd\u0003\u0006\u0003\u0000"+
		"\u03db\u03dd\u0003\u0004\u0002\u0000\u03dc\u03da\u0001\u0000\u0000\u0000"+
		"\u03dc\u03db\u0001\u0000\u0000\u0000\u03dd\u03de\u0001\u0000\u0000\u0000"+
		"\u03de\u03df\u0005\u001a\u0000\u0000\u03df\u03e0\u0003T*\u0000\u03e0\u00b9"+
		"\u0001\u0000\u0000\u0000\u03e1\u03e2\u0003j5\u0000\u03e2\u03e3\u0003\u00de"+
		"o\u0000\u03e3\u00bb\u0001\u0000\u0000\u0000\u03e4\u03e5\u0005$\u0000\u0000"+
		"\u03e5\u03e6\u0003\u00be_\u0000\u03e6\u03e7\u0005\u001f\u0000\u0000\u03e7"+
		"\u00bd\u0001\u0000\u0000\u0000\u03e8\u03ed\u0003\u00c0`\u0000\u03e9\u03ea"+
		"\u0005\n\u0000\u0000\u03ea\u03ec\u0003\u00c0`\u0000\u03eb\u03e9\u0001"+
		"\u0000\u0000\u0000\u03ec\u03ef\u0001\u0000\u0000\u0000\u03ed\u03eb\u0001"+
		"\u0000\u0000\u0000\u03ed\u03ee\u0001\u0000\u0000\u0000\u03ee\u00bf\u0001"+
		"\u0000\u0000\u0000\u03ef\u03ed\u0001\u0000\u0000\u0000\u03f0\u03f1\u0003"+
		"\u00e6s\u0000\u03f1\u03f2\u0003R)\u0000\u03f2\u00c1\u0001\u0000\u0000"+
		"\u0000\u03f3\u03f4\u0005%\u0000\u0000\u03f4\u03f5\u0003T*\u0000\u03f5"+
		"\u03f6\u0005&\u0000\u0000\u03f6\u03f7\u0003\u00c4b\u0000\u03f7\u03f8\u0005"+
		"\u001f\u0000\u0000\u03f8\u00c3\u0001\u0000\u0000\u0000\u03f9\u03fe\u0003"+
		"\u00c6c\u0000\u03fa\u03fb\u0005\n\u0000\u0000\u03fb\u03fd\u0003\u00c6"+
		"c\u0000\u03fc\u03fa\u0001\u0000\u0000\u0000\u03fd\u0400\u0001\u0000\u0000"+
		"\u0000\u03fe\u03fc\u0001\u0000\u0000\u0000\u03fe\u03ff\u0001\u0000\u0000"+
		"\u0000\u03ff\u00c5\u0001\u0000\u0000\u0000\u0400\u03fe\u0001\u0000\u0000"+
		"\u0000\u0401\u0402\u0003T*\u0000\u0402\u0403\u0003P(\u0000\u0403\u0404"+
		"\u0003R)\u0000\u0404\u00c7\u0001\u0000\u0000\u0000\u0405\u0406\u0005\'"+
		"\u0000\u0000\u0406\u0407\u0003\u00c4b\u0000\u0407\u0408\u0005\u001f\u0000"+
		"\u0000\u0408\u0417\u0001\u0000\u0000\u0000\u0409\u040a\u0005\'\u0000\u0000"+
		"\u040a\u040b\u0005(\u0000\u0000\u040b\u040c\u0003T*\u0000\u040c\u040d"+
		"\u0003R)\u0000\u040d\u040e\u0005\u001f\u0000\u0000\u040e\u0417\u0001\u0000"+
		"\u0000\u0000\u040f\u0410\u0005\'\u0000\u0000\u0410\u0411\u0003\u00c4b"+
		"\u0000\u0411\u0412\u0005(\u0000\u0000\u0412\u0413\u0003T*\u0000\u0413"+
		"\u0414\u0003R)\u0000\u0414\u0415\u0005\u001f\u0000\u0000\u0415\u0417\u0001"+
		"\u0000\u0000\u0000\u0416\u0405\u0001\u0000\u0000\u0000\u0416\u0409\u0001"+
		"\u0000\u0000\u0000\u0416\u040f\u0001\u0000\u0000\u0000\u0417\u00c9\u0001"+
		"\u0000\u0000\u0000\u0418\u0419\u0005\u0012\u0000\u0000\u0419\u041a\u0003"+
		"\u0004\u0002\u0000\u041a\u041b\u0005 \u0000\u0000\u041b\u041c\u0003\n"+
		"\u0005\u0000\u041c\u0429\u0001\u0000\u0000\u0000\u041d\u041e\u0005\u0012"+
		"\u0000\u0000\u041e\u041f\u0003\u00ccf\u0000\u041f\u0420\u0005\u0005\u0000"+
		"\u0000\u0420\u0421\u0003\u00ccf\u0000\u0421\u0422\u0005 \u0000\u0000\u0422"+
		"\u0423\u0003\u00ceg\u0000\u0423\u0429\u0001\u0000\u0000\u0000\u0424\u0425"+
		"\u0005\u0012\u0000\u0000\u0425\u0426\u0003\u00d0h\u0000\u0426\u0427\u0005"+
		"\u001f\u0000\u0000\u0427\u0429\u0001\u0000\u0000\u0000\u0428\u0418\u0001"+
		"\u0000\u0000\u0000\u0428\u041d\u0001\u0000\u0000\u0000\u0428\u0424\u0001"+
		"\u0000\u0000\u0000\u0429\u00cb\u0001\u0000\u0000\u0000\u042a\u042d\u0003"+
		"\u0004\u0002\u0000\u042b\u042d\u0003\u0006\u0003\u0000\u042c\u042a\u0001"+
		"\u0000\u0000\u0000\u042c\u042b\u0001\u0000\u0000\u0000\u042d\u00cd\u0001"+
		"\u0000\u0000\u0000\u042e\u0431\u0003\n\u0005\u0000\u042f\u0431\u0003\u0006"+
		"\u0003\u0000\u0430\u042e\u0001\u0000\u0000\u0000\u0430\u042f\u0001\u0000"+
		"\u0000\u0000\u0431\u00cf\u0001\u0000\u0000\u0000\u0432\u0437\u0003\u00d2"+
		"i\u0000\u0433\u0434\u0005\n\u0000\u0000\u0434\u0436\u0003\u00d2i\u0000"+
		"\u0435\u0433\u0001\u0000\u0000\u0000\u0436\u0439\u0001\u0000\u0000\u0000"+
		"\u0437\u0435\u0001\u0000\u0000\u0000\u0437\u0438\u0001\u0000\u0000\u0000"+
		"\u0438\u00d1\u0001\u0000\u0000\u0000\u0439\u0437\u0001\u0000\u0000\u0000"+
		"\u043a\u043b\u0003\u00e0p\u0000\u043b\u043c\u0003P(\u0000\u043c\u043d"+
		"\u0003R)\u0000\u043d\u0444\u0001\u0000\u0000\u0000\u043e\u043f\u0003\u0006"+
		"\u0003\u0000\u043f\u0440\u0003\u00e0p\u0000\u0440\u0441\u0003P(\u0000"+
		"\u0441\u0442\u0003R)\u0000\u0442\u0444\u0001\u0000\u0000\u0000\u0443\u043a"+
		"\u0001\u0000\u0000\u0000\u0443\u043e\u0001\u0000\u0000\u0000\u0444\u00d3"+
		"\u0001\u0000\u0000\u0000\u0445\u0446\u0005)\u0000\u0000\u0446\u0449\u0003"+
		"\u00e2q\u0000\u0447\u0448\u0005&\u0000\u0000\u0448\u044a\u0003\u00c4b"+
		"\u0000\u0449\u0447\u0001\u0000\u0000\u0000\u0449\u044a\u0001\u0000\u0000"+
		"\u0000\u044a\u044b\u0001\u0000\u0000\u0000\u044b\u044c\u0003\u00d6k\u0000"+
		"\u044c\u00d5\u0001\u0000\u0000\u0000\u044d\u044e\u0005\u0019\u0000\u0000"+
		"\u044e\u044f\u0003\u00d8l\u0000\u044f\u0450\u0005\u001f\u0000\u0000\u0450"+
		"\u045c\u0001\u0000\u0000\u0000\u0451\u0452\u0005\u0019\u0000\u0000\u0452"+
		"\u0453\u0003\u00d8l\u0000\u0453\u0454\u0005(\u0000\u0000\u0454\u0455\u0003"+
		"\u00e2q\u0000\u0455\u0456\u0005\u001f\u0000\u0000\u0456\u045c\u0001\u0000"+
		"\u0000\u0000\u0457\u0458\u0005(\u0000\u0000\u0458\u0459\u0003\u00e2q\u0000"+
		"\u0459\u045a\u0005\u001f\u0000\u0000\u045a\u045c\u0001\u0000\u0000\u0000"+
		"\u045b\u044d\u0001\u0000\u0000\u0000\u045b\u0451\u0001\u0000\u0000\u0000"+
		"\u045b\u0457\u0001\u0000\u0000\u0000\u045c\u00d7\u0001\u0000\u0000\u0000"+
		"\u045d\u0462\u0003\u00dam\u0000\u045e\u045f\u0005\n\u0000\u0000\u045f"+
		"\u0461\u0003\u00dam\u0000\u0460\u045e\u0001\u0000\u0000\u0000\u0461\u0464"+
		"\u0001\u0000\u0000\u0000\u0462\u0460\u0001\u0000\u0000\u0000\u0462\u0463"+
		"\u0001\u0000\u0000\u0000\u0463\u00d9\u0001\u0000\u0000\u0000\u0464\u0462"+
		"\u0001\u0000\u0000\u0000\u0465\u0466\u0003T*\u0000\u0466\u0467\u0003P"+
		"(\u0000\u0467\u0468\u0003R)\u0000\u0468\u0474\u0001\u0000\u0000\u0000"+
		"\u0469\u046a\u0003\u00ccf\u0000\u046a\u046b\u0005\u0005\u0000\u0000\u046b"+
		"\u046d\u0001\u0000\u0000\u0000\u046c\u0469\u0001\u0000\u0000\u0000\u046c"+
		"\u046d\u0001\u0000\u0000\u0000\u046d\u046e\u0001\u0000\u0000\u0000\u046e"+
		"\u046f\u0003n7\u0000\u046f\u0470\u0003\u00dcn\u0000\u0470\u0471\u0003"+
		"P(\u0000\u0471\u0472\u0003R)\u0000\u0472\u0474\u0001\u0000\u0000\u0000"+
		"\u0473\u0465\u0001\u0000\u0000\u0000\u0473\u046c\u0001\u0000\u0000\u0000"+
		"\u0474\u00db\u0001\u0000\u0000\u0000\u0475\u0476\u0005\u0005\u0000\u0000"+
		"\u0476\u0478\u0003\u0006\u0003\u0000\u0477\u0475\u0001\u0000\u0000\u0000"+
		"\u0477\u0478\u0001\u0000\u0000\u0000\u0478\u00dd\u0001\u0000\u0000\u0000"+
		"\u0479\u047b\u0005\u0003\u0000\u0000\u047a\u047c\u0003\u00e2q\u0000\u047b"+
		"\u047a\u0001\u0000\u0000\u0000\u047b\u047c\u0001\u0000\u0000\u0000\u047c"+
		"\u047d\u0001\u0000\u0000\u0000\u047d\u047e\u0005\u0004\u0000\u0000\u047e"+
		"\u00df\u0001\u0000\u0000\u0000\u047f\u0481\u0005\u0003\u0000\u0000\u0480"+
		"\u0482\u0003\u00e4r\u0000\u0481\u0480\u0001\u0000\u0000\u0000\u0481\u0482"+
		"\u0001\u0000\u0000\u0000\u0482\u0483\u0001\u0000\u0000\u0000\u0483\u0484"+
		"\u0005\u0004\u0000\u0000\u0484\u00e1\u0001\u0000\u0000\u0000\u0485\u048a"+
		"\u0003T*\u0000\u0486\u0487\u0005\u0006\u0000\u0000\u0487\u0489\u0003T"+
		"*\u0000\u0488\u0486\u0001\u0000\u0000\u0000\u0489\u048c\u0001\u0000\u0000"+
		"\u0000\u048a\u0488\u0001\u0000\u0000\u0000\u048a\u048b\u0001\u0000\u0000"+
		"\u0000\u048b\u00e3\u0001\u0000\u0000\u0000\u048c\u048a\u0001\u0000\u0000"+
		"\u0000\u048d\u0492\u0003n7\u0000\u048e\u048f\u0005\u0006\u0000\u0000\u048f"+
		"\u0491\u0003n7\u0000\u0490\u048e\u0001\u0000\u0000\u0000\u0491\u0494\u0001"+
		"\u0000\u0000\u0000\u0492\u0490\u0001\u0000\u0000\u0000\u0492\u0493\u0001"+
		"\u0000\u0000\u0000\u0493\u00e5\u0001\u0000\u0000\u0000\u0494\u0492\u0001"+
		"\u0000\u0000\u0000\u0495\u049a\u0003\u00e2q\u0000\u0496\u0497\u0005\n"+
		"\u0000\u0000\u0497\u0499\u0003\u00e2q\u0000\u0498\u0496\u0001\u0000\u0000"+
		"\u0000\u0499\u049c\u0001\u0000\u0000\u0000\u049a\u0498\u0001\u0000\u0000"+
		"\u0000\u049a\u049b\u0001\u0000\u0000\u0000\u049b\u00e7\u0001\u0000\u0000"+
		"\u0000\u049c\u049a\u0001\u0000\u0000\u0000\u049d\u04a7\u0003\f\u0006\u0000"+
		"\u049e\u04a7\u0003\n\u0005\u0000\u049f\u04a7\u0003\b\u0004\u0000\u04a0"+
		"\u04a7\u0003\u0004\u0002\u0000\u04a1\u04a3\u0003\u000e\u0007\u0000\u04a2"+
		"\u04a1\u0001\u0000\u0000\u0000\u04a3\u04a4\u0001\u0000\u0000\u0000\u04a4"+
		"\u04a2\u0001\u0000\u0000\u0000\u04a4\u04a5\u0001\u0000\u0000\u0000\u04a5"+
		"\u04a7\u0001\u0000\u0000\u0000\u04a6\u049d\u0001\u0000\u0000\u0000\u04a6"+
		"\u049e\u0001\u0000\u0000\u0000\u04a6\u049f\u0001\u0000\u0000\u0000\u04a6"+
		"\u04a0\u0001\u0000\u0000\u0000\u04a6\u04a2\u0001\u0000\u0000\u0000\u04a7"+
		"\u00e9\u0001\u0000\u0000\u0000\u04a8\u04a9\u0007\u0002\u0000\u0000\u04a9"+
		"\u00eb\u0001\u0000\u0000\u0000\u04aa\u04ab\u0007\u0003\u0000\u0000\u04ab"+
		"\u00ed\u0001\u0000\u0000\u0000\u04ac\u04ad\u0007\u0004\u0000\u0000\u04ad"+
		"\u00ef\u0001\u0000\u0000\u0000\u04ae\u04af\u0007\u0005\u0000\u0000\u04af"+
		"\u00f1\u0001\u0000\u0000\u0000\u04b0\u04b1\u0007\u0006\u0000\u0000\u04b1"+
		"\u00f3\u0001\u0000\u0000\u0000a\u00f7\u00fd\u011d\u0127\u012e\u0138\u014b"+
		"\u0156\u015c\u0163\u016f\u0176\u017c\u0183\u0188\u0193\u019f\u01a3\u01f3"+
		"\u01fb\u01ff\u020a\u0216\u022d\u0248\u024f\u025b\u0263\u026a\u0272\u027a"+
		"\u0281\u0289\u0292\u029b\u02a2\u02a6\u02ab\u02b0\u02c6\u02cb\u02d1\u02d7"+
		"\u02e2\u02ee\u02f5\u02f9\u02fd\u030a\u030e\u0318\u0320\u0328\u0333\u033b"+
		"\u0342\u034a\u0350\u0354\u035b\u0361\u0376\u0382\u0386\u038c\u0396\u039f"+
		"\u03a2\u03a8\u03b6\u03bd\u03c5\u03c9\u03ce\u03d7\u03dc\u03ed\u03fe\u0416"+
		"\u0428\u042c\u0430\u0437\u0443\u0449\u045b\u0462\u046c\u0473\u0477\u047b"+
		"\u0481\u048a\u0492\u049a\u04a4\u04a6";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}