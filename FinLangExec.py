from antlr4 import *
from FinLangLexer import FinLangLexer
from FinLangParser import FinLangParser
from FinLangVisitor import FinLangVisitor


class Executor(FinLangVisitor):
    def __init__(self):
        self.memoria = {}  # armazena variáveis

    # -------------------------
    # PROGRAMA
    # -------------------------
    def visitPrograma(self, ctx):
        for cmd in ctx.comando():
            self.visit(cmd)

    # -------------------------
    # COMANDOS
    # -------------------------
    def visitDeclaracao(self, ctx):
        tipo = ctx.tipo().getText()
        nome = ctx.ID().getText()
        
        if ctx.expr():  # declaração com valor
            valor = self.visit(ctx.expr())
        else:
            valor = self.valor_padrao(tipo)

        self.memoria[nome] = valor
        return valor

    def valor_padrao(self, tipo):
        return {
            "int": 0,
            "real": 0.0,
            "bool": False,
            "texto": ""
        }[tipo]

    def visitAtribuicao(self, ctx):
        nome = ctx.ID().getText()
        valor = self.visit(ctx.expr())

        self.memoria[nome] = valor
        return valor

    def visitCondicional(self, ctx):
        cond = self.visit(ctx.expr())

        if cond:
            return self.visit(ctx.comando(0))
        elif ctx.comando(1):
            return self.visit(ctx.comando(1))

    def visitRepeticao(self, ctx):
        # repete ( i = 0 até 10 ) comando
        nome = ctx.ID().getText()
        inicial = self.visit(ctx.expr(0))
        limite = self.visit(ctx.expr(1))

        self.memoria[nome] = inicial

        while self.memoria[nome] <= limite:
            self.visit(ctx.comando())
            self.memoria[nome] += 1

    def visitEntradaSaida(self, ctx):
        # escreva(expr)
        if ctx.ESCREVA():
            valor = self.visit(ctx.expr())
            print(valor)
            return None

        # leia(ID)
        if ctx.LEIA():
            nome = ctx.ID().getText()
            entrada = input(f"Entrada ({nome}): ")
            self.memoria[nome] = self.converte_input(entrada)
            return None






    def converte_input(self, txt):
        # converte automaticamente para int, real, bool, ou texto
        if txt.isdigit():
            return int(txt)
        try:
            return float(txt)
        except:
            pass
        if txt.lower() == "verdadeiro":
            return True
        if txt.lower() == "falso":
            return False
        return txt  # string pura

    def visitNUM_INT(self, ctx):
        return int(ctx.getText())

    def visitNUM_REAL(self, ctx):
        return float(ctx.getText())

    def visitSTRING(self, ctx):
        return ctx.getText().strip('"')

    def visitBOOL(self, ctx):
        return True if ctx.getText() == "verdadeiro" else False



    # -------------------------
    # EXPRESSÕES
    # -------------------------
    def visitExpr(self, ctx):
        # expr op expr
        if ctx.op:
            left = self.visit(ctx.expr(0))
            right = self.visit(ctx.expr(1))
            op = ctx.op.text

            if op == '+': return left + right
            if op == '-': return left - right
            if op == '*': return left * right
            if op == '/': return left / right

        # (expr)
        if ctx.getChildCount() == 3:
            return self.visit(ctx.expr(0))

        # valores únicos
        if ctx.NUM_INT():
            return int(ctx.NUM_INT().getText())

        if ctx.NUM_REAL():
            return float(ctx.NUM_REAL().getText())

        if ctx.BOOL():
            return ctx.BOOL().getText() == "verdadeiro"

        if ctx.STRING():
            return ctx.STRING().getText().strip('"')

        if ctx.ID():
            nome = ctx.ID().getText()
            return self.memoria[nome]

        return None


# -------------------------
# MAIN
# -------------------------
def executar_codigo(codigo):
    input_stream = InputStream(codigo)
    lexer = FinLangLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = FinLangParser(stream)
    tree = parser.programa()

    executor = Executor()
    executor.visit(tree)


if __name__ == "__main__":
    codigo = ""
    print("Digite código FinLang (vazio para executar):")
    while True:
        linha = input()
        if linha.strip() == "":
            break
        codigo += linha + "\n"

    executar_codigo(codigo)
