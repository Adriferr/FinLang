from antlr4 import *
from FinLangLexer import FinLangLexer
from FinLangParser import FinLangParser
from FinLangCompilador import FinLangCompilador

codigo = FileStream("input.fin", encoding="utf-8")

lexer = FinLangLexer(codigo)
stream = CommonTokenStream(lexer)
parser = FinLangParser(stream)

tree = parser.programa()

compilador = FinLangCompilador()
python_code = compilador.visit(tree)

print("--- PYTHON GERADO ---")
print(python_code)

# opcional: salvar em arquivo
with open("saida.py", "w", encoding="utf-8") as f:
    f.write(python_code)
