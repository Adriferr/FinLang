# Generated from FinLang.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,24,98,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,1,0,5,0,20,8,0,10,0,12,0,23,9,0,1,0,1,0,1,1,1,
        1,1,1,1,1,1,1,1,1,3,1,33,8,1,1,2,1,2,1,2,1,2,3,2,39,8,2,1,3,1,3,
        1,4,1,4,1,4,1,4,1,5,1,5,1,5,1,5,1,5,3,5,52,8,5,1,6,1,6,1,6,1,6,1,
        6,1,6,1,6,1,6,1,6,1,6,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,3,7,73,
        8,7,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,3,8,85,8,8,1,8,1,8,1,
        8,1,8,1,8,1,8,5,8,93,8,8,10,8,12,8,96,9,8,1,8,0,1,16,9,0,2,4,6,8,
        10,12,14,16,0,3,1,0,8,11,1,0,4,5,1,0,6,7,104,0,21,1,0,0,0,2,32,1,
        0,0,0,4,34,1,0,0,0,6,40,1,0,0,0,8,42,1,0,0,0,10,46,1,0,0,0,12,53,
        1,0,0,0,14,72,1,0,0,0,16,84,1,0,0,0,18,20,3,2,1,0,19,18,1,0,0,0,
        20,23,1,0,0,0,21,19,1,0,0,0,21,22,1,0,0,0,22,24,1,0,0,0,23,21,1,
        0,0,0,24,25,5,0,0,1,25,1,1,0,0,0,26,33,3,4,2,0,27,33,3,8,4,0,28,
        33,3,10,5,0,29,33,3,12,6,0,30,33,3,14,7,0,31,33,3,16,8,0,32,26,1,
        0,0,0,32,27,1,0,0,0,32,28,1,0,0,0,32,29,1,0,0,0,32,30,1,0,0,0,32,
        31,1,0,0,0,33,3,1,0,0,0,34,35,3,6,3,0,35,38,5,18,0,0,36,37,5,1,0,
        0,37,39,3,16,8,0,38,36,1,0,0,0,38,39,1,0,0,0,39,5,1,0,0,0,40,41,
        7,0,0,0,41,7,1,0,0,0,42,43,5,18,0,0,43,44,5,1,0,0,44,45,3,16,8,0,
        45,9,1,0,0,0,46,47,5,12,0,0,47,48,3,16,8,0,48,51,3,2,1,0,49,50,5,
        13,0,0,50,52,3,2,1,0,51,49,1,0,0,0,51,52,1,0,0,0,52,11,1,0,0,0,53,
        54,5,14,0,0,54,55,5,2,0,0,55,56,5,18,0,0,56,57,5,1,0,0,57,58,3,16,
        8,0,58,59,5,15,0,0,59,60,3,16,8,0,60,61,5,3,0,0,61,62,3,2,1,0,62,
        13,1,0,0,0,63,64,5,16,0,0,64,65,5,2,0,0,65,66,3,16,8,0,66,67,5,3,
        0,0,67,73,1,0,0,0,68,69,5,17,0,0,69,70,5,2,0,0,70,71,5,18,0,0,71,
        73,5,3,0,0,72,63,1,0,0,0,72,68,1,0,0,0,73,15,1,0,0,0,74,75,6,8,-1,
        0,75,76,5,2,0,0,76,77,3,16,8,0,77,78,5,3,0,0,78,85,1,0,0,0,79,85,
        5,21,0,0,80,85,5,19,0,0,81,85,5,20,0,0,82,85,5,22,0,0,83,85,5,18,
        0,0,84,74,1,0,0,0,84,79,1,0,0,0,84,80,1,0,0,0,84,81,1,0,0,0,84,82,
        1,0,0,0,84,83,1,0,0,0,85,94,1,0,0,0,86,87,10,8,0,0,87,88,7,1,0,0,
        88,93,3,16,8,9,89,90,10,7,0,0,90,91,7,2,0,0,91,93,3,16,8,8,92,86,
        1,0,0,0,92,89,1,0,0,0,93,96,1,0,0,0,94,92,1,0,0,0,94,95,1,0,0,0,
        95,17,1,0,0,0,96,94,1,0,0,0,8,21,32,38,51,72,84,92,94
    ]

