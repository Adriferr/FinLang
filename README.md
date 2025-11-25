# FinLang - Linguagem de Programação Financeira

## 📋 Sobre o Projeto

FinLang é uma linguagem de programação simples desenvolvida usando ANTLR4, criada para demonstrar os conceitos fundamentais de compiladores e interpretadores.

## ✅ Requisitos Implementados

### 1. Tipos de Variáveis (4 tipos)
- `inteiro` - Números inteiros
- `real` - Números reais (ponto flutuante)
- `bool` - Booleanos (verdadeiro/falso)
- `texto` - Strings

### 2. Bloco de código
- { comando }

### 3. Estrutura Condicional
- `se ... senao` (equivalente a if...else)

### 4. Estrutura de Repetição
- `repete(inicialização; condição; iteração)` (equivalente a for)

### 5. Expressões Aritméticas
- Operadores: `+`, `-`, `*`, `/`
- **Precedência correta** implementada na gramática

### 6. Atribuições
- Comando de atribuição com `=`
- Verificação básica de escopo

### 7. Incremento e Decremento
- ++ID (++i)
- --ID  (--i)
- ID++ (i++)
- ID-- (i--)

### 8. Entrada e Saída
- `escreva(expr)` - Imprime valores na tela
- `leia(variavel)` - Lê entrada do usuário

### 9. Tokens Descartados
- Espaços em branco
- Tabs (`\t`)
- Quebras de linha (`\n`)
- Comentários (`//`)

## 🚀 Como Usar

### 1. Executar a Demonstração Completa (Automática)
Demonstra todos os requisitos com valores pré-definidos, compila input.fin e gera arquivo.py
```bash
python main.py
```

### 2. Executar a Demonstração Interativa (com entrada de dados)
Sistema financeiro que pede dados ao usuário via terminal:
```bash
python demo_interativa.py
```
Este programa demonstra o comando `leia()` pedindo:
- Nome e idade
- Salário e renda extra
- Despesas (aluguel, alimentação, transporte, etc)
- Calcula e mostra o saldo final


### 3. Usar como Biblioteca Python
```python
from interpretador import executar

# Executar código diretamente pelo interpretador
executar("""
inteiro x = 10;
inteiro y = 20;
escreva(x + y);
""")

# Ou executar um arquivo pelo compilador
from FinLangCompilador import FinLangCompilador
codigo = FileStream("input.fin", encoding="utf-8")
```

## 📝 Sintaxe da Linguagem

### Declaração de Variáveis
```finlang
inteiro idade = 25;
real salario = 5500.50;
bool ativo = verdadeiro;
texto nome = "Maria Silva";
```

### Atribuições
```finlang
idade = 26;
salario = 6000.00;
```

### Expressões Aritméticas
```finlang
inteiro resultado = 2 + 3 * 4;  // Resultado: 14 (precedência correta)
inteiro outro = (2 + 3) * 4;     // Resultado: 20 (parênteses)
```

### Estrutura Condicional
```finlang
se (condicao){
    escreva("Verdadeiro");
}
senao{
      escreva("Falso");
}
```

### Estrutura de Repetição
```finlang
repete(i = 1; i<10; i++){
    escreva(i);
}
```

### Entrada e Saída
```finlang
escreva("Digite seu nome:");
leia(nome);
escreva(nome);

// O comando leia() converte automaticamente baseado no tipo da variável
inteiro idade = 0;
escreva("Digite sua idade:");
leia(idade);
escreva(idade);

real salario = 0.0;
escreva("Digite seu salário:");
leia(salario);
escreva(salario);
```

**Nota**: O comando `leia()` exige que a variável já tenha sido declarada previamente.

### Comentários
```finlang
// Este é um comentário de linha
inteiro x = 10;  // Comentário no final da linha
```

## 📂 Estrutura do Projeto

