# Valores
faturamento = {
    "SP": 67836.43,
    "RJ": 36678.66,
    "MG": 29229.88,
    "ES": 27165.48,
    "OU": 19849.53
}
# Soma o valor total
total = sum(faturamento.values())

# Define os valores por estado
valor_SP = faturamento["SP"]
valor_RJ = faturamento["RJ"]
valor_MG = faturamento["MG"]
valor_ES = faturamento["ES"]
valor_OU = faturamento["OU"]

# Imprime na tela o valor total de faturamento e a porcentagem de cada estado
print ("O valor total de faturamento é: R$ {:.2f}".format(total))
print ("As porcentagens do faturamento de cada estado são:")
for estado, valor in faturamento.items():
    porcentagem = (valor / total) * 100
    print(f"{estado}: {porcentagem:.2f}%")


