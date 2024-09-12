def is_fibo (number):
     # Função auxiliar para verificar se o número é um quadrado perfeito
    def is_perfect (y):
        x = int (y ** 0.5)
        # Return booleano
        return x*x == y
    return is_perfect (5 * number * number + 4) or is_perfect (5 * number * number - 4)

# Entrada do usuário
number = int(input("Informe um número: "))

# Verifica se o número inserido pertence à sequência Fibonacci
if is_fibo (number):
    print(f"O número {number} pertence à sequência Fibonacci.")
else:
    print(f"O número {number} não pertence à sequência Fibonacci.")