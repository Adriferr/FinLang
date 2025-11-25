from FinLangVisitor import FinLangVisitor
from FinLangParser import FinLangParser

class FinLangCompilador(FinLangVisitor):
    
    def __init__(self):
        self.codigo = []  # lista de linhas de Python

    def indent(self, texto, nivel=1):
        """Indenta blocos de código Python corretamente."""
        prefix = "    " * nivel
        return "\n".join(prefix + linha if linha.strip() != "" else "" for linha in texto.split("\n"))

    # Programa
    def visitPrograma(self, ctx: FinLangParser.ProgramaContext):
        for comando in ctx.comando():
            linha = self.visit(comando)
            if linha:
                self.codigo.append(linha)

        # retorna o código final em Python
        return "\n".join(self.codigo)

    # COMANDO
    def visitComando(self, ctx: FinLangParser.ComandoContext):
        if ctx.declaracao():
            return self.visit(ctx.declaracao())

        if ctx.atribuicao():
            return self.visit(ctx.atribuicao())

        if ctx.entradaSaida():
            return self.visit(ctx.entradaSaida())

        if ctx.incremento():
            return self.visit(ctx.incremento())

        if ctx.condicional():
            return self.visit(ctx.condicional())

        if ctx.repeticao():
            return self.visit(ctx.repeticao())

        if ctx.bloco():
            return self.visit(ctx.bloco())

        return None

    # Declaração
    def visitDeclaracao(self, ctx):
        nome = ctx.ID().getText()
        if ctx.expr():
            return f"{nome} = {self.visit(ctx.expr())}"
        return f"{nome} = 0"

    # Atribuição
    def visitAtribuicao(self, ctx):
        return f"{ctx.ID().getText()} = {self.visit(ctx.expr())}"

    # Entrada / Saída
    def visitEntradaSaida(self, ctx):
        if ctx.ESCREVA():
            return f"print({self.visit(ctx.expr())})"
        else:
            return f"{ctx.ID().getText()} = input()"

    # Incremento e Decremento
    def visitIncremento(self, ctx):
        nome = ctx.ID().getText()
        if ctx.INCREMENTO():
            return f"{nome} += 1"
        if ctx.DECREMENTO():
            return f"{nome} -= 1"

    # Bloco {...}
    def visitBloco(self, ctx: FinLangParser.BlocoContext):
        linhas = []

        for comando in ctx.comando():
            result = self.visit(comando)
            if result is not None:
                linhas.append(result)

        return "\n".join(linhas)




    # Condicional se / senao
    def visitCondicional(self, ctx: FinLangParser.CondicionalContext):
        cond = self.visit(ctx.expr())

        # corpo do if
        bloco_if = self.visit(ctx.comando(0))
        bloco_if = self.indent(bloco_if)

        codigo = f"if {cond}:\n{bloco_if}"

        # tem else?
        if ctx.SENAO():
            bloco_else = self.visit(ctx.comando(1))
            bloco_else = self.indent(bloco_else)
            codigo += f"\nelse:\n{bloco_else}"

        return codigo


    

    # Repete (init ; cond ; step) comando
    def visitRepeticao(self, ctx: FinLangParser.RepeticaoContext):
        # inicialização
        init = ctx.declaracao() or ctx.atribuicao(0)
        init_code = self.visit(init) if init else ""

        # condição
        cond = ctx.expr()
        cond_code = self.visit(cond) if cond else "True"

        # passo
        step = ctx.atribuicao(1) or ctx.incremento()
        step_code = self.visit(step) if step else ""

        # corpo do laço
        corpo = self.visit(ctx.comando())
        corpo = self.indent(corpo)  # indentação dentro do while

        # adiciona o passo ao final indentado
        if step_code:
            corpo += "\n" + self.indent(step_code)

        codigo = ""
        if init_code:
            codigo += init_code + "\n"

        codigo += f"while {cond_code}:\n{corpo}"

        return codigo

    # Expressões
    def visitExpr(self, ctx):
        return self.visit(ctx.exprLogico())

    def visitExprLogico(self, ctx):
        texto = self.visit(ctx.exprRelacional(0))
        for i in range(1, len(ctx.exprRelacional())):
            op = ctx.children[2*i - 1].getText()
            if op == "e": op = "and"
            if op == "ou": op = "or"
            texto += f" {op} {self.visit(ctx.exprRelacional(i))}"
        return texto

    def visitExprRelacional(self, ctx):
        texto = self.visit(ctx.exprAritmetica(0))
        for i in range(1, len(ctx.exprAritmetica())):
            op = ctx.children[2*i - 1].getText()
            texto += f" {op} {self.visit(ctx.exprAritmetica(i))}"
        return texto

    def visitExprAritmetica(self, ctx):
        texto = self.visit(ctx.termo(0))
        for i in range(1, len(ctx.termo())):
            op = ctx.children[2*i - 1].getText()
            texto += f" {op} {self.visit(ctx.termo(i))}"
        return texto

    def visitTermo(self, ctx):
        texto = self.visit(ctx.fator(0))
        for i in range(1, len(ctx.fator())):
            op = ctx.children[2*i - 1].getText()
            texto += f" {op} {self.visit(ctx.fator(i))}"
        return texto

    def visitFator(self, ctx):
        if ctx.expr():
            return f"({self.visit(ctx.expr())})"
        if ctx.BOOL():
            txt = ctx.BOOL().getText()
            return "True" if txt == "verdadeiro" else "False"
        if ctx.NUM_INT():
            return ctx.NUM_INT().getText()
        if ctx.NUM_REAL():
            return ctx.NUM_REAL().getText()
        if ctx.STRING():
            return ctx.STRING().getText()
        if ctx.ID():
            return ctx.ID().getText()
        return self.visitChildren(ctx)
