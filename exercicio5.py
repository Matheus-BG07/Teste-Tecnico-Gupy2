def inverter_string(s):
    # Cria uma nova string vazia para armazenar o resultado
    invertida = ''
    
    # Percorre a string original de trás para frente
    for i in range(len(s) - 1, -1, -1):
        invertida += s[i]
    
    return invertida

# Entrada do usuário
entrada = input("Informe a string que deseja inverter: ")

# Inverte a string e exibe o resultado
resultado = inverter_string(entrada)
print("String invertida:", resultado)