```
A3 FinLang/
│
├── FinLang.g4              # Gramática ANTLR4
├── FinLangLexer.py         # Lexer gerado pelo ANTLR
├── FinLangListener.py      # Listener gerado pelo ANTLR
├── FinLangParser.py        # Parser gerado pelo ANTLR
├── FinLangVisitor.py       # Visitor gerado pelo ANTLR
│
├── FinLangCompilador.py    # ⭐ Compilador da linguagem
├── interpretador.py        # ⭐ Interpretador da linguagem
├── demo_interativa.py      # ⭐ Demonstração interativa da linguagem
├── input.fin               # ⭐ Arquivo contendo a linguagem criada
├── main.py                 # ⭐ Demonstração de todos os requisitos e geração do arquivo.py
│
└── README.md               # Este arquivo
```

### Arquivos Principais

- **`interpretador.py`**: Motor de execução da linguagem FinLang
  - Classe `ExecutorFinal`: Implementa o interpretador
  - Função `executar(codigo)`: Executa código FinLang

- **`FinLangCompilador.py`**: Compilador da linguagem FinLang
  - Classe `FinLangCompilador`: Implementa o compilador
  - Função `visitPrograma`: Passa pela árvore sintática da gramática FinLang
  
- **`main.py`**: Script de demonstração que valida todos os requisitos e gera "saida.py"

- **`input.fin`**: Programa exemplo que demonstra todos os recursos da linguagem

## 🎯 Exemplos Práticos

### Exemplo 1: Cálculo de Área
```finlang
inteiro base = 5;
inteiro altura = 4;
inteiro area = base * altura / 2;
escreva("Área do triângulo:");
escreva(area);
```

### Exemplo 2: Loop com Tabuada
```finlang
escreva("Tabuada do 5:");
repete(i = 1; i<10; i++){
    escreva(5 * i);
}
```

### Exemplo 3: Cálculo de Desconto
```finlang
real preco = 100.00;
real desconto = 15.00;
real precoFinal = preco - preco * desconto / 100;
escreva("Preço com desconto:");
escreva(precoFinal);
```

## 🔍 Análise Técnica

### Gramática ANTLR4
A gramática define:
- **Lexer**: Tokens (palavras-chave, identificadores, números, strings)
- **Parser**: Regras sintáticas (programa, comandos, expressões)
- **Precedência de Operadores**: Multiplicação/divisão antes de adição/subtração

### Interpretador
O interpretador implementa o padrão Visitor para:
- Percorrer a árvore sintática abstrata (AST)
- Executar comandos
- Gerenciar memória (variáveis)
- Controlar fluxo de execução

### Compilador
O compilador importa o FinLangVisitor para:
- Carregar e iniciar o lexer e o parser
- Executar o Visitor para converter FinLang para Python
- Gerenciar erros de compilação
- Salva a conversão em um arquivo.py

### Características
- ✅ Tipagem declarativa
- ✅ Escopo básico de variáveis
- ✅ Avaliação de expressões com precedência
- ✅ Estruturas de controle (if/else, for)
- ✅ I/O básico

## 🧪 Teste Completo

Execute `main.py` para ver uma demonstração de todos os requisitos:

```bash
python main.py
```

Saída esperada:
- Demonstração de todos os 4 tipos de variáveis
- Exemplos de atribuições
- Expressões aritméticas com precedência
- Estruturas condicionais funcionando
- Loops de repetição
- Entrada e saída
- Comentários sendo ignorados
- Arquivo "saida.py" gerado

## 📊 Checklist de Conformidade

| Requisito | Status | Descrição |
|-----------|--------|-----------|
| Tipos de Variáveis | ✅ | 4 tipos (inteiro, real, bool, texto) |
| Estrutura Condicional | ✅ | se...senao (if...else) |
| Estrutura de Repetição | ✅ | repete(inic; cond; incr)... (for) |
| Expressões Aritméticas | ✅ | +, -, *, / com precedência |
| Atribuições | ✅ | Comando = implementado |
| Entrada e Saída | ✅ | escreva e leia |
| Tokens Descartados | ✅ | Espaços, tabs, \n, comentários |

## 👨‍💻 Tecnologias Utilizadas

- **Python 3.x**
- **ANTLR 4.13.2**
- **Padrão Visitor** para interpretação e compilação

## 📖 Referências

- [ANTLR Official Documentation](https://www.antlr.org/)
- [The Definitive ANTLR 4 Reference](https://pragprog.com/titles/tpantlr2/the-definitive-antlr-4-reference/)

---

**Desenvolvido como projeto acadêmico de Compiladores**
