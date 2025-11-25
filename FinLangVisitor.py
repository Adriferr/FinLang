# Generated from FinLang.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .FinLangParser import FinLangParser
else:
    from FinLangParser import FinLangParser

# This class defines a complete generic visitor for a parse tree produced by FinLangParser.

class FinLangVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by FinLangParser#programa.
    def visitPrograma(self, ctx:FinLangParser.ProgramaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FinLangParser#comando.
    def visitComando(self, ctx:FinLangParser.ComandoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FinLangParser#bloco.
    def visitBloco(self, ctx:FinLangParser.BlocoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FinLangParser#declaracao.
    def visitDeclaracao(self, ctx:FinLangParser.DeclaracaoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FinLangParser#tipo.
    def visitTipo(self, ctx:FinLangParser.TipoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FinLangParser#atribuicao.
    def visitAtribuicao(self, ctx:FinLangParser.AtribuicaoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FinLangParser#condicional.
    def visitCondicional(self, ctx:FinLangParser.CondicionalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FinLangParser#repeticao.
    def visitRepeticao(self, ctx:FinLangParser.RepeticaoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FinLangParser#entradaSaida.
    def visitEntradaSaida(self, ctx:FinLangParser.EntradaSaidaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FinLangParser#incremento.
    def visitIncremento(self, ctx:FinLangParser.IncrementoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FinLangParser#expr.
    def visitExpr(self, ctx:FinLangParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FinLangParser#exprLogico.
    def visitExprLogico(self, ctx:FinLangParser.ExprLogicoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FinLangParser#exprRelacional.
    def visitExprRelacional(self, ctx:FinLangParser.ExprRelacionalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FinLangParser#exprAritmetica.
    def visitExprAritmetica(self, ctx:FinLangParser.ExprAritmeticaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FinLangParser#termo.
    def visitTermo(self, ctx:FinLangParser.TermoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FinLangParser#fator.
    def visitFator(self, ctx:FinLangParser.FatorContext):
        return self.visitChildren(ctx)



del FinLangParser