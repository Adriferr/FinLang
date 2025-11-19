from FinLangVisitor import FinLangVisitor

class Interpretador(FinLangVisitor):

    def visitPrograma(self, ctx):
        return self.visitChildren(ctx)

    def visitEntradaSaida(self, ctx):
        # Se for escreva
        if ctx.ESCREVA():
            valor = self.visit(ctx.expr())
            print(valor)
            return None

        # Se for leia
        if ctx.LEIA():
            nome = ctx.ID().getText()
            entrada = input(f"Entrada ({nome}): ")
            return None

    def visitExpr(self, ctx):
        if ctx.NUM_INT():
            return int(ctx.NUM_INT().getText())

        return self.visitChildren(ctx)
