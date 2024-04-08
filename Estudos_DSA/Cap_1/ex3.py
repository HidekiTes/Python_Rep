# Criação da lista com números entre 1 e 100
numeros = list(range(1, 101))

# List comprehension para filtrar os números pares divisíveis por 4
numeros_pares_divisiveis_por_4 = [num for num in numeros if num % 2 == 0 and num % 4 == 0]

# Impressão dos números pares divisíveis por 4
print(numeros_pares_divisiveis_por_4)