class FinLangParser ( Parser ):

    grammarFileName = "FinLang.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'='", "'('", "')'", "'*'", "'/'", "'+'", 
                     "'-'", "'int'", "'real'", "'bool'", "'texto'", "'se'", 
                     "'senao'", "'repete'", "'at\\u00E9'", "'escreva'", 
                     "'leia'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "INT", "REAL", "BOOL_T", "TEXTO", "SE", "SENAO", "REPETE", 
                      "ATE", "ESCREVA", "LEIA", "ID", "NUM_INT", "NUM_REAL", 
                      "BOOL", "STRING", "COMMENT", "WS" ]

    RULE_programa = 0
    RULE_comando = 1
    RULE_declaracao = 2
    RULE_tipo = 3
    RULE_atribuicao = 4
    RULE_condicional = 5
    RULE_repeticao = 6
    RULE_entradaSaida = 7
    RULE_expr = 8

    ruleNames =  [ "programa", "comando", "declaracao", "tipo", "atribuicao", 
                   "condicional", "repeticao", "entradaSaida", "expr" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    INT=8
    REAL=9
    BOOL_T=10
    TEXTO=11
    SE=12
    SENAO=13
    REPETE=14
    ATE=15
    ESCREVA=16
    LEIA=17
    ID=18
    NUM_INT=19
    NUM_REAL=20
    BOOL=21
    STRING=22
    COMMENT=23
    WS=24

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(FinLangParser.EOF, 0)

        def comando(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(FinLangParser.ComandoContext)
            else:
                return self.getTypedRuleContext(FinLangParser.ComandoContext,i)


        def getRuleIndex(self):
            return FinLangParser.RULE_programa

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrograma" ):
                listener.enterPrograma(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrograma" ):
                listener.exitPrograma(self)




    def programa(self):

        localctx = FinLangParser.ProgramaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_programa)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 21
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 8347396) != 0):
                self.state = 18
                self.comando()
                self.state = 23
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 24
            self.match(FinLangParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ComandoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def declaracao(self):
            return self.getTypedRuleContext(FinLangParser.DeclaracaoContext,0)


        def atribuicao(self):
            return self.getTypedRuleContext(FinLangParser.AtribuicaoContext,0)


        def condicional(self):
            return self.getTypedRuleContext(FinLangParser.CondicionalContext,0)


        def repeticao(self):
            return self.getTypedRuleContext(FinLangParser.RepeticaoContext,0)


        def entradaSaida(self):
            return self.getTypedRuleContext(FinLangParser.EntradaSaidaContext,0)


        def expr(self):
            return self.getTypedRuleContext(FinLangParser.ExprContext,0)


        def getRuleIndex(self):
            return FinLangParser.RULE_comando

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComando" ):
                listener.enterComando(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComando" ):
                listener.exitComando(self)




    def comando(self):

        localctx = FinLangParser.ComandoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_comando)
        try:
            self.state = 32
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 26
                self.declaracao()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 27
                self.atribuicao()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 28
                self.condicional()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 29
                self.repeticao()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 30
                self.entradaSaida()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 31
                self.expr(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclaracaoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def tipo(self):
            return self.getTypedRuleContext(FinLangParser.TipoContext,0)


        def ID(self):
            return self.getToken(FinLangParser.ID, 0)

        def expr(self):
            return self.getTypedRuleContext(FinLangParser.ExprContext,0)


        def getRuleIndex(self):
            return FinLangParser.RULE_declaracao

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclaracao" ):
                listener.enterDeclaracao(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclaracao" ):
                listener.exitDeclaracao(self)




    def declaracao(self):

        localctx = FinLangParser.DeclaracaoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_declaracao)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 34
            self.tipo()
            self.state = 35
            self.match(FinLangParser.ID)
            self.state = 38
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==1:
                self.state = 36
                self.match(FinLangParser.T__0)
                self.state = 37
                self.expr(0)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TipoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(FinLangParser.INT, 0)

        def REAL(self):
            return self.getToken(FinLangParser.REAL, 0)

        def BOOL_T(self):
            return self.getToken(FinLangParser.BOOL_T, 0)

        def TEXTO(self):
            return self.getToken(FinLangParser.TEXTO, 0)

        def getRuleIndex(self):
            return FinLangParser.RULE_tipo

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTipo" ):
                listener.enterTipo(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTipo" ):
                listener.exitTipo(self)




    def tipo(self):

        localctx = FinLangParser.TipoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_tipo)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 40
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 3840) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AtribuicaoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(FinLangParser.ID, 0)

        def expr(self):
            return self.getTypedRuleContext(FinLangParser.ExprContext,0)


        def getRuleIndex(self):
            return FinLangParser.RULE_atribuicao

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAtribuicao" ):
                listener.enterAtribuicao(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAtribuicao" ):
                listener.exitAtribuicao(self)




    def atribuicao(self):

        localctx = FinLangParser.AtribuicaoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_atribuicao)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 42
            self.match(FinLangParser.ID)
            self.state = 43
            self.match(FinLangParser.T__0)
            self.state = 44
            self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CondicionalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SE(self):
            return self.getToken(FinLangParser.SE, 0)

        def expr(self):
            return self.getTypedRuleContext(FinLangParser.ExprContext,0)


        def comando(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(FinLangParser.ComandoContext)
            else:
                return self.getTypedRuleContext(FinLangParser.ComandoContext,i)


        def SENAO(self):
            return self.getToken(FinLangParser.SENAO, 0)

        def getRuleIndex(self):
            return FinLangParser.RULE_condicional

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCondicional" ):
                listener.enterCondicional(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCondicional" ):
                listener.exitCondicional(self)




    def condicional(self):

        localctx = FinLangParser.CondicionalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_condicional)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 46
            self.match(FinLangParser.SE)
            self.state = 47
            self.expr(0)
            self.state = 48
            self.comando()
            self.state = 51
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.state = 49
                self.match(FinLangParser.SENAO)
                self.state = 50
                self.comando()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RepeticaoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def REPETE(self):
            return self.getToken(FinLangParser.REPETE, 0)

        def ID(self):
            return self.getToken(FinLangParser.ID, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(FinLangParser.ExprContext)
            else:
                return self.getTypedRuleContext(FinLangParser.ExprContext,i)


        def ATE(self):
            return self.getToken(FinLangParser.ATE, 0)

        def comando(self):
            return self.getTypedRuleContext(FinLangParser.ComandoContext,0)


        def getRuleIndex(self):
            return FinLangParser.RULE_repeticao

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRepeticao" ):
                listener.enterRepeticao(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRepeticao" ):
                listener.exitRepeticao(self)




    def repeticao(self):

        localctx = FinLangParser.RepeticaoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_repeticao)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 53
            self.match(FinLangParser.REPETE)
            self.state = 54
            self.match(FinLangParser.T__1)
            self.state = 55
            self.match(FinLangParser.ID)
            self.state = 56
            self.match(FinLangParser.T__0)
            self.state = 57
            self.expr(0)
            self.state = 58
            self.match(FinLangParser.ATE)
            self.state = 59
            self.expr(0)
            self.state = 60
            self.match(FinLangParser.T__2)
            self.state = 61
            self.comando()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EntradaSaidaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ESCREVA(self):
            return self.getToken(FinLangParser.ESCREVA, 0)

        def expr(self):
            return self.getTypedRuleContext(FinLangParser.ExprContext,0)


        def LEIA(self):
            return self.getToken(FinLangParser.LEIA, 0)

        def ID(self):
            return self.getToken(FinLangParser.ID, 0)

        def getRuleIndex(self):
            return FinLangParser.RULE_entradaSaida

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEntradaSaida" ):
                listener.enterEntradaSaida(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEntradaSaida" ):
                listener.exitEntradaSaida(self)




    def entradaSaida(self):

        localctx = FinLangParser.EntradaSaidaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_entradaSaida)
        try:
            self.state = 72
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [16]:
                self.enterOuterAlt(localctx, 1)
                self.state = 63
                self.match(FinLangParser.ESCREVA)
                self.state = 64
                self.match(FinLangParser.T__1)
                self.state = 65
                self.expr(0)
                self.state = 66
                self.match(FinLangParser.T__2)
                pass
            elif token in [17]:
                self.enterOuterAlt(localctx, 2)
                self.state = 68
                self.match(FinLangParser.LEIA)
                self.state = 69
                self.match(FinLangParser.T__1)
                self.state = 70
                self.match(FinLangParser.ID)
                self.state = 71
                self.match(FinLangParser.T__2)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.op = None # Token

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(FinLangParser.ExprContext)
            else:
                return self.getTypedRuleContext(FinLangParser.ExprContext,i)


        def BOOL(self):
            return self.getToken(FinLangParser.BOOL, 0)

        def NUM_INT(self):
            return self.getToken(FinLangParser.NUM_INT, 0)

        def NUM_REAL(self):
            return self.getToken(FinLangParser.NUM_REAL, 0)

        def STRING(self):
            return self.getToken(FinLangParser.STRING, 0)

        def ID(self):
            return self.getToken(FinLangParser.ID, 0)

        def getRuleIndex(self):
            return FinLangParser.RULE_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr" ):
                listener.enterExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr" ):
                listener.exitExpr(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = FinLangParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 16
        self.enterRecursionRule(localctx, 16, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 84
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [2]:
                self.state = 75
                self.match(FinLangParser.T__1)
                self.state = 76
                self.expr(0)
                self.state = 77
                self.match(FinLangParser.T__2)
                pass
            elif token in [21]:
                self.state = 79
                self.match(FinLangParser.BOOL)
                pass
            elif token in [19]:
                self.state = 80
                self.match(FinLangParser.NUM_INT)
                pass
            elif token in [20]:
                self.state = 81
                self.match(FinLangParser.NUM_REAL)
                pass
            elif token in [22]:
                self.state = 82
                self.match(FinLangParser.STRING)
                pass
            elif token in [18]:
                self.state = 83
                self.match(FinLangParser.ID)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 94
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,7,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 92
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
                    if la_ == 1:
                        localctx = FinLangParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 86
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 87
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==4 or _la==5):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 88
                        self.expr(9)
                        pass

                    elif la_ == 2:
                        localctx = FinLangParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 89
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 90
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==6 or _la==7):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 91
                        self.expr(8)
                        pass

             
                self.state = 96
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,7,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[8] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 8)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 7)
         




