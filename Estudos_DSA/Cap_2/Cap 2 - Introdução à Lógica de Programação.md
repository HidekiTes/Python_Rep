Uma introdução à lógica de programação é essencial para quem deseja ingressar no mundo da computação. Ela proporciona os fundamentos necessários para entender como os programas funcionam e como resolver problemas de forma algorítmica. Este texto oferece uma visão inicial sobre os princípios básicos da lógica de programação, começando com a compreensão de algoritmos simples e estruturas de controle, como loops e condicionais.
# Exercício 1 - Pseudocódigo: Calcular Área do Paralelogramo

Escreva um pseudocódigo para calcular a área de um paralelogramo. O algoritmo deve receber como entrada a base e a altura do paralelogramo. Em seguida, ele deve multiplicar a base pela altura e armazenar o resultado em uma variável denominada "área". Por fim, o algoritmo deve exibir a área calculada. Certifique-se de incluir comentários explicativos ao longo do código para facilitar a compreensão do algoritmo.
## Solução em Pseudocódigo

1. Início
2. Definir as variáveis `base` e `altura` do paralelogramo
3. Solicitar ao usuário que forneça o valor da base do paralelogramo
4. Ler e armazenar o valor da base em uma variável chamada `base`
5. Solicitar ao usuário que forneça o valor da altura do paralelogramo
6. Ler e armazenar o valor da altura em uma variável chamada `altura`
7. Calcular a área do paralelogramo utilizando a fórmula: `área = base * altura`
8. Armazenar o resultado do cálculo em uma variável chamada `area_paralelogramo`
9. Exibir o valor da área do paralelogramo para o usuário
10. Fim
## Solução em Python

``` python
print("Bem-vindo ao calculador de área de paralelogramo")
base = float(input("Insira o comprimento da base: "))
altura = float(input("Insira a altura: "))
area = base * altura
print("A area do paralelogramo é:",area)
```
# Exercício 2 - Pseudocódigo: Lógica de uma calculadora

Desenvolva a lógica para uma calculadora simples. Esta calculadora deve ser capaz de realizar operações básicas de adição, subtração, multiplicação e divisão. O algoritmo deve começar por receber a entrada do usuário, que consiste em dois números e o operador a ser aplicado entre eles.
## Solução em Pseudocódigo

1. Início
2. Exiba "Bem-vindo a calculadora"
3. Peça para o usuário inserir o primeiro número
4. Armazene o primeiro número
5. Peça para o usuário inserir o segundo número
6. Armazene o segundo número
7. Peça para o usuário selecionar uma operação ``(+,-,*,/)``
8. Armazene a operação em uma variável
9. Utilize a operação selecionada e os números armazenados para realizar o cálculo
10. Exiba o resultado
## Solução em Pyhton

``` python
print("Bem-vindo a calculadora")
num1 = float(input("Insira o primeiro número: "))
num2 = float(input("Insira o segundo número: "))
operacao = input("Selecione uma operação (+,-,*,/): ")

if operacao == "+":
    resultado = num1 + num2
    print("O resultado é: ", resultado)

elif operacao == "-":
    resultado = num1 - num2
    print("O resultado é: ", resultado)

elif operacao == "*":
    resultado = num1 * num2
    print("O resultado é: ", resultado)

elif operacao == "/":
    resultado = num1 / num2
    print("O resultado é: ", resultado)

else:
    print("Operação inválida")
```
# Exercicio 3 - Pseudocódigo: Algoritmo Bubble Sort

Bubble Sort é um algoritmo de ordenação simples que funciona comparando cada elemento com o próximo, e trocando-os de lugar se eles estiverem em ordem incorreta. O algoritmo repete esse processo várias vezes, até que todos os elementos estejam ordenados. A cada passagem, o maior elemento "flutua" para o final do array, como uma bolha, dando origem ao nome do algoritmo.

## Solução em Pseudocódigo

1. Para cada elemento i no array de tamanho n
2. Para cada elemento j no array de tamanho n - 1
3. Se elemento i for maior que elemento j
4. Troque os elementos i e j
5. Exiba o array ordenado
## Solução em Python

``` python
lista = [6,8,5,4,1,41,85,3,410,63,4106,40,14,16,38,56,44,165,84,632]

def bubble_sort(arr):

    n = len(arr)

    # Para cada elemento i do array
    for i in range(n):
        # Para cada elemento j do array
        for j in range(0, n-i-1):
            # Se elemento i for maior que elemento j 
            if arr[j] > arr[j+1]:
                #Troque os elementos i e j
                arr[j], arr[j+1] = arr[j+1], arr[j]

    return arr

print (bubble_sort(lista))

lista2 = [60,80,50,4,1,41,85,3,410,63,4106,40,14,16,38,56,44,165,84,632]
print (bubble_sort(lista2))
```