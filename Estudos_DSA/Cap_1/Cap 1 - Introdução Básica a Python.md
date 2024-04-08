Uma introdução básica a Python oferece uma entrada amigável ao vasto mundo da programação. Python é uma linguagem de programação popular, conhecida por sua sintaxe simples e legibilidade, tornando-a uma escolha ideal para iniciantes. Este texto aborda os conceitos fundamentais de Python, começando com a tradicional impressão de "Olá Mundo", um marco inicial para muitos programadores.
 
Print "Olá Mundo
``` python
print('Olá mundo')
```

Crie uma lista com os números que sejam pares e divisíveis por 4 e que sejam pares
``` python
# Crie uma lista com os números entre 1 a 100
numeros = list(range(1,101)) # o 101 é um número exclusivo

# Percorre a lista e verifica se o número é par e divisível por 4
for numero in numeros:
    if numero % 2 == 0 and numero % 4 == 0:
        print(numero)
```

Gere código Python que crie uma lista com os números entre 1 e 100 e então imprima os números pares, mas somente se o número for divisível por 4, usando list comprehension
``` python
# Criação da lista com números entre 1 e 100
numeros = list(range(1, 101))

# List comprehension para filtrar os números pares divisíveis por 4
numeros_pares_divisiveis_por_4 = [num for num in numeros if num % 2 == 0 and num % 4 == 0]

# Impressão dos números pares divisíveis por 4
print(numeros_pares_divisiveis_por_4)
```
