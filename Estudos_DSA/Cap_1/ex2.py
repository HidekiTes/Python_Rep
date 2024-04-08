# Crie uma lista com os números entre 1 a 100
numeros = list(range(1,101)) # o 101 é um número exclusivo

# Percorre a lista e verifica se o número é par e divisível por 4
for numero in numeros:
    if numero % 2 == 0 and numero % 4 == 0:
        print(numero)