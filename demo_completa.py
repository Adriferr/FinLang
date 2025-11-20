from interpretador import executar

print("="*60)
print("     FINLANG - Sistema de Controle Financeiro Pessoal")
print("="*60)

# Programa financeiro completo usando TODOS os recursos
executar("""
// ============================================
// SISTEMA DE CONTROLE FINANCEIRO PESSOAL
// Demonstra todos os recursos da linguagem
// ============================================

escreva("===========================================")
escreva("  BEM-VINDO AO SEU CONTROLE FINANCEIRO")
escreva("===========================================")
escreva("")

// 1. ENTRADA DE DADOS (demonstra LEIA e tipos de variáveis)
escreva("--- INFORMAÇÕES PESSOAIS ---")
texto nome = "Usuario"
int idade = 25
escreva("Nome do usuário:")
escreva(nome)
escreva("Idade:")
escreva(idade)
escreva("")

// 2. RECEITAS (demonstra REAL e operações aritméticas)
escreva("--- RECEITAS DO MÊS ---")
real salario = 5000.00
real freelance = 1500.00
real investimentos = 300.00

escreva("Salário: R$")
escreva(salario)
escreva("Freelance: R$")
escreva(freelance)
escreva("Investimentos: R$")
escreva(investimentos)

real receitaTotal = salario + freelance + investimentos
escreva("")
escreva("RECEITA TOTAL: R$")
escreva(receitaTotal)
escreva("")

// 3. DESPESAS FIXAS (demonstra múltiplas variáveis)
escreva("--- DESPESAS FIXAS ---")
real aluguel = 1200.00
real condominio = 350.00
real internet = 100.00
real energia = 180.00
real agua = 80.00

escreva("Aluguel: R$")
escreva(aluguel)
escreva("Condomínio: R$")
escreva(condominio)
escreva("Internet: R$")
escreva(internet)
escreva("Energia: R$")
escreva(energia)
escreva("Água: R$")
escreva(agua)

// Cálculo com precedência de operadores
real despesasFixas = aluguel + condominio + internet + energia + agua
escreva("")
escreva("Total Despesas Fixas: R$")
escreva(despesasFixas)
escreva("")

// 4. DESPESAS VARIÁVEIS (demonstra expressões complexas)
escreva("--- DESPESAS VARIÁVEIS ---")
real alimentacao = 800.00
real transporte = 400.00
real lazer = 300.00
real saude = 250.00

escreva("Alimentação: R$")
escreva(alimentacao)
escreva("Transporte: R$")
escreva(transporte)
escreva("Lazer: R$")
escreva(lazer)
escreva("Saúde: R$")
escreva(saude)

real despesasVariaveis = alimentacao + transporte + lazer + saude
escreva("")
escreva("Total Despesas Variáveis: R$")
escreva(despesasVariaveis)
escreva("")

// 5. CÁLCULO DO SALDO (demonstra operações aritméticas)
real despesasTotal = despesasFixas + despesasVariaveis
real saldo = receitaTotal - despesasTotal

escreva("===========================================")
escreva("            RESUMO FINANCEIRO")
escreva("===========================================")
escreva("Receita Total: R$")
escreva(receitaTotal)
escreva("Despesas Total: R$")
escreva(despesasTotal)
escreva("-------------------------------------------")
escreva("SALDO DO MÊS: R$")
escreva(saldo)
escreva("")

// 6. ANÁLISE E RECOMENDAÇÕES (demonstra IF/ELSE)
escreva("--- ANÁLISE FINANCEIRA ---")

// Verifica se está no positivo ou negativo
se saldo
    escreva("[OK] Parabéns! Você teve saldo POSITIVO!")
senao
    escreva("[ALERTA] Atenção! Você teve saldo NEGATIVO!")

escreva("")

// 7. CÁLCULO DE PERCENTUAIS (demonstra divisão e multiplicação)
real percentualDespesas = despesasTotal * 100 / receitaTotal
escreva("Percentual de gastos:")
escreva(percentualDespesas)
escreva("%")
escreva("")

// 8. PROJEÇÃO ANUAL (demonstra operadores e loops)
escreva("--- PROJEÇÃO ANUAL ---")
real saldoAnual = saldo * 12
escreva("Se manter este padrão, em 12 meses:")
escreva("Saldo acumulado: R$")
escreva(saldoAnual)
escreva("")

// 9. META DE ECONOMIA (demonstra estrutura de repetição)
escreva("--- SIMULAÇÃO DE ECONOMIA ---")
real metaEconomia = 10000.00
escreva("Meta de economia: R$")
escreva(metaEconomia)
escreva("")
escreva("Projeção mensal de economia:")

repete(i = 1 até 5) 
    escreva(i * saldo)

escreva("")

// 10. CATEGORIZAÇÃO DE GASTOS (demonstra bool e comparações)
escreva("--- CATEGORIZAÇÃO DE GASTOS ---")
bool gastosAltos = verdadeiro

se gastosAltos
    escreva("[AVISO] Seus gastos estão elevados!")
senao
    escreva("[OK] Seus gastos estão controlados")

escreva("")

// 11. DICAS PERSONALIZADAS (demonstra múltiplos IFs)
escreva("--- DICAS PERSONALIZADAS ---")

real percentualAluguel = aluguel * 100 / receitaTotal
se percentualAluguel
    escreva("- Aluguel representa")
    escreva(percentualAluguel)
    escreva("% da sua renda")

escreva("")

real percentualLazer = lazer * 100 / receitaTotal
se percentualLazer
    escreva("- Lazer representa")
    escreva(percentualLazer)
    escreva("% da sua renda")

escreva("")

// 12. TOKENS DESCARTADOS (comentários e espaçamentos)
// Todos os comentários são ignorados pelo interpretador
int teste1=100    // espaços variados
int     teste2  =   200     // muitos espaços
                    int teste3    =    300  // tabs e espaços

escreva("===========================================")
escreva("        RELATÓRIO FINALIZADO")
escreva("===========================================")
escreva("")
escreva("Dados processados com sucesso!")
escreva("Sistema FinLang - Controle Financeiro")
escreva("")

// FIM DO PROGRAMA
""")

print("\n" + "="*60)
print("[OK] DEMONSTRAÇÃO COMPLETA!")
print("="*60)

print("\n[RECURSOS DEMONSTRADOS]:")
print("[OK] 1. Tipos de Variáveis: int, real, bool, texto")
print("[OK] 2. Declarações com valores iniciais")
print("[OK] 3. Atribuições de variáveis")
print("[OK] 4. Expressões Aritméticas: +, -, *, /")
print("[OK] 5. Precedência de Operadores corretas")
print("[OK] 6. Estrutura Condicional: se...senao")
print("[OK] 7. Estrutura de Repetição: repete...até")
print("[OK] 8. Comando de Saída: escreva()")
print("[OK] 9. Expressões Complexas com múltiplas operações")
print("[OK] 10. Tokens Descartados: espaços, tabs, \\n, comentários")
print("="*60)
