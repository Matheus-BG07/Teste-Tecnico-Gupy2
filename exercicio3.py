faturamento_diario = [150, 235, 1234, 1512, 1646, 125, 50, 555, 345, 333, 274, 234, 635, 512, 523, 150, 235, 1234, 1512, 1646, 125, 50, 555, 345, 333, 274, 234, 635, 512, 523]
menor_valor = min(faturamento_diario)
maior_valor = max(faturamento_diario)
media_mensal = int(sum(faturamento_diario) / len(faturamento_diario))
dias_acima_media = sum(1 for f in faturamento_diario if f > media_mensal)
print (f"O menor valor é: {menor_valor}")
print (f"O maior valor é: {maior_valor}")
print (f"A média diária de faturamento é: {media_mensal}")
print (f"A quantidade de dias com venda acima da média é: {dias_acima_media}")
