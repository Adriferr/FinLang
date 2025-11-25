# interpretador.py
from antlr4 import *
from FinLangLexer import FinLangLexer
from FinLangParser import FinLangParser

class ExecutorFinal:
    def __init__(self):
        self.memoria = {}  # nome -> valor
        self.tipos = {}    # nome -> tipo textual ('inteiro','real','bool','texto')

    # entry point: recebe ctx.programa()
    def executar(self, ctx):
        return self.visitPrograma(ctx)

    # Programa: lista de comandos
    def visitPrograma(self, ctx: FinLangParser.ProgramaContext):
        resultado = None
        for cmd in ctx.comando():
            resultado = self.visitComando(cmd)
        return resultado

    # Dispatch para cada comando possível
    def visitComando(self, ctx: FinLangParser.ComandoContext):
        if ctx.declaracao():
            return self.visitDeclaracao(ctx.declaracao())
        if ctx.atribuicao():
            return self.visitAtribuicao(ctx.atribuicao())
        if ctx.incremento():
            return self.visitIncremento(ctx.incremento())
        if ctx.entradaSaida():
            return self.visitEntradaSaida(ctx.entradaSaida())
        if ctx.condicional():
            return self.visitCondicional(ctx.condicional())
        if ctx.repeticao():
            return self.visitRepeticao(ctx.repeticao())
        if ctx.bloco():
            return self.visitBloco(ctx.bloco())
        return None

    # Bloco: { comando* }
    def visitBloco(self, ctx: FinLangParser.BlocoContext):
        resultado = None
        for cmd in ctx.comando():
            resultado = self.visitComando(cmd)
        return resultado

    # Declaração: tipo ID = expr
    def visitDeclaracao(self, ctx: FinLangParser.DeclaracaoContext):
        tipo_txt = ctx.tipo().getText()  # 'inteiro','real','bool','texto'
        nome = ctx.ID().getText()
        valor = self.visitExpr(ctx.expr())
        # salvar tipo e valor
        self.tipos[nome] = tipo_txt
        self.memoria[nome] = self._convert_value_por_tipo(valor, tipo_txt)
        return self.memoria[nome]

    # Atribuição: ID = expr
    def visitAtribuicao(self, ctx: FinLangParser.AtribuicaoContext):
        nome = ctx.ID().getText()
        valor = self.visitExpr(ctx.expr())
        if nome in self.tipos:
            valor = self._convert_value_por_tipo(valor, self.tipos[nome])
        self.memoria[nome] = valor
        return valor

    # Incremento: ++ID | --ID | ID++ | ID--
    def visitIncremento(self, ctx: FinLangParser.IncrementoContext):
        txt = ctx.getText()
        # remover espaços só por segurança
        txt = txt.strip()
        if txt.startswith("++"):
            nome = txt[2:]
            self._ensure_var_exists(nome)
            self.memoria[nome] = self._numeric_add(self.memoria[nome], 1)
            return self.memoria[nome]
        if txt.startswith("--"):
            nome = txt[2:]
            self._ensure_var_exists(nome)
            self.memoria[nome] = self._numeric_add(self.memoria[nome], -1)
            return self.memoria[nome]
        if txt.endswith("++"):
            nome = txt[:-2]
            self._ensure_var_exists(nome)
            val = self.memoria[nome]
            self.memoria[nome] = self._numeric_add(val, 1)
            return val  # post-increment returns old value if needed
        if txt.endswith("--"):
            nome = txt[:-2]
            self._ensure_var_exists(nome)
            val = self.memoria[nome]
            self.memoria[nome] = self._numeric_add(val, -1)
            return val

        return None

    # Condicional: se (expr) comando (senao comando)?
    def visitCondicional(self, ctx: FinLangParser.CondicionalContext):
        cond_val = self.visitExpr(ctx.expr())
        if cond_val:
            return self.visitComando(ctx.comando(0))
        # existe senao?
        if ctx.SENAO() and len(ctx.comando()) > 1:
            return self.visitComando(ctx.comando(1))
        return None

    # Repetição: repete '(' (declaracao | atribuicao) ';' expr ';' (atribuicao | incremento) ')' comando
    def visitRepeticao(self, ctx: FinLangParser.RepeticaoContext):
        # detectar inicialização (declaracao ou atribuicao)
        init_val = None
        init_decl = ctx.declaracao()
        atr_list = ctx.atribuicao()  # pode ser lista
        init_ctx = None
        if init_decl:
            init_ctx = init_decl
        elif atr_list:
            # se houver ao menos uma atribuicao, a primeira aparece como inicialização
            if isinstance(atr_list, list) and len(atr_list) >= 1:
                init_ctx = atr_list[0]
            else:
                init_ctx = atr_list  # caso seja único

        if init_ctx is not None:
            # executar inicialização
            if isinstance(init_ctx, FinLangParser.DeclaracaoContext):
                self.visitDeclaracao(init_ctx)
            else:
                self.visitAtribuicao(init_ctx)

        # condição (expr no meio)
        expr_list = ctx.expr()
        if expr_list:
            # pegar a primeira expressão presente
            cond_ctx = expr_list[0]
        else:
            # se por algum motivo não houver, tratar como True
            cond_ctx = None

        # detectar incremento (pode ser incremento ou atribuicao)
        inc_ctx = None
        inc_nodes = ctx.incremento()
        # ctx.atribuicao() pode ter duas entradas: a primeira foi init, a segunda pode ser incremento
        if inc_nodes:
            # incremento presente
            if isinstance(inc_nodes, list):
                inc_ctx = inc_nodes[0]
            else:
                inc_ctx = inc_nodes
        else:
            # verificar se há segunda atribuicao
            if atr_list:
                if isinstance(atr_list, list) and len(atr_list) >= 2:
                    inc_ctx = atr_list[-1]
                # else: apenas a inicialização existia;

        # corpo do loop: último comando do ctx.comando()
        body_cmds = ctx.comando()
        if body_cmds:
            body_ctx = body_cmds[-1]
        else:
            body_ctx = None

        resultado = None

        # função auxiliar para avaliar condição
        def cond_true():
            if cond_ctx is None:
                return True
            return bool(self.visitExpr(cond_ctx))

        # executar loop
        while cond_true():
            # executar corpo
            if body_ctx:
                resultado = self.visitComando(body_ctx)
            # executar incremento
            if inc_ctx:
                # inc_ctx pode ser atribuicao ou incremento
                # checar tipo por texto
                if hasattr(inc_ctx, 'getText') and inc_ctx.getText().strip().startswith(('++','--')) or hasattr(inc_ctx, 'INCREMENTO'):
                    # trata como incremento via visitIncremento
                    self.visitIncremento(inc_ctx)
                else:
                    # tratá-lo como atribuicao
                    # se for do tipo FinLangParser.AtribuicaoContext, chamar visitAtribuicao
                    # usamos isinstance check via duck-typing: se tiver ID() e expr()
                    if hasattr(inc_ctx, 'ID') and hasattr(inc_ctx, 'expr'):
                        try:
                            self.visitAtribuicao(inc_ctx)
                        except Exception:
                            self.visitComando(inc_ctx)
                    else:
                        try:
                            self.visitIncremento(inc_ctx)
                        except Exception:
                            pass

            # evitar loops infinitos sem progresso
            if not cond_true():
                break

        return resultado

    # Entrada / Saída
    def visitEntradaSaida(self, ctx: FinLangParser.EntradaSaidaContext):
        if ctx.ESCREVA():
            val = self.visitExpr(ctx.expr())
            print(val)
            return val
        if ctx.LEIA():
            nome = ctx.ID().getText()
            entrada = input(f"Entrada ({nome}): ")
            if nome in self.tipos:
                tipo = self.tipos[nome]
                if tipo == "inteiro":
                    self.memoria[nome] = int(entrada)
                elif tipo == "real":
                    self.memoria[nome] = float(entrada)
                elif tipo == "bool":
                    self.memoria[nome] = entrada.lower() in ('verdadeiro','true','1')
                else:
                    self.memoria[nome] = entrada
            else:
                self.memoria[nome] = entrada
            return self.memoria[nome]
        return None

    # ---------------------------
    # EXPRESSÕES (avaliadores)
    # ---------------------------

    def visitExpr(self, ctx: FinLangParser.ExprContext):
        # Expr -> exprLogico
        return self.visitExprLogico(ctx.exprLogico())

    def visitExprLogico(self, ctx: FinLangParser.ExprLogicoContext):
        # exprRelacional ( (AND | OR) exprRelacional )*
        rels = ctx.exprRelacional()
        # coletar ops varrendo children
        ops = []
        for i in range(ctx.getChildCount()):
            ch = ctx.getChild(i)
            txt = ch.getText()
            if txt == 'e' or txt == 'ou':
                ops.append(txt)
        # avaliação left-to-right com short-circuit
        value = self.visitExprRelacional(rels[0])
        for i, op in enumerate(ops):
            right = self.visitExprRelacional(rels[i+1])
            if op == 'e':
                value = bool(value and right)
            else:
                value = bool(value or right)
        return value

    def visitExprRelacional(self, ctx: FinLangParser.ExprRelacionalContext):
        # exprAritmetica ( (MENOR | MAIOR | MENOR_IGUAL | MAIOR_IGUAL | IGUAL | DIF) exprAritmetica )*
        terms = ctx.exprAritmetica()
        # coletar ops varrendo children
        ops = []
        for i in range(ctx.getChildCount()):
            t = ctx.getChild(i).getText()
            if t in ('<','>','<=','>=','==','!='):
                ops.append(t)
        if not ops:
            return self.visitExprAritmetica(terms[0])
        # implementar comparação encadeada como a semântica usual (a < b < c) -> (a<b and b<c)
        vals = [self.visitExprAritmetica(t) for t in terms]
        result = True
        for i, op in enumerate(ops):
            a = vals[i]
            b = vals[i+1]
            if op == '<':
                cmp = (a < b)
            elif op == '>':
                cmp = (a > b)
            elif op == '<=':
                cmp = (a <= b)
            elif op == '>=':
                cmp = (a >= b)
            elif op == '==':
                cmp = (a == b)
            elif op == '!=':
                cmp = (a != b)
            else:
                cmp = False
            result = result and cmp
            if not result:
                break
        return result

    def visitExprAritmetica(self, ctx: FinLangParser.ExprAritmeticaContext):
        # termo ( (MAIS | MENOS) termo )*
        termos = ctx.termo()
        ops = []
        for i in range(ctx.getChildCount()):
            t = ctx.getChild(i).getText()
            if t in ('+','-'):
                ops.append(t)
        # sem operador: apenas primeiro termo
        if not ops:
            return self.visitTermo(termos[0])
        # calcular left-to-right
        value = self.visitTermo(termos[0])
        for i, op in enumerate(ops):
            right = self.visitTermo(termos[i+1])
            if op == '+':
                value = self._plus(value, right)
            else:
                value = self._minus(value, right)
        return value

    def visitTermo(self, ctx: FinLangParser.TermoContext):
        # fator ( (MULT | DIV) fator )*
        fatores = ctx.fator()
        ops = []
        for i in range(ctx.getChildCount()):
            t = ctx.getChild(i).getText()
            if t in ('*','/'):
                ops.append(t)
        if not ops:
            return self.visitFator(fatores[0])
        value = self.visitFator(fatores[0])
        for i, op in enumerate(ops):
            right = self.visitFator(fatores[i+1])
            if op == '*':
                value = value * right
            else:
                # proteção contra divisão por zero (retorna 0)
                try:
                    value = value / right
                except Exception:
                    value = 0
        return value

    def visitFator(self, ctx: FinLangParser.FatorContext):
        # '(' expr ')' | BOOL | NUM_REAL | NUM_INT | STRING | ID
        if ctx.getChildCount() == 3 and ctx.getChild(0).getText() == '(':
            return self.visitExpr(ctx.expr())
        if ctx.BOOL():
            txt = ctx.BOOL().getText()
            return txt == 'verdadeiro'
        if ctx.NUM_REAL():
            return float(ctx.NUM_REAL().getText())
        if ctx.NUM_INT():
            return int(ctx.NUM_INT().getText())
        if ctx.STRING():
            s = ctx.STRING().getText()
            # remover aspas externas
            if len(s) >= 2 and s[0] == '"' and s[-1] == '"':
                return s[1:-1]
            return s
        if ctx.ID():
            nome = ctx.ID().getText()
            if nome in self.memoria:
                return self.memoria[nome]
            # variável não inicializada -> 0 por padrão
            return 0
        return None

    # ---------------------------
    # UTILITÁRIOS
    # ---------------------------
    def _convert_value_por_tipo(self, value, tipo_txt):
        if tipo_txt == 'inteiro':
            try:
                return int(value)
            except Exception:
                return 0
        if tipo_txt == 'real':
            try:
                return float(value)
            except Exception:
                return 0.0
        if tipo_txt == 'bool':
            return bool(value)
        if tipo_txt == 'texto':
            return str(value)
        return value

    def _ensure_var_exists(self, nome):
        if nome not in self.memoria:
            # inicializar com 0 (inteiro) por padrão se desconhecido
            self.memoria[nome] = 0

    def _numeric_add(self, val, delta):
        try:
            return val + delta
        except Exception:
            # tentar converter para número
            try:
                return int(val) + delta
            except Exception:
                try:
                    return float(val) + delta
                except Exception:
                    return val

    def _plus(self, a, b):
        if isinstance(a, str) or isinstance(b, str):
            return str(a) + str(b)
        try:
            return a + b
        except Exception:
            try:
                return int(a) + int(b)
            except:
                try:
                    return float(a) + float(b)
                except:
                    return 0

    def _minus(self, a, b):
        try:
            return a - b
        except Exception:
            try:
                return int(a) - int(b)
            except:
                try:
                    return float(a) - float(b)
                except:
                    return 0

# helpers para executar a partir de texto/arquivo
def executar(codigo):
    input_stream = InputStream(codigo)
    lexer = FinLangLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = FinLangParser(stream)
    tree = parser.programa()
    executor = ExecutorFinal()
    executor.executar(tree)

def executar_arquivo(caminho_arquivo):
    try:
        with open(caminho_arquivo, 'r', encoding='utf-8') as f:
            codigo = f.read()
        print("="*60)
        print(f"EXECUTANDO: {caminho_arquivo}")
        print("="*60)
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

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        executar_arquivo(sys.argv[1])
    else:
        print("Teste rápido do interpretador:")
        sample = """
inteiro x = 2;
escreva(x);
escreva(x + 3 * (2 + 1));
repete(inteiro i = 0; i < 3; i++) {
    escreva(i);
}
"""
        executar(sample)
