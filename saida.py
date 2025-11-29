print("===========================================")
print("  BEM-VINDO AO SEU CONTROLE FINANCEIRO")
print("===========================================")
print("")
print("--- INFORMAÇÕES PESSOAIS ---")
nome = "Usuario"
idade = 25
print("Nome do usuário:")
print(nome)
print("Idade:")
print(idade)
print("")
print("--- RECEITAS DO MÊS ---")
salario = 5000.00
freelance = 1500.00
investimentos = 300.00
print("Salário: R$")
print(salario)
print("Freelance: R$")
print(freelance)
print("Investimentos: R$")
print(investimentos)
receitaTotal = salario + freelance + investimentos
print("")
print("RECEITA TOTAL: R$")
print(receitaTotal)
print("")
print("--- DESPESAS FIXAS ---")
aluguel = 1200.00
condominio = 350.00
internet = 100.00
energia = 180.00
agua = 80.00
print("Aluguel: R$")
print(aluguel)
print("Condomínio: R$")
print(condominio)
print("Internet: R$")
print(internet)
print("Energia: R$")
print(energia)
print("Água: R$")
print(agua)
despesasFixas = aluguel + condominio + internet + energia + agua
print("")
print("Total Despesas Fixas: R$")
print(despesasFixas)
print("")
print("--- DESPESAS VARIÁVEIS ---")
alimentacao = 800.00
transporte = 400.00
lazer = 300.00
saude = 250.00
print("Alimentação: R$")
print(alimentacao)
print("Transporte: R$")
print(transporte)
print("Lazer: R$")
print(lazer)
print("Saúde: R$")
print(saude)
despesasVariaveis = alimentacao + transporte + lazer + saude
print("")
print("Total Despesas Variáveis: R$")
print(despesasVariaveis)
print("")
despesasTotal = despesasFixas + despesasVariaveis
saldo = receitaTotal - despesasTotal
print("===========================================")
print("            RESUMO FINANCEIRO")
print("===========================================")
print("Receita Total: R$")
print(receitaTotal)
print("Despesas Total: R$")
print(despesasTotal)
print("-------------------------------------------")
print("SALDO DO MÊS: R$")
print(saldo)
print("")
print("--- ANÁLISE FINANCEIRA ---")
if saldo > 0:
    print("[OK] Parabéns! Você teve saldo POSITIVO!")
else:
    print("[ALERTA] Atenção! Você teve saldo NEGATIVO!")
print("")
percentualDespesas = despesasTotal * 100 / receitaTotal
print("Percentual de gastos:")
print(percentualDespesas)
print("%")
print("")
print("--- PROJEÇÃO ANUAL ---")
saldoAnual = saldo * 12
print("Se manter este padrão, em 12 meses:")
print("Saldo acumulado: R$")
print(saldoAnual)
print("")
print("--- SIMULAÇÃO DE ECONOMIA ---")
metaEconomia = 10000.00
print("Meta de economia: R$")
print(metaEconomia)
print("")
print("Projeção mensal de economia:")
i = 1
while i < 5:
    print(i * saldo)
    i += 1
print("")
print("--- CATEGORIZAÇÃO DE GASTOS ---")
gastosAltos = True
if gastosAltos == True:
    print("[AVISO] Seus gastos estão elevados!")
else:
    print("[OK] Seus gastos estão controlados")
print("")
print("--- DICAS PERSONALIZADAS ---")
percentualAluguel = aluguel * 100 / receitaTotal
if percentualAluguel > 0:
    print("- Aluguel representa")
    print(percentualAluguel)
    print("% da sua renda")
print("")
percentualLazer = lazer * 100 / receitaTotal
if percentualLazer:
    print("- Lazer representa")
    print(percentualLazer)
    print("% da sua renda")
print("")
teste1 = 100
teste2 = 200
teste3 = 300
print("===========================================")
print("        RELATÓRIO FINALIZADO")
print("===========================================")
print("")
print("Dados processados com sucesso!")
print("Sistema FinLang - Controle Financeiro")
print("")