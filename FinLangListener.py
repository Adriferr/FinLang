# Generated from FinLang.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .FinLangParser import FinLangParser
else:
    from FinLangParser import FinLangParser

# This class defines a complete listener for a parse tree produced by FinLangParser.
class FinLangListener(ParseTreeListener):

    # Enter a parse tree produced by FinLangParser#programa.
    def enterPrograma(self, ctx:FinLangParser.ProgramaContext):
        pass

    # Exit a parse tree produced by FinLangParser#programa.
    def exitPrograma(self, ctx:FinLangParser.ProgramaContext):
        pass


    # Enter a parse tree produced by FinLangParser#comando.
    def enterComando(self, ctx:FinLangParser.ComandoContext):
        pass

    # Exit a parse tree produced by FinLangParser#comando.
    def exitComando(self, ctx:FinLangParser.ComandoContext):
        pass


    # Enter a parse tree produced by FinLangParser#declaracao.
    def enterDeclaracao(self, ctx:FinLangParser.DeclaracaoContext):
        pass

    # Exit a parse tree produced by FinLangParser#declaracao.
    def exitDeclaracao(self, ctx:FinLangParser.DeclaracaoContext):
        pass


    # Enter a parse tree produced by FinLangParser#tipo.
    def enterTipo(self, ctx:FinLangParser.TipoContext):
        pass

    # Exit a parse tree produced by FinLangParser#tipo.
    def exitTipo(self, ctx:FinLangParser.TipoContext):
        pass


    # Enter a parse tree produced by FinLangParser#atribuicao.
    def enterAtribuicao(self, ctx:FinLangParser.AtribuicaoContext):
        pass

    # Exit a parse tree produced by FinLangParser#atribuicao.
    def exitAtribuicao(self, ctx:FinLangParser.AtribuicaoContext):
        pass


    # Enter a parse tree produced by FinLangParser#condicional.
    def enterCondicional(self, ctx:FinLangParser.CondicionalContext):
        pass

    # Exit a parse tree produced by FinLangParser#condicional.
    def exitCondicional(self, ctx:FinLangParser.CondicionalContext):
        pass


    # Enter a parse tree produced by FinLangParser#repeticao.
    def enterRepeticao(self, ctx:FinLangParser.RepeticaoContext):
        pass

    # Exit a parse tree produced by FinLangParser#repeticao.
    def exitRepeticao(self, ctx:FinLangParser.RepeticaoContext):
        pass


    # Enter a parse tree produced by FinLangParser#entradaSaida.
    def enterEntradaSaida(self, ctx:FinLangParser.EntradaSaidaContext):
        pass

    # Exit a parse tree produced by FinLangParser#entradaSaida.
    def exitEntradaSaida(self, ctx:FinLangParser.EntradaSaidaContext):
        pass


    # Enter a parse tree produced by FinLangParser#expr.
    def enterExpr(self, ctx:FinLangParser.ExprContext):
        pass

    # Exit a parse tree produced by FinLangParser#expr.
    def exitExpr(self, ctx:FinLangParser.ExprContext):
        pass



del FinLangParser