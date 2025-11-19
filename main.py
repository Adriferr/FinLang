from antlr4 import *
from FinLangLexer import FinLangLexer
from FinLangParser import FinLangParser
from interpretador import Interpretador

def executar(codigo):
    input_stream = InputStream(codigo)
    lexer = FinLangLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = FinLangParser(stream)

    tree = parser.programa()

    # 👉 Debug para ver como o parser interpretou sua entrada
    print("Árvore gerada:")
    print(tree.toStringTree(recog=parser))

    visitante = Interpretador()
    visitante.visit(tree)

executar("escreva(10)")
