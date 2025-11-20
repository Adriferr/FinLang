from antlr4 import *
from FinLangLexer import FinLangLexer
from FinLangParser import FinLangParser

class ExecutorFinal:
    def __init__(self):
        self.memoria = {}  # armazena variáveis
        self.tipos = {}    # armazena tipos das variáveis

    def executar(self, ctx):
        """Executa o programa"""
        return self.visitPrograma(ctx)

    def visitPrograma(self, ctx):
        resultado = None
        for child in ctx.children:
            if hasattr(child, 'getRuleIndex'):
                if isinstance(child, FinLangParser.ComandoContext):
                    resultado = self.visitComando(child)
        return resultado

    def visitComando(self, ctx):
        if ctx.declaracao():
            return self.visitDeclaracao(ctx.declaracao())
        elif ctx.atribuicao():
            return self.visitAtribuicao(ctx.atribuicao())
        elif ctx.condicional():
            return self.visitCondicional(ctx.condicional())
        elif ctx.repeticao():
            return self.visitRepeticao(ctx.repeticao())
        elif ctx.entradaSaida():
            return self.visitEntradaSaida(ctx.entradaSaida())
        elif ctx.expr():
            return self.visitExpr(ctx.expr())
        return None

    def visitDeclaracao(self, ctx):
        tipo = ctx.tipo().getText()
        nome = ctx.ID().getText()
        self.tipos[nome] = tipo
        
        if ctx.expr():
            valor = self.visitExpr(ctx.expr())
        else:
            valor = {"int": 0, "real": 0.0, "bool": False, "texto": ""}[tipo]
        
        self.memoria[nome] = valor
        return valor

    def visitAtribuicao(self, ctx):
        nome = ctx.ID().getText()
        valor = self.visitExpr(ctx.expr())
        self.memoria[nome] = valor
        return valor

    def visitCondicional(self, ctx):
        condicao = self.visitExpr(ctx.expr())
        if condicao:
            return self.visitComando(ctx.comando(0))
        elif ctx.SENAO() and len(ctx.comando()) > 1:
            return self.visitComando(ctx.comando(1))
        return None

    def visitRepeticao(self, ctx):
        nome = ctx.ID().getText()
        inicial = self.visitExpr(ctx.expr(0))
        limite = self.visitExpr(ctx.expr(1))
        
        self.memoria[nome] = inicial
        resultado = None
        while self.memoria[nome] <= limite:
            resultado = self.visitComando(ctx.comando())
            self.memoria[nome] += 1
        return resultado

    def visitEntradaSaida(self, ctx):
        if ctx.ESCREVA():
            valor = self.visitExpr(ctx.expr())
            print(valor)
            return valor
        elif ctx.LEIA():
            nome = ctx.ID().getText()
            entrada = input(f"Entrada ({nome}): ")
            
            if nome in self.tipos:
                tipo = self.tipos[nome]
                if tipo == "int":
                    self.memoria[nome] = int(entrada)
                elif tipo == "real":
                    self.memoria[nome] = float(entrada)
                elif tipo == "bool":
                    self.memoria[nome] = entrada.lower() in ['verdadeiro', 'true', '1']
                else:
                    self.memoria[nome] = entrada
            else:
                self.memoria[nome] = entrada
            return self.memoria[nome]
        return None

    def visitExpr(self, ctx):
        if ctx.NUM_INT():
            return int(ctx.NUM_INT().getText())
        elif ctx.NUM_REAL():
            return float(ctx.NUM_REAL().getText())
        elif ctx.BOOL():
            return ctx.BOOL().getText() == "verdadeiro"
        elif ctx.STRING():
            return ctx.STRING().getText().strip('"')
        elif ctx.ID():
            nome = ctx.ID().getText()
            if nome in self.memoria:
                return self.memoria[nome]
            return 0
        elif ctx.getChildCount() == 3 and ctx.getChild(0).getText() == '(':
            return self.visitExpr(ctx.expr(0))
        elif ctx.op:
            left = self.visitExpr(ctx.expr(0))
            right = self.visitExpr(ctx.expr(1))
            op = ctx.op.text
            
            if op == '+': return left + right
            elif op == '-': return left - right
            elif op == '*': return left * right
            elif op == '/': return left / right if right != 0 else 0
        
        return 0

def executar(codigo):
    """Executa código FinLang a partir de uma string"""
    input_stream = InputStream(codigo)
    lexer = FinLangLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = FinLangParser(stream)
    tree = parser.programa()
    
    executor = ExecutorFinal()
    executor.executar(tree)

def executar_arquivo(caminho_arquivo):
    """Executa um arquivo .fin"""
    try:
        with open(caminho_arquivo, 'r', encoding='utf-8') as f:
            codigo = f.read()
        
        print("="*60)
        print(f"EXECUTANDO: {caminho_arquivo}")
        print("="*60)
        print()
        
        executar(codigo)
        
        print()
        print("="*60)
        print("EXECUÇÃO CONCLUÍDA COM SUCESSO!")
        print("="*60)
        
    except FileNotFoundError:
        print(f"❌ Erro: Arquivo '{caminho_arquivo}' não encontrado")
    except Exception as e:
        print(f"❌ Erro durante a execução: {e}")
        import traceback
        traceback.print_exc()

# Permite execução via linha de comando ou importação
if __name__ == "__main__":
    import sys
    
    if len(sys.argv) > 1:
        # Executa arquivo passado como argumento
        executar_arquivo(sys.argv[1])
    else:
        # Executa teste padrão
        print("Uso: python interpretador.py <arquivo.fin>")
        print("\nOu importe: from interpretador import executar")
        print("\nExecutando teste padrão...")
        print("="*60)
        
        executar("""
int x = 10
escreva(x)
escreva(x + 5)
repete(i = 1 até 3) escreva(i)
""")
