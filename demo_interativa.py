from interpretador import executar

print("="*60)
print("  FINLANG - Controle Financeiro Pessoal INTERATIVO")
print("="*60)
print("\nEste programa vai pedir suas informações financeiras")
print("e calcular seu saldo mensal automaticamente.\n")

# Programa financeiro INTERATIVO que usa LEIA
executar("""
// ============================================
// SISTEMA FINANCEIRO INTERATIVO
// Demonstra o comando LEIA (entrada de dados)
// ============================================

escreva("===========================================")
escreva("  CONTROLE FINANCEIRO PESSOAL")
escreva("===========================================")
escreva("")

// COLETA DE DADOS DO USUÁRIO
escreva("--- DADOS PESSOAIS ---")
escreva("Digite seu nome:")
texto nome = ""
leia(nome)

escreva("Digite sua idade:")
int idade = 0
leia(idade)

escreva("")
escreva("Olá,")
escreva(nome)
escreva("Vamos calcular suas finanças!")
escreva("")

// RECEITAS
escreva("--- RECEITAS DO MÊS ---")
escreva("Digite seu salário:")
real salario = 0.0
leia(salario)

escreva("Digite renda extra (freelance, etc):")
real rendaExtra = 0.0
leia(rendaExtra)

real receitaTotal = salario + rendaExtra
escreva("")
escreva("Receita Total: R$")
escreva(receitaTotal)
escreva("")

// DESPESAS
escreva("--- DESPESAS DO MÊS ---")
escreva("Digite o valor do aluguel/moradia:")
real aluguel = 0.0
leia(aluguel)

escreva("Digite gastos com alimentação:")
real alimentacao = 0.0
leia(alimentacao)

escreva("Digite gastos com transporte:")
real transporte = 0.0
leia(transporte)

escreva("Digite outras despesas:")
real outras = 0.0
leia(outras)

real despesasTotal = aluguel + alimentacao + transporte + outras
escreva("")
escreva("Despesas Total: R$")
escreva(despesasTotal)
escreva("")

// CÁLCULO DO SALDO
real saldo = receitaTotal - despesasTotal

escreva("===========================================")
escreva("         RESUMO FINANCEIRO")
escreva("===========================================")
escreva("Nome:")
escreva(nome)
escreva("Idade:")
escreva(idade)
escreva("")
escreva("Receitas: R$")
escreva(receitaTotal)
escreva("Despesas: R$")
escreva(despesasTotal)
escreva("-------------------------------------------")
escreva("SALDO: R$")
escreva(saldo)
escreva("")

// ANÁLISE
escreva("--- ANÁLISE ---")
se saldo
    escreva("[OK] Você teve saldo POSITIVO! Continue assim!")
    
int zero = 0
se zero
    escreva("Não executado")
senao
    escreva("[INFO] Controle suas despesas!")

escreva("")

// PERCENTUAIS
real percentualGasto = despesasTotal * 100 / receitaTotal
escreva("Você gastou")
escreva(percentualGasto)
escreva("% da sua renda")
escreva("")

// PROJEÇÃO
escreva("--- PROJEÇÃO ---")
escreva("Se manter este padrão:")
real saldoAnual = saldo * 12
escreva("Em 12 meses você terá: R$")
escreva(saldoAnual)
escreva("")

escreva("===========================================")
escreva("Obrigado por usar o FinLang!")
escreva("===========================================")
""")
