import xml.etree.ElementTree as ET

def carregar_faturamento_xml():
    # Parse do arquivo XML
    tree = ET.parse("valores.xml")
    root = tree.getroot()

    # Inicia a lista para armazenar os valores de faturamento
    faturamento_diario = []
    
    # Itera sobre os elementos 'dia' e extrai o atributo 'valor'
    for dia in root.findall("dia"):
        valor = int(dia.get("valor"))  
        if valor > 0:
            faturamento_diario.append(valor)
    
    return faturamento_diario
# Carrega os valores de faturamento
faturamento_diario = carregar_faturamento_xml()
# Calcula os valores
menor_valor = min(faturamento_diario)
maior_valor = max(faturamento_diario)
media_mensal = int(sum(faturamento_diario) / len(faturamento_diario))
dias_acima_media = sum(1 for f in faturamento_diario if f > media_mensal)
# Exibe os resultados
print (f"O menor valor é: {menor_valor}")
print (f"O maior valor é: {maior_valor}")
print (f"A média diária de faturamento é: {media_mensal}")
print (f"A quantidade de dias com venda acima da média é: {dias_acima_media}")
